# Database Design – PostgreSQL

> Tài liệu tham khảo của Skill `database-design`. Chỉ nạp khi hệ quản trị đã chốt là PostgreSQL, và chỉ mục của bước đang làm. Nguyên tắc nằm ở file chủ đề; file này chỉ nêu cú pháp, giới hạn và phiên bản riêng của PostgreSQL. Luôn kiểm phiên bản dự án đang dùng.

## 1. Đặc điểm cần biết

| Vấn đề | PostgreSQL |
| --- | --- |
| DDL trong transaction | Có, rollback được cả DDL |
| Partial index | Có |
| CHECK | Luôn thực thi |
| Chế độ SQL | Chặt, không tự cắt chuỗi hay đổi giá trị sai |
| Clustered index | Không (bảng heap) |
| Index FK | Không tự tạo |
| So sánh chuỗi | Phân biệt hoa thường theo mặc định |
| Độ dài khoá index | Lớn |
| Mức cô lập mặc định | READ COMMITTED |
| Kết nối | Mỗi kết nối là một tiến trình |

## 2. Kiểu dữ liệu

| Dữ liệu | Kiểu |
| --- | --- |
| Khoá thay thế số | `bigint GENERATED ALWAYS AS IDENTITY` |
| Khoá UUID | `uuid`; sinh UUIDv7 ở ứng dụng hoặc `uuidv7()` từ PG 18 |
| Tiền | `numeric(19,4)` hoặc `bigint` đơn vị nhỏ nhất; không dùng `money` (phụ thuộc locale), `real`, `double precision` |
| Số lượng, tỉ lệ chính xác | `numeric(p,s)` |
| Số đo gần đúng | `double precision` |
| Thời điểm | `timestamptz` |
| Ngày / giờ trong ngày | `date` / `time` + cột múi giờ IANA |
| Khoảng thời gian | `interval`; khoảng ngày giờ: `tstzrange`, `daterange` |
| Văn bản ngắn có giới hạn | `text` + CHECK `char_length(x) <= n`, hoặc `varchar(n)` |
| Văn bản dài | `text` |
| Bảng mã | UTF-8 (mặc định của CSDL) |
| Không phân biệt hoa thường | `citext` hoặc index trên `lower(x)` |
| Boolean | `boolean` |
| Tập giá trị cố định | `text` + CHECK, ưu tiên hơn `ENUM` |
| JSON | `jsonb` |
| Địa chỉ IP | `inet` |
| Nhị phân nhỏ, cột mã hoá | `bytea` |
| Mật khẩu (chuỗi băm) | `text` |
| Toạ độ địa lý | PostGIS `geography(Point, 4326)` (extension: ghi ADR) |

`char(n)`: tài liệu PostgreSQL khuyến nghị không dùng. Không có kiểu `NCHAR`/`NVARCHAR`.

## 3. Index

- **Partial index** `WHERE …`: cho phần hiếm của cột phân bố lệch, cho cột thưa (`WHERE col IS NOT NULL`).
- **HOT update** mất khi cột được index thay đổi: tránh index cột cập nhật liên tục mà không có AP.
- **Covering:** `INCLUDE (…)`; kế hoạch hiện `Index Only Scan`.
- **Index biểu thức:** `CREATE INDEX … ON t (lower(email))`.
- **Cột FK** phải tự tạo index để join và xoá cha không quét bảng con.
- **Index thừa:** `pg_stat_user_indexes.idx_scan`. Không có cách ẩn index; xoá bằng migration có quay lui.
- **Loại chuyên dụng:** GIN cho `jsonb`, mảng, full-text (`tsvector`), trigram (`pg_trgm`); GiST cho khoảng, hình học, exclusion; BRIN cho bảng rất lớn chèn theo thời gian.
- **Tạo không khoá ghi:** `CREATE INDEX CONCURRENTLY`; không chạy trong transaction; lỗi giữa chừng để lại index `INVALID` cần xoá.
- **Skip scan:** từ PG 18.
- **`LIKE 'abc%'`:** chỉ dùng được B-Tree khi collation `C` hoặc index tạo với `text_pattern_ops`/`varchar_pattern_ops`.
- **`OR` nhiều cột:** BitmapOr trên các index riêng.
- **Sắp xếp không dùng được index:** nút `Sort` trong kế hoạch.

## 4. Truy vấn

- Keyset: so sánh bộ giá trị `(created_at, id) < (?, ?)` dùng được index.
- Truy vấn con tương quan: viết lại bằng `JOIN` hoặc `LATERAL`.
- Đếm ước tính: `pg_class.reltuples`.
- Materialized view: `REFRESH MATERIALIZED VIEW CONCURRENTLY` (cần UNIQUE index trên view).
- Nạp hàng loạt: `COPY`.
- Giới hạn thời gian: `statement_timeout`, `idle_in_transaction_session_timeout`.
- PL/pgSQL chỉ cache kế hoạch câu lệnh theo từng phiên.

## 5. Đồng thời và kết nối

- Mức cô lập mặc định READ COMMITTED; `REPEATABLE READ`/`SERIALIZABLE` cần retry khi lỗi serialization.
- Hàng đợi trong bảng: `FOR UPDATE SKIP LOCKED`.
- Tải lớn: PgBouncer. Chế độ transaction không giữ prepared statement (driver cũ), biến phiên, advisory lock giữa các transaction.

## 6. Kiểm chứng và theo dõi

| | PostgreSQL |
| --- | --- |
| Cập nhật thống kê | `ANALYZE`; tương quan giữa cột: `CREATE STATISTICS` |
| Lệnh | `EXPLAIN (ANALYZE, BUFFERS)`; chạy thật câu lệnh, lệnh ghi bọc trong `BEGIN … ROLLBACK` |
| Tốt | `Index Scan`, `Index Only Scan`, `Bitmap Index Scan` trên bảng lớn |
| Cần xem lại | `Seq Scan` trên bảng lớn với điều kiện chọn lọc; `Sort`/`Hash` tràn đĩa (`external merge`, `Batches > 1`); `Rows Removed by Filter` lớn |
| Index đang dùng | Tên trong nút `Index Scan using …` |
| Ước tính sai | `rows` ước tính lệch xa `actual rows` |
| Theo dõi | `pg_stat_statements`, `auto_explain`, `log_min_duration_statement`; bloat và autovacuum trên bảng cập nhật nhiều |
| Cấu hình bậc 1 | `shared_buffers`, `work_mem` |

## 7. Partition và sharding

- Partition khai báo: PK và UNIQUE phải chứa khoá phân vùng; FK trỏ vào bảng partition được từ PG 12.
- Tạo phân vùng trước hạn: job định kỳ hoặc `pg_partman`; xoá theo khối bằng `DETACH PARTITION`/`DROP`.
- Sharding: Citus.

## 8. Migration

- DDL chạy trong transaction: gói mỗi migration trong transaction, trừ lệnh không chạy được trong transaction (`CREATE INDEX CONCURRENTLY`).
- Giới hạn chờ khoá: `SET lock_timeout = '5s'`.

| Thao tác | Mức khoá / cách làm |
| --- | --- |
| Thêm cột NULL / DEFAULT hằng | Nhanh (PG ≥ 11 không ghi lại bảng) |
| Thêm cột DEFAULT biến đổi | Ghi lại toàn bảng |
| Đổi kiểu cột | Thường ghi lại bảng + khoá độc quyền |
| Đặt NOT NULL | CHECK `NOT VALID` → `VALIDATE CONSTRAINT` → `SET NOT NULL` |
| Thêm FK | `NOT VALID` rồi `VALIDATE CONSTRAINT` |
| Thêm index | `CREATE INDEX CONCURRENTLY` |
| Thêm UNIQUE | Unique index `CONCURRENTLY` rồi `ADD CONSTRAINT … USING INDEX` |

## 9. Mẫu mô hình hoá

- Tập giá trị cố định: `text` + CHECK; `ENUM` thêm giá trị được nhưng bỏ hoặc đổi thứ tự khó.
- Cây: CTE đệ quy; materialized path dùng `ltree`.
- Chống chồng lấn khoảng hiệu lực: exclusion constraint với `btree_gist` + `tstzrange`.
- Trạng thái quá khứ của bảng: không có bảng temporal; dùng bảng lịch sử + trigger.
- UNIQUE bỏ qua dòng xoá mềm: partial unique index `WHERE deleted_at IS NULL`.

## 10. Bảo mật

- Mã hoá trong CSDL bằng `pgcrypto` đưa khoá vào câu lệnh: tránh, mã hoá ở ứng dụng.
- Thu hồi `CREATE` trên schema `public` (mặc định từ PG 15).
- Row-Level Security: `ENABLE` + `FORCE ROW LEVEL SECURITY`, policy theo `current_setting('app.tenant_id')`; tài khoản App không có `BYPASSRLS` và không là owner bảng.
- SQL động: `format()` với `%I`, `%L` hoặc `EXECUTE … USING`.
- `SECURITY DEFINER`: đặt `search_path` cố định trong định nghĩa hàm.
