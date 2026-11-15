---
name: frontend-development
description: Implement frontend pages, components, forms, state, and API integration per Approved requirements, UI/UX design, and API contract, with a list of cases to test and a handoff report.
---

# Frontend Development Skill

Implement the UI exactly per FR/AC, UI/UX design, and API contract; handle all loading, error, and empty states.

## Entry gate

Beyond `project-rules` 2, requires: the project's UI/UX docs and Design System; the API contract in api-design.

Primary sources: plan; UI/UX docs and Design System for the relevant screens; existing frontend code.
If the plan lacks something, look up only the exact section, do not read the whole file: api-design §1.2 Chi tiết API (relevant endpoints), §3.2 Quy ước chung; system-architecture §3.3 Các tầng và trách nhiệm; coding-standards §4 Naming Convention, §11.2 Frontend; security-standards §5 Kiểm tra đầu vào, §6.3 Che dữ liệu (masking).

## References

Load only the file of the framework the frontend uses, and read only the listed sections.

| File in `references/` | Load at step |
| --- | --- |
| `nextjs.md` (Next.js App Router only) | Step 2: §1 · Step 3: §1, §2, §5, §6 · Step 4: §4 · Step 5: §2, §3 · Step 6: §4 |

## Procedure

1. **Analyze:** users, screens, displayed data, interactions, loading/error/empty states, permission-dependent behavior.
2. **Survey existing code:** structure, routing, shared components, API call pattern. Reuse before creating new.
3. **Implement components** per coding-standards and Design System.
4. **Forms:** client-side validation only assists the user, does not replace the backend; show server validation errors; prevent duplicate submits; give feedback on success.
5. **Integrate APIs** exactly per contract; handle HTTP errors, network loss, loading.
6. **Display permissions** come from the backend or session. Hiding UI is not an authorization check. Handle session expiry and denied responses.
7. **Accessibility and responsiveness** per Design System.
8. **Cases to test:** record in plan §5, unit layer (components, forms) and e2e (main flows per AC).

## Limits

- Do not add UI libraries or duplicate shared components.
- Do not change global UI conventions until approved.
- Do not place sensitive business logic only in the frontend.

## Done when

- UI matches UI/UX and every AC; loading, error, and empty states all present.
- Cases to test from step 8 are recorded in the plan.

## Report

Write in the Task's handoff report: pages and components created or changed, APIs integrated, known limitations.
