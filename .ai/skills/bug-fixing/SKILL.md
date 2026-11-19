---
name: bug-fixing
description: Fix bugs from a Bug Report (BUG-TEMPLATE) against approved requirements and AC - reproduce, find root cause, minimal fix, add regression test; stop when the bug stems from wrong/missing requirements.
---

# Bug Fixing Skill

Fix the root cause of a bug (deviation from approved requirements and AC) with a minimal change, without causing regressions.

## Entry gate

Input is a Bug Report per BUG-TEMPLATE. If any of the following is missing, stop and request it: bug ID, violated FR/BR/AC, bug-fix Task, severity, risk level.

Read: Bug Report, Task, related FR/BR/AC, related source code and tests.

## Procedure

1. **Identify the violated requirement.** If the AC is missing or ambiguous, or docs conflict: stop, record an open question and report. If the bug stems from a wrong requirement, do not fix it here.
2. **Reproduce** locally or on staging; mask sensitive data. If it cannot be reproduced, say so clearly; do not claim it was reproduced.
3. **Find the root cause**, distinguished from symptoms. If it cannot be established, stop and report.
4. **Assess impact:** modules, roles, data, security, regressions. If production data must be fixed, split into a separate Task, with approval.
5. **Propose the fix:** cause, fix approach, files, risks, tests. Wait for approval before fixing if the Task is `high`-risk, autonomy is `step-by-step`, or touches authorization, architecture, schema, contract.
6. **Write a regression test** at the lowest layer that reproduces the bug; run it and see it red before fixing.
7. **Fix minimally** at the root cause; no accompanying refactoring.
8. **Run** the regression test (must be green), the project's check gates and related regressions.

## Limits

- Do not mask bugs by swallowing errors or using workarounds.
- Do not modify business rules.

## Done when

- Root cause is recorded.
- Regression test red before, green after, with output of both runs.
- Check gates and related regressions pass.

## Report

Fill in the "Kết quả sửa" section of BUG-TEMPLATE (root cause, regression test). Write the rest in the handoff report per DELIVERY-REPORT-TEMPLATE.
