---
name: backend-development
description: Implement backend business logic, services, data processing, integrations and background operations following approved architecture and security requirements.
---

# Backend Development Skill

## 1. Objective

Build reliable, secure, maintainable and testable
backend components.

## 2. Required Inputs

- Functional Requirements
- Business Rules
- Architecture Documents
- Database Schema
- API Specifications
- Security Requirements
- Existing Backend Code
- Relevant Skills and Rules

## 3. Development Workflow

### Step 1: Analyze Business Logic

Identify:
- Business operations
- Actors
- Preconditions
- Business constraints
- State transitions
- Expected results
- Failure scenarios

### Step 2: Inspect Existing Backend

Review:
- Framework
- Application structure
- Service layer
- Repository/data access layer
- Shared utilities
- Existing integrations
- Error handling
- Logging conventions

### Step 3: Design Service Responsibilities

Define:
- Service responsibilities
- Input and output
- Dependencies
- Business validation
- Transaction boundaries
- Error behavior

Keep business logic independent from presentation
and transport layers where appropriate.

### Step 4: Implement Business Logic

- Follow approved business rules.
- Use existing services where appropriate.
- Keep responsibilities focused.
- Avoid duplicated logic.
- Handle state transitions explicitly.
- Validate critical business invariants.

### Step 5: Implement Data Access

- Follow approved database schema.
- Use parameterized queries or safe ORM methods.
- Handle transactions appropriately.
- Avoid N+1 queries.
- Respect data ownership.
- Avoid unnecessary data retrieval.

### Step 6: Handle Errors

Distinguish:
- Validation errors
- Business rule violations
- Authentication errors
- Authorization errors
- Resource not found
- Conflict errors
- External service failures
- Unexpected system errors

Do not expose internal stack traces to clients.

### Step 7: Logging and Observability

Log relevant events:
- Business operations
- Failed operations
- Integration failures
- Security-relevant events
- Performance anomalies

Never log passwords, tokens or unnecessary sensitive data.

### Step 8: External Integrations

Consider:
- Timeouts
- Retry policies
- Idempotency
- Rate limits
- Circuit breaking where appropriate
- Failure recovery
- Data consistency

### Step 9: Testing

Write:
- Unit tests
- Integration tests
- Business rule tests
- Failure scenario tests
- Transaction tests

## 4. Output Format

Produce:
1. Business Logic Summary
2. Services Implemented
3. Data Access Changes
4. Transaction Handling
5. Error Handling
6. Integrations
7. Logging
8. Tests
9. Documentation Updates

## 5. Quality Checklist

- [ ] Business rules are implemented correctly.
- [ ] Service responsibilities are clear.
- [ ] Database access is safe.
- [ ] Transactions are appropriate.
- [ ] Errors are handled explicitly.
- [ ] Permissions are enforced.
- [ ] Sensitive information is protected.
- [ ] External failures are handled.
- [ ] No unnecessary queries.
- [ ] Tests pass.

## 6. Restrictions

- Do not invent business rules.
- Do not bypass authorization.
- Do not access production data without approval.
- Do not expose internal errors.
- Do not silently change database schema.
- Do not introduce unnecessary services or abstractions.

## 7. Definition of Done

- Business logic implemented.
- Data integrity preserved.
- Error handling implemented.
- Security requirements satisfied.
- Tests executed.
- Documentation updated.
- Changes reviewed.

## 8. Delivery Report

Report:
- Services created or modified
- Business logic implemented
- Database interactions
- Integrations
- Tests executed
- Risks and limitations
