---
name: security-review
description: Assess security risk of a change or system: authentication, authorization, data handling, input, dependencies, and configuration; with real run evidence and an exception process.
---

# Security Review Skill

Find vulnerabilities and assess the effectiveness of protections, based on real run evidence when possible.

## Entry gate

- Review scope is clear (diff, module, or system), with risk level and data level. If missing, stop and ask.
- Target ASVS level is declared in PROJECT.md §4. If not, stop and ask.

Read: Task, AC; security-standards; architecture docs (roles, authorization matrix), api-design, database-design; PROJECT.md §3; source code, deployment configuration, dependency list.

## Procedure

1. **Attack surface:** public, authenticated, admin endpoints; uploads; external integrations; input entry points; where sensitive data is stored. Assign data levels.
2. **Authentication:** password storage, login, sessions, tokens, expiry, revocation, account lifecycle, rate limiting and brute-force protection.
3. **Authorization:** missing checks, privilege escalation, IDOR/BOLA, per-record permissions, role boundaries, cross-application access.
4. **Input and output:** injection (SQL, command), XSS, CSRF, SSRF, path traversal, deserialization; uploads (type, size, content, storage location, access permissions).
5. **Data protection:** sensitive data exposure, secret management, encryption in transit and at rest, backups; `secret` data in logs, URLs, error messages.
6. **Audit log:** sufficient security events and no `secret` data.
7. **Dependencies:** known vulnerabilities, end-of-life packages, excess permissions, supply chain risk.
8. **Configuration:** environment variables, DB exposure, CORS, HTTPS, security headers; pipeline and artifact integrity.
9. **Map against OWASP Top 10 and ASVS** per the mapping table in security-standards: for each item record applicable or not with reason; for applicable items check the ASVS chapters up to the project's declared level.
10. **Run real evidence:** secret scan, dependency scan, permission boundary tests (wrong role, wrong owner, not logged in). If a tool is unavailable, record not-run with the reason; not-run does not mean safe.
11. **Rate findings** by impact, likelihood, exploitability. Tag OWASP Top 10 code and ASVS requirement ID if identifiable.
12. **Handle:** for Critical/High, create a bug per BUG-TEMPLATE and notify Tech Lead, Security. If unfixed, block merge, or have an exception per security-standards §12 Quản lý ngoại lệ bảo mật. Recheck after the fix.

## Limits

- Do not test outside the permitted scope; do not exploit production.
- Do not conclude safety from reading code alone.
- Do not change security policy on your own.

## Done when

- Entire scope covered; each finding has evidence, impact, severity, remediation.
- Critical/High are fixed, merge-blocked, or have an unexpired exception.

## Report

- Scope, attack surface, data level, target ASVS level.
- OWASP Top 10 table: applicable or not, ASVS chapters checked, result.
- Evidence: commands, output; not-run with reason.
- Findings by severity, with OWASP/ASVS codes and bug IDs.
- Active exceptions; residual risk; recheck requirements.
