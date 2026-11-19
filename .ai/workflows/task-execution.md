# Task Execution Workflow

> Status: **Approved**. **Mandatory** workflow for every piece of work. Changing this file requires a dedicated Task and a reviewer.

## Model: Plan → Task → Run, linked to Goals and requirements

Concepts fall in three groups (definitions, where each lives, all links: [work-model](../../docs/04-project-management/work-model.md)): A business and product definition (BRD, BRQ, Goal, Epic, Feature, User Story); B planning and work management (Plan, Task, Subtask, Dependency); C AI execution (Agent, Run, model·effort, Tool, Result, Review). Links are references, not a parent-child tree.

| Level | Answers | ID | Lives in |
| --- | --- | --- | --- |
| Goal (group A) | What outcome do we want? | `GOAL-<NN>` | [goals.md](../../docs/04-project-management/goals.md) |
| Plan | How will we do it? The split into Tasks and their order | `PLAN-<NNN>` | `.ai/plans/PLAN-<NNN>-<slug>/PLAN.md` |
| Task | What exactly to do: inputs, outputs, AC, type, risk, autonomy, agent, level | `<KEY>-<N>` | `.ai/plans/<plan>/tasks/<KEY>-<N>.yaml` (manifest) |
| Run | One execution of a Task: agent, real model·effort, result, evidence, cost | `<KEY>-<N>#<n>` | `.ai/plans/<plan>/runs.md` |

A Plan has exactly one Source (a Goal, Epic, User Story, or a standalone request) and optional Goals (zero or more); one Plan has many Tasks; a Task serves one or more User Stories/FRs; one Task has many Runs. A Plan is not a Task and a Task is not an Agent: the Agent (role in [agents/README](../agents/README.md)) executes a Task using tools.

**New Plan instead of more Tasks in an existing Plan** when at least one holds: a different output goal; can be done independently; its own lifecycle and done criteria; needs separate progress tracking or access. Default: each stretch ending at its own approval gate (analysis → `requirements` gate, design → `design` gate, implementation → `code-complete` gate) is a Plan.

Templates: [PLAN-TEMPLATE](../templates/PLAN-TEMPLATE.md), [TASK-MANIFEST-TEMPLATE](../templates/TASK-MANIFEST-TEMPLATE.yaml), [RUNS-TEMPLATE](../templates/RUNS-TEMPLATE.md).

## Orchestration

The main session is the **Orchestrator** (level per [model-effort.md](model-effort.md) §1). It: creates Plans and Tasks; sets each Task's type, proposed risk and autonomy level, agent, Skills and level; dispatches each Task to a fresh subagent or session configured from the manifest; receives results; evaluates and escalates (model-effort §3); checks dependencies; merges outputs and updates Plan and Goal status.

The Orchestrator does not write a Task's code or documents itself, does not approve, and stops at every ⏸ gate. A subagent receives only: its manifest, the failure note of the previous Run if any, `project-rules`, and the Rules, Skills, and document sections the manifest lists. It never receives the Orchestrator's history.

**Dispatch mode** follows the Task's autonomy level:
- **`full-task`, `pre-approved`: dispatched.** The Orchestrator starts the Run in a subagent or a non-interactive session at the manifest's level.
- **`step-by-step` or lower: attended.** Never dispatched to a subagent or non-interactive session, since those cannot pause for per-step approval. The Orchestrator hands the manifest, the Task's worktree path, and an opening line to a human, who opens an interactive session in that worktree at the manifest's level; that session stops after each step for approval and returns the handoff report with the Run's cost if the tool shows it. Escalation of an attended Task is proposed to the human, who opens the next session.
- **Tool without per-Task model control** (see its reference file): every Run is attended in the same way.

**Isolation and merging:** each Task runs in its own worktree under `.claude/worktrees/<Task-ID>` (Claude Code creates it with `claude -w <Task-ID>`; other tools use `git worktree add .claude/worktrees/<Task-ID> -b <branch> <base>`), branched from a commit that already contains the accepted result of every Task it depends on. Parallel Runs never share a worktree. The Orchestrator merges accepted Task branches in dependency order before step 6; a merge conflict is a Fail of the later Task. After any fix accepted at step 6 or 8, the Orchestrator rebases the Task's dependents onto the fixed result, merges again in dependency order, and reruns step 6; a dependent that then fails opens its own error. If a failure cannot be attributed to one Task (e.g. two Tasks interacting), stop and ask a human.

## Load just in time

Each step loads only what its "Load" column lists. From [task-types.md](task-types.md) read only the row of the Task type at hand:

```sh
awk -v t=bug-fix '!/^\| `[a-z-]+` \|/ || index($0, "| `" t "` |")==1' .ai/workflows/task-types.md
```

Replace `bug-fix` with the Task type key. To classify, list the types; if still unclear, stop and ask:

```sh
awk -F' \\| ' '/^\| `[a-z-]+` \|/{gsub(/^\| |`/,"",$1); print $1" | "$2}' .ai/workflows/task-types.md
```

Read one section of `docs/` instead of the whole file (`s` is the heading level and section number, e.g. `## 5` or `### 5.2`); if the section does not exist, the command exits with code 1:

```sh
awk -v s='## 5' 'BEGIN{n=index(s," ")} /^```/{f=!f} !f&&!p&&(index($0,s" ")==1||index($0,s". ")==1){p=1;print;next} p&&!f&&match($0,/^#+ /)&&RLENGTH<=n{exit} p; END{exit !p}' docs/03-engineering/error-handling.md
```

## Steps

Steps 1–4 and the evaluation in 5 run in the Orchestrator; the work of each Task in step 5 runs in its own Run.

| Step | Work | Load | Output |
| --- | --- | --- | --- |
| 1 · Intake | Read the request: a Goal, Epic, User Story, standalone request, or a single Task (then a Plan of one Task). Record it as the Plan's Source; link existing Goals it serves (goals.md) and the User Stories/FRs in scope; do not draft a Goal only to host a Plan. Determine the Task types involved; never combine a bug fix with a large refactor. Missing rigor S: ask. A Task the Tech Lead already gave R and A keeps them | Request; `project-rules`; `PROJECT.md` §2, §4; `gates-and-rigor.md` §2 when applying S; Task type rows; [load-conditions.md](load-conditions.md) §1 | Goal, Task types, load set |
| 2 · Analysis | Read requirements, design, related code; unclear points become open questions. Code revealing further Rule load conditions extends the load set | FR/BR/AC, ADR, design the request points to; code in scope | Open questions (if any) |
| 3 · Plan | Decide the Plans (criteria above). Split each into Tasks using the type's Skill chain as template (task-types §1), **except `code-review` and `security-review`, which run only at step 8** after test results exist. Write one manifest per Task: inputs, outputs, scope, AC with checks, dependencies, proposed R and A with reason, agent, Skills and Rules, document sections to load, level and escalation (model-effort §2), budget, gate. Record applicable points from documents read, with document, § and section name | PLAN-TEMPLATE, TASK-MANIFEST-TEMPLATE; [model-effort.md](model-effort.md); `load-conditions.md` §2 when the chain has a `[ ]` Skill; Skill `task-planning`; Rule `testing` and every Rule in the load set | Plan + manifests |
| 4 · Plan approval | Reviewer, per "Plan approval" | — | Plan Approved |
| 5 · Run | For each Task whose dependencies are Done, in order: start a Run at its current level, dispatched or attended per "Orchestration"; the Run executes each Skill in turn (entry gate → procedure → Done-when) and returns a handoff with evidence; the Orchestrator evaluates and accepts, escalates, or stops (model-effort §3); record the Run. Parallel Runs only for Tasks sharing no files, schema, or contract | Orchestrator: manifest, `runs.md`. Run: its manifest; `SKILL.md` of each Skill and the `references/` it points to; `docs/` sections the Skill allows when the manifest lacks them; Rules in the manifest; Rule `coding`; Rule `git-workflow` when committing | Diff or documents; `runs.md` |
| 6 · Test | Merge Task branches in dependency order; run all of the project's check gates on the merged result. A failure opens a new error quota for the responsible Task (model-effort §3 rule 5) | Matching testing Skill; TEST-REPORT-TEMPLATE | Real output |
| 7 · Self-review | Check the merged diff against every Task's AC and scope and the loaded Rules; draft one handoff report for the Plan with a row per Task; metrics from `runs.md` | DELIVERY-REPORT-TEMPLATE | Handoff report |
| 8 · Review | `code-review`, then `security-review` when its condition holds (load-conditions §2), each as a review Run with agent Reviewer or Security, declared in the Plan's "Review" row (level and budget per model-effort §2, approved with the Plan; recorded in `runs.md` as `PLAN-<NNN>-REVIEW#<n>`), fresh context, never the Orchestrator's or coding Runs' history; level per model-effort §2. A finding opens a new error quota for the responsible Task. A human reviewer approves the PR | Row `pr-review` | PR approved |
| 9 · Release | A human merges; AI only prepares per [release-workflow.md](release-workflow.md) | — | Release |
| 10 · Knowledge update | Update affected documents; update Goal status when the Plan lists Goals. Changes to Rules, Skills, workflows: propose a dedicated Task | Skill `documentation` | Docs match reality |

Analysis- or design-only Plans (Tasks of types `new-feature`, `requirement-change`, `architecture-change`, `requirement-review`, `periodic-review`) skip step 6: their Runs output Draft documents, evaluated by completeness and validity, then by a human at the gate.

## Fast lane for `low`-risk Tasks

Applies when all hold: the Plan has a single `low`-risk Task whose risk and autonomy the Tech Lead set; no load condition for Rules `architecture`, `database`, `security`, `cache` is met; no yellow zone 🟡 or red zone 🔴 touched.

- No Orchestrator, no plan or manifest file: a few-line plan in the session (Source and the User Story/FR served, files to change, tests to run, level). The Source ID also goes into the commit message and the handoff report.
- The session runs at the Task's start level (model-effort §2) and loads only the main Skill.
- One error: at most 3 rounds in this session (`project-rules` 18); no escalation inside the session. Past that: stop and ask a human to open a session at a higher level or move to the full lane.
- Steps 6–7 unchanged; the handoff report fills only sections with content.
- Step 8: the human opens a new session at the `code-review` level (model-effort §2) with the `pr-review` opening line in getting-started §5.3; never in the coding session.

If a condition outside the fast lane arises: stop, go back to step 3.

## Plan approval

Before step 5 the Tech Lead approves the Plan, including each Task's risk, autonomy, level range, ladder, budget, and scope. Approving the Plan grants the risk and autonomy written in its manifests (`project-rules` 8).

Exception, approval not awaited: every Task had its risk and autonomy set by the Tech Lead in the request, **and** every manifest uses the model-effort §2 defaults with no deviation and a budget within the project's default, **and** none of these holds: `high`-risk Task; autonomy `step-by-step` or lower; changes architecture, API contract, permissions, schema, or data; touches a yellow zone 🟡; the chain has an action requiring approval. The reviewer then approves the final result.

Re-approval is needed when adding a Task, or changing a Task's AC, scope, risk, autonomy, `start`, `floor`, `ceiling`, `ladder`, or `budget`. Escalation within the approved ladder is not a change.

## Step transition rules

1. **The manifest is compressed context:** enough to execute one Task. From step 5 a Run follows its manifest and does not reread documents the Plan summarized. If the manifest lacks something, look up only sections the Skill allows, with the one-section command, and record it under "loaded_extra" in the Run's handoff; if not found, record an open question.
2. **One Run, one fresh context:** every Task, and every escalation of a Task, starts a new subagent or session. Never switch model inside a Run.
3. **One Skill at a time** inside a Run: do not load the next Skill until the Done-when results are met.
4. **Pass gates with evidence** (check output, diff, Approved documents), not with claims.
5. **A condition arises** (e.g. a bug fix turns out to touch authorization): the Run stops and reports; the Orchestrator loads the matching Rule and Skill and updates the manifest. If it changes risk level, scope, any level field (e.g. a Skill raising the floor), or needs a design Skill: back to step 3 and re-approval.

## On errors

| Finding | Go back to |
| --- | --- |
| Run fails an AC check, incomplete or invalid output | Escalation per model-effort §3 |
| Tool denies a permission the Run needs | Stop (`stop_on`); a human adjusts the session's permissions within `allowed_paths`; rerun at the same level |
| Test fails due to code | New Run of the coding Task in progress or a `bug-fixing` Task, rerun tests |
| Test fails due to environment or test data | Fix the environment, rerun at the same level; do not loosen assertions, do not escalate |
| Review reports a logic bug | New Run of the matching coding Task, rerun tests and review |
| Critical/High security finding | Stop; new Task with the matching coding Skill, rerun `security-review` on the affected part |
| Requirement missing or conflicting | **Stop**; `requirement-review`, wait for a human decision |
| Design not feasible | `architecture-design` or `database-design` Task; architecture changes need approval |

## Stop and ask

Stop the affected Task, still run independent and safe Tasks, when:

- documents conflict or a decision is missing;
- an approval gate has no reviewer or evidence (which gate, which person: `gates-and-rigor.md` §1);
- it exceeds a Task's scope or autonomy level; it needs changes to permissions, security, or production data;
- a secret or vulnerability is found;
- the Task type, environment, or run command cannot be determined;
- the root cause cannot be found, or the Run limit, ceiling, or budget is reached (`project-rules` 18, model-effort §3).

When stopping, state: what was done, where it is blocked, who must decide what.
