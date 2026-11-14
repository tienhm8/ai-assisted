---
name: incident-analysis
description: Analyze incidents from logs, metrics, traces exported by a human with D3 data masked; build a timeline, separate confirmed causes from hypotheses, draft a Draft incident report and bugs; AI only reads and reports.
---

# Incident Analysis Skill

Understand what happened, why, and the impact, from human-provided data. Only read and report (A1); a human decides how to handle it.

## Entry gate

- Logs, metrics, traces exported by an authorized person with D3 masked. If unmasked D3 is seen, stop, report, and do not use it.
- Incident description: time, symptoms, environment.
- If missing, stop and state what data is needed.

Read: masked data, user reports; release report, handoff reports, PRs near the incident time; monitoring, deployment, backup-recovery; relevant FR/AC.

## Procedure

1. **Build a timeline**, citing the source of each milestone: detection, error spike, changes, handling.
2. **Correlate with recent changes:** release, migration, configuration, infrastructure.
3. **Separate** confirmed causes (with evidence) from hypotheses (with how to verify).
4. **Assess impact:** users, modules, data, security, duration.
5. **Propose immediate action** (rollback or hotfix) per deployment and backup-recovery; a human decides.
6. **Propose prevention:** missing tests, monitoring, alerts, runbooks.
7. **Create a bug** per BUG-TEMPLATE for each defect.
8. **Propose next Tasks** for a human to decide: bug fix (T3) per bug; security review (T10) if security-related; runbook update (T12).

## Limits

- Do not run commands on production; do not rollback or hotfix on your own.
- Do not blame individuals.

## Done when

- Every conclusion has evidence or is marked as a hypothesis.
- Bugs created; missing data stated.

## Report

Incident report (Draft): summary, timeline, root cause (confirmed and hypotheses), impact, proposed immediate action and prevention, missing data, bugs and open questions created.
