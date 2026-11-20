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
| caching | Thiết kế, cài đặt cache dữ liệu L1/L2 |
| task-planning | Từ Nguồn (Goal, Epic, User Story, yêu cầu độc lập) chia thành Plan, Plan thành Task kèm Task Manifest |
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

- Mỗi Skill một thư mục, `SKILL.md` là file bắt buộc. Khi cần thì thêm `references/` (chi tiết theo chủ đề hoặc theo công nghệ), `examples.md` (ví dụ minh hoạ, không phải nghiệp vụ chính thức; không nạp khi làm Task trừ khi Task yêu cầu, `SKILL.md` không cần nhắc lại), `scripts/`.
- `SKILL.md` giữ quy trình tổng quát, trung lập công nghệ. Chi tiết dài hoặc chỉ dùng ở một bước thì đưa vào `references/`, và `SKILL.md` ghi rõ bước nào nạp file nào.
- Chọn và phối hợp Skill nằm ở workflow (`task-types`, `task-execution`), không nằm trong từng Skill.

## Cấu trúc một SKILL.md

| Mục (tên trong file) | Nội dung |
| --- | --- |
| Frontmatter `name`, `description` | Skill làm gì và dùng khi nào; đủ để chọn Skill mà không cần đọc phần thân |
| Mở đầu | Một đến hai câu về mục tiêu |
| Cổng vào (`Entry gate`) | Điều kiện bắt đầu, thiếu thì dừng; tài liệu cần đọc |
| Quy trình (`Procedure`) | Các bước theo thứ tự |
| Giới hạn (`Limits`, nếu có) | Chỉ điều riêng của Skill này |
| Hoàn thành khi (`Done when`) | Kết quả kiểm chứng được |
| Báo cáo (`Report`) | Chỉ phần riêng của Skill; phần chung theo template |

Thiếu Cổng vào, Quy trình, Hoàn thành khi hoặc Báo cáo thì Skill chưa được chuyển Approved.

Nội dung `SKILL.md` và `references/` viết bằng tiếng Anh để tiết kiệm token (`project-rules` 22); tên mục `docs/` và template được dẫn chiếu thì giữ nguyên tiếng Việt.

## Viết Skill cho gọn

Mỗi dòng trong Skill được nạp lại ở mọi Task dùng nó, nên:

- **Không nhắc lại Rule.** Rule đã được nạp cùng Task. Skill chỉ ghi giới hạn mà Rule chưa có.
- **Không nhắc lại Quy trình** dưới dạng checklist. "Hoàn thành khi" chỉ ghi kết quả kiểm chứng được.
- **Không chép template.** Báo cáo chỉ nêu phần Skill này thêm vào.
- **Không ghi kiến thức chung model đã biết.** Chỉ ghi quy ước đã chốt, lỗi AI hay mắc, và điểm dễ sót.
- **Không chép chuẩn, ngưỡng, mã lỗi** từ `docs/`; nêu tên tài liệu cần đọc ở Cổng vào.
- **Skill chạy sau plan** (code, test, refactor): nguồn chính là Task Manifest của Run cùng các điểm ở PLAN mà manifest trỏ tới. Cổng vào ghi nguồn chính đó, rồi liệt kê mục `docs/` được tra khi manifest thiếu, mỗi mục kèm § và tên mục (tên giữ dẫn chiếu đúng khi đánh số lại), không nêu cả file. Đổi tiêu đề mục trong `docs/` thì rà dẫn chiếu trong Skill.
- Một `SKILL.md` vượt khoảng 150 dòng thì tách phần chi tiết sang `references/`.

## Khi đưa Skill vào dùng

- Skill không thay Rule và không thay tài liệu nghiệp vụ; ví dụ trong Skill không phải nghiệp vụ chính thức.
- Skill mới hoặc Skill vừa sửa phải chạy thử trên Task thật trước khi chuyển Approved.
- Chỉ tạo Skill khi quy trình đã ổn định; không tạo Skill để đặt tên cho một prompt ngắn.
- Sửa Skill cần Task riêng và người duyệt.

## Tiếp nhận Skill bên ngoài

Skill cộng đồng và guideline do package sinh ra chỉ là tài liệu tham khảo, không cài thẳng. Quy trình tiếp nhận: [.ai/guide/external-skills.md](../guide/external-skills.md).
