"""
Expert-curated IT career roadmaps.

Each roadmap is a chronological sequence of "stages". A stage represents a phase
in the journey to qualify for the target role. Stage kinds drive the colour/icon
in the UI:
    foundation   - core knowledge to build first
    education     - structured learning / degree-equivalent skills
    certification - ONLY recruiter-recognised, hiring-relevant certs
    lab           - hands-on labs / practice platforms
    experience    - portfolio projects & real-world experience to gain
    role          - the target job (final node)

Every item that has a credible official URL includes one so the UI can render it
as a clickable link.

This data is hand-curated to exclude "garbage" certs and filler courses. Only the
credentials and practice that recruiters and hiring managers actually look for are
included.
"""

import re
from difflib import SequenceMatcher

# ---------------------------------------------------------------------------
# Roadmap definitions
# ---------------------------------------------------------------------------

ROADMAPS = {

    # ===================================================================
    "project_manager": {
        "title": "IT / Technical Project Manager",
        "tagline": "Lead delivery of technology projects on time, on scope, on budget.",
        "salary": "$95k - $145k (US median ~$115k)",
        "duration": "9 - 15 months",
        "demand": "High",
        "keywords": ["project manager", "pm", "technical project manager", "it project manager",
                     "program manager", "delivery manager", "scrum master", "project management"],
        "stages": [
            {
                "kind": "foundation",
                "phase": "Phase 1 - Foundations",
                "timeframe": "Months 1-2",
                "title": "Project management fundamentals",
                "blurb": "Learn the language of delivery: scope, schedule, budget, risk, stakeholders.",
                "items": [
                    {"name": "Google Project Management Professional Certificate", "type": "education",
                     "url": "https://www.coursera.org/professional-certificates/google-project-management",
                     "detail": "Best beginner-to-job program; covers Agile + Waterfall end-to-end."},
                    {"name": "PMI's 'PMBOK Guide' (7th ed.) core concepts", "type": "skill",
                     "url": "https://www.pmi.org/pmbok-guide-standards",
                     "detail": "Reference standard recruiters expect you to know."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 2 - Entry credential",
                "timeframe": "Months 2-4",
                "title": "CAPM or PSM I",
                "blurb": "An entry-level cert that clears resume filters before you have 3 years' experience.",
                "items": [
                    {"name": "CAPM - Certified Associate in Project Management", "type": "certification",
                     "url": "https://www.pmi.org/certifications/certified-associate-capm",
                     "detail": "PMI's entry cert; no experience required. Strong recruiter signal."},
                    {"name": "PSM I - Professional Scrum Master", "type": "certification",
                     "url": "https://www.scrum.org/professional-scrum-master-i-certification",
                     "detail": "Cheaper, lifetime-valid Agile credential. Highly searched by recruiters."},
                ],
            },
            {
                "kind": "lab",
                "phase": "Phase 3 - Tooling & practice",
                "timeframe": "Months 3-6",
                "title": "Master the PM tool stack",
                "blurb": "Run mock projects in the tools real teams use. Build artifacts you can show.",
                "items": [
                    {"name": "Jira (Atlassian) - boards, sprints, roadmaps", "type": "lab",
                     "url": "https://university.atlassian.com/student/catalog",
                     "detail": "Free Atlassian University paths + a free Jira cloud site."},
                    {"name": "Build a full project plan in MS Project / Smartsheet", "type": "lab",
                     "url": "https://www.smartsheet.com/",
                     "detail": "Produce a real Gantt chart, RAID log, and status report."},
                ],
            },
            {
                "kind": "experience",
                "phase": "Phase 4 - Real experience",
                "timeframe": "Months 4-9",
                "title": "Lead a real project end-to-end",
                "blurb": "Recruiters hire on demonstrated delivery, not theory. Get logged hours.",
                "items": [
                    {"name": "Volunteer to lead a project (non-profit / internal)", "type": "experience",
                     "url": "https://www.catchafire.org/",
                     "detail": "Catchafire matches volunteers to real org projects you can manage."},
                    {"name": "Log 1,500+ leading/directing hours toward PMP eligibility", "type": "experience",
                     "url": "https://www.pmi.org/certifications/project-management-pmp",
                     "detail": "Track every project; you'll need the hours for the flagship cert."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 5 - Flagship credential",
                "timeframe": "Months 9-15",
                "title": "PMP - the recruiter gold standard",
                "blurb": "The single most requested PM credential in job postings worldwide.",
                "items": [
                    {"name": "PMP - Project Management Professional", "type": "certification",
                     "url": "https://www.pmi.org/certifications/project-management-pmp",
                     "detail": "Requires 36 months experience + 35 contact hours. The credential that gets interviews."},
                    {"name": "(Optional) PMI-ACP for Agile-heavy orgs", "type": "certification",
                     "url": "https://www.pmi.org/certifications/agile-acp",
                     "detail": "Add only if targeting Agile/Scrum-first companies."},
                ],
            },
            {
                "kind": "role",
                "phase": "Goal",
                "timeframe": "Apply now",
                "title": "IT / Technical Project Manager",
                "blurb": "You now have the credentials, tools, and delivery track record recruiters screen for.",
                "items": [],
            },
        ],
    },

    # ===================================================================
    "data_engineer": {
        "title": "Data Engineer",
        "tagline": "Build the pipelines and platforms that move and shape data at scale.",
        "salary": "$110k - $170k (US median ~$130k)",
        "duration": "12 - 18 months",
        "demand": "Very High",
        "keywords": ["data engineer", "data engineering", "etl", "pipeline", "data platform",
                     "analytics engineer", "big data engineer"],
        "stages": [
            {
                "kind": "foundation",
                "phase": "Phase 1 - Foundations",
                "timeframe": "Months 1-3",
                "title": "SQL, Python & data modeling",
                "blurb": "Non-negotiable core. Every data-engineer interview tests these hard.",
                "items": [
                    {"name": "Advanced SQL (window functions, CTEs, optimization)", "type": "skill",
                     "url": "https://mode.com/sql-tutorial/",
                     "detail": "Mode's SQL tutorial then grind StrataScratch / DataLemur."},
                    {"name": "Python for data (pandas, requests, OOP basics)", "type": "skill",
                     "url": "https://www.kaggle.com/learn/python",
                     "detail": "Free Kaggle micro-courses; fastest path to fluency."},
                    {"name": "Dimensional modeling (Kimball star schemas)", "type": "skill",
                     "url": "https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/",
                     "detail": "Star/snowflake schemas are core interview material."},
                ],
            },
            {
                "kind": "education",
                "phase": "Phase 2 - The modern data stack",
                "timeframe": "Months 3-6",
                "title": "Pipelines, orchestration & transformation",
                "blurb": "Learn the tools that appear in 90% of data-engineer job descriptions.",
                "items": [
                    {"name": "Apache Spark (PySpark)", "type": "skill",
                     "url": "https://spark.apache.org/docs/latest/api/python/getting_started/index.html",
                     "detail": "Distributed processing - the workhorse of big-data roles."},
                    {"name": "Apache Airflow orchestration", "type": "skill",
                     "url": "https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html",
                     "detail": "Schedule & monitor pipelines; appears constantly in postings."},
                    {"name": "dbt (data build tool)", "type": "skill",
                     "url": "https://courses.getdbt.com/courses/fundamentals",
                     "detail": "Free dbt Fundamentals course - the modern transformation standard."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 3 - Cloud certification",
                "timeframe": "Months 6-10",
                "title": "Pick ONE cloud and certify",
                "blurb": "Recruiters filter on cloud certs. One strong cert beats three weak ones.",
                "items": [
                    {"name": "AWS Certified Data Engineer - Associate", "type": "certification",
                     "url": "https://aws.amazon.com/certification/certified-data-engineer-associate/",
                     "detail": "AWS dominates the market; this is the top data-engineer cert."},
                    {"name": "Google Professional Data Engineer", "type": "certification",
                     "url": "https://cloud.google.com/learn/certification/data-engineer",
                     "detail": "Choose if targeting GCP shops; very well respected."},
                    {"name": "Microsoft DP-700: Fabric Data Engineer", "type": "certification",
                     "url": "https://learn.microsoft.com/en-us/credentials/certifications/fabric-data-engineer-associate/",
                     "detail": "Choose for Azure/Microsoft-stack employers."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 4 - Platform credential",
                "timeframe": "Months 9-12",
                "title": "Snowflake or Databricks",
                "blurb": "A platform cert proves you can ship on the warehouse/lakehouse employers run.",
                "items": [
                    {"name": "SnowPro Core Certification", "type": "certification",
                     "url": "https://www.snowflake.com/en/certifications/",
                     "detail": "Snowflake is everywhere; SnowPro Core is recruiter-recognised."},
                    {"name": "Databricks Certified Data Engineer Associate", "type": "certification",
                     "url": "https://www.databricks.com/learn/certification/data-engineer-associate",
                     "detail": "Lakehouse / Spark-first orgs love this credential."},
                ],
            },
            {
                "kind": "experience",
                "phase": "Phase 5 - Portfolio & practice",
                "timeframe": "Months 8-18",
                "title": "Ship 2-3 end-to-end pipelines",
                "blurb": "A public portfolio of real pipelines is what converts interviews to offers.",
                "items": [
                    {"name": "Build a batch + streaming pipeline (ingest->warehouse->dashboard)", "type": "experience",
                     "url": "https://github.com/DataExpert-io/data-engineer-handbook",
                     "detail": "Free community handbook + project ideas, by Zach Wilson."},
                    {"name": "Data Engineering Zoomcamp (free, project-based)", "type": "lab",
                     "url": "https://github.com/DataTalksClub/data-engineering-zoomcamp",
                     "detail": "Full hands-on bootcamp with a capstone you can show recruiters."},
                ],
            },
            {
                "kind": "role",
                "phase": "Goal",
                "timeframe": "Apply now",
                "title": "Data Engineer",
                "blurb": "Strong fundamentals, a cloud + platform cert, and a real pipeline portfolio.",
                "items": [],
            },
        ],
    },

    # ===================================================================
    "cybersecurity_engineer": {
        "title": "Cybersecurity Engineer",
        "tagline": "Defend systems, networks and data against attackers.",
        "salary": "$105k - $165k (US median ~$130k)",
        "duration": "12 - 24 months",
        "demand": "Very High",
        "keywords": ["cyber security", "cybersecurity", "security engineer", "infosec", "soc analyst",
                     "penetration tester", "pentester", "blue team", "security analyst", "cyber"],
        "stages": [
            {
                "kind": "foundation",
                "phase": "Phase 1 - Foundations",
                "timeframe": "Months 1-3",
                "title": "Networking, OS & scripting",
                "blurb": "You can't secure what you don't understand. Build IT bedrock first.",
                "items": [
                    {"name": "Networking fundamentals (TCP/IP, DNS, HTTP, subnetting)", "type": "skill",
                     "url": "https://www.professormesser.com/network-plus/n10-009/n10-009-training-course/",
                     "detail": "Professor Messer's free Network+ course is the gold reference."},
                    {"name": "Linux + Windows administration", "type": "skill",
                     "url": "https://linuxjourney.com/",
                     "detail": "Comfort on the command line is mandatory for security work."},
                    {"name": "Python / Bash scripting for automation", "type": "skill",
                     "url": "https://tryhackme.com/",
                     "detail": "Automate recon and parsing; TryHackMe has guided rooms."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 2 - Entry certs",
                "timeframe": "Months 3-6",
                "title": "Security+ (and Network+)",
                "blurb": "CompTIA Security+ is the #1 cert recruiters require for entry security roles.",
                "items": [
                    {"name": "CompTIA Security+ (SY0-701)", "type": "certification",
                     "url": "https://www.comptia.org/certifications/security",
                     "detail": "The baseline. DoD-approved and demanded in nearly every junior posting."},
                    {"name": "CompTIA Network+ (optional precursor)", "type": "certification",
                     "url": "https://www.comptia.org/certifications/network",
                     "detail": "Add if your networking foundation is weak."},
                ],
            },
            {
                "kind": "lab",
                "phase": "Phase 3 - Hands-on labs",
                "timeframe": "Months 4-9",
                "title": "Practice on real attack/defense ranges",
                "blurb": "Security is a hands-on field. Labs prove skill where certs prove knowledge.",
                "items": [
                    {"name": "TryHackMe - Cyber Security 101 & SOC paths", "type": "lab",
                     "url": "https://tryhackme.com/paths",
                     "detail": "Guided, beginner-friendly; great for blue-team fundamentals."},
                    {"name": "Hack The Box Academy", "type": "lab",
                     "url": "https://academy.hackthebox.com/",
                     "detail": "Deeper offensive practice; build toward OSCP-style skills."},
                    {"name": "Build a home SOC lab (Splunk/ELK + Sysmon)", "type": "lab",
                     "url": "https://github.com/clong/DetectionLab",
                     "detail": "DetectionLab spins up a full monitored network to defend."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 4 - Specialize",
                "timeframe": "Months 9-15",
                "title": "Blue-team or red-team credential",
                "blurb": "Pick a lane. These certs separate you from the Security+-only crowd.",
                "items": [
                    {"name": "CompTIA CySA+ (defensive / SOC analyst)", "type": "certification",
                     "url": "https://www.comptia.org/certifications/cybersecurity-analyst",
                     "detail": "Blue-team path: threat detection & incident response."},
                    {"name": "OSCP - Offensive Security Certified Professional", "type": "certification",
                     "url": "https://www.offsec.com/courses/pen-200/",
                     "detail": "Red-team path: the most respected hands-on pentest cert."},
                    {"name": "GIAC GCIH - Incident Handler", "type": "certification",
                     "url": "https://www.giac.org/certifications/certified-incident-handler-gcih/",
                     "detail": "Premium DFIR credential valued by SOC/IR teams."},
                ],
            },
            {
                "kind": "experience",
                "phase": "Phase 5 - Experience & profile",
                "timeframe": "Months 6-24",
                "title": "Get logged hours & public proof",
                "blurb": "An IT/SOC support role + a public skills profile beats a wall of certs alone.",
                "items": [
                    {"name": "Start in IT support or a SOC Tier-1 role", "type": "experience",
                     "url": "https://www.cyberseek.org/pathway.html",
                     "detail": "CyberSeek maps realistic entry roles that feed into security engineering."},
                    {"name": "Capture-the-Flag competitions + writeups", "type": "experience",
                     "url": "https://ctftime.org/",
                     "detail": "Public CTF writeups are strong, recruiter-visible signals."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 6 - Senior credential",
                "timeframe": "Months 18-24+",
                "title": "CISSP - the management gold standard",
                "blurb": "The most requested senior security cert. Needs 5 years' experience.",
                "items": [
                    {"name": "CISSP - (ISC)2 Certified Information Systems Security Professional", "type": "certification",
                     "url": "https://www.isc2.org/certifications/cissp",
                     "detail": "Unlocks senior/lead roles. Pass earlier as an Associate of (ISC)2."},
                ],
            },
            {
                "kind": "role",
                "phase": "Goal",
                "timeframe": "Apply now",
                "title": "Cybersecurity Engineer",
                "blurb": "Foundations, Security+, real labs, a specialization cert, and hands-on experience.",
                "items": [],
            },
        ],
    },

    # ===================================================================
    "solutions_architect": {
        "title": "Solutions Architect",
        "tagline": "Design scalable, secure systems that solve real business problems.",
        "salary": "$130k - $200k+ (US median ~$155k)",
        "duration": "18 - 30 months",
        "demand": "High",
        "keywords": ["solutions architect", "solution architect", "cloud architect", "enterprise architect",
                     "systems architect", "technical architect", "architect"],
        "stages": [
            {
                "kind": "foundation",
                "phase": "Phase 1 - Engineering base",
                "timeframe": "Prerequisite",
                "title": "Be a strong engineer first",
                "blurb": "Architecture is built on real delivery experience. Earn this before the rest.",
                "items": [
                    {"name": "3-5 years as a software/cloud/infra engineer", "type": "experience",
                     "url": "https://aws.amazon.com/architecture/",
                     "detail": "Architects are senior. Study the AWS Architecture Center patterns."},
                    {"name": "Programming + one cloud + networking fundamentals", "type": "skill",
                     "url": "https://roadmap.sh/software-architect",
                     "detail": "roadmap.sh's architect track maps the underlying skills."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 2 - Associate cloud cert",
                "timeframe": "Months 1-4",
                "title": "Cloud Architect - Associate",
                "blurb": "Prove cloud design fluency on the platform employers run.",
                "items": [
                    {"name": "AWS Certified Solutions Architect - Associate (SAA-C03)", "type": "certification",
                     "url": "https://aws.amazon.com/certification/certified-solutions-architect-associate/",
                     "detail": "The single most recognised architecture cert in the market."},
                    {"name": "Microsoft AZ-305: Azure Solutions Architect Expert", "type": "certification",
                     "url": "https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/",
                     "detail": "Choose for Azure/enterprise-Microsoft employers."},
                    {"name": "Google Professional Cloud Architect", "type": "certification",
                     "url": "https://cloud.google.com/learn/certification/cloud-architect",
                     "detail": "Choose for GCP-first companies; consistently rated top-paying."},
                ],
            },
            {
                "kind": "education",
                "phase": "Phase 3 - Architecture craft",
                "timeframe": "Months 3-9",
                "title": "System design & well-architected thinking",
                "blurb": "Move from building components to designing whole systems with tradeoffs.",
                "items": [
                    {"name": "AWS Well-Architected Framework", "type": "skill",
                     "url": "https://aws.amazon.com/architecture/well-architected/",
                     "detail": "The 6 pillars are interview and on-the-job gospel."},
                    {"name": "System Design (scalability, caching, queues, CAP)", "type": "skill",
                     "url": "https://github.com/donnemartin/system-design-primer",
                     "detail": "The System Design Primer - the standard free study resource."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 4 - Professional cert",
                "timeframe": "Months 9-15",
                "title": "Cloud Architect - Professional",
                "blurb": "The advanced cert that signals you can design enterprise-grade systems.",
                "items": [
                    {"name": "AWS Certified Solutions Architect - Professional (SAP-C02)", "type": "certification",
                     "url": "https://aws.amazon.com/certification/certified-solutions-architect-professional/",
                     "detail": "Heavyweight credential; strongly differentiates senior candidates."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 5 - Enterprise framework",
                "timeframe": "Months 12-24",
                "title": "TOGAF (for enterprise architect tracks)",
                "blurb": "Add when targeting enterprise architecture / large organisations.",
                "items": [
                    {"name": "TOGAF Enterprise Architecture (Foundation + Practitioner)", "type": "certification",
                     "url": "https://www.opengroup.org/togaf",
                     "detail": "The de-facto enterprise-architecture standard for big employers."},
                ],
            },
            {
                "kind": "experience",
                "phase": "Phase 6 - Lead real designs",
                "timeframe": "Ongoing",
                "title": "Own architecture decisions",
                "blurb": "Document real designs and tradeoffs you've led - this is what panels probe.",
                "items": [
                    {"name": "Author Architecture Decision Records (ADRs) on real projects", "type": "experience",
                     "url": "https://adr.github.io/",
                     "detail": "A portfolio of ADRs proves architectural judgement to interviewers."},
                    {"name": "Lead a cross-team design + present to stakeholders", "type": "experience",
                     "url": "https://aws.amazon.com/architecture/",
                     "detail": "Communication and stakeholder buy-in are core architect skills."},
                ],
            },
            {
                "kind": "role",
                "phase": "Goal",
                "timeframe": "Apply now",
                "title": "Solutions Architect",
                "blurb": "Senior engineering base + pro-level cloud cert + proven system-design leadership.",
                "items": [],
            },
        ],
    },

    # ===================================================================
    "devops_engineer": {
        "title": "DevOps / Cloud Engineer",
        "tagline": "Automate, ship and run reliable infrastructure at scale.",
        "salary": "$110k - $175k (US median ~$135k)",
        "duration": "12 - 18 months",
        "demand": "Very High",
        "keywords": ["devops", "cloud engineer", "sre", "site reliability", "platform engineer",
                     "infrastructure engineer", "ci/cd", "kubernetes"],
        "stages": [
            {
                "kind": "foundation",
                "phase": "Phase 1 - Foundations",
                "timeframe": "Months 1-3",
                "title": "Linux, networking & scripting",
                "blurb": "DevOps lives on the command line. Get fluent before the fancy tools.",
                "items": [
                    {"name": "Linux administration + Bash", "type": "skill",
                     "url": "https://linuxjourney.com/",
                     "detail": "You'll automate everything from the shell - master it."},
                    {"name": "Git & GitHub workflows", "type": "skill",
                     "url": "https://learngitbranching.js.org/",
                     "detail": "Branching, PRs and CI triggers are daily DevOps work."},
                    {"name": "Python or Go for tooling", "type": "skill",
                     "url": "https://gobyexample.com/",
                     "detail": "Glue, operators and tooling are written in Python/Go."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 2 - Cloud cert",
                "timeframe": "Months 3-6",
                "title": "Cloud Associate certification",
                "blurb": "Cloud is the platform of DevOps. Certify on the one employers use.",
                "items": [
                    {"name": "AWS Certified Solutions Architect - Associate", "type": "certification",
                     "url": "https://aws.amazon.com/certification/certified-solutions-architect-associate/",
                     "detail": "Broadest cloud cert; covers the services you'll automate."},
                    {"name": "Microsoft AZ-104: Azure Administrator", "type": "certification",
                     "url": "https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/",
                     "detail": "Choose for Azure shops."},
                ],
            },
            {
                "kind": "education",
                "phase": "Phase 3 - The DevOps toolchain",
                "timeframe": "Months 4-9",
                "title": "Containers, IaC & CI/CD",
                "blurb": "The three pillars in nearly every DevOps job description.",
                "items": [
                    {"name": "Docker + Kubernetes", "type": "skill",
                     "url": "https://kubernetes.io/docs/tutorials/kubernetes-basics/",
                     "detail": "Containers and orchestration are table stakes."},
                    {"name": "Terraform (Infrastructure as Code)", "type": "skill",
                     "url": "https://developer.hashicorp.com/terraform/tutorials",
                     "detail": "The dominant IaC tool; HashiCorp's tutorials are excellent."},
                    {"name": "CI/CD (GitHub Actions / GitLab CI / Jenkins)", "type": "skill",
                     "url": "https://docs.github.com/en/actions",
                     "detail": "Build automated build->test->deploy pipelines."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 4 - Specialist certs",
                "timeframe": "Months 9-14",
                "title": "Kubernetes & Terraform credentials",
                "blurb": "These specialist certs are heavily searched and prove hands-on depth.",
                "items": [
                    {"name": "CKA - Certified Kubernetes Administrator", "type": "certification",
                     "url": "https://www.cncf.io/training/certification/cka/",
                     "detail": "Hands-on, performance-based; the K8s credential recruiters trust."},
                    {"name": "HashiCorp Certified: Terraform Associate", "type": "certification",
                     "url": "https://developer.hashicorp.com/certifications/infrastructure-automation",
                     "detail": "Validates IaC skills; common in DevOps postings."},
                ],
            },
            {
                "kind": "experience",
                "phase": "Phase 5 - Build & run",
                "timeframe": "Months 6-18",
                "title": "Ship a real platform project",
                "blurb": "A public repo that provisions + deploys an app end-to-end seals the deal.",
                "items": [
                    {"name": "IaC + CI/CD a full app to the cloud (public GitHub)", "type": "experience",
                     "url": "https://roadmap.sh/devops",
                     "detail": "Follow roadmap.sh/devops and build the capstone in public."},
                    {"name": "Set up monitoring/alerting (Prometheus + Grafana)", "type": "lab",
                     "url": "https://prometheus.io/docs/introduction/overview/",
                     "detail": "Observability separates real DevOps engineers from scripters."},
                ],
            },
            {
                "kind": "role",
                "phase": "Goal",
                "timeframe": "Apply now",
                "title": "DevOps / Cloud Engineer",
                "blurb": "Linux + cloud cert + container/IaC/CI-CD mastery + a public platform project.",
                "items": [],
            },
        ],
    },

    # ===================================================================
    "data_scientist": {
        "title": "Data Scientist / ML Engineer",
        "tagline": "Turn data into models and decisions that move the business.",
        "salary": "$115k - $180k (US median ~$140k)",
        "duration": "12 - 20 months",
        "demand": "High",
        "keywords": ["data scientist", "machine learning", "ml engineer", "ai engineer",
                     "data science", "ml", "ai"],
        "stages": [
            {
                "kind": "foundation",
                "phase": "Phase 1 - Math & coding base",
                "timeframe": "Months 1-4",
                "title": "Python, statistics & linear algebra",
                "blurb": "Data science rests on stats + code. Skip the hype, build the base.",
                "items": [
                    {"name": "Python + pandas + NumPy", "type": "skill",
                     "url": "https://www.kaggle.com/learn",
                     "detail": "Kaggle Learn micro-courses are the fastest practical start."},
                    {"name": "Statistics & probability", "type": "skill",
                     "url": "https://www.khanacademy.org/math/statistics-probability",
                     "detail": "Hypothesis testing, distributions, inference - interview staples."},
                    {"name": "Linear algebra & calculus intuition", "type": "skill",
                     "url": "https://www.3blue1brown.com/topics/linear-algebra",
                     "detail": "3Blue1Brown builds the intuition ML depends on."},
                ],
            },
            {
                "kind": "education",
                "phase": "Phase 2 - Core machine learning",
                "timeframe": "Months 4-8",
                "title": "ML algorithms & workflow",
                "blurb": "Learn the models, evaluation, and the end-to-end ML workflow properly.",
                "items": [
                    {"name": "Andrew Ng - Machine Learning Specialization", "type": "education",
                     "url": "https://www.coursera.org/specializations/machine-learning-introduction",
                     "detail": "The canonical ML course recruiters recognise instantly."},
                    {"name": "scikit-learn end-to-end projects", "type": "skill",
                     "url": "https://scikit-learn.org/stable/tutorial/index.html",
                     "detail": "Feature engineering -> model -> evaluation pipelines."},
                ],
            },
            {
                "kind": "education",
                "phase": "Phase 3 - Deep learning",
                "timeframe": "Months 8-12",
                "title": "Neural networks & modern AI",
                "blurb": "Add deep learning to be competitive for ML/AI engineering roles.",
                "items": [
                    {"name": "DeepLearning.AI Deep Learning Specialization", "type": "education",
                     "url": "https://www.coursera.org/specializations/deep-learning",
                     "detail": "Builds CNNs, RNNs, transformers from the ground up."},
                    {"name": "PyTorch hands-on", "type": "skill",
                     "url": "https://pytorch.org/tutorials/beginner/basics/intro.html",
                     "detail": "PyTorch is the research + industry standard framework."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 4 - Cloud ML cert (optional but valued)",
                "timeframe": "Months 10-14",
                "title": "Productionizing ML",
                "blurb": "Companies hire scientists who can ship. A cloud-ML cert proves it.",
                "items": [
                    {"name": "AWS Certified Machine Learning - Specialty", "type": "certification",
                     "url": "https://aws.amazon.com/certification/certified-machine-learning-specialty/",
                     "detail": "Validates building/deploying ML on the dominant cloud."},
                    {"name": "Google Professional ML Engineer", "type": "certification",
                     "url": "https://cloud.google.com/learn/certification/machine-learning-engineer",
                     "detail": "Choose for GCP/Vertex AI environments."},
                ],
            },
            {
                "kind": "experience",
                "phase": "Phase 5 - Portfolio & competitions",
                "timeframe": "Months 6-20",
                "title": "Build a visible track record",
                "blurb": "Public, end-to-end projects with real data beat any certificate here.",
                "items": [
                    {"name": "3-4 end-to-end projects on GitHub (with deployment)", "type": "experience",
                     "url": "https://github.com/",
                     "detail": "Problem -> data -> model -> deployed app -> writeup."},
                    {"name": "Kaggle competitions (aim for top-tier finishes)", "type": "lab",
                     "url": "https://www.kaggle.com/competitions",
                     "detail": "A strong Kaggle profile is a recruiter magnet."},
                ],
            },
            {
                "kind": "role",
                "phase": "Goal",
                "timeframe": "Apply now",
                "title": "Data Scientist / ML Engineer",
                "blurb": "Solid math + ML + deep learning, a cloud-ML cert, and a deployed-project portfolio.",
                "items": [],
            },
        ],
    },

    # ===================================================================
    "software_engineer": {
        "title": "Software Engineer",
        "tagline": "Design, build and ship the applications businesses run on.",
        "salary": "$100k - $170k (US median ~$130k)",
        "duration": "9 - 18 months",
        "demand": "Very High",
        "keywords": ["software engineer", "developer", "programmer", "full stack", "backend",
                     "frontend", "web developer", "software developer", "swe"],
        "stages": [
            {
                "kind": "foundation",
                "phase": "Phase 1 - Programming foundations",
                "timeframe": "Months 1-4",
                "title": "One language + CS fundamentals",
                "blurb": "Depth in one language beats shallow exposure to five.",
                "items": [
                    {"name": "Master one language (Python / JavaScript / Java)", "type": "skill",
                     "url": "https://cs50.harvard.edu/x/",
                     "detail": "Harvard's CS50 is the best free CS foundation, full stop."},
                    {"name": "Data structures & algorithms", "type": "skill",
                     "url": "https://neetcode.io/roadmap",
                     "detail": "NeetCode's roadmap is the standard interview-prep path."},
                    {"name": "Git & GitHub", "type": "skill",
                     "url": "https://learngitbranching.js.org/",
                     "detail": "Version control fluency is expected day one."},
                ],
            },
            {
                "kind": "education",
                "phase": "Phase 2 - Build real applications",
                "timeframe": "Months 4-9",
                "title": "Full-stack web development",
                "blurb": "Pick a stack and ship working apps. Employers hire builders.",
                "items": [
                    {"name": "Frontend: HTML/CSS/JS + React", "type": "skill",
                     "url": "https://www.theodinproject.com/",
                     "detail": "The Odin Project is a complete, free, project-based curriculum."},
                    {"name": "Backend: APIs, databases, auth", "type": "skill",
                     "url": "https://roadmap.sh/backend",
                     "detail": "roadmap.sh/backend maps the server-side skills employers want."},
                    {"name": "SQL + one database (PostgreSQL)", "type": "skill",
                     "url": "https://www.postgresql.org/docs/current/tutorial.html",
                     "detail": "Relational data modeling is in every backend interview."},
                ],
            },
            {
                "kind": "experience",
                "phase": "Phase 3 - Portfolio",
                "timeframe": "Months 6-12",
                "title": "Ship 3+ real projects",
                "blurb": "A deployed portfolio is worth more than any bootcamp certificate.",
                "items": [
                    {"name": "Build & deploy 3 full-stack apps (public GitHub + live URL)", "type": "experience",
                     "url": "https://github.com/",
                     "detail": "Real, deployed apps with clean READMEs are your resume."},
                    {"name": "Contribute to open source", "type": "experience",
                     "url": "https://goodfirstissue.dev/",
                     "detail": "Merged PRs in real projects signal collaboration skill."},
                ],
            },
            {
                "kind": "lab",
                "phase": "Phase 4 - Interview readiness",
                "timeframe": "Months 9-15",
                "title": "Crack the technical interview",
                "blurb": "The coding interview is its own skill. Train it deliberately.",
                "items": [
                    {"name": "LeetCode patterns (grind 150-200 problems)", "type": "lab",
                     "url": "https://leetcode.com/",
                     "detail": "Pattern-based practice, not random grinding."},
                    {"name": "System design basics (for mid-level+)", "type": "skill",
                     "url": "https://github.com/donnemartin/system-design-primer",
                     "detail": "Expected once you target non-junior roles."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 5 - Optional differentiators",
                "timeframe": "As needed",
                "title": "Cloud cert (optional)",
                "blurb": "Not required, but a cloud cert helps resume-screen pass rates.",
                "items": [
                    {"name": "AWS Certified Developer - Associate", "type": "certification",
                     "url": "https://aws.amazon.com/certification/certified-developer-associate/",
                     "detail": "Signals you can build on the cloud most employers use."},
                ],
            },
            {
                "kind": "role",
                "phase": "Goal",
                "timeframe": "Apply now",
                "title": "Software Engineer",
                "blurb": "Strong fundamentals, a deployed portfolio, and interview-ready problem solving.",
                "items": [],
            },
        ],
    },

    # ===================================================================
    "business_analyst": {
        "title": "IT Business Analyst",
        "tagline": "Bridge business needs and technical solutions with data and requirements.",
        "salary": "$80k - $120k (US median ~$95k)",
        "duration": "6 - 12 months",
        "demand": "Moderate-High",
        "keywords": ["business analyst", "ba", "systems analyst", "product analyst",
                     "requirements analyst", "data analyst"],
        "stages": [
            {
                "kind": "foundation",
                "phase": "Phase 1 - Core analyst skills",
                "timeframe": "Months 1-3",
                "title": "Requirements, process & data literacy",
                "blurb": "The BA core: elicit needs, model processes, read the data.",
                "items": [
                    {"name": "Requirements gathering & user stories", "type": "skill",
                     "url": "https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation/",
                     "detail": "IIBA's BABOK is the recognised body of knowledge."},
                    {"name": "Process modeling (BPMN, flowcharts)", "type": "skill",
                     "url": "https://www.lucidchart.com/pages/bpmn",
                     "detail": "Visualizing as-is / to-be processes is daily BA work."},
                    {"name": "SQL + Excel fundamentals", "type": "skill",
                     "url": "https://mode.com/sql-tutorial/",
                     "detail": "BAs are expected to pull and analyze data themselves."},
                ],
            },
            {
                "kind": "education",
                "phase": "Phase 2 - Tools & visualization",
                "timeframe": "Months 2-5",
                "title": "BI & collaboration tooling",
                "blurb": "Turn requirements and data into dashboards and clear artifacts.",
                "items": [
                    {"name": "Power BI or Tableau", "type": "skill",
                     "url": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi",
                     "detail": "Microsoft's free Power BI learning path; Tableau if preferred."},
                    {"name": "Jira / Confluence for backlog & docs", "type": "skill",
                     "url": "https://university.atlassian.com/student/catalog",
                     "detail": "Free Atlassian University; standard BA collaboration tools."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 3 - Certification",
                "timeframe": "Months 4-9",
                "title": "ECBA / CCBA (IIBA)",
                "blurb": "IIBA credentials are the recruiter-recognised standard for BAs.",
                "items": [
                    {"name": "ECBA - Entry Certificate in Business Analysis", "type": "certification",
                     "url": "https://www.iiba.org/business-analysis-certifications/ecba/",
                     "detail": "Entry-level; no experience required. Strong resume signal."},
                    {"name": "CBAP / CCBA (as you gain experience)", "type": "certification",
                     "url": "https://www.iiba.org/business-analysis-certifications/",
                     "detail": "Advance to these once you have logged BA hours."},
                    {"name": "PMI-PBA (analysis within projects)", "type": "certification",
                     "url": "https://www.pmi.org/certifications/business-analysis-pba",
                     "detail": "Great fit if you work inside project teams."},
                ],
            },
            {
                "kind": "experience",
                "phase": "Phase 4 - Real deliverables",
                "timeframe": "Months 5-12",
                "title": "Build a portfolio of BA artifacts",
                "blurb": "Show real requirements docs, process maps, and dashboards you produced.",
                "items": [
                    {"name": "Document a real or mock project (BRD, user stories, process maps)", "type": "experience",
                     "url": "https://www.modernanalyst.com/",
                     "detail": "ModernAnalyst has templates and a BA community."},
                    {"name": "Build 1-2 BI dashboards from public datasets", "type": "lab",
                     "url": "https://public.tableau.com/app/discover",
                     "detail": "Publish to Tableau Public for a recruiter-visible portfolio."},
                ],
            },
            {
                "kind": "role",
                "phase": "Goal",
                "timeframe": "Apply now",
                "title": "IT Business Analyst",
                "blurb": "Requirements + data + BI tooling, an IIBA cert, and a portfolio of real artifacts.",
                "items": [],
            },
        ],
    },

    # ===================================================================
    "network_engineer": {
        "title": "Network Engineer",
        "tagline": "Design, build and maintain the networks that keep everything connected.",
        "salary": "$85k - $135k (US median ~$110k)",
        "duration": "9 - 18 months",
        "demand": "Moderate-High",
        "keywords": ["network engineer", "network administrator", "noc", "networking",
                     "ccna", "cisco", "network"],
        "stages": [
            {
                "kind": "foundation",
                "phase": "Phase 1 - Networking foundations",
                "timeframe": "Months 1-3",
                "title": "How networks actually work",
                "blurb": "OSI model, TCP/IP, routing & switching concepts - the bedrock.",
                "items": [
                    {"name": "CompTIA Network+ knowledge base", "type": "skill",
                     "url": "https://www.professormesser.com/network-plus/n10-009/n10-009-training-course/",
                     "detail": "Professor Messer's free, complete Network+ course."},
                    {"name": "Subnetting & IP addressing fluency", "type": "skill",
                     "url": "https://subnettingpractice.com/",
                     "detail": "Drill until subnetting is second nature - interviews test it."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 2 - Entry cert",
                "timeframe": "Months 3-5",
                "title": "CompTIA Network+",
                "blurb": "Vendor-neutral baseline that clears junior-role resume filters.",
                "items": [
                    {"name": "CompTIA Network+ (N10-009)", "type": "certification",
                     "url": "https://www.comptia.org/certifications/network",
                     "detail": "Recognised entry credential; good stepping stone to CCNA."},
                ],
            },
            {
                "kind": "lab",
                "phase": "Phase 3 - Hands-on labs",
                "timeframe": "Months 4-8",
                "title": "Build & break virtual networks",
                "blurb": "Networking is learned by configuring. Simulators make it free.",
                "items": [
                    {"name": "Cisco Packet Tracer labs", "type": "lab",
                     "url": "https://www.netacad.com/courses/packet-tracer",
                     "detail": "Free Cisco simulator; build routed/switched topologies."},
                    {"name": "GNS3 / EVE-NG for real IOS images", "type": "lab",
                     "url": "https://www.gns3.com/",
                     "detail": "Run real network OS images for deeper, job-like practice."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 4 - Flagship cert",
                "timeframe": "Months 6-12",
                "title": "Cisco CCNA",
                "blurb": "The single most requested networking credential in job postings.",
                "items": [
                    {"name": "Cisco Certified Network Associate (CCNA 200-301)", "type": "certification",
                     "url": "https://www.cisco.com/site/us/en/learn/training-certifications/certifications/enterprise/ccna/index.html",
                     "detail": "The recruiter gold standard for network roles."},
                ],
            },
            {
                "kind": "experience",
                "phase": "Phase 5 - Experience & next cert",
                "timeframe": "Months 9-18",
                "title": "Get on the job, then specialize",
                "blurb": "Start in a NOC/helpdesk-to-network role, then deepen with CCNP or cloud networking.",
                "items": [
                    {"name": "NOC / junior network role for real device time", "type": "experience",
                     "url": "https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html",
                     "detail": "Production experience is what unlocks senior roles."},
                    {"name": "CCNP Enterprise or cloud-networking cert (next step)", "type": "certification",
                     "url": "https://www.cisco.com/site/us/en/learn/training-certifications/certifications/enterprise/ccnp-enterprise/index.html",
                     "detail": "Advance once you have CCNA + hands-on experience."},
                ],
            },
            {
                "kind": "role",
                "phase": "Goal",
                "timeframe": "Apply now",
                "title": "Network Engineer",
                "blurb": "Solid fundamentals, Network+ -> CCNA, real lab + production experience.",
                "items": [],
            },
        ],
    },
}


# ---------------------------------------------------------------------------
# Generic fallback (used when no curated roadmap matches)
# ---------------------------------------------------------------------------

def _generic_roadmap(role_text):
    nice = role_text.strip().title() or "Your Target Role"
    return {
        "title": nice,
        "tagline": "A general framework - tell us a more specific IT role for an expert-curated path.",
        "salary": "Varies by role & region",
        "duration": "9 - 18 months (typical)",
        "demand": "Varies",
        "generic": True,
        "stages": [
            {
                "kind": "foundation",
                "phase": "Phase 1 - Foundations",
                "timeframe": "Months 1-3",
                "title": "Build the core knowledge",
                "blurb": "Identify the 3-4 fundamental skills this role lists in real job postings.",
                "items": [
                    {"name": "Read 15-20 live job postings for this exact title", "type": "skill",
                     "url": "https://www.linkedin.com/jobs/",
                     "detail": "Extract the most-repeated required skills and tools."},
                    {"name": "Find the role's roadmap on roadmap.sh", "type": "education",
                     "url": "https://roadmap.sh/",
                     "detail": "Community skill roadmaps for most tech roles."},
                ],
            },
            {
                "kind": "certification",
                "phase": "Phase 2 - Recognised certification",
                "timeframe": "Months 3-8",
                "title": "Earn the cert recruiters ask for",
                "blurb": "Pick the ONE credential that shows up most in postings - skip the filler.",
                "items": [
                    {"name": "Identify the top cert from job-posting frequency", "type": "certification",
                     "url": "https://www.google.com/search?q=" + role_text.replace(" ", "+") + "+top+certification",
                     "detail": "Choose the most-requested, vendor-respected credential."},
                ],
            },
            {
                "kind": "lab",
                "phase": "Phase 3 - Hands-on practice",
                "timeframe": "Months 4-10",
                "title": "Practice on real platforms",
                "blurb": "Use sandboxes and labs to turn knowledge into demonstrable skill.",
                "items": [
                    {"name": "Find a hands-on lab platform for this domain", "type": "lab",
                     "url": "https://roadmap.sh/",
                     "detail": "e.g. TryHackMe, Kaggle, AWS Skill Builder, depending on field."},
                ],
            },
            {
                "kind": "experience",
                "phase": "Phase 4 - Portfolio & experience",
                "timeframe": "Months 6-18",
                "title": "Build a visible track record",
                "blurb": "Ship 2-3 real projects and get any adjacent role to log experience.",
                "items": [
                    {"name": "Publish 2-3 portfolio projects (GitHub / public)", "type": "experience",
                     "url": "https://github.com/",
                     "detail": "Real, documented work beats certificates for most roles."},
                ],
            },
            {
                "kind": "role",
                "phase": "Goal",
                "timeframe": "Apply now",
                "title": nice,
                "blurb": "Foundations + the key cert + hands-on practice + a real portfolio.",
                "items": [],
            },
        ],
    }


# ---------------------------------------------------------------------------
# Matching logic
# ---------------------------------------------------------------------------

def _score(query, keyword):
    """Combined word-boundary substring + fuzzy score.

    Short keywords (<= 3 chars, e.g. 'pm', 'ai', 'ml') must match as a whole
    word so they don't trigger on substrings like 'ai' inside 'chain'.
    """
    q, k = query.lower().strip(), keyword.lower().strip()
    if not q or not k:
        return 0.0

    # whole-word match in either direction -> strong signal
    if re.search(r"\b" + re.escape(k) + r"\b", q):
        return 1.0
    # for longer keywords also allow the query being a substring of the keyword
    if len(q) > 3 and q in k:
        return 0.95

    return SequenceMatcher(None, q, k).ratio()


def match_roadmap(role_text):
    """Return (roadmap_dict, matched_key, confidence)."""
    query = (role_text or "").strip().lower()
    if not query:
        return _generic_roadmap(""), None, 0.0

    best_key, best_score = None, 0.0
    for key, rm in ROADMAPS.items():
        for kw in rm["keywords"]:
            s = _score(query, kw)
            if s > best_score:
                best_score, best_key = s, key

    if best_key and best_score >= 0.6:
        return ROADMAPS[best_key], best_key, round(best_score, 2)

    return _generic_roadmap(role_text), None, round(best_score, 2)


def list_roles():
    """Suggested roles for the UI chips."""
    return [
        {"key": k, "title": v["title"], "demand": v["demand"]}
        for k, v in ROADMAPS.items()
    ]
