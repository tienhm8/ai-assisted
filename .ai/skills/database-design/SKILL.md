---
name: database-design
description: Design, evaluate and modify relational database schemas, relationships, constraints, indexes and migrations based on approved business requirements.
---

# Database Design Skill

## 1. Objective

Design reliable, consistent, performant and maintainable
database structures.

## 2. Required Inputs

- Approved Functional Requirements
- Business Rules
- Existing Database Schema
- Data Model
- Architecture Documents
- API Data Requirements
- Data Retention Requirements

## 3. Design Workflow

### Step 1: Identify Data Entities

Identify:
- Main entities
- Supporting entities
- Lookup entities
- Transaction entities
- Relationship entities
- Audit entities

### Step 2: Define Attributes

For every attribute specify:
- Name
- Data type
- Nullability
- Default value
- Validation constraints
- Business meaning
- Sensitivity classification

### Step 3: Define Relationships

Identify:
- One-to-one
- One-to-many
- Many-to-many

Define:
- Primary keys
- Foreign keys
- Referential actions
- Unique constraints

### Step 4: Apply Data Integrity Rules

Consider:
- NOT NULL
- UNIQUE
- CHECK
- FOREIGN KEY
- Appropriate defaults
- Transaction boundaries

Do not rely only on frontend validation.

### Step 5: Evaluate Normalization

Evaluate:
- First Normal Form
- Second Normal Form
- Third Normal Form

Use denormalization only when justified by measured
performance or explicit architectural requirements.

### Step 6: Design Indexes

Consider:
- Frequently filtered columns
- Join columns
- Sorting columns
- Composite indexes
- Unique indexes

Avoid unnecessary indexes.

### Step 7: Design Migrations

Every schema change must include:
- Migration script
- Expected database state
- Data transformation if required
- Deployment considerations
- Rollback strategy where feasible

Consider backward compatibility during deployment.

### Step 8: Evaluate Performance

Review:
- Query patterns
- N+1 query risks
- Large table scans
- Pagination
- Index utilization
- Transaction duration

### Step 9: Review Security

Consider:
- Least privilege
- Sensitive data
- Access boundaries
- Data retention
- Backup requirements
- Auditability

## 4. Output Format

Produce:

1. Entity List
2. ERD
3. Table Definitions
4. Column Definitions
5. Relationships
6. Constraints
7. Index Strategy
8. Migration Scripts
9. Data Integrity Rules
10. Performance Considerations
11. Security Considerations

## 5. Quality Checklist

- [ ] All entities map to requirements.
- [ ] Primary keys are defined.
- [ ] Foreign keys are defined.
- [ ] Unique constraints are appropriate.
- [ ] Nullability is correct.
- [ ] Data types are appropriate.
- [ ] Indexes support query patterns.
- [ ] Migration is included.
- [ ] Existing data is protected.
- [ ] Sensitive data is handled appropriately.
- [ ] Rollback or recovery strategy is considered.

## 6. Restrictions

- Never modify production data directly.
- Never delete existing columns without impact analysis.
- Never change schema without migration.
- Never remove constraints to bypass errors.
- Do not invent relationships.
- Do not expose sensitive data unnecessarily.

## 7. Definition of Done

The design is complete when:
- ERD is documented.
- Schema is reviewed.
- Constraints are defined.
- Index strategy is justified.
- Migration is prepared.
- Data integrity is verified.
- Changes are approved.

## 8. Delivery Report

Report:
- Entities created or modified
- Schema changes
- Constraints
- Indexes
- Migration files
- Data migration risks
- Performance considerations
