# Git Workflow Rules

> Status: **Approved**
>
> Changing this file is in the 🔴 zone: requires a dedicated Task and a reviewer.
1. One Task maps to one branch or one independent change unit; work on a dedicated branch, never directly on long-lived branches (`master`, `develop`) or `release/*` branches.
2. Branching model follows Gitflow (nvie). Working branches are named `<type>/<TASK-ID>-<short-description>`, where type is `feature`, `fix`, `refactor`, `docs`, or `chore`, branched from `develop` and merged back into `develop`; except a `fix` for a bug in an open release is branched from `release/*` and merged back into it. Example: `fix/PRJ-12-login-timeout`. Two special branch types:
   - `release/<X.Y.0>`: branched from `develop` at sprint close, deployed to Staging, accepts only bug fixes (no new features), closed by merging into `master` (tagged `vX.Y.0`) and merging back into `develop`.
   - `hotfix/<X.Y.Z>`: branched from `master` to fix a critical Production bug, merged into `master` (tagged `vX.Y.Z`) and into `develop` (or the open `release/*`).
   Merge these branches with `--no-ff`. Tags have the form `vMAJOR.MINOR.PATCH`: release bumps MINOR, hotfix bumps PATCH, breaking changes bump MAJOR.
3. Commit messages **must** follow the Angular convention: first line `type(scope?): subject`, `type` is one of `build`, `ci`, `chore`, `docs`, `feat`, `fix`, `perf`, `refactor`, `revert`, `style`, `test`; body states `TASK-ID`. Every project has an automated mechanism blocking malformed commits. Each commit contains only files within the Task scope. Do not add a `Co-Authored-By` line or any AI attribution line to commit messages.
4. After committing, show the reviewer: branch, short hash, and the **full message** (first line + body) of each commit just created, plus each commit's file list (`git show --stat --format=full`). Do not just report "committed".
5. `master`, `develop`, and open `release/*` branches are protected: they accept changes only via PR with review and passing check gates. AI does not merge into these branches itself and does not create release tags itself; a human merges and tags after approval and passing checks (or a time-limited waiver).
6. No force-push, no rewriting shared branch history.
7. Do not use `--no-verify` or equivalents to bypass hooks or check gates.
8. Do not commit secrets, `.env*`, or production data.
9. Changes in the 🔴 zone (rules, skills, workflows, permission/CI config) go in a separate Task and PR, not bundled into a feature Task.
10. The PR states `TASK-ID` and includes the handoff report (link or paste, declared in PR-TEMPLATE §1); the PR does not copy sections already in the handoff report.
