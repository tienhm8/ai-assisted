---
name: bug-fixing
description: Investigate software defects, identify root causes, implement minimal safe fixes and verify corrections with regression tests.
---

# Bug Fixing Skill

## 1. Objective

Resolve software defects accurately while minimizing
unintended changes and regression risks.

## 2. Required Inputs

- Bug Report
- Steps to Reproduce
- Expected Behavior
- Actual Behavior
- Error Messages
- Logs and Stack Traces
- Relevant Source Code
- Related Requirements
- Existing Test Cases

## 3. Bug Fixing Workflow

### Step 1: Understand the Bug

Identify:
- Bug ID
- Affected feature
- Environment
- User role
- Preconditions
- Reproduction steps
- Expected result
- Actual result
- Frequency

### Step 2: Reproduce the Bug

Attempt to reproduce the issue.

Record:
- Input data
- User actions
- API requests
- API responses
- Browser console errors
- Server logs
- Database state where appropriate

Do not claim reproduction if it was not successful.

### Step 3: Investigate Root Cause

Inspect:
- Related components
- Business logic
- API behavior
- Database queries
- Authentication
- Authorization
- Configuration
- External dependencies

Identify the actual cause.

Distinguish root cause from symptoms.

### Step 4: Assess Impact

Determine:
- Affected modules
- Affected user roles
- Data integrity risks
- Security implications
- Related workflows
- Potential regressions

### Step 5: Propose Fix

Define:
- Root cause
- Proposed correction
- Files affected
- Risks
- Required tests

For critical changes, request human approval.

### Step 6: Implement Minimal Fix

- Fix the root cause.
- Minimize scope.
- Preserve existing behavior.
- Avoid unrelated refactoring.
- Follow project rules.

### Step 7: Add Regression Test

Create a test that:
- Reproduces the original defect.
- Fails before the fix where feasible.
- Passes after the fix.
- Verifies related edge cases.

### Step 8: Run Tests

Execute:
- Relevant unit tests
- Integration tests
- E2E tests where appropriate
- Related regression tests
- Relevant static checks

### Step 9: Review Changes

Verify:
- Root cause is addressed.
- No workaround hides the problem.
- No unrelated changes exist.
- Existing behavior remains correct.

## 4. Output Format

Produce:

1. Bug Summary
2. Reproduction Results
3. Root Cause
4. Impact Analysis
5. Proposed Fix
6. Files Changed
7. Regression Tests
8. Test Execution Results
9. Remaining Risks

## 5. Quality Checklist

- [ ] Bug is understood.
- [ ] Reproduction is documented.
- [ ] Root cause is identified.
- [ ] Impact is assessed.
- [ ] Fix addresses the root cause.
- [ ] Changes are minimal.
- [ ] Regression test is added.
- [ ] Related tests pass.
- [ ] No unrelated changes.
- [ ] Documentation is updated if necessary.

## 6. Restrictions

- Do not randomly modify code.
- Do not suppress errors to hide defects.
- Do not disable failing tests.
- Do not alter business rules without approval.
- Do not modify production data to bypass the bug.
- Do not claim a fix is verified without executing tests.
- Stop when the root cause cannot be established reliably.

## 7. Definition of Done

- Root cause identified.
- Fix implemented.
- Regression test added.
- Relevant tests executed.
- No unresolved critical regression.
- Results documented.

## 8. Delivery Report

Report:
- Bug ID
- Root cause
- Fix summary
- Files changed
- Regression tests
- Test results
- Remaining risks
