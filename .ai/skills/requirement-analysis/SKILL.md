---
name: requirement-analysis
description: Analyze business needs into traceable software requirements (BRQ, Epic, Feature, User Story, FR, business rules, NFR, acceptance criteria) and write them into the correct requirement documents; unclear points go into open-questions.
---

# Requirement Analysis Skill

Turn business needs into clear, testable, traceable requirements, sufficient for architects, developers, and QA.

## Entry gate

- Vision and scope are Approved, or there is an approved stakeholder source registered as `SRC-<NN>`. If vision and scope are missing, switch to `product-discovery`.

Read: existing vision, scope, BRD, features, product-backlog (Epic, User Story), FR, business-rules, NFR, acceptance-criteria; glossary; open-questions (apply `Closed` answers, do not re-ask); sources index and registered sources.

## Conventions

- IDs: `SRC-<NN>`, `BRQ-<NN>`, `EPIC-<NN>`, `FEAT-<NN>`, `US-<MODULE>-<NN>`, `FR-<MODULE>-<NN>`, `BR-<MODULE>-<NN>`, `NFR-<NN>`, `<FR>-AC<N>`, `OQ-<NN>`.
- Every BRQ and BR cites its `SRC-<NN>` and section; a BR whose source is a customer answer cites the answer's `SRC-<NN>`.
- Concepts and links: work-model §2–§3. Links are many-to-many references, not a tree. Plan and Task (group B) never appear in requirement documents or the product backlog.
- One-way traceability: Feature holds BRQs; Epic holds BRQs and Goals; User Story holds Epic, Features, FRs; FR holds BRQ, Feature, and BR; AC points to the FR and BR it verifies. Do not declare the reverse direction; do not build a separate traceability matrix.

## Procedure

1. **Context:** problem, goals, users, scope and out of scope, constraints. Record goals in the BRD.
2. **Actors:** roles, responsibilities, permissions; do not assume all actors have the same permissions.
3. **Feature, Epic, User Story:** Features in `01-requirements/features.md`; Epics and User Stories ("Là <vai>, tôi muốn…, để…", roles from the glossary) in `04-project-management/product-backlog.md`. Do not invent any of them without a BRQ; do not create Goals (owner's decision), only propose them as open questions.
4. **FR:** write into the FR table of `FR/FR-<MODULE>.md`, one sentence per FR. Only high-risk or ambiguous FRs get extra detail (preconditions, main flow, error flows) below the table.
5. **Business rule:** write into business-rules only with an approved source, stating the source. Without a source, record an open question.
6. **NFR:** each NFR has a metric and how to measure; if not measurable, record an open question.
7. **AC:** Given / When / Then form, observable results; include error flows and boundary values.
8. **Dependencies** between FRs, modules, APIs, data entities, external services, roles: record at the relevant FR.
9. **Unclear points:** ambiguities, missing decisions, contradictions, assumptions all go into open-questions with a type (`Input`, `Clarify`, `Decision`); assumptions have a review deadline. Questions for the customer go through the liaison as a question pack (open-questions §"Hỏi khách hàng qua đầu mối"). When the customer must confirm a process, screens or rules, draft one confirmation pack per topic from [CONFIRMATION-PACK-TEMPLATE](../../templates/CONFIRMATION-PACK-TEMPLATE.md) (scope, process, wireframe or mockup per screen, rules, questions, sign-off); it holds the question pack. Wireframes show layout and content only: no invented fields, rules or numbers; each unsure point gets a numbered pin and an `OQ-<NN>`. The BA exports it with `python3 -I .ai/scripts/export-pack.py`.

## Limits

- Do not mix FRs with technical implementation details.
- Changing an Approved FR must record change history (date, FR, change, reason, approver).

## Done when

- Every Feature and Epic has a BRQ; every User Story an Epic and at least one FR.
- Every FR has a BRQ source, a Feature, and AC; every BR has a source and AC.
- Every NFR is measurable; IDs are unique; terms match the glossary.
- Ready to move to `requirement-review`.

## Report

Requirements created or changed (by ID and file), BRs and their `SRC-<NN>`, new `OQ-<NN>` by type, question pack for the liaison (if any), assumptions and review deadlines, items needing an approver. Do not repeat content already in the documents.
