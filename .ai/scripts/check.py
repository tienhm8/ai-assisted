"""Shared checks of the framework (moved from PLAN-001): broken links, leftover choice codes, file sizes.
History of Plans 001 and 002 still names the old path .ai/plans/PLAN-001-framework-refactor/check.py.

Usage (from the repo root; -I keeps Python from importing files in the repo):
  python3 -I .ai/scripts/check.py links [paths...]
  python3 -I .ai/scripts/check.py codes [paths...]
  python3 -I .ai/scripts/check.py sizes [paths...]
  python3 -I .ai/scripts/check.py vocab    # scale words defined in project-rules
  python3 -I .ai/scripts/check.py types    # task-types rows + filter command
  python3 -I .ai/scripts/check.py config   # ai-config.yaml + tool reference blocks
  python3 -I .ai/scripts/check.py tree     # README "Cấu trúc" tree matches the repo
Paths default to the whole repo. Exit code 1 when a check finds a problem.
"""
import os
import re
import sys

ROOT = os.getcwd()
SKIP_DIRS = {".git", "project", "pilot", "worktrees", "node_modules"}
SKIP_FILES = {"AI-10-goal-plan-task-run.md"}  # history, not maintained
TEXT_EXT = (".md", ".yaml", ".yml")

# Choice codes being replaced by words. IDs of objects (FR-, OQ-, SRC-, PLAN-...) are kept.
CODE = re.compile(
    r"(?<![\w\-./])("
    r"R[1-3]|A[0-4]|S[1-3]|D[0-3]|G[0-7]|T1[0-5]|T[1-9]|M[1-3]\+?(?:·E[1-4])?|E[1-4]"
    r")(?![\w\-])"
    r"|\[0[1-8]\]"
)
# External standard names that look like codes: OWASP A01:2025, AWS S3.
ALLOW = re.compile(r"A\d\d:\d{4}|AWS S3|Amazon S3")
LINK = re.compile(r"\]\(([^)\s]+)\)")


def files(paths):
    for p in paths or ["."]:
        if os.path.isfile(p):
            yield p
            continue
        for d, dirs, fs in os.walk(p):
            dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
            for f in fs:
                if f.endswith(TEXT_EXT) and f not in SKIP_FILES:
                    yield os.path.join(d, f)


def lines_outside_fences(path):
    fence = False
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            if line.lstrip().startswith("```"):
                fence = not fence
                continue
            yield n, line, fence


def check_links(paths):
    bad = 0
    for f in files(paths):
        if not f.endswith(".md"):
            continue
        for n, line, fence in lines_outside_fences(f):
            if fence:
                continue
            for target in LINK.findall(line):
                if re.match(r"^(https?:|mailto:|#|<)", target):
                    continue
                path = target.split("#", 1)[0]
                full = os.path.normpath(os.path.join(os.path.dirname(f), path))
                if not os.path.exists(full):
                    print(f"{f}:{n}: broken link -> {target}")
                    bad += 1
    print(f"broken links: {bad}")
    return bad


def check_codes(paths):
    hits = 0
    per_file = {}
    for f in files(paths):
        for n, line, _ in lines_outside_fences(f):
            text = ALLOW.sub("", line)
            found = [m.group(0) for m in CODE.finditer(text)]
            if found:
                hits += len(found)
                per_file[f] = per_file.get(f, 0) + len(found)
                print(f"{f}:{n}: {', '.join(found)}")
    for f, c in sorted(per_file.items(), key=lambda x: -x[1]):
        print(f"  {c:4d} {f}", file=sys.stderr)
    print(f"choice codes: {hits} in {len(per_file)} files")
    return hits


def sizes(paths):
    total = 0
    for f in sorted(files(paths)):
        b = os.path.getsize(f)
        total += b
        print(f"{b:7d} {f}")
    print(f"total bytes: {total}")


# Vocabulary approved in PLAN-001 §6.1.
TYPES = ["new-feature", "feature", "bug-fix", "refactor", "schema-change", "requirement-change",
         "architecture-change", "requirement-review", "pr-review", "security-check", "tests-only",
         "docs-only", "release", "incident", "periodic-review"]
SCALES = {
    "autonomy": ["answer-only", "read-only", "step-by-step", "full-task", "pre-approved"],
    "rigor": ["lean", "standard", "strict"],
    "data": ["public", "internal", "sensitive", "secret"],
    "gates": ["setup", "scope", "requirements", "design", "task-ready", "code-complete",
              "release-ready", "operations"],
    "stages": ["discovery", "requirements", "design", "ai-context", "implementation", "testing",
               "release", "improvement"],
}
# A level is `model/effort`, or `model` alone when the tool cannot set effort (Cursor, Gemini CLI).
LEVEL = re.compile(r"^[\w.\-]+/(low|medium|high|xhigh|max)$")
MODEL_ONLY = re.compile(r"^[\w.\-]+$")


def check_vocab():
    text = open(".ai/rules/project-rules.md", encoding="utf-8").read()
    bad = 0
    for scale, words in SCALES.items():
        for w in words:
            if not re.search(r"`" + re.escape(w) + r"`", text):
                print(f"project-rules: {scale} term `{w}` not defined (write it in backticks)")
                bad += 1
    print(f"missing scale terms: {bad}")
    return bad


def check_types():
    import subprocess
    path = ".ai/workflows/task-types.md"
    rows = [l.split("|")[1].strip() for l in open(path, encoding="utf-8")
            if l.startswith("| ") and not l.startswith("| ---")]
    keys = [r.strip("`") for r in rows if r.strip("`") in TYPES or re.fullmatch(r"`?[a-z][a-z-]+`?", r)]
    bad = 0
    if sorted(keys) != sorted(TYPES):
        print(f"task-types rows {sorted(keys)} != expected {sorted(TYPES)}")
        bad += 1
    cmds = [l.strip() for l in open(".ai/workflows/task-execution.md", encoding="utf-8")
            if l.startswith("awk") and "task-types.md" in l and "-v t=" in l]
    if len(cmds) != 1:
        print(f"task-execution: expected 1 row-filter command, found {len(cmds)}")
        return bad + 1
    for t in TYPES:
        cmd = re.sub(r"-v t=\S+", f"-v t={t}", cmds[0])
        out = subprocess.run(["bash", "-c", cmd], capture_output=True, text=True).stdout
        hits = [l for l in out.splitlines() if l.startswith("| ")
                and l.split("|")[1].strip().strip("`") in TYPES]
        if len(hits) != 1:
            print(f"filter for {t}: {len(hits)} type rows")
            bad += 1
    print(f"type problems: {bad}")
    return bad


def _level_ok(lv, with_effort):
    return bool((LEVEL if with_effort else MODEL_ONLY).match(str(lv)))


def check_config():
    """ai-config.yaml: keys, one `try` row per Skill, one level format for the whole file.
    Without effort, the next item in `try` must be another (stronger) model, so no two
    adjacent items repeat. Tool reference files are gone: .ai/agents/references must not exist."""
    import yaml
    skills = sorted(d for d in os.listdir(".ai/skills") if os.path.isdir(os.path.join(".ai/skills", d)))
    skills.append("lookup")
    bad = 0
    try:
        cfg = yaml.safe_load(open("ai-config.yaml", encoding="utf-8"))
    except Exception as e:
        print(f"ai-config.yaml: {e}")
        return 1
    for key in ("tool", "auto_runs", "sessions", "tasks", "high_risk_min", "budget_usd_per_task", "stack", "commands"):
        if key not in cfg:
            print(f"ai-config.yaml: missing {key}")
            bad += 1
    if cfg.get("auto_runs") not in (True, False):
        print(f"ai-config.yaml: auto_runs must be true or false, got {cfg.get('auto_runs')!r}")
        bad += 1
    levels = [lv for e in cfg.get("tasks", []) for lv in e.get("try", [])]
    levels += list((cfg.get("sessions") or {}).values()) + [cfg.get("high_risk_min")]
    with_effort = "/" in str(levels[0]) if levels else True
    for lv in levels:
        if not _level_ok(lv, with_effort):
            print(f"ai-config.yaml: bad level {lv!r} (whole file uses {'model/effort' if with_effort else 'model only'})")
            bad += 1
    seen = []
    for e in cfg.get("tasks", []):
        seen += e.get("for", [])
        t = e.get("try", [])
        if not t:
            print(f"ai-config.yaml: empty try for {e.get('for')}")
            bad += 1
        for a, b in zip(t, t[1:]):
            if a == b:
                print(f"ai-config.yaml: try {t} repeats {a!r}; the next item must be a stronger level")
                bad += 1
    for sk in skills:
        if seen.count(sk) != 1:
            print(f"ai-config.yaml: skill {sk} listed {seen.count(sk)} times")
            bad += 1
    if os.path.exists(".ai/agents/references"):
        print(".ai/agents/references still exists (tool reference files are removed)")
        bad += 1
    tpl = yaml.safe_load(open(".ai/templates/TASK-MANIFEST-TEMPLATE.yaml", encoding="utf-8"))
    ex = tpl.get("execution", {})
    if "try" not in ex or any(k in ex for k in ("start", "floor", "ceiling")) or "ladder" in tpl.get("escalation", {}):
        print("TASK-MANIFEST-TEMPLATE: execution must use try, without start/floor/ceiling/ladder")
        bad += 1
    print(f"config problems: {bad}")
    return bad


def check_tree():
    """README.md "## Cấu trúc" tree: every listed path exists, and every tracked entry at the
    repo root, in .ai/ and in docs/ is listed (git-ignored folders listed in the tree are allowed)."""
    import subprocess
    text = open("README.md", encoding="utf-8").read()
    m = re.search(r"^## Cấu trúc\n.*?```text\n(.*?)```", text, re.S | re.M)
    if not m:
        print("README.md: no ```text tree under '## Cấu trúc'")
        return 1
    listed, stack, bad = set(), [], 0
    for line in m.group(1).splitlines()[1:]:          # first line is the repo root label
        g = re.match(r"^([│ ]*)[├└]── (\S+)", line)
        if not g:
            continue
        depth = len(g.group(1)) // 4
        name = g.group(2)
        stack = stack[:depth] + [name.rstrip("/")]
        path = "/".join(stack)
        listed.add(path)
        # a folder ignored as "dir/" only matches with the trailing slash
        q = path + "/" if name.endswith("/") else path
        ignored = subprocess.run(["git", "check-ignore", "-q", q]).returncode == 0
        if not os.path.exists(path) and not ignored:
            print(f"README tree lists missing path: {path}")
            bad += 1
    tracked = subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.split()
    expected = set()
    for f in tracked:
        parts = f.split("/")
        if parts[-1] in {".gitkeep", ".gitignore"} and len(parts) == 1:
            continue
        expected.add(parts[0])
        if parts[0] in {".ai", "docs"} and len(parts) > 1:
            if parts[-1] == ".gitkeep" and len(parts) == 2:
                continue
            expected.add("/".join(parts[:2]))
    expected -= {".gitignore"}
    for p in sorted(expected - listed):
        print(f"README tree misses tracked path: {p}")
        bad += 1
    print(f"tree problems: {bad}")
    return bad


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] in {"vocab", "types", "config", "tree"}:
        fn = {"vocab": check_vocab, "types": check_types, "config": check_config, "tree": check_tree}[sys.argv[1]]
        sys.exit(1 if fn() else 0)
    if len(sys.argv) < 2 or sys.argv[1] not in {"links", "codes", "sizes"}:
        print(__doc__)
        sys.exit(2)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "links":
        sys.exit(1 if check_links(args) else 0)
    if cmd == "codes":
        sys.exit(1 if check_codes(args) else 0)
    sizes(args)
