---
name: deployment
description: Prepare, validate and execute software deployments across development, staging and production environments following approved release, security and rollback procedures.
---

# Deployment Skill

## 1. Objective

Deploy software reliably while minimizing downtime,
configuration errors, data loss and service disruption.

## 2. Required Inputs

- Approved Release Scope
- Release Notes
- Git Commit / Tag
- CI/CD Configuration
- Environment Configuration
- Deployment Documentation
- Database Migration Scripts
- Test Results
- Rollback Plan

## 3. Deployment Workflow

### Step 1: Identify Deployment Target

Identify:
- Development
- Testing
- Staging
- Production

Confirm the target environment before execution.

### Step 2: Verify Release Readiness

Check:
- Required features are complete.
- Code review is approved.
- CI checks pass.
- Required tests pass.
- Critical security findings are resolved.
- Configuration is prepared.
- Dependencies are available.
- Database migrations are reviewed.

### Step 3: Validate Environment

Check:
- Runtime version
- Environment variables
- Database connectivity
- Network configuration
- Secrets
- External service credentials
- Storage
- Domain and TLS configuration

Never expose secret values in logs or reports.

### Step 4: Validate Database Migrations

Evaluate:
- Migration order
- Data compatibility
- Execution duration
- Locking risks
- Backward compatibility
- Rollback feasibility

Use backward-compatible migration strategies
when application and database versions overlap.

### Step 5: Execute Deployment

Follow the approved deployment mechanism.

Examples:
- Build artifact
- Container image
- Application deployment
- Database migration
- Static asset deployment
- Service restart when necessary

Do not improvise production deployment commands.

### Step 6: Verify Deployment

Check:
- Application startup
- Health checks
- Database connectivity
- Critical APIs
- Authentication
- Core business workflows
- Error logs
- Monitoring alerts

### Step 7: Monitor Release

Monitor:
- Application errors
- Response times
- Failed requests
- Resource usage
- Database performance
- Background jobs
- External integrations

### Step 8: Rollback or Recovery

If serious problems occur:
- Stop further deployment.
- Assess impact.
- Follow approved rollback procedures.
- Protect data integrity.
- Verify service recovery.
- Report incident details.

Never assume rolling back application code
automatically reverses database changes.

### Step 9: Document Release

Create release records containing:
- Version
- Deployment time
- Environment
- Commit reference
- Changes
- Migration status
- Verification results
- Known issues

## 4. Output Format

Produce:

1. Deployment Target
2. Release Version
3. Pre-deployment Checklist
4. Configuration Validation
5. Migration Summary
6. Deployment Steps
7. Health Check Results
8. Monitoring Results
9. Rollback Plan
10. Release Report

## 5. Quality Checklist

- [ ] Correct environment selected.
- [ ] Release approval obtained.
- [ ] CI checks passed.
- [ ] Required tests passed.
- [ ] Secrets are protected.
- [ ] Configuration is validated.
- [ ] Database migration is reviewed.
- [ ] Backup/recovery requirements are satisfied.
- [ ] Rollback strategy is available.
- [ ] Health checks pass.
- [ ] Critical workflows are verified.
- [ ] Release documentation is updated.

## 6. Restrictions

- Never deploy to production without approval.
- Never expose secrets.
- Never run destructive migrations without approval.
- Never bypass failed release gates.
- Never modify production data directly.
- Never assume rollback is safe without evaluation.
- Never report deployment success without verification.

## 7. Definition of Done

- Deployment completed.
- Application health verified.
- Critical workflows verified.
- Monitoring checked.
- Migration status confirmed.
- Release report completed.
- Remaining issues documented.

## 8. Delivery Report

Report:
- Release version
- Environment
- Deployment status
- Commit reference
- Migration status
- Health checks
- Test results
- Monitoring results
- Known issues
- Rollback status
