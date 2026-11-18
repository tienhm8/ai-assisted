# Task types: which Rules to load, which Skills to use

> Status: **Approved**. Changing this file requires a dedicated Task and a reviewer.

## 1. Routing table

AI reads only the row of the current Task type (filter command in [task-execution.md](task-execution.md)). `project-rules` is always loaded, so it is not listed. Short Rule names: `git` is `git-workflow-rules`, others are `<name>-rules`. `cache`, `document-database` load by condition for every Task type.

Skill chain notation: `→` sequential · `∥` may run in parallel · `[ ]` conditional (load-conditions §2) · `⏸` wait for approver.

The Skill chain is the template for splitting a Plan into Tasks (task-execution step 3): one Task per Skill, or several adjacent Skills of the same default level in one Task; each `⏸` ends a Task and usually a Plan. Model and effort are set per Task from its Skills ([model-effort.md](model-effort.md) §2), not per Task type.

| # | Task type | Rules always loaded | Conditional Rules (load-conditions §1) | Skill chain | Template |
| --- | --- | --- | --- | --- | --- |
| T1 | New feature (no FR, AC yet) | architecture | database, security, git | [product-discovery] → requirement-analysis → requirement-review → ⏸ PO/BA → architecture-design ∥ database-design → [caching] → ⏸ Architect → task-planning → ⏸ Tech Lead → T2 Tasks | PLAN, ADR |
| T2 | Feature implementation (FR, AC, design exist) | git, coding, architecture, testing | database, security | [authentication-rbac] → backend-development → [caching] → api-development ∥ frontend-development → unit-testing → [integration-testing] → [e2e-testing] → [security-review] → code-review → [documentation] | PLAN, TEST-REPORT, DELIVERY-REPORT |
| T3 | Bug fix | git, coding, testing | architecture, database, security | bug-fixing → [caching] → [integration-testing / e2e-testing] → [security-review] → code-review → [documentation] | BUG (input), DELIVERY-REPORT |
| T4 | Refactor | git, coding, architecture, testing | database | unit-testing (baseline) → refactoring → unit-testing / integration-testing (compare) → code-review | PLAN, DELIVERY-REPORT |
| T5 | Schema change | git, database, architecture, testing | security, coding | database-design → [caching] → integration-testing → code-review → documentation | PLAN, DELIVERY-REPORT |
| T6 | Requirement change | — | architecture, git | requirement-analysis → requirement-review → ⏸ PO/BA → affected T2/T5 Tasks | — |
| T7 | Architecture or contract change | architecture | database, security, git | architecture-design → ⏸ Architect (ADR) → affected T2/T5 Tasks → documentation | ADR, PLAN |
| T8 | Requirement document review | — | — | requirement-review | — |
| T9 | Review Pull Request | coding, architecture, testing | database, security, git | code-review → [security-review] | PR (input), DELIVERY-REPORT |
| T10 | Security check | security, coding | database, architecture | security-review → bug-fixing (Critical/High findings) → security-review (recheck) | DELIVERY-REPORT |
| T11 | Tests only | git, coding, testing | database, security | unit-testing / integration-testing / e2e-testing (by layer) | TEST-REPORT, DELIVERY-REPORT |
| T12 | Documentation only | git | architecture | documentation | DELIVERY-REPORT |
| T13 | Release | git, security, testing | database | [security-review if not done] → deployment (prepare) → ⏸ Owner → executor → documentation | TEST-REPORT, RELEASE-REPORT |
| T14 | Production incident | security | database, architecture | incident-analysis → separate T3 Task to fix → continuous-improvement | BUG |
| T15 | Periodic review | — | — | continuous-improvement → separate Task for each Rule/Skill change proposal | — |

The Skill chain is the default; the Plan may drop or add Skills, with a reason in the manifest.

- **Order:** analysis and design before code; tests with or right after code; `code-review`, `security-review` after diff and test results exist; `documentation` once behavior is stable.
- **T1 → T2 is not automatic:** needs PO/BA approval (every FR has AC) and Architect approval (design Approved).
- **T2:** `backend-development` does services and business logic; `api-development` does contract, validation, handlers. An API that only forwards to an existing service uses only `api-development`. `api-development` ∥ `frontend-development` only when the API contract is Approved.
- **`code-review`** is never dropped when the Task has a diff.
