---
name: authentication-rbac
description: Implement and review authentication, authorization, RBAC, session management and resource-level permission checks per the Approved access policy; deny by default, check on the backend.
---

# Authentication & RBAC Skill

Implement authentication and authorization exactly per the approved policy, enforced on the backend, deny by default. `high`-risk work by default.

## Entry gate

Besides `project-rules` 2, the design must have a role model, permission matrix, session policy. Undecided parts are open questions; do not infer them.

**Changing** the role model, permissions or session policy: stop, requires Tech Lead and Security approval. Before modifying auth files, check the project's zone map.

Primary sources: Task Manifest (and the Plan points it cites); existing authentication and authorization code.
If the manifest lacks something, look up the exact section, do not read the whole file: system-architecture §6 Authentication & Authorization (design); security-standards §3 Authentication, §4 Authorization, §9 Logging và Audit; api-design §4 Authentication & Authorization; error-handling §5.2 Ánh xạ HTTP status.

## Procedure

1. **Read the approved policy:** authentication method, roles, permissions, resource scope, session boundaries, account lifecycle.
2. **Authentication** per the approved architecture: registration, login, logout, passwords, account status.
3. **Backend authorization:** check role, permission, ownership, scope; deny by default. Do not assume any role has all permissions.
4. **Application boundaries:** if the system has multiple applications, keep access boundaries and session policy per spec; block cross-application access.
5. **Sessions** per security-standards, including expiry and revocation.
6. **Permission-boundary test cases:** record in the Run handoff for Plan §7, integration layer (e2e if needed). Cover: unauthenticated, wrong role, wrong owner, out of scope, expired or revoked session, client-supplied fake role, cross-application access. Response codes per error-handling.

## Done when

- Every in-scope resource has backend permission checks, deny by default.
- Test cases from step 6 are recorded in the Run handoff.

## Report

Write in the Task's handoff report: changes to authentication, roles, permissions, sessions; protected resources.
