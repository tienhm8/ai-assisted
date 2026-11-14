# Code Review – Checklist for concurrency, performance, operability (priorities 4, 5, 7)

## Priority 4: What happens under load and concurrency?

- Two simultaneous requests on the same data: is there a "read then write" pattern (read value, decide, write back) without a lock, optimistic locking, or conditional update?
- Is the unique constraint guaranteed at the storage layer, or only checked "already exists?" in code (prone to duplicates under concurrency)?
- Reruns (retry, message delivered twice, user double-clicks): idempotent? Is there an idempotency key for create/payment operations?
- Background tasks: timeout, retry limit, backoff, handling of final failure; prevent overlapping runs when needed?
- Events/background tasks are emitted **after** the transaction commits, not before (avoid processing data that does not exist yet or was rolled back).
- Shared in-process memory state (global variables, stateful singletons): safe with many requests or many instances?
- External calls have timeouts; external system failures do not bring down the main flow.

## Priority 5: Performance, data, cache

- Queries or network calls inside loops (N+1), including indirect calls via lazy-load properties.
- How many records the query runs over, today and as data grows; is there a limit, pagination, batching, or streaming, or is everything loaded into memory?
- Fetch only needed columns and data.
- Indexes for new or changed queries: do filter, join, and sort conditions have suitable indexes (including column order in composite indexes); do conditions make an index unusable (`database-rules`)?
- Are indexes still sound after the change: does an old index still serve any access pattern; is a new index a duplicate or covered by an existing index (same column prefix); which indexes do changed or dropped columns affect? Adding or dropping an index requires evidence per `database-rules` and the index ↔ access pattern table in the DB design doc updated in the same PR; if missing, ask the author to fix it; the reviewer does not fix it.
- Migrations on large tables: long table locks, need for batching or splitting into steps?
- Should it be cached (conditions in `cache-rules`); if cached: placed only in repository or adapter, write paths do not read through cache, keys deleted after commit on every write path, is L1 of other instances deleted, time to live, are cache keys separated by user/tenant/permission (missing means cross-data leaks), do keys contain sensitive data, what happens when many requests miss the cache together.
- Check against performance NFR when the change is on a hot path.

## Priority 7: Is it operable?

- Important errors are logged with context and correlation ID, without sensitive data.
- When background tasks fail, someone knows (log, alert, dead-letter queue).
- New metrics or alerts needed? Does new config have values for every environment?
- Can it be rolled back; does the feature flag have a removal plan?
