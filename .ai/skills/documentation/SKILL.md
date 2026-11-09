---
name: documentation
description: Create, update and maintain accurate software documentation aligned with approved requirements, architecture, source code and operational behavior.
---

# Documentation Skill

## 1. Objective

Maintain accurate, consistent, structured and
up-to-date project documentation.

## 2. Required Inputs

- Project Documentation
- Functional Requirements
- Business Rules
- Architecture Documents
- Database Schema
- API Specifications
- Source Code
- Change History
- Task Specification

## 3. Documentation Workflow

### Step 1: Identify Documentation Scope

Determine whether the change affects:
- README
- Project Overview
- Functional Requirements
- Business Rules
- Architecture
- Database Design
- API Documentation
- Authentication and RBAC
- Coding Standards
- Deployment
- Operations
- Troubleshooting

### Step 2: Verify Information Sources

Use the following precedence:

1. Approved business decisions.
2. Approved requirements.
3. Approved architecture and ADRs.
4. Current implementation.
5. Existing documentation.

If sources conflict, report the conflict.

Do not silently treat implementation behavior as
an approved business requirement.

### Step 3: Create or Update Documentation

Follow:
- Existing document structure
- Naming conventions
- Requirement IDs
- Markdown conventions
- Cross-reference conventions
- Versioning conventions

### Step 4: Maintain Traceability

Link documentation to:
- Requirement IDs
- Business Rule IDs
- Architecture decisions
- API endpoints
- Database entities
- Related Tasks

### Step 5: Record Decisions

For significant technical decisions:
- Create or update ADR.
- Document context.
- Document alternatives.
- Document decision.
- Document consequences.
- Record approval status.

### Step 6: Validate Documentation

Check:
- Accuracy
- Completeness
- Consistency
- Links
- Code examples
- API examples
- Diagrams
- Status labels

### Step 7: Prevent Documentation Drift

Compare documentation against:
- Actual source code
- Current database schema
- API implementation
- Approved requirements

Identify outdated statements.

## 4. Output Format

Produce:

1. Documents Created
2. Documents Updated
3. Change Summary
4. Requirement Traceability
5. Decisions Recorded
6. Conflicts Found
7. Outdated Information
8. Remaining Documentation Gaps

## 5. Quality Checklist

- [ ] Documents reflect approved decisions.
- [ ] Technical descriptions match implementation.
- [ ] Requirement IDs are preserved.
- [ ] Business rules are accurate.
- [ ] Architecture references are correct.
- [ ] Links are valid.
- [ ] Examples are consistent.
- [ ] Open questions remain open.
- [ ] Draft and approved statuses are clear.
- [ ] No unsupported claims are added.

## 6. Restrictions

- Do not invent business decisions.
- Do not mark documents approved without authorization.
- Do not delete historical decisions without justification.
- Do not duplicate authoritative documentation.
- Do not silently resolve conflicting sources.
- Do not update unrelated documents unnecessarily.

## 7. Definition of Done

- Required documentation is updated.
- Information is verified.
- Traceability is preserved.
- Conflicts are reported.
- Relevant links are validated.
- Review requirements are satisfied.

## 8. Delivery Report

Report:
- Files created
- Files updated
- Changes made
- References updated
- Conflicts
- Remaining gaps
