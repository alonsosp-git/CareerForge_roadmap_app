# CareerForge - IT Career Roadmap Generator
CareerForge  a premium Flask web app that turns any IT role into a chronological, hire-focused career roadmap, rendered as a live workflow infographic with top certifications, hands-on labs, and real experience. Exports to a standalone HTML report and a portable .exe.

<img width="904" height="883" alt="01-CareerForge" src="https://github.com/user-attachments/assets/33f0bed0-a55b-40bc-8782-fb9aa53e78f3" />



<img width="951" height="2978" alt="02-CareerForge" src="https://github.com/user-attachments/assets/d9ad950f-9ed2-4a0c-b2cd-84d009749207" />


Or by Programming Language
<img width="905" height="1406" alt="03-CareerForge" src="https://github.com/user-attachments/assets/de194b9e-4810-4e45-a384-98292d538bfe" />



# CareerForge — IT Career Roadmap Generator

A premium Python/Flask web app. Type an IT role **or** pick a language/technology
and it builds a chronological workflow infographic of exactly what to learn — top
certifications, hands-on labs, and real experience — with clickable links at every step.

## What it does
- Type any IT role (or click a suggested role) to get a get-hired roadmap.
- Or open the language / technology picker and choose from 81 technologies.
- A node-and-arrow workflow, colour-coded stages in chronological order
  (foundation → education → certification → lab → experience → target).
- Every certification, course, lab and project links to its official page.
- Export to HTML report — a self-contained file anyone can open on any computer, offline.
- Where a matching roadmap.sh roadmap exists, roles and technologies also link to it
  for an interactive roadmap and project ideas (basic → advanced).

## Job roadmaps (15)
IT / Technical Project Manager, IT Manager (people-leadership / non-IC),
Data Engineer, Cybersecurity Engineer, Solutions Architect,
DevOps / Cloud Engineer, Full Stack Developer, Frontend Developer,
Backend Developer, Artificial Intelligence Engineer, Python Developer,
Data Scientist / ML Engineer, Software Engineer, IT Business Analyst,
Network Engineer.
Only recruiter-recognised credentials — no filler. Any other role falls back to a
general framework.

## Language / technology paths (81)
8 categories, sorted by market popularity, with a colour-coded popularity badge on
every item (Very High → Emerging): Languages (general-purpose), Web / app frameworks,
Data / AI / ML, Data stores / query, DevOps / cloud / tooling, Web markup / styling,
Blockchain / smart contracts, Other. Each path: Setup → Core → Practice → Build → Proficient,
linking to official docs, a deeper tutorial, and (where supported) an Exercism track.

## Run it (pick one)  — needs Python 3.9+
Just run it:
    pip install -r requirements.txt
    python app.py            # then open http://127.0.0.1:5000
or double-click Run_CareerForge.bat (Windows) / run_careerforge.sh (Mac/Linux).

Make a portable executable (runs with no Python afterward):
    Windows: double-click build_exe.bat   ->  dist\CareerForge.exe
    Mac/Lin: ./build_exe.sh               ->  dist/CareerForge

## Notes
Salary figures are US-market estimates. Popularity tiers are grounded in the
Stack Overflow Developer Survey, TIOBE, GitHub Octoverse, and hiring demand.
Roadmaps are served instantly from curated data (offline, no API keys, no cost).


