---
name: security-review
description: Assess application security risks, identify vulnerabilities and recommend mitigations across code, APIs, authentication, authorization, data handling and infrastructure configuration.
---

# Security Review Skill

## 1. Objective

Identify security vulnerabilities and evaluate
the effectiveness of security controls.

## 2. Required Inputs

- System Architecture
- Security Requirements
- Authentication and RBAC Specification
- API Specifications
- Source Code
- Database Design
- Deployment Configuration
- Dependency Information

## 3. Security Review Workflow

### Step 1: Identify Attack Surface

Identify:
- Public endpoints
- Authenticated endpoints
- Administrative endpoints
- File upload functionality
- External integrations
- User input boundaries
- Sensitive data stores

### Step 2: Review Authentication

Check:
- Password storage
- Login security
- Session handling
- Token validation
- Session expiration
- Session revocation
- Account lifecycle

### Step 3: Review Authorization

Check:
- Missing permission checks
- Privilege escalation
- IDOR / BOLA
- Resource ownership
- Role boundaries
- Administrative permissions
- Cross-application access

### Step 4: Review Input and Output Security

Check:
- SQL injection
- XSS
- CSRF
- SSRF
- Command injection
- Path traversal
- Unsafe deserialization
- Output encoding

Apply mitigations relevant to the actual application.

### Step 5: Review Data Protection

Check:
- Sensitive data exposure
- Password handling
- Secret management
- Encryption in transit
- Encryption at rest where required
- Logging of personal data
- Backup protection

### Step 6: Review File Uploads

Check:
- File type validation
- File size limits
- Content validation
- Storage isolation
- Executable file handling
- Access permissions
- Malware scanning where appropriate

### Step 7: Review Dependencies

Check:
- Known vulnerabilities
- Unsupported packages
- Outdated dependencies
- Unnecessary permissions
- Supply-chain risks

### Step 8: Review Infrastructure

Check:
- Environment variables
- Database exposure
- CORS configuration
- HTTPS
- Security headers
- Network access
- Backup and recovery
- Deployment secrets

### Step 9: Assess Findings

Classify:
- Critical
- High
- Medium
- Low
- Informational

Assess impact, likelihood and exploitability.

Use established security frameworks such as OWASP
when relevant.

## 4. Output Format

Produce:

1. Scope
2. Attack Surface
3. Security Controls Reviewed
4. Vulnerability Findings
5. Severity
6. Evidence
7. Impact
8. Recommended Mitigation
9. Residual Risks
10. Retest Requirements

## 5. Quality Checklist

- [ ] Authentication reviewed.
- [ ] Authorization reviewed.
- [ ] Resource ownership reviewed.
- [ ] Input validation reviewed.
- [ ] Data protection reviewed.
- [ ] Dependencies reviewed.
- [ ] File uploads reviewed.
- [ ] Infrastructure reviewed.
- [ ] Findings include evidence.
- [ ] Mitigations are actionable.

## 6. Restrictions

- Only perform authorized security testing.
- Do not exploit production systems without approval.
- Do not access unrelated customer data.
- Do not expose secrets in reports.
- Do not perform destructive testing without approval.
- Do not claim a system is secure based only on code inspection.
- Do not make unapproved security policy changes.

## 7. Definition of Done

- Review scope completed.
- Findings documented.
- Severity assigned.
- Mitigations recommended.
- Critical findings escalated.
- Retest requirements defined.

## 8. Delivery Report

Report:
- Review scope
- Security controls evaluated
- Findings by severity
- Evidence
- Recommended fixes
- Remaining risks
