# DELIVERY REPORT: <KEY>-<N>

> AI điền khi bàn giao Task. Là nguồn duy nhất của báo cáo bàn giao; các báo cáo khác chỉ tóm tắt rồi trỏ về đây. Chi tiết kiểm thử nằm ở báo cáo kiểm thử.

## 1. Kết quả
Task đã làm gì, đạt tiêu chí nghiệm thu nào.

## 2. Thay đổi
Gộp từ **mọi** worktree, nhánh và phiên của Task (không chỉ phiên hiện tại). Lấy từ `git diff <nhánh gốc>...<nhánh Task>` của từng nguồn.

**Nguồn đã gộp**

| Worktree / nhánh | Phiên | Commit (hash ngắn) |
| --- | --- | --- |
| | | |

**Tóm tắt triển khai:** 1–3 câu, Task đã thay đổi hành vi gì.

**Thay đổi theo nghiệp vụ** (gom theo nghiệp vụ, không theo thứ tự file; dòng thêm/sửa tính trên file mới, dòng xoá tính trên file cũ)

| # | Nghiệp vụ (FR/BR/AC) | File:dòng | Loại | Nội dung thay đổi | Đề xuất tốt hơn (nếu có) |
| --- | --- | --- | --- | --- | --- |
| 1 | | `path/file.ext:L10-L25` | Thêm / Sửa / Xoá | | |

**Điểm reviewer nên xem kỹ:** đoạn rủi ro cao, logic khó, chỗ lệch plan.

## 3. Kiểm thử
Tóm tắt và mã báo cáo kiểm thử. Phân biệt pass / fail / skipped / not-run, kèm lệnh và kết quả thật.
**Chưa kiểm tra:** AC, tầng test hoặc trường hợp chưa kiểm, mỗi mục kèm lý do (tóm tắt từ mục "Chưa kiểm chứng" của báo cáo kiểm thử); không có thì ghi "không".

## 4. Giả định, quyết định, câu hỏi mở
- Giả định:
- Quyết định đã đưa ra:
- Câu hỏi mở (`OQ-<NN>`) chưa giải quyết, mỗi mã kèm bản tóm tắt đủ để quyết theo `project-rules` 21 (vấn đề, mỗi phương án một dòng được/mất, đề xuất, nếu chưa quyết); chi tiết và lịch sử ở open-questions:

## 5. Hành động cần người thực hiện
(duyệt, merge, deploy, cấp quyền...). Chỉ việc người phải làm; câu hỏi cần quyết ghi ở mục 4 dưới dạng `OQ-<NN>`.

## 6. Quy trình đã dùng
- Chuỗi Skill đã dùng, Skill bỏ qua và lý do:
- Tài liệu và phiên bản đã đọc:

## 7. Hạn chế và rủi ro còn lại

## 8. Số đo
Số thật, không ước lượng; không có thì ghi "không đo" và lý do. Là nguồn cho [ai-kpi](../../docs/04-project-management/ai-kpi.md).

| Chỉ số | Giá trị | Nguồn |
| --- | --- | --- |
| Giờ người (soạn Task, trả lời câu hỏi, duyệt, review, sửa tay) | | |
| Thời gian AI chạy | | |
| Chi phí AI (token hoặc tiền) | | Công cụ AI |
| Số vòng sửa (test fail, review trả về) | | |
| Số lần người sửa lại bản AI soạn; số lần AI bịa hoặc sai phải quay lại | | |
