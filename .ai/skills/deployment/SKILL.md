---
name: deployment
description: Prepare and check releases (confirm readiness, draft commands, runbook, rollback plan, release notes, release report); AI does not execute on production, execution is done by an authorized person after Owner approval.
---

# Deployment Skill

AI prepares and checks the release; an authorized person executes. Outside production, AI runs only when the Task explicitly grants permission.

## Entry gate

- The release Task states version, target environment, risk level. If missing, stop and ask.
- Every PR in the release has been merged by a human into `develop` or `release/*` and passed check gates; exclude PRs that have not passed from the list and report them.
- Operations docs (deployment, monitoring, backup and restore) exist in the needed sections; if still empty, stop and ask.

Read: release Task, list of merged Tasks/PRs, commits or tags; operations docs; migrations; test reports; RELEASE-REPORT-TEMPLATE.

## Procedure

1. **Identify** the target environment and the authorized person who executes.
2. **Check readiness:** in-scope Tasks are done, PRs reviewed and passed gates, no open Critical/High findings, tests actually run. If any gate fails, stop.
3. **Configuration:** list the **names** of environment variables and configuration required in the target environment. Do not read, create, rotate or write secret values.
4. **Merge and migration order:** merge order when there are migrations or backward-incompatible API contracts; migration order, compatibility while app and DB versions overlap, run time, table-lock risk, whether destructive, backup before running, rollback path. Code rollback does not revert DB changes; state clearly how to restore data.
5. **Prepare execution:** draft commands, a step-by-step runbook and migration scripts per the approved deployment mechanism; do not invent deploy commands. Commands to cut a release, close a release, hotfix come from `references/gitflow-release.md`. Load the reference file matching ai-config.yaml `stack`; if `stack` lacks the entry, ask.
6. **Release notes** from merged Tasks, written for end users, with Task/FR and PR.
7. **Rollback plan:** trigger conditions, steps, decision maker, whether tested outside production.
8. **Verify:** run regression and smoke tests on staging or local. After a human deploys, compare health checks and monitoring against the project's thresholds; if thresholds are exceeded, recommend rollback.
9. **Fill in the release report** and record lessons; Owner approves or postpones.

Special cases (Trường hợp đặc biệt):
- **Urgent hotfix:** separate Task, minimal analysis, still goes through `code-review`; supplementary records within the project's declared deadline, with a hotfix approver.
- **No staging, server or CI/CD yet:** work in the declared substitute environment and request a time-limited waiver, with an approver.

## Done when

- Commands, runbook, release notes, rollback plan are drafted; migrations are assessed.
- Smoke tests and regression have run, with real output.
- The authorized person has confirmed the deploy or the Owner has postponed; post-deploy results are recorded in the report.

## Report

Fill in RELEASE-REPORT-TEMPLATE. Record actions needing a human in the Task's handoff report with the release report ID.
