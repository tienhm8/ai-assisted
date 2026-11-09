---
name: architecture-design
description: Design and evaluate software architecture, system boundaries, module structures, integrations and technical decisions based on approved requirements.
---

# Architecture Design Skill

## 1. Objective

Produce maintainable, secure, scalable and testable
software architecture aligned with approved requirements.

## 2. Required Inputs

- Project Vision
- Approved FR and BR
- NFR
- System Scope
- Existing Architecture
- Technology Stack
- Database Design
- API Specification
- Security Requirements

## 3. Design Workflow

### Step 1: Analyze Requirements

Identify:
- Business capabilities
- System actors
- Functional boundaries
- Quality attributes
- Integration requirements
- Technical constraints

### Step 2: Define System Boundaries

Identify:
- Applications
- Modules
- Services
- External systems
- Trust boundaries
- Data ownership

### Step 3: Define Architecture Style

Evaluate appropriate patterns:
- Modular Monolith
- Layered Architecture
- Clean Architecture
- Domain-driven Design
- Microservices

Choose the simplest architecture that satisfies requirements.

Do not introduce unnecessary complexity.

### Step 4: Design Components

For each module define:
- Responsibility
- Inputs
- Outputs
- Dependencies
- Data ownership
- Interfaces
- Error boundaries

### Step 5: Design Data Flow

Describe:
- Request flow
- Authentication flow
- Authorization flow
- Business processing
- Database interactions
- External integrations
- Error handling

### Step 6: Design Security Boundaries

Define:
- Authentication boundaries
- Authorization enforcement
- Service permissions
- Data access boundaries
- Sensitive information handling

### Step 7: Evaluate Architecture Quality

Evaluate:
- Maintainability
- Modularity
- Reliability
- Performance
- Scalability
- Security
- Observability
- Testability

### Step 8: Record Architecture Decisions

For significant decisions create an ADR.

Each ADR must contain:
- Context
- Problem
- Options considered
- Decision
- Consequences
- Status

### Step 9: Review Existing Architecture

Identify:
- Architecture violations
- Circular dependencies
- Duplicate responsibilities
- Unnecessary coupling
- Scalability risks
- Security risks

## 4. Output Format

Produce:

1. Architecture Overview
2. Architecture Principles
3. System Context Diagram
4. Container / Component Diagram
5. Module Responsibilities
6. Dependency Map
7. Data Flow
8. Security Boundaries
9. Technology Decisions
10. ADRs
11. Risks and Trade-offs
12. Implementation Recommendations

## 5. Quality Checklist

- [ ] Architecture satisfies approved requirements.
- [ ] System boundaries are explicit.
- [ ] Module responsibilities are clear.
- [ ] Dependencies are controlled.
- [ ] Data ownership is defined.
- [ ] Security boundaries are defined.
- [ ] Failure handling is considered.
- [ ] Testing strategy is feasible.
- [ ] Decisions have documented trade-offs.
- [ ] No unnecessary architectural complexity.

## 6. Restrictions

- Do not change approved technology choices without approval.
- Do not introduce microservices without justification.
- Do not bypass established module boundaries.
- Do not silently modify existing architecture.
- Do not make unresolved business decisions.

## 7. Definition of Done

Architecture must be:
- Documented
- Traceable to requirements
- Reviewed for security
- Reviewed for maintainability
- Supported by necessary ADRs
- Approved before implementation

## 8. Delivery Report

Report:
- Architecture designed
- Modules affected
- Decisions made
- ADRs created
- Trade-offs
- Risks
- Approval requirements
