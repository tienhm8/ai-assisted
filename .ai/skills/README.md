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
