---
name: task-planning
description: From FRs with AC and Approved design, draft a Draft plan in .ai/plans and propose small Tasks for task-breakdown and backlog for Tech Lead approval before assigning work.
---

# Task Planning Skill

Split approved requirements into a plan and small, verifiable Tasks, clear enough to assign without guessing. AI proposes; Tech Lead approves the plan and assigns risk level and autonomy level.

## Entry gate

If missing, stop and record an open question:
- FRs with approved AC.
- Related design (architecture, API, DB) is Approved.

Read: FR, business-rules, AC, NFR; related design docs and ADRs; task-breakdown, backlog, roadmap; PLAN-TEMPLATE; PROJECT.md §2.

## Procedure

1. **Read** FR, AC, BR, design; identify dependencies and sensitive areas.
2. **Split Tasks** per the principles in task-breakdown: small, single responsibility; split Tasks that mix work types.
3. **Fill each Task:** goal, scope (in and out), AC, dependencies, estimate, risk level and autonomy level as a proposal with rationale.
4. **Parallelize** only when Tasks share no files, schema, or contract.
5. **Draft the plan** in `.ai/plans/` per PLAN-TEMPLATE, status Draft.
6. **Check Definition of Ready** per task-breakdown for each Task; do not assign a Task that lacks conditions, record an open question.
7. **Propose Tasks** into task-breakdown and backlog as Proposed.
8. **Submit to Tech Lead** once every point needing a decision is a complete open question. Do not assign work until approved.
9. **After a Task is done:** fill the plan's "Kết quả" section.

## Done when

- Each Task has in/out scope, AC traced to FR, clear order and dependencies.
- The plan has tests for every AC.
- Tasks meet Definition of Ready or state clearly what is missing.

## Report

Proposed plan and Tasks (IDs, files), proposed risk level and autonomy level, Tasks not ready, `OQ-<NN>` IDs needing a decision-maker.
