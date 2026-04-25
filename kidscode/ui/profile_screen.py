"""
Profile Selection Screen — the first screen children see.
Big colourful cards for Joshua (age 5) and Toby (age 10).
"""
import tkinter as tk
from tkinter import font as tkfont


class ProfileScreen(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg='#0d0d1a')
        self.app = app
        self._build()

    def _build(self):
        # ── Stars / decorative background dots ────────────────────────
        self._canvas = tk.Canvas(self, bg='#0d0d1a', highlightthickness=0)
        self._canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        self._draw_stars()

        # ── Title ─────────────────────────────────────────────────────
        title_frame = tk.Frame(self, bg='#0d0d1a')
        title_frame.place(relx=0.5, rely=0.08, anchor='n')

        tk.Label(
            title_frame, text="🚀 KidsCode", bg='#0d0d1a', fg='#ffffff',
            font=('Segoe UI', 42, 'bold'),
        ).pack()
        tk.Label(
            title_frame,
            text="Your coding adventure starts here!",
            bg='#0d0d1a', fg='#cccccc',
            font=('Segoe UI', 16),
        ).pack(pady=(4, 0))

        # ── Profile cards ─────────────────────────────────────────────
        cards_frame = tk.Frame(self, bg='#0d0d1a')
        cards_frame.place(relx=0.5, rely=0.5, anchor='center')

        self._build_profile_card(
            cards_frame,
            profile='joshua',
            emoji='🌟',
            name='Joshua',
            age='Age 5',
            tagline='Coding Explorer',
            primary='#FF6B6B',
            secondary='#FFD93D',
            description=(
                "Start your adventure!\n"
                "Learn the magic of\n"
                "coding step by step!"
            ),
            side='left',
        )

        # Divider
        tk.Label(
            cards_frame, text="or", bg='#0d0d1a', fg='#555',
            font=('Segoe UI', 20), width=4,
        ).pack(side='left', padx=20)

        self._build_profile_card(
            cards_frame,
            profile='toby',
            emoji='⚡',
            name='Toby',
            age='Age 10',
            tagline='Code Developer',
            primary='#00B4D8',
            secondary='#7B2FBE',
            description=(
                "Level up your skills!\n"
                "Python, AI, Networking\n"
                "and Game Development!"
            ),
            side='left',
        )

        # ── Footer ────────────────────────────────────────────────────
        tk.Label(
            self,
            text="🔒  Safe sandbox  •  🔊  Voice narration  •  🏆  Achievements",
            bg='#0d0d1a', fg='#888888',
            font=('Segoe UI', 11),
        ).place(relx=0.5, rely=0.95, anchor='center')

    def _build_profile_card(self, parent, profile, emoji, name, age, tagline,
                             primary, secondary, description, side):
        """Build a large clickable profile card."""
        card = tk.Frame(
            parent, bg='#16213e', cursor='hand2',
            relief='flat', bd=0,
        )
        card.pack(side=side, padx=20)

        # Coloured top band
        band = tk.Frame(card, bg=primary, height=8)
        band.pack(fill='x')

        inner = tk.Frame(card, bg='#16213e', padx=40, pady=30)
        inner.pack()

        # Emoji avatar
        tk.Label(
            inner, text=emoji, bg='#16213e',
            font=('Segoe UI', 72),
        ).pack()

        # Name
        tk.Label(
            inner, text=name, bg='#16213e', fg='#ffffff',
            font=('Segoe UI', 32, 'bold'),
        ).pack(pady=(8, 0))

        # Age badge
        age_frame = tk.Frame(inner, bg=primary, padx=10, pady=4)
        age_frame.pack(pady=6)
        tk.Label(
            age_frame, text=age, bg=primary, fg='white',
            font=('Segoe UI', 13, 'bold'),
        ).pack()

        # Tagline
        tk.Label(
            inner, text=tagline, bg='#16213e', fg=secondary,
            font=('Segoe UI', 14, 'bold'),
        ).pack()

        # Description
        tk.Label(
            inner, text=description, bg='#16213e', fg='#dddddd',
            font=('Segoe UI', 12), justify='center',
        ).pack(pady=(12, 20))

        # Big START button
        btn_label = '▶  Start Coding!' if profile == 'joshua' else '▶  Enter Academy'
        btn_frame = tk.Frame(inner, bg=primary, cursor='hand2')
        btn_frame.pack(fill='x', ipady=8)
        tk.Label(
            btn_frame, text=btn_label,
            bg=primary, fg='white',
            font=('Segoe UI', 16, 'bold'), cursor='hand2',
        ).pack()

        # Bind click events to the whole card
        for widget in [card, inner, btn_frame] + list(inner.winfo_children()):
            try:
                widget.bind('<Button-1>', lambda e, p=profile: self._select_profile(p))
                widget.bind('<Enter>', lambda e, c=card, col=primary: self._hover(c, col))
                widget.bind('<Leave>', lambda e, c=card: self._unhover(c))
            except Exception:
                pass

        return card

    def _hover(self, card, color):
        """Highlight card on hover."""
        try:
            card.configure(bg=color)
        except Exception:
            pass

    def _unhover(self, card):
        try:
            card.configure(bg='#16213e')
        except Exception:
            pass

    def _select_profile(self, profile: str):
        # Prevent double-click
        if getattr(self, '_loading', False):
            return
        self._loading = True

        # Show loading overlay immediately (before any I/O)
        self._show_loading(profile)

        # Do the slow initialisation in a background thread
        import threading
        def _init_worker():
            self.app.current_profile = profile
            self.app.progress.start_session(profile)
            self.app.audio.set_profile(profile)

            if profile == 'joshua':
                sessions = self.app.progress._profile('joshua').get('sessions', 0)
                greeting = "Hi Joshua! Welcome to KidsCode!" if sessions <= 1 else "Hi Joshua! Welcome back!"
                self.app.audio.speak(
                    f"{greeting} Let's start coding! Choose a module to begin!",
                    profile='joshua', clear_queue=True,
                )
            else:
                sessions = self.app.progress._profile('toby').get('sessions', 0)
                greeting = "Hi Toby! Welcome to KidsCode!" if sessions <= 1 else "Welcome back Toby!"
                self.app.audio.speak(
                    f"{greeting} Let's code something awesome today!",
                    profile='toby', clear_queue=True,
                )

            self.app.audio.play('start')
            # Switch screen on main thread
            self.after(0, lambda: self._finish_loading(profile))

        threading.Thread(target=_init_worker, daemon=True).start()

    def _show_loading(self, profile):
        """Show an animated loading overlay with progress bar."""
        name = 'Joshua' if profile == 'joshua' else 'Toby'
        color = '#FF6B6B' if profile == 'joshua' else '#00B4D8'
        emoji = '🌟' if profile == 'joshua' else '⚡'

        self._loading_overlay = tk.Frame(self, bg='#0d0d1a')
        self._loading_overlay.place(relx=0, rely=0, relwidth=1, relheight=1)

        tk.Label(
            self._loading_overlay, text=f'{emoji}  Loading {name}\'s World...  {emoji}',
            bg='#0d0d1a', fg=color,
            font=('Segoe UI', 32, 'bold'),
        ).place(relx=0.5, rely=0.38, anchor='center')

        tk.Label(
            self._loading_overlay, text='Getting everything ready for you!',
            bg='#0d0d1a', fg='#cccccc',
            font=('Segoe UI', 16),
        ).place(relx=0.5, rely=0.46, anchor='center')

        # Animated progress bar
        bar_frame = tk.Frame(self._loading_overlay, bg='#1c2333', height=12)
        bar_frame.place(relx=0.25, rely=0.54, relwidth=0.5, height=12)

        self._loading_fill = tk.Frame(bar_frame, bg=color, height=12)
        self._loading_fill.place(relx=0, rely=0, relheight=1, relwidth=0)

        self._loading_progress = 0.0
        self._animate_loading(color)

    def _animate_loading(self, color):
        """Animate the loading bar with a smooth fill."""
        if not getattr(self, '_loading', False):
            return
        self._loading_progress = min(self._loading_progress + 0.04, 0.92)
        try:
            self._loading_fill.place_configure(relwidth=self._loading_progress)
        except tk.TclError:
            return
        self.after(50, lambda: self._animate_loading(color))

    def _finish_loading(self, profile):
        """Complete the loading bar and transition to home screen."""
        # Fill bar to 100%
        try:
            self._loading_fill.place_configure(relwidth=1.0)
        except (tk.TclError, AttributeError):
            pass

        # Brief pause at 100% so the child sees it complete
        def _go():
            self._loading = False
            try:
                self._loading_overlay.destroy()
            except (tk.TclError, AttributeError):
                pass
            self.app.show_screen('home', profile=profile)

        self.after(300, _go)

    def prepare(self, **kwargs):
        pass  # nothing to prepare for profile screen

    def _draw_stars(self):
        """Draw small decorative dots on the background canvas."""
        import random
        self.update_idletasks()
        w = self.winfo_width() or 1280
        h = self.winfo_height() or 800
        for _ in range(80):
            x = random.randint(0, w)
            y = random.randint(0, h)
            r = random.randint(1, 3)
            brightness = random.randint(40, 120)
            col = f'#{brightness:02x}{brightness:02x}{brightness + 20:02x}'
            self._canvas.create_oval(x-r, y-r, x+r, y+r, fill=col, outline='')
