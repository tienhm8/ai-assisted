---
name: e2e-testing
description: Design and execute end-to-end tests that verify complete user journeys and critical business workflows across the application.
---

# E2E Testing Skill

## 1. Objective

Verify that complete user journeys work correctly
from the user's perspective.

## 2. Required Inputs

- User Stories
- Acceptance Criteria
- Business Workflows
- UI/UX Specifications
- API Specifications
- RBAC Matrix
- Test Environment
- Existing browser automation configuration

## 3. Testing Workflow

### Step 1: Identify User Journeys

Identify critical workflows such as:
- User registration and email verification
- Login and logout
- Creating, updating and approving core business entities
- Search
- Customer request or contact flows
- Internal management workflows

See [examples.md](examples.md) for project-specific journeys.

### Step 2: Define Test Personas

Define test accounts representing each role in the RBAC matrix,
plus an unauthenticated visitor.

Use only approved permissions for each persona.

See [examples.md](examples.md) for project-specific personas.

### Step 3: Define Test Scenarios

For each journey include:
- Preconditions
- User actions
- Expected UI behavior
- Expected system response
- Expected data changes
- Failure behavior

### Step 4: Implement E2E Tests

Use the project's approved browser automation framework.

Prefer stable selectors:
- Accessible roles
- Labels
- Test IDs where appropriate

Avoid fragile selectors tied to visual layout.

### Step 5: Test Negative Scenarios

Test:
- Invalid input
- Unauthorized access
- Forbidden actions
- Expired sessions
- Invalid state transitions
- Network failures
- Duplicate submissions

### Step 6: Manage Test Data

- Create deterministic test data.
- Avoid shared mutable test records.
- Isolate parallel tests.
- Clean up test data safely.
- Avoid production environments.

### Step 7: Execute Tests

Run:
- Targeted E2E tests
- Critical workflow suite
- Regression suite

Capture screenshots, traces and logs when failures occur.

### Step 8: Analyze Failures

Distinguish:
- Application bugs
- UI timing issues
- Environment problems
- Test data problems
- Flaky tests

Do not blindly increase timeouts to hide failures.

## 4. Output Format

Produce:
1. User Journeys
2. Personas
3. Test Scenarios
4. E2E Test Files
5. Test Data Strategy
6. Execution Results
7. Failure Evidence
8. Regression Coverage

## 5. Quality Checklist

- [ ] Critical user journeys are covered.
- [ ] All relevant roles are represented.
- [ ] Positive and negative flows are tested.
- [ ] Permission boundaries are verified.
- [ ] Test data is isolated.
- [ ] Selectors are stable.
- [ ] Tests are reproducible.
- [ ] Failure evidence is captured.
- [ ] Flaky tests are investigated.

## 6. Restrictions

- Never execute destructive E2E tests on production.
- Never use real customer credentials.
- Never weaken assertions to hide failures.
- Never bypass authentication or authorization in tests.
- Do not create unnecessary end-to-end tests for every small function.

## 7. Definition of Done

- Critical workflows are covered.
- E2E tests execute successfully.
- Failures are investigated.
- Regression tests are maintained.
- Test evidence is available.

## 8. Delivery Report

Report:
- User journeys tested
- Roles tested
- Tests passed / failed / skipped
- Screenshots and traces
- Known flaky tests
- Remaining gaps
