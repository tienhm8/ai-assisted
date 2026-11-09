---
name: requirement-analysis
description: Analyze business needs and transform them into structured, traceable software requirements, including functional requirements, business rules, user stories and acceptance criteria.
---

# Requirement Analysis Skill

## 1. Objective

Analyze business requirements and produce clear, complete,
consistent and implementable software requirements.

The output must be understandable by:
- Product Owner
- Business Analyst
- Software Architect
- Frontend Developer
- Backend Developer
- QA Engineer

## 2. Required Inputs

- Business objectives
- Existing business documentation
- Project scope
- Stakeholder requirements
- Existing FR and BR documents
- Existing system behavior
- Relevant architecture documents

## 3. Analysis Workflow

### Step 1: Understand Business Context

- Identify the business problem.
- Identify business objectives.
- Identify target users.
- Identify stakeholders.
- Identify expected business outcomes.
- Identify project scope and constraints.

### Step 2: Identify Actors

For each actor, identify:
- Actor name
- Responsibilities
- Permissions
- Business objectives
- Interactions with the system

Do not assume all actors have the same access.

### Step 3: Identify Functional Requirements

Break business needs into functional requirements.

Each requirement must include:
- Requirement ID
- Requirement name
- Description
- Actor
- Preconditions
- Main flow
- Alternative flows
- Exception flows
- Expected result

### Step 4: Identify Business Rules

Identify explicit business rules.

Examples:
- Account eligibility
- Ownership of core entities
- Approval of core entities
- Status transitions
- Data visibility
- Assignment restrictions

See [examples.md](examples.md) for project-specific examples.

Never invent business rules.

### Step 5: Identify Non-functional Requirements

Consider:
- Performance
- Scalability
- Availability
- Security
- Privacy
- Accessibility
- Maintainability
- Compatibility
- Auditability

### Step 6: Define Acceptance Criteria

Write testable acceptance criteria.

Prefer Given / When / Then format.

Each criterion must describe an observable outcome.

### Step 7: Identify Dependencies

Identify dependencies between:
- Requirements
- Modules
- APIs
- Database entities
- External services
- User roles

### Step 8: Identify Open Questions

Record:
- Ambiguous requirements
- Missing business decisions
- Conflicting requirements
- Assumptions
- Out-of-scope items

Do not silently resolve unresolved decisions.

## 4. Output Format

Produce:

1. Business Context
2. Scope and Out of Scope
3. Actors and Roles
4. Functional Requirements
5. Business Rules
6. Non-functional Requirements
7. User Stories / Use Cases
8. Acceptance Criteria
9. Dependencies
10. Assumptions
11. Open Questions
12. Traceability Matrix

## 5. Quality Checklist

- [ ] Every requirement has a unique ID.
- [ ] Requirements are specific and understandable.
- [ ] Requirements are testable.
- [ ] Business rules are explicit.
- [ ] Actors are identified.
- [ ] Permission boundaries are considered.
- [ ] Dependencies are documented.
- [ ] Open questions are recorded.
- [ ] No unsupported assumptions are presented as facts.
- [ ] Requirements are traceable to business objectives.

## 6. Restrictions

- Do not invent missing business requirements.
- Do not make unapproved business decisions.
- Do not change approved requirements.
- Do not mix functional requirements with technical implementation.
- Do not mark draft requirements as approved.
- Ask for clarification when a decision materially affects implementation.

## 7. Definition of Done

The analysis is complete when:
- Requirements are documented.
- Business rules are identified.
- Acceptance criteria are testable.
- Dependencies are identified.
- Open questions are recorded.
- Stakeholder review is possible.

## 8. Delivery Report

Report:
- Requirements analyzed
- Requirements created or updated
- Business rules identified
- Dependencies found
- Open questions
- Assumptions
- Items requiring approval
