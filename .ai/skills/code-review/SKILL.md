---
name: code-review
description: Perform structured code reviews to identify correctness, maintainability, architecture, performance, security and testing issues before code is merged.
---

# Code Review Skill

## 1. Objective

Review code changes against requirements, architecture
and engineering standards.

## 2. Required Inputs

- Task Specification
- Approved Requirements
- Business Rules
- Architecture Documents
- Project Rules
- Coding Standards
- Security Rules
- Git Diff
- Test Results

## 3. Review Workflow

### Step 1: Understand the Change

Identify:
- Task objective
- Scope
- Changed files
- Affected modules
- Related requirements
- Expected behavior

### Step 2: Review Correctness

Check:
- Business logic
- Input validation
- Edge cases
- State transitions
- Error handling
- Data consistency

### Step 3: Review Architecture

Check:
- Layer boundaries
- Module responsibilities
- Dependency direction
- Reusability
- Coupling
- Duplication

### Step 4: Review Code Quality

Check:
- Naming
- Readability
- Complexity
- Maintainability
- Type safety
- Dead code
- Unnecessary abstractions

### Step 5: Review Security

Check:
- Authentication
- Authorization
- Input validation
- Sensitive information
- SQL injection
- XSS
- CSRF where applicable
- Resource access boundaries

### Step 6: Review Performance

Check:
- Database query patterns
- N+1 problems
- Unnecessary computations
- Memory usage
- Unnecessary network calls
- Rendering performance

### Step 7: Review Tests

Check:
- Tests match requirements.
- Important branches are covered.
- Negative cases are tested.
- Tests are meaningful.
- No assertions are weakened.
- Reported results have evidence.

### Step 8: Report Findings

Classify findings:

- Critical: Severe correctness or security issue.
- High: Major defect or significant risk.
- Medium: Maintainability or functional issue.
- Low: Minor improvement.
- Informational: Non-blocking observation.

Every finding must identify the affected file and location
where possible.

## 4. Output Format

Produce:

1. Review Summary
2. Critical Findings
3. High Findings
4. Medium Findings
5. Low Findings
6. Positive Observations
7. Test Assessment
8. Merge Recommendation

## 5. Quality Checklist

- [ ] Changes satisfy the Task.
- [ ] No unrelated changes.
- [ ] Architecture is respected.
- [ ] Business logic is correct.
- [ ] Error handling is appropriate.
- [ ] Security is considered.
- [ ] Performance is acceptable.
- [ ] Tests are meaningful.
- [ ] Documentation is updated.
- [ ] No unresolved critical findings.

## 6. Restrictions

- Do not approve code with unresolved critical issues.
- Do not assume code is correct because tests pass.
- Do not rewrite unrelated code during review.
- Do not invent defects without technical evidence.
- Do not approve your own changes as an independent reviewer.

## 7. Definition of Done

The review is complete when:
- Findings are documented.
- Severity is assigned.
- Required corrections are identified.
- Test evidence is evaluated.
- Merge recommendation is provided.

## 8. Delivery Report

Report:
- Files reviewed
- Findings by severity
- Required fixes
- Tests evaluated
- Merge recommendation
