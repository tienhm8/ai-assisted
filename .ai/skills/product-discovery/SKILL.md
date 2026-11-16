---
name: product-discovery
description: Turn a PO idea or brief and stakeholder documents into drafts of vision, scope, glossary, and open-questions in docs/00-project-overview; does not write BRD or FR.
---

# Product Discovery Skill

Clarify the problem, audience, and scope from real PO and stakeholder sources, written as drafts sufficient for PO approval.

## Entry gate

- A brief or source documents from the PO or stakeholders exist. If missing, stop and ask; do not invent ideas.
- Know who the PO is (approver of vision and scope).

Read: brief and existing decisions; existing vision, scope, glossary, open-questions; PROJECT.md.

## Procedure

1. **Read sources:** tag each point by source (who said it, which document). Points without a source must not be written as fact.
2. **vision:** problem, target users, measurable outcomes as `OUT-<NN>` (metric and how to measure). If not yet measurable, record an open question; do not invent numbers.
3. **scope:** in scope, out of scope, constraints. Record constraints, including legal ones, only when sourced.
4. **glossary:** terms taken from sources. For ambiguous or synonymous terms, record an open question.
5. **open-questions:** record every gap, contradiction, assumption as `OQ-<NN>` with decision-maker and deadline; assumptions have a review deadline.
6. **Cross-check:** vision, scope, glossary use the same terms and do not contradict each other.
7. **Submit to PO.** PO approves vision, scope and resolves scope-blocking open questions before moving to `requirement-analysis`.

## Limits

- Do not write BRD, FR, business rules, or technical design.

## Done when

- All four documents in Draft, with all template sections; each item has a source or is marked as an assumption.
- Each `OUT-<NN>` is measurable or has an open question.
- Scope-blocking open questions name a decision-maker.

## Report

Files created or changed, new `OUT-<NN>` and `OQ-<NN>`, sources used, assumptions and review deadlines, items needing PO approval.
