# Database Design – Hiệu năng và mở rộng

> Tài liệu tham khảo của Skill `database-design`, dùng ở bước 2 và 7. Ngưỡng hiệu năng (độ trễ, thông lượng) lấy từ NFR của dự án, không lấy từ file này.

## 1. Hồ sơ mẫu truy cập (AP)

Mọi quyết định hiệu năng bắt đầu từ bảng này. Không có AP thì không có index, partition hay phi chuẩn hoá.

| AP | Mô tả | Loại | Điều kiện lọc | Sắp xếp / phân trang | Tần suất (ước tính) | Độ trễ mục tiêu | Số dòng trả về | Index / cấu trúc phục vụ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AP-01 | Danh sách đơn của khách | Đọc | `customer_id = ?`, `status IN (…)` | `created_at DESC`, keyset | 200/giây | p95 < NFR | ≤ 50 | `ix_order_customer_status_created` |

Bổ sung ước tính khối lượng mỗi bảng: số dòng hiện tại, tăng trưởng/tháng, kích thước dòng trung bình, sau 1 và 3 năm; tỉ lệ đọc/ghi; điểm nóng (một dòng bị nhiều phiên ghi đồng thời, ví dụ số dư, tồn kho, bộ đếm).

## 2. Thiết kế index

1. **Xuất phát từ AP**, không từ cột. Mỗi index ghi AP mà nó phục vụ.
2. **Thứ tự cột composite:** cột so sánh bằng trước, sau đó cột khoảng hoặc sắp xếp. Index `(a, b, c)` dùng được cho điều kiện trên `a`, `a,b`, `a,b,c`, không dùng được khi thiếu `a`.
3. **Độ chọn lọc:** cột có ít giá trị (boolean, trạng thái) hiếm khi đứng một mình; kết hợp trong composite hoặc partial index (PostgreSQL).
4. **Covering index:** đưa cột trả về vào index để tránh đọc bảng (PostgreSQL `INCLUDE`; InnoDB: index phụ đã chứa PK).
5. **Index biểu thức** khi điều kiện lọc dùng hàm (`lower(email)`); MariaDB/MySQL dùng cột sinh có index (MySQL ≥ 8.0.13 có functional index).
6. **Cột FK** cần index trên PostgreSQL để join và xoá cha không quét bảng con.
7. **Loại index thừa:** index là tiền tố của index khác, index trùng với UNIQUE, index không AP nào dùng.
8. **Chi phí ghi:** mỗi index làm chậm INSERT/UPDATE và tốn chỗ; bảng ghi nhiều cần ít index.
9. **Loại index chuyên dụng (PostgreSQL):** GIN cho `jsonb`, mảng, full-text; GiST cho khoảng, hình học, exclusion; BRIN cho bảng rất lớn chèn theo thời gian.
10. **Tạo index không khoá ghi:** PostgreSQL `CREATE INDEX CONCURRENTLY` (không chạy trong transaction); MariaDB/MySQL `ALGORITHM=INPLACE, LOCK=NONE`.

## 3. Mẫu truy vấn

| Vấn đề | Cách xử lý |
| --- | --- |
| Phân trang `OFFSET` lớn | Keyset: `WHERE (created_at, id) < (?, ?) ORDER BY created_at DESC, id DESC LIMIT n` |
| N+1 | Join hoặc nạp theo lô `WHERE id IN (…)` |
| Hàm bọc cột trong WHERE (`DATE(created_at) = ?`) | Viết thành khoảng `created_at >= ? AND created_at < ?` |
| `LIKE '%x%'` | Full-text index hoặc trigram (`pg_trgm`) |
| `SELECT *` | Liệt kê cột cần |
| Đếm toàn bảng thường xuyên | Bộ đếm duy trì riêng, ước tính từ thống kê, hoặc chấp nhận gần đúng |
| `OR` trên nhiều cột | Tách `UNION ALL` hoặc index riêng mỗi nhánh |
| Ép kiểu ngầm (so sánh chuỗi với số, khác collation) | Đúng kiểu tham số; FK cùng kiểu và collation |

Kiểm chứng bằng EXPLAIN (PostgreSQL `EXPLAIN (ANALYZE, BUFFERS)`; MariaDB `ANALYZE FORMAT=JSON`; MySQL `EXPLAIN ANALYZE`) trên dữ liệu giả có kích thước gần thật. Bảng nhỏ luôn quét toàn bảng nên không chứng minh được gì.

## 4. Đồng thời và transaction

- Transaction ngắn; không gọi API ngoài, không chờ người dùng trong transaction.
- Khoá lạc quan (cột `version`, `UPDATE … WHERE id = ? AND version = ?`) cho xung đột hiếm; khoá bi quan (`SELECT … FOR UPDATE`) cho điểm nóng cần tuần tự.
- Hàng đợi việc trong bảng: `FOR UPDATE SKIP LOCKED` (PostgreSQL, MySQL ≥ 8.0, MariaDB ≥ 10.6).
- Tránh deadlock: khoá theo thứ tự cố định (ví dụ theo `id` tăng dần).
- Mức cô lập mặc định: PostgreSQL READ COMMITTED; InnoDB REPEATABLE READ (có gap lock). Nghiệp vụ cần chặt hơn thì ghi rõ và xử lý lỗi serialization bằng retry.
- Cập nhật bộ đếm nóng: `UPDATE … SET qty = qty - ? WHERE id = ? AND qty >= ?` thay cho đọc rồi ghi.

## 5. Bậc mở rộng

Đi từ trên xuống; chỉ lên bậc sau khi bậc trước không đủ và có số liệu. Từ bậc 4 trở đi cần ADR.

| Bậc | Biện pháp | Dấu hiệu cần | Chi phí / hệ quả |
| --- | --- | --- | --- |
| 1 | Sửa truy vấn, thêm/bỏ index, cấu hình CSDL, connection pool | Truy vấn chậm cụ thể | Thấp |
| 2 | Cache ở ứng dụng; bản sao chỉ đọc (read replica) | Đọc chiếm đa số, chấp nhận trễ đồng bộ | Dữ liệu cũ trên replica; định tuyến đọc/ghi |
| 3 | Phi chuẩn hoá có kiểm soát; bảng tổng hợp; materialized view | Báo cáo/tổng hợp đắt, chạy lặp lại | Đồng bộ dữ liệu suy ra |
| 4 | Partition | Bảng rất lớn theo thời gian hoặc theo khoá rõ ràng; cần xoá/lưu trữ theo khối; truy vấn luôn lọc theo khoá phân vùng | Ràng buộc trên PK/UNIQUE, FK, vận hành phân vùng |
| 5 | Lưu trữ dữ liệu cũ (archive) ra bảng/kho riêng | Dữ liệu nóng chỉ là phần nhỏ | Truy vấn lịch sử chậm hơn, quy trình lưu trữ |
| 6 | Tách CSDL theo module / tách OLAP sang kho phân tích | Tải khác bản chất, ranh giới module rõ | Mất join và transaction chéo; cần đồng bộ dữ liệu (CDC, sự kiện) |
| 7 | Sharding | Một máy chủ không chịu nổi ghi hoặc dung lượng dù đã qua các bậc trên | Rất cao: truy vấn chéo shard, transaction phân tán, cân bằng lại |

## 6. Partition

- **Kiểu:** RANGE (thời gian, phổ biến nhất), LIST (vùng, tenant lớn), HASH (phân tán đều khi không có khoá tự nhiên).
- **Khoá phân vùng** là cột có mặt trong hầu hết truy vấn để loại bỏ phân vùng (partition pruning); kiểm bằng EXPLAIN.
- **Hệ quả ràng buộc:**
  - PostgreSQL (khai báo partition): PK và UNIQUE phải chứa khoá phân vùng; FK trỏ vào bảng partition được từ PG 12.
  - MariaDB/MySQL: mọi UNIQUE (kể cả PK) phải chứa khoá phân vùng; **bảng partition InnoDB không hỗ trợ FK** (cả trỏ đi lẫn trỏ đến).
- **Vận hành:** tạo phân vùng trước hạn (job định kỳ hoặc `pg_partman`), phân vùng mặc định bắt dữ liệu lạc, xoá/lưu trữ bằng DETACH/DROP phân vùng thay cho DELETE.
- **Kích thước:** không chia quá nhỏ; hàng nghìn phân vùng làm chậm lập kế hoạch truy vấn.
- Partition không thay thế index; mỗi phân vùng vẫn cần index cho AP.

## 7. Sharding

Chỉ đề xuất khi có số liệu chứng minh bậc 1–6 không đủ. ADR phải trả lời:

- **Khoá shard:** cột có trong gần như mọi truy vấn và transaction (thường `tenant_id` hoặc `customer_id`), phân bố đều, không đổi theo thời gian.
- **Chiến lược định tuyến:** hash, range, hay bảng thư mục (directory); cách thêm shard và cân bằng lại.
- **Dữ liệu dùng chung** (danh mục, cấu hình): nhân bản tới mọi shard hay CSDL riêng.
- **Truy vấn và transaction chéo shard:** loại bỏ bằng thiết kế, hay chấp nhận saga / tổng hợp ở tầng ứng dụng.
- **Định danh:** sinh ID duy nhất toàn cục (UUIDv7, Snowflake), không dựa vào auto-increment từng shard.
- **Công cụ:** Citus (PostgreSQL), Vitess (MySQL), Spider (MariaDB) hay định tuyến ở ứng dụng; chi phí vận hành, sao lưu, khôi phục.
- **Phương án thay thế đã loại** và lý do.
