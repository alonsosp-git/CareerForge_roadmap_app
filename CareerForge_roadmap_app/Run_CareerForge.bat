@echo off
cd /d "%~dp0"
REM Runs CareerForge and opens it in your browser. Requires Python 3.9+.
where python >nul 2>&1 && (set "PY=python") || (set "PY=py")
%PY% -m pip install flask --quiet
%PY% launcher.py
pause
