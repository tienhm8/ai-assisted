---
name: unit-testing
description: Design, implement and execute isolated unit tests for business logic, functions, services and components using the project's approved testing framework.
---

# Unit Testing Skill

## 1. Objective

Verify that individual units behave correctly
under expected and unexpected conditions.

## 2. Required Inputs

- Functional Requirements
- Business Rules
- Acceptance Criteria
- Source Code
- Existing Test Structure
- Testing Standards
- Approved Test Framework

## 3. Testing Workflow

### Step 1: Identify Test Targets

Identify:
- Pure functions
- Business services
- Validation functions
- Utility functions
- Components
- State transformations

### Step 2: Identify Test Scenarios

For each target identify:
- Normal cases
- Boundary cases
- Invalid inputs
- Empty inputs
- Null or undefined values
- Error cases
- Business rule violations

### Step 3: Design Test Cases

Use Arrange / Act / Assert.

Each test should:
- Have one clear purpose.
- Use descriptive names.
- Be deterministic.
- Be independent.
- Verify observable behavior.

### Step 4: Mock Dependencies

Mock external dependencies when necessary.

Examples:
- Network calls
- External services
- Time-dependent operations
- Database access in isolated unit tests

Do not mock the actual business logic under test.

### Step 5: Implement Tests

Follow:
- Existing test conventions
- Naming conventions
- Test file locations
- Shared test utilities

Avoid unnecessary test duplication.

### Step 6: Execute Tests

Run:
- Targeted unit tests
- Related test suite
- Full unit test suite when appropriate

Capture actual execution results.

### Step 7: Evaluate Coverage

Review:
- Statement coverage
- Branch coverage
- Function coverage
- Critical business rule coverage

Prioritize meaningful behavior coverage over arbitrary percentages.

## 4. Output Format

Produce:
1. Test Target
2. Test Scenarios
3. Test Cases
4. Test Files
5. Execution Results
6. Coverage Information
7. Failed Tests
8. Remaining Gaps

## 5. Quality Checklist

- [ ] Normal cases are tested.
- [ ] Boundary cases are tested.
- [ ] Invalid inputs are tested.
- [ ] Error scenarios are tested.
- [ ] Business rules are covered.
- [ ] Tests are isolated.
- [ ] Tests are deterministic.
- [ ] Assertions verify actual behavior.
- [ ] Tests are maintainable.
- [ ] Execution results are recorded.

## 6. Restrictions

- Do not modify production code merely to satisfy incorrect tests.
- Do not weaken assertions to make tests pass.
- Do not skip failing tests without justification.
- Do not claim tests passed without execution.
- Do not overuse mocks.

## 7. Definition of Done

- Relevant test cases implemented.
- Tests executed successfully.
- Failures investigated.
- Coverage gaps documented.
- No unreported skipped tests.

## 8. Delivery Report

Report:
- Test files created or modified
- Test scenarios
- Tests executed
- Passed / Failed / Skipped
- Coverage results
- Remaining gaps
