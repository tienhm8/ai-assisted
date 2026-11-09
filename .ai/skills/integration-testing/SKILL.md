---
name: integration-testing
description: Design and execute integration tests to verify correct interactions between application components, APIs, databases and external dependencies.
---

# Integration Testing Skill

## 1. Objective

Verify that integrated system components work correctly
across defined interfaces and boundaries.

## 2. Required Inputs

- Architecture Documents
- API Specifications
- Database Schema
- Business Rules
- Integration Contracts
- Authentication and RBAC Requirements
- Test Environment
- Existing Test Infrastructure

## 3. Testing Workflow

### Step 1: Identify Integration Boundaries

Identify:
- API to service
- Service to database
- Service to service
- Authentication to authorization
- Application to external services
- Event producer to consumer

### Step 2: Identify Test Scenarios

Consider:
- Successful interactions
- Invalid requests
- Database constraint violations
- Transaction failures
- Concurrent operations
- Timeout scenarios
- External service failures
- Permission failures

### Step 3: Prepare Test Environment

- Use isolated test databases.
- Apply required migrations.
- Prepare deterministic test data.
- Configure test credentials.
- Isolate external dependencies.

Never use production data without explicit approval.

### Step 4: Implement Integration Tests

Verify:
- Actual data flow
- Request and response contracts
- Database persistence
- Transaction behavior
- Rollback behavior
- Error propagation
- Authorization enforcement

Use real infrastructure components where needed
to verify the integration boundary.

### Step 5: Test Data Consistency

Check:
- Foreign key integrity
- Unique constraints
- Transaction atomicity
- Concurrent updates
- Duplicate requests
- Partial failure recovery

### Step 6: Execute and Analyze

Run relevant integration suites.

Investigate failures by identifying:
- Application defects
- Environment defects
- Test data defects
- Configuration defects
- External dependency failures

### Step 7: Cleanup

Ensure test data and resources are cleaned up safely.

## 4. Output Format

Produce:
1. Integration Boundaries
2. Test Scenarios
3. Test Data
4. Environment Configuration
5. Test Cases
6. Execution Results
7. Failure Analysis
8. Remaining Risks

## 5. Quality Checklist

- [ ] All critical integration boundaries are covered.
- [ ] Database interactions are verified.
- [ ] Transactions are tested.
- [ ] Error propagation is tested.
- [ ] Authentication and authorization are tested.
- [ ] External failure scenarios are covered.
- [ ] Test data is isolated.
- [ ] Cleanup is safe.
- [ ] Tests are reproducible.

## 6. Restrictions

- Never use production data by default.
- Do not replace all integration tests with mocks.
- Do not ignore database constraint failures.
- Do not suppress environment-related failures without reporting.
- Do not modify production configuration.

## 7. Definition of Done

- Critical integration scenarios are tested.
- Tests execute in an isolated environment.
- Results are reproducible.
- Failures are resolved or documented.
- Relevant regressions are covered.

## 8. Delivery Report

Report:
- Integration boundaries tested
- Test scenarios
- Environment used
- Tests passed / failed / skipped
- Data integrity findings
- Remaining risks
