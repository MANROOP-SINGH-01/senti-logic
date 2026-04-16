@echo off
TITLE Research Intelligence Platform v7.2 - LAUNCHER
:: Controlled Research Environment Launcher
:: Author: Antigravity AI

echo [OS] Initializing Research Environment...
python scripts/setup_project.py
if %ERRORLEVEL% NEQ 0 (
    echo [!] Environment check failed. Please resolve errors above.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [SERVER] Starting Live Data Hosting on port 8000...
echo [SYSTEM] Platform UI: http://localhost:8000/dashboard/index.html
echo.

:: Start the browser in a new window
start http://localhost:8000/dashboard/index.html

:: Start the HTTP server in the current window
python -m http.server 8000
pause
