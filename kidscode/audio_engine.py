"""
Audio Engine - Text-to-Speech and Sound Effects

Uses pyttsx3 for offline TTS (Windows SAPI5) and winsound/pygame for effects.

TTS design note
---------------
pyttsx3 on Windows SAPI5 has a well-known threading issue: after the first
`runAndWait()` completes, the internal COM event loop is in a finished state
and silent hangs occur on subsequent calls if you reuse the same engine object
across calls.  The reliable fix is to create a **fresh engine instance** for
every speech item.  This is slightly less efficient but 100% reliable.
"""
import threading
import queue

# Profile voice settings  (profile key = lowercase profile name)
PROFILE_VOICE_SETTINGS = {
    'joshua': {
        'rate': 135,
        'volume': 1.0,
        'voice_preference': ['zira', 'hazel', 'female'],
    },
    'toby': {
        'rate': 165,
        'volume': 0.95,
        'voice_preference': ['david', 'george', 'male'],
    },
    'default': {
        'rate': 150,
        'volume': 1.0,
        'voice_preference': [],
    },
}


class AudioEngine:
    """Manages TTS voice narration and sound effects."""

    def __init__(self):
        self._tts_queue = queue.Queue()
        self._current_profile = 'default'
        self._enabled = True
        self._voice_cache: dict = {}   # profile -> voice_id (populated lazily)
        self._voices_scanned = False

        # Sound effects
        self._sounds_ready = False
        self._sounds = {}
        self._sound_backend = 'none'

        # Start the TTS worker thread
        self._tts_thread = threading.Thread(target=self._tts_worker, daemon=True)
        self._tts_thread.start()

        # Initialise sound effects (non-blocking)
        threading.Thread(target=self._init_sounds, daemon=True).start()

    # ------------------------------------------------------------------
    # TTS public API
    # ------------------------------------------------------------------

    def speak(self, text: str, profile: str = None, clear_queue: bool = False):
        """Queue a TTS utterance.  Pass clear_queue=True to drop pending items."""
        if not self._enabled or not text:
            return
        if clear_queue:
            self.clear_queue()
        profile = profile or self._current_profile
        # Normalise profile to lowercase so lookups always hit the dict
        self._tts_queue.put((str(text)[:600], profile.lower()))

    def clear_queue(self):
        """Drain all pending (not yet spoken) TTS items."""
        while not self._tts_queue.empty():
            try:
                self._tts_queue.get_nowait()
            except queue.Empty:
                break

    def set_profile(self, profile: str):
        self._current_profile = profile.lower()

    def set_enabled(self, enabled: bool):
        self._enabled = enabled
        if not enabled:
            self.clear_queue()

    def stop(self):
        """Signal the worker thread to shut down."""
        self.clear_queue()
        self._tts_queue.put(None)

    # ------------------------------------------------------------------
    # TTS worker — fresh engine per item fixes SAPI5 threading hang
    # ------------------------------------------------------------------

    def _tts_worker(self):
        """
        Background thread.
        KEY FIX: a brand-new pyttsx3 engine is created for every item.
        This avoids the SAPI5 COM event-loop issue where runAndWait()
        silently stops working after the first call on a reused engine.
        """
        # Scan available voices once so we can choose the right one quickly
        self._scan_voices()

        while True:
            try:
                item = self._tts_queue.get(timeout=0.5)
            except queue.Empty:
                continue

            if item is None:
                break  # shutdown signal

            text, profile = item
            if self._enabled and text:
                self._speak_item(text, profile)

    def _scan_voices(self):
        """Enumerate SAPI voices once and cache preferred IDs per profile."""
        try:
            import pyttsx3
            engine = pyttsx3.init()
            voices = engine.getProperty('voices') or []
            # engine.stop() avoids leaving the COM loop in a started state
            try:
                engine.stop()
            except Exception:
                pass

            for prof, settings in PROFILE_VOICE_SETTINGS.items():
                for pref in settings.get('voice_preference', []):
                    for v in voices:
                        if (pref in (v.name or '').lower() or
                                pref in (v.id or '').lower()):
                            self._voice_cache[prof] = v.id
                            break
                    if prof in self._voice_cache:
                        break

            self._voices_scanned = True
        except Exception as e:
            print(f"[TTS] Voice scan failed: {e}")

    def _speak_item(self, text: str, profile: str):
        """
        Speak one item using a fresh engine instance.
        Creating a new engine each time is the standard fix for the SAPI5
        threading bug in pyttsx3 on Windows.
        """
        try:
            import pyttsx3
            engine = pyttsx3.init()

            settings = PROFILE_VOICE_SETTINGS.get(profile,
                        PROFILE_VOICE_SETTINGS['default'])
            engine.setProperty('rate',   settings['rate'])
            engine.setProperty('volume', settings['volume'])

            voice_id = self._voice_cache.get(profile)
            if voice_id:
                engine.setProperty('voice', voice_id)

            engine.say(text)
            engine.runAndWait()

            # Explicit stop keeps the COM object tidy before GC collects it
            try:
                engine.stop()
            except Exception:
                pass

        except Exception as e:
            print(f"[TTS] Speak error: {e}")

    # ------------------------------------------------------------------
    # Sound Effects  (winsound primary, pygame optional fallback)
    # ------------------------------------------------------------------

    _WINSOUND_BEEPS = {
        'correct': (880, 150),
        'wrong':   (220, 250),
        'click':   (660,  70),
    }
    _STAR_FANFARE  = [(523, 100), (659, 100), (784, 100), (1047, 200)]
    _START_FANFARE = [(523, 80),  (659, 80),  (784, 150)]

    def _init_sounds(self):
        """Prefer pygame; fall back to winsound."""
        try:
            import pygame
            pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)
            self._sounds['correct'] = self._tone_pygame(880, 0.15)
            self._sounds['wrong']   = self._tone_pygame(220, 0.25)
            self._sounds['star']    = self._fanfare_pygame()
            self._sounds['click']   = self._tone_pygame(660, 0.07)
            self._sounds['start']   = self._fanfare_pygame([523, 659, 784])
            self._sound_backend = 'pygame'
            self._sounds_ready = True
            return
        except Exception:
            pass

        try:
            import winsound  # noqa – just check it's importable
            self._sound_backend = 'winsound'
            self._sounds_ready = True
        except ImportError:
            self._sound_backend = 'none'

    def _tone_pygame(self, freq: int, dur: float):
        import pygame, array, math
        sr, n = 44100, int(44100 * dur)
        buf = array.array('h', (
            int(32767 * (1 - i / n) * math.sin(2 * math.pi * freq * i / sr))
            for i in range(n)
        ))
        return pygame.mixer.Sound(buffer=bytes(buf))

    def _fanfare_pygame(self, notes=None):
        import pygame, array, math
        notes = notes or [523, 659, 784, 1047]
        sr, nd = 44100, int(44100 * 0.12)
        buf = array.array('h', [0] * nd * len(notes))
        for ni, freq in enumerate(notes):
            for i in range(nd):
                buf[ni * nd + i] = int(
                    32767 * (1 - i / nd * 0.5) *
                    math.sin(2 * math.pi * freq * i / sr)
                )
        return pygame.mixer.Sound(buffer=bytes(buf))

    def play(self, sound_name: str):
        """Play a named sound effect (non-blocking)."""
        if not self._sounds_ready:
            return
        if self._sound_backend == 'pygame':
            s = self._sounds.get(sound_name)
            if s:
                try:
                    s.play()
                except Exception:
                    pass
        elif self._sound_backend == 'winsound':
            threading.Thread(
                target=self._winsound_play,
                args=(sound_name,), daemon=True
            ).start()

    def _winsound_play(self, name: str):
        try:
            import winsound
            if name in ('star', 'start'):
                notes = self._STAR_FANFARE if name == 'star' else self._START_FANFARE
                for f, d in notes:
                    winsound.Beep(f, d)
            else:
                beep = self._WINSOUND_BEEPS.get(name)
                if beep:
                    winsound.Beep(*beep)
        except Exception:
            pass

