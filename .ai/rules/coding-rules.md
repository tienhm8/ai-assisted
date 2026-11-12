# Coding Rules

> Trạng thái: **Approved**. Rule bắt buộc, trung lập về ngôn ngữ.

1. Theo đúng ngôn ngữ, phiên bản, naming và công cụ lint/kiểm tra kiểu đã chốt cho dự án. Mục chưa chốt: dừng và hỏi, không tự chọn.
2. Cơ chế nới lỏng kiểm tra (bỏ qua kiểu, tắt lint...) chỉ dùng khi có lý do ghi tại chỗ và reviewer chấp nhận.
3. Không lặp logic nghiệp vụ; chỉ tách phần dùng chung khi đã lặp lại thật sự.
4. Không nuốt lỗi (bắt lỗi rồi bỏ qua); mọi lỗi phải được xử lý, ghi log hoặc ném tiếp.
5. Phân loại lỗi và dùng mã lỗi chung của dự án; phản hồi lỗi không lộ stack trace, câu truy vấn hay đường dẫn nội bộ.
6. Mọi lời gọi ra ngoài (CSDL, API, hàng đợi) có timeout; chỉ retry lỗi tạm thời và thao tác idempotent.
7. Log kèm correlation ID.
8. Giải phóng tài nguyên (kết nối, file, lock) kể cả khi lỗi.
9. Kiểm tra dữ liệu đầu vào tại biên hệ thống.
10. Không để lại import thừa, code chết, hoặc code ngoài nhu cầu của Task.
