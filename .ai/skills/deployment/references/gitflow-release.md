# Gitflow: cut release, release, hotfix

Load when a release Task needs to cut a release, close a release or do a hotfix. Merge, tag and push commands to `master`, `develop`, `release/*` are run by a **human**; AI drafts these commands into the runbook.

The examples below assume the current Production version is `v1.3.0` and this sprint releases `v1.4.0`.

## Branches and environments

| Branch | Branched from | Merges into | Deploys to |
| --- | --- | --- | --- |
| `master` | — | — | Production, each commit is a tag |
| `develop` | — | — | Dev |
| `release/X.Y.0` | `develop` | `master` and `develop` | Staging |
| `hotfix/X.Y.Z` | `master` | `master` and `develop` (or open `release/*`) | Staging quick check, then Production |

## Cut release

```bash
git checkout develop && git pull
git checkout -b release/1.4.0
git push -u origin release/1.4.0
```

- Deploy `release/1.4.0` to Staging for QA and UAT.
- Bugs found: `fix/...` branch from `release/1.4.0`, PR into `release/1.4.0`, redeploy Staging.
- Next sprint's features still merge into `develop`, without affecting the release.

## Production release

Conditions: QA, UAT, regression pass on Staging; rollback verified; Owner approved.

```bash
git checkout master && git pull
git merge --no-ff release/1.4.0
git tag -a v1.4.0 -m "Release 1.4.0"
git push origin master --tags      # deploy Production from tag v1.4.0

git checkout develop && git pull
git merge --no-ff release/1.4.0    # bring release fixes back to develop
git push origin develop

git branch -d release/1.4.0
git push origin --delete release/1.4.0
```

## Hotfix

Conditions: critical bug on Production, Owner agrees.

```bash
git checkout master && git pull
git checkout -b hotfix/1.4.1
# ... fix bug, commit

git checkout master
git merge --no-ff hotfix/1.4.1
git tag -a v1.4.1 -m "Hotfix 1.4.1"
git push origin master --tags      # deploy Production

git checkout develop
git merge --no-ff hotfix/1.4.1
git push origin develop
```

If a `release/*` is open, merge the hotfix into `release/*` instead of `develop`; the release reaches `develop` when closed.

## Common pitfalls

- Forgetting to back-merge release or hotfix into `develop`: fixed bugs reappear in the next version.
- Deleting the release branch before back-merging.
- Deploying Production from a branch instead of a tag.
