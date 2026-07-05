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

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", roles=list_roles())


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


@app.route("/api/roles")
def api_roles():
    return jsonify(list_roles())


if __name__ == "__main__":
    print("\n  CareerForge running -> http://127.0.0.1:5000\n")
    app.run(debug=True, port=5000)
