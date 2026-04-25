"""
Safe Code Execution Sandbox

Runs user-submitted Python code safely using:
  - AST analysis to block dangerous patterns
  - Restricted built-ins namespace
  - Captured stdout/stderr
  - Execution timeout

Age-based restriction levels:
  joshua (age 5) - only print, input, range, basic maths
  toby   (age 10) - additionally: math, random, datetime, json, re, collections
"""
import ast
import io
import sys
import threading
import traceback
import textwrap

# ---------------------------------------------------------------------------
# Dangerous module names that are never allowed for any profile
# ---------------------------------------------------------------------------
ALWAYS_BLOCKED_MODULES = frozenset({
    'os', 'subprocess', 'sys', 'shutil', 'pathlib', 'glob',
    'socket', 'ssl', 'asyncio', 'httplib', 'urllib', 'http',
    'requests', 'ftplib', 'smtplib', 'telnetlib', 'imaplib',
    'threading', 'multiprocessing', 'concurrent',
    'ctypes', 'cffi', 'mmap',
    'pickle', 'marshal', 'shelve', 'copyreg',
    'importlib', 'imp', '__future__',
    'winreg', 'winsound', 'msvcrt', 'nt',
    'builtins', '__builtins__',
    'code', 'codeop', 'py_compile', 'compileall',
    'dis', 'inspect', 'gc', 'weakref',
    'signal', 'atexit', 'traceback',
    'tempfile', 'io', 'struct',
    'cryptography', 'hashlib', 'hmac', 'secrets',
    'paramiko', 'fabric',
})

# Modules additionally allowed for Toby (age 10)
TOBY_ALLOWED = frozenset({
    'math', 'random', 'datetime', 'json', 're',
    'string', 'collections', 'itertools', 'functools',
    'operator', 'copy', 'pprint', 'textwrap',
    'fractions', 'decimal', 'statistics',
})

# Modules allowed for Joshua (age 5) - very restricted
JOSHUA_ALLOWED = frozenset({
    'math', 'random',
})

# Dangerous built-in names that must NOT appear in restricted namespace
BLOCKED_BUILTINS = frozenset({
    '__import__', '__loader__', '__spec__', '__build_class__',
    'open', 'exec', 'eval', 'compile',
    'globals', 'locals', 'vars', 'dir',
    'breakpoint', 'memoryview',
})


def _make_safe_builtins(extra_allowed=None, allow_classes=False):
    """Return a restricted __builtins__ dict."""
    safe = {
        # I/O
        'print': print,
        # Types
        'bool': bool, 'int': int, 'float': float, 'complex': complex,
        'str': str, 'bytes': bytes, 'bytearray': bytearray,
        'list': list, 'tuple': tuple, 'set': set, 'frozenset': frozenset,
        'dict': dict,
        # Iteration / functional
        'range': range, 'enumerate': enumerate, 'zip': zip,
        'map': map, 'filter': filter, 'reversed': reversed, 'sorted': sorted,
        # Math helpers
        'abs': abs, 'divmod': divmod, 'pow': pow, 'round': round,
        'max': max, 'min': min, 'sum': sum,
        # String / char
        'chr': chr, 'ord': ord, 'hex': hex, 'oct': oct, 'bin': bin,
        'format': format, 'repr': repr, 'len': len, 'hash': hash,
        # Type checks
        'isinstance': isinstance, 'issubclass': issubclass, 'type': type,
        'callable': callable, 'hasattr': hasattr,
        # Object creation helpers
        'object': object, 'slice': slice,
        # Constants
        'True': True, 'False': False, 'None': None,
        'NotImplemented': NotImplemented, 'Ellipsis': Ellipsis,
        # Exceptions (read-only – can't be re-assigned to do harm)
        'Exception': Exception, 'BaseException': BaseException,
        'ValueError': ValueError, 'TypeError': TypeError,
        'IndexError': IndexError, 'KeyError': KeyError,
        'AttributeError': AttributeError, 'NameError': NameError,
        'RuntimeError': RuntimeError, 'StopIteration': StopIteration,
        'ZeroDivisionError': ZeroDivisionError, 'OverflowError': OverflowError,
        'AssertionError': AssertionError, 'NotImplementedError': NotImplementedError,
        'OSError': OSError, 'IOError': IOError,
        'ArithmeticError': ArithmeticError, 'LookupError': LookupError,
        'ImportError': ImportError, 'ModuleNotFoundError': ModuleNotFoundError,
        # Misc helpers
        'iter': iter, 'next': next, 'all': all, 'any': any,
        'id': id,
    }
    if extra_allowed:
        safe.update(extra_allowed)
    # Allow class definitions for profiles that need OOP (Toby's M6+)
    if allow_classes:
        safe['__build_class__'] = __builtins__['__build_class__'] if isinstance(__builtins__, dict) else getattr(__builtins__, '__build_class__')
    return safe


class CodeSafetyError(Exception):
    pass


class _ImportBlocker(ast.NodeVisitor):
    """AST visitor that raises CodeSafetyError on disallowed imports."""

    def __init__(self, allowed_modules):
        self.allowed = allowed_modules

    def visit_Import(self, node):
        for alias in node.names:
            mod = alias.name.split('.')[0]
            self._check(mod)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module:
            mod = node.module.split('.')[0]
            self._check(mod)
        self.generic_visit(node)

    def visit_Call(self, node):
        """Block __import__('os') style calls."""
        if isinstance(node.func, ast.Name) and node.func.id == '__import__':
            raise CodeSafetyError(
                "Direct use of __import__() is not allowed. Use 'import module' instead."
            )
        self.generic_visit(node)

    def _check(self, module_name: str):
        if module_name in ALWAYS_BLOCKED_MODULES:
            raise CodeSafetyError(
                f"The module '{module_name}' is not available in the learning sandbox."
            )
        if module_name not in self.allowed and module_name != '__future__':
            raise CodeSafetyError(
                f"The module '{module_name}' is not available at your current level. "
                f"Keep going and it will unlock!"
            )


class _DangerousPatternChecker(ast.NodeVisitor):
    """Catch additional dangerous patterns in the AST."""

    def visit_Attribute(self, node):
        dangerous_attrs = {
            '__class__', '__subclasses__', '__bases__', '__mro__',
            '__globals__', '__builtins__', '__code__', '__closure__',
            '__func__', '__self__',
        }
        if isinstance(node.attr, str) and node.attr in dangerous_attrs:
            raise CodeSafetyError(
                f"Accessing '{node.attr}' is not permitted in the sandbox."
            )
        self.generic_visit(node)

    def visit_Name(self, node):
        blocked_names = {'__import__', 'open', 'exec', 'eval', 'compile',
                         'globals', 'locals', 'vars', '__builtins__'}
        if node.id in blocked_names:
            raise CodeSafetyError(
                f"'{node.id}' is not available in the learning sandbox."
            )
        self.generic_visit(node)


def _run_with_timeout(func, timeout_seconds: float):
    """Run func() in a thread; return (result, exception) within timeout."""
    result = [None]
    exc = [None]

    def target():
        try:
            result[0] = func()
        except Exception as e:
            exc[0] = e

    t = threading.Thread(target=target, daemon=True)
    t.start()
    t.join(timeout_seconds)
    if t.is_alive():
        return None, TimeoutError(
            f"Your code took too long to run (over {timeout_seconds}s). "
            "Check for infinite loops!"
        )
    return result[0], exc[0]


class SafeCodeRunner:
    """Runs sandboxed Python code for a specific profile."""

    TIMEOUT = 8.0  # seconds

    def __init__(self, profile: str = 'toby'):
        self.profile = profile
        allowed = TOBY_ALLOWED if profile == 'toby' else JOSHUA_ALLOWED
        self._allowed_modules = allowed
        # Toby gets class definitions for OOP modules
        self._safe_builtins = _make_safe_builtins(allow_classes=(profile == 'toby'))

    def run(self, code: str, prefilled_inputs=None) -> dict:
        """
        Execute code safely.

        Returns a dict:
          {
            'output': str,    # captured stdout
            'error':  str,    # error message (empty string if none)
            'success': bool,
          }
        """
        code = textwrap.dedent(code)

        # ---- 1. Parse ----
        try:
            tree = ast.parse(code, mode='exec')
        except SyntaxError as e:
            return {
                'output': '',
                'error': f"Syntax Error on line {e.lineno}: {e.msg}",
                'success': False,
            }

        # ---- 2. Safety analysis ----
        try:
            _ImportBlocker(self._allowed_modules).visit(tree)
            _DangerousPatternChecker().visit(tree)
        except CodeSafetyError as e:
            return {
                'output': '',
                'error': f"Safety Check: {e}",
                'success': False,
            }

        # ---- 3. Prepare restricted namespace ----
        input_values = list(prefilled_inputs or [])
        input_index = [0]

        def safe_input(prompt=''):
            """input() that draws from prefilled list or returns empty string."""
            if prompt:
                captured_stdout.write(str(prompt))
            if input_index[0] < len(input_values):
                val = str(input_values[input_index[0]])
                input_index[0] += 1
                captured_stdout.write(val + '\n')
                return val
            return ''

        def safe_import(name, *args, **kwargs):
            top = name.split('.')[0]
            if top in ALWAYS_BLOCKED_MODULES:
                raise ImportError(f"Module '{name}' is not available in the sandbox.")
            if top not in self._allowed_modules:
                raise ImportError(f"Module '{name}' is not available at your level yet.")
            return __builtins__['__import__'](name, *args, **kwargs) \
                if isinstance(__builtins__, dict) \
                else __import__(name, *args, **kwargs)

        restricted_globals = {
            '__builtins__': dict(self._safe_builtins),
            '__name__': '__kidscode__',
        }
        restricted_globals['__builtins__']['input'] = safe_input
        restricted_globals['__builtins__']['__import__'] = safe_import

        # ---- 4. Execute with timeout and captured I/O ----
        captured_stdout = io.StringIO()
        captured_stderr = io.StringIO()

        def execute():
            old_stdout = sys.stdout
            old_stderr = sys.stderr
            sys.stdout = captured_stdout
            sys.stderr = captured_stderr
            try:
                exec(compile(tree, '<kidscode>', 'exec'), restricted_globals)  # noqa: S102
            finally:
                sys.stdout = old_stdout
                sys.stderr = old_stderr

        _, exc = _run_with_timeout(execute, self.TIMEOUT)

        output = captured_stdout.getvalue()
        if exc:
            err_type = type(exc).__name__
            if isinstance(exc, TimeoutError):
                err_msg = str(exc)
            else:
                lines = traceback.format_exception(type(exc), exc, exc.__traceback__)
                # Strip internal sandbox frames; show only user-visible part
                user_lines = [l for l in lines if '<kidscode>' in l or err_type in l]
                err_msg = ''.join(user_lines).strip() if user_lines else str(exc)
                err_msg = f"{err_type}: {exc}"
            return {'output': output, 'error': err_msg, 'success': False}

        return {'output': output, 'error': '', 'success': True}
