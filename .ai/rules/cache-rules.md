# Cache Rules

> Trạng thái: **Approved**. Rule bắt buộc khi thay đổi có thêm, sửa hoặc đọc cache.

1. Chỉ thêm cache khi truy vấn đã tối ưu mà vẫn không đạt yêu cầu phi chức năng, có số liệu đo. CSDL là nguồn sự thật: xoá toàn bộ cache thì hệ thống vẫn đúng, chỉ chậm hơn.
2. Không cache số dư và giao dịch tiền, tồn kho hoặc trạng thái đang tranh chấp, lock nghiệp vụ, secret, token, mật khẩu. Lock chống dồn tải của cache không dùng làm khoá nghiệp vụ.
3. Ghi CSDL xong thì xoá key, không cập nhật key. Việc xoá đặt ở tầng truy cập dữ liệu của module sở hữu dữ liệu; module khác không xoá hộ.
4. Dữ liệu phụ thuộc tenant, người xem, quyền hoặc ngôn ngữ thì key phải chứa yếu tố đó. Mọi key chứa dữ liệu có TTL kèm jitter; không cache kết quả lỗi.
5. Cache lỗi không làm request lỗi: bỏ qua cache, đọc nguồn, ghi log. Timeout gọi cache ngắn hơn truy vấn gốc; không dùng lệnh chặn toàn server như `KEYS`.
6. Production có cache thì có job warm-up. Job chỉ chạy trên một instance, nạp tập key chọn lọc theo lô có giới hạn tải CSDL, dùng chung hàm nạp với luồng đọc, không ghi đè dữ liệu mới hơn; job lỗi không chặn khởi động.
