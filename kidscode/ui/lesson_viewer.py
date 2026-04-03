"""
Lesson Viewer — renders lesson steps for both profiles.

Step types: story, teach, example, exercise, quiz
"""
import tkinter as tk
from tkinter import ttk, scrolledtext
import threading


# ── Profile-specific style dictionaries ─────────────────────────────────────
STYLES = {
    'joshua': {
        'bg':         '#0f0f20',
        'card_bg':    '#1a1a35',
        'primary':    '#FF6B6B',
        'secondary':  '#FFD93D',
        'text':       '#FFFFFF',
        'subtext':    '#aaaaaa',
        'font':       'Comic Sans MS',
        'font_size':  20,   # raised from 16 → 20pt (BBC Bitesize min for emergent readers)
        'title_size': 26,   # raised from 24 → 26pt
        'code_size':  16,   # raised from 14 → 16pt
    },
    'toby': {
        'bg':         '#0d0d1a',
        'card_bg':    '#16213e',
        'primary':    '#00B4D8',
        'secondary':  '#7B2FBE',
        'text':       '#eaeaea',
        'subtext':    '#888',
        'font':       'Segoe UI',
        'font_size':  13,
        'title_size': 18,
        'code_size':  14,   # raised from 12 → 14pt (BBC Bitesize/Trinket minimum)
    },
}


class LessonViewer(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg='#0d0d1a')
        self.app = app
        self._lesson = None
        self._steps = []
        self._step_idx = 0
        self._quiz_answer = None
        self._hint_idx = 0
        self._step_cache = {}  # lesson_id -> last step index (for back-navigation resume)

    # ================================================================
    # prepare() — called by app.show_screen('lesson', lesson_id=...)
    # ================================================================

    def prepare(self, lesson_id: str = None, **kwargs):
        if lesson_id is None:
            return
        lesson = self.app.curriculum.get_lesson(lesson_id)
        if lesson is None:
            return

        self._lesson = lesson
        self._steps = lesson.get('steps', [])
        # Restore step position from cache (so back-navigation resumes where left off)
        self._step_idx = self._step_cache.get(lesson_id, 0)
        self._quiz_answer = None
        self._hint_idx = 0

        profile = self.app.current_profile
        self._style = STYLES.get(profile, STYLES['toby'])
        self.configure(bg=self._style['bg'])

        # Destroy and rebuild UI
        for w in self.winfo_children():
            w.destroy()

        self._build_header(lesson, profile)
        self._content_area = tk.Frame(self, bg=self._style['bg'])
        self._content_area.pack(fill='both', expand=True, padx=0, pady=0)
        self._build_footer()
        self._show_step()

    # ------------------------------------------------------------------
    # Layout builders
    # ------------------------------------------------------------------

    def _build_header(self, lesson, profile):
        s = self._style
        header = tk.Frame(self, bg=s['primary'], padx=16, pady=10)
        header.pack(fill='x')

        # Back button
        tk.Button(
            header, text='← Back',
            bg='white', fg=s['primary'],
            font=(s['font'], 11, 'bold'),
            relief='flat', bd=0, padx=10, pady=4,
            cursor='hand2',
            command=self._go_home,
        ).pack(side='left')

        # Title
        title = f"{lesson.get('icon', '📖')}  {lesson['title']}"
        tk.Label(
            header, text=title,
            bg=s['primary'], fg='white',
            font=(s['font'], s['title_size'], 'bold'),
        ).pack(side='left', padx=20)

        # XP badge — for Toby show XP, for Joshua show star reward
        if self.app.current_profile == 'joshua':
            xp_text = '⭐ +1 Star when you finish!'
        else:
            xp_text = f"⭐ {lesson.get('xp', 50)} XP"
        tk.Label(
            header, text=xp_text,
            bg=s['secondary'], fg='#333',
            font=(s['font'], 12, 'bold'),
            padx=8, pady=4,
        ).pack(side='right')

        # Voice toggle
        self._voice_on = tk.BooleanVar(value=True)
        tk.Checkbutton(
            header, text='🔊',
            variable=self._voice_on,
            bg=s['primary'], fg='white',
            font=(s['font'], 14),
            selectcolor=s['primary'],
            activebackground=s['primary'],
            relief='flat', bd=0,
            cursor='hand2',
            command=lambda: self.app.audio.set_enabled(self._voice_on.get()),
        ).pack(side='right', padx=8)

        # "Say it again!" replay button — Joshua gets large button, Toby gets compact icon
        if self.app.current_profile == 'joshua':
            tk.Button(
                header, text='🔊 Say it again!',
                bg=s['secondary'], fg='#333',
                font=(s['font'], 13, 'bold'),
                relief='flat', bd=0, padx=12, pady=4, cursor='hand2',
                command=self._replay_voice,
            ).pack(side='right', padx=8)
        else:
            tk.Button(
                header, text='↺',
                bg=s['card_bg'], fg=s['text'],
                font=(s['font'], 12),
                relief='flat', bd=0, padx=8, pady=4, cursor='hand2',
                command=self._replay_voice,
            ).pack(side='right', padx=4)

    def _build_footer(self):
        s = self._style
        footer = tk.Frame(self, bg=s['card_bg'], padx=16, pady=10)
        footer.pack(fill='x', side='bottom')

        # Step indicator — use profile font_size for Joshua so it's readable
        step_font_size = s['font_size'] if self.app.current_profile == 'joshua' else 11
        self._step_label = tk.Label(
            footer, text='',
            bg=s['card_bg'], fg=s['subtext'],
            font=(s['font'], step_font_size),
        )
        self._step_label.pack(side='left')

        # Progress dots (updated per step)
        self._dots_frame = tk.Frame(footer, bg=s['card_bg'])
        self._dots_frame.pack(side='left', padx=20)

        # Buttons
        self._next_btn = tk.Button(
            footer, text='Next →',
            bg=s['primary'], fg='white',
            font=(s['font'], 13, 'bold'),
            relief='flat', bd=0, padx=16, pady=6,
            cursor='hand2',
            command=self._next_step,
        )
        self._next_btn.pack(side='right')

        self._hint_btn = tk.Button(
            footer, text='💡 Hint',
            bg=s['card_bg'], fg=s['secondary'],
            font=(s['font'], 11),
            relief='flat', bd=0, padx=12, pady=6,
            cursor='hand2',
            command=self._show_hint,
        )
        # Hint button visibility is toggled per-step in _show_step

        # Keyboard shortcut: Enter or Space to advance (but NOT when typing in code editor)
        def _maybe_next(event):
            focused = self.app.root.focus_get()
            if not isinstance(focused, (tk.Text, tk.Entry)):
                self._next_step()

        self.app.root.bind('<Return>', _maybe_next)
        self.app.root.bind('<space>', _maybe_next)

    # ------------------------------------------------------------------
    # Step rendering
    # ------------------------------------------------------------------

    def _show_step(self):
        """Clear content area and render current step."""
        for w in self._content_area.winfo_children():
            w.destroy()

        if self._step_idx >= len(self._steps):
            self._show_completion()
            return

        step = self._steps[self._step_idx]
        s = self._style

        # Update footer
        total = len(self._steps)
        current = self._step_idx + 1
        self._step_label.configure(text=f'Step {current} of {total}')
        self._update_dots(current, total)
        self._hint_idx = 0

        # Show/hide hint button based on whether this step has hints
        self._current_step_hints = step.get('hints', [])
        stype = step.get('type', 'teach')
        has_hints = bool(self._current_step_hints) or stype in ('exercise', 'quiz')
        if has_hints:
            self._hint_btn.pack(side='right', padx=8)
        else:
            self._hint_btn.pack_forget()

        # Determine next button label
        is_last = self._step_idx == len(self._steps) - 1
        self._next_btn.configure(
            text='Finish! 🎉' if is_last else 'Next →',
            state='normal',
            bg=s['primary'], fg='white',
        )

        # Speak the voice text
        voice = step.get('voice') or step.get('content', '')
        if voice:
            self.app.audio.speak(voice[:500], profile=self.app.current_profile, clear_queue=True)

        if stype in ('story', 'teach'):
            self._render_teach(step, s)
        elif stype == 'example':
            self._render_example(step, s)
        elif stype == 'exercise':
            self._render_exercise(step, s)
        elif stype == 'quiz':
            self._render_quiz(step, s)
        else:
            self._render_teach(step, s)

    def _update_dots(self, current, total):
        for w in self._dots_frame.winfo_children():
            w.destroy()
        s = self._style
        for i in range(1, total + 1):
            col = s['primary'] if i == current else (s['subtext'] if i < current else '#333')
            tk.Frame(
                self._dots_frame, bg=col,
                width=10 if i == current else 8,
                height=10 if i == current else 8,
            ).pack(side='left', padx=3, pady=5)

    # ── TEACH / STORY ──────────────────────────────────────────────

    def _render_teach(self, step, s):
        scroll_canvas = self._make_scroll_canvas()
        inner = scroll_canvas

        # Title
        if step.get('title'):
            tk.Label(
                inner, text=step['title'],
                bg=s['card_bg'], fg=s['primary'],
                font=(s['font'], s['title_size'], 'bold'),
                wraplength=900, justify='left', anchor='w',
            ).pack(anchor='w', padx=40, pady=(30, 8))

        # Content
        if step.get('content'):
            tk.Label(
                inner, text=step['content'],
                bg=s['card_bg'], fg=s['text'],
                font=(s['font'], s['font_size']),
                wraplength=900, justify='left', anchor='w',
            ).pack(anchor='w', padx=40, pady=(8, 30))

    # ── EXAMPLE ───────────────────────────────────────────────────

    def _render_example(self, step, s):
        inner = self._make_scroll_canvas()

        if step.get('title'):
            tk.Label(
                inner, text=step['title'],
                bg=s['card_bg'], fg=s['primary'],
                font=(s['font'], s['title_size'], 'bold'),
                wraplength=900, justify='left', anchor='w',
            ).pack(anchor='w', padx=40, pady=(30, 8))

        if step.get('content'):
            tk.Label(
                inner, text=step['content'],
                bg=s['card_bg'], fg=s['text'],
                font=(s['font'], s['font_size']),
                wraplength=900, justify='left', anchor='w',
            ).pack(anchor='w', padx=40, pady=(0, 12))

        # Code display (read-only)
        if step.get('code'):
            code_frame = tk.Frame(inner, bg='#0d1117', padx=0, pady=0)
            code_frame.pack(fill='x', padx=40, pady=4)

            tk.Label(
                code_frame, text='  📄 Example Code',
                bg='#161b22', fg='#58a6ff',
                font=('Consolas', 11, 'bold'),
                anchor='w', padx=8, pady=6,
            ).pack(fill='x')

            code_text = tk.Text(
                code_frame,
                bg='#0d1117', fg='#c9d1d9',
                font=('Consolas', s['code_size']),
                relief='flat', bd=0,
                padx=12, pady=8, height=min(20, step['code'].count('\n') + 3),
                state='normal',
            )
            code_text.insert('1.0', step['code'])
            code_text.configure(state='disabled')
            code_text.pack(fill='both')

            # Try it button
            from kidscode.ui.code_editor import CodeEditor
            editor = CodeEditor(inner, self.app, profile=self.app.current_profile, height=8)
            editor.pack(fill='x', padx=40, pady=(8, 20))
            editor.set_code(step['code'])

    # ── EXERCISE ───────────────────────────────────────────────────

    def _render_exercise(self, step, s):
        # For exercises, use a two-pane layout on Toby, single pane for Joshua
        profile = self.app.current_profile

        outer = tk.Frame(self._content_area, bg=s['bg'])
        outer.pack(fill='both', expand=True)

        if profile == 'toby':
            self._render_exercise_toby(outer, step, s)
        else:
            self._render_exercise_joshua(outer, step, s)

        self._current_step_hints = step.get('hints', [])

    def _render_exercise_toby(self, parent, step, s):
        """Side-by-side: instructions left, code editor right."""
        left = tk.Frame(parent, bg=s['card_bg'], width=380)
        left.pack(side='left', fill='y', padx=0, pady=0)
        left.pack_propagate(False)

        right = tk.Frame(parent, bg='#0d1117')
        right.pack(side='left', fill='both', expand=True)

        # Instructions pane
        tk.Label(
            left, text='📋 Instructions',
            bg=s['card_bg'], fg=s['primary'],
            font=(s['font'], 14, 'bold'), anchor='w',
        ).pack(anchor='w', padx=20, pady=(20, 4))

        tk.Label(
            left, text=step.get('content', ''),
            bg=s['card_bg'], fg=s['text'],
            font=(s['font'], s['font_size']),
            wraplength=340, justify='left', anchor='w',
        ).pack(anchor='w', padx=20, pady=4)

        # Expected output hint
        if step.get('expected_output'):
            tk.Label(
                left, text=f"Expected output:\n{step['expected_output']}",
                bg='#0d1117', fg='#4ade80',
                font=('Courier New', 10),
                wraplength=340, justify='left', anchor='w',
                padx=8, pady=6,
            ).pack(anchor='w', padx=20, pady=(16, 0), fill='x')

        # Code editor
        from kidscode.ui.code_editor import CodeEditor
        self._editor = CodeEditor(right, self.app, profile=self.app.current_profile, height=14)
        self._editor.pack(fill='both', expand=True, padx=0, pady=0)

        if step.get('starter_code'):
            self._editor.set_code(step['starter_code'])

        # Hook run results to check answer
        expected = step.get('expected_output')
        self._editor.set_on_run(lambda r, exp=expected: self._check_exercise(r, exp))

    def _render_exercise_joshua(self, parent, step, s):
        """Joshua: big clear layout with large code editor."""
        inner = tk.Frame(parent, bg=s['bg'])
        inner.pack(fill='both', expand=True, padx=30, pady=16)

        tk.Label(
            inner, text=step.get('title', '✏️ Your Turn!'),
            bg=s['bg'], fg=s['primary'],
            font=(s['font'], s['title_size'], 'bold'), anchor='w',
        ).pack(anchor='w', pady=(0, 8))

        tk.Label(
            inner, text=step.get('content', ''),
            bg=s['bg'], fg=s['text'],
            font=(s['font'], s['font_size']),
            wraplength=900, justify='left', anchor='w',
        ).pack(anchor='w', pady=(0, 16))

        from kidscode.ui.code_editor import CodeEditor
        self._editor = CodeEditor(inner, self.app, profile='joshua', height=10)
        self._editor.pack(fill='x')

        if step.get('starter_code'):
            self._editor.set_code(step['starter_code'])

        expected = step.get('expected_output')
        self._current_step_hints = step.get('hints', [])
        self._editor.set_on_run(lambda r, exp=expected: self._check_exercise(r, exp))

    def _check_exercise(self, result: dict, expected_output: str):
        """Called when the user runs their code in an exercise step."""
        profile = self.app.current_profile
        display_name = self.app.progress.get_display_name(profile)

        if not result['success']:
            self.app.audio.play('wrong')
            self.app.audio.speak(
                f"Hmm, there's an error in the code. Check the hints for help!",
                profile=profile,
            )
            return

        if expected_output is None:
            # Free-form exercise — running without error is success
            self.app.audio.play('correct')
            self.app.audio.speak(
                f"Amazing! Your code ran perfectly, {display_name}! Great work!",
                profile=profile,
            )
            self._next_btn.configure(bg='#4ade80', fg='#111')
            return

        # Compare trimmed output
        actual = result['output'].strip()
        expected = expected_output.strip()
        if actual == expected:
            self.app.audio.play('correct')
            self.app.audio.speak(
                f"Brilliant! That is exactly right! Amazing work {display_name}!",
                profile=profile,
            )
            self._next_btn.configure(bg='#4ade80', fg='#111')
        else:
            self.app.audio.play('wrong')
            self.app.audio.speak(
                "Not quite right yet. Check your output and try again!",
                profile=profile,
            )

    # ── QUIZ ──────────────────────────────────────────────────────

    def _render_quiz(self, step, s):
        inner = self._make_scroll_canvas()

        # Question
        tk.Label(
            inner, text=step.get('title', '🧠 Quiz Time!'),
            bg=s['card_bg'], fg=s['secondary'],
            font=(s['font'], s['title_size'], 'bold'), anchor='w',
            wraplength=900,
        ).pack(anchor='w', padx=40, pady=(30, 4))

        tk.Label(
            inner, text=step['question'],
            bg=s['card_bg'], fg=s['text'],
            font=(s['font'], s['font_size'] + 2, 'bold'),
            wraplength=900, justify='left', anchor='w',
        ).pack(anchor='w', padx=40, pady=(0, 20))

        # Options
        self._quiz_var = tk.IntVar(value=-1)
        self._quiz_result_label = tk.Label(
            inner, text='',
            bg=s['card_bg'], fg=s['text'],
            font=(s['font'], s['font_size']),
            wraplength=900, justify='left', anchor='w',
        )

        options_frame = tk.Frame(inner, bg=s['card_bg'])
        options_frame.pack(anchor='w', padx=40, fill='x')

        for idx, option in enumerate(step.get('options', [])):
            opt_frame = tk.Frame(
                options_frame, bg='#1e2a40', cursor='hand2',
                relief='flat', bd=0,
            )
            opt_frame.pack(fill='x', pady=4, ipady=4)

            rb = tk.Radiobutton(
                opt_frame,
                text=f"  {option}",
                variable=self._quiz_var,
                value=idx,
                bg='#1e2a40', fg=s['text'],
                selectcolor='#1e2a40',
                activebackground='#1e2a40',
                font=(s['font'], s['font_size']),
                anchor='w',
                cursor='hand2',
                relief='flat',
                command=lambda i=idx, sf=opt_frame, st=step: self._select_quiz(i, sf, st, s),
            )
            rb.pack(fill='x', padx=12, pady=4)
            rb.bind('<Button-1>', lambda e, i=idx, sf=opt_frame, st=step:
                    self._select_quiz(i, sf, st, s))

        self._quiz_result_label.pack(anchor='w', padx=40, pady=(16, 0))
        # Disable Next until the correct answer is selected
        self._next_btn.configure(state='disabled', bg=s['subtext'])

    def _select_quiz(self, idx, frame, step, s):
        """Handle a quiz option click."""
        correct = step['answer']
        if idx == correct:
            frame.configure(bg='#1a4731')
            self._quiz_result_label.configure(
                text=f"✅  Correct! {step.get('explanation', '')}",
                fg='#4ade80',
            )
            self.app.audio.play('correct')
            voice = step.get('explanation_voice', step.get('explanation', 'Correct! Well done!'))
            self.app.audio.speak(voice, profile=self.app.current_profile)
            self._next_btn.configure(bg='#4ade80', fg='#111')
            # Persist quiz result
            lesson_id = self._lesson.get('id', '')
            self.app.progress.record_quiz_score(
                self.app.current_profile, lesson_id, step.get('title', ''), True
            )
        else:
            frame.configure(bg='#4a1a1a')
            self._quiz_result_label.configure(
                text='❌  Not quite — try again!',
                fg='#f85149',
            )
            self.app.audio.play('wrong')

    # ================================================================
    # Navigation
    # ================================================================

    def _next_step(self):
        # Cache current progress before advancing
        if self._lesson:
            self._step_cache[self._lesson['id']] = self._step_idx + 1
        self._step_idx += 1
        self._show_step()

    def _show_hint(self):
        hints = getattr(self, '_current_step_hints', [])
        if not hints:
            return
        hint = hints[self._hint_idx % len(hints)]
        self._hint_idx += 1
        self.app.audio.speak(f"Hint: {hint}", profile=self.app.current_profile)
        # Show hint as a floating label — 10 seconds for emergent readers (was 4s)
        s = self._style
        hint_label = tk.Label(
            self, text=f"💡 {hint}",
            bg='#2a2a1a', fg=s['secondary'],
            font=(s['font'], 15), padx=16, pady=8,  # raised from 12 → 15pt
            wraplength=700,
        )
        hint_label.place(relx=0.5, rely=0.82, anchor='center')  # raised from 0.9 to clear footer
        self.after(10000, hint_label.destroy)  # raised from 4000 → 10000ms

    def _replay_voice(self):
        """Re-speak the current step's narration (for Joshua's 'Say it again!' button)."""
        if self._step_idx < len(self._steps):
            step = self._steps[self._step_idx]
            voice = step.get('voice') or step.get('content', '')
            if voice:
                self.app.audio.speak(
                    voice[:500], profile=self.app.current_profile, clear_queue=True
                )

    def _go_home(self):
        self.app.audio.clear_queue()
        self.app.show_screen('home', profile=self.app.current_profile)

    # ================================================================
    # Lesson Completion
    # ================================================================

    def _show_completion(self):
        """Show the lesson completion celebration screen."""
        profile = self.app.current_profile
        lesson = self._lesson
        s = self._style

        # ── Enforce lesson ordering within a module ─────────────────
        # Prevent completing a lesson if prior lessons in the same module
        # haven't been done yet (e.g. completing while-loop before for-loop)
        module_id = None
        for m in self.app.curriculum.get_modules(profile):
            for l in m.get('lessons', []):
                if l['id'] == lesson['id']:
                    module_id = m
                    break
            if module_id:
                break

        if module_id:
            lessons_in_module = [l['id'] for l in module_id.get('lessons', [])]
            lesson_idx = lessons_in_module.index(lesson['id']) if lesson['id'] in lessons_in_module else -1
            if lesson_idx > 0:
                completed = self.app.progress.get_completed_lessons(profile)
                for prior_id in lessons_in_module[:lesson_idx]:
                    if prior_id not in completed:
                        # Redirect to first incomplete prerequisite lesson
                        self.app.audio.speak(
                            f"Let's go back and finish the earlier lesson first!",
                            profile=profile, clear_queue=True,
                        )
                        self.app.show_screen('lesson', lesson_id=prior_id)
                        return

        # Award XP and mark complete
        xp = lesson.get('xp', 50)
        self.app.progress.complete_lesson(profile, lesson['id'], xp=xp)
        # Clear step cache now that lesson is finished
        self._step_cache.pop(lesson['id'], None)

        # Check for module badge
        earned_badge_name = None
        earned_badge_icon = None
        if module_id:
            lesson_ids = [l['id'] for l in module_id.get('lessons', [])]
            done, total = self.app.progress.get_module_progress(profile, lesson_ids)
            if done >= total:
                badge = module_id.get('badge', '')
                if badge:
                    is_new = self.app.progress.award_badge(profile, badge)
                    if is_new:
                        earned_badge_name = badge
                        earned_badge_icon = module_id.get('badge_icon', '🏅')

        self.app.audio.play('star')

        # Build celebration UI
        for w in self.winfo_children():
            w.destroy()

        outer = tk.Frame(self, bg=s['bg'])
        outer.pack(fill='both', expand=True)

        # Big celebration
        tk.Label(
            outer, text='🎉', bg=s['bg'],
            font=('Segoe UI', 80),
        ).pack(pady=(60, 0))

        tk.Label(
            outer, text='Lesson Complete!',
            bg=s['bg'], fg=s['primary'],
            font=(s['font'], s['title_size'] + 8, 'bold'),
        ).pack()

        tk.Label(
            outer, text=lesson['title'],
            bg=s['bg'], fg=s['text'],
            font=(s['font'], s['font_size'] + 2),
        ).pack(pady=4)

        tk.Label(
            outer, text=f"+ {xp} XP  ⭐",
            bg=s['bg'], fg=s['secondary'],
            font=(s['font'], 20, 'bold'),
        ).pack(pady=12)

        # Next lesson or home buttons
        btn_row = tk.Frame(outer, bg=s['bg'])
        btn_row.pack(pady=24)

        next_lesson = self.app.curriculum.next_lesson(profile, lesson['id'])
        if next_lesson:
            tk.Button(
                btn_row,
                text=f"Next Lesson: {next_lesson['title']} →",
                bg=s['primary'], fg='white',
                font=(s['font'], s['font_size'], 'bold'),
                relief='flat', bd=0, padx=20, pady=10,
                cursor='hand2',
                command=lambda lid=next_lesson['id']: self.prepare(lesson_id=lid),
            ).pack(side='left', padx=8)

        tk.Button(
            btn_row, text='🏠 Back to Modules',
            bg=s['card_bg'], fg=s['text'],
            font=(s['font'], s['font_size']),
            relief='flat', bd=0, padx=16, pady=10,
            cursor='hand2',
            command=self._go_home,
        ).pack(side='left', padx=8)

        # Speak completion — use "stars" for Joshua, "XP" for Toby
        name = 'Joshua' if profile == 'joshua' else 'Toby'
        reward_phrase = f"earned {xp} stars" if profile == 'joshua' else f"earned {xp} XP"
        self.app.audio.speak(
            f"Fantastic work {name}! You completed the lesson and {reward_phrase}! "
            "You are doing brilliantly!",
            profile=profile, clear_queue=True,
        )

        # Show badge celebration overlay if a new badge was just earned
        if earned_badge_name:
            self.after(1200, lambda: self._show_badge_unlock(
                earned_badge_name, earned_badge_icon, outer
            ))

    def _show_badge_unlock(self, badge_name: str, badge_icon: str, parent: tk.Frame):
        """Full-screen badge unlock overlay with celebration voice."""
        s = self._style

        overlay = tk.Frame(parent, bg='#000000')
        overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
        overlay.configure(bg='#0a0a1a')

        popup = tk.Frame(overlay, bg='#1a1a35', padx=50, pady=40)
        popup.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(popup, text='🏅 NEW BADGE UNLOCKED!',
                 bg='#1a1a35', fg='#fbbf24',
                 font=(s['font'], 18, 'bold')).pack()

        tk.Label(popup, text=badge_icon, bg='#1a1a35',
                 font=('Segoe UI', 80)).pack(pady=(12, 4))

        tk.Label(popup, text=badge_name,
                 bg='#1a1a35', fg='white',
                 font=(s['font'], s['font_size'] + 4, 'bold')).pack(pady=4)

        tk.Button(popup,
                  text='Awesome! 🚀' if self.app.current_profile == 'toby' else 'YAY! 🌟',
                  bg=s['primary'], fg='white',
                  font=(s['font'], 14, 'bold'),
                  relief='flat', padx=24, pady=10, cursor='hand2',
                  command=overlay.destroy).pack(pady=20)

        name = 'Joshua' if self.app.current_profile == 'joshua' else 'Toby'
        voice = (
            f"Yes! You earned the {badge_name} badge! Absolutely brilliant {name}!"
            if self.app.current_profile == 'joshua'
            else f"Boom! You just earned the {badge_name} badge! Absolutely fire, {name}!"
        )
        self.app.audio.speak(voice, profile=self.app.current_profile)

    # ================================================================
    # Helpers
    # ================================================================

    def _make_scroll_canvas(self) -> tk.Frame:
        """Create a scrollable frame inside content_area, return inner frame."""
        s = self._style

        canvas = tk.Canvas(self._content_area, bg=s['card_bg'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(self._content_area, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')
        canvas.pack(side='left', fill='both', expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)

        inner = tk.Frame(canvas, bg=s['card_bg'])
        cw = canvas.create_window((0, 0), window=inner, anchor='nw')

        def on_resize(e):
            canvas.itemconfig(cw, width=e.width)

        canvas.bind('<Configure>', on_resize)
        inner.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.bind_all('<MouseWheel>', lambda e: canvas.yview_scroll(-1*(e.delta//120), 'units'))

        return inner
