# Code Review – Security checklist (priority 6)

## Priority 6: Security (per OWASP Top 10)

Quickly check common bugs visible in the diff:

- Missing backend authorization checks, especially per-record authorization (fetching by ID without checking ownership: IDOR/BOLA).
- Assigning all input to an object (mass assignment/over-posting) instead of accepting only validated fields.
- Injection: string concatenation into queries, system commands, templates, path expressions.
- Output not encoded/escaped for context (XSS).
- Returning or logging sensitive fields, secrets, tokens, D3 data.
- Upload: no check of type, size, content, storage location.
- Calling user-supplied URLs (SSRF); file paths from input (path traversal).
- Missing rate limits at sensitive points (login, OTP, password reset).
