# skills

Skill là **kỹ năng chuyên môn và quy trình làm việc của AI**. Khác với Rule:

- **Rule** trả lời: AI phải tuân thủ điều gì?
- **Skill** trả lời: AI phải thực hiện một loại công việc như thế nào?

Yêu cầu AI "hãy code API" là chưa đủ: Skill hướng dẫn AI từng bước (đọc yêu cầu, kiểm tra thiết kế đã duyệt, xác định quyền, viết, kiểm thử, cập nhật tài liệu, báo cáo kết quả).

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

Các Skill ở trạng thái Draft, làm rõ dần theo Task thật. Chỉ thêm Skill mới khi quy trình đã ổn định.

## Cách tổ chức

- **Mỗi Skill một thư mục riêng**, `SKILL.md` là file bắt buộc. Không gộp nhiều Skill vào một file lớn.
- Khi cần, bổ sung vào thư mục của Skill đó: `examples.md` (ví dụ minh hoạ), `references/`, `scripts/`. Chỉ thêm khi thực sự dùng; checklist nằm trong `SKILL.md`, không tách file.
- `SKILL.md` giữ quy trình **tổng quát**. Ví dụ và chi tiết gắn với dự án (vai trò, thực thể, công cụ cụ thể) nằm trong `examples.md`; ví dụ không phải nghiệp vụ chính thức.
- `SKILL.md` là nguồn chính của quy trình; file bổ sung không được mâu thuẫn với nó.
- Việc chọn và phối hợp nhiều Skill nằm ở workflow, không nằm trong từng Skill.
- Skill chỉ nêu **cách làm**: không chép chuẩn, ngưỡng, mã lỗi hay quy tắc từ `docs/` hoặc `rules/`, và không trỏ link đi đâu; chỉ `docs/` trỏ sang Skill.

## Một Skill tốt phải có đủ

> Lưu ý: thiếu bất kỳ mục nào dưới đây thì Skill chưa đạt, chưa được chuyển sang Approved.

- Mục tiêu.
- Cổng vào (điều kiện bắt đầu; thiếu thì dừng và hỏi).
- Đầu vào.
- Quy trình thực hiện.
- Checklist.
- Việc không được phép làm.
- Tiêu chí hoàn thành.
- Báo cáo bàn giao (đầu ra).

## Skill không đồng nghĩa với Prompt

- **Prompt** là yêu cầu cụ thể trong một lần làm việc.
- **Skill** là quy trình có thể tái sử dụng nhiều lần.

| Thành phần | Ví dụ |
| --- | --- |
| Prompt | Tạo API cho chức năng X. |
| Skill | Quy trình chuẩn để phát triển API. |
| Rule | API phải kiểm tra quyền ở backend. |
| Documentation | Mô tả nghiệp vụ của chức năng X và phân quyền. |

Bốn thành phần này phối hợp với nhau để tạo ra kết quả nhất quán.

## Quy chuẩn sử dụng Skill

### Chọn và phối hợp Skill

Không yêu cầu AI đọc và dùng toàn bộ Skill trong mọi Task; chọn theo loại công việc. Một Task có thể cần nhiều Skill phối hợp: có Skill chạy song song, có Skill được kích hoạt lặp lại khi phát hiện lỗi.

Quy trình chi tiết nằm ở workflow:

- `skill-selection`: bảng "công việc → Skill" và chuỗi Skill theo loại Task (T1–T15).
- `skill-orchestration`: nhận diện Task, lập chuỗi Skill, cổng vào/ra, vòng lặp khi lỗi, bàn giao.

### Năm nguyên tắc kỹ thuật khi đưa Skill vào thực tế

1. **Skill không thay thế Rule.**
   - `authentication-rbac` hướng dẫn cách triển khai phân quyền.
   - Rule bảo mật quy định mọi API đặc quyền phải kiểm tra quyền ở backend.
2. **Skill không thay thế tài liệu nghiệp vụ.** AI phải đọc FR/BR trước khi triển khai. Không được lấy ví dụ trong Skill làm nghiệp vụ chính thức.
3. **Skill phải có phiên bản và được kiểm thử.** Khi cập nhật Skill, kiểm tra bằng một số Task thực tế để xác định AI có làm đúng hướng dẫn không.
4. **Skill có thể gọi Skill khác.** Ví dụ `backend-development` có thể yêu cầu sử dụng `unit-testing` và `security-review` khi cần. Quan hệ này được khai báo trong workflow `skill-orchestration` (mục "Skill gọi Skill khác"), không chép vào từng `SKILL.md`.
5. **Không phải Skill nào cũng được phép tự thực hiện hành động.**
   - `deployment` chỉ chuẩn bị và kiểm tra release; AI không deploy production, người có quyền thực hiện sau khi được duyệt.
   - `database-design` được tạo migration; chạy migration trên production phải tuân thủ quy trình phê duyệt.

## Nguyên tắc tạo Skill

- Chỉ tạo khi quy trình đã ổn định; không tạo skill chỉ để đặt tên cho một prompt ngắn.
- Skill mới phải chạy thử trên Task thật trước khi chuyển Approved.
- Sửa skill thuộc vùng 🔴: cần Task riêng và người duyệt.

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
