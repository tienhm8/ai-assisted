---
name: integration-testing
description: Design and run integration tests verifying interactions between API, services, DB, and external dependencies, traced to AC, reported with TEST-REPORT-TEMPLATE.
---

# Integration Testing Skill

Prove components cooperate correctly across boundaries: API, DB, authorization, external systems.

## Entry gate

- Task has AC. If missing, stop and ask.
- An isolated test environment exists (local or disposable temporary DB). If not, record not-run with the reason and request a time-limited waiver.

Primary sources: plan (AC → test); existing test infrastructure.
If the plan lacks something, look up only the exact section, do not read the whole file: testing-strategy §4 Các tầng test, §7 Dữ liệu test (giả/ẩn danh), §10 Môi trường test; api-design §1.2 Chi tiết API (relevant endpoints); database-design §6 Transaction và đồng thời; module-design §4 Giao tiếp giữa các module; security-standards §4 Authorization.

## Procedure

1. **Identify boundaries:** API–service, service–DB, service–service, authentication–authorization, application–external system, producer–consumer.
2. **List scenarios** per AC: success, bad request, DB constraint violation, transaction failure, concurrency, timeout, external system failure, insufficient permission (wrong role, wrong owner, not logged in).
3. **Prepare the environment:** isolated test DB, migrations applied, deterministic data, fake credentials, isolated external dependencies.
4. **Write tests** checking real data flow, request/response contract, persistence, transactions and rollback, error propagation, authorization enforcement. Use real infrastructure at the boundary under test; tests carry AC IDs.
5. **Data consistency:** foreign keys, unique, atomicity, concurrent updates, duplicate requests, recovery from partial failure.
6. **Migration** (when schema changes): run from scratch on a clean DB, check the restore path.
7. **Run and classify failures:** application, environment, test data, configuration, external dependency.
8. **Clean up** test data and resources.

## Limits

- Do not use production data, even if approved.
- Do not replace integration tests entirely with mocks.
- Do not hide environment errors.

## Done when

- Each important boundary has tests for success, failure, and insufficient-permission cases.
- Tests are repeatable in the isolated environment.

## Report

Fill TEST-REPORT-TEMPLATE: boundaries and scenarios tested with AC, environment used, migration check results, data integrity findings.
