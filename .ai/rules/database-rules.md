# Database Rules

> Trạng thái: **Draft**. Rule bắt buộc, trung lập về hệ quản trị CSDL.

1. Chỉ thay đổi schema theo thiết kế Approved; mọi thay đổi đi qua migration trong mã nguồn, không sửa thủ công.
2. Migration chạy được trên CSDL sạch và có cách quay lui. Không quay lui được thì ghi lý do và cách khôi phục để người duyệt xác nhận.
3. Chạy migration trên production phải được duyệt; AI chỉ soạn migration, không tự chạy và không truy cập CSDL production.
4. Không sửa hoặc xoá dữ liệu production trực tiếp; xử lý dữ liệu bằng script đã duyệt.
5. Khai báo ràng buộc (khoá ngoại, unique, kiểm tra) rõ ràng; thêm index khi có truy vấn cần.
6. Không xoá dữ liệu nghiệp vụ lịch sử khi chưa có chính sách lưu giữ được duyệt.
7. Lỗi giữa transaction phải rollback toàn bộ, không commit dở dang.
8. Dữ liệu seed và dữ liệu test là dữ liệu giả hoặc đã ẩn danh.
