---
name: requirement-review
description: Review requirements for completeness, clarity, consistency, testability, and traceability before design/implementation; recommend only, do not change status or edit documents.
---

# Requirement Review Skill

Find gaps, contradictions, ambiguities, and risks in requirements. Propose only in the report: do not edit requirement files.

## Entry gate

Requirement documents to review (BRD, features, product-backlog, FR table, AC) exist in Draft or In Review. If missing, stop and ask.

Read: work-model §3; BRD, features, product-backlog, FR table, business-rules, NFR, acceptance-criteria, scope, glossary, open-questions, relevant architecture docs if any.

## Procedure

1. **Completeness:** main, alternative, error flows; input validation; outputs; permissions; data ownership; state transitions.
2. **Clarity:** unambiguous sentences, terms match glossary, clear actors, measurable constraints.
3. **Consistency:** FR vs. BR, vs. NFR, vs. scope, vs. authorization, vs. existing decisions, across FRs.
4. **Testability:** AC observable, with preconditions and results, with boundaries and error flows.
5. **One-way traceability:** each BRQ and BR cites a `SRC-<NN>`; each Feature and Epic links to BRQs, each User Story to an Epic and FRs; each FR links to BRQ/Feature/BR; each Must/Should BRQ has at least one FR (filter the "BRQ nguồn" column of the FR table); each AC points to an FR; every BR has AC. A requirement document or product backlog naming Plan or Task, or a document declaring two-way links, is a finding.
6. **Open questions:** which scope each `Open`/`Asked` question blocks; `Asked` questions past their deadline; assumptions past their review deadline; ambiguities without an open question.
7. **Feasibility:** only flag risks (technical, integration, data, performance, security) to hand to `architecture-design`; do not make architecture decisions.
8. **Classify findings:** Critical (blocks implementation) · High (major gap or contradiction) · Medium (unclear) · Low (documentation improvement).

## Done when

All seven aspects above reviewed; each finding has all fields; the report states the recommendation and unmet conditions.

## Report

One report: number of requirements reviewed, finding count by level, finding list, blocking issues, approval recommendation.

- Each finding: ID `FND-<NN>` (used only within this report), severity, related requirement ID, description, impact, proposed fix.
- Recommend approval when: every FR has AC, QA has reviewed, no scope-blocking open questions remain.
