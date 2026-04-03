"""
KidsCode Main Application

Sets up the root Tk window, initialises all services, and routes between screens.
"""
import tkinter as tk
from tkinter import ttk
import sys
import os


# ── App-level colour palette ────────────────────────────────────────────────
PALETTE = {
    'bg_dark':    '#0d0d1a',
    'bg_mid':     '#1a1a2e',
    'bg_card':    '#16213e',
    'accent':     '#e94560',
    'text_main':  '#eaeaea',
    'text_dim':   '#888',
    'white':      '#ffffff',
    'green':      '#4ade80',
    'yellow':     '#fbbf24',
    'blue':       '#60a5fa',
    'purple':     '#c084fc',
}

# Profile-specific accents
PROFILE_COLORS = {
    'joshua': {
        'primary':    '#FF6B6B',
        'secondary':  '#FFD93D',
        'bg':         '#1a1a2e',
        'card':       '#16213e',
        'text':       '#FFFFFF',
        'font_family':'Comic Sans MS',
        'font_size':  16,
        'btn_size':   18,
    },
    'toby': {
        'primary':    '#00B4D8',
        'secondary':  '#7B2FBE',
        'bg':         '#0d0d1a',
        'card':       '#16213e',
        'text':       '#eaeaea',
        'font_family':'Segoe UI',
        'font_size':  13,
        'btn_size':   13,
    },
}


class KidsCodeApp:
    """Main application controller."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("KidsCode 🚀")
        self.root.geometry("1280x800")
        self.root.configure(bg=PALETTE['bg_dark'])
        self.root.resizable(True, True)
        self._center_window(1280, 800)

        # Application state
        self.current_profile: str = 'toby'   # 'toby' or 'joshua'
        self.current_lesson_id: str = None
        self._screen_stack = []

        # Initialise services
        self._init_audio()
        self._init_progress()
        self._init_curriculum()
        self._setup_styles()

        # Build screens (each is a Frame; only one is visible at a time)
        self._screens: dict[str, tk.Frame] = {}
        self._current_frame: tk.Frame = None
        self._build_screens()

        # Wire window close
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

        # Show splash → profile select
        self.show_screen('profile_select')
        self.audio.speak(
            "Welcome to Kids Code! The coding adventure for Toby and Joshua. "
            "Who is coding today?",
            profile='default',
            clear_queue=True,
        )

    # ------------------------------------------------------------------
    # Initialisation helpers
    # ------------------------------------------------------------------

    def _center_window(self, w: int, h: int):
        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    def _init_audio(self):
        try:
            from kidscode.audio_engine import AudioEngine
            self.audio = AudioEngine()
        except Exception as e:
            print(f"Audio engine failed to start: {e}")
            self.audio = _NullAudio()

    def _init_progress(self):
        from kidscode.progress_tracker import ProgressTracker
        self.progress = ProgressTracker()

    def _init_curriculum(self):
        from kidscode.curriculum.curriculum_manager import CurriculumManager
        self.curriculum = CurriculumManager()

    def _setup_styles(self):
        style = ttk.Style(self.root)
        try:
            style.theme_use('clam')
        except Exception:
            pass

        style.configure('TFrame', background=PALETTE['bg_dark'])
        style.configure('Card.TFrame', background=PALETTE['bg_card'])
        style.configure(
            'TButton',
            background=PALETTE['accent'],
            foreground='white',
            font=('Segoe UI', 12, 'bold'),
            borderwidth=0,
            relief='flat',
            padding=(12, 8),
        )
        style.map('TButton',
                  background=[('active', '#c73652'), ('pressed', '#a02a41')])
        style.configure('TLabel',
                        background=PALETTE['bg_dark'],
                        foreground=PALETTE['text_main'],
                        font=('Segoe UI', 12))
        style.configure('TProgressbar',
                        troughcolor=PALETTE['bg_mid'],
                        background=PALETTE['green'],
                        thickness=8)

    def _build_screens(self):
        from kidscode.ui.profile_screen import ProfileScreen
        from kidscode.ui.home_screen import HomeScreen
        from kidscode.ui.lesson_viewer import LessonViewer

        container = tk.Frame(self.root, bg=PALETTE['bg_dark'])
        container.pack(fill='both', expand=True)
        self._container = container

        for name, cls in [
            ('profile_select', ProfileScreen),
            ('home', HomeScreen),
            ('lesson', LessonViewer),
        ]:
            frame = cls(container, self)
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
            frame.lower()  # hide
            self._screens[name] = frame

    # ------------------------------------------------------------------
    # Screen routing
    # ------------------------------------------------------------------

    def show_screen(self, name: str, **kwargs):
        """Raise a named screen to the front, calling prepare() if available."""
        if name not in self._screens:
            print(f"Unknown screen: {name}")
            return

        # Hide current
        if self._current_frame:
            self._current_frame.lower()

        frame = self._screens[name]
        if hasattr(frame, 'prepare'):
            frame.prepare(**kwargs)

        frame.lift()
        self._current_frame = frame
        self._screen_stack.append(name)

    def go_back(self):
        if len(self._screen_stack) > 1:
            self._screen_stack.pop()
            self.show_screen(self._screen_stack[-1])
        else:
            self.show_screen('profile_select')

    # ------------------------------------------------------------------
    # Entry point
    # ------------------------------------------------------------------

    def run(self):
        self.root.mainloop()

    def _on_close(self):
        try:
            self.audio.stop()
        except Exception:
            pass
        self.root.destroy()


# ---------------------------------------------------------------------------
# Fallback audio object if pyttsx3 / pygame fail completely
# ---------------------------------------------------------------------------

class _NullAudio:
    def speak(self, *a, **kw):
        pass

    def play(self, *a, **kw):
        pass

    def set_profile(self, *a, **kw):
        pass

    def set_enabled(self, *a, **kw):
        pass

    def stop(self):
        pass

    def clear_queue(self, *a, **kw):
        pass
