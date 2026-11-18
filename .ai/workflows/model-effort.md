# Model, effort, and dynamic escalation

> Status: **Approved**. Changing this file requires a dedicated Task and a reviewer. Load at step 3 (Plan) and step 5 (Run), or when the Tech Lead configures it.

Model and effort are set **per Task**, never per Plan or per whole workflow. A session does not switch model mid-way: each Task runs in its own fresh subagent or session configured from its manifest ([task-execution](task-execution.md), "Orchestration").

- **Model tier:** M1 light (lookups, summaries, template work) · M2 standard (everyday code, tests, docs) · M3 strong (design, review, security, incidents).
- **Effort:** E1 low · E2 medium · E3 high · E4 very high.
- **Level** = tier·effort, e.g. `M2·E1`. Order, lowest to highest: `M1·E1 < M1·E2 < M2·E1 < M2·E2 < M2·E3 < M3·E1 < M3·E2 < M3·E3 < M3·E4`. Within a tier, higher effort is higher; any M3 level is above any M2 level. A strong model at lower effort is often better than a weaker model at high effort; measure before choosing.

## 1. Orchestrator session

The main session that plans, classifies, dispatches, evaluates, and merges (steps 1–4, evaluation in step 5, steps 6–7 of task-execution): **M3·E3**; **M3·E4** when the Plan contains a T7 Task (architecture or contract change). Its own cost counts toward the Plan budget. Fast lane: no Orchestrator; the session runs the single Task at that Task's start level.

## 2. Default levels per Skill

A Task's `start`, `floor`, `ceiling`, `ladder` in its manifest default to the row of the Task's main Skill. A Task merging several Skills takes the highest of each value among them. Any value different from this table is a **deviation**: the manifest states the reason, and the Plan always needs approval (task-execution, "Plan approval").

| Skill | Start | Floor | Ceiling | Ladder | Evaluated by |
| --- | --- | --- | --- | --- | --- |
| (lookup, no Skill: explorer) | M1·E1 | M1·E1 | M2·E2 | M1·E1 → M2·E2 | Orchestrator |
| documentation | M2·E1 | M2·E1 | M2·E3 | M2·E1 → M2·E3 | Orchestrator |
| unit-testing, integration-testing, e2e-testing | M2·E1 | M2·E1 | M3·E3 | M2·E1 → M2·E3 → M3·E3 | Commands |
| backend-development, api-development, frontend-development | M2·E1 | M2·E1 | M3·E3 | M2·E1 → M2·E3 → M3·E3 | Commands |
| refactoring, caching, deployment, requirement-review, continuous-improvement | M2·E2 | M2·E2 | M3·E3 | M2·E2 → M3·E2 → M3·E3 | Commands or Orchestrator |
| bug-fixing | M2·E2 | M2·E2 | M3·E4 | M2·E2 → M3·E3 → M3·E4 | Commands |
| product-discovery, requirement-analysis, architecture-design, database-design, task-planning, incident-analysis | M3·E3 | M3·E3 | M3·E4 | M3·E3 → M3·E4 | Human at the gate |
| code-review | M3·E3 | M3·E3 | M3·E4 | M3·E3 → M3·E4 | Human reviewer |
| authentication-rbac, security-review | M3·E3 | M3·E3 | M3·E4 | M3·E3 → M3·E4 | Commands and human |

Constraints, checked at Plan approval:
- **Hard floor:** R3 Task, or a Task using `authentication-rbac` or `security-review`: `floor` and `start` at least M3·E3; the ladder drops every step below it. A manifest never lowers this.
- **Reachable ceiling:** the ladder ends at `ceiling` and has at most `max_attempts` steps, so every approved level can actually run.
- **Raised floor during a Run** (e.g. a Skill added under task-execution transition rule 5): changing `start`, `floor`, or `ceiling` always needs Plan re-approval.

These defaults are starting points to measure. Periodic review (T15) reads `runs.md` across Plans: a Skill whose Tasks often escalate gets a higher `start`; one that always passes at `start` may go lower. Change this table only through a dedicated Task.

## 3. Dynamic escalation

A Task first runs at `start`. The Orchestrator evaluates the result; only a failure caused by capability moves the next Run one step up the ladder.

```text
Run at start ──► Evaluate ──► Pass ──────────────► accept, record Run, unblock dependents
                    │           └─ Pass with uncertainty ─► human looks; does not escalate
                    │
                    └─► Fail ──► cause in stop_on? ──yes──► Stop, ask a human
                                      │
                                      └─no─► attempts and budget left? ──no──► Stop, ask a human
                                                     │
                                                     └─yes─► reset to error base, new Run at next step
                                                             (at ceiling: same level), fresh context
```

**Evaluation** (Orchestrator, from evidence only):

| Criterion | Checked by | Can decide Pass |
| --- | --- | --- |
| Complete | Every `outputs` entry exists; the handoff report has every required section | Yes |
| Correct | Every `acceptance_criteria[].check` passes (command output or file); `human` checks are marked pending | Yes, mandatory |
| Valid | Lint, type check; changed files all inside `scope.allowed_paths`; documents follow their template | Yes |
| Confidence | Uncertainties and assumptions the subagent reports | **No.** Never makes a Pass and never triggers escalation; on an otherwise passing Run it sends the result to a human |

- **Pass** needs all three of Complete, Correct, Valid. **Partial pass** (some AC pass, some fail) is a Fail.
- A Pass with `human` checks pending is provisional: dependents may start only if the manifest's `gate` is `none`; the human decides at the gate.
- A subagent saying "done" or "confident" is not evidence (task-execution, transition rule 4).

**Rules:**

1. **Escalate only on capability failures:** AC check fails, output incomplete, wrong logic, invalid output. On `stop_on` causes (missing input, conflicting requirement, out of scope, security finding, environment error, permission denied by the tool) stop: a stronger model cannot supply missing information or access.
2. **Ladder:** the manifest's `escalation.ladder`, ending at `ceiling` (§2 constraints). Already at `ceiling` with attempts left (e.g. an R3 Task whose ladder collapsed to one step): rerun at the same level with a fresh context and the failure note.
3. **Fresh start per Run:** each error has its own `base`: the worktree commit just before that error's first Run (for error 1, the Task's starting commit; for a later error, the accepted result it fixes). Before every retry Run of that error (escalated or same-level), reset the worktree to that error's `base`; the new Run redoes the fix from there, so accepted work is never discarded. A new error starts at the level of the Task's last accepted Run, not at `start`. It gets the manifest plus a short failure note (failed criteria, failing output excerpt), not the previous transcript or diff. Keeping the previous diff instead needs a reason in `runs.md`.
4. **Never below `floor`, never step down** during a Task.
5. **Attempt quota:** `max_attempts` (at most 3) counts Runs of one error: the first Run and its escalations. A new error found later (step 6 tests, step 8 review) opens its own quota of up to 3 Runs (`project-rules` 18). The hard cap across all quotas is `budget.max_cost_usd`.
6. **Budget is cumulative per Task:** the Orchestrator adds the cost of every Run of the Task from `runs.md` and stops before a Run that would start over budget. A tool's per-call limit (e.g. Claude Code `--max-budget-usd`) is set to the remaining budget, not the full budget. Where the tool has no limit, the Orchestrator checks after each Run.
7. **No approval per step:** escalation within an approved ladder and budget needs no human approval; it is recorded in `runs.md`. Past `ceiling`, attempts, or budget: stop, report the levels tried and their failures, propose next steps.
8. **Start low only when evaluation is cheap and automatic** (rows "Commands"). Tasks evaluated by a human at a gate start at their default, since a failed low Run is discovered late and costs a full rerun.

## 4. Mapping to real tools

To map levels, load only the mapping rows of §1 of the reference file for the AI tool in use, not the whole file:

```sh
grep -nE '^\| (M[1-3]|E[1-4])' .ai/agents/references/<tool>.md
```

Empty output means the table format changed: stop and ask; do not guess. Read the rest of the reference file (its section on running Tasks) only when setting up dispatch or when a Run fails on tool configuration. Do not copy the tables here.

Always set effort explicitly on every Run; never rely on the tool's or model's default, which differs per model.

| Tool | Reference |
| --- | --- |
| Claude Code | [claude-code.md](../agents/references/claude-code.md) |
| Cursor | [cursor.md](../agents/references/cursor.md) |
| GitHub Copilot | [copilot.md](../agents/references/copilot.md) |
| Gemini CLI | [gemini.md](../agents/references/gemini.md) |
| Codex (ChatGPT) | [codex.md](../agents/references/codex.md) |

The manifest is metadata: it changes nothing unless the executor applies it. A field the tool cannot apply (e.g. effort in Cursor, Gemini CLI; `max_output_tokens` in Claude Code) is recorded in the Run as "not applied: <field>", never silently ignored. If the tool lacks a model of the required tier, or quota runs out: stop and ask; do not downgrade.

A tool not listed: add a reference file under `.ai/agents/references/` with the same sections and add a row here.
