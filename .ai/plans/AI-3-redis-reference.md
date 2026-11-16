# PLAN: AI-3 — Tiếp nhận skill redis/agent-skills vào reference Redis của caching

> AI soạn; người duyệt theo điều kiện của quy trình thực hiện Task. Mục "Kết quả" điền sau khi xong.

| Mục | Giá trị |
| --- | --- |
| Trạng thái | Done |
| Loại Task | T12 (Documentation only, sửa vùng 🔴 `.ai/`) |
| Mức rủi ro · Mức tự chủ | R1 · A3 (Tech Lead duyệt 2026-11-15); độ nghiêm ngặt S2 |
| Model · Effort phiên thực thi | M2·E1 |

## 1. Mục tiêu và phạm vi
- Làm: tạo `caching/references/redis.md` (cách làm riêng Redis cho L2, client Node); thêm dòng vào bảng References của `caching/SKILL.md`.
- Không làm: sửa `cache-rules`, `patterns.md`, `warmup.md`; chọn client cho dự án; cấu hình máy chủ thuộc hạ tầng.

## 2. Yêu cầu và ngữ cảnh đã nạp
- Nguồn: github.com/redis/agent-skills @ 74708da, MIT, `redis-core`, `redis-connections` v0.1.0 (tham khảo `redis-security`, `redis-clustering`); không có script; ví dụ gốc là Python/Java.
- cache-rules 3, 4, 5, 7, 9 và patterns.md §3, §4, §8: file mới chỉ ghi cách làm bằng Redis cho các điểm đó, không nhắc lại.

## 3. Rule và chuỗi Skill
- Rule: project-rules; git. `cache` đọc để đối chiếu, không áp cho Task (Task không thêm cache). Chuỗi Skill: `documentation`.

## 4. Thiết kế và file dự kiến thay đổi
`redis.md` 6 mục theo bước: §1 key/TTL, §2 client và fail-open, §3 khoá single-flight, §4 xoá sau commit và L1, §5 cluster/replica, §6 bộ nhớ, persistence, ACL/TLS.

## 5. Kế hoạch kiểm thử
`npm pack redis@6.3.1 @redis/client ioredis@6.0.0` và đọc `.d.ts`/README (không chạy code package); lệnh Redis đối chiếu redis.io; `wc -l`.

## 6. Rủi ro và điểm cần người quyết
Không có. Ghi nhận: README ioredis 6.0.0 khuyên dùng node-redis cho dự án mới; chọn client là quyết định dự án, ghi khi điền system-architecture §4.

## 7. Kết quả
- `redis.md` 55 dòng; bảng References thêm một dòng.
- Bốn chỗ nguồn trái Rule đã sửa: Hash để cập nhật từng field (trái cache-rules 5); đọc replica "hợp cho cache" (trái patterns.md §4); `retry_on_timeout` không giới hạn (trái cache-rules 9); ACL mẫu `~*` (trái cache-rules 4, patterns.md §8).
- Đã đối chiếu: mặc định timeout, offline queue, `maxRetriesPerRequest`, RESP3, `reconnectStrategy` trả `false` khi socket timeout, cảnh báo `keyPrefix` với `scanIterator`, không có `delex` trong ioredis (file `.d.ts`); `SET` (IFEQ từ 8.4), `DELEX` (8.4), `UNLINK`, `SCAN`, eviction, Pub/Sub at-most-once, sharded Pub/Sub (7.0), ACL kênh (7.0), persistence (redis.io).
- Chưa kiểm: không chạy với Redis thật; chữ ký chính xác của `delEx` chỉ thấy tồn tại trong `commands/index.d.ts`.
