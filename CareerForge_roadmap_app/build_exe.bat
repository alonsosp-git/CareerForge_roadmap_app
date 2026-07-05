@echo off
cd /d "%~dp0"
echo ============================================================
echo   CareerForge - building portable executable
echo ============================================================
echo.

set "PY=python"
where python >nul 2>&1
if errorlevel 1 (
  where py >nul 2>&1
  if errorlevel 1 (
    echo ERROR: Python is not installed on this machine.
    echo Install Python 3.9+ from https://www.python.org/downloads/
    echo During install, tick "Add python.exe to PATH", then run this again.
    echo PYTHON_MISSING> "%~dp0BUILD_STATUS.txt"
    echo.
    pause
    exit /b 1
  ) else (
    set "PY=py"
  )
)

echo Using interpreter: %PY%
echo BUILDING> "%~dp0BUILD_STATUS.txt"
echo.
echo Installing Flask + PyInstaller (one-time)...
%PY% -m pip install --upgrade pip
%PY% -m pip install flask pyinstaller
echo.
echo Packaging the portable executable...
%PY% -m PyInstaller --onefile --name CareerForge --add-data "templates;templates" --collect-all flask launcher.py

if exist "%~dp0dist\CareerForge.exe" (
  echo BUILD_OK> "%~dp0BUILD_STATUS.txt"
  echo.
  echo ============================================================
  echo   SUCCESS  ^|  Your portable app:  dist\CareerForge.exe
  echo   Double-click it to launch - no Python needed to run.
  echo ============================================================
) else (
  echo BUILD_FAILED> "%~dp0BUILD_STATUS.txt"
  echo.
  echo Build did not produce the .exe - see the messages above.
)
echo.
pause
