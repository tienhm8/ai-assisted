---
name: database-design
description: Đóng vai Database Architect cho CSDL quan hệ (PostgreSQL, MariaDB/MySQL...): phân tích nghiệp vụ, lập mẫu truy cập, thiết kế mô hình khái niệm → logic → vật lý, chọn kiểu dữ liệu, ràng buộc, index, partition/sharding, bảo mật, rồi soạn migration SQL có kiểm chứng; ghi vào database-design.md.
---

# Database Design Skill

## 1. Mục tiêu

Thiết kế dữ liệu như một Database Architect, không chỉ sinh câu lệnh SQL: mỗi bảng, cột, ràng buộc, index và quyết định mở rộng đều có lý do truy ra nghiệp vụ hoặc mẫu truy cập; schema đúng, toàn vẹn, đủ nhanh cho tải dự kiến, an toàn và thay đổi được mà không làm gián đoạn hệ thống. AI chỉ soạn ở trạng thái Draft/Proposed.

## 2. Cổng vào

- **Chế độ triển khai** (migration đưa vào mã nguồn): cần FR đã qua cổng (có AC), BR liên quan và kiến trúc Approved; đã biết hệ quản trị CSDL và phiên bản. Thiếu thì dừng, ghi open-questions.md (`OQ-NN`).
- **Chế độ phác thảo** (được yêu cầu thiết kế cho một nghiệp vụ khi chưa có FR Approved): được làm bước 1–8 của quy trình, mọi giả định ghi `OQ-NN`, kết quả gắn nhãn "Phác thảo – chưa dùng để triển khai". SQL chỉ nằm trong tài liệu thiết kế, không tạo file migration trong mã nguồn.
- Chưa rõ hệ quản trị CSDL: hỏi. Không tự chọn; nếu được yêu cầu đề xuất, so sánh phương án và soạn ADR nháp.
- Yêu cầu chạm partition, sharding, tách CSDL, đổi hệ quản trị, đa tenant: cần `architecture-design` và ADR; Skill này chỉ cung cấp phân tích dữ liệu cho ADR.

## 3. Đầu vào

- FR, BR, AC; glossary (thuật ngữ → thực thể); NFR (độ trễ, thông lượng, tính sẵn sàng, RPO/RTO, khối lượng, thời hạn lưu).
- Kiến trúc: module sở hữu dữ liệu, ranh giới, hệ quản trị và phiên bản; api-design (nhu cầu đọc/ghi của API).
- Schema và migration hiện có; quy ước CSDL đã chốt (database-design §2); quy tắc mức dữ liệu D0–D3 và yêu cầu pháp lý.
- Số liệu thật nếu có: kích thước bảng, truy vấn chậm, kế hoạch thực thi, tốc độ tăng trưởng.
- Tài liệu tham khảo của Skill (nạp đúng phần cần cho bước đang làm): `references/modeling-patterns.md`, `references/data-types.md`, `references/performance-scaling.md`, `references/caching.md`, `references/migration.md`, `references/security.md`.

## 4. Quy trình

### Giai đoạn A · Hiểu nghiệp vụ

1. **Phân tích nghiệp vụ.** Từ FR/BR rút ra: danh từ nghiệp vụ (thực thể ứng viên), sự kiện (giao dịch phát sinh dữ liệu), vòng đời trạng thái, quy tắc bất biến, ai tạo/sửa/xem dữ liệu. Với mỗi điểm sau, phải có câu trả lời từ tài liệu hoặc ghi `OQ-NN`, không đoán:
   - Bản số quan hệ (một hay nhiều, bắt buộc hay tuỳ chọn) và có đổi theo thời gian không.
   - Có cần lịch sử (giá trị tại thời điểm giao dịch, ai đổi gì khi nào) hay chỉ trạng thái hiện tại.
   - Định danh nghiệp vụ là gì, có duy nhất không, duy nhất trong phạm vi nào (toàn hệ thống, theo tenant, theo cha).
   - Đa tenant, đa tiền tệ, đa ngôn ngữ, đa múi giờ.
   - Xoá: xoá mềm, xoá cứng, lưu trữ, xoá theo yêu cầu chủ thể dữ liệu; thời hạn lưu giữ.
2. **Hồ sơ tải và mẫu truy cập.** Lập bảng `AP-NN`: thao tác (đọc/ghi), điều kiện lọc, sắp xếp, phân trang, tần suất, độ trễ mục tiêu, số dòng trả về. Ước tính khối lượng mỗi bảng (hiện tại, sau 1 và 3 năm), tỉ lệ đọc/ghi, điểm nóng ghi đồng thời. Phân loại tải: giao dịch (OLTP), báo cáo/phân tích (OLAP) hay hỗn hợp. Không có số liệu thì ghi giả định và `OQ-NN`.

### Giai đoạn B · Mô hình hoá

3. **Mô hình khái niệm.** Thực thể và quan hệ ở mức nghiệp vụ, vẽ ERD (Mermaid); mỗi thực thể truy ra FR/BR và thuộc đúng một module sở hữu. Phân loại: thực thể chính, tra cứu (lookup), giao dịch, liên kết (n-n), lịch sử/audit.
4. **Mô hình logic.** Chuẩn hoá tới 3NF mặc định. Chọn mẫu mô hình cho từng tình huống (lookup hay CHECK, bảng liên kết, cây phân cấp, máy trạng thái, snapshot giá trị giao dịch, lịch sử thay đổi, đa tenant) theo `references/modeling-patterns.md`; tránh các phản mẫu ở đó (EAV, liên kết đa hình không khoá ngoại, cột chứa danh sách). Phi chuẩn hoá chỉ khi có mẫu truy cập cần và số liệu hoặc NFR chứng minh; ghi cách giữ nhất quán bản sao.
5. **Mô hình vật lý.** Theo hệ quản trị và phiên bản đã chốt:
   - Kiểu dữ liệu từng cột theo `references/data-types.md` (tiền, thời gian, định danh, văn bản, enum, JSON, IP, khoảng).
   - Khoá chính: khoá thay thế (identity hoặc UUID có thứ tự thời gian) cộng UNIQUE trên khoá nghiệp vụ; lý do chọn.
   - Nullability: mặc định NOT NULL; cột cho phép NULL phải có ý nghĩa "chưa biết/không áp dụng" rõ ràng.
   - Cột chuẩn theo quy ước dự án: audit (tạo/sửa bởi ai, lúc nào), phiên bản cho khoá lạc quan, cờ hoặc thời điểm xoá mềm.
   - Đặt tên bảng, cột, ràng buộc, index theo quy ước; tên ràng buộc đặt tường minh, không để hệ quản trị tự sinh.

### Giai đoạn C · Toàn vẹn, hiệu năng, bảo mật

6. **Toàn vẹn và đồng thời.**
   - Ánh xạ từng BR sang ràng buộc CSDL (NOT NULL, UNIQUE, CHECK, FK, exclusion nếu hệ quản trị hỗ trợ); BR không biểu diễn được ở CSDL thì ghi nơi kiểm tra và cách tránh race condition.
   - FK: chọn hành vi ON DELETE/ON UPDATE tường minh (RESTRICT mặc định cho dữ liệu nghiệp vụ; CASCADE chỉ cho dữ liệu phụ thuộc hoàn toàn vào cha).
   - Ranh giới transaction cho mỗi thao tác ghi nhiều bảng; mức cô lập; chọn khoá lạc quan (cột phiên bản) hay khoá bi quan (`SELECT … FOR UPDATE`); idempotency key cho thao tác có thể gửi lặp.
7. **Hiệu năng.** Theo `references/performance-scaling.md`:
   - Thiết kế index từ bảng `AP-NN`: mỗi index ghi AP mà nó phục vụ; thứ tự cột composite theo quy tắc tiền tố trái nhất (so sánh bằng → khoảng/sắp xếp); unique, partial, covering, biểu thức khi hệ quản trị hỗ trợ; index cho cột FK khi hệ quản trị không tự tạo. Không index cột ít giá trị đứng một mình, bảng rất nhỏ, cột cập nhật liên tục mà không AP nào lọc. Loại index trùng hoặc bị index khác bao phủ.
   - Viết truy vấn dùng được index: không bọc hàm quanh cột, không `LIKE '%x'`, cẩn thận với `!=`, `OR` nhiều cột và ép kiểu ngầm; chỉ chọn cột cần, có `LIMIT`, phân trang keyset cho danh sách lớn; tránh N+1 và truy vấn con theo từng dòng; `NOT EXISTS` thay `NOT IN`; `UNION ALL` khi không cần loại trùng; điều kiện không tổng hợp đặt ở `WHERE`, không ở `HAVING`.
   - Kết nối: connection pool giới hạn, tổng kết nối nhỏ hơn `max_connections`.
   - Cache (bậc 2) chỉ cho AP đã qua bậc 1 mà vẫn không đạt NFR, theo `references/caching.md`: kiểm đủ ba điều kiện (đọc ≫ ghi, nguồn đắt, chấp nhận trễ); với mỗi cache ghi key, TTL có jitter, mọi đường ghi phải xoá key, biện pháp chống dồn tải tương xứng với mức hot của key. Production có cache thì có job warm-up theo tầng (T1 bắt buộc, T2 hot) với registry nhóm do module sở hữu khai báo. Không thêm Bloom filter hay L1 nhiều instance khi chưa có số liệu.
   - Đi theo bậc mở rộng, chỉ lên bậc sau khi bậc trước không đủ và có số liệu: tối ưu truy vấn/index → cache, bản sao chỉ đọc → partition → lưu trữ dữ liệu cũ → tách CSDL theo module → sharding. Mỗi bậc từ partition trở lên ghi khoá phân vùng/khoá shard, lý do, hệ quả (ràng buộc unique, FK, truy vấn chéo), cách vận hành, và đưa vào ADR.
8. **Bảo mật dữ liệu.** Theo `references/security.md`: gán mức D0–D3 cho từng cột; băm mật khẩu, mã hoá cột D3, che dữ liệu ở môi trường không phải production; tách tài khoản CSDL (sở hữu schema, chạy migration, ứng dụng, chỉ đọc) với quyền tối thiểu; cách ly dữ liệu tenant; bảng audit; vòng đời dữ liệu (lưu giữ, lưu trữ, huỷ, xoá theo yêu cầu).

### Giai đoạn D · Migration và kiểm chứng

9. **Soạn migration.** Theo `references/migration.md` và quy ước công cụ migration của dự án:
   - Mỗi thay đổi một migration có tên mô tả; có phần lên và phần quay lui (hoặc ghi lý do không quay lui được và cách khôi phục).
   - Thay đổi trên bảng đang có dữ liệu theo mở rộng → chuyển dữ liệu → thu gọn; ghi rõ lần phát hành nào chứa bước nào.
   - Ghi mức khoá, thời gian chạy ước tính, tuỳ chọn online DDL của hệ quản trị; backfill tách riêng, chạy theo lô, chạy lại được.
   - Seed chỉ chứa dữ liệu tra cứu bắt buộc hoặc dữ liệu giả.
10. **Kiểm chứng thật** trên CSDL không phải production (container hoặc môi trường dev) cùng hệ quản trị và phiên bản với production:
    - Chạy lên → quay lui → lên lại trên CSDL sạch; chạy trên bản sao schema hiện tại nếu là thay đổi trên bảng có sẵn.
    - Thử ràng buộc bằng ca âm: chèn dữ liệu vi phạm từng NOT NULL/UNIQUE/CHECK/FK quan trọng và xác nhận bị từ chối.
    - Với AP quan trọng: nạp dữ liệu giả đủ lớn, chạy EXPLAIN (ANALYZE nếu được) và ghi index được dùng.
    - Ghi lệnh và kết quả thật; phần chưa chạy được ghi not-run kèm lý do.
11. **Ghi tài liệu.** Cập nhật database-design.md (ERD, danh sách bảng, ràng buộc/BR, index/AP, vòng đời, bảo mật, transaction, migration); quyết định mở rộng hoặc ngoại lệ quy ước ghi ADR nháp; điểm chưa rõ ghi `OQ-NN`.

## 5. Checklist

**Nghiệp vụ và mô hình**
- [ ] Mọi thực thể, bảng truy ra FR/BR; mọi giả định có `OQ-NN`.
- [ ] Bảng `AP-NN` và ước tính khối lượng đã có (hoặc ghi rõ là giả định).
- [ ] ERD khớp schema; đạt 3NF hoặc phi chuẩn hoá có lý do và cách đồng bộ.
- [ ] Không có phản mẫu: EAV, liên kết đa hình không FK, cột chứa danh sách, bảng "để dành".

**Vật lý và toàn vẹn**
- [ ] Kiểu dữ liệu đúng: tiền dùng số chính xác, thời điểm có múi giờ/UTC, Unicode đầy đủ, độ dài có căn cứ.
- [ ] Mọi bảng có PK; khoá nghiệp vụ có UNIQUE (đúng phạm vi, tính cả xoá mềm và tenant).
- [ ] FK đủ, hành vi xoá/cập nhật tường minh; BR quan trọng có ràng buộc ở CSDL.
- [ ] Tên bảng, cột, ràng buộc, index theo quy ước; tên ràng buộc tường minh.
- [ ] Ranh giới transaction, chiến lược khoá, idempotency cho thao tác ghi quan trọng.

**Hiệu năng**
- [ ] Mỗi index phục vụ ít nhất một AP; không index trùng; FK có index; composite đúng thứ tự tiền tố trái nhất.
- [ ] Điều kiện lọc của AP quan trọng dùng được index (không hàm bọc cột, không `LIKE '%x'`, không ép kiểu ngầm).
- [ ] Không `SELECT *` ở truy vấn của ứng dụng; danh sách có giới hạn, danh sách lớn phân trang keyset; không N+1.
- [ ] Cache (nếu có) truy ra AP và số liệu; không cache dữ liệu tranh chấp/tiền/secret; key có tenant/quyền khi cần; xoá key ở mọi đường ghi; TTL có jitter; fail-open; warm-up có tầng T1/T2, trigger, chạy một instance và ngân sách tải CSDL.
- [ ] Partition/sharding/phi chuẩn hoá (nếu có) có số liệu, ADR và hệ quả đã ghi.

**Bảo mật**
- [ ] Mức D0–D3 cho từng cột nhạy cảm; D3 băm hoặc mã hoá; masking ngoài production.
- [ ] Tài khoản CSDL tách vai, quyền tối thiểu; cách ly tenant (nếu có).
- [ ] Vòng đời dữ liệu: lưu giữ, lưu trữ, huỷ, xoá theo yêu cầu.

**Migration**
- [ ] Có quay lui hoặc lý do + cách khôi phục; không sửa migration đã chạy ở môi trường dùng chung.
- [ ] Tương thích với phiên bản ứng dụng đang chạy; mức khoá và thời gian chạy đã ghi; backfill theo lô.
- [ ] Đã chạy lên/lui/lên trên CSDL sạch, thử ca âm ràng buộc, EXPLAIN cho AP quan trọng (hoặc not-run kèm lý do).
- [ ] database-design.md đã cập nhật; không tạo báo cáo schema song song.

## 6. Việc không được làm

- Theo database rules (migration, dữ liệu production). AI không chạy migration trên production và không truy cập CSDL production.
- Sinh SQL trước khi phân tích nghiệp vụ và mẫu truy cập; tự đặt bản số quan hệ, khoá nghiệp vụ hay quy tắc lưu giữ khi tài liệu chưa nói.
- Bỏ hoặc nới ràng buộc để lách lỗi; chuyển BR từ CSDL lên ứng dụng chỉ để migration chạy được.
- Thêm index "phòng khi cần"; partition, sharding hay phi chuẩn hoá khi chưa có số liệu và ADR.
- Xoá hoặc đổi tên cột/bảng khi chưa phân tích tác động lên code, báo cáo, tích hợp và dữ liệu hiện có.
- Đưa dữ liệu thật (D2/D3) vào seed, ví dụ, prompt hay kết quả EXPLAIN dán vào tài liệu.
- Dùng tính năng riêng của một hệ quản trị khác với hệ quản trị đã chốt; bịa cú pháp hoặc tính năng không có ở phiên bản đang dùng.

## 7. Tiêu chí hoàn thành (DoD)

- Phân tích nghiệp vụ, bảng `AP-NN`, ERD, danh sách bảng, ràng buộc ↔ BR, index ↔ AP, bảo mật, vòng đời đã ghi trong database-design.md.
- Migration (chế độ triển khai) đã có, đã chạy lên/lui/lên trên CSDL sạch; ca âm ràng buộc và EXPLAIN cho AP quan trọng có bằng chứng.
- Quyết định mở rộng hoặc ngoại lệ quy ước có ADR nháp; câu hỏi mở đã ghi.
- Người duyệt: Kiến trúc sư; thêm Security khi có migration, tiền hoặc dữ liệu cá nhân. Chỉ họ chuyển sang Approved.

## 8. Báo cáo bàn giao

1. Chế độ (phác thảo/triển khai), hệ quản trị và phiên bản, phạm vi nghiệp vụ.
2. Tóm tắt phân tích: thực thể, quy tắc bất biến, giả định và `OQ-NN`.
3. Mẫu truy cập `AP-NN` và ước tính khối lượng.
4. ERD và danh sách bảng (module sở hữu, mức D).
5. Quyết định thiết kế đáng chú ý kèm lý do và phương án đã loại (kiểu khoá, mẫu mô hình, phi chuẩn hoá, partition…).
6. Ràng buộc ↔ BR; index ↔ AP.
7. Cache (nếu có): key, AP, TTL, sự kiện xoá, chống dồn tải, tầng warm-up.
8. Bảo mật: cột D2/D3, mã hoá, tài khoản và quyền, cách ly tenant.
9. Migration: danh sách file, thứ tự phát hành, mức khoá/thời gian chạy, cách quay lui, rủi ro dữ liệu.
10. Bằng chứng kiểm chứng (lệnh, kết quả; not-run kèm lý do).
11. Người cần duyệt và ADR cần quyết.
