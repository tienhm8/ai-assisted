---
name: refactoring
description: Cải thiện cấu trúc nội bộ của code (dễ đọc, dễ bảo trì) mà giữ nguyên hành vi quan sát được; có baseline test trước và so sánh sau, không đổi schema/contract/API.
---

# Refactoring Skill

Cải thiện cấu trúc code mà giữ nguyên hành vi quan sát được.

## Cổng vào

- Task refactor nêu rõ phạm vi. Thiếu thì dừng và hỏi.
- Task kèm sửa lỗi hoặc thêm tính năng: tách thành Task riêng.
- Refactor lớn cần plan được duyệt trước khi sửa.

Đọc: Task, mã nguồn và test hiện có, thiết kế và ranh giới module, coding-standards.

## Quy trình

1. **Hiểu hành vi hiện tại:** giao diện công khai, quy tắc nghiệp vụ, phụ thuộc, vùng đã có test.
2. **Baseline:** chạy test liên quan và ghi lại lỗi có sẵn. Chỗ chưa có test thì bổ sung test mô tả hành vi hiện tại bằng `unit-testing`.
3. **Chọn mục tiêu:** chỉ những vấn đề ảnh hưởng tới Task (lặp, hàm hoặc lớp quá lớn, điều kiện rối, phụ thuộc chặt hoặc vòng, tên khó hiểu, khó test).
4. **Kiểm ràng buộc:** cần đổi schema, contract, API, ranh giới module thì dừng xin duyệt và chuyển Skill tương ứng.
5. **Refactor từng bước nhỏ**, chạy test sau mỗi bước.
6. **So với baseline:** đầu vào/ra, lỗi, quyền truy cập, thứ tự side effect không đổi.

## Giới hạn

- Không thêm tính năng, không đổi hành vi, không gộp sửa lỗi.
- Không khẳng định cải thiện hiệu năng khi chưa đo.

## Hoàn thành khi

- Test sau refactor khớp baseline; không test nào bị xoá hay làm yếu.
- Cổng kiểm tra của dự án đạt.

## Báo cáo

Ghi vào báo cáo bàn giao của Task: vấn đề đã xử lý, kết quả baseline so với sau refactor, nợ kỹ thuật còn lại.
