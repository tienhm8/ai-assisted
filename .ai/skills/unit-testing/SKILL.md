---
name: unit-testing
description: Design, write, and run isolated unit tests for business logic, functions, services, and components, traced to AC, reported with TEST-REPORT-TEMPLATE.
---

# Unit Testing Skill

Prove each code unit works correctly under normal, boundary, and error conditions; each test traces to an AC.

## Entry gate

- Task has AC. If missing, stop and ask.
- The project's test framework is decided; if not, record an open question, do not choose one yourself.

Primary sources: Task Manifest (AC → check); code under test and existing test structure.
If the manifest lacks something, look up only the exact section, do not read the whole file: testing-strategy §4 Các tầng test, §6 Thiết kế test, §9 Cổng chất lượng (Quality Gates).

## Procedure

1. **Identify test targets** from AC: pure functions, business services, validation, state transitions, components.
2. **List scenarios:** normal, boundary, invalid/empty/null input, errors, business rule violations, permission denied (if the logic checks permissions).
3. **Design tests** as Arrange / Act / Assert: one purpose, descriptive name, deterministic, independent, checks observable behavior rather than implementation details. Name or comment carries the AC ID.
4. **Mock** only external dependencies: network, external services, time, DB.
5. **Write tests** per the project's conventions, file locations, and shared utilities.
6. **Run:** targeted tests, then the related suite, then the full unit suite when needed.
7. **Coverage:** compare against the threshold in testing-strategy. Prioritize covering behavior and business rules over the number.

## Limits

- Do not modify production code just to make tests pass.

## Done when

- Each in-scope AC has a passing test; AC without tests are recorded as missing.
- Tests do not depend on run order.
- Coverage is not below the project threshold.

## Report

Fill TEST-REPORT-TEMPLATE: tests added or changed (file::name) and corresponding AC, coverage vs. threshold.
