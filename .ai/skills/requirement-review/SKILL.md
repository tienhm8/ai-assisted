---
name: requirement-review
description: Review software requirements for completeness, consistency, clarity, feasibility, testability and traceability before implementation.
---

# Requirement Review Skill

## 1. Objective

Evaluate the quality of existing requirements and identify
gaps, contradictions, ambiguities and implementation risks.

## 2. Required Inputs

- BRD
- Functional Requirements
- Non-functional Requirements
- Business Rules
- User Stories
- Acceptance Criteria
- Scope documentation
- Related architecture documents

## 3. Review Workflow

### Step 1: Completeness Review

Check whether requirements cover:
- Main business flows
- Alternative flows
- Exception flows
- Input validation
- Output behavior
- User permissions
- Data ownership
- State transitions
- Error handling

### Step 2: Clarity Review

Check whether:
- Statements are unambiguous.
- Terms are consistently defined.
- Actors are explicitly identified.
- Expected outcomes are clear.
- Constraints are measurable.

### Step 3: Consistency Review

Compare:
- FR against BR
- FR against NFR
- Requirements against project scope
- Requirements against RBAC
- Requirements against existing decisions
- Related requirements against each other

### Step 4: Testability Review

Verify:
- Acceptance criteria are observable.
- Expected results are defined.
- Preconditions are specified.
- Boundary cases are considered.
- Failure scenarios are testable.

### Step 5: Feasibility Review

Evaluate:
- Technical feasibility
- Integration dependencies
- Data availability
- Performance constraints
- Security implications
- Implementation complexity

Do not make architecture decisions without authorization.

### Step 6: Traceability Review

Check whether each requirement has:
- Unique ID
- Business objective
- Related business rules
- Related modules
- Acceptance criteria
- Planned test coverage

### Step 7: Risk Assessment

Classify findings:

- Critical: Blocks implementation or creates serious risk.
- High: Major requirement gap or conflict.
- Medium: Incomplete or unclear behavior.
- Low: Documentation improvement.

## 4. Output Format

Produce a review report:

1. Review Summary
2. Completeness Findings
3. Ambiguity Findings
4. Inconsistency Findings
5. Missing Requirements
6. Missing Acceptance Criteria
7. Traceability Findings
8. Risks
9. Recommended Corrections
10. Approval Recommendation

## 5. Review Checklist

- [ ] Scope is clear.
- [ ] All actors are identified.
- [ ] Main flows are documented.
- [ ] Exception flows are documented.
- [ ] Business rules are complete.
- [ ] Permissions are specified.
- [ ] Data requirements are clear.
- [ ] Acceptance criteria are testable.
- [ ] Requirements do not contradict each other.
- [ ] Dependencies are documented.
- [ ] Open decisions remain explicitly open.

## 6. Restrictions

- Do not silently rewrite approved requirements.
- Do not convert assumptions into approved requirements.
- Do not invent missing business behavior.
- Do not approve requirements on behalf of stakeholders.
- Preserve original requirement IDs where possible.

## 7. Definition of Done

Every finding must include:
- Finding ID
- Severity
- Related requirement
- Problem description
- Impact
- Recommended correction

## 8. Delivery Report

Report:
- Total requirements reviewed
- Critical findings
- High findings
- Medium findings
- Low findings
- Blocking issues
- Approval recommendation
