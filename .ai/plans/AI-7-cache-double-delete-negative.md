# PLAN: AI-7 — Skill caching: bỏ xoá kép trái Rule, bổ sung điều kiện negative cache

> AI soạn; người duyệt theo điều kiện của quy trình thực hiện Task. Mục "Kết quả" điền sau khi xong.

| Mục | Giá trị |
| --- | --- |
| Trạng thái | Done (plan Tech Lead duyệt 2026-11-15) |
| Loại Task | T12 (Documentation only, sửa vùng 🔴 `.ai/`) |
| Mức rủi ro · Mức tự chủ | R1 · A3 (Tech Lead duyệt 2026-11-15); độ nghiêm ngặt S2 |
| Model · Effort phiên thực thi | M2·E1 (mặc định T12) |

## 1. Mục tiêu và phạm vi
- Làm: điểm (1) và (6) của bản rà soát Skill caching; Tech Lead chọn phương án A cho cả hai (2026-11-15).
  - (1) `patterns.md` §4: bỏ "delayed double delete" (lần xoá đầu trước commit, trái cache-rules 5); trỏ về cơ chế chống ghi lại giá trị cũ đã thêm ở AI-6.
  - (6) `patterns.md` §5: negative cache chỉ dùng khi bảng AP có số liệu; sentinel khác miss; TTL ≤ khoảng trễ chấp nhận; đường tạo xoá key rỗng sau commit, kể cả khoá tự nhiên; không dùng cho danh sách. §6: chuyển negative cache từ cột mặc định sang cột thêm khi cần cho khớp.
- Không làm: sửa `cache-rules.md` (Rule 5, 6 đã bao); sửa `docs/`; chuyển Approved.

## 2. Yêu cầu và ngữ cảnh đã nạp
- cache-rules 5: chỉ xoá sau commit → lý do bỏ xoá trước commit.
- cache-rules 6: không cache kết quả lỗi; key có TTL jitter → áp dụng cho key rỗng.
- patterns §4 (AI-6): marker / version / chấp nhận TTL thay vai trò của xoá kép.

## 3. Rule và chuỗi Skill
- Rule đã nạp: project-rules; git; cache.
- Chuỗi Skill: `documentation`.

## 4. Thiết kế và file dự kiến thay đổi
- `.ai/skills/caching/references/patterns.md`: §4 dòng "Read right after write"; §5 dòng "Negative caching"; §6 dòng "Lookups for nonexistent IDs".

## 5. Kế hoạch kiểm thử
| AC | Kiểm |
| --- | --- |
| AC1 không còn chỉ dẫn xoá trước commit | `grep -n "double delete" .ai docs` không còn kết quả ngoài `plans/` |
| AC2 không mâu thuẫn Rule | Rà với cache-rules 5, 6 |
| AC3 mục nạp vẫn chạy | Lệnh đọc một mục với `## 4`, `## 5`, `## 6` của `patterns.md`: exit 0 |
| AC4 tham chiếu đúng | §5 được nhắc ở §6 tồn tại |

## 6. Rủi ro và điểm cần người quyết
Không có.

## 7. Kết quả
- `patterns.md` +6/−3 dòng: §4 xoá kép thay bằng trỏ về marker/version, cấm xoá trước commit; §5 negative cache thêm điều kiện dùng, sentinel, TTL, xoá ở đường tạo; §6 negative cache chuyển sang cột "Add when needed".
- AC1: `grep "double delete"` ngoài `plans/` không còn. AC2: rà với cache-rules 5, 6, không mâu thuẫn. AC3: `## 4`, `## 5`, `## 6` exit 0. AC4: §5 "Key and TTL" tồn tại.
- Lệch kế hoạch: không. Chưa kiểm: chạy thử trên Task cache thật (theo waiver của Skill).
