# Model, effort, and dynamic escalation

> Status: **Approved**. Changing this file requires a dedicated Task and a reviewer. Load at step 3 (Plan) and step 5 (Run), or when the Tech Lead configures it.

Model and effort are set **per Task**, never per Plan or per whole workflow. A session does not switch model mid-way: each Task runs in its own fresh subagent or session configured from its manifest ([task-execution](task-execution.md), "Orchestration").

The values live in [ai-config.yaml](../../ai-config.yaml) (`sessions`, `tasks`, `high_risk_min`, `budget_usd_per_task`, `budget_warn_pct`, `budget_topup_max_pct`, `budget_pool_pct`); this file holds only the rules. A level is written `model/effort`, e.g. `sonnet/low`, or `model` alone when the tool cannot set effort; the whole file uses one form. A strong model at lower effort is often better than a weaker model at high effort; measure before choosing.

## 1. Orchestrator session

The main session that plans, classifies, dispatches, evaluates, and merges (steps 1–4, evaluation in step 5, steps 6–7 of task-execution) runs at `sessions.orchestrator`; its comment names the level for a Plan that contains an `architecture-change` Task. Its own cost counts toward the Plan budget. Fast lane: no Orchestrator; the session runs the single Task at that Task's start level.

## 2. Levels of a Task

A Task's levels come from `tasks` in `ai-config.yaml`: the row whose `for` list contains the Task's main Skill. Skills of one Task come from the same `tasks` row. A Skill from another row added during a Run (task-execution transition rule 5) makes `try` the item-wise higher of the two rows, longer row's tail kept; this changes `try`, so it needs Plan re-approval. `try` is the order of levels to run: `try[0]` is the start level and the last item is the maximum level. Escalation moves one item right. Without effort, each next item in `try` is a stronger model; adjacent items never repeat the same model (a repeat is not an escalation). A `try` of one item reruns at the same level (§3 rule 2). Order of levels: the position in `try`. Between rows: a stronger model is higher; with the same model, effort `low < medium < high < xhigh < max`. Model-only levels: the order of models in `sessions`, `tasks` of ai-config.yaml, weakest first. `high_risk_min` and 'never step down' use this order.

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
5. **Attempt quota:** `max_attempts` (at most 3) counts Runs of one error: the first Run and its escalations. A new error found later (step 6 tests, step 8 review) opens its own quota of up to 3 Runs (`project-rules` 18). The hard cap across all quotas is the Task's current budget (rule 6).
6. **Budget is cumulative per Task:** the Orchestrator adds the cost of every Run of the Task from `runs.md` and stops before a Run that would start over budget. The Task's **current budget** = its initial budget (`budget.initial_cost_usd`) plus the top-ups granted under rule 10, recorded in the `runs.md` ledger; `budget.max_cost_usd` always equals the current budget (rule 12). A tool's per-call limit (e.g. Claude Code `--max-budget-usd`) for the next Run is set to the current budget minus the cost so far, not the full budget. Where the tool has no limit, the Orchestrator checks after each Run. The default budget is `budget_usd_per_task`. A Task that has not been granted a top-up and has no reclaim keeps its budget at the initial amount; the Orchestrator never raises `budget.max_cost_usd` except by a top-up under rule 10 or the manifest sync under rule 12.
7. **No approval per step:** escalation within an approved `try` and budget needs no human approval; it is recorded in `runs.md`. Past the last item, attempts, or a budget that rules 10 to 12 cannot top up: stop, report the levels tried and their failures, propose next steps.
8. **Start low only when evaluation is cheap and automatic** (Tasks whose AC are all `command` checks: testing, development, refactoring, bug-fixing, caching, deployment Skills). Tasks evaluated by a human at a gate start at their default, since a failed low Run is discovered late and costs a full rerun.
9. **Warning and reassessment:** after each Run, when the cumulative cost reaches `budget_warn_pct` of the current budget, or the Run was cut at the per-call limit: no new Run starts. The Orchestrator reassesses from `runs.md` without a new Run and writes: work done, work remaining, why the cost was high, and ONE cost estimate named explicitly: `DuKienTong` (projected total: total cost of the Task from the start to done) or `DuKienThem` (extra cost still to spend from now). An unnamed estimate cannot be used in rule 10. No concrete remaining work: stop.
10. **Shortfall and conditions:** remaining = current budget - spent. If the estimate is `DuKienTong`: shortfall = max(0, DuKienTong - current budget). If it is `DuKienThem`: shortfall = max(0, DuKienThem - remaining). Both give the same result when the numbers are consistent (DuKienTong = spent + DuKienThem). Never confuse the two: do not subtract the current budget from a DuKienThem (under-grant); do not subtract `remaining` from a DuKienTong (over-grant by the amount spent); never subtract `remaining` twice. The top-up amount is the shortfall. The Orchestrator grants it from the Plan pool only when ALL hold: the Task is not `high` risk; the shortfall is within the pool balance read from the `runs.md` ledger; the Task's total top-ups plus this amount (the shortfall counted in that total) stay within `budget_topup_max_pct` of `initial_cost_usd`; the reservation of rule 11 can be written. Otherwise stop and ask a human in the `project-rules` 21 format. No pool (fast lane, or a Plan without one): no top-up, stop and ask.
11. **Reserve and serialize:** handle one top-up decision at a time, in the order the Runs ended in `runs.md`. Read the pool balance only from the ledger, never from memory. The pool balance at the start of a Plan is the amount approved in the Plan, recorded in the ledger by the opening row of step C before any reservation. Order: read the balance, check rule 10, write the reservation row in the ledger (the balance drops now), only then continue. The next decision reads the lowered balance. If two Tasks both qualify but the pool covers only one, the second is not granted a partial amount: stop and ask a human. A Task waiting for a decision starts no new Run.
12. **Sync the manifest:** after the reservation and before the next Run, set `budget.max_cost_usd` in the Task's manifest to the new current budget; never edit `budget.initial_cost_usd` or any history. Order: reservation, manifest edit, Run. If the manifest edit fails, write a row returning the reservation and do not run. This edit is not a change needing re-approval.
13. **Reclaim and ledger:** when a Task is accepted with spent below its current budget, the difference returns to the pool only after the Task has passed review step 8 (task-execution step 8, with no finding that opens a new error for this Task). Until then the difference stays inside the Task budget and the pool does not grow. A cancelled Task, or one waiting for a human, returns nothing until a human decides. Every reservation, return of a reservation, reclaim and stop-and-ask is a new row in the `runs.md` table "Điều chỉnh ngân sách"; old rows are never edited. The Orchestrator and Review budgets are not paid from the pool.

## 4. Tool settings

The values are in `ai-config.yaml`. Switching AI tool = edit `tool`, `auto_runs` and the model names there; nothing else to copy. `auto_runs: false` makes every Run attended ([task-execution](task-execution.md), "Orchestration"). When `auto_runs: true`, how to start a Run is in [ai-tools.md](../guide/ai-tools.md) §3.

Always set effort explicitly on every Run when the tool has effort; never rely on the tool's or model's default, which differs per model.

The manifest is metadata: it changes nothing unless the executor applies it. A field the tool cannot apply (e.g. effort in a tool without it; `max_output_tokens` in Claude Code) is recorded in the Run as "not applied: <field>", never silently ignored. If the tool lacks a model of the required strength, or quota runs out: stop and ask; do not downgrade.
