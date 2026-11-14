---
name: api-development
description: Cài đặt hoặc sửa endpoint API backend đúng contract đã Approved trong api-design.md, gồm validation, guard phân quyền, ánh xạ lỗi, danh sách ca cần test và báo cáo bàn giao.
---

# API Development Skill

Hiện thực endpoint đúng contract đã Approved: validate đầu vào, áp guard phân quyền, trả lỗi theo ánh xạ chuẩn. Không tự tạo hay đổi contract.

## Cổng vào

Ngoài `project-rules` 2, cần: contract của endpoint trong api-design; schema liên quan trong database-design (chưa có thì dừng và báo).

Nguồn chính: plan; mã API hiện có.
Plan thiếu thì tra đúng mục, không đọc cả file: api-design §1.2 Chi tiết API (endpoint liên quan), §3.2 Quy ước chung, §4 Authentication & Authorization; database-design §3.3 Chi tiết bảng (bảng liên quan); module-design §5 Ranh giới và quyền sở hữu; error-handling §3 Mã lỗi, §5 Phản hồi lỗi API; security-standards §5 Kiểm tra đầu vào, §8 Bảo mật API.

## Quy trình

1. **Đọc** FR/AC, business rule, contract; xác định actor và yêu cầu quyền.
2. **Đối chiếu contract** với yêu cầu. Thiếu hoặc mâu thuẫn thì dừng, ghi câu hỏi mở; đổi contract cần duyệt.
3. **Hiện thực** theo quy ước hiện có của dự án: validation đầu vào → handler mỏng gọi service → trả response hoặc lỗi theo error-handling. Logic nghiệp vụ nằm trong service, thuộc `backend-development`.
4. **Phân quyền:** áp guard đã có theo ma trận quyền; không tự định nghĩa quyền.
5. **Ca cần test:** ghi vào plan §5, kèm tầng (unit, integration; e2e nếu AC yêu cầu). Phủ: thành công, đầu vào sai hoặc thiếu, chưa xác thực, sai quyền, truy cập tài nguyên của người khác, vi phạm business rule, lỗi tương tác CSDL.

## Hoàn thành khi

- Endpoint khớp từng chi tiết của contract, kể cả phân trang, sắp xếp, lọc và idempotency nếu contract có.
- Mã lỗi và định dạng lỗi theo error-handling; response không trả trường nhạy cảm ngoài contract.
- Ca cần test ở bước 5 đã ghi vào plan.

## Báo cáo

Ghi vào báo cáo bàn giao của Task: endpoint đã làm hoặc sửa và contract tham chiếu.
