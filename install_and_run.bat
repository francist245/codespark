@echo off
title KidsCode - Installing...
echo ============================================
echo    KidsCode - Coding for Toby and Joshua!
echo ============================================
echo.
echo Checking Python...
python --version 2>nul
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please download Python from https://python.org
    pause
    exit /b 1
)
echo.
echo Installing required packages...
python -m pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo ERROR: Failed to install packages.
    echo Please run: pip install pyttsx3 pygame Pillow
    pause
    exit /b 1
)
echo.
echo Starting KidsCode...
echo.
python main.py
pause
