# Database Design – Mẫu mô hình hoá

> Tài liệu tham khảo của Skill `database-design`, dùng ở bước 3–4 và 6. Đây là **cách làm**; quy ước riêng của dự án (đặt tên, kiểu khoá) lấy từ database-design §2 và được ưu tiên hơn.

## 1. Từ nghiệp vụ sang thực thể

| Câu trong FR/BR | Gợi ý mô hình |
| --- | --- |
| "Mỗi X thuộc một Y" | FK `x.y_id NOT NULL` → Y |
| "X có thể có (hoặc không) một Y" | FK cho phép NULL, hoặc bảng con 1-1 nếu thuộc tính của Y thưa |
| "X có nhiều Y, Y thuộc nhiều X" | Bảng liên kết `x_y(x_id, y_id)` với PK hoặc UNIQUE `(x_id, y_id)` |
| Liên kết có thuộc tính riêng (số lượng, vai trò, từ ngày) | Bảng liên kết thành thực thể có tên nghiệp vụ (ví dụ `enrollment`, `order_line`) |
| "Trạng thái chuyển từ A sang B" | Cột trạng thái + CHECK tập giá trị; bảng lịch sử chuyển trạng thái nếu cần truy vết |
| "Giá tại thời điểm mua" | Snapshot giá trị vào dòng giao dịch, không tham chiếu giá hiện tại |
| "Lưu lịch sử thay đổi" | Bảng lịch sử hoặc mô hình hiệu lực theo thời gian (mục 5) |
| "Mã duy nhất trong mỗi cửa hàng" | UNIQUE `(store_id, code)`, không UNIQUE `code` toàn bảng |

Kiểm tra bản số bằng câu hỏi hai chiều: "Một A có bao nhiêu B?" và "Một B có bao nhiêu A?", kể cả theo thời gian ("trước đây" có khác "hiện tại" không).

## 2. Tra cứu: bảng lookup hay CHECK/enum

| Tiêu chí | CHECK (hoặc kiểu enum) | Bảng lookup + FK |
| --- | --- | --- |
| Tập giá trị | Nhỏ, ổn định, gắn với logic code | Thay đổi bởi người vận hành, có thuộc tính (nhãn, thứ tự, đang dùng) |
| Đổi giá trị | Cần migration | Thêm dòng |
| Đa ngôn ngữ nhãn | Không | Có |

- PostgreSQL: ưu tiên `text` + CHECK hơn `ENUM` (thêm giá trị được, nhưng bỏ hoặc đổi thứ tự giá trị ENUM khó).
- MariaDB/MySQL: `ENUM` lưu theo chỉ số, đổi thứ tự giá trị làm sai dữ liệu sắp xếp; ưu tiên `VARCHAR` + CHECK (MySQL ≥ 8.0.16 và MariaDB ≥ 10.2 mới thực thi CHECK).

## 3. Cây phân cấp

| Mẫu | Hợp khi | Lưu ý |
| --- | --- | --- |
| Adjacency list (`parent_id`) | Cây nông, ghi nhiều, đọc theo cấp | Truy vấn cả nhánh dùng CTE đệ quy (PostgreSQL, MySQL ≥ 8.0, MariaDB ≥ 10.2) |
| Materialized path (`path` = `/1/4/9/`) | Đọc nhánh nhiều, ít di chuyển nút | Index tiền tố; PostgreSQL có `ltree` |
| Closure table (`ancestor_id, descendant_id, depth`) | Đọc tổ tiên/con cháu bất kỳ, cần FK đầy đủ | Ghi tốn thêm dòng |
| Nested set | Hầu như chỉ đọc | Ghi rất đắt; tránh cho dữ liệu thay đổi |

## 4. Máy trạng thái

- Cột `status` + CHECK tập trạng thái hợp lệ.
- Chuyển trạng thái hợp lệ kiểm ở ứng dụng hoặc trigger, kèm điều kiện trong UPDATE (`WHERE id = ? AND status = 'pending'`) để tránh race condition.
- Cần truy vết: bảng `<entity>_status_history(entity_id, from_status, to_status, changed_by, changed_at, reason)`.
- Ràng buộc theo trạng thái dùng CHECK có điều kiện, ví dụ `CHECK (status <> 'paid' OR paid_at IS NOT NULL)`.

## 5. Lịch sử và thời gian hiệu lực

| Nhu cầu | Mẫu |
| --- | --- |
| Biết ai đổi gì, khi nào (audit) | Bảng audit dạng append-only, ghi bởi ứng dụng hoặc trigger; không cho UPDATE/DELETE |
| Giá trị đúng tại một thời điểm (giá, chính sách, thuế suất) | Bảng phiên bản `valid_from`, `valid_to`; chống chồng lấn bằng exclusion constraint (PostgreSQL `btree_gist` + `tstzrange`) hoặc kiểm ở ứng dụng trong transaction có khoá |
| Truy vấn trạng thái quá khứ của cả bảng | MariaDB system-versioned table (`WITH SYSTEM VERSIONING`); PostgreSQL dùng bảng lịch sử + trigger |
| Nguồn sự thật là chuỗi sự kiện | Event store append-only; cần ADR |

## 6. Xoá mềm

- Chỉ dùng khi nghiệp vụ cần khôi phục hoặc truy vết; không mặc định cho mọi bảng.
- Cột `deleted_at` (thời điểm) tốt hơn cờ boolean.
- UNIQUE phải bỏ qua dòng đã xoá: PostgreSQL dùng partial unique index `WHERE deleted_at IS NULL`; MariaDB/MySQL không có partial index, dùng cột sinh (generated column) bằng NULL khi đã xoá rồi UNIQUE trên cột đó (NULL không vi phạm UNIQUE).
- FK tới dòng đã xoá mềm vẫn hợp lệ; quyết định nghiệp vụ cho dòng con.
- Dữ liệu cá nhân bị yêu cầu xoá: xoá mềm không đủ, cần xoá cứng hoặc ẩn danh hoá.

## 7. Đa tenant

| Mẫu | Cách ly | Chi phí vận hành | Hợp khi |
| --- | --- | --- | --- |
| Cột `tenant_id` trong bảng dùng chung | Logic (cần RLS hoặc kiểm tra bắt buộc) | Thấp | Nhiều tenant nhỏ |
| Schema riêng mỗi tenant | Trung bình | Migration nhân theo số tenant | Vài chục đến vài trăm tenant |
| CSDL riêng mỗi tenant | Cao | Cao | Yêu cầu pháp lý, tenant lớn |

Với cột `tenant_id`: có trong mọi bảng nghiệp vụ, đứng đầu PK hoặc UNIQUE và index composite, FK composite `(tenant_id, parent_id)` để không trỏ chéo tenant; PostgreSQL bật Row-Level Security làm lớp bảo vệ thứ hai. Chọn mẫu là quyết định kiến trúc: cần ADR.

## 8. Tiền và giao dịch tài chính

- Số tiền dùng kiểu số chính xác kèm mã tiền tệ (ISO 4217) khi đa tiền tệ.
- Sổ cái: bút toán bất biến (append-only); sửa sai bằng bút toán đảo, không UPDATE.
- Số dư tính từ bút toán hoặc lưu số dư kèm cột phiên bản để khoá lạc quan.
- Idempotency key UNIQUE cho thao tác thanh toán.

## 9. Phản mẫu cần tránh

| Phản mẫu | Vấn đề | Thay bằng |
| --- | --- | --- |
| EAV (`entity, attribute, value`) | Mất kiểu, mất ràng buộc, truy vấn phức tạp | Cột thật; thuộc tính động hiếm dùng thì cột JSON |
| Liên kết đa hình (`target_type`, `target_id`) | Không có FK | Mỗi loại một cột FK có CHECK "đúng một cột khác NULL", hoặc bảng liên kết riêng |
| Cột chứa danh sách (`"1,4,9"`) | Không join, không ràng buộc | Bảng liên kết |
| Cột lặp (`phone1`, `phone2`, `phone3`) | Giới hạn cứng, truy vấn lặp | Bảng con |
| Bảng "god" nhiều cột thưa cho nhiều loại | NULL tràn lan, ràng buộc yếu | Tách theo loại (bảng cha chung + bảng con) |
| Lưu giá trị suy ra mà không có cách đồng bộ | Lệch dữ liệu | Tính khi đọc, cột sinh, hoặc ghi rõ cơ chế đồng bộ |
| Khoá chính là dữ liệu nghiệp vụ có thể đổi (email, mã số thuế) | Đổi khoá lan ra mọi FK | Khoá thay thế + UNIQUE trên khoá nghiệp vụ |
