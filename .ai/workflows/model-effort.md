# Model và effort theo loại Task

> Trạng thái: **Approved**. Sửa file này cần Task riêng và người duyệt. Chỉ nạp khi lập plan (ghi model, effort cho phiên thực thi) hoặc khi Tech Lead cấu hình.

Cột "Model · Effort" ở bảng định tuyến [task-types.md](task-types.md) §1 là mặc định cho mọi Task cùng loại. "Plan" là phiên làm bước 1–4, "thực thi" là phiên làm bước 5–7; bước 8 dùng dòng T9. Tech Lead chốt bằng cách sửa trực tiếp cột đó và điền bảng ánh xạ dưới đây; không khai báo ở nơi khác.

- **Hạng model:** M1 nhẹ (tra cứu, tóm tắt, việc theo mẫu) · M2 chuẩn (code, test, tài liệu hằng ngày) · M3 mạnh (thiết kế, review, bảo mật, sự cố).
- **Effort:** E1 thấp · E2 trung bình · E3 cao · E4 rất cao.
- Task R3, hoặc bước dùng `authentication-rbac` hay `security-review`: tối thiểu M3·E3.
- Model của phiên thấp hơn hạng yêu cầu, thiếu model đúng hạng hoặc hết hạn mức: dừng và đề nghị người đổi; không tự hạ để chạy tiếp. Plan ghi model và effort cho phiên thực thi.

**Ánh xạ sang công cụ thật** (ví dụ cho Claude Code: [agents/examples/claude-code.md](../agents/examples/claude-code.md)):

| Hạng / mức | Model hoặc tham số thật (tên · phiên bản) |
| --- | --- |
| M1 · Nhẹ | |
| M2 · Chuẩn | |
| M3 · Mạnh | |
| E1 · Thấp | |
| E2 · Trung bình | |
| E3 · Cao | |
| E4 · Rất cao | |
