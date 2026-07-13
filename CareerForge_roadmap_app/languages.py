"""
Predefined learning paths for programming languages & technologies.

Each entry has a category, an official "getting started" URL, an optional deeper
learning resource, and an optional Exercism track slug for graded practice.
build_language_roadmap() turns any entry into a chronological learning path in
the same shape the roadmap UI renders (so the workflow + HTML export just work).
"""

# (name, official_url, learn_url_or_None, exercism_slug_or_None)
CATEGORIES = [
    ("Languages (general-purpose)", [
        ("Ada", "https://learn.adacore.com/", None, "ada"),
        ("Assembly (x86-64)", "https://cs.lmu.edu/~ray/notes/x86assembly/", "https://www.nasm.us/doc/", None),
        ("C", "https://en.cppreference.com/w/c", "https://www.learn-c.org/", "c"),
        ("C++", "https://en.cppreference.com/w/", "https://www.learncpp.com/", "cpp"),
        ("COBOL", "https://github.com/openmainframeproject/cobol-programming-course", None, "cobol"),
        ("Common Lisp", "https://lisp-lang.org/learn/", "https://gigamonkeys.com/book/", "common-lisp"),
        ("Crystal", "https://crystal-lang.org/reference/", None, "crystal"),
        ("D", "https://dlang.org/", "https://tour.dlang.org/", "d"),
        ("Elixir", "https://elixir-lang.org/learning.html", None, "elixir"),
        ("Erlang", "https://www.erlang.org/docs", "https://learnyousomeerlang.com/", "erlang"),
        ("F#", "https://learn.microsoft.com/en-us/dotnet/fsharp/", "https://fsharpforfunandprofit.com/", "fsharp"),
        ("Fortran", "https://fortran-lang.org/learn/", None, "fortran"),
        ("GDScript", "https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/index.html", None, "gdscript"),
        ("Go", "https://go.dev/learn/", "https://go.dev/tour/", "go"),
        ("Groovy", "https://groovy-lang.org/documentation.html", None, "groovy"),
        ("Haskell", "https://www.haskell.org/documentation/", "http://learnyouahaskell.com/", "haskell"),
        ("Java", "https://dev.java/learn/", None, "java"),
        ("JavaScript", "https://developer.mozilla.org/en-US/docs/Web/JavaScript", "https://javascript.info/", "javascript"),
        ("Julia", "https://julialang.org/learning/", None, "julia"),
        ("Kotlin", "https://kotlinlang.org/docs/getting-started.html", None, "kotlin"),
        ("Lua", "https://www.lua.org/manual/5.4/", "https://www.lua.org/pil/", "lua"),
        ("MATLAB", "https://www.mathworks.com/help/matlab/getting-started-with-matlab.html", None, None),
        ("Nim", "https://nim-lang.org/documentation.html", "https://nim-lang.org/docs/tut1.html", "nim"),
        ("OCaml", "https://ocaml.org/docs", None, "ocaml"),
        ("Perl", "https://www.perl.org/learn.html", "https://perldoc.perl.org/", "perl5"),
        ("PHP", "https://www.php.net/manual/en/", "https://phptherightway.com/", "php"),
        ("PowerShell", "https://learn.microsoft.com/en-us/powershell/scripting/learn/", None, "powershell"),
        ("Python", "https://docs.python.org/3/tutorial/", "https://realpython.com/", "python"),
        ("R", "https://cran.r-project.org/manuals.html", "https://r4ds.hadley.nz/", "r"),
        ("Racket", "https://docs.racket-lang.org/", None, "racket"),
        ("Ruby", "https://www.ruby-lang.org/en/documentation/", "https://rubykoans.com/", "ruby"),
        ("Rust", "https://doc.rust-lang.org/book/", "https://rust-book.cs.brown.edu/", "rust"),
        ("Scala", "https://docs.scala-lang.org/", None, "scala"),
        ("Scheme", "https://docs.scheme.org/", None, "scheme"),
        ("Shell / Bash", "https://www.gnu.org/software/bash/manual/", "https://learnxinyminutes.com/docs/bash/", "bash"),
        ("Swift & SwiftUI", "https://www.swift.org/getting-started/", "https://developer.apple.com/tutorials/swiftui", "swift"),
        ("Tcl", "https://www.tcl-lang.org/doc/", None, "tcl"),
        ("TypeScript", "https://www.typescriptlang.org/docs/handbook/intro.html", "https://www.totaltypescript.com/tutorials", "typescript"),
        ("V", "https://docs.vlang.io/", None, None),
        ("Zig", "https://ziglang.org/learn/", None, "zig"),
    ]),
    ("Web / app frameworks", [
        ("Angular", "https://angular.dev/tutorials", None, None),
        ("ASP.NET Core", "https://learn.microsoft.com/en-us/aspnet/core/", None, None),
        ("Django", "https://docs.djangoproject.com/en/stable/intro/tutorial01/", None, None),
        ("Flask", "https://flask.palletsprojects.com/en/stable/tutorial/", None, None),
        ("Flutter", "https://docs.flutter.dev/get-started/learn-flutter", None, None),
        ("Laravel", "https://bootcamp.laravel.com/", "https://laravel.com/docs", None),
        ("Next.js", "https://nextjs.org/learn", None, None),
        ("Node.js", "https://nodejs.org/en/learn", None, None),
        ("React", "https://react.dev/learn", None, None),
        ("React Native", "https://reactnative.dev/docs/getting-started", None, None),
        ("Ruby on Rails", "https://guides.rubyonrails.org/getting_started.html", None, None),
        ("Vue", "https://vuejs.org/tutorial/", None, None),
    ]),
    ("Data / AI / ML", [
        ("AI Agent Development", "https://huggingface.co/learn/agents-course", "https://python.langchain.com/docs/introduction/", None),
        ("Python · AI & ML", "https://www.coursera.org/specializations/machine-learning-introduction", "https://scikit-learn.org/stable/tutorial/index.html", None),
        ("Python · Data Analysis", "https://pandas.pydata.org/docs/getting_started/index.html", "https://www.kaggle.com/learn/pandas", None),
        ("Python · Data Engineering", "https://github.com/DataTalksClub/data-engineering-zoomcamp", None, None),
        ("TensorFlow", "https://www.tensorflow.org/learn", "https://www.tensorflow.org/tutorials", None),
    ]),
    ("Data stores / query", [
        ("Elasticsearch", "https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html", None, None),
        ("GraphQL", "https://graphql.org/learn/", None, None),
        ("MongoDB", "https://learn.mongodb.com/", "https://www.mongodb.com/docs/manual/tutorial/", None),
        ("Redis", "https://redis.io/docs/latest/develop/", "https://university.redis.io/", None),
        ("SQL", "https://sqlbolt.com/", "https://mode.com/sql-tutorial/", None),
    ]),
    ("DevOps / cloud / tooling", [
        ("Cloudflare", "https://developers.cloudflare.com/learning-paths/", None, None),
        ("Docker", "https://docs.docker.com/get-started/", None, None),
        ("Git & GitHub", "https://learngitbranching.js.org/", "https://docs.github.com/en/get-started", None),
        ("Kubernetes", "https://kubernetes.io/docs/tutorials/kubernetes-basics/", None, None),
        ("Terraform", "https://developer.hashicorp.com/terraform/tutorials", None, None),
        ("YAML", "https://learnxinyminutes.com/docs/yaml/", "https://yaml.org/", None),
    ]),
    ("Web markup / styling", [
        ("CSS", "https://web.dev/learn/css", "https://developer.mozilla.org/en-US/docs/Learn/CSS", None),
        ("HTML", "https://web.dev/learn/html", "https://developer.mozilla.org/en-US/docs/Learn/HTML", None),
    ]),
    ("Blockchain / smart contracts", [
        ("Cadence", "https://cadence-lang.org/docs/", None, None),
        ("Cairo", "https://book.cairo-lang.org/", None, None),
        ("Clarity", "https://book.clarity-lang.org/", None, None),
        ("ink!", "https://use.ink/", None, None),
        ("Michelson", "https://opentezos.com/michelson/", "https://tezos.gitlab.io/active/michelson.html", None),
        ("Move", "https://move-language.github.io/move/", "https://aptos.dev/en/build/smart-contracts", None),
        ("Solidity", "https://docs.soliditylang.org/", "https://cryptozombies.io/", None),
        ("Vyper", "https://docs.vyperlang.org/", None, None),
        ("Yul", "https://docs.soliditylang.org/en/latest/yul.html", None, None),
    ]),
    ("Other", [
        ("API Design", "https://roadmap.sh/api-design", "https://learn.openapis.org/", None),
        ("ColdFusion", "https://cfdocs.org/", "https://helpx.adobe.com/coldfusion/get-started.html", None),
    ]),
]

_INDEX = {}
for _cat, _items in CATEGORIES:
    for (_name, _off, _learn, _ex) in _items:
        _INDEX[_name.lower()] = {"name": _name, "category": _cat,
                                 "official": _off, "learn": _learn, "exercism": _ex}

_TAGLINE = {
    "Languages (general-purpose)": "Learn {name} from setup to real proficiency.",
    "Web / app frameworks": "Go from zero to shipping apps with {name}.",
    "Data / AI / ML": "A hands-on path to build with {name}.",
    "Data stores / query": "Master {name} for real-world data work.",
    "DevOps / cloud / tooling": "Get productive with {name} the way teams use it.",
    "Web markup / styling": "Build clean, modern interfaces with {name}.",
    "Blockchain / smart contracts": "Learn {name} and ship smart contracts safely.",
    "Other": "A practical, hands-on learning path for {name}.",
}



# ---------------------------------------------------------------------------
# Market popularity tiers (grounded in Stack Overflow Developer Survey, TIOBE,
# GitHub Octoverse, and general hiring demand). Used to sort the picker and to
# label each learning path.
#     Very High  - ubiquitous, top of every usage/demand ranking
#     High       - widely used and in strong demand
#     Moderate   - solid, common in its niche
#     Niche      - specialized or legacy; smaller but real communities
#     Emerging   - newer, growing momentum, lower current usage
# ---------------------------------------------------------------------------

POPULARITY = {
    # general-purpose
    "JavaScript": "Very High", "Python": "Very High", "TypeScript": "Very High", "Java": "Very High",
    "C": "High", "C++": "High", "Go": "High", "PHP": "High", "Rust": "High", "Kotlin": "High",
    "Shell / Bash": "High", "PowerShell": "High", "Swift & SwiftUI": "High",
    "Ruby": "Moderate", "R": "Moderate", "Scala": "Moderate", "Lua": "Moderate", "MATLAB": "Moderate",
    "Ada": "Niche", "Assembly (x86-64)": "Niche", "COBOL": "Niche", "Common Lisp": "Niche",
    "D": "Niche", "Elixir": "Niche", "Erlang": "Niche", "F#": "Niche", "Fortran": "Niche",
    "Groovy": "Niche", "Haskell": "Niche", "Julia": "Niche", "OCaml": "Niche", "Perl": "Niche",
    "Racket": "Niche", "Scheme": "Niche", "Tcl": "Niche",
    "Crystal": "Emerging", "GDScript": "Emerging", "Nim": "Emerging", "V": "Emerging", "Zig": "Emerging",
    # web / app frameworks
    "React": "Very High", "Node.js": "Very High",
    "Angular": "High", "Vue": "High", "Next.js": "High", "ASP.NET Core": "High", "Flask": "High",
    "Django": "High", "Flutter": "High", "React Native": "High", "Laravel": "High",
    "Ruby on Rails": "Moderate",
    # data / ai / ml
    "Python · AI & ML": "Very High", "Python · Data Analysis": "Very High",
    "Python · Data Engineering": "High", "TensorFlow": "High", "AI Agent Development": "Emerging",
    # data stores / query
    "SQL": "Very High", "MongoDB": "High", "Redis": "High", "Elasticsearch": "High", "GraphQL": "High",
    # devops / cloud / tooling
    "Docker": "Very High", "Git & GitHub": "Very High", "Kubernetes": "High", "Terraform": "High",
    "YAML": "High", "Cloudflare": "Moderate",
    # web markup / styling
    "HTML": "Very High", "CSS": "Very High",
    # blockchain / smart contracts
    "Solidity": "Moderate", "Cairo": "Emerging", "Move": "Emerging",
    "Cadence": "Niche", "Clarity": "Niche", "ink!": "Niche", "Michelson": "Niche",
    "Vyper": "Niche", "Yul": "Niche",
    # other
    "API Design": "High", "ColdFusion": "Niche",
}

POP_RANK = {"Very High": 0, "High": 1, "Moderate": 2, "Niche": 3, "Emerging": 4}


def list_language_groups():
    groups = []
    for cat, items in CATEGORIES:
        enriched = []
        for (n, o, l, e) in items:
            pop = POPULARITY.get(n, "Moderate")
            enriched.append({"name": n, "popularity": pop, "rank": POP_RANK[pop]})
        enriched.sort(key=lambda x: (x["rank"], x["name"].lower()))
        groups.append({"category": cat, "items": enriched})
    return groups



# roadmap.sh skill roadmaps for the technologies that have one.
LANG_ROADMAPSH = {
    "Python": "https://roadmap.sh/python", "JavaScript": "https://roadmap.sh/javascript",
    "TypeScript": "https://roadmap.sh/typescript", "Java": "https://roadmap.sh/java",
    "C++": "https://roadmap.sh/cpp", "Go": "https://roadmap.sh/golang", "Rust": "https://roadmap.sh/rust",
    "PHP": "https://roadmap.sh/php", "Kotlin": "https://roadmap.sh/kotlin", "Ruby": "https://roadmap.sh/ruby",
    "Scala": "https://roadmap.sh/scala", "Shell / Bash": "https://roadmap.sh/shell-bash",
    "Swift & SwiftUI": "https://roadmap.sh/swift-ui",
    "Angular": "https://roadmap.sh/angular", "ASP.NET Core": "https://roadmap.sh/aspnet-core",
    "Django": "https://roadmap.sh/django", "Flutter": "https://roadmap.sh/flutter",
    "Laravel": "https://roadmap.sh/laravel", "Next.js": "https://roadmap.sh/nextjs",
    "Node.js": "https://roadmap.sh/nodejs", "React": "https://roadmap.sh/react",
    "React Native": "https://roadmap.sh/react-native", "Ruby on Rails": "https://roadmap.sh/ruby-on-rails",
    "Vue": "https://roadmap.sh/vue",
    "AI Agent Development": "https://roadmap.sh/ai-agents",
    "Python · AI & ML": "https://roadmap.sh/ai-data-scientist",
    "Python · Data Analysis": "https://roadmap.sh/python-data-analysis",
    "Python · Data Engineering": "https://roadmap.sh/data-engineer",
    "TensorFlow": "https://roadmap.sh/machine-learning",
    "Elasticsearch": "https://roadmap.sh/elasticsearch", "MongoDB": "https://roadmap.sh/mongodb",
    "Redis": "https://roadmap.sh/redis", "SQL": "https://roadmap.sh/sql",
    "Cloudflare": "https://roadmap.sh/cloudflare", "Docker": "https://roadmap.sh/docker",
    "Git & GitHub": "https://roadmap.sh/git-github", "Kubernetes": "https://roadmap.sh/kubernetes",
    "Terraform": "https://roadmap.sh/terraform",
    "CSS": "https://roadmap.sh/css", "HTML": "https://roadmap.sh/html",
    "Solidity": "https://roadmap.sh/blockchain", "API Design": "https://roadmap.sh/api-design",
}


def build_language_roadmap(name):
    info = _INDEX.get((name or "").strip().lower())
    if not info:
        info = {"name": name or "This technology", "category": "Other",
                "official": "https://roadmap.sh/", "learn": None, "exercism": None}
    nm = info["name"]; cat = info["category"]
    off = info["official"]; learn = info["learn"] or off; ex = info["exercism"]

    if ex:
        practice_name = "Exercism %s track (graded practice)" % nm
        practice_url = "https://exercism.org/tracks/%s" % ex
        practice_detail = "Dozens of small problems with mentoring - the fastest way to fluency."
        practice_metric = "Exercism"
    else:
        practice_name = "Work through exercises & official examples"
        practice_url = learn
        practice_detail = "Re-implement the tutorial examples, then vary them until they stick."
        practice_metric = "Projects"

    tagline = _TAGLINE.get(cat, "A practical learning path for {name}.").format(name=nm)

    stages = [
        {"kind": "foundation", "phase": "Step 1 - Setup", "timeframe": "Week 1",
         "title": "Install & run your first program",
         "blurb": "Get the toolchain working and ship a tiny first program in %s." % nm,
         "items": [{"name": "%s - official getting started" % nm, "type": "education",
                    "url": off, "detail": "Install the tools and run your first program."}]},
        {"kind": "education", "phase": "Step 2 - Core", "timeframe": "Weeks 2-6",
         "title": "Learn the core",
         "blurb": "Syntax, types, control flow, functions, and the standard library.",
         "items": [{"name": "Primary %s tutorial / guide" % nm, "type": "skill",
                    "url": learn, "detail": "Work through the fundamentals end to end."},
                   {"name": "Official documentation", "type": "skill",
                    "url": off, "detail": "Your reference for everything as you build."}]},
        {"kind": "lab", "phase": "Step 3 - Practice", "timeframe": "Weeks 4-10",
         "title": "Practice deliberately",
         "blurb": "Cement the fundamentals by solving real, graded problems.",
         "items": [{"name": practice_name, "type": "lab",
                    "url": practice_url, "detail": practice_detail}]},
        {"kind": "experience", "phase": "Step 4 - Build", "timeframe": "Weeks 8-16",
         "title": "Build & publish real projects",
         "blurb": "Nothing proves skill like shipped projects on your GitHub.",
         "items": [{"name": "Build 2-3 projects and publish them", "type": "experience",
                    "url": "https://github.com/",
                    "detail": "Pick problems you care about; write clean READMEs."}]},
        {"kind": "role", "phase": "Goal", "timeframe": "You're proficient",
         "title": "Proficient in %s" % nm,
         "blurb": "Toolchain, core language, deliberate practice, and a real project portfolio.",
         "items": []},
    ]

    _rsh = LANG_ROADMAPSH.get(nm)
    if _rsh and not any(it.get("url", "") == _rsh for _s in stages for it in _s["items"]):
        for _st in stages:
            if _st["kind"] == "experience":
                _st["items"].append({
                    "name": "roadmap.sh interactive roadmap + projects",
                    "type": "lab", "url": _rsh,
                    "detail": "Visual roadmap and project ideas, basic to advanced."})
                break

    return {"title": "Learn %s" % nm, "tagline": tagline, "language": True,
            "metrics": [{"k": "Category", "v": cat},
                        {"k": "Popularity", "v": POPULARITY.get(nm, "Moderate")},
                        {"k": "Practice", "v": practice_metric}],
            "stages": stages}
