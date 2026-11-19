# Task types: which Rules to load, which Skills to use

> Status: **Approved**. Changing this file requires a dedicated Task and a reviewer.

## 1. Routing table

AI reads only the row of the current Task type (filter command in [task-execution.md](task-execution.md)). `project-rules` is always loaded, so it is not listed. Short Rule names: `git` is `git-workflow-rules`, others are `<name>-rules`. `cache`, `document-database` load by condition for every Task type.

Skill chain notation: `→` sequential · `∥` may run in parallel · `[ ]` conditional (load-conditions §2) · `⏸` wait for approver.

The Skill chain is the template for splitting a Plan into Tasks (task-execution step 3): one Task per Skill, or several adjacent Skills of the same default level in one Task; each `⏸` ends a Task and usually a Plan. Model and effort are set per Task from its Skills ([model-effort.md](model-effort.md) §2), not per Task type.

| Type | Task type | Rules always loaded | Conditional Rules (load-conditions §1) | Skill chain | Template |
| --- | --- | --- | --- | --- | --- |
| `new-feature` | New feature (no FR, AC yet) | architecture | database, security, git | [product-discovery] → requirement-analysis → requirement-review → ⏸ PO/BA → architecture-design ∥ database-design → [caching] → ⏸ Architect → task-planning → ⏸ Tech Lead → `feature` Tasks | PLAN, ADR |
| `feature` | Feature implementation (FR, AC, design exist) | git, coding, architecture, testing | database, security | [authentication-rbac] → backend-development → [caching] → api-development ∥ frontend-development → unit-testing → [integration-testing] → [e2e-testing] → [security-review] → code-review → [documentation] | PLAN, TEST-REPORT, DELIVERY-REPORT |
| `bug-fix` | Bug fix | git, coding, testing | architecture, database, security | bug-fixing → [caching] → [integration-testing / e2e-testing] → [security-review] → code-review → [documentation] | BUG (input), DELIVERY-REPORT |
| `refactor` | Refactor | git, coding, architecture, testing | database | unit-testing (baseline) → refactoring → unit-testing / integration-testing (compare) → code-review | PLAN, DELIVERY-REPORT |
| `schema-change` | Schema change | git, database, architecture, testing | security, coding | database-design → [caching] → integration-testing → code-review → documentation | PLAN, DELIVERY-REPORT |
| `requirement-change` | Requirement change | — | architecture, git | requirement-analysis → requirement-review → ⏸ PO/BA → affected `feature`/`schema-change` Tasks | — |
| `architecture-change` | Architecture or contract change | architecture | database, security, git | architecture-design → ⏸ Architect (ADR) → affected `feature`/`schema-change` Tasks → documentation | ADR, PLAN |
| `requirement-review` | Requirement document review | — | — | requirement-review | — |
| `pr-review` | Review Pull Request | coding, architecture, testing | database, security, git | code-review → [security-review] | PR (input), DELIVERY-REPORT |
| `security-check` | Security check | security, coding | database, architecture | security-review → bug-fixing (Critical/High findings) → security-review (recheck) | DELIVERY-REPORT |
| `tests-only` | Tests only | git, coding, testing | database, security | unit-testing / integration-testing / e2e-testing (by layer) | TEST-REPORT, DELIVERY-REPORT |
| `docs-only` | Documentation only | git | architecture | documentation | DELIVERY-REPORT |
| `release` | Release | git, security, testing | database | [security-review if not done] → deployment (prepare) → ⏸ Owner → executor → documentation | TEST-REPORT, RELEASE-REPORT |
| `incident` | Production incident | security | database, architecture | incident-analysis → separate `bug-fix` Task to fix → continuous-improvement | BUG |
| `periodic-review` | Periodic review | — | — | continuous-improvement → separate Task for each Rule/Skill change proposal | — |

The Skill chain is the default; the Plan may drop or add Skills, with a reason in the manifest.

- **Order:** analysis and design before code; tests with or right after code; `code-review`, `security-review` after diff and test results exist; `documentation` once behavior is stable.
- **`new-feature` → `feature` is not automatic:** needs PO/BA approval (every FR has AC) and Architect approval (design Approved).
- **`feature`:** `backend-development` does services and business logic; `api-development` does contract, validation, handlers. An API that only forwards to an existing service uses only `api-development`. `api-development` ∥ `frontend-development` only when the API contract is Approved.
- **`code-review`** is never dropped when the Task has a diff.
