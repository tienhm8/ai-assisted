# skills

Skill là kỹ năng chuyên môn và quy trình làm việc của AI: làm một loại việc thì làm thế nào. Rule trả lời câu hỏi khác: AI phải tuân thủ điều gì.

File này dành cho người viết và duyệt Skill; AI không cần nạp khi làm Task.

## Danh mục Skill

| Skill | Nhiệm vụ |
| --- | --- |
| product-discovery | Biến brief của PO thành vision, scope, glossary, câu hỏi mở |
| requirement-analysis | Phân tích yêu cầu |
| requirement-review | Kiểm tra tính đầy đủ của yêu cầu |
| architecture-design | Thiết kế kiến trúc |
| database-design | Thiết kế database |
| task-planning | Lập plan và chia Task từ FR/thiết kế đã duyệt |
| api-development | Phát triển API |
| frontend-development | Phát triển giao diện |
| backend-development | Phát triển backend |
| authentication-rbac | Xây dựng phân quyền |
| unit-testing | Viết unit test |
| integration-testing | Viết integration test |
| e2e-testing | Kiểm thử end-to-end |
| code-review | Review code |
| security-review | Kiểm tra bảo mật |
| bug-fixing | Điều tra và sửa lỗi |
| refactoring | Tái cấu trúc |
| documentation | Cập nhật tài liệu |
| deployment | Chuẩn bị và kiểm tra phát hành |
| incident-analysis | Phân tích log và sự cố |
| continuous-improvement | Tổng hợp KPI, đề xuất cải tiến rule/skill |

## Cách tổ chức

- Mỗi Skill một thư mục, `SKILL.md` là file bắt buộc. Khi cần thì thêm `references/` (chi tiết theo chủ đề hoặc theo công nghệ), `examples.md` (ví dụ minh hoạ, không phải nghiệp vụ chính thức), `scripts/`.
- `SKILL.md` giữ quy trình tổng quát, trung lập công nghệ. Chi tiết dài hoặc chỉ dùng ở một bước thì đưa vào `references/`, và `SKILL.md` ghi rõ bước nào nạp file nào.
- Chọn và phối hợp Skill nằm ở workflow (`task-types`, `task-execution`), không nằm trong từng Skill.

## Cấu trúc một SKILL.md

| Mục | Nội dung |
| --- | --- |
| Frontmatter `name`, `description` | Skill làm gì và dùng khi nào; đủ để chọn Skill mà không cần đọc phần thân |
| Mở đầu | Một đến hai câu về mục tiêu |
| Cổng vào | Điều kiện bắt đầu, thiếu thì dừng; tài liệu cần đọc |
| Quy trình | Các bước theo thứ tự |
| Giới hạn (nếu có) | Chỉ điều riêng của Skill này |
| Hoàn thành khi | Kết quả kiểm chứng được |
| Báo cáo | Chỉ phần riêng của Skill; phần chung theo template |

Thiếu Cổng vào, Quy trình, Hoàn thành khi hoặc Báo cáo thì Skill chưa được chuyển Approved.

## Viết Skill cho gọn

Mỗi dòng trong Skill được nạp lại ở mọi Task dùng nó, nên:

- **Không nhắc lại Rule.** Rule đã được nạp cùng Task. Skill chỉ ghi giới hạn mà Rule chưa có.
- **Không nhắc lại Quy trình** dưới dạng checklist. "Hoàn thành khi" chỉ ghi kết quả kiểm chứng được.
- **Không chép template.** Báo cáo chỉ nêu phần Skill này thêm vào.
- **Không ghi kiến thức chung model đã biết.** Chỉ ghi quy ước đã chốt, lỗi AI hay mắc, và điểm dễ sót.
- **Không chép chuẩn, ngưỡng, mã lỗi** từ `docs/`; nêu tên tài liệu cần đọc ở Cổng vào.
- Một `SKILL.md` vượt khoảng 150 dòng thì tách phần chi tiết sang `references/`.

## Khi đưa Skill vào dùng

- Skill không thay Rule và không thay tài liệu nghiệp vụ; ví dụ trong Skill không phải nghiệp vụ chính thức.
- Skill mới hoặc Skill vừa sửa phải chạy thử trên Task thật trước khi chuyển Approved.
- Chỉ tạo Skill khi quy trình đã ổn định; không tạo Skill để đặt tên cho một prompt ngắn.
- Sửa Skill cần Task riêng và người duyệt.

## Tiếp nhận Skill bên ngoài

Skill bên ngoài gồm skill cộng đồng (ví dụ skills.sh) và guideline do package sinh ra (ví dụ Laravel Boost). Chúng **chỉ là tài liệu tham khảo**. Người chọn lọc phần phù hợp rồi thêm hoặc sửa vào Skill hiện có. Lý do: AI chỉ có một nguồn chỉ dẫn, nội dung đã có người đọc trước khi vào repo, và context không bị nạp thừa.

### Không được

- Cài skill bên ngoài vào thư mục mà công cụ AI tự nạp (ví dụ `.claude/skills/`, `.cursor/rules/`) hoặc để AI đọc trực tiếp từ URL.
- Chạy script đi kèm skill bên ngoài khi chưa đọc và chưa được duyệt.
- Chép nguyên cả skill. Chỉ lấy phần dự án cần.

### Chọn lọc phần nào

Chỉ lấy phần làm AI làm đúng hơn, không lấy kiến thức chung về framework mà model đã biết:

- quy ước nhóm đã chốt;
- lỗi AI hay mắc với framework đó;
- khác biệt giữa các phiên bản framework (API cũ, API đã bỏ).

### Đưa vào đâu

| Nội dung lấy từ skill bên ngoài | Đưa vào |
| --- | --- |
| Bước làm việc hoặc mục checklist tổng quát, không gắn công nghệ | `SKILL.md` của Skill tương ứng |
| Cách làm riêng của một công nghệ (framework, ORM, CSDL) | `references/<công-nghệ>.md` trong thư mục Skill, ví dụ `backend-development/references/nestjs.md` |
| Điều bắt buộc (cấm, phải, ngưỡng) | `docs/03-engineering/` hoặc `.ai/rules/`, vì Skill không chép chuẩn |
| Đoạn code minh hoạ | `examples.md` |

`SKILL.md` vẫn giữ trung lập công nghệ. `references/` có thể đã có file theo chủ đề (ví dụ `database-design/references/caching.md`). Nội dung chung cho nhiều công nghệ thì bổ sung vào file chủ đề đó; nội dung riêng một công nghệ thì để file `<công-nghệ>.md` riêng, mỗi file một công nghệ. Không file nào được mâu thuẫn với `SKILL.md`, `docs/` hay `.ai/rules/`.

### Ghi nguồn

Đầu mỗi file `references/` lấy từ nguồn ngoài ghi:

```markdown
> Nguồn: <repo hoặc package> @ <commit/phiên bản> · Ngày lấy: YYYY-MM-DD · Áp dụng cho: <công nghệ> <phiên bản>
> Đã điều chỉnh: <tóm tắt phần bỏ hoặc sửa so với bản gốc>
```

Nhiều nguồn thì ghi đủ từng nguồn. Không ghi được nguồn thì không tiếp nhận.

### Quy trình

1. **Task riêng** (loại T12, sửa vùng 🔴). Task nêu skill bên ngoài nào, lấy cho Skill nào.
2. **Đọc toàn bộ** skill bên ngoài, gồm cả script. Bỏ chỉ dẫn mâu thuẫn với `docs/`, `.ai/rules/` hoặc mức tự chủ ở `PROJECT.md`, ví dụ tự chạy migration, tự deploy, tự cài dependency.
3. **Viết lại** bằng giọng văn và khung của repo, theo bảng "Đưa vào đâu".
4. **PR**, Tech Lead duyệt. Mô tả PR liệt kê phần đã lấy và phần đã bỏ, kèm lý do.
5. **Chạy thử** bằng một Task thật của công nghệ đó trước khi chuyển Approved.
6. **Rà soát định kỳ** (T15, `continuous-improvement`): so lại với bản gốc và với phiên bản công nghệ dự án đang dùng. Khi nâng cấp phiên bản framework thì rà ngay, không đợi tới kỳ.

### Công cụ đi kèm (MCP server)

Package như Laravel Boost có thêm MCP server, tức công cụ cho AI gọi (đọc schema, tra tài liệu, đọc log, chạy lệnh). Phần này **không chép được**. Nếu dùng thì khai báo ở `PROJECT.md` §2.1 như một công cụ có giới hạn quyền. Phần guideline của package vẫn tiếp nhận theo quy trình trên; tắt tính năng tự ghi guideline vào file tích hợp (`CLAUDE.md`, `AGENTS.md`…) để file đó vẫn chỉ trỏ về `.ai/`.
