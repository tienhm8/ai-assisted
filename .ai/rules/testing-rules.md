# Testing Rules

> Status: **Approved**. Mandatory Rule.

1. Each AC of the Task has at least one test; the test name or comment includes the AC ID for traceability.
2. A bug fix must include a regression test: run it red before the fix, green after.
3. Test both success and error paths, including boundary values and permission-denied cases.
4. Do not mock the very behavior under test.
5. Do not delete, disable, or weaken tests; do not lower coverage thresholds.
6. Before reporting completion, run all the project's check gates (build, lint, type check, test, secret scan) with the commands in ai-config.yaml `commands`; if a gate has no command there, ask, do not guess it. If there is no CI, run locally and record a time-limited waiver; do not skip silently.
7. Do not claim tests pass without running them. Report includes the commands run and actual results; clearly distinguish pass, fail, skipped, not-run.
8. Test data is fake or anonymized; do not touch production.
9. E2E tests are written with Playwright.
