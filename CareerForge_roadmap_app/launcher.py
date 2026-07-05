"""
CareerForge portable launcher.

This is the entry point used to build the standalone .exe with PyInstaller.
It starts the Flask server and automatically opens the app in your browser.
The rest of the app (app.py, roadmaps.py, templates/) is reused unchanged.
"""
import os
import sys
import time
import threading
import webbrowser

import jinja2


def resource_path(rel):
    """Locate bundled files whether running from source or a PyInstaller .exe."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel)


# Import the existing Flask app unchanged, then point its template loader at the
# bundled templates folder so it works inside the packaged executable.
from app import app  # noqa: E402

app.jinja_loader = jinja2.FileSystemLoader(resource_path("templates"))

HOST = "127.0.0.1"
PORT = 5000
URL = f"http://{HOST}:{PORT}"


def open_browser():
    time.sleep(1.3)
    try:
        webbrowser.open(URL)
    except Exception:
        pass


if __name__ == "__main__":
    print("=" * 52)
    print("  CareerForge - IT Career Roadmap Generator")
    print(f"  Running at: {URL}")
    print("  Your browser will open automatically.")
    print("  Close this window to stop the app.")
    print("=" * 52)
    threading.Thread(target=open_browser, daemon=True).start()
    # No debug/reloader: the reloader spawns a subprocess that breaks when frozen.
    app.run(host=HOST, port=PORT, debug=False, use_reloader=False)
