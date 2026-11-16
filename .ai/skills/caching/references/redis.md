# Caching – Redis

> Nguồn: github.com/redis/agent-skills @ 74708da, skill `redis-core`, `redis-connections` (đối chiếu thêm `redis-security`, `redis-clustering`) v0.1.0, MIT · Ngày lấy: 2026-11-15 · Áp dụng cho: Redis server 7.x/8.x; client Node `redis` (node-redis) 6.3.1 (`@redis/client` 6.3.1) và `ioredis` 6.0.0, chọn client là quyết định dự án (dự án chưa chốt phiên bản ở system-architecture §4, rà lại khi chốt)
> Đã điều chỉnh: viết lại cho client Node (bản gốc Python/Java), chỉ giữ lỗi AI hay mắc khi làm L2 bằng Redis: timeout và hàng đợi offline của client, kết nối dùng chung, `SCAN`, `SET … NX PX` và nhả khoá có kiểm tra chủ, `UNLINK`, pub/sub cho L1, hash tag, `maxmemory-policy`, ACL/TLS theo service. Bổ sung từ tài liệu redis.io và file `.d.ts` của hai client (không có trong bản gốc): `SET` mất TTL, `DELEX`/`SET IFEQ` (8.4), pub/sub at-most-once, ACL kênh, `keyPrefix`. Bỏ: chọn kiểu dữ liệu (Hash để sửa từng field trái Rule `cache` 5: xoá, không cập nhật), kiến thức chung (đặt tên key có dấu `:`, `SSCAN`/`HSCAN`, hàng đợi `BLPOP`), cấu hình máy chủ thuộc hạ tầng (`bind`, `protected-mode`, firewall, `rename-command`); sửa: đọc từ replica không còn là "phù hợp cho cache" (§5). Không lấy code minh hoạ.

Reference for Skill `caching`. Load only when L2 is Redis, and only the section for the current step. Rule `cache` and `patterns.md` win over anything here; this file only adds the Redis/Node-client HOW.

## 1. Keys and TTL (step 2)

- Write value and TTL in one command: `SET key value EX <s>` (or `PX <ms>`). Never `SET` then `EXPIRE`: a crash between them leaves a key with no TTL. A plain `SET` on an existing key also **drops** its TTL; overwriting keeps a TTL only with `EX`/`PX` again or `KEEPTTL`.
- Jitter is computed in the app and passed as an integer (`EX` takes whole seconds; use `PX` for sub-second jitter).
- `keyPrefix` (both clients) prefixes keys sent, but not `SCAN`/`KEYS` `MATCH` patterns, Pub/Sub channels, or keys returned by `SCAN`: passing scanned keys back double-prefixes them. Prefer building the full key in the shared key function, one place.
- Pub/Sub channels ignore the DB number: prefix channels with environment and service too.

## 2. Client setup and fail-open (steps 3, 5)

- One long-lived client per process (a provider closed in shutdown hooks), never one per request. Both clients multiplex one connection and pipeline concurrent commands (node-redis automatically per tick; ioredis with `enableAutoPipelining`).
- Commands that hold a connection (`BLPOP`-style, `WATCH`/`MULTI`, `SUBSCRIBE` on RESP2) need their own connection: `duplicate()` in both clients, or node-redis `createClientPool`. The cache read path uses none of them.
- Defaults wait too long for Rule `cache` 9; set explicitly, shorter than the source query:
  - node-redis: `commandOptions.timeout` (default 5000 ms), `socket.connectTimeout` (default 5000 ms), `disableOfflineQueue: true` so commands fail at once while reconnecting instead of queuing.
  - ioredis: `commandTimeout` (default none: waits forever), `connectTimeout` (default 10000 ms), `maxRetriesPerRequest` (default 20 reconnect attempts per queued command) set low, or `enableOfflineQueue: false`.
- node-redis: if you set `socket.socketTimeout`, the default `reconnectStrategy` returns `false` on that timeout and the client closes for good; provide your own `reconnectStrategy` (bounded backoff with jitter).
- node-redis throws and exits the process on an `error` event with no listener; always attach one (log, count fail-open). ioredis only logs to console, still attach one.
- A timeout or error is a cache error, not a miss (`patterns.md` §3): do not write back. Retries stay in the app wrapper with a bound, not in unlimited client retries.

## 3. Single-flight lock across instances (steps 3, 5)

- Acquire: `SET <lock-key> <random token> NX PX <ms>`, one command. Not `SETNX` + `EXPIRE`. Lock TTL ≥ loader timeout; waiters give up per `patterns.md` §3.
- Release only if the token still matches: Lua `if GET == token then DEL` (node-redis `defineScript`, ioredis `defineCommand`), or on Redis ≥ 8.4 `DELEX <lock-key> IFEQ <token>` (node-redis `delEx`; ioredis 6.0.0 has no typed method, use `call`). A plain `DEL` can remove another instance's lock after yours expired.
- Single-node `SET NX` lock is enough for stampede only; it is not safe as a business lock (Rule `cache` 3), and Redlock is not a reason to use it as one.
- Version-compare overwrite (`patterns.md` §4) needs a Lua script comparing versions. `SET … IFEQ` (8.4) only checks equality with the current value, not "newer than".

## 4. Delete after commit and L1 invalidation (steps 3, 5)

- Delete with `UNLINK` (memory freed in a background thread); `DEL` on a large value blocks the server. Both are idempotent, so retrying a failed delete is safe.
- Group delete when no version prefix: `SCAN` cursor loop (`scanIterator` in node-redis, `scanStream` in ioredis) + batched `UNLINK`. `MATCH` filters after fetching, so pages can be empty: stop only when the cursor returns `0`. Keys may repeat; `COUNT` is a hint.
- L1 events via Pub/Sub are **at-most-once**: a message published while an instance is disconnected is lost, and resubscribe on reconnect does not replay it. Clear all of L1 on the client's reconnect/`ready` event, not only on channel errors.
- Subscribe on a dedicated `duplicate()` connection. On RESP2 a subscribed connection rejects normal commands; both clients default to RESP3, but do not rely on mixing.
- RESP3 client-side caching (node-redis `clientSideCache`, RESP 3 only; not built into ioredis 6.0.0) is an L1: record it in the design under Rule `cache` 7, do not switch it on silently.

## 5. Cluster and replicas (steps 2, 3)

- Multi-key commands (`MGET`, multi-key `UNLINK`, `MULTI`, Lua with several `KEYS`) fail with `CROSSSLOT` unless all keys share a slot; ioredis also rejects cross-slot pipelines. Either send per key or put a hash tag on the entity, e.g. `<service>:<module>:{<entity>:<id>}:<variant>`; tag only key groups that need multi-key ops (tagging everything makes hot slots).
- `SCAN` in a cluster covers one node: iterate every master (node-redis `cluster.masters` + `nodeClient`, ioredis `cluster.nodes('master')`).
- Classic `PUBLISH` broadcasts to every node; Redis ≥ 7.0 sharded Pub/Sub (`SPUBLISH`/`SSUBSCRIBE`; node-redis `sSubscribe`, ioredis `shardedSubscribers`) scales better if invalidation traffic is heavy.
- Replica reads (node-redis `useReplicas`, ioredis `scaleReads`) lag the primary: a read right after delete-after-commit can return the old value. Keep cache reads on primaries unless the staleness window explicitly allows replica lag.

## 6. Memory, persistence, access (step 4; step 2 when the value is D3)

- Default `maxmemory` 0 means no limit. Dedicated cache instance: `allkeys-lru` or `allkeys-lfu`. `volatile-*` behaves like `noeviction` when no key has a TTL; `noeviction` makes writes fail when full (cache writes are then errors, fail-open applies).
- If locks, the hot-list sorted set, or the warm-up epoch key share the instance, `allkeys-*` may evict them; this is acceptable only because each is safe to lose (`warmup.md` §3). Otherwise use a separate instance.
- D3 key group with persistence off: `save ""` and `appendonly no` on that instance (replicas too).
- Per-service ACL user: `~<service>:*` keys, `&<service>:*` channels (from 7.0 new users get no channels; subscribe fails with `NOPERM`), only needed commands. Key patterns do not limit `FLUSHALL`/`FLUSHDB`/`SWAPDB`: remove them (`-@dangerous` also removes `KEYS`). Without `INFO`, ioredis skips its ready check with a warning; set `enableReadyCheck: false` deliberately.
- TLS: node-redis `socket.tls: true` (or `rediss://` URL), ioredis `tls: {}`; with `username`/`password` of that ACL user.
- Eviction and hit metrics come from `INFO stats` (`keyspace_hits`, `keyspace_misses`, `evicted_keys`) read by a monitoring account, since the app user has no `INFO`.
