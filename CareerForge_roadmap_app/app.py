"""
CareerForge - IT Career Roadmap Generator
A premium web UI that turns an IT role into a chronological, hire-focused roadmap
of certifications, labs and experience - rendered as a live workflow infographic.

Run:
    pip install flask
    python app.py
Then open http://127.0.0.1:5000 in your browser.
"""

from flask import Flask, jsonify, render_template, request

from roadmaps import match_roadmap, list_roles
from languages import list_language_groups, build_language_roadmap

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", roles=list_roles(), lang_groups=list_language_groups())


@app.route("/api/roadmap")
def api_roadmap():
    role = request.args.get("role", "")
    roadmap, key, confidence = match_roadmap(role)
    return jsonify({
        "query": role,
        "matched_key": key,
        "confidence": confidence,
        "roadmap": roadmap,
    })


@app.route("/api/language")
def api_language():
    name = request.args.get("name", "")
    rm = build_language_roadmap(name)
    return jsonify({"query": name, "matched_key": name, "confidence": 1.0, "roadmap": rm})


@app.route("/api/roles")
def api_roles():
    return jsonify(list_roles())


if __name__ == "__main__":
    print("\n  CareerForge running -> http://127.0.0.1:5000\n")
    app.run(debug=True, port=5000)
