---
name: requirement-analysis
description: Analyze business needs into traceable software requirements (BRQ, FR, business rules, NFR, acceptance criteria) and write them into the correct requirement documents; unclear points go into open-questions.
---

# Requirement Analysis Skill

Turn business needs into clear, testable, traceable requirements, sufficient for architects, developers, and QA.

## Entry gate

- Vision and scope are Approved, or there is an approved stakeholder source. If vision and scope are missing, switch to `product-discovery`.

Read: existing vision, scope, BRD, FR, business-rules, NFR, acceptance-criteria; glossary; open-questions; stakeholder sources.

## Conventions

- IDs: `BRQ-<NN>`, `FR-<MODULE>-<NN>`, `BR-<MODULE>-<NN>`, `NFR-<NN>`, `<FR>-AC<N>`, `OQ-<NN>`.
- One-way traceability: FR holds links to BRQ and BR; AC points to the FR and BR it verifies. Do not declare the reverse direction; do not build a separate traceability matrix.

## Procedure

1. **Context:** problem, goals, users, scope and out of scope, constraints. Record goals in the BRD.
2. **Actors:** roles, responsibilities, permissions; do not assume all actors have the same permissions.
3. **FR:** write into the FR table of `FR/FR-<MODULE>.md`, one sentence per FR. Only high-risk or ambiguous FRs get extra detail (preconditions, main flow, error flows) below the table.
4. **Business rule:** write into business-rules only with an approved source, stating the source. Without a source, record an open question.
5. **NFR:** each NFR has a metric and how to measure; if not measurable, record an open question.
6. **AC:** Given / When / Then form, observable results; include error flows and boundary values.
7. **Dependencies** between FRs, modules, APIs, data entities, external services, roles: record at the relevant FR.
8. **Unclear points:** ambiguities, missing decisions, contradictions, assumptions all go into open-questions; assumptions have a review deadline.

## Limits

- Do not mix FRs with technical implementation details.
- Changing an Approved FR must record change history (date, FR, change, reason, approver).

## Done when

- Every FR has a BRQ source and AC; every BR has a source and AC.
- Every NFR is measurable; IDs are unique; terms match the glossary.
- Ready to move to `requirement-review`.

## Report

Requirements created or changed (by ID and file), BRs and sources, new `OQ-<NN>`, assumptions and review deadlines, items needing an approver. Do not repeat content already in the documents.
