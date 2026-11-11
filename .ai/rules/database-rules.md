# Database Rules

> Trạng thái: **Draft**. Rule bắt buộc, trung lập về hệ quản trị CSDL. Với CSDL tài liệu, "bảng" hiểu là collection, "cột" là field; mục cuối là rule riêng cho loại CSDL này.

## Thiết kế

1. Chỉ thay đổi schema theo thiết kế Approved; mọi thay đổi đi qua migration trong mã nguồn, không sửa thủ công.
2. Mỗi bảng, cột, ràng buộc và index truy ra được một yêu cầu, quy tắc nghiệp vụ hoặc mẫu truy cập đã ghi; không tạo bảng, cột "để dành".
3. Đặt tên, kiểu dữ liệu chuẩn, chiến lược khoá chính theo quy ước CSDL đã chốt của dự án. Mục chưa chốt: đề xuất và chờ duyệt, không tự áp.
4. Mọi bảng có khoá chính. Quan hệ khai báo bằng khoá ngoại với hành vi xoá/cập nhật chọn tường minh; không dùng khoá ngoại (khác module, partition, shard) thì ghi lý do và cách giữ toàn vẹn.
5. Bất biến nghiệp vụ khai báo ngay ở CSDL bằng NOT NULL, UNIQUE, CHECK, khoá ngoại; không chỉ dựa vào kiểm tra ở ứng dụng.
6. Tiền và số lượng cần chính xác dùng kiểu số chính xác, không dùng số thực dấu phẩy động. Thời điểm lưu kèm múi giờ hoặc chuẩn hoá UTC. Văn bản dùng bảng mã hỗ trợ đủ Unicode.
7. Không gộp nhiều giá trị vào một cột để né việc tạo bảng hoặc quan hệ. Dữ liệu bán cấu trúc chỉ dành cho thuộc tính không ràng buộc toàn vẹn và không dùng làm điều kiện truy vấn chính.

## Hiệu năng và mở rộng

8. Mỗi index phục vụ ít nhất một truy vấn đã ghi. Thêm hoặc bỏ index trên bảng lớn phải kèm kế hoạch thực thi (EXPLAIN) trước và sau.
9. Truy vấn trả danh sách phải có giới hạn số dòng; không tải toàn bộ bảng khi không giới hạn.
10. Phi chuẩn hoá, partition, sharding, tách CSDL hay đổi hệ quản trị chỉ làm khi có số liệu đo hoặc yêu cầu phi chức năng, và phải có ADR được duyệt.
11. Truy vấn của ứng dụng chỉ chọn cột cần dùng, không `SELECT *`; không truy vấn lặp theo từng dòng kết quả (N+1).
12. Điều kiện lọc và join của truy vấn quan trọng phải dùng được index: không bọc hàm hoặc phép tính quanh cột được index, không `LIKE` bắt đầu bằng ký tự đại diện trên B-Tree, tham số cùng kiểu và collation với cột.
13. Ứng dụng kết nối CSDL qua connection pool có giới hạn; tổng kết nối tối đa của mọi tiến trình phải nhỏ hơn `max_connections` của máy chủ.
14. Không đưa logic nghiệp vụ vào stored procedure, function hay trigger chỉ để tăng tốc khi chưa có số liệu đo và ADR được duyệt.

## Migration

15. Migration chạy được trên CSDL sạch và có cách quay lui. Không quay lui được thì ghi lý do và cách khôi phục để người duyệt xác nhận.
16. Migration đã chạy ở môi trường dùng chung thì không sửa nữa; muốn sửa thì viết migration mới.
17. Thay đổi schema tương thích với phiên bản ứng dụng đang chạy (mở rộng → chuyển dữ liệu → thu gọn). Không đổi tên hoặc xoá cột/bảng trong cùng lần phát hành với code còn dùng nó.
18. Migration chạm bảng lớn phải ghi mức khoá và thời gian chạy ước tính. Chuyển dữ liệu (backfill) chia theo lô, chạy lại được, không gói trong một transaction dài; tách khỏi migration đổi cấu trúc.
19. Chạy migration trên production phải được duyệt; AI chỉ soạn migration, không tự chạy.

## Dữ liệu và transaction

20. Không sửa hoặc xoá dữ liệu production trực tiếp; xử lý dữ liệu bằng script đã duyệt.
21. Không xoá dữ liệu nghiệp vụ lịch sử khi chưa có chính sách lưu giữ được duyệt.
22. Cột chứa dữ liệu D2/D3 phải được đánh dấu trong thiết kế. Mật khẩu chỉ lưu dạng băm một chiều; dữ liệu D3 khác lưu mã hoá theo cách đã duyệt.
23. Quyền đổi cấu trúc (DDL) chỉ cấp cho tài khoản chạy migration; tài khoản ứng dụng không có quyền DDL.
24. Lỗi giữa transaction phải rollback toàn bộ, không commit dở dang. Transaction giữ ngắn; không gọi dịch vụ bên ngoài khi transaction đang mở.
25. Dữ liệu seed là dữ liệu giả hoặc đã ẩn danh.

## CSDL tài liệu (MongoDB, NoSQL)

26. Mô hình document (nhúng hay tham chiếu) suy ra từ mẫu truy cập đã ghi; không có mảng nhúng tăng không giới hạn.
27. Mọi collection có schema validation khai báo bằng migration; validator, index và chuyển dữ liệu đều đi qua migration trong mã nguồn.
28. Bất biến không giữ được bằng ràng buộc của CSDL (tham chiếu giữa document, quy tắc trên nhiều document) phải ghi cách giữ: gom vào một document, transaction đa document, hoặc kiểm ở ứng dụng kèm đối soát.
29. Không đưa object từ đầu vào vào điều kiện truy vấn nguyên trạng; ép kiểu từng trường, từ chối khoá bắt đầu bằng `$`; không chạy JavaScript phía máy chủ với đầu vào người dùng.
30. Ghi dữ liệu nghiệp vụ với mức xác nhận đa số bản sao (write concern `majority`); hạ mức chỉ khi có ADR được duyệt.
