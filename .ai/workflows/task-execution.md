# Task Execution Workflow

> Status: **Approved**. **Mandatory** workflow for every Task. Changing this file requires a dedicated Task and a reviewer.

**Load just in time.** Each step loads only what its "Load" column lists. From [task-types.md](task-types.md) read only the row of the current Task type:

```sh
awk -v t=T2 '!/^\| T[0-9]+ \|/ || index($0, "| " t " |")==1' .ai/workflows/task-types.md
```

Replace `T2` with the Task type. If the Task has no type, list the types to classify it; if still unclear, stop and ask:

```sh
awk -F' \\| ' '/^\| T[0-9]+ \|/{print $1" | "$2}' .ai/workflows/task-types.md
```

Read one section of `docs/` instead of the whole file (`s` is the heading level and section number, e.g. `## 5` or `### 5.2`); if the section does not exist, the command exits with code 1:

```sh
awk -v s='## 5' 'BEGIN{n=index(s," ")} /^```/{f=!f} !f&&!p&&(index($0,s" ")==1||index($0,s". ")==1){p=1;print;next} p&&!f&&match($0,/^#+ /)&&RLENGTH<=n{exit} p; END{exit !p}' docs/03-engineering/error-handling.md
```

## Steps

| Step | Work | Load | Output |
| --- | --- | --- | --- |
| 1 · Intake | Read the Task: goal, scope, AC, risk level, autonomy level. Determine the Task type; split a hybrid Task into sub-Tasks, never combine a bug fix with a large refactor. Missing risk level, autonomy level, or rigor S: ask, do not assign yourself | Task; `project-rules`; `PROJECT.md` §2, §4; `gates-and-rigor.md` §2 when applying S; Task type row; [load-conditions.md](load-conditions.md) §1 | Task type, load set |
| 2 · Analysis | Read requirements, design, related code; unclear points become open questions. If code reveals further Rule load conditions (e.g. a repository with cache), add them to the load set | FR/BR/AC, ADR, design the Task points to; code in scope | Open questions (if any) |
| 3 · Plan | Files to change, design decisions, AC → tests, Skill chain (dropping or adding a Skill needs a reason), model and effort for the execution session. Record applicable points from documents read, with document, § and section name | PLAN-TEMPLATE; [model-effort.md](model-effort.md); `load-conditions.md` §2 when the chain has a `[ ]` Skill; Rule `testing` and every Rule in the load set from steps 1–2 | Plan |
| 4 · Plan approval | Reviewer, per "Plan approval" | — | Plan Approved |
| 5 · Implement | Run each Skill in turn: entry gate → procedure → Done-when results. Record output in the plan before loading the next Skill | Plan; `SKILL.md` of the current Skill and the `references/` it points to; `docs/` sections the Skill allows when the plan lacks them; Rules listed in the plan; Rule `coding`; Rule `git-workflow` when committing | Diff |
| 6 · Test | Run all of the project's check gates | Matching testing Skill; TEST-REPORT-TEMPLATE | Real output |
| 7 · Self-review | Check the diff against AC, scope, and loaded Rules; draft the handoff report | DELIVERY-REPORT-TEMPLATE | Handoff report |
| 8 · Review | Another session reviews per row T9; a reviewer approves the PR | Do not use the coding session's history | PR approved |
| 9 · Release | A human merges; AI only prepares per [release-workflow.md](release-workflow.md) | — | Release |
| 10 · Knowledge update | Update affected documents. Changes to Rules, Skills, workflows: propose a dedicated Task | Skill `documentation` | Docs match reality |

Analysis- or design-only Tasks (T1, T6, T7, T8, T15) skip steps 5–6: Skills and Rules in the load set are loaded at step 2; output is Draft documents.

## Fast lane for R1 Tasks

Applies when all three hold: R1 Task; no load condition for Rules `architecture`, `database`, `security`, `cache` is met; no 🟡/🔴 zone touched.

- A few-line plan in the session (files to change, tests to run); no plan file, no waiting for approval.
- One session, load only the main Skill.
- Steps 6–8 unchanged; the handoff report fills only sections with content.

If a condition outside the fast lane arises: stop, go back to step 3.

## Plan approval

Wait for a reviewer before step 5 when any holds: R3 Task; autonomy level ≤ A2; changes architecture, API contract, permissions, schema, or data; touches a 🟡 zone; the chain has an action requiring approval. Otherwise continue; the reviewer approves the final result.

## Step transition rules

1. **The plan is compressed context:** enough to execute (requirements, applicable points from documents with §, design decisions, files to change, AC → tests, Skill chain); from step 5 follow the plan, do not reread documents the plan summarized. If the plan lacks something, look up only sections the Skill allows, with the one-section command, and record it under "Nạp bổ sung" in the plan; if not found, record an open question.
2. **New session for step 5** when the Task is R2/R3 or the chain has 3+ Skills: the execution session receives only the plan and Rules.
3. **One Skill at a time:** do not load the next Skill until the Done-when results are met.
4. **Pass gates with evidence** (test output, diff, Approved documents), not with claims.
5. **A condition arises** (e.g. a bug fix turns out to touch authorization): load the matching Rule and Skill, record it in the plan; when in doubt about security or data, load. If it changes risk level or scope, or needs a design Skill: stop and report.

## On errors

| Finding | Go back to |
| --- | --- |
| Test fails due to code | The coding Skill in progress or `bug-fixing`, rerun tests |
| Test fails due to environment or test data | Fix the environment; do not loosen assertions |
| Review reports a logic bug | Matching coding Skill, rerun tests and review |
| Critical/High security finding | Matching coding Skill, rerun `security-review` on the affected part |
| Requirement missing or conflicting | **Stop**; `requirement-review`, wait for a human decision |
| Design not feasible | `architecture-design` or `database-design`; architecture changes need approval |

## Stop and ask

Stop the affected part, still do independent and safe parts, when:

- documents conflict or a decision is missing;
- an approval gate has no reviewer or evidence (which gate, which person: `gates-and-rigor.md` §1);
- it exceeds Task scope or autonomy level; it needs changes to permissions, security, or production data;
- a secret or vulnerability is found;
- the Task type, environment, or run command cannot be determined;
- the root cause cannot be found, or the fix-round limit is reached (`project-rules` 18).

When stopping, state: what was done, where it is blocked, who must decide what.
