---
name: authentication-rbac
description: Implement and review authentication, authorization, role-based access control, session management and resource-level permissions according to approved security policies.
---

# Authentication & RBAC Skill

## 1. Objective

Implement secure authentication and authorization
while preserving approved role and permission boundaries.

## 2. Required Inputs

- Authentication Requirements
- RBAC Specification
- User Roles
- Permission Matrix
- Session Policy
- API Specification
- Security Rules
- Existing Authentication Implementation

## 3. Development Workflow

### Step 1: Read Approved Access Policies

Identify:
- Authentication methods
- User roles
- Permissions
- Resource ownership
- Access scope
- Session boundaries
- Account lifecycle
- Approval workflows

Treat unresolved policies as open questions.

### Step 2: Design Authentication

Consider:
- Registration
- Email verification
- Login
- Logout
- Password handling
- Session creation
- Session expiration
- Session revocation
- Account status

Follow the approved authentication architecture.

### Step 3: Implement Authorization

Implement:
- Role checks
- Permission checks
- Resource ownership checks
- Scope checks
- Backend authorization
- Default-deny behavior

Do not rely on frontend role visibility.

### Step 4: Enforce Application Boundaries

For systems with more than one application
(for example a public web app and an internal management app):
- Preserve application access boundaries.
- Enforce independent session policies where specified.
- Prevent unauthorized cross-application access.
- Validate all internal-application APIs on the backend.

See [examples.md](examples.md) for a project-specific example.

### Step 5: Implement Resource-Level Access

Examples:
- A user can access only permitted resources.
- A role with limited scope can access only resources within approved scope.
- A role tied to assignment can access only assigned data where required.
- Administrative access follows explicit permissions.

See [examples.md](examples.md) for concrete roles. Examples are not
the official permission matrix.

Do not assume a role has unrestricted access.

### Step 6: Handle Session Security

Consider:
- Secure cookies
- HttpOnly
- SameSite
- Secure flag
- CSRF protection where applicable
- Session revocation
- Concurrent sessions
- Session invalidation after security events

### Step 7: Test Authorization Boundaries

Test:
- Unauthenticated access
- Authenticated but unauthorized access
- Wrong role
- Wrong resource owner
- Out-of-scope resource
- Revoked session
- Expired session
- Forged client-side role
- Cross-application access

### Step 8: Audit

Review:
- Privilege escalation
- Insecure direct object references
- Missing permission checks
- Inconsistent access policies
- Session management weaknesses

## 4. Output Format

Produce:
1. Authentication Flow
2. Role and Permission Matrix
3. Authorization Rules
4. Session Management
5. API Protection
6. Resource Access Rules
7. Test Cases
8. Security Findings
9. Documentation Updates

## 5. Quality Checklist

- [ ] Authentication is correctly enforced.
- [ ] Passwords are securely handled.
- [ ] Backend authorization is enforced.
- [ ] Default-deny behavior is applied.
- [ ] Resource ownership is verified.
- [ ] Scope restrictions are enforced.
- [ ] Session revocation is considered.
- [ ] Cross-application boundaries are preserved.
- [ ] Privilege escalation is tested.
- [ ] No unresolved policy is silently assumed.

## 6. Restrictions

- Never bypass backend authorization.
- Never trust client-provided role information.
- Never grant permissions implicitly.
- Never assume Admin has unrestricted access.
- Never change approved role definitions without approval.
- Never weaken authentication to make tests pass.
- Never invent unresolved session policies.

## 7. Definition of Done

- Authentication behavior verified.
- Authorization enforced at backend.
- Resource boundaries tested.
- Session behavior tested.
- Security tests passed.
- Documentation updated.
- Sensitive changes approved.

## 8. Delivery Report

Report:
- Authentication changes
- Role/permission changes
- APIs protected
- Resource scope enforcement
- Session changes
- Authorization tests
- Security risks
- Decisions requiring approval
