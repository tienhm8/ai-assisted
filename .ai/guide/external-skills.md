# Tiếp nhận Skill bên ngoài

> Dành cho người viết và duyệt Skill; AI không nạp khi làm Task. Tách từ `.ai/skills/README.md`.

Skill bên ngoài gồm skill cộng đồng (ví dụ skills.sh) và guideline do package sinh ra (ví dụ Laravel Boost). Chúng **chỉ là tài liệu tham khảo**. Người chọn lọc phần phù hợp rồi thêm hoặc sửa vào Skill hiện có. Lý do: AI chỉ có một nguồn chỉ dẫn, nội dung đã có người đọc trước khi vào repo, và context không bị nạp thừa.

## Không được

- Cài skill bên ngoài vào thư mục mà công cụ AI tự nạp (ví dụ `.claude/skills/`, `.cursor/rules/`) hoặc để AI đọc trực tiếp từ URL.
- Chạy script đi kèm skill bên ngoài khi chưa đọc và chưa được duyệt.
- Chép nguyên cả skill. Chỉ lấy phần dự án cần.

## Chọn lọc phần nào

Chỉ lấy phần làm AI làm đúng hơn, không lấy kiến thức chung về framework mà model đã biết:

- quy ước nhóm đã chốt;
- lỗi AI hay mắc với framework đó;
- khác biệt giữa các phiên bản framework (API cũ, API đã bỏ).

## Đưa vào đâu

| Nội dung lấy từ skill bên ngoài | Đưa vào |
| --- | --- |
| Bước làm việc hoặc mục checklist tổng quát, không gắn công nghệ | `SKILL.md` của Skill tương ứng |
| Cách làm riêng của một công nghệ (framework, ORM, CSDL) | `references/<công-nghệ>.md` trong thư mục Skill, ví dụ `backend-development/references/nestjs-11.md` |
| Điều bắt buộc (cấm, phải, ngưỡng) | `docs/03-engineering/` hoặc `.ai/rules/`, vì Skill không chép chuẩn |
| Đoạn code minh hoạ | `examples.md` |

`SKILL.md` vẫn giữ trung lập công nghệ. `references/` có thể đã có file theo chủ đề (ví dụ `caching/references/patterns.md`). Nội dung chung cho nhiều công nghệ thì bổ sung vào file chủ đề đó; nội dung riêng một công nghệ thì để file `<công-nghệ>.md` riêng, mỗi file một công nghệ. Không file nào được mâu thuẫn với `SKILL.md`, `docs/` hay `.ai/rules/`.

## Đầu file reference

Chỉ ghi một dòng phạm vi áp dụng, không trích dẫn nguồn:

```markdown
> Áp dụng cho: <công nghệ> <phiên bản>. <điều kiện hoặc ngoại lệ của project, nếu có>
```

Nguồn, ngày lấy và phần đã bỏ thuộc về mô tả PR (bước 4 bên dưới), không nằm trong file. Không ghi được nguồn trong PR thì không tiếp nhận.

## Quy trình

1. **Task riêng** (loại chỉ sửa tài liệu, sửa vùng 🔴). Task nêu skill bên ngoài nào, lấy cho Skill nào.
2. **Đọc toàn bộ** skill bên ngoài, gồm cả script. Bỏ chỉ dẫn mâu thuẫn với `docs/`, `.ai/rules/` hoặc mức tự chủ ở `PROJECT.md`, ví dụ tự chạy migration, tự deploy, tự cài dependency.
3. **Viết lại** bằng giọng văn và khung của repo, theo bảng "Đưa vào đâu".
4. **PR**, Tech Lead duyệt. Mô tả PR ghi nguồn (repo hoặc package, commit hoặc phiên bản, ngày lấy), liệt kê phần đã lấy và phần đã bỏ, kèm lý do.
5. **Chạy thử** bằng một Task thật của công nghệ đó trước khi chuyển Approved.
6. **Rà soát định kỳ** (loại rà soát định kỳ, `continuous-improvement`): so lại với nguồn ghi trong PR và với phiên bản công nghệ dự án đang dùng. Khi nâng cấp phiên bản framework thì rà ngay, không đợi tới kỳ.

## Công cụ đi kèm (MCP server)

Package như Laravel Boost có thêm MCP server, tức công cụ cho AI gọi (đọc schema, tra tài liệu, đọc log, chạy lệnh). Phần này **không chép được**. Nếu dùng thì khai báo ở [PROJECT.md](../../PROJECT.md) mục "Công cụ AI" như một công cụ có giới hạn quyền. Phần guideline của package vẫn tiếp nhận theo quy trình trên; tắt tính năng tự ghi guideline vào file tích hợp (`CLAUDE.md`, `AGENTS.md`…) để file đó vẫn chỉ trỏ về `.ai/`.
