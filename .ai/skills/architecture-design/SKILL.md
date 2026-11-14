---
name: architecture-design
description: Design and evaluate software architecture (system boundaries, modules, data flow, security, technology decisions) based on approved requirements; record in architecture docs and ADRs.
---

# Architecture Design Skill

Propose the simplest architecture that meets the approved requirements: maintainable, secure, testable.

## Entry gate

FRs have ACs, with related BRs and NFRs. If not met, stop and record an open question.

Read: vision, scope, FR/BR/NFR; existing architecture, chosen technologies, security requirements. Read database-design and api-design only if they exist.

## Procedure

1. **Analyze requirements:** business capabilities, actors, quality attributes, integrations, technical constraints.
2. **System boundaries:** applications, modules, external services, trust boundaries, data owners.
3. **Architecture style:** choose the simplest option that meets requirements; a distributed option must be justified by NFRs.
4. **Modules:** responsibility, inputs/outputs, dependencies, owned data, interfaces, error boundaries, FRs served. Record as a table in module-design.
5. **Data flow:** request, authentication, authorization, business processing, data access, external integration, error handling.
6. **Security boundaries:** authentication, where authorization is enforced, service permissions, sensitive data.
7. **Quality evaluation:** maintainability, reliability, performance, scalability, security, observability, testability.
8. **ADR:** for each major decision create `ADR-<NNNN>-<slug>.md` from `_template.md`, status Proposed, add to the ADR index. Design docs record only the outcome and cite the ADR ID.
9. **Review existing architecture** (project already has code): boundary violations, circular dependencies, duplicated responsibilities, excess coupling.

## Limits

- Do not change chosen technologies.
- Write directly into system-architecture, module-design, api-design; do not create a parallel architecture report.

## Done when

- Every module traces to an FR; boundaries, data ownership and security boundaries are clear.
- Major decisions have a Proposed ADR in the index.
- Approver: Architect; add Security if it touches money, authorization, personal data or migrations.

## Report

Files modified, affected modules, ADRs created, trade-offs and risks, required approvers. Do not repeat doc content.
