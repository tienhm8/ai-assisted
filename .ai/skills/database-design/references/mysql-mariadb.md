# Database Design – MySQL và MariaDB

> Tài liệu tham khảo của Skill `database-design`. Chỉ nạp khi hệ quản trị đã chốt là MySQL hoặc MariaDB (engine InnoDB), và chỉ mục của bước đang làm. Nguyên tắc nằm ở file chủ đề; file này chỉ nêu cú pháp, giới hạn và phiên bản riêng. Hai hệ đã tách nhánh: luôn kiểm đúng hệ và phiên bản dự án đang dùng.

## 1. Đặc điểm cần biết

| Vấn đề | MySQL / MariaDB (InnoDB) |
| --- | --- |
| DDL trong transaction | Không; mỗi DDL tự commit, migration lỗi giữa chừng để lại trạng thái dở |
| Partial index | Không; dùng cột sinh |
| CHECK | Chỉ thực thi từ MySQL 8.0.16, MariaDB 10.2 |
| Chế độ SQL | Cần `STRICT_TRANS_TABLES` (hoặc tương đương) để không tự cắt chuỗi, tự đổi giá trị sai |
| Clustered index | Theo PK: PK ngẫu nhiên hoặc rộng làm chậm ghi và phình mọi index phụ (PK nằm trong mọi index phụ) |
| Index FK | Tự tạo nếu chưa có |
| So sánh chuỗi | Theo collation, thường không phân biệt hoa thường |
| Độ dài khoá index | Giới hạn byte (3072 với row format DYNAMIC); `utf8mb4` tính 4 byte/ký tự |
| Mức cô lập mặc định | REPEATABLE READ, có gap lock |

## 2. Kiểu dữ liệu

| Dữ liệu | Kiểu |
| --- | --- |
| Khoá thay thế số | `BIGINT UNSIGNED AUTO_INCREMENT` |
| Khoá UUID | MariaDB ≥ 10.7: `UUID`; MySQL: `BINARY(16)` + `UUID_TO_BIN(…, 1)` |
| Tiền | `DECIMAL(19,4)` hoặc `BIGINT` đơn vị nhỏ nhất; không dùng `FLOAT`/`DOUBLE` |
| Số lượng, tỉ lệ chính xác | `DECIMAL(p,s)` |
| Số đo gần đúng | `DOUBLE` |
| Thời điểm | `DATETIME(6)` lưu UTC (quy ước ứng dụng). `TIMESTAMP` giới hạn tới 2038 và tự đổi theo múi giờ phiên |
| Ngày / giờ trong ngày | `DATE` / `TIME` + cột múi giờ |
| Khoảng thời gian | Không có kiểu khoảng: hai cột `start`, `end` + CHECK `start < end` |
| Văn bản ngắn có giới hạn | `VARCHAR(n)` |
| Văn bản dài | `TEXT`/`MEDIUMTEXT`; bản cũ không cho DEFAULT, index cần độ dài tiền tố |
| Bảng mã | `utf8mb4` + collation phù hợp (`utf8mb4_0900_ai_ci`, `utf8mb4_unicode_520_ci`, `uca1400` ở MariaDB mới); không dùng `utf8`/`utf8mb3` |
| Không phân biệt hoa thường | Collation `_ci` |
| Boolean | `BOOLEAN` (= `TINYINT(1)`) |
| Tập giá trị cố định | `VARCHAR` + CHECK; `ENUM` lưu theo chỉ số, đổi thứ tự giá trị làm sai sắp xếp |
| JSON | MySQL `JSON`; MariaDB `JSON` là `LONGTEXT` + CHECK `JSON_VALID` |
| Địa chỉ IP | MariaDB `INET4`/`INET6`; MySQL `VARBINARY(16)` |
| Nhị phân nhỏ, cột mã hoá | `VARBINARY`/`BLOB` |
| Mật khẩu (chuỗi băm) | `VARCHAR(255)` |
| Toạ độ địa lý | `POINT SRID 4326` + `SPATIAL` index |

`NVARCHAR` được coi là `VARCHAR` với charset `utf8mb3`: không dùng. FK phải trùng kiểu PK kể cả `UNSIGNED`, charset và collation.

## 3. Index

- **Không có partial index:** cột phân bố lệch dùng composite có cột chọn lọc đứng sau; cột thưa dùng index thường (vẫn lưu NULL).
- **Covering:** index phụ đã chứa PK; kế hoạch hiện `Using index` trong `Extra`.
- **Index biểu thức:** MySQL ≥ 8.0.13 functional index; MariaDB dùng cột sinh có index.
- **Index thừa:** MySQL `sys.schema_unused_indexes`; MariaDB bật `userstat` rồi xem `INFORMATION_SCHEMA.INDEX_STATISTICS`. Tắt thử trước khi xoá: MySQL ≥ 8.0 `INVISIBLE`, MariaDB ≥ 10.6 `IGNORED`.
- **Loại chuyên dụng:** `FULLTEXT`, `SPATIAL`.
- **Tạo không khoá ghi:** `ALGORITHM=INPLACE, LOCK=NONE`.
- **Skip scan:** MySQL ≥ 8.0.13.
- **`LIKE 'abc%'`:** dùng được B-Tree với collation của cột.
- **`OR` nhiều cột:** index merge trên các index riêng.
- **Sắp xếp không dùng được index:** `Using filesort` trong `Extra`.

## 4. Truy vấn

- Keyset: nếu bộ tối ưu không dùng index cho so sánh bộ giá trị, viết tách `created_at < ? OR (created_at = ? AND id < ?)`.
- Đếm ước tính: `information_schema.TABLES.TABLE_ROWS`.
- Không có materialized view: dùng bảng tổng hợp.
- Nạp hàng loạt: `LOAD DATA`.
- Giới hạn thời gian: MariaDB `max_statement_time`; MySQL `max_execution_time` (chỉ cho SELECT).
- Procedure được cache theo từng kết nối.

## 5. Đồng thời và kết nối

- REPEATABLE READ có gap lock: khoá cả khoảng trống giữa các khoá, dễ gây chờ hoặc deadlock khi chèn đồng thời.
- Hàng đợi trong bảng: `FOR UPDATE SKIP LOCKED` (MySQL ≥ 8.0, MariaDB ≥ 10.6).
- MariaDB có thể dùng thread pool.

## 6. Kiểm chứng và theo dõi

| | MySQL / MariaDB |
| --- | --- |
| Cập nhật thống kê | `ANALYZE TABLE`; histogram: MariaDB ≥ 10.4 `ANALYZE TABLE … PERSISTENT FOR …`, MySQL 8.0 `ANALYZE TABLE … UPDATE HISTOGRAM` |
| Lệnh | `EXPLAIN`; số liệu thực tế: MariaDB `ANALYZE FORMAT=JSON`, MySQL ≥ 8.0.18 `EXPLAIN ANALYZE` |
| Tốt | Cột `type`: `const`, `eq_ref`, `ref`, `range` |
| Cần xem lại | `type = ALL` (quét toàn bảng); `type = index` (quét toàn bộ index); `Extra`: `Using filesort`, `Using temporary` |
| Index đang dùng | Cột `key` (`possible_keys` chỉ là ứng viên) |
| Ước tính sai | Cột `rows`/`filtered` lệch thực tế |
| Theo dõi | Slow query log (`long_query_time`), `performance_schema` |
| Cấu hình bậc 1 | `innodb_buffer_pool_size` |

## 7. Partition và sharding

- Mọi UNIQUE (kể cả PK) phải chứa khoá phân vùng.
- **Bảng partition InnoDB không hỗ trợ FK**, cả trỏ đi lẫn trỏ đến.
- Sharding: Vitess (MySQL), Spider (MariaDB).

## 8. Migration

- DDL tự commit: mỗi migration chỉ một DDL, hoặc viết chạy lại được (`IF NOT EXISTS`, kiểm tra trước).
- Giới hạn chờ khoá: `SET SESSION lock_wait_timeout = 5`.

| Thao tác | Mức khoá / cách làm |
| --- | --- |
| Thêm cột NULL / DEFAULT hằng | MySQL ≥ 8.0 `ALGORITHM=INSTANT`; MariaDB ≥ 10.3 instant ADD COLUMN |
| Thêm cột DEFAULT biến đổi | Ghi lại bảng |
| Đổi kiểu cột | `ALGORITHM=COPY`, khoá ghi; bảng lớn dùng công cụ online (gh-ost, pt-online-schema-change) |
| Đặt NOT NULL | Ghi lại bảng |
| Thêm FK | Khoá bảng con trong thời gian kiểm tra |
| Thêm index | `ALGORITHM=INPLACE, LOCK=NONE` |
| Thêm UNIQUE | INPLACE; dữ liệu trùng làm migration lỗi, kiểm trước |

## 9. Mẫu mô hình hoá

- Tập giá trị cố định: `VARCHAR` + CHECK (CHECK chỉ thực thi từ MySQL 8.0.16, MariaDB 10.2); `ENUM` lưu theo chỉ số, đổi thứ tự làm sai sắp xếp.
- Cây: CTE đệ quy từ MySQL 8.0, MariaDB 10.2.
- Chống chồng lấn khoảng hiệu lực: không có exclusion constraint; kiểm ở ứng dụng trong transaction có khoá.
- Trạng thái quá khứ của bảng: MariaDB `WITH SYSTEM VERSIONING`; MySQL dùng bảng lịch sử + trigger.
- UNIQUE bỏ qua dòng xoá mềm: cột sinh bằng NULL khi `deleted_at` khác NULL, UNIQUE trên cột đó.

## 10. Bảo mật

- Mã hoá toàn CSDL: MariaDB data-at-rest encryption, MySQL InnoDB tablespace encryption.
- Mã hoá bằng `AES_ENCRYPT` đưa khoá vào câu lệnh: tránh, mã hoá ở ứng dụng.
- Không có Row-Level Security: bắt buộc lọc tenant ở tầng truy cập dữ liệu dùng chung, kèm test truy cập chéo tenant.
