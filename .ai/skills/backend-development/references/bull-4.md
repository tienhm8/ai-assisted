# Backend Development – Bull 4 queues (`@nestjs/bull`)

> Áp dụng cho: `bull` 4.16.x, `@nestjs/bull` 11.x. Trạng thái: Approved (2026-11-20), chưa chạy thử bằng Task thật.

This is Bull 4, not BullMQ: do not use `Worker`, `FlowProducer`, `QueueEvents` or BullMQ options; verify each option in the installed `bull` types. Queue names and Redis connection are project config.

## 1. Delivery guarantee (steps 3, 4)

- Delivery is **at least once**: a job can run more than once (retry after failure, or recovery when a worker stalls because the event loop was blocked longer than `lockDuration`, 30 s by default; a stalled job is recovered only `maxStalledCount` times, default 1, then fails). A processor must give the same final result when run twice: use a business unique key or check state before writing, not "it only runs once".
- Keep CPU-heavy or long synchronous work out of a processor; it blocks the event loop, lets the lock expire and the job run twice.

## 2. Adding jobs (step 4)

- Enqueue after the database transaction commits, not inside it (`nestjs-11.md` §6, error-handling §9). If the process dies between commit and `add`, the job is lost; the Task must state whether that is acceptable, otherwise stop and report (reliable publication needs an outbox, which is an architecture decision).
- Payload is small, serializable and holds identifiers rather than whole records; no `secret` data (tokens, personal data) because it is stored in Redis and visible in job failure output. Do not pass entities or class instances.
- A stable `jobId` (for example derived from the business key) deduplicates only while a job with that id still exists: with `removeOnComplete: true` the key is removed on completion, so the same id can be added again afterwards. Decide whether duplicates should be ignored or allowed, and set retention to match.
- Defaults are weak: `attempts` is 1 (no retry) and there is no `backoff`. When setting `attempts`, set `backoff` as well (`{ type: 'exponential', delay }`), otherwise retries run immediately and hit a failing dependency at full speed. Do not set retries on a non-idempotent job.
- `removeOnFail` is off by default: failed jobs stay in Redis forever. Set a retention (`removeOnFail: <count>` or `true`) per queue as the Task or error-handling says; failed jobs are the only record unless the failure is also logged.

## 3. Processors (steps 4, 5)

- `@Process('<name>')` handlers must `await` all async work and let the error propagate: a swallowed error marks the job completed. A thrown error triggers retry up to `attempts`.
- Separate failures that retry (timeouts, 5xx, deadlock) from failures that never succeed (invalid payload, missing record, business rule). For the second kind, do not rethrow into another retry: call `job.discard()` before throwing, or log and return per error-handling §8.
- `@OnQueueFailed` and `@OnQueueError` only log; they do not retry or compensate. Log with job id, name, `attemptsMade` and the correlation ID (do not log `job.data` when it can hold personal data, `security-standards` §9).
- A job that exhausted its attempts must not disappear silently: ensure the failure is visible (log at error level and, if the Task has an alert mechanism, that metric) and that it can be replayed by a person; do not build an automatic replay or dead-letter queue yourself (new mechanism, `project-rules` 5).
- Concurrency of a processor is set per `@Process` (`@Process({ name, concurrency })`); do not raise it without checking database pool size and external rate limits.

## 4. Shutdown (step 4)

- Closing the app with in-flight jobs requires `app.enableShutdownHooks()` (`nestjs-11.md` §3); `@nestjs/bull` then closes each queue in `onApplicationShutdown`. Check it exists before adding a long-running processor, otherwise the job is left locked until the lock expires and then runs again (see §1).

## 5. Tests (step 8)

- Unit test the processor method directly with a fake `Job` (`{ data, id, attemptsMade }`) and fake repositories; assert idempotency by calling it twice with the same data.
- Test the code that calls `queue.add` with a fake `Queue` and assert name, payload and options (`attempts`, `backoff`, `jobId`), not that Redis stores them. Integration tests that need real Redis follow Skill `integration-testing`.
