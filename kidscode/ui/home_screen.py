"""
Home Screen — per-profile module selection dashboard.

Joshua (5):  Large colourful module cards with star progress.
Toby   (10): Module list with progress bars, XP level, and badges.
"""
import tkinter as tk
from tkinter import ttk
from typing import List, Dict


class HomeScreen(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg='#0d0d1a')
        self.app = app
        self._profile = 'toby'

    def prepare(self, profile: str = 'toby', **kwargs):
        self._profile = profile
        # Rebuild the screen for this profile
        for w in self.winfo_children():
            w.destroy()
        if profile == 'joshua':
            self._build_joshua()
        else:
            self._build_toby()

    # ================================================================
    # JOSHUA HOME
    # ================================================================

    def _build_joshua(self):
        pc = {
            'primary': '#FF6B6B', 'secondary': '#FFD93D',
            'bg': '#0f0f20', 'card': '#1a1a35',
            'text': '#FFFFFF', 'font': 'Comic Sans MS',
        }
        self.configure(bg=pc['bg'])

        # ── Header ──────────────────────────────────────────────────
        header = tk.Frame(self, bg=pc['primary'], padx=20, pady=14)
        header.pack(fill='x')

        tk.Label(
            header, text="🌟 Joshua's Code Adventure!", bg=pc['primary'],
            fg='white', font=('Comic Sans MS', 22, 'bold'),
        ).pack(side='left')

        stars = self.app.progress.get_stars('joshua')
        tk.Label(
            header,
            text=f"⭐ {stars} Stars",
            bg=pc['primary'], fg='white',
            font=('Comic Sans MS', 16, 'bold'),
        ).pack(side='left', padx=30)

        # Back button
        tk.Button(
            header, text="🏠 Go Back",
            bg='white', fg=pc['primary'],
            font=('Comic Sans MS', 13, 'bold'),
            relief='flat', bd=0, padx=12, pady=4, cursor='hand2',
            command=lambda: self.app.show_screen('profile_select'),
        ).pack(side='right')

        # Voice button
        tk.Button(
            header, text="🔊 Read to me",
            bg=pc['secondary'], fg='#333',
            font=('Comic Sans MS', 13, 'bold'),
            relief='flat', bd=0, padx=12, pady=4, cursor='hand2',
            command=self._joshua_read_aloud,
        ).pack(side='right', padx=8)

        # ── Badge row (shown when Joshua has earned badges) ──────────
        badges = self.app.progress.get_badges('joshua')
        if badges:
            badge_icons = {m.get('badge', ''): m.get('badge_icon', '🏅')
                           for m in self.app.curriculum.get_modules('joshua')}
            badge_bar = tk.Frame(self, bg=pc['primary'], padx=20, pady=6)
            badge_bar.pack(fill='x')
            tk.Label(
                badge_bar, text="🏅 My Badges!",
                bg=pc['primary'], fg='white',
                font=('Comic Sans MS', 14, 'bold'),
            ).pack(side='left')
            for b_name in badges[:6]:
                b_icon = badge_icons.get(b_name, '🏅')
                tk.Label(
                    badge_bar, text=f"{b_icon} {b_name}",
                    bg='#ff8888', fg='white',
                    font=('Comic Sans MS', 13, 'bold'), padx=8, pady=2,
                ).pack(side='left', padx=6)

        # ── Scrollable module cards ──────────────────────────────────
        canvas = tk.Canvas(self, bg=pc['bg'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')
        canvas.pack(fill='both', expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)

        inner = tk.Frame(canvas, bg=pc['bg'])
        cw = canvas.create_window((0, 0), window=inner, anchor='nw')

        def on_resize(e):
            canvas.itemconfig(cw, width=e.width)
        canvas.bind('<Configure>', on_resize)
        inner.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        # Bind scroll on canvas
        canvas.bind_all('<MouseWheel>', lambda e: canvas.yview_scroll(-1*(e.delta//120), 'units'))

        # ── Build module cards ───────────────────────────────────────
        modules = self.app.curriculum.get_modules('joshua')
        completed = self.app.progress.get_completed_lessons('joshua')

        for i, module in enumerate(modules):
            lesson_ids = [l['id'] for l in module.get('lessons', [])]
            done, total = self.app.progress.get_module_progress('joshua', lesson_ids)

            # Is module unlocked?
            prereq_ids = []
            for pm_id in module.get('prerequisite_modules', []):
                pm = self.app.curriculum.get_module_by_id('joshua', pm_id)
                if pm:
                    for l in pm.get('lessons', []):
                        prereq_ids.append(l['id'])
            unlocked = self.app.progress.is_module_unlocked('joshua', prereq_ids)

            self._joshua_module_card(inner, module, done, total, unlocked, completed)

    def _joshua_module_card(self, parent, module, done, total, unlocked, completed):
        color = module.get('color', '#FF6B6B')
        is_done = done >= total and total > 0

        card = tk.Frame(
            parent, bg='#1a1a35',
            relief='flat', bd=0,
            padx=0, pady=0,
        )
        card.pack(fill='x', padx=30, pady=12)

        # Left colour bar
        bar = tk.Frame(card, bg=color if unlocked else '#444', width=12)
        bar.pack(side='left', fill='y')

        body = tk.Frame(card, bg='#1a1a35', padx=20, pady=16)
        body.pack(side='left', fill='both', expand=True)

        # Icon + title
        head = tk.Frame(body, bg='#1a1a35')
        head.pack(fill='x')

        icon_text = module.get('icon', '📖')
        if not unlocked:
            icon_text = '🔒'
        elif is_done:
            icon_text = '✅'

        tk.Label(
            head, text=icon_text, bg='#1a1a35',
            font=('Segoe UI', 36),
        ).pack(side='left', padx=(0, 12))

        info = tk.Frame(head, bg='#1a1a35')
        info.pack(side='left', fill='both', expand=True)

        tk.Label(
            info, text=module['title'],
            bg='#1a1a35', fg='#ffffff',
            font=('Comic Sans MS', 18, 'bold'), anchor='w',
        ).pack(anchor='w')

        tk.Label(
            info, text=module.get('description', ''),
            bg='#1a1a35', fg='#aaaaaa',
            font=('Comic Sans MS', 15), anchor='w', wraplength=600, justify='left',
        ).pack(anchor='w')

        # "With a grown-up" banner for assisted modules
        if module.get('assisted') and unlocked:
            tk.Label(
                info, text='👨\u200d👩\u200d👦 Do this with a grown-up!',
                bg='#3a2a10', fg='#fbbf24',
                font=('Comic Sans MS', 13, 'bold'), anchor='w',
                padx=8, pady=2,
            ).pack(anchor='w', pady=(4, 0))

        # Stars progress
        if total > 0:
            stars_earned = '⭐' * done + '☆' * (total - done)
            tk.Label(
                body, text=stars_earned,
                bg='#1a1a35', fg=color,
                font=('Segoe UI', 18),
                anchor='w',
            ).pack(anchor='w', pady=(6, 0))

        # Action button
        btn_frame = tk.Frame(card, bg='#1a1a35', padx=16, pady=16)
        btn_frame.pack(side='right')

        if not unlocked:
            tk.Label(
                btn_frame, text='🔒\nDo the one\nabove first!',
                bg='#1a1a35', fg='#aaaaaa',
                font=('Comic Sans MS', 14, 'bold'), justify='center',
            ).pack()
        else:
            # Find first incomplete lesson
            first_lesson = None
            for lesson in module.get('lessons', []):
                if lesson['id'] not in completed:
                    first_lesson = lesson
                    break
            if first_lesson is None and module.get('lessons'):
                first_lesson = module['lessons'][0]  # revisit first

            label = '▶ Start!' if done == 0 else ('⭐ Do Again!' if is_done else '▶ Continue')
            btn = tk.Button(
                btn_frame,
                text=label,
                bg=color, fg='white',
                font=('Comic Sans MS', 16, 'bold'),
                relief='flat', bd=0,
                padx=20, pady=10,
                cursor='hand2',
                command=lambda lid=first_lesson['id']: self._open_lesson(lid),
            )
            btn.pack()

    def _joshua_read_aloud(self):
        self.app.audio.speak(
            "Here are your modules! Each module has fun coding lessons. "
            "Complete them in order to unlock new ones. "
            "Click on a module to start learning!",
            profile='joshua', clear_queue=True,
        )

    # ================================================================
    # TOBY HOME
    # ================================================================

    def _build_toby(self):
        self.configure(bg='#0d0d1a')

        # ── Header ──────────────────────────────────────────────────
        header = tk.Frame(self, bg='#00B4D8', padx=20, pady=12)
        header.pack(fill='x')

        xp = self.app.progress.get_xp('toby')
        level = self.app.progress.get_level('toby')
        level_xp, level_needed = self.app.progress.get_xp_to_next_level('toby')
        streak = self.app.progress.get_streak('toby')

        tk.Label(
            header, text="⚡ Toby's Code Academy",
            bg='#00B4D8', fg='white',
            font=('Segoe UI', 20, 'bold'),
        ).pack(side='left')

        stats = tk.Frame(header, bg='#00B4D8')
        stats.pack(side='left', padx=30)

        if streak >= 7:
            streak_text = f"  🔥 {streak}-day streak! 🏆"
        elif streak >= 2:
            streak_text = f"  🔥 {streak}-day streak!"
        elif streak == 1:
            streak_text = f"  🔥 Day 1 — come back tomorrow!"
        else:
            streak_text = ""
        tk.Label(
            stats,
            text=f"🏆 Level {level}   •   ⭐ {xp} XP{streak_text}",
            bg='#00B4D8', fg='white',
            font=('Segoe UI', 13, 'bold'),
        ).pack(side='left')

        # XP progress bar
        xp_bar = tk.Frame(stats, bg='#00B4D8')
        xp_bar.pack(side='left', padx=(16, 0))
        tk.Label(xp_bar, text=f"{level_xp}/{level_needed} XP to Level {level+1}",
                 bg='#00B4D8', fg='#d0f0ff', font=('Segoe UI', 10)).pack(anchor='w')
        bar_bg = tk.Frame(xp_bar, bg='#0090ae', height=8, width=160)
        bar_bg.pack_propagate(False)
        bar_bg.pack(anchor='w')
        fill_w = max(4, int(160 * level_xp / level_needed))
        tk.Frame(bar_bg, bg='#fbbf24', height=8, width=fill_w).place(x=0, y=0)

        tk.Button(
            header, text="← Dashboard",
            bg='white', fg='#00B4D8',
            font=('Segoe UI', 11, 'bold'),
            relief='flat', bd=0, padx=10, pady=4, cursor='hand2',
            command=lambda: self.app.show_screen('profile_select'),
        ).pack(side='right')

        # ── Scrollable content ───────────────────────────────────────
        canvas = tk.Canvas(self, bg='#0d0d1a', highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')
        canvas.pack(fill='both', expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)

        inner = tk.Frame(canvas, bg='#0d0d1a')
        cw = canvas.create_window((0, 0), window=inner, anchor='nw')

        def on_resize(e):
            canvas.itemconfig(cw, width=e.width)
        canvas.bind('<Configure>', on_resize)
        inner.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.bind_all('<MouseWheel>', lambda e: canvas.yview_scroll(-1*(e.delta//120), 'units'))

        # ── Badges ───────────────────────────────────────────────────
        badges = self.app.progress.get_badges('toby')
        if badges:
            # Build a lookup of badge_name -> badge_icon from curriculum
            badge_icons = {}
            for m in self.app.curriculum.get_modules('toby'):
                badge_icons[m.get('badge', '')] = m.get('badge_icon', '🏅')

            badge_sec = tk.Frame(inner, bg='#0d0d1a')
            badge_sec.pack(fill='x', padx=30, pady=(16, 4))
            tk.Label(
                badge_sec, text="🏅 Your Badges",
                bg='#0d0d1a', fg='#fbbf24',
                font=('Segoe UI', 14, 'bold'),
            ).pack(anchor='w')
            badge_row = tk.Frame(badge_sec, bg='#0d0d1a')
            badge_row.pack(anchor='w', pady=6)
            for b in badges[:8]:
                icon = badge_icons.get(b, '🏅')
                tk.Label(
                    badge_row, text=f"{icon} {b}", bg='#16213e', fg='white',
                    font=('Segoe UI', 11), padx=10, pady=4, relief='flat',
                ).pack(side='left', padx=4)

        # ── Overall progress summary ─────────────────────────────────
        all_modules = self.app.curriculum.get_modules('toby')
        modules_done = sum(
            1 for m in all_modules
            if self.app.progress.get_module_progress(
                'toby', [l['id'] for l in m.get('lessons', [])]
            )[0] > 0 and
            self.app.progress.get_module_progress(
                'toby', [l['id'] for l in m.get('lessons', [])]
            )[0] >= self.app.progress.get_module_progress(
                'toby', [l['id'] for l in m.get('lessons', [])]
            )[1]
        )
        summary_frame = tk.Frame(inner, bg='#0d0d1a')
        summary_frame.pack(fill='x', padx=30, pady=(8, 0))
        tk.Label(
            summary_frame,
            text=f"🗺️  {modules_done} of {len(all_modules)} modules complete",
            bg='#0d0d1a', fg='#555',
            font=('Segoe UI', 11),
        ).pack(side='left')

        # ── Module rows label ─────────────────────────────────────────
        tk.Label(
            inner, text="📚 Learning Modules",
            bg='#0d0d1a', fg='#eaeaea',
            font=('Segoe UI', 16, 'bold'),
        ).pack(anchor='w', padx=30, pady=(16, 4))

        modules = self.app.curriculum.get_modules('toby')
        completed = self.app.progress.get_completed_lessons('toby')

        for module in modules:
            lesson_ids = [l['id'] for l in module.get('lessons', [])]
            done, total = self.app.progress.get_module_progress('toby', lesson_ids)

            prereq_ids = []
            for pm_id in module.get('prerequisite_modules', []):
                pm = self.app.curriculum.get_module_by_id('toby', pm_id)
                if pm:
                    for l in pm.get('lessons', []):
                        prereq_ids.append(l['id'])
            unlocked = self.app.progress.is_module_unlocked('toby', prereq_ids)

            self._toby_module_row(inner, module, done, total, unlocked, completed)

    def _toby_module_row(self, parent, module, done, total, unlocked, completed):
        color = module.get('color', '#00B4D8')
        is_done = done >= total and total > 0
        pct = int(100 * done / total) if total > 0 else 0

        row = tk.Frame(parent, bg='#16213e', padx=0, pady=0)
        row.pack(fill='x', padx=30, pady=6)

        # Hover feedback for Toby's module rows
        def _row_hover_on(e):
            try:
                row.configure(bg='#1e2d4a')
                body.configure(bg='#1e2d4a')
            except Exception:
                pass

        def _row_hover_off(e):
            try:
                row.configure(bg='#16213e')
                body.configure(bg='#16213e')
            except Exception:
                pass

        # Left accent stripe
        tk.Frame(row, bg=color if unlocked else '#333', width=6).pack(side='left', fill='y')

        body = tk.Frame(row, bg='#16213e', padx=16, pady=12)
        body.pack(side='left', fill='both', expand=True)

        # Top row: icon + title + % badge
        top = tk.Frame(body, bg='#16213e')
        top.pack(fill='x')

        icon_text = module.get('icon', '📖')
        if not unlocked:
            icon_text = '🔒'
        elif is_done:
            icon_text = '✅'

        tk.Label(
            top, text=icon_text, bg='#16213e',
            font=('Segoe UI', 22),
        ).pack(side='left', padx=(0, 10))

        title_area = tk.Frame(top, bg='#16213e')
        title_area.pack(side='left', fill='both', expand=True)

        tk.Label(
            title_area, text=module['title'],
            bg='#16213e', fg='#ffffff' if unlocked else '#555',
            font=('Segoe UI', 14, 'bold'), anchor='w',
        ).pack(anchor='w')

        tk.Label(
            title_area, text=module.get('description', ''),
            bg='#16213e', fg='#777' if not unlocked else '#aaa',
            font=('Segoe UI', 11), anchor='w', wraplength=650, justify='left',
        ).pack(anchor='w')

        # Progress bar
        if total > 0 and unlocked:
            pb_frame = tk.Frame(body, bg='#16213e')
            pb_frame.pack(fill='x', pady=(8, 0))
            tk.Label(
                pb_frame, text=f"{done}/{total} lessons  ({pct}%)",
                bg='#16213e', fg='#666',
                font=('Segoe UI', 10),
            ).pack(side='right')
            bar_bg = tk.Frame(pb_frame, bg='#0d0d1a', height=6)
            bar_bg.pack(fill='x', side='left', expand=True, pady=3, padx=(0, 8))
            fill_w_rel = pct / 100
            bar_bg.update_idletasks()
            # Use a frame that fills based on proportion
            fill_frame = tk.Frame(bar_bg, bg=color if pct < 100 else '#4ade80', height=6)
            fill_frame.place(relx=0, rely=0, relwidth=fill_w_rel, relheight=1)

        # Action button area
        btn_frame = tk.Frame(row, bg='#16213e', padx=16)
        btn_frame.pack(side='right', fill='y')

        if not unlocked:
            # Find the first incomplete prerequisite module name
            prereq_text = 'Complete previous modules'
            for pm_id in module.get('prerequisite_modules', []):
                pm = self.app.curriculum.get_module_by_id('toby', pm_id)
                if pm:
                    pm_lessons = [l['id'] for l in pm.get('lessons', [])]
                    done, total = self.app.progress.get_module_progress('toby', pm_lessons)
                    if done < total:
                        prereq_text = f"Finish '{pm['title'].split(' ')[0]}…' first"
                        break
            tk.Label(
                btn_frame, text=f'🔒\n{prereq_text}',
                bg='#16213e', fg='#555',
                font=('Segoe UI', 10), justify='center',
            ).pack(expand=True)
        else:
            first_lesson = None
            for lesson in module.get('lessons', []):
                if lesson['id'] not in completed:
                    first_lesson = lesson
                    break
            if first_lesson is None and module.get('lessons'):
                first_lesson = module['lessons'][0]

            label = 'Start →' if done == 0 else ('Revisit' if is_done else 'Continue →')
            fg_color = color

            btn = tk.Button(
                btn_frame,
                text=label,
                bg='#0d0d1a', fg=fg_color,
                activebackground='#16213e', activeforeground=fg_color,
                font=('Segoe UI', 13, 'bold'),
                relief='flat', bd=0,
                padx=14, pady=8,
                cursor='hand2',
                command=lambda lid=first_lesson['id']: self._open_lesson(lid),
            )
            btn.pack(expand=True)

        # Expandable lesson list (click row to toggle)
        if unlocked and len(module.get('lessons', [])) > 0:
            lessons_frame = tk.Frame(parent, bg='#0d1117')
            lessons_frame_visible = [False]

            def _toggle_lessons(e=None):
                if lessons_frame_visible[0]:
                    lessons_frame.pack_forget()
                    lessons_frame_visible[0] = False
                else:
                    # Pack right after the row
                    lessons_frame.pack(fill='x', padx=30, pady=(0, 2), after=row)
                    lessons_frame_visible[0] = True

            for widget in [row, body]:
                widget.bind('<Button-1>', _toggle_lessons)

            # Build lesson entries
            for lesson in module.get('lessons', []):
                lid = lesson['id']
                is_complete = lid in completed
                icon = '✅' if is_complete else '📖'
                fg = '#4ade80' if is_complete else '#ccc'

                l_row = tk.Frame(lessons_frame, bg='#0d1117', padx=24, pady=4, cursor='hand2')
                l_row.pack(fill='x')
                tk.Label(
                    l_row, text=f"  {icon}  {lesson.get('title', lid)}",
                    bg='#0d1117', fg=fg,
                    font=('Segoe UI', 11), anchor='w',
                ).pack(side='left')
                xp = lesson.get('xp', 0)
                if xp:
                    tk.Label(
                        l_row, text=f"+{xp} XP",
                        bg='#0d1117', fg='#666',
                        font=('Segoe UI', 9),
                    ).pack(side='right', padx=8)
                l_row.bind('<Button-1>', lambda e, _lid=lid: self._open_lesson(_lid))
                for child in l_row.winfo_children():
                    child.bind('<Button-1>', lambda e, _lid=lid: self._open_lesson(_lid))

        # Bind hover events to row and body
        for widget in [row, body]:
            widget.bind('<Enter>', _row_hover_on)
            widget.bind('<Leave>', _row_hover_off)

    # ================================================================
    # Shared
    # ================================================================

    def _open_lesson(self, lesson_id: str):
        self.app.current_lesson_id = lesson_id
        self.app.show_screen('lesson', lesson_id=lesson_id)
