# CareerForge — IT Career Roadmap Generator
CareerForge  a premium Flask web app that turns any IT role into a chronological, hire-focused career roadmap, rendered as a live workflow infographic with top certifications, hands-on labs, and real experience. Exports to a standalone HTML report and a portable .exe.

<img width="694" height="623" alt="01-CareerForge" src="https://github.com/user-attachments/assets/11d14841-0509-4559-98f4-d07463b98566" />

<img width="918" height="2329" alt="02-CareerForge" src="https://github.com/user-attachments/assets/98393c2c-066a-45c8-ac48-f4cfbf573e3b" />



# CareerForge — IT Career Roadmap Generator

A premium Python/Flask web app. Type an IT role and it builds a **chronological
workflow infographic** of the top certifications, hands-on labs, and real
experience that actually get you hired — with clickable links at every step.

## What it does

- Type any IT role (or click a suggestion chip).
- Watch a live "researching the market → building roadmap" animation.
- Get a node-and-arrow workflow: rectangles connected in chronological order,
  colour-coded by stage (foundation → education → certification → lab →
  experience → target role).
- Every certification, course, lab and project links to its official URL
  (opens in a new tab).
- Print / Save-as-PDF and Replay-build buttons included.

Roadmaps are **hand-curated** to include only recruiter-recognised credentials —
no filler certs. Built-in expert paths cover:

Project Manager · Data Engineer · Cybersecurity Engineer · Solutions Architect ·
DevOps / Cloud Engineer · Data Scientist / ML Engineer · Software Engineer ·
IT Business Analyst · Network Engineer

Any other role you type falls back to a sensible general framework.

## Run it

You need Python 3.9+.

```bash
cd roadmap_app
pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Files

```
roadmap_app/
├── app.py              # Flask server + JSON API
├── roadmaps.py         # Curated roadmap database + fuzzy role matching
├── requirements.txt
├── templates/
│   └── index.html      # The premium animated single-page UI
└── README.md
```

## How to extend it

Add or edit roles in `roadmaps.py` → the `ROADMAPS` dict. Each role has
`keywords` (used for fuzzy matching) and an ordered list of `stages`. Each stage
has a `kind` (drives colour/icon) and `items` with optional `url`s. No frontend
changes needed — the UI renders whatever the API returns.

## Notes

- Salary figures are US-market estimates; they vary by region and seniority.
- The "market scanning" animation is a UX flourish; roadmaps are served instantly
  from the curated database (works fully offline, no API keys, no cost).
<img width="694" height="623" alt="01-CareerForge" src="https://github.com/user-attachments/assets/f1f2e808-3ab3-4540-926f-36f0e8b603e9" />
<img width="694" height="623" alt="01-CareerForge" src="https://github.com/user-attachments/assets/b7c7cbbb-1f76-4e6e-b52d-676c334da15f" />
