# Database Design – MongoDB

> Tài liệu tham khảo của Skill `database-design`, dùng khi hệ quản trị đã chốt là MongoDB. Thay cho phần quan hệ ở bước 4–5, 7, 9–10; bước 1–3, 6, 8, 11 giữ nguyên. Phiên bản MongoDB, công cụ migration, driver/ODM lấy theo dự án; tính năng có ghi phiên bản tối thiểu thì kiểm phiên bản đang dùng trước khi áp.

Ánh xạ thuật ngữ trong database-design.md: bảng → collection, dòng → document, cột → field, FK → tham chiếu (`_id` của document khác), CHECK/NOT NULL → schema validation.

## 1. Nguyên tắc mô hình

Quan hệ: chuẩn hoá trước, tối ưu sau. MongoDB thì ngược lại: **thiết kế theo mẫu truy cập**. Dữ liệu đọc cùng nhau thì lưu cùng nhau. Vì vậy bảng `AP-NN` (bước 2) bắt buộc phải có trước khi vẽ document. Thiếu AP thì chưa thiết kế.

Với mỗi quan hệ trong ERD, chọn nhúng (embed) hay tham chiếu (reference):

| Quan hệ | Mặc định | Đổi sang tham chiếu khi |
| --- | --- | --- |
| 1-1 | Nhúng vào cha | Phần con lớn, ít đọc cùng cha, hoặc có quyền truy cập khác |
| 1-ít (vài chục phần tử, có giới hạn rõ) | Nhúng mảng | Phần con được đọc/sửa độc lập hoặc được nhiều cha dùng chung |
| 1-nhiều (hàng trăm đến hàng nghìn) | Mảng `_id` ở cha, hoặc `parent_id` ở con | Không có giới hạn trên → `parent_id` ở con |
| 1-rất nhiều (không giới hạn: log, sự kiện, bình luận) | `parent_id` ở con, có index | — |
| n-n | Mảng `_id` ở phía ít phần tử hơn | Cần thuộc tính trên quan hệ → collection liên kết riêng |

Câu hỏi quyết định cho mỗi quan hệ, trả lời từ AP, không đoán:

1. Dữ liệu con có luôn đọc cùng cha không?
2. Số phần tử con tối đa là bao nhiêu? Có giới hạn nghiệp vụ không?
3. Con có được sửa độc lập, thường xuyên, hoặc bởi nhiều tiến trình đồng thời không?
4. Con có được truy vấn riêng (không qua cha) không?
5. Bản sao nhúng có cần đồng bộ khi nguồn đổi không, hay là snapshot tại thời điểm giao dịch?

Ghi lựa chọn và lý do vào bảng quyết định thiết kế (báo cáo bàn giao mục 5).

## 2. Mẫu mô hình nên dùng

| Mẫu | Dùng khi | Lưu ý |
| --- | --- | --- |
| Tham chiếu mở rộng (extended reference) | AP đọc cha cần vài field của document khác (tên khách trên đơn) | Chỉ chép field ít đổi; ghi nguồn chuẩn và cách đồng bộ, hoặc ghi rõ đây là snapshot |
| Tập con (subset) | Cha cần N phần tử con mới nhất (10 đánh giá gần nhất) | Phần còn lại ở collection riêng; giới hạn mảng bằng `$push` + `$slice` |
| Giá trị tính sẵn (computed) | AP đọc tổng/đếm tần suất cao | Cập nhật cùng thao tác ghi bằng `$inc`; có job đối soát |
| Gom nhóm (bucket) | Dữ liệu theo thời gian, ghi nhiều, đọc theo khoảng | MongoDB ≥ 5.0 dùng time series collection trước khi tự làm bucket |
| Ngoại lệ (outlier) | Hầu hết document nhỏ, vài document có mảng rất lớn | Cờ `has_overflow` + collection phụ cho phần tràn |
| Đa hình (polymorphic) | Một collection chứa nhiều biến thể cùng được truy vấn chung | Field phân loại (`type`) bắt buộc; validator theo từng biến thể bằng `oneOf` |
| Phiên bản schema | Mọi collection có thể đổi cấu trúc | Field `schema_version` ở mọi document (§6) |

## 3. Phản mẫu

| Phản mẫu | Hậu quả | Cách thay |
| --- | --- | --- |
| Mảng tăng không giới hạn | Chạm giới hạn 16 MB mỗi document; index đa khoá phình to; mỗi lần ghi phải ghi lại document lớn | Tham chiếu từ con về cha; mẫu tập con hoặc bucket |
| Tách dữ liệu luôn đọc cùng nhau ra nhiều collection rồi `$lookup` ở AP tần suất cao | Mất lợi thế document, chậm hơn join quan hệ | Nhúng hoặc tham chiếu mở rộng |
| Nhúng dữ liệu bị nhiều nơi sửa (thông tin khách nhúng vào mọi đơn rồi đồng bộ khi đổi) | Cập nhật lan rộng, dễ lệch dữ liệu | Tham chiếu; chỉ nhúng snapshot hoặc field gần như không đổi |
| Document phình to (nhiều field ít dùng) | Tốn bộ nhớ đệm (working set), chậm đọc | Tách phần ít dùng sang collection khác |
| Một collection cho mỗi tenant/ngày/người dùng | Số collection và index lớn làm tốn tài nguyên, khó vận hành | Một collection + field phân loại có index |
| Tên field động (dùng giá trị làm key: `{"2026-11-11": 5}`) | Không đánh index được, không validate được | Mảng `{ k, v }` (mẫu thuộc tính) có index `(k, v)` |
| Không có schema validation | Dữ liệu sai kiểu, thiếu field lọt vào và chỉ lộ ra khi đọc | Validator `$jsonSchema` cho mọi collection (§4) |

## 4. Kiểu dữ liệu và schema validation

| Dữ liệu | Kiểu BSON | Không dùng |
| --- | --- | --- |
| Tiền, số lượng cần chính xác | `Decimal128`, hoặc `long` theo đơn vị nhỏ nhất khi chỉ một tiền tệ | `double` |
| Thời điểm | `Date` (luôn UTC); múi giờ hiển thị lưu riêng nếu nghiệp vụ cần | Chuỗi ngày giờ |
| Định danh | `ObjectId` mặc định; UUID lưu dạng `Binary` subtype 4, không lưu chuỗi | Số tự tăng tự quản (cần bộ đếm, nghẽn ghi) trừ khi nghiệp vụ bắt buộc |
| Mã nghiệp vụ hiển thị cho người dùng | `string` + unique index, tách khỏi `_id` | Dùng mã nghiệp vụ làm `_id` khi mã có thể đổi định dạng |
| Trạng thái, enum | `string` + `enum` trong validator | Số ma thuật |
| Tham chiếu | Cùng kiểu với `_id` đích (`ObjectId` với `ObjectId`) | Lẫn kiểu: so sánh `string` với `ObjectId` không khớp và không dùng được index |

Mọi collection có validator `$jsonSchema` khai báo bằng migration: `required`, `bsonType`, `enum`, `minimum`, `maxItems` cho mảng nhúng, `additionalProperties: false` khi cấu trúc đã ổn định. Mặc định `validationLevel: "strict"`, `validationAction: "error"`. Dùng `moderate`/`warn` chỉ tạm thời trong lúc chuyển schema (§6) và ghi thời hạn bỏ.

Validator không thay được ràng buộc giữa các document. Mỗi BR cần ánh xạ sang một trong các cách:

| BR | Cách giữ ở MongoDB |
| --- | --- |
| Duy nhất | Unique index (unique theo phạm vi: compound gồm field phạm vi; tính cả xoá mềm bằng partial index) |
| Field bắt buộc, miền giá trị, quan hệ giữa field trong một document | Validator (`$jsonSchema`, hoặc biểu thức query trong validator) |
| Tham chiếu tồn tại, không xoá cha khi còn con | Không có FK: kiểm ở ứng dụng trong transaction, hoặc chặn xoá cứng (chỉ xoá mềm); ghi rõ cách xử lý và job đối soát |
| Bất biến trên nhiều document | Gom vào một document nếu được (ghi một document là nguyên tử); nếu không, transaction đa document |

## 5. Index và truy vấn

### 5.1 Index

1. Mỗi index phục vụ ít nhất một AP; ghi AP cạnh index. `_id` đã có index sẵn.
2. **Quy tắc ESR** cho compound index: field so sánh bằng (Equality) → field sắp xếp (Sort) → field khoảng (Range). Index `(a, b, c)` dùng được cho tiền tố `a`, `a,b`, `a,b,c`.
3. Chiều sắp xếp trong index phải khớp, hoặc ngược hoàn toàn, với `sort` của AP để tránh stage `SORT` trong bộ nhớ.
4. Loại index cần biết:
   - Unique; partial (`partialFilterExpression`), thường dùng cho unique bỏ qua document đã xoá mềm.
   - TTL cho dữ liệu tự hết hạn (phiên, OTP, log ngắn hạn). TTL xoá theo chu kỳ nền, không đúng từng giây.
   - Multikey (field mảng): một compound index chỉ được có tối đa một field mảng.
   - Wildcard chỉ dùng cho mẫu thuộc tính khi không biết trước tên field.
   - Text index hoặc dịch vụ search riêng cho tìm toàn văn.
5. Index có collation cho truy vấn không phân biệt hoa thường; truy vấn phải dùng đúng collation đó.
6. Kiểm index thừa bằng `$indexStats`. Trước khi xoá index trên production, ẩn thử bằng `hideIndex` (≥ 4.4), theo dõi rồi mới xoá.
7. Tạo index trên collection lớn chạy nền nhưng vẫn tốn I/O và đi qua replica: chạy ngoài giờ cao điểm, theo dõi độ trễ replica. Unique index lỗi giữa chừng nếu dữ liệu trùng, nên kiểm trùng trước.

### 5.2 Điều kiện làm index kém

| Điều kiện | Cách thay |
| --- | --- |
| Regex không neo đầu (`/abc/`), không phân biệt hoa thường (`/^abc/i`) | Regex neo đầu, phân biệt hoa thường (`/^abc/`); index collation; text/search index |
| `$ne`, `$nin`, `$not` | Đảo thành điều kiện dương (`$in`); partial index cho phần cần tìm |
| `$or` trên nhiều field | Mỗi nhánh có index riêng; kiểm bằng explain |
| `$where`, `$expr` với hàm trên field | Lưu sẵn giá trị tính (mẫu computed) rồi index |
| Kiểu tham số khác kiểu field (`"123"` với `123`, chuỗi với `ObjectId`) | Ép kiểu ở ứng dụng trước khi truy vấn |

### 5.3 Mẫu truy vấn

- Luôn có projection; không trả nguyên document khi AP chỉ cần vài field.
- Danh sách luôn có `limit`. Danh sách lớn phân trang theo khoá (`{ created_at: { $lt: ? } }` kèm `_id` để phá hoà), không dùng `skip` lớn.
- Không N+1: nạp theo lô bằng `$in`, hoặc `$lookup` một lần. `$lookup` ở AP tần suất cao là dấu hiệu nên xem lại mô hình.
- Aggregation: `$match` và `$sort` (dùng được index) đặt đầu pipeline; `$project` sớm để giảm dữ liệu chuyền qua các stage.
- Cập nhật nguyên tử bằng toán tử (`$set`, `$inc`, `$push`), không đọc toàn document rồi ghi đè.
- Ghi nhiều document dùng `bulkWrite`/`insertMany` theo lô vừa phải.
- Đặt `maxTimeMS` cho truy vấn của ứng dụng.

### 5.4 Kiểm chứng bằng explain

`explain("executionStats")` trên dữ liệu giả đủ lớn:

| Tốt | Cần xem lại |
| --- | --- |
| `IXSCAN`, `totalKeysExamined` và `totalDocsExamined` gần `nReturned` | `COLLSCAN` trên collection lớn |
| Không có stage `SORT` (sắp theo index) | Stage `SORT` trong bộ nhớ; `totalDocsExamined` lớn hơn nhiều so với `nReturned` |
| Index được chọn là index thiết kế cho AP (`winningPlan`) | Index khác được chọn; nhiều kế hoạch bị loại (`rejectedPlans`) do index chồng nhau |

Theo dõi khi có tải thật: profiler (`slowms`), log truy vấn chậm, `$indexStats`, `$collStats`.

## 6. Thay đổi schema (migration)

MongoDB không có DDL bắt buộc, nhưng **mọi thay đổi cấu trúc vẫn đi qua migration trong mã nguồn**: tạo/xoá collection, index, validator; chuyển dữ liệu. Công cụ migration lấy theo dự án.

- Mỗi document có `schema_version`. Ứng dụng đọc được phiên bản cũ và mới trong thời gian chuyển.
- Áp mở rộng → chuyển dữ liệu → thu gọn như quan hệ:
  1. Ứng dụng đọc được cả hai dạng, ghi dạng mới; validator nới (`oneOf` hai phiên bản, hoặc `moderate` có thời hạn).
  2. Backfill theo lô theo `_id` (`{ _id: { $gt: last }, schema_version: { $lt: N } }`), chạy lại được, theo dõi độ trễ replica.
  3. Đối soát xong mới siết validator về phiên bản mới và bỏ code đọc dạng cũ.
- Đổi tên field: thêm field mới, ghi cả hai, backfill, rồi mới bỏ field cũ. Không `$rename` trên collection lớn khi code cũ còn chạy.
- Phần quay lui: xoá index/collection mới, khôi phục validator cũ. Backfill làm mất dữ liệu dạng cũ thì ghi rõ cách khôi phục (sao lưu trước khi chạy).
- Kiểm chứng trên MongoDB cùng phiên bản với production và cùng topology (replica set; sharded nếu production sharded, vì transaction và `$lookup` chịu ràng buộc khác):
  1. Lên → lui → lên trên CSDL sạch.
  2. Ca âm: chèn document vi phạm validator và unique index, xác nhận bị từ chối.
  3. Explain cho AP quan trọng sau khi nạp dữ liệu giả.

## 7. Đồng thời, transaction, độ bền

- Ghi một document là nguyên tử. Ưu tiên mô hình để thao tác nghiệp vụ chỉ chạm một document.
- Transaction đa document chỉ có trên replica set (≥ 4.0) hoặc sharded cluster (≥ 4.2): giữ ngắn (mặc định bị huỷ sau 60 giây), số document ít, xử lý lỗi `TransientTransactionError` / `UnknownTransactionCommitResult` bằng retry. Không gọi dịch vụ ngoài trong transaction.
- Khoá lạc quan: field `version`, `updateOne({ _id, version }, { $set: …, $inc: { version: 1 } })`; `matchedCount = 0` thì báo xung đột.
- Chuyển trạng thái có điều kiện trạng thái nguồn trong filter (`{ _id, status: "pending" }`).
- Bộ đếm nóng: `$inc` có điều kiện (`{ _id, qty: { $gte: n } }`, `{ $inc: { qty: -n } }`).
- Idempotency: unique index trên `(phạm vi, idempotency_key)`.
- Write concern `majority` cho dữ liệu nghiệp vụ (mặc định từ 5.0); không hạ xuống `w: 1` khi chưa có ADR. Đọc ngay sau ghi ở thao tác quan trọng thì dùng causal consistency hoặc đọc từ primary. Đọc từ secondary chỉ cho AP chấp nhận dữ liệu cũ.
- Một `MongoClient` cho mỗi tiến trình, `maxPoolSize` có giới hạn; tổng kết nối của mọi tiến trình nhỏ hơn giới hạn kết nối của máy chủ.

## 8. Mở rộng

Bậc mở rộng giống `performance-scaling.md` §6. Khác biệt riêng:

- Time series collection (≥ 5.0) và TTL index thay cho partition theo thời gian.
- Lưu trữ dữ liệu cũ: chuyển sang collection/cluster lưu trữ bằng job.
- **Sharding** cần ADR, trả lời thêm:
  - Khoá shard có trong gần như mọi truy vấn (tránh truy vấn rải mọi shard), độ phân tán cao, không tăng đơn điệu khi dùng ranged sharding (`ObjectId`, thời điểm làm dồn ghi vào một shard; dùng hashed hoặc compound).
  - Unique index trên collection sharded phải có khoá shard làm tiền tố.
  - Đổi khoá shard (`reshardCollection` ≥ 5.0) tốn kém, chọn đúng từ đầu.

## 9. Bảo mật

Áp `security.md`, cộng thêm:

- Bật xác thực (SCRAM hoặc x.509) và TLS. Không mở cổng ra ngoài mạng nội bộ.
- Tài khoản ứng dụng chỉ có `readWrite` trên database của nó (hoặc custom role hẹp hơn), không có `dbAdmin`, `dbOwner`, `root`. Tài khoản migration tách riêng để tạo index, đổi validator.
- **Chống NoSQL injection:** không đưa object từ request vào filter nguyên trạng (`{ password: { $ne: null } }`). Ép kiểu từng field, từ chối key bắt đầu bằng `$` hoặc chứa `.`. Không dùng `$where`, `$function`, `$accumulator` với đầu vào người dùng; tắt server-side JavaScript nếu không cần.
- Dữ liệu D3: mã hoá ở ứng dụng, hoặc Client-Side Field Level Encryption / Queryable Encryption (≥ 7.0) nếu dự án chọn. Mã hoá đĩa theo hạ tầng.
- Bật audit log nếu phiên bản/hạ tầng hỗ trợ và yêu cầu pháp lý cần.
