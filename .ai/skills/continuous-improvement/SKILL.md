---
name: continuous-improvement
description: Compile periodic KPIs from real sources, compare with baseline, find root causes and propose improvements to rules, skills, workflows, agents in ai-kpi.md; changes to the AI configuration zone are only proposed and done by the reviewer.
---

# Continuous Improvement Skill

Use real data to learn whether AI improves development, and propose improvements to Rules, Skills, workflows, agents. Metrics are for improving the system, not for ranking individuals.

## Entry gate

- Data for the measurement period and a baseline exist in ai-kpi.
- Missing baseline: state that it is missing and propose how to measure. Missing period data: stop and record an open question.

Read: [framework-evolution](../../guide/framework-evolution.md) when the period ends a Plan or a major change happened (a new AI model, a major version of a stack technology); ai-kpi; the period's handoff reports, test reports, bugs, release reports, review results, security findings; roadmap; related Rules, Skills, workflows.

## Procedure

1. **Define the period** and measurement scope; use only KPIs already defined in ai-kpi.
2. **Collect data** from real sources, recording the source. If unavailable, write "not measured".
3. **Record results** in the per-period results table, split by module and complexity level, compared with baseline.
4. **Analyze trends:** productivity counts as improved only when quality and security did not worsen.
5. **Root cause** for each worsened KPI: trace from handoff reports, bugs, reviews to the related Rules, Skills, workflows. If evidence is insufficient, record it as a hypothesis.
6. **Propose improvements** in the action table: problem, target, action, owner, how to measure effectiveness next period, and level (`Framework` or `Project`). Level `Framework` only for a lesson that is technology-neutral and has evidence; a lesson tied to one technology or version stays `Project` (a `references/` file, `docs/`, `ai-config.yaml`). Write each proposal in neutral wording; do not name the project's technology in a `Framework` row.
7. **External review** at the end of a Plan or on a major change: list new technologies, AI models, skills, tools, libraries or patterns relevant to the project's `stack` and `ai-config.yaml`, record them in the external-review table of ai-kpi §6 with source and date, and mark each as "try in this project" or "not now". Do not adopt anything from outside directly; external skills follow `.ai/guide/external-skills.md`.
8. **Split a separate Task** for each Rule, Skill, workflow change. A `Framework` proposal waits for the approver of the `.ai/` zone before its Task is created.

## Limits

- Do not round or guess data.
- Do not edit `.ai/` yourself and do not move a `Project` lesson into the Framework; propose only.
- Do not treat an external source as evidence: evidence comes from a Run or a result in this project.

## Done when

- Period results and improvement actions are recorded in ai-kpi (Draft); all data has a source.
- Each worsened KPI has a root cause or a hypothesis with a way to verify it.

## Report

Measurement period, updated KPIs and sources, worsened KPIs with causes, proposed actions with their level, the external review result, split Tasks, missing data.
