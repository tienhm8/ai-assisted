# PLAN: <KEY>-<N> — <Tên ngắn>

> AI soạn; người duyệt theo điều kiện của quy trình thực hiện Task. Mục "Kết quả" điền sau khi xong.

| Mục | Giá trị |
| --- | --- |
| Trạng thái | Draft / Approved / Done |
| Loại Task | T1–T15 |
| Mức rủi ro · Mức tự chủ | lấy từ Task |
| Model · Effort phiên thực thi | |

## 1. Mục tiêu và phạm vi
- Làm:
- Không làm:

## 2. Yêu cầu và ngữ cảnh đã nạp
FR, BR, AC, ADR, câu hỏi mở.
Điểm áp dụng từ tài liệu thiết kế, kỹ thuật: tài liệu, § và tên mục → điều áp dụng cho Task (ví dụ: error-handling §5.2 Ánh xạ HTTP status → lỗi hạn mức trả 422).

## 3. Rule và chuỗi Skill
- Rule đã nạp (Rule theo điều kiện ghi kèm lý do):
- Chuỗi Skill theo thứ tự; Skill bỏ hoặc thêm so với mặc định kèm lý do:
- Nạp bổ sung trong khi làm (tài liệu, § và tên mục, kèm lý do plan thiếu):

## 4. Thiết kế và file dự kiến thay đổi

## 5. Kế hoạch kiểm thử
Mỗi AC ứng với test nào, chạy bằng lệnh nào.

## 6. Rủi ro và điểm cần người quyết
Điểm cần người quyết ghi mã `OQ-<NN>` kèm bản tóm tắt đủ để quyết theo `project-rules` 21 (vấn đề, mỗi phương án một dòng được/mất, đề xuất, nếu chưa quyết); chi tiết và lịch sử ở [open-questions](../../docs/00-project-overview/open-questions.md).

## 7. Kết quả (điền sau khi xong)
Đầu ra của từng Skill, lệch kế hoạch ở đâu, bằng chứng test.
