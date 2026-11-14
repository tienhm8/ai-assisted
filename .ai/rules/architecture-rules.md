# Architecture Rules

> Status: **Approved**. Mandatory Rule, architecture-neutral.

1. If the relevant design section is still Draft or empty: stop and ask; do not assume layers, style, or technology.
2. Respect declared layers and module boundaries: do not skip layers, do not access another module's data or internals directly, do not create circular dependencies.
3. An exception to a layer or module boundary is also an architecture change: AI only drafts an ADR (status Proposed); the Architect approves it before coding.
4. Do not put business logic in the presentation layer, and the presentation layer must not access data directly (if the project has a presentation layer).
5. APIs match the approved specification; breaking changes require an ADR.
6. Changes affecting performance, availability, or security must be checked against the non-functional requirements (NFR).
