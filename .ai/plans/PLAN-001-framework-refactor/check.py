"""Checks for PLAN-001: broken links, leftover choice codes, file sizes.

Usage (from the repo root; -I keeps Python from importing files in the repo):
  python3 -I .ai/plans/PLAN-001-framework-refactor/check.py links [paths...]
  python3 -I .ai/plans/PLAN-001-framework-refactor/check.py codes [paths...]
  python3 -I .ai/plans/PLAN-001-framework-refactor/check.py sizes [paths...]
  python3 -I .ai/plans/PLAN-001-framework-refactor/check.py vocab    # scale words defined in project-rules
  python3 -I .ai/plans/PLAN-001-framework-refactor/check.py types    # task-types rows + filter command
  python3 -I .ai/plans/PLAN-001-framework-refactor/check.py config   # ai-config.yaml + tool reference blocks
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
LEVEL = re.compile(r"^(haiku|sonnet|opus|fable)/(low|medium|high|xhigh|max)$")


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


def _check_tasks(tasks, skills, where, need_effort):
    bad, seen = 0, []
    for entry in tasks:
        seen += entry.get("for", [])
        for lv in entry.get("try", []):
            ok = LEVEL.match(str(lv)) if need_effort else re.match(r"^[\w.\-]+(/\w+)?$", str(lv))
            if not ok:
                print(f"{where}: bad level {lv!r}")
                bad += 1
    for sk in skills:
        if seen.count(sk) != 1:
            print(f"{where}: skill {sk} listed {seen.count(sk)} times")
            bad += 1
    return bad


def check_config():
    import yaml
    skills = sorted(d for d in os.listdir(".ai/skills") if os.path.isdir(os.path.join(".ai/skills", d)))
    skills.append("lookup")
    bad = 0
    try:
        cfg = yaml.safe_load(open("ai-config.yaml", encoding="utf-8"))
    except Exception as e:
        print(f"ai-config.yaml: {e}")
        return 1
    for key in ("tool", "sessions", "tasks", "high_risk_min", "budget_usd_per_task", "stack", "commands"):
        if key not in cfg:
            print(f"ai-config.yaml: missing {key}")
            bad += 1
    bad += _check_tasks(cfg.get("tasks", []), skills, "ai-config.yaml", True)
    for v in list((cfg.get("sessions") or {}).values()) + [cfg.get("high_risk_min")]:
        if not LEVEL.match(str(v)):
            print(f"ai-config.yaml: bad level {v!r}")
            bad += 1
    refdir = ".ai/agents/references"
    for f in sorted(os.listdir(refdir)):
        text = open(os.path.join(refdir, f), encoding="utf-8").read()
        blocks = [b for b in re.findall(r"```yaml\n(.*?)```", text, re.S) if "tasks:" in b]
        if len(blocks) != 1:
            print(f"{f}: expected 1 yaml block with tasks:, found {len(blocks)}")
            bad += 1
            continue
        block = yaml.safe_load(blocks[0])
        bad += _check_tasks(block.get("tasks", []), skills, f, False)
    tpl = yaml.safe_load(open(".ai/templates/TASK-MANIFEST-TEMPLATE.yaml", encoding="utf-8"))
    ex = tpl.get("execution", {})
    if "try" not in ex or any(k in ex for k in ("start", "floor", "ceiling")) or "ladder" in tpl.get("escalation", {}):
        print("TASK-MANIFEST-TEMPLATE: execution must use try, without start/floor/ceiling/ladder")
        bad += 1
    print(f"config problems: {bad}")
    return bad


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] in {"vocab", "types", "config"}:
        fn = {"vocab": check_vocab, "types": check_types, "config": check_config}[sys.argv[1]]
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
