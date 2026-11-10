# workflows

Quy trình nhiều bước gắn với vòng đời và các điểm duyệt của người (điều kiện duyệt và người quyết ghi ngay trong tài liệu liên quan). Mỗi workflow nêu bước, người duyệt, bằng chứng cần có ở mỗi cổng.

| File | Nội dung | Trạng thái |
| --- | --- | --- |
| [task-execution.md](task-execution.md) | Quy trình 10 bước AI thực hiện một Task (bắt buộc) | Draft |
| [skill-orchestration.md](skill-orchestration.md) | Quy trình điều phối: nhận diện Task, chọn Skill, phối hợp, kiểm tra điều kiện đầu ra, bàn giao | Draft |
| [skill-selection.md](skill-selection.md) | Bảng chọn Skill theo công việc và chuỗi Skill theo loại Task (T1–T15) | Draft |
| [release-workflow.md](release-workflow.md) | Chuẩn bị phát hành; người quyết định và deploy (Owner quyết) | Draft |

Workflow theo loại việc (feature, bug fix, refactor, đổi yêu cầu, đổi kiến trúc, sự cố bảo mật, phát hành) hiện được biểu diễn dưới dạng **chuỗi Skill** trong [skill-selection.md](skill-selection.md). Chỉ tách thành file riêng khi một loại cần thêm bước, người duyệt hoặc bằng chứng mà chuỗi Skill chưa diễn tả được.

Quy ước: workflow chỉ điều phối, không chép lại nội dung Skill hay Rule. Sửa workflow thuộc vùng 🔴.
