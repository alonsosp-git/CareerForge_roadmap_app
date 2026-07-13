#!/usr/bin/env bash
cd "$(dirname "$0")"
python3 -m pip install flask --quiet
python3 launcher.py
