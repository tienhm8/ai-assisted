---
name: code-review
description: Review a code change (PR or local commit range), language-agnostic, in priority order correctness → tests → placement → concurrency → performance → security → operability → clean code; read the change description before the code; every finding has a location, failure scenario, and severity.
---

# Code Review Skill

Confirm before merge that the change does the right thing, stays within Task scope, sits in the right place in the architecture, withstands load and concurrency, is safe, is operable, and has real test evidence.

**Wrong logic: do not approve; ugly code: comment, do not block the change.**

## Input

The change description is ONE of: (a) the description of the PR, when reviewing a PR; (b) the handoff report (DELIVERY-REPORT) of the Plan or Task plus the commit range `git diff <base>..<head>`, when reviewing on the machine before a PR (Plan step 8, fast lane). Both must cover the items of Step 1.

## Entry gate

If any item is missing, stop, state the missing item, and return it to the author (or the Orchestrator); do not review the code:

- Change description has all items in Step 1.
- Task has scope, AC, risk level.
- Automated gates (build, lint, type check, test, secret scan) are green: taken from CI; no CI yet, then from a local run recorded in the change description, with command and output.
- Change size is within the project threshold; over threshold, suggest splitting, unless the change description states a reason (generated code, mass rename…).

Read: change description, Task, AC, related FR/BR; architecture docs (layers, module boundaries, dependency direction), coding-standards, error-handling, testing-strategy, NFR; git diff **and context outside the diff** (callers of the changed code, schema, migrations, config, existing tests); test report and handoff report.

## Procedure

### Step 1: Read the change description first, not the code yet

From the change description, answer the following; any you cannot answer becomes a finding or question; do not infer it from the code:

1. What problem is being solved, linked to which Task and AC?
2. Behavior change or refactor only? If refactor, external behavior must stay the same.
3. What is affected: data/schema, API/contract with callers, jobs/background tasks/messages, cache, config/environment variables, access permissions?
4. Out of scope: what is intentionally not done?
5. How was it tested, where is the evidence?
6. Data changes: affected volume, table locks, backward compatible with running code?
7. Breaking change, feature flag needed, deploy order (code first or migration first), how to roll back?

From that, form a **hypothesis of what the code must do**, then read the diff to test the hypothesis.

### Step 2: Compare Task with diff

- List changed files and affected modules; compare with the scope in the Task ticket and the change description's "out of scope" item.
- Report files in the 🟡/🔴 zone and files out of scope.
- Report tests deleted, disabled, or weakened; columns/tables deleted out of scope; new dependencies without a stated reason.
- Change description says "refactor only" but the diff changes behavior (changed conditions, return values, side-effect order): finding.

### Step 3: Review in priority order

Go through priorities 1 to 8 in order. Load the checklist of the group in progress; do not load ones not yet reached:

| Priority | Main question | Checklist |
| --- | --- | --- |
| 1 | Does the code do the right thing? (AC, edge cases, states, errors, data types, transactions, BR from FR/BR) | `references/correctness.md` |
| 2 | Are there tests proving it? (each AC has a test and real output) | `references/correctness.md` |
| 3 | Is the code in the right place? (layer and responsibility per the project's architecture docs) | `references/correctness.md` |
| 4 | What about load and concurrency? (race, idempotency, retry, event after commit) | `references/runtime.md` |
| 5 | Performance, data, cache (N+1, volume, missing/redundant/duplicate indexes after the change, large-table migrations) | `references/runtime.md` |
| 6 | Security per OWASP Top 10 (per-record authorization, injection, XSS, `secret` data exposure, upload, SSRF) | `references/security.md` |
| 7 | Is it operable? (logs, alerts, config, rollback) | `references/runtime.md` |
| 8 | Clean code and style; do not comment on what formatter/linter already catches | — |

If the diff touches authentication, authorization, sensitive data, or external input, trigger `security-review`; do not do it yourself in this skill.

### Step 4: Write findings

Each finding must have:

- Location `file:line`.
- **Concrete failure scenario**: which input or state → what wrong result. If you cannot build a scenario, record it as a **question**, not a bug.
- Severity on the shared scale; common cases:

| Severity | Common cases |
| --- | --- |
| Critical | Data loss/corruption, exploitable security vulnerability |
| High | Logic wrong vs AC/BR, race condition corrupting data, AC without test, migration not rollbackable |
| Medium | Wrong layer, N+1 or missing index on still-small data, missing error handling in a secondary branch, missing log/alert |
| Low | Clean code, naming, minor structure |

- Fix request or fix direction.

Suggestions and points to watch are not bugs: put them in the questions and suggestions section, without severity.

Presentation rules:

- Merge findings with the same cause into one; cap the number of Low findings and suggestions, keeping only the most valuable, so important findings are not buried.
- Acknowledge specific good points of the change.
- Feedback tone targets the code, not the author.

### Step 5: Recommendation

- **Do not approve**: Critical/High remain, or the entry gate failed.
- **Approve with conditions**: Medium remain; state the conditions clearly (fix in this change or create a Task with a deadline).
- **Approve**: only Low, suggestions, or no findings.

## Limits

- Do not assume code is correct just because tests pass.
- Do not conclude on concurrency, performance, or architecture from the diff alone; read context outside the diff.
- Do not rewrite code during review.

## Done when

- All 8 priorities covered in order; non-applicable priorities have a stated reason.
- Every finding has all parts in Step 4.
- There is a recommendation with reasons.

## Report

- Change summary as the reviewer understands it: problem, behavior change or refactor, impact scope; risk level; files reviewed, including 🟡/🔴 zone files and out-of-scope files.
- Missing items in the change description.
- Findings by severity; questions and suggestions for the author.
- Test assessment: AC with or without evidence, source of gate results (CI or local).
- Non-applicable priorities and reasons; whether `security-review` was used.
- Notable good points.
- Recommendation and conditions.
