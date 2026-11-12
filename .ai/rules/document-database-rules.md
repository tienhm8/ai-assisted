# Document Database Rules

> Trạng thái: **Approved**. Rule bắt buộc khi dự án dùng CSDL tài liệu (MongoDB, NoSQL); áp dụng cùng Database Rules. "Bảng" hiểu là collection, "cột" là field.

1. Mô hình document (nhúng hay tham chiếu) suy ra từ mẫu truy cập đã ghi; không có mảng nhúng tăng không giới hạn.
2. Mọi collection có schema validation khai báo bằng migration; validator, index và chuyển dữ liệu đều đi qua migration trong mã nguồn.
3. Bất biến không giữ được bằng ràng buộc của CSDL (tham chiếu giữa document, quy tắc trên nhiều document) phải ghi cách giữ: gom vào một document, transaction đa document, hoặc kiểm ở ứng dụng kèm đối soát.
4. Không đưa object từ đầu vào vào điều kiện truy vấn nguyên trạng; ép kiểu từng trường, từ chối khoá bắt đầu bằng `$`; không chạy JavaScript phía máy chủ với đầu vào người dùng.
5. Ghi dữ liệu nghiệp vụ với mức xác nhận đa số bản sao (write concern `majority`); hạ mức chỉ khi có ADR được duyệt.
