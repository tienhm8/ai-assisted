---
name: api-development
description: Cài đặt hoặc sửa endpoint API backend đúng contract đã Approved trong api-design.md, gồm validation, guard phân quyền, ánh xạ lỗi, test và báo cáo bàn giao.
---

# API Development Skill

Hiện thực endpoint đúng contract đã Approved: validate đầu vào, áp guard phân quyền, trả lỗi theo ánh xạ chuẩn. Không tự tạo hay đổi contract.

## Cổng vào

Thiếu một điều kiện thì dừng và ghi câu hỏi mở:
- FR có AC đã duyệt.
- Contract của endpoint ở trạng thái Approved trong api-design.
- Schema liên quan đã có trong database-design; chưa có thì chuyển `database-design`.

Đọc: FR, AC, business-rules; api-design, database-design, module-design; error-handling, security-standards; mã API hiện có.

## Quy trình

1. **Đọc** FR/AC, business rule, contract; xác định actor và yêu cầu quyền.
2. **Đối chiếu contract** với yêu cầu. Thiếu hoặc mâu thuẫn thì dừng, ghi câu hỏi mở; đổi contract cần duyệt.
3. **Hiện thực** theo quy ước hiện có của dự án: validation đầu vào → handler mỏng gọi service → trả response hoặc lỗi theo error-handling. Logic nghiệp vụ nằm trong service, thuộc `backend-development`.
4. **Phân quyền:** áp guard theo `authentication-rbac`; không tự định nghĩa quyền.
5. **Test** bằng `unit-testing`, `integration-testing` (và `e2e-testing` nếu AC yêu cầu). Phủ: thành công, đầu vào sai hoặc thiếu, chưa xác thực, sai quyền, truy cập tài nguyên của người khác, vi phạm business rule, lỗi tương tác CSDL.

## Hoàn thành khi

- Endpoint khớp từng chi tiết của contract, kể cả phân trang, sắp xếp, lọc và idempotency nếu contract có.
- Mã lỗi và định dạng lỗi theo error-handling; response không trả trường nhạy cảm ngoài contract.
- Các ca test ở bước 5 đã chạy, có output thật.

## Báo cáo

Ghi vào báo cáo bàn giao của Task: endpoint đã làm hoặc sửa và contract tham chiếu.
