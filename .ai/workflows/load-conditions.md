# Rule and Skill load conditions

> Status: **Approved**. Changing this file requires a dedicated Task and a reviewer.

§1 is loaded at step 1, §2 at step 3 when the chain has a `[ ]` Skill.

## 1. Rule load conditions

| Rule | Load when |
| --- | --- |
| git | Task has a commit or PR |
| coding | Editing code, including test code |
| testing | Editing code, writing or running tests, or reporting check results |
| architecture | Design; touching module or layer boundaries, API contracts; adding a module or dependency; affecting NFRs |
| database | Touching schema, migrations, queries, transactions, seeds or test data in the DB, deleting data |
| cache | Adding a cache; editing a cached read function (parameters, returned fields, tenant/permission filters, data types); adding or editing a write path (repository, bulk update, raw SQL, migration, import, job) to a table listed in database-design §3.7 |
| document-database | `database` is loaded and the DBMS is a document database (MongoDB, NoSQL) |
| security | `high`-risk Task; touching authentication, sessions, authorization; `sensitive` or `secret` data; external input, uploads; third-party integration; adding or changing a dependency; secrets, security config; release |

A Rule whose condition is met is never dropped, even for `low`-risk Tasks; risk level only changes check depth.

## 2. Conditional Skill conditions

| Skill | Use when |
| --- | --- |
| product-discovery | No vision or scope yet |
| authentication-rbac | Login, sessions, roles, permissions, or resource-level access are involved. When done, always followed by `security-review` and `integration-testing` |
| integration-testing | Touching the DB, inter-module communication, APIs, or external services |
| e2e-testing | Important user journeys or a multi-screen flow change |
| security-review | Rule `security` condition in §1 is met. Mandatory for `high`-risk Tasks |
| documentation | Changing behavior, API, schema, architecture, or operations |
| caching | Rule `cache` condition in §1 is met, unless only editing an existing write path without changing the data set it touches |
| architecture-design (draft ADR) | Data design needs partitioning, sharding, DB split, DBMS change, or a multi-tenant pattern choice |
