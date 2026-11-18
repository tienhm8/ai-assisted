---
name: product-discovery
description: Turn a PO idea or brief and stakeholder documents into drafts of vision, scope, glossary, and open-questions in docs/00-project-overview; does not write BRD or FR.
---

# Product Discovery Skill

Clarify the problem, audience, and scope from real PO and stakeholder sources, written as drafts sufficient for PO approval.

## Entry gate

- A brief or source documents from the PO or stakeholders exist, registered as `SRC-<NN>` in `docs/00-project-overview/sources/`. Unregistered: list them for registration. Marked "Chưa ẩn danh" (not anonymized): do not open; ask for an anonymized copy. Missing: record an `Input` open question and stop; do not invent ideas.
- Know who the PO is (approver of vision and scope).

Read: sources index and registered sources; existing vision, scope, glossary, open-questions; PROJECT.md (§3 data levels, §5 roles).

## Procedure

1. **Read sources:** tag each point by `SRC-<NN>` and section/page. Points without a source must not be written as fact. Missing documents, ambiguous or contradicting passages become open questions typed `Input` or `Clarify`.
2. **vision:** problem, target users, measurable outcomes as `OUT-<NN>` (metric and how to measure). If not yet measurable, record an open question; do not invent numbers.
3. **scope:** in scope, out of scope, constraints. Record constraints, including legal ones, only when sourced.
4. **glossary:** terms taken from sources. For ambiguous or synonymous terms, record an open question.
5. **open-questions:** record every gap, contradiction, assumption as `OQ-<NN>` with type (`Input`, `Clarify`, `Decision`), decision-maker and deadline; assumptions have a review deadline. If PROJECT.md §5 names a customer representative, draft a question pack per open-questions §"Hỏi khách hàng qua đầu mối" for the liaison; never contact the customer directly.
6. **Cross-check:** vision, scope, glossary use the same terms and do not contradict each other.
7. **Submit to PO.** PO approves vision, scope and resolves scope-blocking open questions before moving to `requirement-analysis`.

## Limits

- Do not write BRD, FR, business rules, or technical design.

## Done when

- All four documents in Draft, with all template sections; each item has a source or is marked as an assumption.
- Each `OUT-<NN>` is measurable or has an open question.
- Scope-blocking open questions name a decision-maker.

## Report

Files created or changed, new `OUT-<NN>` and `OQ-<NN>`, `SRC-<NN>` used, question pack for the liaison (if any), assumptions and review deadlines, items needing PO approval.
