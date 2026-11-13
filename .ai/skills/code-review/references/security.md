# Code Review – Checklist bảo mật (ưu tiên 6)

## Ưu tiên 6: Bảo mật (theo OWASP Top 10)

Kiểm nhanh các lỗi hay gặp nhìn thấy được trong diff:

- Thiếu kiểm quyền ở backend, đặc biệt quyền trên từng bản ghi (lấy theo ID mà không kiểm quyền sở hữu: IDOR/BOLA).
- Gán toàn bộ input vào đối tượng (mass assignment/over-posting) thay vì chỉ nhận trường đã kiểm.
- Injection: nối chuỗi vào truy vấn, lệnh hệ thống, template, biểu thức đường dẫn.
- Đầu ra không được mã hoá/escape theo ngữ cảnh (XSS).
- Trả về hoặc ghi log trường nhạy cảm, secret, token, dữ liệu D3.
- Upload: không kiểm loại, kích thước, nội dung, nơi lưu.
- Gọi URL do người dùng cung cấp (SSRF); đường dẫn file từ input (path traversal).
- Thiếu giới hạn tần suất ở điểm nhạy cảm (đăng nhập, OTP, đặt lại mật khẩu).
- Dependency mới có lỗ hổng đã biết hoặc chưa ghi lý do.

Diff chạm xác thực, phân quyền, dữ liệu nhạy cảm hoặc input từ bên ngoài thì kích hoạt `security-review`; không tự làm thay trong skill này.
