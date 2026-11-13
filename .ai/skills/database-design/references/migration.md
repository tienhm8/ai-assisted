# Database Design – Migration

> Tài liệu tham khảo của Skill `database-design`, dùng ở bước 9–10. Công cụ migration, thư mục, cách đặt tên file lấy theo dự án (database-design §7); file này nêu cách viết migration an toàn, không phụ thuộc công cụ. Cú pháp riêng của hệ quản trị tra ở `postgresql.md` hoặc `mysql-mariadb.md`.

## 1. Cấu trúc một migration

- Tên mô tả hành động: `<timestamp>_create_order`, `<timestamp>_add_order_paid_at`, `<timestamp>_backfill_order_paid_at`.
- Một migration một mục đích; đổi cấu trúc và chuyển dữ liệu tách migration riêng.
- Có phần lên và phần quay lui. Quay lui làm mất dữ liệu (xoá cột đã có dữ liệu) thì ghi rõ trong migration và trong báo cáo.
- Đặt tên ràng buộc, index tường minh để quay lui và migration sau tham chiếu được.
- Không phụ thuộc code ứng dụng (model, ORM) có thể đổi sau này; migration dữ liệu dùng SQL hoặc truy vấn độc lập.
- Hệ có DDL trong transaction: gói migration trong transaction (trừ lệnh không chạy được trong transaction). Hệ DDL tự commit: mỗi migration chỉ một DDL hoặc viết sao cho chạy lại được (`IF NOT EXISTS`, kiểm tra trước).

## 2. Mở rộng → chuyển dữ liệu → thu gọn (expand / migrate / contract)

Thay đổi trên bảng đang dùng chia qua nhiều lần phát hành để phiên bản cũ và mới của ứng dụng cùng chạy được.

| Thay đổi | Lần phát hành 1 (mở rộng) | Lần 2 (chuyển) | Lần 3 (thu gọn) |
| --- | --- | --- | --- |
| Thêm cột bắt buộc | Thêm cột cho phép NULL (hoặc có DEFAULT) | Code ghi cột mới; backfill theo lô | Đặt NOT NULL (cách không khoá lâu: §8 file hệ quản trị) |
| Đổi tên cột | Thêm cột mới; code ghi cả hai | Backfill; code đọc cột mới | Bỏ cột cũ |
| Đổi kiểu cột | Thêm cột kiểu mới; ghi cả hai | Backfill; chuyển đọc | Bỏ cột cũ |
| Tách bảng | Tạo bảng mới; ghi cả hai | Backfill; chuyển đọc | Bỏ cột ở bảng cũ |
| Xoá cột/bảng | Code ngừng dùng | — | Xoá (sau ít nhất một chu kỳ phát hành) |

## 3. Thao tác và mức khoá

Trước khi viết migration trên bảng có dữ liệu, tra mức khoá và cách làm không khoá của từng thao tác ở §8 file hệ quản trị đã chốt. Nguyên tắc chung:

- Thêm cột cho phép NULL hoặc DEFAULT hằng thường nhanh; DEFAULT biến đổi (`now()`, hàm) ghi lại toàn bảng.
- Đổi kiểu cột, đặt NOT NULL thường ghi lại hoặc quét bảng dưới khoá: dùng mở rộng → chuyển → thu gọn (§2), hoặc ràng buộc kiểm sau (thêm chưa kiểm, rồi kiểm) nếu hệ hỗ trợ.
- Thêm index, UNIQUE, FK trên bảng lớn: dùng chế độ không khoá ghi hoặc công cụ online; dữ liệu trùng làm migration lỗi, kiểm trước.

Luôn đặt giới hạn chờ khoá (vài giây) để migration không treo hàng đợi truy vấn. Lỗi do khoá thì thử lại sau, không tăng timeout vô hạn.

## 4. Backfill (chuyển dữ liệu)

- Tách khỏi migration đổi cấu trúc; có thể là job hoặc script chạy riêng.
- Chạy theo lô theo khoá chính (`WHERE id > ? ORDER BY id LIMIT n`), commit mỗi lô, có điểm dừng nghỉ.
- Chạy lại được (idempotent): chỉ cập nhật dòng chưa xử lý (`WHERE new_col IS NULL`).
- Theo dõi độ trễ replica khi có bản sao.
- Ghi số dòng dự kiến, thời gian ước tính, cách kiểm tra hoàn tất (truy vấn đối soát).

## 5. Kiểm chứng trước khi bàn giao

Chạy trên CSDL không phải production, cùng hệ quản trị và phiên bản (ví dụ container):

1. CSDL sạch: lên toàn bộ → quay lui migration mới → lên lại. Không lỗi, schema sau lần lên thứ hai giống lần đầu.
2. Schema hiện tại có dữ liệu giả: lên migration mới, chạy backfill, kiểm đối soát.
3. Ca âm ràng buộc: chèn dữ liệu vi phạm NOT NULL, UNIQUE, CHECK, FK; xác nhận bị từ chối với đúng tên ràng buộc.
4. EXPLAIN cho AP quan trọng sau khi nạp dữ liệu giả đủ lớn.
5. So sánh schema dump trước/sau (hoặc diff do công cụ migration sinh) để chắc không có thay đổi ngoài ý muốn.

Ghi lệnh và kết quả. Không có môi trường để chạy thì ghi not-run kèm lý do; không khẳng định migration chạy được khi chưa chạy.

## 6. Ghi chú triển khai đi kèm migration

- Thứ tự so với deploy ứng dụng (trước, sau, hay tách nhiều lần phát hành).
- Mức khoá và thời gian ước tính trên khối lượng production (từ số liệu dự án, không từ dữ liệu thật đưa vào AI).
- Có cần sao lưu riêng hoặc cửa sổ bảo trì không.
- Cách quay lui và giới hạn của quay lui (dữ liệu ghi sau migration có bị mất không).
- Truy vấn kiểm tra sau triển khai.
