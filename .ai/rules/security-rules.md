# Security Rules

> Status: **Approved**. Mandatory Rule. Cannot be lowered; an exception requires a reason, compensating controls, an approver, and an expiry date.

1. Authorization is checked server-side; do not trust permissions sent by the client; deny by default when permissions are not declared.
2. Check permissions on the actual record being accessed, not only the role.
3. Use parameterized queries and context-aware output encoding; do not concatenate input into queries.
4. Do not hardcode secrets; get secrets from an approved store. A leaked secret is considered compromised: report immediately.
5. Apply least privilege to users, services, and DB accounts.
6. Log security events: successful/failed logins, permission changes, denied access, security configuration changes.
7. When dependencies change, run vulnerability scanning and license checks; every commit runs secret scanning.
8. Do not disable or relax security checks (lint, scan, authentication) to make tests pass.
9. Changes to authorization, money, personal data, or migrations require Tech Lead and Security approval. AI does not manage secrets on its own.
10. Tools given to AI (MCP servers, plugins) do not connect to production or `sensitive`/`secret` data.
