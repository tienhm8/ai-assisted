---
name: refactoring
description: Cải thiện cấu trúc nội bộ của code (dễ đọc, dễ bảo trì) mà giữ nguyên hành vi quan sát được; có baseline test trước và so sánh sau, không đổi schema/contract/API.
---

# Refactoring Skill

## 1. Mục tiêu

Cải thiện cấu trúc code mà không đổi hành vi nghiệp vụ đã duyệt.

## 2. Cổng vào

- Có Task refactor nêu rõ phạm vi, mức rủi ro và mức tự chủ. Thiếu thì dừng và hỏi.
- Task **lai** (refactor kèm sửa lỗi hoặc thêm tính năng): tách thành Task riêng, không làm chung.
- Refactor lớn cần plan được duyệt trước khi sửa; ngưỡng "lớn" do plan chốt.

## 3. Đầu vào

Task, mã nguồn và bộ test hiện có, thiết kế/ranh giới module đã duyệt, chuẩn code của dự án, nợ kỹ thuật đã biết.

## 4. Quy trình

1. **Hiểu hành vi hiện tại:** giao diện công khai, quy tắc nghiệp vụ, phụ thuộc, vùng được test.
2. **Baseline:** chạy test liên quan trước (dùng unit-testing để bổ sung test mô tả hành vi cho chỗ chưa có), ghi lại lỗi có sẵn. Không đổ lỗi có sẵn cho refactor.
3. **Xác định mục tiêu:** chỉ những mùi code ảnh hưởng thực sự tới Task (lặp, hàm/lớp quá lớn, điều kiện rối, phụ thuộc chặt hoặc vòng, đặt tên khó hiểu, khó test).
4. **Kiểm tra ràng buộc:** refactor **không đổi schema, contract hay API**; cần đổi thì chuyển database-design hoặc api-development và cần duyệt (ADR nếu thuộc diện). Cần đổi ranh giới module hay kiến trúc đã duyệt thì **dừng xin duyệt**.
5. **Plan** (refactor lớn): vấn đề, cấu trúc mong muốn, file, rủi ro, test; chờ duyệt.
6. **Refactor từng bước nhỏ**, chạy test sau mỗi bước; tối đa 3 vòng sửa–chạy khi test đỏ, quá thì dừng và báo.
7. **So sánh với baseline:** đầu vào/ra, lỗi, quyền truy cập, thứ tự hiệu ứng phụ không đổi. Không khẳng định cải thiện hiệu năng khi chưa đo.
8. **Cập nhật tài liệu** nếu cấu trúc đã ghi ở tài liệu thiết kế bị đổi (skill documentation).
9. **Bàn giao** cho code-review ở phiên khác.

## 5. Checklist

- [ ] Task không lai; phạm vi rõ.
- [ ] Baseline test đã chạy và ghi lại trước khi sửa.
- [ ] Thay đổi nhỏ, tăng dần; không đổi schema/contract/API.
- [ ] Test sau refactor đạt và khớp baseline; test không bị xoá hay làm yếu.
- [ ] Không thêm tính năng; quyền truy cập không đổi.

## 6. Việc không được làm

- Không thêm tính năng, không đổi hành vi nghiệp vụ, không gộp sửa lỗi vào refactor.
- Không đổi schema, contract, API, ranh giới module khi chưa được duyệt.
- Không viết lại quy mô lớn khi chưa có plan được duyệt.
- Không xoá hay làm yếu test cho dễ qua.
- Không tối ưu hiệu năng khi thiếu số đo.
- Không tự duyệt refactor của mình.

## 7. Tiêu chí hoàn thành (DoD)

- Mục tiêu refactor đạt, hành vi giữ nguyên (so với baseline).
- Cổng kiểm tra của dự án đạt, có bằng chứng.
- Đã bàn giao cho code-review ở phiên khác, không tự duyệt.
- Nợ kỹ thuật còn lại được ghi.

## 8. Báo cáo bàn giao

Điền DELIVERY-REPORT-TEMPLATE, nêu thêm: vấn đề đã xử lý, file đã sửa, kết quả baseline so với sau refactor, đánh giá giữ nguyên hành vi, cải thiện đạt được, nợ kỹ thuật còn lại.
