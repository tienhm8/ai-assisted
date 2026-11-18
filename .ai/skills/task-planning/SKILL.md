---
name: task-planning
description: For a Goal, split work into Plans and each Plan into small Tasks with one Task Manifest each (inputs, outputs, AC with checks, agent, model·effort range); draft in .ai/plans for Tech Lead approval before any Run.
---

# Task Planning Skill

Turn a Goal into Plans and small, verifiable Tasks, clear enough to run without guessing. AI proposes risk level, autonomy level and model·effort per Task; Tech Lead approving the Plan grants them.

## Entry gate

If missing, stop and record an open question:
- A Goal in goals.md (or a drafted one awaiting its owner).
- For implementation Plans: FRs with approved AC and Approved related design (architecture, API, DB). Analysis or design Plans need only the inputs their first Skill requires.

Read: goals.md; FR, business-rules, AC, NFR; related design docs and ADRs; task-breakdown §1, §2, §7, backlog, roadmap; PLAN-TEMPLATE, TASK-MANIFEST-TEMPLATE; model-effort §2; PROJECT.md §2.

## Procedure

1. **Read** the Goal, FR, AC, BR, design; identify dependencies and sensitive areas.
2. **Split Plans** by the criteria in goals.md §2: different output goal, independent, own lifecycle and done criteria, separate tracking or access; default one Plan per stretch ending at a gate.
3. **Split Tasks** per task-breakdown §1, using the Task type's Skill chain as template (task-types §1). Work needing a different model·effort level becomes a separate Task; adjacent Skills with the same default level may share one.
4. **Write one manifest per Task** per TASK-MANIFEST-TEMPLATE: objective, inputs, outputs, scope with allowed paths, dependencies, AC each with a check (command, file, or named human), proposed risk and autonomy level with reason, agent, Skills, Rules, document sections to load, level range and escalation from model-effort §2 (deviation needs a reason), budget, gate.
5. **Parallelize** only when Tasks share no files, schema, or contract.
6. **Draft the Plan** in `.ai/plans/<GOAL>-P<N>-<slug>/` per PLAN-TEMPLATE, status Draft; add the Plan to the Goal's row in goals.md.
7. **Check Definition of Ready** per task-breakdown §7 for each Task; a Task lacking conditions stays New with an open question.
8. **Propose Tasks** into task-breakdown and backlog as New, with their Plan.
9. **Submit to Tech Lead** once every point needing a decision is a complete open question. No Run until the Plan is Approved.
10. **After the Plan is done:** fill the Plan's "Kết quả" section from `runs.md`.

## Done when

- Each Plan belongs to a Goal and has done criteria.
- Each Task has a manifest with in/out scope, AC traced to FR with a check each, clear order and dependencies, a level range within model-effort floors.
- Tasks meet Definition of Ready or state clearly what is missing.

## Report

Proposed Plans and Tasks (IDs, manifest files), proposed risk level, autonomy level and level range per Task, Tasks not ready, `OQ-<NN>` IDs needing a decision-maker.
