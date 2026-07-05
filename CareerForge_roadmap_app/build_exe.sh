#!/usr/bin/env bash
# Builds a portable CareerForge binary for macOS/Linux.
set -e
python3 -m pip install --upgrade pip
python3 -m pip install flask pyinstaller
python3 -m PyInstaller --onefile --name CareerForge \
  --add-data "templates:templates" --collect-all flask launcher.py
echo "Done -> dist/CareerForge"
