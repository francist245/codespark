#!/usr/bin/env python3
"""
KidsCode - Interactive Python Coding Education
For Toby (age 10) and Joshua (age 5)

Run this file to start learning!
"""
import subprocess
import sys
import os

REQUIRED_PACKAGES = [
    ('pyttsx3', 'pyttsx3'),
    ('PIL', 'Pillow'),
]
# pygame is optional — used for richer sounds & game lessons.
# If it installs on your Python version, great; otherwise winsound is used.
OPTIONAL_PACKAGES = [('pygame', 'pygame')]


def check_and_install():
    """Check for required packages and install if missing."""
    missing = []
    for import_name, pip_name in REQUIRED_PACKAGES:
        try:
            __import__(import_name)
        except ImportError:
            missing.append(pip_name)

    if missing:
        print("=" * 50)
        print("  KidsCode - First Time Setup")
        print("=" * 50)
        print(f"Installing: {', '.join(missing)}")
        for pkg in missing:
            print(f"  Installing {pkg}...", end=' ', flush=True)
            try:
                subprocess.check_call(
                    [sys.executable, '-m', 'pip', 'install', pkg],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                print("✓")
            except subprocess.CalledProcessError:
                print("✗ FAILED")
                print(f"\nPlease run manually:  pip install {pkg}")
                sys.exit(1)

    # Try optional packages silently
    for import_name, pip_name in OPTIONAL_PACKAGES:
        try:
            __import__(import_name)
        except ImportError:
            try:
                subprocess.check_call(
                    [sys.executable, '-m', 'pip', 'install', pip_name],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                )
            except Exception:
                pass  # Optional — no problem if it fails

    if missing:
        print("\nAll packages ready! Starting KidsCode...\n")


if __name__ == '__main__':
    check_and_install()

    # Ensure the app directory is on the path
    app_dir = os.path.dirname(os.path.abspath(__file__))
    if app_dir not in sys.path:
        sys.path.insert(0, app_dir)

    from kidscode.app import KidsCodeApp
    app = KidsCodeApp()
    app.run()
