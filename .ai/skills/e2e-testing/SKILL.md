---
name: e2e-testing
description: Design and run end-to-end tests for critical user journeys, traced to E2E-type ACs, reported with TEST-REPORT-TEMPLATE.
---

# E2E Testing Skill

Prove critical journeys work correctly from the user's perspective.

## Entry gate

- The Task has E2E-type ACs; journeys come from them. If missing, stop and ask.
- A runtime environment with fake data exists. If not, record not-run with the reason and request a time-limited waiver.

Primary sources: plan (E2E-type AC → test); existing browser automation config.
If the plan lacks something, look up the exact section, do not read the whole file: testing-strategy §4 Các tầng test, §7 Dữ liệu test (giả/ẩn danh), §8 Tự động hoá test; api-design §4 Authentication & Authorization; security-standards §4.2 Phân quyền theo vai trò.

## Procedure

1. **Identify journeys** from E2E-type ACs.
2. **Personas:** one test account per role in the authorization matrix, plus an unauthenticated guest.
3. **Describe scenarios** for each journey: preconditions, actions, expected UI behavior, data changes, behavior on error.
4. **Write tests**; stable selectors (role, label, test id), not tied to layout. Tests carry the AC ID.
5. **Negative cases:** invalid input, unauthorized access, forbidden actions, expired session, invalid state transitions, network errors, duplicate submission.
6. **Data:** deterministic, no shared mutable records, isolated in parallel runs, cleaned up after runs.
7. **Run:** targeted tests, the critical-journey suite, regression. On failure capture screenshots, traces, logs.
8. **Classify failures:** application, UI timing, environment, test data, flaky.

## Limits

- Do not increase timeouts to mask failures.
- Do not bypass authentication or authorization in tests.
- Do not write E2E for each small function; that belongs to unit or integration.

## Done when

- Each in-scope journey has passing tests for positive and negative flows, covering all relevant roles.
- Tests are repeatable; flaky tests have been investigated.

## Report

Fill in TEST-REPORT-TEMPLATE: tested journeys and roles with ACs, screenshots or traces on failure, known flaky tests.
