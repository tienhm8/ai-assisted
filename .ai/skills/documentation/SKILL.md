---
name: documentation
description: Create and update project docs (requirements, architecture, engineering, management, operations, draft ADRs) to match approved decisions and the current system; do not set Approved yourself, do not decide business logic yourself.
---

# Documentation Skill

Keep docs consistent with approved decisions and the real system, without duplication.

## Entry gate

- The Task states the changes to document. If missing, stop and ask.
- The source (approved decision, requirement, design) can be identified. If there is no source, record an open question; do not fill it in yourself.

Read: Task, diff or change description, related existing docs, related ADRs.

## Procedure

1. **Identify affected docs:**

   | Change | Doc |
   | --- | --- |
   | Behavior, business rules, AC | `01-requirements` |
   | Architecture, schema, API, modules | `02-architecture` |
   | Coding standards, security, testing, error handling | `03-engineering` |
   | Goals, Epics, User Stories, Tasks, progress, KPI | `04-project-management` |
   | Deployment, monitoring, backup | `05-operations` |
   | Open questions, assumptions | open-questions |

2. **Verify sources** in priority order: approved business decisions, Approved requirements, Approved designs and ADRs, then current code and old docs. Current code does not by itself become a requirement. If sources conflict, report; do not choose yourself.
3. **Write or update** per the project's structure, naming and standard IDs; keep existing IDs unchanged.
4. **Single source:** each rule, decision, status is managed in only one place; other places reference it by ID.
5. **One-way traceability** per work-model §3 (links, not a tree): Goal → Source (BRQ/OUT/strategy/request); Feature → BRQs; Epic → BRQs, Goals; User Story → Epic, Features, FRs; FR → BRQ, Feature, BR; AC → FR; Plan → Source, Goals; Task → Plan, User Stories/FRs. Do not create back-links.
6. **ADR**, only when the decision requires an ADR per the ADR folder's guidance: create `ADR-<NNNN>-<slug>.md` from `_template.md` with the next number, status Proposed, at least two options; add one row to the index. Small, easily reversible decisions go in the design doc.
7. **Check drift:** compare docs with existing code, schema, API; list outdated, conflicting and missing parts.

## Limits

- Do not delete historical decisions without a reason.
- Do not modify docs outside the Task's scope.

## Done when

- Every affected doc is updated or has a recorded reason it is not needed.
- No content is duplicated in two places; standard IDs are kept.
- ADRs (if any) are Proposed and in the index.

## Report

Write in the Task's handoff report: docs created or modified, ADRs created, source conflicts, outdated spots and remaining gaps.
