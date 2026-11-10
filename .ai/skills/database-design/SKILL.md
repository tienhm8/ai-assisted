---
name: database-design
description: Thiết kế, đánh giá và thay đổi lược đồ cơ sở dữ liệu (thực thể, quan hệ, ràng buộc, index, migration) dựa trên yêu cầu và kiến trúc đã duyệt; ghi vào database-design.md.
---

# Database Design Skill

## 1. Mục tiêu

Thiết kế cấu trúc dữ liệu đúng, nhất quán, hiệu năng đủ dùng và bảo trì được. AI chỉ soạn ở trạng thái Draft/Proposed.

## 2. Cổng vào

Cần FR đã qua cổng (có AC) và kiến trúc liên quan đã Approved. Chưa đạt thì dừng, ghi open-questions.md (`OQ-NN`).

## 3. Đầu vào

FR và BR đã duyệt, schema hiện có, kiến trúc, nhu cầu dữ liệu của API, yêu cầu lưu trữ dữ liệu, mức dữ liệu D0–D3 (theo quy định của dự án).

## 4. Quy trình

1. **Thực thể:** chính, hỗ trợ, tra cứu, giao dịch, quan hệ, audit; mỗi thực thể truy ra FR/BR.
2. **Thuộc tính:** tên, kiểu, nullability, mặc định, ràng buộc, ý nghĩa, mức dữ liệu D0–D3. Bảng đơn giản không cần mô tả lặp từng cột: schema/migration trong mã nguồn là nguồn chuẩn; database-design.md chỉ giữ ERD, quan hệ, ràng buộc và quyết định đáng chú ý.
3. **Quan hệ:** 1-1, 1-n, n-n; khoá chính, khoá ngoại, hành vi tham chiếu, unique.
4. **Toàn vẹn:** NOT NULL, UNIQUE, CHECK, FK, mặc định, ranh giới transaction; không chỉ dựa vào validate phía giao diện.
5. **Chuẩn hoá:** mặc định đạt 1NF–3NF; chỉ phi chuẩn hoá khi có số liệu đo hoặc yêu cầu kiến trúc, và ghi lý do.
6. **Index:** theo truy vấn thực tế (lọc, join, sắp xếp, composite, unique); tránh index thừa.
7. **Migration:** mỗi thay đổi schema có migration, trạng thái DB mong đợi, biến đổi dữ liệu (nếu có), lưu ý triển khai; theo database rules.
8. **Hiệu năng:** mẫu truy vấn, N+1, quét bảng lớn, phân trang, thời lượng transaction.
9. **Bảo mật:** quyền tối thiểu, dữ liệu nhạy cảm (D2–D3), thời gian lưu, sao lưu, audit.

## 5. Checklist

- [ ] Đầu ra ghi vào database-design.md; file migration nằm trong mã nguồn; không tạo báo cáo schema song song.
- [ ] Mọi thực thể ánh xạ tới yêu cầu.
- [ ] Khoá chính, khoá ngoại, unique, nullability, kiểu dữ liệu phù hợp.
- [ ] Index có truy vấn hỗ trợ.
- [ ] Đã đánh giá tác động lên dữ liệu hiện có và mức dữ liệu D0–D3.
- [ ] Đã cập nhật database-design.md.

## 6. Việc không được làm

- Theo database rules (migration, dữ liệu production). AI không chạy migration trên production.
- Không xoá cột khi chưa phân tích tác động; không bỏ ràng buộc để lách lỗi; không bịa quan hệ; không để lộ dữ liệu nhạy cảm không cần thiết.
- Dữ liệu lịch sử nghiệp vụ không xoá khi chưa có chính sách lưu trữ.

## 7. Tiêu chí hoàn thành (DoD)

- ERD và ràng buộc đã ghi; index có lý do; migration đã chuẩn bị.
- Đã kiểm: chạy migration thử trên DB sạch (không phải production) và kiểm ràng buộc hoạt động đúng.
- Người duyệt: Kiến trúc sư; thêm Security khi có migration, tiền hoặc dữ liệu cá nhân. Chỉ họ chuyển sang Approved.

## 8. Báo cáo bàn giao

Nêu: thực thể và schema thay đổi, migration, rủi ro dữ liệu, ảnh hưởng hiệu năng, người cần duyệt.
