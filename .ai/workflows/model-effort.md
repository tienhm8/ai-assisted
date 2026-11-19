# Model, effort, and dynamic escalation

> Status: **Approved**. Changing this file requires a dedicated Task and a reviewer. Load at step 3 (Plan) and step 5 (Run), or when the Tech Lead configures it.

Model and effort are set **per Task**, never per Plan or per whole workflow. A session does not switch model mid-way: each Task runs in its own fresh subagent or session configured from its manifest ([task-execution](task-execution.md), "Orchestration").

The values live in [ai-config.yaml](../../ai-config.yaml) (`sessions`, `tasks`, `high_risk_min`, `budget_usd_per_task`); this file holds only the rules. A level is written `model/effort`, e.g. `sonnet/low`, or `model` alone when the tool cannot set effort; the whole file uses one form. A strong model at lower effort is often better than a weaker model at high effort; measure before choosing.

## 1. Orchestrator session

The main session that plans, classifies, dispatches, evaluates, and merges (steps 1–4, evaluation in step 5, steps 6–7 of task-execution) runs at `sessions.orchestrator`; its comment names the level for a Plan that contains an `architecture-change` Task. Its own cost counts toward the Plan budget. Fast lane: no Orchestrator; the session runs the single Task at that Task's start level.

## 2. Levels of a Task

A Task's levels come from `tasks` in `ai-config.yaml`: the row whose `for` list contains the Task's main Skill. A Task with several Skills takes the row with the longest `try`. `try` is the order of levels to run: `try[0]` is the start level and the last item is the maximum level. Escalation moves one item right. Without effort, each next item in `try` is a stronger model; adjacent items never repeat the same model (a repeat is not an escalation). A `try` of one item reruns at the same level (§3 rule 2).

`high_risk_min`: a `high`-risk Task, or one using `authentication-rbac` or `security-review`, never runs below it; drop the items of `try` below it. A manifest never lowers this.

The manifest copies `try` into `execution.try`. Any `try` different from `ai-config.yaml` is a **deviation**: the manifest states the reason in `deviation_reason`, and the Plan always needs approval (task-execution, "Plan approval"). Review Runs use `sessions.review` (the Skill `code-review` and `security-review` rows of `tasks` set the same level).

Constraints, checked at Plan approval:
- **Reachable maximum:** `try` has at most `max_attempts` items after dropping those below `high_risk_min`, so every approved level can actually run.
- **Changing `try` during a Run** (e.g. a Skill added under task-execution transition rule 5) always needs Plan re-approval.

The levels in `ai-config.yaml` are starting points to measure. Periodic review (`periodic-review`) reads `runs.md` across Plans: a Skill whose Tasks often escalate gets a higher first item; one that always passes at the first item may go lower. Change the levels only through a dedicated Task.

## 3. Dynamic escalation

A Task first runs at `try[0]`. The Orchestrator evaluates the result; only a failure caused by capability moves the next Run to the next item in `try`.

```text
Run at try[0] ──► Evaluate ──► Pass ──────────────► accept, record Run, unblock dependents
                    │           └─ Pass with uncertainty ─► human looks; does not escalate
                    │
                    └─► Fail ──► cause in stop_on? ──yes──► Stop, ask a human
                                      │
                                      └─no─► attempts and budget left? ──no──► Stop, ask a human
                                                     │
                                                     └─yes─► reset to error base, new Run at next item in try
                                                             (at last item: same level), fresh context
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
2. **Order of levels:** the manifest's `execution.try`. Already at the last item with attempts left (e.g. a `high`-risk Task whose `try` collapsed to one item): rerun at the same level with a fresh context and the failure note.
3. **Fresh start per Run:** each error has its own `base`: the worktree commit just before that error's first Run (for error 1, the Task's starting commit; for a later error, the accepted result it fixes). Before every retry Run of that error (escalated or same-level), reset the worktree to that error's `base`; the new Run redoes the fix from there, so accepted work is never discarded. A new error starts at the level of the Task's last accepted Run, not at `try[0]`. It gets the manifest plus a short failure note (failed criteria, failing output excerpt), not the previous transcript or diff. Keeping the previous diff instead needs a reason in `runs.md`.
4. **Never below the start level, never step down** during a Task.
5. **Attempt quota:** `max_attempts` (at most 3) counts Runs of one error: the first Run and its escalations. A new error found later (step 6 tests, step 8 review) opens its own quota of up to 3 Runs (`project-rules` 18). The hard cap across all quotas is `budget.max_cost_usd`.
6. **Budget is cumulative per Task:** the Orchestrator adds the cost of every Run of the Task from `runs.md` and stops before a Run that would start over budget. A tool's per-call limit (e.g. Claude Code `--max-budget-usd`) is set to the remaining budget, not the full budget. Where the tool has no limit, the Orchestrator checks after each Run. The default budget is `budget_usd_per_task`.
7. **No approval per step:** escalation within an approved `try` and budget needs no human approval; it is recorded in `runs.md`. Past the last item, attempts, or budget: stop, report the levels tried and their failures, propose next steps.
8. **Start low only when evaluation is cheap and automatic** (Skills whose Tasks are evaluated by commands). Tasks evaluated by a human at a gate start at their default, since a failed low Run is discovered late and costs a full rerun.

## 4. Tool settings

The values are in `ai-config.yaml`. Switching AI tool = edit `tool`, `auto_runs` and the model names there; nothing else to copy. `auto_runs: false` makes every Run attended ([task-execution](task-execution.md), "Orchestration"). When `auto_runs: true`, how to start a Run is in [ai-tools.md](../guide/ai-tools.md) §3.

Always set effort explicitly on every Run when the tool has effort; never rely on the tool's or model's default, which differs per model.

The manifest is metadata: it changes nothing unless the executor applies it. A field the tool cannot apply (e.g. effort in a tool without it; `max_output_tokens` in Claude Code) is recorded in the Run as "not applied: <field>", never silently ignored. If the tool lacks a model of the required strength, or quota runs out: stop and ask; do not downgrade.
