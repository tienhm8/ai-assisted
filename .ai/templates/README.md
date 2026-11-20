# templates

Mẫu báo cáo công việc của AI, chỉ giữ cấu trúc (trường, cột, mã định danh); giá trị cụ thể do dự án điền hoặc lấy từ Task. Sửa `.ai/templates/` thuộc vùng 🔴.

| Mẫu | Dùng khi | AI soạn · Người duyệt |
| --- | --- | --- |
| PLAN-TEMPLATE | Lập một Plan (kế hoạch thực hiện, gồm nhiều Task; có Nguồn và Goals tuỳ chọn) | AI (Orchestrator) · Tech Lead |
| TASK-MANIFEST-TEMPLATE | Khai báo một Task: làm gì, chạy bằng cấu hình nào, kiểm thế nào | AI (Orchestrator) · Tech Lead, duyệt cùng Plan |
| RUNS-TEMPLATE | Ghi từng lần chạy Task, nâng mức, chi phí | AI (Orchestrator) · không cần duyệt |
| BUG-TEMPLATE | Giao việc sửa lỗi | Người báo · Tech Lead |
| DELIVERY-REPORT-TEMPLATE | Bàn giao một Task | AI · Reviewer |
| TEST-REPORT-TEMPLATE | Báo cáo kiểm thử | AI · người xác nhận độc lập |
| RELEASE-REPORT-TEMPLATE | Báo cáo phát hành | AI · Owner |
| CONFIRMATION-PACK-TEMPLATE | Gói gửi khách hàng chốt phạm vi, quy trình, màn hình (wireframe/mockup), quy tắc, câu hỏi; xuất HTML/PDF bằng `.ai/scripts/export-pack.py` | AI · BA (Đầu mối) rà, khách hàng xác nhận |
| PR-TEMPLATE | Mô tả Pull Request trước khi yêu cầu review | Người viết PR (người hoặc AI) · Reviewer |

Kết quả review code ghi theo mục "Report" của skill code-review; không có mẫu riêng. PR thiếu mục bắt buộc của PR-TEMPLATE thì bị trả về trước khi review.
