---
name: refactoring
description: Improve internal code structure, readability, modularity and maintainability while preserving existing externally observable behavior.
---

# Refactoring Skill

## 1. Objective

Improve code quality and maintainability without
changing approved business behavior.

## 2. Required Inputs

- Refactoring Task
- Existing Source Code
- Architecture Documents
- Coding Standards
- Business Requirements
- Existing Test Suite
- Known Technical Debt

## 3. Refactoring Workflow

### Step 1: Understand Existing Behavior

Identify:
- Current functionality
- Public interfaces
- Business rules
- Dependencies
- Existing test coverage
- Known edge cases

### Step 2: Identify Refactoring Targets

Consider:
- Duplicated code
- Large functions
- Large components
- High coupling
- Low cohesion
- Complex conditional logic
- Poor naming
- Unclear responsibilities
- Circular dependencies
- Difficult-to-test code

### Step 3: Establish Baseline

Before changing code:
- Run relevant tests.
- Record existing failures.
- Review current behavior.
- Identify compatibility constraints.

Do not attribute pre-existing failures to refactoring.

### Step 4: Create Refactoring Plan

Specify:
- Problem
- Desired structure
- Files affected
- Expected benefits
- Potential risks
- Tests required

### Step 5: Refactor Incrementally

Apply small, controlled changes.

Examples:
- Extract function
- Extract component
- Extract service
- Simplify conditions
- Remove duplication
- Improve naming
- Separate responsibilities
- Reduce coupling

### Step 6: Preserve Behavior

Verify:
- Inputs remain compatible.
- Outputs remain compatible.
- Business rules remain unchanged.
- Error behavior remains compatible.
- Permission boundaries remain unchanged.

### Step 7: Run Tests

Run:
- Existing unit tests
- Integration tests
- Relevant E2E tests
- Regression tests
- Static checks

### Step 8: Evaluate Improvements

Compare:
- Complexity
- Duplication
- Maintainability
- Dependency structure
- Testability

Do not claim performance improvement without measurement.

## 4. Output Format

Produce:

1. Existing Problems
2. Refactoring Objectives
3. Proposed Changes
4. Files Changed
5. Behavior Preservation Assessment
6. Tests Executed
7. Quality Improvements
8. Remaining Technical Debt

## 5. Quality Checklist

- [ ] Existing behavior is understood.
- [ ] Refactoring scope is clear.
- [ ] Baseline tests are recorded.
- [ ] Changes are incremental.
- [ ] Business rules are preserved.
- [ ] Public interfaces remain compatible.
- [ ] Permissions are unchanged.
- [ ] Regression tests pass.
- [ ] No unrelated feature is added.
- [ ] Documentation is updated if needed.

## 6. Restrictions

- Do not introduce new features.
- Do not change business behavior.
- Do not combine large refactoring with unrelated bug fixes.
- Do not remove tests simply because they are inconvenient.
- Do not perform large-scale rewrites without approval.
- Do not optimize performance without evidence.

## 7. Definition of Done

- Refactoring objectives achieved.
- Existing behavior preserved.
- Relevant tests passed.
- No new critical defects.
- Code review completed.
- Technical debt documented.

## 8. Delivery Report

Report:
- Refactoring targets
- Problems addressed
- Files changed
- Behavior preservation
- Tests executed
- Quality improvements
- Remaining technical debt
