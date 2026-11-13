# Database Design – Hiệu năng và mở rộng

> Tài liệu tham khảo của Skill `database-design`, dùng ở bước 2, 7 và 10. Ngưỡng hiệu năng (độ trễ, thông lượng) lấy từ NFR của dự án, không lấy từ file này. File này nêu nguyên tắc trung lập; cú pháp, tên công cụ và giới hạn phiên bản tra ở file của hệ quản trị đã chốt (`postgresql.md`, `mysql-mariadb.md`): index §3, truy vấn §4, đồng thời §5, kiểm chứng §6, partition và sharding §7.

## 1. Hồ sơ mẫu truy cập (AP)

Mọi quyết định hiệu năng bắt đầu từ bảng này. Không có AP thì không có index, partition hay phi chuẩn hoá.

| AP | Mô tả | Loại | Điều kiện lọc | Sắp xếp / phân trang | Tần suất (ước tính) | Độ trễ mục tiêu | Số dòng trả về | Index / cấu trúc phục vụ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AP-01 | Danh sách đơn của khách | Đọc | `customer_id = ?`, `status IN (…)` | `created_at DESC`, keyset | 200/giây | p95 < NFR | ≤ 50 | `ix_order_customer_status_created` |

Bổ sung ước tính khối lượng mỗi bảng: số dòng hiện tại, tăng trưởng/tháng, kích thước dòng trung bình, sau 1 và 3 năm; tỉ lệ đọc/ghi; điểm nóng (một dòng bị nhiều phiên ghi đồng thời, ví dụ số dư, tồn kho, bộ đếm).

## 2. Thiết kế index

### 2.1 Nguyên tắc

1. **Xuất phát từ AP**, không từ cột. Mỗi index ghi AP mà nó phục vụ.
2. **Ứng viên nên xét:** cột trong `WHERE`, điều kiện `JOIN`, `ORDER BY`, `GROUP BY` của AP quan trọng; cột FK; cột có nhiều giá trị khác nhau (độ chọn lọc cao) và thường dùng để tìm kiếm, lọc.
3. **Thường không đáng đánh index:**
   - Bảng rất nhỏ (vài nghìn dòng trở xuống): quét toàn bảng rẻ hơn, bộ tối ưu sẽ bỏ qua index.
   - Cột ít giá trị và phân bố đều (boolean, trạng thái 0/1) khi đứng một mình. Ngoại lệ: phân bố lệch và AP chỉ tìm phần hiếm (ví dụ 1% đơn `pending`), khi đó dùng partial index nếu hệ có, hoặc composite có cột chọn lọc đứng sau.
   - Cột bị cập nhật liên tục mà không có AP lọc theo nó: mỗi UPDATE phải sửa cả index và có thể mất tối ưu cập nhật tại chỗ của hệ quản trị.
   - Truy vấn không lọc (`SELECT … FROM t` lấy toàn bộ): index không giúp gì.
4. **Cột thưa (phần lớn NULL):** nếu AP tìm các dòng khác NULL thì index lại rất chọn lọc. Hệ có partial index thì dùng `WHERE col IS NOT NULL` cho gọn; không thì index thường.
5. **Covering index:** đưa cột trả về vào index để tránh đọc bảng; với clustered index, index phụ đã chứa PK.
6. **Index biểu thức** khi điều kiện lọc bắt buộc dùng hàm (`lower(email)`): index biểu thức, hoặc cột sinh có index.
7. **Cột FK** cần index để join và xoá cha không quét bảng con; kiểm hệ quản trị có tự tạo không.
8. **Loại index thừa:** index là tiền tố của index khác, index trùng với UNIQUE/PK, index không AP nào dùng (kiểm bằng thống kê sử dụng index của hệ quản trị). Trước khi xoá index trên production, ẩn thử nếu hệ hỗ trợ; không thì xoá bằng migration có quay lui.
9. **Chi phí ghi:** mỗi index làm chậm INSERT/UPDATE/DELETE và tốn chỗ; bảng ghi nhiều cần ít index.
10. **Loại index chuyên dụng:** full-text, không gian, JSON/mảng, khoảng, bảng rất lớn chèn theo thời gian; chỉ dùng loại hệ đã chốt hỗ trợ.
11. **Tạo index trên bảng có dữ liệu** bằng chế độ không khoá ghi của hệ quản trị; ghi hệ quả khi lỗi giữa chừng.

### 2.2 Index nhiều cột (composite)

- **Quy tắc tiền tố trái nhất (left-most prefix):** index `(a, b, c)` dùng để tìm được cho điều kiện trên `a`, `a,b`, `a,b,c`; không dùng để tìm khi thiếu `a`. Ngoại lệ: skip scan (nếu hệ có) dùng được khi `a` có ít giá trị, không nên thiết kế dựa vào nó.
- **Thứ tự cột:** cột so sánh bằng trước, sau đó cột khoảng (`>`, `<`, `BETWEEN`, `LIKE 'x%'`) hoặc sắp xếp. Sau cột khoảng đầu tiên, các cột tiếp theo không còn dùng để thu hẹp phạm vi tìm (chỉ lọc trong index).
- **Phục vụ cả `ORDER BY … LIMIT`:** khi cột sắp xếp nối tiếp các cột so sánh bằng và cùng chiều (hoặc ngược hoàn toàn), CSDL đọc theo thứ tự index và dừng sớm, không phải sắp xếp (kế hoạch thực thi không có bước sắp xếp).
- Không đặt cột chọn lọc cao lên đầu một cách máy móc; thứ tự do các AP quyết định, một index composite tốt thường thay được vài index một cột.

### 2.3 Điều kiện làm index kém hoặc không dùng được

| Điều kiện | Lý do | Cách viết / thiết kế thay |
| --- | --- | --- |
| `LIKE '%abc'`, `LIKE '%abc%'` | B-Tree sắp theo đầu chuỗi; không biết chuỗi bắt đầu bằng gì thì không xác định được phạm vi | Full-text hoặc index trigram; tìm theo đuôi: index trên `reverse(col)` |
| `LIKE 'abc%'` | Dùng được B-Tree tuỳ collation | Kiểm điều kiện collation/operator class của hệ quản trị |
| Hàm hoặc phép tính trên cột: `DATE(created_at) = ?`, `col + 1 = ?`, `lower(email) = ?` | Index lưu giá trị gốc, không lưu kết quả hàm | Viết thành khoảng `created_at >= ? AND created_at < ?`; chuyển phép tính sang vế hằng; hoặc index biểu thức (§2.1 mục 6) |
| `!=`, `<>`, `NOT IN` | Thường khớp phần lớn bảng nên quét toàn bảng rẻ hơn | Đảo thành điều kiện dương (`status IN (…)`); partial index nếu phần cần tìm nhỏ |
| `OR` trên nhiều cột (`a = ? OR b = ?`) | Một index composite không phục vụ được cả hai nhánh | Index riêng mỗi cột (bộ tối ưu gộp kết quả) hoặc tách `UNION ALL`; kiểm bằng EXPLAIN |
| Ép kiểu ngầm: cột chuỗi so với số, khác collation hoặc charset khi join | CSDL phải chuyển đổi giá trị cột từng dòng | Tham số đúng kiểu; FK cùng kiểu, cùng charset và collation |
| `IS NULL` | B-Tree thông dụng dùng được index | Không cần tránh; cột phần lớn NULL xem §2.1 mục 4 |

## 3. Mẫu truy vấn

| Vấn đề | Cách xử lý |
| --- | --- |
| `SELECT *` | Liệt kê cột cần: giảm I/O và dữ liệu truyền đi, mở đường cho covering index, không vỡ khi thêm cột |
| Không giới hạn số dòng | Luôn có `LIMIT`; danh sách lớn dùng phân trang |
| Phân trang `OFFSET` lớn | Keyset: `WHERE (created_at, id) < (?, ?) ORDER BY created_at DESC, id DESC LIMIT n`; bộ tối ưu không dùng index cho so sánh bộ giá trị thì viết tách `created_at < ? OR (created_at = ? AND id < ?)` |
| N+1 (truy vấn con cho từng dòng ở ứng dụng/ORM) | Join, hoặc nạp theo lô `WHERE id IN (…)` (eager loading của ORM); phát hiện bằng đếm số truy vấn mỗi request trong test hoặc log |
| Truy vấn con vô hướng trong `SELECT` (chạy lại cho từng dòng) | Viết bằng `JOIN` (kèm `GROUP BY` nếu cần) hoặc `LATERAL` nếu hệ có; bộ tối ưu không phải lúc nào cũng tự khử tương quan, kiểm bằng EXPLAIN |
| Kiểm tra tồn tại | `EXISTS (SELECT 1 …)` dừng ở dòng khớp đầu tiên; không dùng `COUNT(*) > 0`. Với `IN (subquery)`, hệ quản trị hiện đại thường tự đổi thành semi-join nên hiệu năng tương đương; khác biệt đáng kể là `NOT IN`: subquery có NULL thì trả về rỗng, luôn dùng `NOT EXISTS` |
| Lọc bằng `HAVING` điều kiện không phải hàm tổng hợp | Đưa vào `WHERE` để loại dòng trước khi gom nhóm; `HAVING` chỉ cho điều kiện trên kết quả tổng hợp (`HAVING SUM(x) > ?`) |
| Join bảng lớn rồi mới lọc | Điều kiện lọc mỗi bảng đặt trong `WHERE`/`ON` để thu nhỏ tập trước khi join; cột join có index và cùng kiểu |
| `UNION` khi các nhánh không trùng hoặc chấp nhận trùng | `UNION ALL`: không tốn sắp xếp/hash để loại trùng |
| `DISTINCT` để chữa join nhân dòng | Sửa điều kiện join hoặc dùng `EXISTS` thay vì join rồi `DISTINCT` |
| Đếm toàn bảng thường xuyên | Bộ đếm duy trì riêng, ước tính từ thống kê của hệ quản trị, hoặc chấp nhận gần đúng |
| Báo cáo/thống kê quét bảng lớn mỗi lần gọi | Bảng tổng hợp cập nhật theo lô hoặc theo sự kiện, materialized view nếu hệ có; ghi tần suất làm mới và độ trễ dữ liệu chấp nhận được (bậc 3 ở §6) |
| Ghi từng dòng trong vòng lặp | Insert/update theo lô (multi-row `INSERT`, lệnh nạp hàng loạt của hệ quản trị); lô vừa phải để không giữ khoá lâu |
| Truy vấn chạy vô hạn | Đặt giới hạn thời gian câu lệnh và thời gian transaction rảnh |

**Phi chuẩn hoá để giảm join** (lưu dư một cột từ bảng khác, bảng tổng hợp) là bậc 3 ở §6: chỉ làm khi AP và số liệu chứng minh join là nút thắt, ghi nguồn chuẩn của dữ liệu và cách đồng bộ bản sao (cùng transaction, trigger, job, sự kiện).

**Stored procedure, function, trigger:** không phải công cụ tăng tốc mặc định. Lợi ích "biên dịch sẵn" có giới hạn: kế hoạch thường chỉ cache theo phiên hoặc kết nối. Prepared statement ở tầng ứng dụng/driver cho phần lớn lợi ích đó. Lợi ích thật là giảm số lượt gọi qua mạng cho xử lý nhiều bước trên nhiều dòng. Đưa logic nghiệp vụ vào CSDL ảnh hưởng kiểm thử, review, migration và tính di chuyển giữa hệ quản trị nên cần ADR.

## 4. Kiểm chứng và theo dõi

Kiểm chứng AP quan trọng bằng kế hoạch thực thi trên dữ liệu giả có kích thước và phân bố gần thật. Bảng nhỏ luôn quét toàn bảng nên không chứng minh được gì. Sau khi nạp dữ liệu lớn, cập nhật thống kê trước khi đo.

Đọc kế hoạch thực thi:

- **Tốt:** truy cập bằng index (hoặc chỉ index) trên bảng lớn; ghi tên index được dùng.
- **Cần xem lại:** quét toàn bảng lớn với điều kiện chọn lọc; quét toàn bộ index; sắp xếp hoặc bảng tạm (nhất là tràn đĩa); số dòng bị lọc bỏ lớn.
- **Ước tính sai:** số dòng ước tính lệch xa thực tế do thống kê cũ hoặc tương quan giữa cột; cập nhật thống kê, thêm thống kê mở rộng hoặc histogram.

Theo dõi liên tục ở môi trường có tải thật bằng thống kê truy vấn và log truy vấn chậm của hệ quản trị. Ưu tiên tối ưu theo tổng thời gian (tần suất × độ trễ), không chỉ truy vấn chậm nhất. Lệnh và chỉ dấu cụ thể: §6 của file hệ quản trị.

## 5. Đồng thời và transaction

- Transaction ngắn; không gọi API ngoài, không chờ người dùng trong transaction.
- Khoá lạc quan (cột `version`, `UPDATE … WHERE id = ? AND version = ?`) cho xung đột hiếm; khoá bi quan (`SELECT … FOR UPDATE`) cho điểm nóng cần tuần tự.
- Hàng đợi việc trong bảng: `FOR UPDATE SKIP LOCKED` nếu hệ hỗ trợ.
- Tránh deadlock: khoá theo thứ tự cố định (ví dụ theo `id` tăng dần).
- Biết mức cô lập mặc định của hệ đã chốt. Nghiệp vụ cần chặt hơn thì ghi rõ và xử lý lỗi serialization bằng retry.
- Cập nhật bộ đếm nóng: `UPDATE … SET qty = qty - ? WHERE id = ? AND qty >= ?` thay cho đọc rồi ghi.
- **Kết nối:** ứng dụng dùng connection pool có kích thước giới hạn; tổng kết nối của mọi instance ứng dụng, job, công cụ cộng lại nhỏ hơn `max_connections` và chừa chỗ cho quản trị. Nhiều kết nối hơn không làm nhanh hơn: vượt số lõi CPU và năng lực I/O thì tranh chấp tăng. Tải lớn cân nhắc connection pooler đứng trước CSDL hoặc thread pool. Giá trị pool và `max_connections` ghi ở cấu hình môi trường, không đặt theo cảm tính.

## 6. Bậc mở rộng

Đi từ trên xuống; chỉ lên bậc sau khi bậc trước không đủ và có số liệu. Từ bậc 4 trở đi cần ADR.

| Bậc | Biện pháp | Dấu hiệu cần | Chi phí / hệ quả |
| --- | --- | --- | --- |
| 1 | Sửa truy vấn, thêm/bỏ index, cập nhật thống kê, cấu hình CSDL (bộ nhớ đệm, bộ nhớ sắp xếp), connection pool | Truy vấn chậm cụ thể | Thấp |
| 2 | Cache ở ứng dụng; bản sao chỉ đọc (read replica) | Đọc chiếm đa số, chấp nhận trễ đồng bộ | Dữ liệu cũ trên replica; định tuyến đọc/ghi |
| 3 | Phi chuẩn hoá có kiểm soát; bảng tổng hợp; materialized view | Báo cáo/tổng hợp đắt, chạy lặp lại | Đồng bộ dữ liệu suy ra |
| 4 | Partition | Bảng rất lớn theo thời gian hoặc theo khoá rõ ràng; cần xoá/lưu trữ theo khối; truy vấn luôn lọc theo khoá phân vùng | Ràng buộc trên PK/UNIQUE, FK, vận hành phân vùng |
| 5 | Lưu trữ dữ liệu cũ (archive) ra bảng/kho riêng | Dữ liệu nóng chỉ là phần nhỏ | Truy vấn lịch sử chậm hơn, quy trình lưu trữ |
| 6 | Tách CSDL theo module / tách OLAP sang kho phân tích | Tải khác bản chất, ranh giới module rõ | Mất join và transaction chéo; cần đồng bộ dữ liệu (CDC, sự kiện) |
| 7 | Sharding | Một máy chủ không chịu nổi ghi hoặc dung lượng dù đã qua các bậc trên | Rất cao: truy vấn chéo shard, transaction phân tán, cân bằng lại |

## 7. Partition

- **Kiểu:** RANGE (thời gian, phổ biến nhất), LIST (vùng, tenant lớn), HASH (phân tán đều khi không có khoá tự nhiên).
- **Khoá phân vùng** là cột có mặt trong hầu hết truy vấn để loại bỏ phân vùng (partition pruning); kiểm bằng EXPLAIN.
- **Hệ quả ràng buộc:**
  - PK và UNIQUE thường phải chứa khoá phân vùng.
  - Hỗ trợ FK với bảng partition khác nhau giữa các hệ, có hệ không hỗ trợ: kiểm §7 của file hệ quản trị trước khi chọn.
- **Vận hành:** tạo phân vùng trước hạn (job định kỳ hoặc công cụ quản lý phân vùng), phân vùng mặc định bắt dữ liệu lạc, xoá/lưu trữ bằng DETACH/DROP phân vùng thay cho DELETE.
- **Kích thước:** không chia quá nhỏ; hàng nghìn phân vùng làm chậm lập kế hoạch truy vấn.
- Partition không thay thế index; mỗi phân vùng vẫn cần index cho AP.

## 8. Sharding

Chỉ đề xuất khi có số liệu chứng minh bậc 1–6 không đủ. ADR phải trả lời:

- **Khoá shard:** cột có trong gần như mọi truy vấn và transaction (thường `tenant_id` hoặc `customer_id`), phân bố đều, không đổi theo thời gian.
- **Chiến lược định tuyến:** hash, range, hay bảng thư mục (directory); cách thêm shard và cân bằng lại.
- **Dữ liệu dùng chung** (danh mục, cấu hình): nhân bản tới mọi shard hay CSDL riêng.
- **Truy vấn và transaction chéo shard:** loại bỏ bằng thiết kế, hay chấp nhận saga / tổng hợp ở tầng ứng dụng.
- **Định danh:** sinh ID duy nhất toàn cục (UUIDv7, Snowflake), không dựa vào auto-increment từng shard.
- **Công cụ:** giải pháp sharding của hệ quản trị (§7 của file hệ quản trị) hay định tuyến ở ứng dụng; chi phí vận hành, sao lưu, khôi phục.
- **Phương án thay thế đã loại** và lý do.
