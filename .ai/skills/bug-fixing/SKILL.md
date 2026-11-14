---
name: bug-fixing
description: Sửa lỗi theo Bug Report (BUG-TEMPLATE) so với yêu cầu và AC đã duyệt - tái hiện, tìm nguyên nhân gốc, sửa tối thiểu, thêm test hồi quy; dừng khi lỗi do yêu cầu sai/thiếu.
---

# Bug Fixing Skill

Sửa đúng nguyên nhân gốc của lỗi (sai khác so với yêu cầu và AC đã duyệt) bằng thay đổi tối thiểu, không gây hồi quy.

## Cổng vào

Đầu vào là Bug Report theo BUG-TEMPLATE. Thiếu một mục sau thì dừng và yêu cầu bổ sung: mã bug, FR/BR/AC bị vi phạm, Task sửa lỗi, mức nghiêm trọng, mức rủi ro.

Đọc: Bug Report, Task, FR/BR/AC liên quan, mã nguồn và test liên quan.

## Quy trình

1. **Xác định yêu cầu bị vi phạm.** AC thiếu, mơ hồ hoặc tài liệu mâu thuẫn: dừng, ghi câu hỏi mở và báo. Lỗi do yêu cầu sai thì không sửa ở đây.
2. **Tái hiện** ở local hoặc staging; che dữ liệu nhạy cảm. Không tái hiện được thì nói rõ, không tuyên bố đã tái hiện.
3. **Tìm nguyên nhân gốc**, phân biệt với triệu chứng. Không xác lập được thì dừng và báo.
4. **Đánh giá tác động:** module, vai trò, dữ liệu, bảo mật, hồi quy. Cần sửa dữ liệu production thì tách Task riêng, có duyệt.
5. **Đề xuất sửa:** nguyên nhân, cách sửa, file, rủi ro, test. Chờ duyệt trước khi sửa nếu Task R3, mức tự chủ A2, hoặc đụng phân quyền, kiến trúc, schema, contract.
6. **Viết test hồi quy** ở tầng thấp nhất tái hiện được lỗi; chạy thấy đỏ trước khi sửa.
7. **Sửa tối thiểu** đúng nguyên nhân gốc; không refactor kèm.
8. **Chạy** test hồi quy (phải xanh), cổng kiểm tra của dự án và hồi quy liên quan.

## Giới hạn

- Không che lỗi bằng cách nuốt lỗi hoặc workaround.
- Không sửa business rule.

## Hoàn thành khi

- Nguyên nhân gốc đã ghi.
- Test hồi quy đỏ trước, xanh sau, kèm output cả hai lần.
- Cổng kiểm tra và hồi quy liên quan đạt.

## Báo cáo

Điền mục "Kết quả sửa" của BUG-TEMPLATE (nguyên nhân gốc, test hồi quy). Phần còn lại ghi vào báo cáo bàn giao theo DELIVERY-REPORT-TEMPLATE.
