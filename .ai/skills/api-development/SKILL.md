---
name: api-development
description: Cài đặt hoặc sửa endpoint API backend đúng contract đã Approved trong api-design.md, gồm validation, guard phân quyền, ánh xạ lỗi, test và báo cáo bàn giao.
---

# API Development Skill

## 1. Mục tiêu

Hiện thực endpoint đúng contract đã Approved: validate đầu vào, áp guard phân quyền, trả lỗi theo ánh xạ chuẩn, có test và bằng chứng. Không tự tạo hay đổi contract.

## 2. Cổng vào

Dừng và ghi `open-questions.md` (OQ-<NN>) nếu thiếu một trong các điều kiện:
- FR có AC (acceptance-criteria.md) đã duyệt.
- Contract endpoint ở trạng thái Approved trong api-design.md.
- Schema liên quan đã có (database-design.md); chưa có thì chuyển skill `database-design`.

## 3. Đầu vào

- FR, acceptance-criteria.md, business-rules.md
- api-design.md (contract), database-design.md, module-design.md
- error-handling.md (ánh xạ lỗi), security-standards.md
- Mã nguồn API hiện có

## 4. Quy trình

1. **Đọc**: FR/AC, business rule, contract; xác định actor và yêu cầu quyền.
2. **Đối chiếu contract**: so khớp yêu cầu với contract Approved trong api-design.md. Thiếu hoặc mâu thuẫn thì dừng, ghi OQ. Đổi contract là việc cần duyệt, không tự chế.
3. **Hiện thực**: validation đầu vào → handler mỏng gọi service → trả response/lỗi theo error-handling.md. Logic nghiệp vụ trong service thuộc `backend-development`. Theo quy ước hiện có của dự án.
4. **Phân quyền**: áp guard theo `authentication-rbac`; không tự định nghĩa quyền.
5. **Test**: gọi `unit-testing` / `integration-testing` (và `e2e-testing` nếu AC yêu cầu). Phủ: thành công, đầu vào sai, chưa xác thực, sai quyền, truy cập tài nguyên người khác, vi phạm business rule.
6. **Tự review**: chuyển `code-review`; vùng bảo mật chuyển `security-review`.
7. **Bàn giao**: theo mục 8.

## 5. Checklist

- [ ] Endpoint khớp từng chi tiết contract Approved.
- [ ] Mọi đầu vào ngoài hệ thống được validate ở backend.
- [ ] Guard phân quyền ở backend, không tin client.
- [ ] Mã lỗi/định dạng lỗi theo error-handling.md; không lộ stack trace hay dữ liệu nhạy cảm.
- [ ] Không hardcode secret.
- [ ] Đổi schema có migration và đã qua `database-design`.

## 6. Việc không được làm

- Không bịa business rule hoặc contract.
- Không bỏ qua hay nới phân quyền.
- Không sửa module không liên quan.
- Không đổi schema khi chưa có migration được duyệt.
- Yêu cầu mâu thuẫn thì dừng và hỏi.

## 7. Tiêu chí hoàn thành (DoD)

- Cổng vào thoả; endpoint khớp contract.
- Test đã chạy có bằng chứng; test skip/fail được ghi rõ.
- Checklist đạt; review hoàn tất.
- Tài liệu bị ảnh hưởng đã cập nhật hoặc ghi lại cần cập nhật.

## 8. Báo cáo bàn giao

- Endpoint đã làm/sửa và contract tham chiếu
- File thay đổi
- Test đã chạy và kết quả
- Quyết định cần duyệt, OQ còn mở
- Rủi ro còn lại
