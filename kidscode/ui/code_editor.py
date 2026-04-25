"""
Code Editor Widget — embedded Python editor with sandbox execution.
Used inside LessonViewer for exercise steps.
"""
import tkinter as tk
from tkinter import scrolledtext
import threading


DARK_BG    = '#0d1117'
LINE_BG    = '#1c2333'
TEXT_FG    = '#c9d1d9'
CURSOR_FG  = '#58a6ff'
OUTPUT_BG  = '#0d1117'
OUTPUT_FG  = '#3fb950'
ERROR_FG   = '#f85149'
KEYWORD_FG = '#ff7b72'
STRING_FG  = '#a5d6ff'
COMMENT_FG = '#8b949e'
NUMBER_FG  = '#79c0ff'


class CodeEditor(tk.Frame):
    """A simple Python code editor with syntax highlighting and sandbox run."""

    def __init__(self, parent, app, profile='toby', height=12, **kwargs):
        super().__init__(parent, bg=DARK_BG, **kwargs)
        self.app = app
        self.profile = profile
        self._running = False
        self._on_run_callback = None
        self._build(height)
        self._setup_highlighting()
        self._show_placeholder()

    # ------------------------------------------------------------------
    # Build
    # ------------------------------------------------------------------

    def _build(self, height):
        self._starter_code = ''  # stored for Reset button
        is_joshua = self.profile == 'joshua'
        code_font_size = 18 if is_joshua else 12
        btn_font_size = 16 if is_joshua else 11
        small_btn_size = 13 if is_joshua else 10

        # ── Toolbar ──────────────────────────────────────────────────
        toolbar = tk.Frame(self, bg='#161b22', padx=8, pady=6)
        toolbar.pack(fill='x')

        editor_label = '✏️ My Code' if is_joshua else '</> Code Editor'
        tk.Label(
            toolbar, text=editor_label,
            bg='#161b22', fg='#58a6ff',
            font=('Courier New', btn_font_size, 'bold'),
        ).pack(side='left')

        self._run_btn = tk.Button(
            toolbar, text='▶  Run Code',
            bg='#238636', fg='white',
            font=('Segoe UI', btn_font_size, 'bold'),
            relief='flat', bd=0, padx=12, pady=4,
            cursor='hand2',
            command=self._run_code,
        )
        self._run_btn.pack(side='right', padx=4)

        reset_label = '🔄 Start Again' if is_joshua else '🔄 Reset'
        tk.Button(
            toolbar, text=reset_label,
            bg='#21262d', fg='#aaa',
            font=('Segoe UI', small_btn_size),
            relief='flat', bd=0, padx=10, pady=4,
            cursor='hand2',
            command=self._reset_code,
        ).pack(side='right', padx=4)

        clear_label = '🗑 Rub Out' if is_joshua else '🗑 Clear'
        tk.Button(
            toolbar, text=clear_label,
            bg='#21262d', fg='#aaa',
            font=('Segoe UI', small_btn_size),
            relief='flat', bd=0, padx=10, pady=4,
            cursor='hand2',
            command=self._clear_output,
        ).pack(side='right', padx=4)

        # ── Code text area ───────────────────────────────────────────
        self._editor_frame = tk.Frame(self, bg=DARK_BG)
        self._editor_frame.pack(fill='both', expand=True)

        # Line numbers
        self._line_nums = tk.Text(
            self._editor_frame,
            width=4, bg=LINE_BG, fg='#555',
            font=('Courier New', code_font_size),
            state='disabled', relief='flat', bd=0,
            padx=4, pady=6, selectbackground=LINE_BG,
        )
        self._line_nums.pack(side='left', fill='y')

        self._text = tk.Text(
            self._editor_frame,
            bg=DARK_BG, fg=TEXT_FG,
            insertbackground=CURSOR_FG,
            font=('Courier New', code_font_size),
            relief='flat', bd=0,
            height=height,
            padx=8, pady=6,
            undo=True,
            tabs=('1c',),
            wrap='none',
        )
        self._text.pack(side='left', fill='both', expand=True)

        yscroll = tk.Scrollbar(self._editor_frame, command=self._text.yview)
        yscroll.pack(side='right', fill='y')
        self._text.configure(yscrollcommand=yscroll.set)

        self._text.bind('<KeyRelease>', self._on_key)
        self._text.bind('<Tab>', self._handle_tab)
        self._text.bind('<Return>', self._handle_enter)
        self._text.bind('<FocusIn>', self._hide_placeholder)
        self._text.bind('<FocusOut>', lambda e: self._show_placeholder())

        # ── Inputs panel (shown when code has input() calls) ─────────
        self._inputs_frame = tk.Frame(self, bg='#1c2333')
        # (packed/unpacked dynamically in _on_key and set_code)

        inputs_header = tk.Frame(self._inputs_frame, bg='#1c2333', padx=8, pady=4)
        inputs_header.pack(fill='x')
        inputs_label = '✏️ Type your answers here!' if is_joshua else \
            '⌨  Program Inputs  (type one value per line — your answers go here!)'
        tk.Label(
            inputs_header, text=inputs_label,
            bg='#1c2333', fg='#fbbf24',
            font=('Segoe UI', small_btn_size, 'bold'),
        ).pack(side='left')

        self._inputs_text = tk.Text(
            self._inputs_frame,
            bg='#1c2333', fg='#fbbf24',
            insertbackground='#fbbf24',
            font=('Courier New', 11),
            height=3, relief='flat', bd=0,
            padx=8, pady=4,
        )
        self._inputs_text.pack(fill='x')
        tk.Label(
            self._inputs_frame,
            text='💡 Each input() in your code reads one line from here (top to bottom)',
            bg='#1c2333', fg='#666',
            font=('Segoe UI', 9),
        ).pack(anchor='w', padx=8, pady=(0, 4))

        # ── Output panel ─────────────────────────────────────────────
        out_header = tk.Frame(self, bg='#161b22', padx=8, pady=4)
        out_header.pack(fill='x')
        tk.Label(
            out_header, text='⚙  Output',
            bg='#161b22', fg='#8b949e',
            font=('Segoe UI', 10),
        ).pack(side='left')

        self._output = tk.Text(
            self,
            bg=OUTPUT_BG, fg=OUTPUT_FG,
            font=('Courier New', code_font_size - 2),
            height=6, state='disabled',
            relief='flat', bd=0,
            padx=8, pady=6,
            wrap='word',
        )
        self._output.pack(fill='both', expand=False)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def set_code(self, code: str):
        """Set the code editor content and store as starter code for reset."""
        self._has_placeholder = False
        self._starter_code = code
        self._text.delete('1.0', 'end')
        self._text.insert('1.0', code)
        self._highlight()
        self._update_line_numbers()
        self._update_inputs_panel(code)

    def get_code(self) -> str:
        return self._text.get('1.0', 'end-1c')

    def get_output(self) -> str:
        return self._output.get('1.0', 'end-1c')

    def set_profile(self, profile: str):
        self.profile = profile

    # ------------------------------------------------------------------
    # Code execution
    # ------------------------------------------------------------------

    def _reset_code(self):
        """Restore the original starter code."""
        if self._starter_code:
            self._text.delete('1.0', 'end')
            self._text.insert('1.0', self._starter_code)
            self._highlight()
            self._update_line_numbers()
            self._clear_output()

    def _run_code(self):
        if self._running:
            return
        self._hide_placeholder()
        code = self.get_code().strip()
        if not code:
            self._clear_output()
            self._append_output('✏️ Type some code first, then press Run Code!', '#fbbf24')
            return
        self._running = True
        self._run_btn.configure(text='⏳ Running…', state='disabled', bg='#555')
        self._clear_output()
        self._append_output('Running...\n', '#8b949e')

        # Collect prefilled inputs from the inputs panel
        inputs_raw = self._inputs_text.get('1.0', 'end-1c') if hasattr(self, '_inputs_text') else ''
        prefilled = [line for line in inputs_raw.splitlines() if line] or None

        def worker():
            from kidscode.sandbox import SafeCodeRunner
            runner = SafeCodeRunner(profile=self.profile)
            result = runner.run(code, prefilled_inputs=prefilled)
            self.after(0, lambda: self._show_result(result))

        threading.Thread(target=worker, daemon=True).start()

    def _show_result(self, result: dict):
        self._running = False
        self._run_btn.configure(text='▶  Run Code', state='normal', bg='#238636')
        self._clear_output()

        if result['output']:
            self._append_output(result['output'], OUTPUT_FG)

        if result['error']:
            friendly = self._friendly_error(result['error'])
            self._append_output('\n' + friendly, ERROR_FG)
            self.app.audio.play('wrong')
        elif result['success']:
            if not result['output']:
                self._append_output('✅ Your code ran successfully! (no output)', '#4ade80')
            self.app.audio.play('correct')

        # Flash the output panel so kids notice the result
        self._flash_output()

        if hasattr(self, '_on_run_callback') and self._on_run_callback:
            self._on_run_callback(result)

    def _flash_output(self):
        """Brief green flash on output panel to draw the child's eye."""
        orig_bg = self._output.cget('bg')
        self._output.configure(bg='#1a3a1a')
        self.after(400, lambda: self._output.configure(bg=orig_bg))

    @staticmethod
    def _friendly_error(msg: str) -> str:
        """Convert raw Python errors into kid-friendly messages."""
        m = msg.lower()
        if "could not convert string to float: ''" in m or "invalid literal for int() with base 10: ''" in m:
            return ("❓ input() didn't get a value!\n"
                    "👆 Type your answer in the 'Program Inputs' box above, then run again.")
        if 'zerodivisionerror' in m:
            return "🚫 ZeroDivisionError — you tried to divide by zero! Maths doesn't allow that."
        if 'nameerror' in m:
            parts = msg.split("'")
            name = parts[1] if len(parts) > 1 else '?'
            return (f"❓ NameError — Python can't find a variable called '{name}'.\n"
                    "Did you create it with = before using it?")
        if 'indentationerror' in m:
            return ("📐 IndentationError — your code isn't lined up correctly.\n"
                    "Python uses spaces/indentation to group code. Check your spacing!")
        if 'syntaxerror' in m or 'syntax error' in m:
            return f"✏️ Syntax Error — there's a typo in your code.\n{msg}"
        if 'typeerror' in m:
            return f"🔤 TypeError — wrong type used somewhere.\n{msg}"
        if 'valueerror' in m:
            return f"🔢 ValueError — unexpected value.\n{msg}"
        if 'safety check' in m:
            return f"🛡️ {msg}"
        if 'took too long' in m or 'infinite loop' in m:
            return "⏱️ Your code took too long! Check for an infinite loop (a loop that never stops)."
        return f"❌ Error: {msg}"

    def set_on_run(self, callback):
        """Register a callback called with the run result dict."""
        self._on_run_callback = callback

    # ------------------------------------------------------------------
    # Placeholder text
    # ------------------------------------------------------------------

    def _show_placeholder(self):
        """Show ghost placeholder text when editor is empty."""
        if self.get_code().strip():
            return
        hint = '# Type your code here...' if self.profile == 'toby' else '# Type your code here! 😊'
        self._text.insert('1.0', hint)
        self._text.tag_add('placeholder', '1.0', 'end')
        self._text.tag_configure('placeholder', foreground='#555')
        self._has_placeholder = True

    def _hide_placeholder(self, event=None):
        """Remove placeholder text when editor gets focus."""
        if getattr(self, '_has_placeholder', False):
            self._text.delete('1.0', 'end')
            self._has_placeholder = False

    # ------------------------------------------------------------------
    # Output helpers
    # ------------------------------------------------------------------

    def _clear_output(self):
        self._output.configure(state='normal')
        self._output.delete('1.0', 'end')
        self._output.configure(state='disabled')

    def _append_output(self, text: str, color: str = OUTPUT_FG):
        self._output.configure(state='normal')
        tag = f'col_{color.strip("#")}'
        self._output.tag_configure(tag, foreground=color)
        self._output.insert('end', text, tag)
        self._output.configure(state='disabled')
        self._output.see('end')

    # ------------------------------------------------------------------
    # Syntax highlighting (basic)
    # ------------------------------------------------------------------

    KEYWORDS = {
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
        'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
        'while', 'with', 'yield', 'print', 'input', 'range', 'len', 'int',
        'str', 'float', 'bool', 'list', 'dict', 'tuple', 'set',
    }

    def _setup_highlighting(self):
        sz = 18 if self.profile == 'joshua' else 12
        self._text.tag_configure('keyword', foreground=KEYWORD_FG, font=('Courier New', sz, 'bold'))
        self._text.tag_configure('string',  foreground=STRING_FG)
        self._text.tag_configure('comment', foreground=COMMENT_FG, font=('Courier New', sz, 'italic'))
        self._text.tag_configure('number',  foreground=NUMBER_FG)

    def _highlight(self):
        """Apply basic syntax highlighting."""
        import re
        t = self._text

        # Remove all existing highlight tags
        for tag in ('keyword', 'string', 'comment', 'number'):
            t.tag_remove(tag, '1.0', 'end')

        content = t.get('1.0', 'end')
        lines = content.split('\n')

        for lineno, line in enumerate(lines, start=1):
            # Comments
            idx = line.find('#')
            if idx != -1:
                t.tag_add('comment', f'{lineno}.{idx}', f'{lineno}.end')
                line = line[:idx]

            # Strings (simple single and double quoted)
            for m in re.finditer(r'(\"\"\".*?\"\"\"|\'\'\'.*?\'\'\'|\"[^\"]*\"|\'[^\']*\')',
                                  line, re.DOTALL):
                t.tag_add('string', f'{lineno}.{m.start()}', f'{lineno}.{m.end()}')

            # Numbers
            for m in re.finditer(r'\b\d+\.?\d*\b', line):
                t.tag_add('number', f'{lineno}.{m.start()}', f'{lineno}.{m.end()}')

            # Keywords
            for m in re.finditer(r'\b([A-Za-z_]\w*)\b', line):
                word = m.group(1)
                if word in self.KEYWORDS:
                    t.tag_add('keyword', f'{lineno}.{m.start()}', f'{lineno}.{m.end()}')

    def _on_key(self, event=None):
        self._highlight()
        self._update_line_numbers()
        self._update_inputs_panel(self.get_code())

    def _update_inputs_panel(self, code: str):
        """Show/hide the inputs panel based on whether code uses input()."""
        import re
        has_input = bool(re.search(r'\binput\s*\(', code))
        if has_input:
            self._inputs_frame.pack(fill='x', after=self._editor_frame)
        else:
            self._inputs_frame.pack_forget()

    def _update_line_numbers(self):
        code = self._text.get('1.0', 'end-1c')
        lines = code.count('\n') + 1
        nums = '\n'.join(str(i) for i in range(1, lines + 1))
        self._line_nums.configure(state='normal')
        self._line_nums.delete('1.0', 'end')
        self._line_nums.insert('1.0', nums)
        self._line_nums.configure(state='disabled')

    def _handle_tab(self, event):
        """Convert Tab key to 4 spaces."""
        self._text.insert('insert', '    ')
        return 'break'

    def _handle_enter(self, event):
        """Auto-indent: match previous line's indent, add 4 spaces after ':'."""
        current_line = self._text.get('insert linestart', 'insert')
        indent = len(current_line) - len(current_line.lstrip())
        if current_line.rstrip().endswith(':'):
            indent += 4
        self._text.insert('insert', '\n' + ' ' * indent)
        self._on_key()
        return 'break'
