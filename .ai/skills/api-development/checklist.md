# API Development – Checklist bổ sung

> Bổ sung cho SKILL.md; không lặp lại quy trình. Dùng khi cần soát nhanh các điểm dễ sót.

## Ca test nên phủ
- [ ] Thành công · đầu vào sai/thiếu · chưa xác thực · sai quyền.
- [ ] Truy cập tài nguyên của người khác · vi phạm business rule · lỗi tương tác DB.
- Mã HTTP theo ánh xạ trong error-handling.md; không cố định trong checklist này.

## Điểm dễ sót
- [ ] Phân trang/sắp xếp/lọc đúng contract (nếu endpoint danh sách).
- [ ] Idempotency khi contract yêu cầu.
- [ ] Response không trả trường nhạy cảm ngoài contract.
- [ ] Log không chứa dữ liệu nhạy cảm.
