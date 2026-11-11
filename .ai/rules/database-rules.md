# Database Rules

> Trạng thái: **Draft**. Rule bắt buộc, trung lập về hệ quản trị CSDL.

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

## Migration

11. Migration chạy được trên CSDL sạch và có cách quay lui. Không quay lui được thì ghi lý do và cách khôi phục để người duyệt xác nhận.
12. Migration đã chạy ở môi trường dùng chung thì không sửa nữa; muốn sửa thì viết migration mới.
13. Thay đổi schema tương thích với phiên bản ứng dụng đang chạy (mở rộng → chuyển dữ liệu → thu gọn). Không đổi tên hoặc xoá cột/bảng trong cùng lần phát hành với code còn dùng nó.
14. Migration chạm bảng lớn phải ghi mức khoá và thời gian chạy ước tính. Chuyển dữ liệu (backfill) chia theo lô, chạy lại được, không gói trong một transaction dài; tách khỏi migration đổi cấu trúc.
15. Chạy migration trên production phải được duyệt; AI chỉ soạn migration, không tự chạy.

## Dữ liệu và transaction

16. Không sửa hoặc xoá dữ liệu production trực tiếp; xử lý dữ liệu bằng script đã duyệt.
17. Không xoá dữ liệu nghiệp vụ lịch sử khi chưa có chính sách lưu giữ được duyệt.
18. Cột chứa dữ liệu D2/D3 phải được đánh dấu trong thiết kế. Mật khẩu chỉ lưu dạng băm một chiều; dữ liệu D3 khác lưu mã hoá theo cách đã duyệt.
19. Quyền đổi cấu trúc (DDL) chỉ cấp cho tài khoản chạy migration; tài khoản ứng dụng không có quyền DDL.
20. Lỗi giữa transaction phải rollback toàn bộ, không commit dở dang. Transaction giữ ngắn; không gọi dịch vụ bên ngoài khi transaction đang mở.
21. Dữ liệu seed là dữ liệu giả hoặc đã ẩn danh.
