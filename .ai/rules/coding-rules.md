# Coding Rules

> Trạng thái: **Approved**. Rule bắt buộc, trung lập về ngôn ngữ.

## Nguyên tắc thiết kế

1. **Clean Code.** Tên nói rõ ý định. Hàm ngắn, làm một việc, không có side effect ẩn. Comment chỉ giải thích lý do, không lặp lại điều code đã nói. Không để lại import thừa hay code chết.
2. **SOLID.**
   - Single Responsibility: mỗi hàm, lớp, file một trách nhiệm; phải thêm việc thứ hai thì tách.
   - Open/Closed: thêm biến thể hành vi bằng cách mở rộng qua điểm mở rộng đã có, không sửa lan sang code đang chạy đúng.
   - Liskov Substitution: kiểu con thay được kiểu cha mà bên gọi không phải biết hay kiểm tra kiểu cụ thể.
   - Interface Segregation: interface nhỏ, theo nhu cầu của bên dùng; không buộc bên dùng phụ thuộc vào method nó không gọi.
   - Dependency Inversion: phụ thuộc vào abstraction và được truyền vào qua tham số hoặc interface; không tự khởi tạo phụ thuộc bên trong, không dùng trạng thái toàn cục.
3. **DRY.** Logic nghiệp vụ chỉ có một nơi định nghĩa. Trước khi viết mới, tìm và dùng lại hàm, component, tiện ích sẵn có. Chỉ tách phần dùng chung khi đã lặp lại thật sự.
4. **KISS.** Chọn cách đơn giản nhất đáp ứng AC; viết theo cách code xung quanh đang làm.
5. **YAGNI.** Không viết code, tầng trừu tượng, tham số cấu hình hay điểm mở rộng cho nhu cầu chưa có trong Task.
6. **Separation of Concerns.** Không trộn giao diện, nghiệp vụ và truy cập dữ liệu trong cùng một đơn vị code.

Khi hai nguyên tắc kéo ngược nhau, KISS và YAGNI thắng: không thêm abstraction để đạt SOLID hay DRY khi Task chưa cần.

## Quy ước và xử lý lỗi

7. Theo đúng ngôn ngữ, phiên bản, naming và công cụ lint/kiểm tra kiểu đã chốt cho dự án. Mục chưa chốt: dừng và hỏi, không tự chọn.
8. Cơ chế nới lỏng kiểm tra (bỏ qua kiểu, tắt lint...) chỉ dùng khi có lý do ghi tại chỗ và reviewer chấp nhận.
9. Không nuốt lỗi (bắt lỗi rồi bỏ qua); mọi lỗi phải được xử lý, ghi log hoặc ném tiếp.
10. Phân loại lỗi và dùng mã lỗi chung của dự án; phản hồi lỗi không lộ stack trace, câu truy vấn hay đường dẫn nội bộ.
11. Mọi lời gọi ra ngoài (CSDL, API, hàng đợi) có timeout; chỉ retry lỗi tạm thời và thao tác idempotent.
12. Log kèm correlation ID.
13. Giải phóng tài nguyên (kết nối, file, lock) kể cả khi lỗi.
14. Kiểm tra dữ liệu đầu vào tại biên hệ thống.
15. File mã nguồn tối đa 500 dòng, không tính file sinh tự động; vượt thì tách theo trách nhiệm. Áp cho file mới và file bị sửa trong Task; file cũ đang vượt chỉ tách khi Task chạm tới.
