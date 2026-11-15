# PLAN: AI-6 — Vá lỗ hổng nhất quán của Skill caching (ghi đè giá trị cũ, độ trễ replica, lock, failover)

> AI soạn; người duyệt theo điều kiện của quy trình thực hiện Task. Mục "Kết quả" điền sau khi xong.

| Mục | Giá trị |
| --- | --- |
| Trạng thái | Done (plan Tech Lead duyệt 2026-11-15) |
| Loại Task | T12 (Documentation only, sửa vùng 🔴 `.ai/`) |
| Mức rủi ro · Mức tự chủ | R1 · A3 (Tech Lead duyệt 2026-11-15); độ nghiêm ngặt S2 |
| Model · Effort phiên thực thi | M2·E1 (mặc định T12) |

## 1. Mục tiêu và phạm vi
- Làm: 4 điểm rà soát được Tech Lead đồng ý (2026-11-15), đánh số theo bản rà soát:
  - (2) Đường đọc ghi lại giá trị cũ sau khi đường ghi đã xoá key.
  - (3) Hàm nạp hoặc warm-up đọc read replica của CSDL, nạp lại dòng cũ.
  - (4) Nguyên tắc lock không phụ thuộc công nghệ (cách làm với Redis đã có ở `redis.md` §3).
  - (5) Failover của tầng cache làm sống lại key vừa xoá.
- File: `caching/references/patterns.md`, `caching/references/warmup.md`, `caching/SKILL.md` (thêm 1 ca kiểm ở bước 6).
- Không làm:
  - Điểm (1) (thứ tự xoá kép ở `patterns.md:59`) và điểm (6) (negative cache): Tech Lead chưa chọn đề xuất. Giữ nguyên dòng 59 và 73.
  - Sửa `cache-rules.md`: các thay đổi chỉ nói cách làm, nằm trong phạm vi Rule 5 và 9 hiện có.
  - Sửa `docs/` (database-design §3.7, deployment): đã có cột "Mô hình đọc/ghi" để ghi lựa chọn, không cần thêm cột.
  - Chuyển Approved.

## 2. Yêu cầu và ngữ cảnh đã nạp
- cache-rules 5: xoá sau commit; ghi đè chỉ khi so version. Điểm (2) không trái Rule: marker không phải giá trị dữ liệu, key dữ liệu vẫn bị xoá.
- cache-rules 1: xoá toàn bộ cache không đổi kết quả nghiệp vụ. Điểm (5) dùng xoá theo nhóm, nên phù hợp.
- patterns §3 (đường đọc), §4 (đường ghi), §11 (ghi vào thiết kế); warmup §1 (trigger), §4 (quy tắc job).
- redis.md §3: lock `SET NX PX`, nhả khoá bằng token, cần Lua khi so version; §5: hash tag cho thao tác nhiều key.

## 3. Rule và chuỗi Skill
- Rule đã nạp: project-rules; git (Task có commit); cache (Task sửa nội dung Skill caching). `architecture` không nạp: không chạm ranh giới module.
- Chuỗi Skill: `documentation`.

## 4. Thiết kế và nội dung dự kiến (bản nháp để duyệt)

### 4.1 `patterns.md` §3 Read path
Sau gạch đầu dòng `Across instances` (dòng 44), thêm:
```
    - Lock TTL ≥ loader timeout, otherwise a second loader runs while the first is still loading. Only the owner releases the lock (token check); a plain delete can remove another instance's lock. Redis: `redis.md` §3.
```
Sau gạch đầu dòng `Write paths bypass cache` (dòng 47), thêm:
```
- **Loader reads the primary.** With DB read replicas, a loader reading a replica right after delete-after-commit can reload the old row and cache it for a full TTL. Read a replica only when the acceptable staleness window covers max replica lag plus TTL; record it in the cache row. Same for warm-up.
```

### 4.2 `patterns.md` §4 Write path and invalidation
Sau gạch đầu dòng `Delete, do not update` (dòng 57), thêm:
```
- **Stale write-back race:** delete-after-commit alone does not prevent it. Read A misses and loads the old row; write B commits and deletes the key; A then writes the old value, which lives until TTL. Choose one per cache, record it in the cache row:
  - **Invalidation marker (default when read-after-write matters):** the delete step first sets a short marker for the key (TTL ≥ loader timeout), then deletes the key. Write-back is an atomic conditional write: skip if the marker exists, just return the DB value. Marker and key must be usable in one atomic step (Redis: one Lua script, same hash slot, `redis.md` §3, §5).
  - **Version overwrite:** writes overwrite with version comparison instead of deleting, and write-back also compares versions (W1 keys).
  - **Accept TTL:** only when the staleness window ≥ that key's TTL.
- **Cache failover can undo deletes:** with asynchronous replication, deletes acknowledged shortly before a failover may be lost and old values reappear. For groups whose staleness window is shorter than TTL, the failover runbook clears the group (version prefix bump or batched scan + delete) then triggers warm-up (`warmup.md` §1); otherwise record that TTL covers it.
```

### 4.3 `patterns.md` §11 Recording in the design
Thêm:
```
- Stale write-back guard chosen (§4), loader source primary or replica with reason (§3), failover handling (§4).
```

### 4.4 `warmup.md`
§1, thêm dòng vào bảng trigger:
```
| Cache failover (deletes may be lost) | Failover event or alert from the cache's HA; runbook per `patterns.md` §4 |
```
§4, dòng `Read from a read-only replica if available` đổi thành:
```
  - Read from a read-only replica only if the cache row allows replica reads (`patterns.md` §3); otherwise read the primary within the load budget.
```
§4, dòng `W2 writes only when the key does not exist (SET NX)` đổi thành:
```
  - W2 writes only when the key does not exist and no invalidation marker exists (`patterns.md` §4), in one atomic step.
```

### 4.5 `SKILL.md` bước 6 Verify
Thêm ca kiểm:
```
   - A read missing the key runs concurrently with a write: the cache does not end up holding the old value (unless the cache row records "accept TTL").
```

## 5. Kế hoạch kiểm thử
| AC | Kiểm |
| --- | --- |
| AC1 không mâu thuẫn Rule | Rà từng đoạn thêm với cache-rules 1, 5, 9; với redis.md §3, §5 |
| AC2 không đụng điểm (1), (6) | `git diff` không chạm `patterns.md` dòng 59, 73 |
| AC3 mục nạp vẫn chạy | Lệnh đọc một mục ở task-execution với `## 3`, `## 4` của `patterns.md`, `## 1`, `## 4` của `warmup.md`: exit 0 |
| AC4 tham chiếu chéo đúng | Mọi `§` được nhắc tới tồn tại; bảng References của `SKILL.md` không cần đổi (§3, §4, §11 đã nạp ở bước 3, 4) |

## 6. Rủi ro và điểm cần người quyết
Đã quyết (Tech Lead, 2026-11-15, theo đề xuất): mã Task `AI-6`; R1 · A3 · S2; điểm (2) mặc định marker.

## 7. Kết quả (điền sau khi xong)
- `patterns.md` +8 dòng: §3 lock TTL và chủ lock, loader đọc primary; §4 race ghi lại giá trị cũ (marker mặc định, version, chấp nhận TTL), failover cache; §11 ghi lựa chọn vào dòng cache.
- `warmup.md`: §1 thêm trigger failover; §4 replica theo dòng cache, W2 kiểm tra marker.
- `SKILL.md` bước 6: thêm ca đọc miss chạy song song với ghi.
- AC1: rà với cache-rules 1, 5, 9 và redis.md §3, §5, không mâu thuẫn. AC2: `git diff` không xoá dòng nào của `patterns.md`; dòng xoá kép và negative caching giữ nguyên (nay ở dòng 66, 80). AC3: lệnh đọc một mục trả exit 0 cho patterns `## 3`, `## 4`, `## 11`, warmup `## 1`, `## 4`. AC4: patterns §3, §4, warmup §1, redis §3, §5 tồn tại; bảng References không cần đổi.
- Lệch kế hoạch: không. Chưa kiểm: chạy thử trên Task cache thật (theo waiver của Skill).
