# Database Design – Chọn kiểu dữ liệu

> Tài liệu tham khảo của Skill `database-design`, dùng ở bước 5. Kiểu chuẩn đã chốt ở database-design §2 được ưu tiên; file này dùng khi đề xuất hoặc khi dự án chưa chốt. Tên kiểu cụ thể tra ở file của hệ quản trị đã chốt (`postgresql.md` §2, `mysql-mariadb.md` §2). Luôn kiểm phiên bản hệ quản trị trước khi dùng một kiểu.

## 1. Bảng tra theo loại dữ liệu

| Dữ liệu | Chọn | Tránh |
| --- | --- | --- |
| Khoá thay thế số | Số nguyên 64 bit tự tăng | Số nguyên 32 bit với bảng giao dịch (dễ cạn) |
| Khoá UUID | UUID có thứ tự thời gian (v7), lưu bằng kiểu UUID gốc hoặc nhị phân 16 byte | UUID ngẫu nhiên (v4) trên hệ có clustered index theo PK: phân mảnh index, chậm ghi |
| Tiền | Số thập phân chính xác (19,4) hoặc số nguyên đơn vị nhỏ nhất | Số dấu phẩy động; kiểu tiền phụ thuộc locale |
| Số lượng, tỉ lệ chính xác | Số thập phân `(p,s)` theo nghiệp vụ | |
| Số đo khoa học, toạ độ gần đúng | Số dấu phẩy động độ chính xác kép | Dùng khi không chấp nhận sai số |
| Thời điểm (sự kiện đã xảy ra) | Kiểu thời điểm có múi giờ, hoặc lưu UTC theo quy ước ứng dụng | Kiểu giới hạn năm 2038 hoặc tự đổi theo múi giờ phiên |
| Ngày (sinh nhật, ngày hiệu lực) | Kiểu ngày | Lưu ngày dạng thời điểm |
| Giờ địa phương, lịch hẹn tương lai | Giờ địa phương + cột múi giờ IANA | Đổi sang UTC sớm |
| Khoảng thời gian | Kiểu khoảng nếu hệ có; không thì hai cột `start`, `end` + CHECK `start < end` | |
| Văn bản ngắn có giới hạn nghiệp vụ | Chuỗi độ dài thay đổi, giới hạn `n` có căn cứ | `255` theo thói quen |
| Văn bản dài | Kiểu văn bản dài | Index toàn cột (thường cần tiền tố hoặc full-text) |
| Bảng mã | UTF-8 đầy đủ (4 byte/ký tự) ở mức CSDL/bảng | Biến thể UTF-8 3 byte (thiếu emoji, một số ký tự); `NCHAR`/`NVARCHAR` |
| So sánh không phân biệt hoa thường | Collation/kiểu không phân biệt hoa thường, hoặc index trên dạng chuẩn hoá | Email: UNIQUE trên dạng chưa chuẩn hoá |
| Boolean | Kiểu boolean | Cờ có hơn hai trạng thái: dùng cột trạng thái |
| Tập giá trị cố định | Chuỗi + CHECK (xem modeling-patterns §2) | `ENUM` khi giá trị có thể đổi hoặc đổi thứ tự |
| JSON | Kiểu JSON (nhị phân nếu có) cho thuộc tính bán cấu trúc | Khoá JSON bị truy vấn thường xuyên: đưa ra cột thật |
| Địa chỉ IP | Kiểu IP gốc nếu có; không thì nhị phân 16 byte | Chuỗi |
| Dữ liệu nhị phân, file | Đường dẫn/khoá object storage + checksum | Lưu file trong CSDL; nhị phân chỉ cho dữ liệu nhỏ (khoá, chữ ký) |
| Mật khẩu | Chuỗi chứa giá trị băm (argon2id/bcrypt) | Mật khẩu thô hay mã hoá hai chiều |
| Dữ liệu mã hoá ở mức cột | Nhị phân, kèm cột phiên bản khoá nếu xoay vòng khoá | |
| Số điện thoại, mã bưu chính, số tài khoản | Chuỗi | Kiểu số: mất số 0 đầu, không phải đại lượng tính toán |
| Toạ độ địa lý | Kiểu không gian SRID 4326 + spatial index | Cần extension/engine: ghi ADR |

## 2. Quy tắc chọn

1. **Theo nghĩa nghiệp vụ, không theo dữ liệu mẫu.** "Mã đơn hàng gồm chữ số" vẫn là văn bản nếu không dùng để tính toán.
2. **Nhỏ nhất đủ dùng có dự phòng tăng trưởng.** Ước tính giá trị lớn nhất sau nhiều năm; PK giao dịch dùng 64 bit.
3. **Kiểu của FK trùng kiểu của PK được tham chiếu**, kể cả dấu, charset và collation.
4. **NOT NULL mặc định**, DEFAULT chỉ khi giá trị mặc định có nghĩa nghiệp vụ.
5. **Không lưu giá trị định dạng** (tiền có dấu phân cách, ngày dạng chuỗi).
6. **Ghi rõ đơn vị** trong tên cột khi không hiển nhiên (`weight_grams`, `duration_seconds`).
7. **Cột sinh (generated column)** cho giá trị suy ra cần index hoặc ràng buộc; không lưu giá trị suy ra bằng tay.
8. **Unicode đặt ở mức CSDL/bảng**, không dùng `NCHAR`/`NVARCHAR` (cách của SQL Server).
9. **Chuỗi độ dài cố định chỉ cho giá trị cố định thật** (mã quốc gia ISO, mã tiền tệ): kiểu cố định đệm khoảng trắng, tốn chỗ, so sánh khó lường.
10. **Kiểu nhỏ hơn giúp index nhỏ hơn**, nhất là khi PK nằm trong mọi index phụ (clustered index); nhưng không đánh đổi khả năng tăng trưởng (quy tắc 2).
11. **Kiểm khác biệt hành vi của hệ đã chốt** trước khi dùng: DDL có rollback được không, CHECK có thực thi không, chế độ SQL chặt, độ dài khoá index, so sánh chuỗi mặc định (§1 của file hệ quản trị).
