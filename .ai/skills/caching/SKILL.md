---
name: caching
description: Design, implement, or review L1/L2 data caches: check cache eligibility, choose key, TTL, read path with single-flight, delete keys after commit plus L1 sync across instances, fail-open, warm-up, and metrics; record in the database-design cache table. Use when adding, changing, or reading a cache, or changing cached data.
---

# Caching Skill

> Status: **Approved** (Tech Lead approved 2026-11-13). Waiver of trial run before approval: trial run in the first Task that adds or changes a cache; errors found then are fixed via a dedicated Task.

Put a cache into a read path so it is faster without being wrong: clearing the whole cache at any time leaves business results unchanged.

## Entry gate

- Access pattern `AP-<NN>` has gone through root optimization (index, query, table structure) in `database-design` step 7. If the source is a DB query, there is an execution plan after optimization; if still designing with no DB yet, record an assumption and verify it in `database-design` step 10 before implementing the cache. If the source is an external service or computation, record measured latency and cost instead of an execution plan.
- The AP has frequency, target latency, and the business-acceptable staleness window. Missing staleness window: record an open question for PO/BA; do not set it yourself.
- The module owning the data and every write path touching that data are known.
- Implementation: the cache row in database-design §3.7 is Approved. If not, do steps 1–4 then stop and wait for approval.
- Value contains D3: Security must approve the design before implementation.

Main sources: Task Manifest (and the Plan points it cites); existing cache code (shared read function, client, config).
If the manifest is missing something, look up the exact section: database-design §3.4 Mẫu truy cập và khối lượng, §3.7 Cache; module-design §5 Ranh giới và quyền sở hữu; system-architecture §7 Cross-cutting Concerns; error-handling §8 Retry, timeout, fallback, §9 Transaction và nhất quán dữ liệu; security-standards §1 Xử lý dữ liệu theo mức (D0–D3), §6 Bảo vệ dữ liệu; monitoring §4 Metrics; deployment §9 Database Deployment and Migration.

## References

Load the file matching ai-config.yaml `stack`; if `stack` lacks the entry, ask. Read only the listed sections.

| File in `references/` | Load at step |
| --- | --- |
| `patterns.md` | Step 1: §1, §2 · Step 2: §5, §8 · Step 3: §3, §4, §6, §7 · Step 4: §11 · Step 5: §9 · Step 6: §10 |
| `warmup.md` | Step 4, only when production has a cache |
| `redis.md` (L2 is Redis only) | Step 2: §1, §5 · Step 3: §2–§5 · Step 4: §6 · Step 5: §2–§4 |

## Procedure

1. **Decide whether to cache.** Use query cost **after** optimization, not pre-optimization numbers. Check each condition of Rule `cache` against the access pattern; record whether each condition is met by data or by assumption. "Changes constantly" and "rarely read" are checked against thresholds in database-design §3.7; no threshold yet: record an assumption with data from the AP table. On the do-not-cache list, or missing one condition: stop and report; do not cache.
2. **Key and TTL.** Key format, distinguishing factors (tenant, viewer, permission, language), version, TTL per tier based on the acceptable staleness window, jitter. Assign a data level to the value; D3: record all protection measures.
3. **Read and write paths.**
   - Read through the shared read function with single-flight; if none exists, implement it first and use it for every path.
   - List **every** write path touching the data (repository, bulk update, raw SQL, import, job, other services) and where each path deletes keys after commit.
   - If L1 lives longer than one request: choose the L1 invalidation event channel and how to recover when an event fails.
   - Record how fail-open works and how DB load is limited when the cache goes down.
4. **Record the design.** Add a row to the database-design cache table; if production has a cache, declare the warm-up group. Changing cache technology or HA is an architectural decision: draft an ADR.
5. **Implement** per the approved design: key, TTL, loader, delete after commit, L1 event, warm-up group, metrics.
6. **Verify** with real running tests:
   - Clear the whole cache then rerun business cases: results unchanged.
   - Read after write: no stale value returned, including from another instance's L1.
   - A read missing the key runs concurrently with a write: the cache does not end up holding the old value (unless the cache row records "accept TTL").
   - Cache down or timeout: request still succeeds from DB.
   - Many concurrent requests missing the same key: DB queries do not grow with request count, at most one per instance; one for hot keys.
   - Keys of different users/tenants cannot be cross-read.
   - Data types survive serialize and deserialize unchanged.

## Limits

- Do not cache free-form filtered or paginated lists until you show how to delete every related key correctly.
- Do not add a new write path to cached data without a key-deletion step.
- Do not create a second cache read function when the project already has one.

## Done when

- Each cache has a row in database-design, traceable to an AP, recording all cache-eligibility conditions and every key-deletion event.
- The verification cases in step 6 have real test output.
- Cache metrics are in monitoring, or the missing parts are stated.

## Report

Write in the handoff report: each sample key with its cache-eligibility conditions, TTL, data level; the list of write paths and where keys are deleted; how L1 is synced; stampede-prevention measures; warm-up group; metrics added.
