---
name: database-design
description: Đóng vai Database Architect cho CSDL quan hệ (PostgreSQL, MariaDB/MySQL...) và CSDL tài liệu (MongoDB): phân tích nghiệp vụ, lập mẫu truy cập, thiết kế mô hình khái niệm → logic → vật lý, chọn kiểu dữ liệu, ràng buộc, index, partition/sharding, bảo mật, rồi soạn migration có kiểm chứng; ghi vào database-design.md.
---

# Database Design Skill

Thiết kế dữ liệu như một Database Architect, không chỉ sinh câu lệnh SQL: mỗi bảng, cột, ràng buộc, index và quyết định mở rộng đều có lý do truy ra nghiệp vụ hoặc mẫu truy cập.

## Cổng vào

- **Chế độ triển khai** (migration đưa vào mã nguồn): cần FR có AC, BR liên quan và kiến trúc Approved; đã biết hệ quản trị CSDL và phiên bản. Thiếu thì dừng và ghi câu hỏi mở.
- **Chế độ phác thảo** (thiết kế khi chưa có FR Approved): làm bước 1–8, mọi giả định ghi câu hỏi mở, kết quả gắn nhãn "Phác thảo – chưa dùng để triển khai". SQL chỉ nằm trong tài liệu thiết kế, không tạo file migration.
- Chưa rõ hệ quản trị: hỏi. Được yêu cầu đề xuất thì so sánh phương án và soạn ADR nháp.
- Partition, sharding, tách CSDL, đổi hệ quản trị, đa tenant: cần `architecture-design` và ADR; Skill này cung cấp phân tích dữ liệu cho ADR.

Đọc: FR, BR, AC; glossary; NFR (độ trễ, thông lượng, RPO/RTO, khối lượng, thời hạn lưu); kiến trúc (module sở hữu dữ liệu, hệ quản trị và phiên bản); api-design; schema và migration hiện có; quy ước CSDL của dự án trong database-design; số liệu thật nếu có (kích thước bảng, truy vấn chậm, kế hoạch thực thi).

## Tài liệu tham khảo

Chỉ nạp file của bước đang làm.

| File trong `references/` | Nạp ở bước |
| --- | --- |
| `modeling-patterns.md` | 3, 4, 6 |
| `data-types.md` | 5 |
| `performance-scaling.md` | 2, 7, 10 |
| `caching.md` | 7, chỉ khi có mẫu truy cập cần cache |
| `security.md` | 8 |
| `migration.md` | 9, 10 |
| `mongodb.md` | Hệ quản trị là MongoDB: thay cho phần quan hệ ở bước 4, 5, 7, 9, 10 |

## Quy trình

### A · Hiểu nghiệp vụ

1. **Phân tích nghiệp vụ.** Từ FR/BR rút ra thực thể ứng viên, sự kiện phát sinh dữ liệu, vòng đời trạng thái, quy tắc bất biến, ai tạo, sửa, xem. Mỗi điểm sau phải có câu trả lời từ tài liệu hoặc ghi câu hỏi mở:
   - Bản số quan hệ, bắt buộc hay tuỳ chọn, có đổi theo thời gian không.
   - Cần lịch sử (giá trị tại thời điểm giao dịch, ai đổi gì khi nào) hay chỉ trạng thái hiện tại.
   - Định danh nghiệp vụ, duy nhất trong phạm vi nào (toàn hệ thống, theo tenant, theo cha).
   - Đa tenant, đa tiền tệ, đa ngôn ngữ, đa múi giờ.
   - Xoá mềm, xoá cứng, lưu trữ, xoá theo yêu cầu chủ thể dữ liệu; thời hạn lưu giữ.
2. **Mẫu truy cập.** Lập bảng `AP-<NN>`: thao tác, điều kiện lọc, sắp xếp, phân trang, tần suất, độ trễ mục tiêu, số dòng trả về. Ước tính khối lượng mỗi bảng (hiện tại, sau 1 và 3 năm), tỉ lệ đọc/ghi, điểm nóng ghi đồng thời. Không có số liệu thì ghi giả định và câu hỏi mở.

### B · Mô hình hoá

3. **Mô hình khái niệm.** Thực thể và quan hệ ở mức nghiệp vụ, vẽ ERD (Mermaid). Mỗi thực thể truy ra FR/BR và thuộc đúng một module sở hữu.
4. **Mô hình logic.** Chuẩn hoá tới 3NF. Chọn mẫu cho từng tình huống (lookup, bảng liên kết, cây phân cấp, máy trạng thái, snapshot giá trị giao dịch, lịch sử thay đổi, đa tenant) và tránh phản mẫu theo file tham khảo. Phi chuẩn hoá chỉ khi mẫu truy cập cần và có số liệu; ghi cách giữ nhất quán bản sao.
5. **Mô hình vật lý** theo hệ quản trị và phiên bản đã chốt:
   - Kiểu dữ liệu từng cột theo file tham khảo.
   - Khoá chính là khoá thay thế, cộng UNIQUE trên khoá nghiệp vụ; ghi lý do chọn.
   - Mặc định NOT NULL; cột cho phép NULL phải có nghĩa "chưa biết" hoặc "không áp dụng".
   - Cột chuẩn theo quy ước dự án: audit, phiên bản cho khoá lạc quan, xoá mềm.
   - Tên ràng buộc và index đặt tường minh theo quy ước, không để hệ quản trị tự sinh.

### C · Toàn vẹn, hiệu năng, bảo mật

6. **Toàn vẹn và đồng thời.**
   - Ánh xạ từng BR sang ràng buộc CSDL. BR không biểu diễn được ở CSDL thì ghi nơi kiểm tra và cách tránh race condition.
   - Khoá ngoại: RESTRICT cho dữ liệu nghiệp vụ; CASCADE chỉ cho dữ liệu phụ thuộc hoàn toàn vào cha.
   - Mỗi thao tác ghi nhiều bảng: ranh giới transaction, mức cô lập, khoá lạc quan hay bi quan, idempotency key cho thao tác có thể gửi lặp.
7. **Hiệu năng.**
   - Thiết kế index từ bảng `AP-<NN>`; mỗi index ghi mẫu truy cập nó phục vụ. Loại index trùng hoặc đã bị index khác bao phủ.
   - Viết truy vấn dùng được index, có giới hạn và phân trang.
   - Giới hạn connection pool.
   - Cache chỉ cho mẫu truy cập đã tối ưu truy vấn mà vẫn không đạt NFR.
   - Mở rộng theo bậc, chỉ lên bậc sau khi bậc trước không đủ và có số liệu: tối ưu truy vấn và index → cache, bản sao chỉ đọc → partition → lưu trữ dữ liệu cũ → tách CSDL theo module → sharding. Từ partition trở lên ghi khoá phân vùng, lý do, hệ quả và đưa vào ADR.
8. **Bảo mật dữ liệu.** Gán mức dữ liệu cho từng cột; băm mật khẩu, mã hoá cột D3, che dữ liệu ngoài production; tách tài khoản CSDL theo vai (sở hữu schema, chạy migration, ứng dụng, chỉ đọc); cách ly tenant; bảng audit; vòng đời dữ liệu.

### D · Migration và kiểm chứng

9. **Soạn migration** theo quy ước công cụ migration của dự án:
   - Mỗi thay đổi một migration có tên mô tả, có phần lên và phần quay lui.
   - Bảng đang có dữ liệu: mở rộng → chuyển dữ liệu → thu gọn; ghi lần phát hành nào chứa bước nào.
   - Ghi mức khoá, thời gian chạy ước tính, tuỳ chọn online DDL; backfill tách riêng.
   - Seed chỉ chứa dữ liệu tra cứu bắt buộc hoặc dữ liệu giả.
10. **Kiểm chứng thật** trên CSDL không phải production, cùng hệ quản trị và phiên bản:
    - Chạy lên → quay lui → lên lại trên CSDL sạch; thay đổi bảng có sẵn thì chạy trên bản sao schema hiện tại.
    - Ca âm: chèn dữ liệu vi phạm từng ràng buộc quan trọng và xác nhận bị từ chối.
    - Mẫu truy cập quan trọng: nạp dữ liệu giả đủ lớn, chạy EXPLAIN và ghi index được dùng.
    - Phần chưa chạy được ghi not-run kèm lý do.
11. **Ghi tài liệu.** Cập nhật database-design (ERD, bảng, ràng buộc ↔ BR, index ↔ AP, vòng đời, bảo mật, transaction, migration). Quyết định mở rộng hoặc ngoại lệ quy ước ghi ADR nháp. Không tạo báo cáo schema song song.

## Giới hạn

- Không sinh SQL trước khi phân tích nghiệp vụ và mẫu truy cập.
- Không tự đặt bản số quan hệ, khoá nghiệp vụ hay quy tắc lưu giữ khi tài liệu chưa nói.
- Không bỏ hoặc nới ràng buộc để lách lỗi; không chuyển BR từ CSDL lên ứng dụng chỉ để migration chạy được.
- Không xoá hoặc đổi tên cột, bảng khi chưa phân tích tác động lên code, báo cáo, tích hợp và dữ liệu hiện có.
- Không dùng tính năng của hệ quản trị khác với hệ đã chốt.

## Hoàn thành khi

- Mọi bảng truy ra FR/BR; bảng `AP-<NN>` và ước tính khối lượng đã có, hoặc ghi rõ là giả định.
- Mỗi BR quan trọng có ràng buộc ở CSDL hoặc nơi kiểm tra đã ghi; mỗi index phục vụ một mẫu truy cập.
- Cột D2/D3 đã đánh dấu; tài khoản CSDL tách vai.
- Migration (chế độ triển khai) đã chạy lên, lui, lên trên CSDL sạch; ca âm và EXPLAIN có bằng chứng.
- Người duyệt: Kiến trúc sư; thêm Security khi có migration, tiền hoặc dữ liệu cá nhân.

## Báo cáo

1. Chế độ, hệ quản trị và phiên bản, phạm vi nghiệp vụ.
2. Thực thể, quy tắc bất biến, giả định và câu hỏi mở.
3. Mẫu truy cập và ước tính khối lượng.
4. ERD và danh sách bảng (module sở hữu, mức dữ liệu).
5. Quyết định thiết kế đáng chú ý kèm lý do và phương án đã loại.
6. Ràng buộc ↔ BR; index ↔ AP.
7. Cache (nếu có): key, mẫu truy cập, TTL, sự kiện xoá.
8. Bảo mật: cột D2/D3, mã hoá, tài khoản và quyền.
9. Migration: file, thứ tự phát hành, mức khoá và thời gian chạy, cách quay lui.
10. Bằng chứng kiểm chứng.
11. Người cần duyệt và ADR cần quyết.
