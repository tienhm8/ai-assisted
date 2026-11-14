# Task types: which Rules to load, which Skills to use

> Status: **Approved**. Changing this file requires a dedicated Task and a reviewer.

## 1. Routing table

AI reads only the row of the current Task type (filter command in [task-execution.md](task-execution.md)). `project-rules` is always loaded, so it is not listed. Short Rule names: `git` is `git-workflow-rules`, others are `<name>-rules`. `cache`, `document-database` load by condition for every Task type.

Skill chain notation: `→` sequential · `∥` may run in parallel · `[ ]` conditional (load-conditions §2) · `⏸` wait for approver.

| # | Task type | Rules always loaded | Conditional Rules (load-conditions §1) | Skill chain | Template | Model · Effort (plan / execution) |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | New feature (no FR, AC yet) | architecture | database, security, git | [product-discovery] → requirement-analysis → requirement-review → ⏸ PO/BA → architecture-design ∥ database-design → [caching] → ⏸ Architect → task-planning → ⏸ Tech Lead → T2 Tasks | PLAN, ADR | M3·E3 / — |
| T2 | Feature implementation (FR, AC, design exist) | git, coding, architecture, testing | database, security | [authentication-rbac] → backend-development → [caching] → api-development ∥ frontend-development → unit-testing → [integration-testing] → [e2e-testing] → [security-review] → code-review → [documentation] | PLAN, TEST-REPORT, DELIVERY-REPORT | M3·E3 / M2·E2 |
| T3 | Bug fix | git, coding, testing | architecture, database, security | bug-fixing → [caching] → [integration-testing / e2e-testing] → [security-review] → code-review → [documentation] | BUG (input), DELIVERY-REPORT | M2·E3 / M2·E3 |
| T4 | Refactor | git, coding, architecture, testing | database | unit-testing (baseline) → refactoring → unit-testing / integration-testing (compare) → code-review | PLAN, DELIVERY-REPORT | M2·E3 / M2·E2 |
| T5 | Schema change | git, database, architecture, testing | security, coding | database-design → [caching] → integration-testing → code-review → documentation | PLAN, DELIVERY-REPORT | M3·E3 / M2·E3 |
| T6 | Requirement change | — | architecture, git | requirement-analysis → requirement-review → ⏸ PO/BA → affected T2/T5 Tasks | — | M2·E3 / — |
| T7 | Architecture or contract change | architecture | database, security, git | architecture-design → ⏸ Architect (ADR) → affected T2/T5 Tasks → documentation | ADR, PLAN | M3·E4 / — |
| T8 | Requirement document review | — | — | requirement-review | — | M2·E2 / — |
| T9 | Review Pull Request | coding, architecture, testing | database, security, git | code-review → [security-review] | PR (input), DELIVERY-REPORT | M3·E3 / — |
| T10 | Security check | security, coding | database, architecture | security-review → bug-fixing (Critical/High findings) → security-review (recheck) | DELIVERY-REPORT | M3·E3 / M2·E3 |
| T11 | Tests only | git, coding, testing | database, security | unit-testing / integration-testing / e2e-testing (by layer) | TEST-REPORT, DELIVERY-REPORT | M2·E2 / M2·E2 |
| T12 | Documentation only | git | architecture | documentation | DELIVERY-REPORT | M2·E2 / M2·E1 |
| T13 | Release | git, security, testing | database | [security-review if not done] → deployment (prepare) → ⏸ Owner → executor → documentation | TEST-REPORT, RELEASE-REPORT | M2·E2 / M2·E2 |
| T14 | Production incident | security | database, architecture | incident-analysis → separate T3 Task to fix → continuous-improvement | BUG | M3·E3 / per T3 |
| T15 | Periodic review | — | — | continuous-improvement → separate Task for each Rule/Skill change proposal | — | M2·E2 / — |

The Skill chain is the default; the plan may drop or add Skills, with a reason.

- **Order:** analysis and design before code; tests with or right after code; `code-review`, `security-review` after diff and test results exist; `documentation` once behavior is stable.
- **T1 → T2 is not automatic:** needs PO/BA approval (every FR has AC) and Architect approval (design Approved).
- **T2:** `backend-development` does services and business logic; `api-development` does contract, validation, handlers. An API that only forwards to an existing service uses only `api-development`. `api-development` ∥ `frontend-development` only when the API contract is Approved.
- **`code-review`** is never dropped when the Task has a diff.
