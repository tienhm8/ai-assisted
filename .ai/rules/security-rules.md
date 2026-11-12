# Security Rules

> Trạng thái: **Approved**. Rule bắt buộc. Không hạ được; cần ngoại lệ thì phải có lý do, biện pháp bù, người duyệt và thời hạn.

1. Phân quyền kiểm tra ở phía server, không tin quyền do client gửi; mặc định từ chối khi chưa khai báo quyền.
2. Kiểm tra quyền trên chính bản ghi được truy cập, không chỉ kiểm tra vai trò.
3. Dùng truy vấn tham số hoá và mã hoá đầu ra theo ngữ cảnh; không nối chuỗi từ đầu vào vào câu truy vấn.
4. Không hardcode secret; secret lấy từ nơi lưu trữ được duyệt. Secret đã lộ coi như bị xâm phạm: báo ngay.
5. Áp dụng đặc quyền tối thiểu cho người dùng, dịch vụ và tài khoản CSDL.
6. Ghi log sự kiện bảo mật: đăng nhập thành công/thất bại, đổi quyền, truy cập bị từ chối, đổi cấu hình bảo mật.
7. Đổi dependency thì chạy quét lỗ hổng và kiểm tra license; mọi commit chạy quét secret.
8. Không tắt hay nới kiểm tra bảo mật (lint, scan, xác thực) để test qua.
9. Thay đổi phân quyền, tiền, dữ liệu cá nhân hoặc migration cần Tech Lead và Security duyệt. AI không tự quản lý secret.
10. Công cụ cấp cho AI (MCP server, plugin) không kết nối production hoặc dữ liệu D2/D3.
