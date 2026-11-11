# Database Design – Migration

> Tài liệu tham khảo của Skill `database-design`, dùng ở bước 9–10. Công cụ migration, thư mục, cách đặt tên file lấy theo dự án (database-design §7); file này nêu cách viết migration an toàn, không phụ thuộc công cụ.

## 1. Cấu trúc một migration

- Tên mô tả hành động: `<timestamp>_create_order`, `<timestamp>_add_order_paid_at`, `<timestamp>_backfill_order_paid_at`.
- Một migration một mục đích; đổi cấu trúc và chuyển dữ liệu tách migration riêng.
- Có phần lên và phần quay lui. Quay lui làm mất dữ liệu (xoá cột đã có dữ liệu) thì ghi rõ trong migration và trong báo cáo.
- Đặt tên ràng buộc, index tường minh để quay lui và migration sau tham chiếu được.
- Không phụ thuộc code ứng dụng (model, ORM) có thể đổi sau này; migration dữ liệu dùng SQL hoặc truy vấn độc lập.
- PostgreSQL: gói migration trong transaction (trừ lệnh không chạy được trong transaction như `CREATE INDEX CONCURRENTLY`). MariaDB/MySQL: DDL tự commit, nên mỗi migration chỉ một DDL hoặc viết sao cho chạy lại được (`IF NOT EXISTS`, kiểm tra trước).

## 2. Mở rộng → chuyển dữ liệu → thu gọn (expand / migrate / contract)

Thay đổi trên bảng đang dùng chia qua nhiều lần phát hành để phiên bản cũ và mới của ứng dụng cùng chạy được.

| Thay đổi | Lần phát hành 1 (mở rộng) | Lần 2 (chuyển) | Lần 3 (thu gọn) |
| --- | --- | --- | --- |
| Thêm cột bắt buộc | Thêm cột cho phép NULL (hoặc có DEFAULT) | Code ghi cột mới; backfill theo lô | Đặt NOT NULL (PostgreSQL: CHECK `NOT VALID` → `VALIDATE` → `SET NOT NULL`) |
| Đổi tên cột | Thêm cột mới; code ghi cả hai | Backfill; code đọc cột mới | Bỏ cột cũ |
| Đổi kiểu cột | Thêm cột kiểu mới; ghi cả hai | Backfill; chuyển đọc | Bỏ cột cũ |
| Tách bảng | Tạo bảng mới; ghi cả hai | Backfill; chuyển đọc | Bỏ cột ở bảng cũ |
| Xoá cột/bảng | Code ngừng dùng | — | Xoá (sau ít nhất một chu kỳ phát hành) |

## 3. Thao tác và mức khoá

| Thao tác | PostgreSQL | MariaDB / MySQL (InnoDB) |
| --- | --- | --- |
| Thêm cột NULL / có DEFAULT hằng | Nhanh (PG ≥ 11 không ghi lại bảng) | MySQL ≥ 8.0 `ALGORITHM=INSTANT`; MariaDB ≥ 10.3 instant ADD COLUMN |
| Thêm cột DEFAULT biến đổi (`now()`, hàm) | Ghi lại toàn bảng | Ghi lại bảng |
| Đổi kiểu cột | Thường ghi lại bảng + khoá độc quyền | `ALGORITHM=COPY`, khoá ghi; dùng công cụ online (gh-ost, pt-online-schema-change) với bảng lớn |
| Đặt NOT NULL | Quét bảng dưới khoá; dùng CHECK `NOT VALID` rồi `VALIDATE` | Ghi lại bảng |
| Thêm FK | `NOT VALID` rồi `VALIDATE CONSTRAINT` | Khoá bảng con trong thời gian kiểm tra |
| Thêm index | `CREATE INDEX CONCURRENTLY` | `ALGORITHM=INPLACE, LOCK=NONE` |
| Thêm UNIQUE | Tạo unique index CONCURRENTLY rồi `ADD CONSTRAINT … USING INDEX` | INPLACE; dữ liệu trùng làm migration lỗi, kiểm trước |

Luôn đặt giới hạn chờ khoá để migration không treo hàng đợi truy vấn: PostgreSQL `SET lock_timeout = '5s'`; MariaDB/MySQL `SET SESSION lock_wait_timeout = 5`. Lỗi do khoá thì thử lại sau, không tăng timeout vô hạn.

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
