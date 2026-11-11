# Database Design – Bảo mật dữ liệu

> Tài liệu tham khảo của Skill `database-design`, dùng ở bước 8. Định nghĩa mức D0–D3, thuật toán và nơi quản lý khoá, yêu cầu pháp lý lấy từ tài liệu bảo mật của dự án; file này nêu cách áp xuống bảng và cột.

## 1. Phân loại cột

Với mỗi bảng, đánh dấu cột D2/D3 trong danh sách bảng của database-design. Câu hỏi cho từng cột:

- Có thật cần lưu không? Không cần thì không thu thập.
- Cần đọc lại giá trị gốc không? Không cần (mật khẩu, mã OTP, token) thì chỉ lưu băm.
- Cần tìm kiếm chính xác theo giá trị không? Có thì thêm cột băm có khoá (HMAC) để tra cứu, giá trị gốc mã hoá riêng.
- Ai được xem: toàn bộ, che một phần, hay không ai trừ tiến trình hệ thống?
- Lưu bao lâu, sau đó xoá hay ẩn danh?

## 2. Lưu trữ theo loại dữ liệu

| Dữ liệu | Cách lưu |
| --- | --- |
| Mật khẩu | Băm một chiều có salt, thuật toán chậm (argon2id, bcrypt, scrypt) ở ứng dụng; không mã hoá hai chiều |
| Token phiên, token đặt lại mật khẩu, API key | Lưu băm (SHA-256 là đủ vì token ngẫu nhiên dài); hiển thị gốc một lần |
| Dữ liệu cá nhân cần đọc lại (CMND/CCCD, số tài khoản) | Mã hoá ở ứng dụng (envelope encryption, khoá từ KMS/vault) + cột HMAC nếu cần tra cứu; cột phiên bản khoá để xoay vòng |
| Dữ liệu D2 | Theo quy định dự án; tối thiểu mã hoá khi lưu ở mức đĩa/tablespace |
| Toàn bộ CSDL | Mã hoá đĩa hoặc TDE (MariaDB data-at-rest encryption, MySQL InnoDB tablespace encryption); kết nối bắt buộc TLS |

Mã hoá trong CSDL bằng hàm SQL (`pgcrypto`, `AES_ENCRYPT`) đưa khoá vào câu lệnh và có thể lộ qua log truy vấn; ưu tiên mã hoá ở ứng dụng.

## 3. Tài khoản và quyền

| Tài khoản | Quyền | Dùng bởi |
| --- | --- | --- |
| Owner | Sở hữu schema; không đăng nhập thường ngày | Quản trị |
| Migrator | DDL trên schema của ứng dụng | Pipeline chạy migration |
| App | SELECT/INSERT/UPDATE/DELETE trên bảng cần; EXECUTE hàm cần; không DDL | Ứng dụng |
| Read-only | SELECT trên view hoặc bảng được phép, đã che D3 | Báo cáo, hỗ trợ |

- Bảng audit, sổ cái: tài khoản App chỉ INSERT và SELECT, không UPDATE/DELETE.
- Không cấp quyền cho `PUBLIC`; PostgreSQL thu hồi `CREATE` trên schema `public` (mặc định từ PG 15).
- Mỗi module (nếu tách schema) có tài khoản riêng, không đọc trực tiếp schema module khác.

## 4. Cách ly tenant

- Cột `tenant_id` trong mọi bảng nghiệp vụ, đứng đầu index; FK composite có `tenant_id`.
- PostgreSQL Row-Level Security: `ENABLE` + `FORCE ROW LEVEL SECURITY`, policy theo `current_setting('app.tenant_id')`; tài khoản App không có `BYPASSRLS` và không là owner bảng.
- MariaDB/MySQL không có RLS: bắt buộc lọc ở tầng truy cập dữ liệu dùng chung, kèm test truy cập chéo tenant.

## 5. Chống injection ở tầng CSDL

- Truy vấn tham số hoá; tên bảng/cột động chỉ lấy từ allow-list.
- Hàm/thủ tục lưu trữ: không ghép chuỗi trong SQL động (PostgreSQL dùng `format()` với `%I`, `%L` hoặc `EXECUTE … USING`).
- PostgreSQL `SECURITY DEFINER`: đặt `search_path` cố định trong định nghĩa hàm.

## 6. Audit

- Bảng audit ghi: ai (ID người dùng hoặc dịch vụ), làm gì, trên bản ghi nào, khi nào, từ đâu (correlation ID), giá trị trước/sau với cột không phải D3.
- Append-only, có thể tách phân vùng theo thời gian, thời hạn lưu theo chính sách.
- Không ghi giá trị D3 vào audit; chỉ ghi "đã đổi".

## 7. Vòng đời và môi trường không phải production

- Chính sách lưu giữ cho từng nhóm dữ liệu; job lưu trữ hoặc huỷ theo phân vùng/lô.
- Xoá theo yêu cầu chủ thể dữ liệu: liệt kê mọi bảng chứa dữ liệu của người đó (kể cả audit, bản sao phi chuẩn hoá, bản sao lưu) và cách xử lý (xoá cứng, ẩn danh).
- Dữ liệu dev/test/staging: dữ liệu giả hoặc bản sao đã ẩn danh không đảo ngược được; không sao chép dump production nguyên trạng.
- Sao lưu được mã hoá; quyền khôi phục giới hạn.
