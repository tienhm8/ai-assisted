# Database Design – Chọn kiểu dữ liệu

> Tài liệu tham khảo của Skill `database-design`, dùng ở bước 5. Kiểu chuẩn đã chốt ở database-design §2 được ưu tiên; bảng này dùng khi đề xuất hoặc khi dự án chưa chốt. Luôn kiểm phiên bản hệ quản trị trước khi dùng một kiểu.

## 1. Bảng tra nhanh

| Dữ liệu | PostgreSQL | MariaDB / MySQL | Ghi chú |
| --- | --- | --- | --- |
| Khoá thay thế số | `bigint GENERATED ALWAYS AS IDENTITY` | `BIGINT UNSIGNED AUTO_INCREMENT` | `int` dễ cạn với bảng giao dịch |
| Khoá UUID | `uuid` (sinh UUIDv7 ở ứng dụng hoặc `uuidv7()` từ PG 18) | MariaDB ≥ 10.7: `UUID`; MySQL: `BINARY(16)` + `UUID_TO_BIN(…, 1)` | UUID ngẫu nhiên (v4) làm phân mảnh index clustered của InnoDB; ưu tiên UUID có thứ tự thời gian |
| Tiền | `numeric(19,4)` hoặc số nguyên đơn vị nhỏ nhất (`bigint`) | `DECIMAL(19,4)` hoặc `BIGINT` | Không dùng `float`/`double`/`real`; PostgreSQL không dùng kiểu `money` (phụ thuộc locale) |
| Số lượng, tỉ lệ chính xác | `numeric(p,s)` | `DECIMAL(p,s)` | Chọn `p,s` theo nghiệp vụ |
| Số đo khoa học, toạ độ gần đúng | `double precision` | `DOUBLE` | Chỉ khi chấp nhận sai số |
| Thời điểm (sự kiện đã xảy ra) | `timestamptz` | `DATETIME(6)` lưu UTC (quy ước ứng dụng) | MySQL/MariaDB `TIMESTAMP` giới hạn tới 2038 và tự đổi theo múi giờ phiên |
| Ngày (sinh nhật, ngày hiệu lực) | `date` | `DATE` | Không lưu ngày dạng thời điểm |
| Giờ trong ngày, lịch hẹn theo giờ địa phương | `time` + cột múi giờ IANA | `TIME` + cột múi giờ | Sự kiện tương lai theo giờ địa phương: lưu giờ địa phương + múi giờ, không đổi sang UTC sớm |
| Khoảng thời gian | `interval`; khoảng ngày giờ: `tstzrange`/`daterange` | Hai cột `start`, `end` + CHECK `start < end` | |
| Văn bản ngắn có giới hạn nghiệp vụ | `text` + CHECK `char_length(x) <= n` hoặc `varchar(n)` | `VARCHAR(n)` | `n` có căn cứ nghiệp vụ, không đặt `255` theo thói quen |
| Văn bản dài | `text` | `TEXT`/`MEDIUMTEXT` | MariaDB/MySQL: cột TEXT không có giá trị mặc định ở bản cũ, index cần độ dài tiền tố |
| Bảng mã | UTF-8 (mặc định của CSDL) | `utf8mb4` + collation phù hợp (`utf8mb4_0900_ai_ci`, `utf8mb4_unicode_520_ci`, `uca1400` ở MariaDB mới) | Không dùng `utf8`/`utf8mb3` (thiếu emoji, một số ký tự) |
| So sánh không phân biệt hoa thường | `citext` hoặc index trên `lower(x)` | Collation `_ci` | Email: UNIQUE trên dạng đã chuẩn hoá |
| Boolean | `boolean` | `BOOLEAN` (= `TINYINT(1)`) | Cờ có nhiều hơn hai trạng thái thì dùng cột trạng thái |
| Tập giá trị cố định | `text` + CHECK | `VARCHAR` + CHECK | Xem modeling-patterns §2 |
| JSON | `jsonb` | MySQL `JSON`; MariaDB `JSON` (là `LONGTEXT` + CHECK `JSON_VALID`) | Chỉ cho thuộc tính bán cấu trúc; truy vấn thường xuyên vào khoá JSON thì đưa ra cột thật |
| Địa chỉ IP | `inet` | MariaDB `INET4`/`INET6`; MySQL `VARBINARY(16)` | |
| Dữ liệu nhị phân, file | Không lưu file trong CSDL; lưu đường dẫn/khóa object storage + checksum | Như trên | `bytea`/`BLOB` chỉ cho dữ liệu nhỏ (khoá, chữ ký) |
| Mật khẩu | `text` chứa chuỗi băm (argon2id/bcrypt) | `VARCHAR(255)` | Không bao giờ lưu mật khẩu thô hay mã hoá hai chiều |
| Dữ liệu mã hoá ở mức cột | `bytea` | `VARBINARY`/`BLOB` | Kèm cột phiên bản khoá nếu có xoay vòng khoá |
| Số điện thoại, mã bưu chính, số tài khoản | `text`/`VARCHAR` | `VARCHAR` | Không dùng kiểu số: mất số 0 đầu, không phải đại lượng tính toán |
| Toạ độ địa lý | PostGIS `geography(Point, 4326)` | `POINT SRID 4326` + spatial index | Cần extension/engine: ghi vào ADR |

## 2. Quy tắc chọn

1. **Theo nghĩa nghiệp vụ, không theo dữ liệu mẫu.** "Mã đơn hàng gồm chữ số" vẫn là văn bản nếu không dùng để tính toán.
2. **Nhỏ nhất đủ dùng có dự phòng tăng trưởng.** Ước tính giá trị lớn nhất sau nhiều năm; PK giao dịch dùng 64 bit.
3. **Kiểu của FK trùng kiểu của PK được tham chiếu**, kể cả `UNSIGNED` và collation ở MariaDB/MySQL.
4. **NOT NULL mặc định**, DEFAULT chỉ khi giá trị mặc định có nghĩa nghiệp vụ.
5. **Không lưu giá trị định dạng** (tiền có dấu phân cách, ngày dạng chuỗi).
6. **Ghi rõ đơn vị** trong tên cột khi không hiển nhiên (`weight_grams`, `duration_seconds`).
7. **Cột sinh (generated column)** cho giá trị suy ra cần index hoặc ràng buộc; không lưu giá trị suy ra bằng tay.
8. **Không dùng `NCHAR`/`NVARCHAR` để có Unicode.** Đó là cách của SQL Server; PostgreSQL không có kiểu này, MariaDB/MySQL coi `NVARCHAR` là `VARCHAR` với charset `utf8mb3` (thiếu emoji, một số ký tự). Đặt `utf8mb4` ở mức CSDL/bảng và dùng `VARCHAR`/`TEXT`.
9. **`CHAR(n)` chỉ cho giá trị độ dài cố định thật** (mã quốc gia ISO, mã tiền tệ). Chuỗi độ dài thay đổi dùng `VARCHAR`/`text`: `CHAR` đệm khoảng trắng, tốn chỗ và gây so sánh khó lường; PostgreSQL khuyến nghị không dùng `char(n)`.
10. **Kiểu nhỏ hơn giúp index nhỏ hơn**, nhất là với InnoDB nơi PK nằm trong mọi index phụ; nhưng không đánh đổi khả năng tăng trưởng (quy tắc 2).

## 3. Khác biệt hay gây lỗi giữa PostgreSQL và MariaDB/MySQL

| Vấn đề | PostgreSQL | MariaDB / MySQL |
| --- | --- | --- |
| DDL trong transaction | Có (rollback được cả DDL) | Không; mỗi DDL tự commit, migration lỗi giữa chừng để lại trạng thái dở |
| Partial index | Có | Không; dùng cột sinh |
| CHECK | Luôn thực thi | MySQL ≥ 8.0.16, MariaDB ≥ 10.2 |
| Chế độ SQL | Chặt | Cần `STRICT_TRANS_TABLES` (hoặc tương đương) để không tự cắt chuỗi, tự đổi giá trị sai |
| Clustered index | Không (heap) | InnoDB clustered theo PK: PK ngẫu nhiên hoặc rộng làm chậm ghi và phình mọi index phụ |
| Index FK | Không tự tạo | InnoDB tự tạo nếu chưa có |
| So sánh chuỗi | Phân biệt hoa thường theo mặc định | Theo collation, thường không phân biệt |
| Độ dài khoá index | Lớn | Giới hạn byte (3072 với InnoDB DYNAMIC); `utf8mb4` = 4 byte/ký tự |
