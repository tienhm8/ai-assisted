---
name: api-development
description: Implement or modify backend API endpoints exactly per the Approved contract in api-design.md, including validation, authorization guards, error mapping, test case list and handoff report.
---

# API Development Skill

Implement endpoints exactly per the Approved contract: validate input, apply authorization guards, return errors per the standard mapping. Do not create or change contracts yourself.

## Entry gate

Besides `project-rules` 2, required: the endpoint's contract in api-design; related schema in database-design (if missing, stop and report).

Primary sources: plan; existing API code.
If the plan lacks something, look up the exact section, do not read the whole file: api-design §1.2 Chi tiết API (related endpoints), §3.2 Quy ước chung, §4 Authentication & Authorization; database-design §3.3 Chi tiết bảng (related tables); module-design §5 Ranh giới và quyền sở hữu; error-handling §3 Mã lỗi, §5 Phản hồi lỗi API; security-standards §5 Kiểm tra đầu vào, §8 Bảo mật API.

## Procedure

1. **Read** FR/AC, business rules, contract; identify the actor and permission requirements.
2. **Check the contract** against the requirements. If missing or conflicting, stop and record an open question; changing the contract requires approval.
3. **Implement** following the project's existing conventions: input validation → thin handler calling a service → return response or error per error-handling. Business logic lives in the service and belongs to `backend-development`.
4. **Authorization:** apply existing guards per the permission matrix; do not define permissions yourself.
5. **Test cases:** record in plan §5 with layer (unit, integration; e2e if an AC requires it). Cover: success, invalid or missing input, unauthenticated, wrong permission, access to another user's resource, business rule violation, DB interaction errors.

## Done when

- The endpoint matches every detail of the contract, including pagination, sorting, filtering and idempotency if the contract specifies them.
- Error codes and error format follow error-handling; responses return no sensitive fields beyond the contract.
- Test cases from step 5 are recorded in the plan.

## Report

Write in the Task's handoff report: endpoints implemented or modified and the referenced contract.
