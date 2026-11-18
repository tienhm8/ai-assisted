---
name: task-planning
description: From a Source (Goal, Epic, User Story, or standalone request), split work into Plans and each Plan into small Tasks with one Task Manifest each (inputs, outputs, AC with checks, agent, model·effort range); draft in .ai/plans for Tech Lead approval before any Run.
---

# Task Planning Skill

Turn a Source (Goal, Epic, User Story, or standalone request) into Plans and small, verifiable Tasks, clear enough to run without guessing. AI proposes risk level, autonomy level and model·effort per Task; Tech Lead approving the Plan grants them.

## Entry gate

If missing, stop and record an open question:
- A Source: a Goal in goals.md, an Epic or User Story in product-backlog, or a standalone request from an authorized person.
- For implementation Plans: FRs with approved AC and Approved related design (architecture, API, DB). Analysis or design Plans need only the inputs their first Skill requires.

Read: work-model; the Source; goals.md; product-backlog (Epic, User Story); FR, business-rules, AC, NFR; related design docs and ADRs; task-breakdown §1, §2, §7, task-backlog, roadmap; PLAN-TEMPLATE, TASK-MANIFEST-TEMPLATE; model-effort §2; PROJECT.md §2.

## Procedure

1. **Read** the Source, the Goals it serves, the User Stories and FRs in scope, AC, BR, design; identify dependencies and sensitive areas.
2. **Split Plans** by the criteria in task-execution ("New Plan"): different output goal, independent, own lifecycle and done criteria, separate tracking or access; default one Plan per stretch ending at a gate.
3. **Split Tasks** per task-breakdown §1, using the Task type's Skill chain as template (task-types §1). Work needing a different model·effort level becomes a separate Task; adjacent Skills with the same default level may share one.
4. **Write one manifest per Task** per TASK-MANIFEST-TEMPLATE: objective, inputs, outputs, scope with allowed paths, dependencies, AC each with a check (command, file, or named human), proposed risk and autonomy level with reason, agent, Skills, Rules, document sections to load, level range and escalation from model-effort §2 (deviation needs a reason), budget, gate.
5. **Parallelize** only when Tasks share no files, schema, or contract.
6. **Draft the Plan** in `.ai/plans/PLAN-<NNN>-<slug>/` per PLAN-TEMPLATE, status Draft, with next free `PLAN-<NNN>`, exactly one Source, optional Goals. Do not write the Plan into goals.md or product-backlog (one-way links).
7. **Check Definition of Ready** per task-breakdown §7 for each Task; a Task lacking conditions stays New with an open question.
8. **Propose Tasks** into task-breakdown and task-backlog as New, with their Plan and the User Stories/FRs each serves.
9. **Submit to Tech Lead** once every point needing a decision is a complete open question. No Run until the Plan is Approved.
10. **After the Plan is done:** fill the Plan's "Kết quả" section from `runs.md`.

## Done when

- Each Plan has a Source, optional Goals, the User Stories/FRs it implements (or the reason for a technical Plan), and done criteria.
- Each Task lists what it serves (`serves`), so a Task traces to BRQ, User Story, or Goal.
- Each Task has a manifest with in/out scope, AC traced to FR with a check each, clear order and dependencies, a level range within model-effort floors.
- Tasks meet Definition of Ready or state clearly what is missing.

## Report

Proposed Plans and Tasks (IDs, manifest files), proposed risk level, autonomy level and level range per Task, Tasks not ready, `OQ-<NN>` IDs needing a decision-maker.
