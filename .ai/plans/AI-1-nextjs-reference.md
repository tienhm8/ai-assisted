# PLAN: AI-1 — Tiếp nhận skill vercel-react-best-practices vào reference Next.js

> AI soạn; người duyệt theo điều kiện của quy trình thực hiện Task. Mục "Kết quả" điền sau khi xong.

| Mục | Giá trị |
| --- | --- |
| Trạng thái | Done |
| Loại Task | T12 (Documentation only, sửa vùng 🔴 `.ai/`) |
| Mức rủi ro · Mức tự chủ | R1 · A3 (Tech Lead duyệt 2026-11-15); độ nghiêm ngặt S2 |
| Model · Effort phiên thực thi | M2·E1 (mặc định T12) |

## 1. Mục tiêu và phạm vi
- Làm: tạo `frontend-development/references/nextjs.md` từ skill nguồn; thêm bảng References vào `frontend-development/SKILL.md`.
- Không làm: skill `vercel/next.js/next-cache-components-*`; sửa `docs/`, Rule, Skill khác; chuyển Approved (cần chạy thử trên Task thật, external-skills §Quy trình bước 5).

## 2. Yêu cầu và ngữ cảnh đã nạp
- Nguồn: github.com/vercel-labs/agent-skills @ dc8367e (commit cuối của thư mục skill; HEAD repo 1a2c79d, nội dung SKILL.md trùng), MIT, v1.0.0, 70 quy tắc, không có script.
- external-skills §Chọn lọc phần nào: chỉ lấy lỗi AI hay mắc, khác biệt phiên bản; §Đưa vào đâu: riêng công nghệ → `references/<công-nghệ>.md`; §Ghi nguồn: hai dòng Nguồn/Đã điều chỉnh.
- skills/README §Cách tổ chức: `SKILL.md` trung lập công nghệ, ghi bước nào nạp mục nào.
- cache-rules 7, 11 → bỏ `server-cache-lru`. project-rules 6 → bỏ quy tắc cần SWR, `better-all`. project-rules 16 → đối chiếu API với package.

## 3. Rule và chuỗi Skill
- Rule đã nạp: project-rules; git (Task có commit). `architecture` không nạp: không chạm ranh giới module, hợp đồng API.
- Chuỗi Skill: `documentation` (mặc định T12).
- Nạp bổ sung: docs nâng cấp `next/dist/docs/01-app/02-guides/upgrading/version-16.md` của next 16.4.6, để lấy khác biệt phiên bản mà skill nguồn không có.

## 4. Thiết kế và file dự kiến thay đổi
- `nextjs.md` chia 6 mục theo bước của Skill để nạp từng mục: §1 khác biệt v16, §2 ranh giới server/client, §3 fetch dữ liệu, §4 Server Action/Route Handler, §5 render/hydration, §6 bundle.
- `SKILL.md`: thêm mục `## References` theo mẫu backend-development.

## 5. Kế hoạch kiểm thử
| AC | Kiểm |
| --- | --- |
| AC1 dòng nguồn | Đọc lại đầu file |
| AC2 không mâu thuẫn Rule, không thêm package | Rà từng quy tắc giữ lại với cache-rules, project-rules 6 |
| AC3 API có trong phiên bản | `npm pack next@16.4.6 react@19.3.1 @types/react@19`, grep `.d.ts` và docs đi kèm |
| AC4 bảng References | Đọc `SKILL.md`; không tên công nghệ trong phần thân |
| AC5 ≤ 80 dòng | `wc -l` |
| Nạp theo mục | Lệnh đọc một mục ở task-execution chạy với `## 1`, `## 4`, `## 6` |

## 6. Rủi ro và điểm cần người quyết
Không có.

## 7. Kết quả
- `nextjs.md` 51 dòng; lệnh đọc một mục trả exit 0 cho các mục thử.
- Đối chiếu (AC3): `after` (`next/server.d.ts`, `after.md`: chạy cả khi lỗi/redirect/notFound, Server Component không gọi `cookies`/`headers` bên trong); `optimizePackageImports`, `reactCompiler`, `cacheComponents` (`config-shared.d.ts`); danh sách thư viện tối ưu sẵn (`optimizePackageImports.md`); `cache`, `use`, `Activity`, `useEffectEvent`, `suppressHydrationWarning` (`@types/react` 19.3.0 `index.d.ts`); Server Action là POST công khai (`server-actions.md`); `NEXT_PUBLIC_` (`environment-variables.md`); memo `fetch` không áp dụng Route Handler (`04-glossary.md`); khác biệt v16 (`version-16.md` §Async Request APIs, §Caching APIs, §middleware to proxy, §Parallel Routes, §Removals).
- Lệch kế hoạch: thêm §1 khác biệt phiên bản lấy từ docs Next.js (không có trong skill gốc), đã ghi ở dòng "Đã điều chỉnh". Bỏ `Activity` khỏi file vì là tối ưu, không phải lỗi hay mắc.
