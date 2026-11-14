---
name: continuous-improvement
description: Compile periodic KPIs from real sources, compare with baseline, find root causes and propose improvements to rules, skills, workflows, agents in ai-kpi.md; changes to the AI configuration zone are only proposed and done by the reviewer.
---

# Continuous Improvement Skill

Use real data to learn whether AI improves development, and propose improvements to Rules, Skills, workflows, agents. Metrics are for improving the system, not for ranking individuals.

## Entry gate

- Data for the measurement period and a baseline exist in ai-kpi.
- Missing baseline: state that it is missing and propose how to measure. Missing period data: stop and record an open question.

Read: ai-kpi; the period's handoff reports, test reports, bugs, release reports, review results, security findings; roadmap; related Rules, Skills, workflows.

## Procedure

1. **Define the period** and measurement scope; use only KPIs already defined in ai-kpi.
2. **Collect data** from real sources, recording the source. If unavailable, write "not measured".
3. **Record results** in the per-period results table, split by module and complexity level, compared with baseline.
4. **Analyze trends:** productivity counts as improved only when quality and security did not worsen.
5. **Root cause** for each worsened KPI: trace from handoff reports, bugs, reviews to the related Rules, Skills, workflows. If evidence is insufficient, record it as a hypothesis.
6. **Propose improvements** in the action table: problem, target, action, owner, how to measure effectiveness next period.
7. **Split a separate Task** for each Rule, Skill, workflow change.

## Limits

- Do not round or guess data.

## Done when

- Period results and improvement actions are recorded in ai-kpi (Draft); all data has a source.
- Each worsened KPI has a root cause or a hypothesis with a way to verify it.

## Report

Measurement period, updated KPIs and sources, worsened KPIs with causes, proposed actions and split Tasks, missing data.
