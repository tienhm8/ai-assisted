---
name: backend-development
description: Implement backend business logic, services, data access, integrations and background jobs within Approved module boundaries and design, with a test case list and handoff report.
---

# Backend Development Skill

Implement backend business logic, data access and integrations: correct business rules, correct module boundaries, easy to test.

## Entry gate

Besides `project-rules` 2, required: related business rules; design including module-design, database-design, and the api-design contract if there are endpoints or external integrations.

Primary sources: Task Manifest (and the Plan points it cites); existing backend code.
If the manifest lacks something, look up the exact section, do not read the whole file: module-design §3 Phụ thuộc giữa các module, §5 Ranh giới và quyền sở hữu; system-architecture §3.3 Các tầng và trách nhiệm; database-design §6 Transaction và đồng thời; api-design §1.2 Chi tiết API (related endpoints), §2 Integration Specification; error-handling §3 Mã lỗi, §4 Xử lý exception, §7 Logging, §8 Retry, timeout, fallback, §9 Transaction và nhất quán dữ liệu; security-standards §4 Authorization, §5 Kiểm tra đầu vào, §9 Logging và Audit.

## References

Load the file matching ai-config.yaml `stack`; if `stack` lacks the entry, ask. Read only the listed sections.

| File in `references/` | Load at step |
| --- | --- |
| `nestjs.md` (NestJS only) | Step 2: §1 · Step 3: §1, §2 · Step 4: §3, §5, §6 · Step 5: §4 · Step 8: §7 |
| `prisma.md` (Prisma ORM only) | Step 2: §1 · Step 3: §1 · Step 4: §2, §3, §4 · Step 5: §5 |
| `sequelize.md` (Sequelize only) | Step 2: §1 · Step 3: §1 · Step 4: §2, §3, §4 · Step 5: §5 |

## Procedure

1. **Analyze:** business operations, actors, preconditions, constraints, state transitions, error scenarios.
2. **Survey existing code:** structure, services, data access layer, shared utilities, error handling and logging. Reuse before creating new.
3. **Design services:** responsibility, inputs/outputs, dependencies, transaction boundaries. Module boundaries per module-design.
4. **Implement:** explicit state transitions; check key invariants; avoid N+1 queries.
5. **Errors and logging:** per error-handling; log business events, failures and security events.
6. **External integrations:** timeout, retry, idempotency, rate limit per the spec in api-design; if the spec is missing, stop and record an open question.
7. **Authorization:** use existing permission-check mechanisms; if missing, handle per task-execution, section "Step transition rules" item 5 (A condition arises); do not add them yourself.
8. **Test cases:** record in the Run handoff for Plan §7 cases covering business rules, error scenarios, transactions, with layer (unit, integration).

## Limits

- If a schema change is needed, stop and report; do not change it yourself.
- Do not add services or abstractions the Task does not need.

## Done when

- Logic satisfies every AC and related business rule; no cross-module calls contrary to the design.
- Transactions cover all writes that must succeed or fail together.
- Test cases from step 8 are recorded in the Run handoff.

## Report

Write in the Task's handoff report: services created or modified, DB interactions, external integrations.
