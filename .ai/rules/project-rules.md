# Project Rules

> Trạng thái: **Draft**. Rule bắt buộc cho AI trong mọi phiên làm việc, không phụ thuộc dự án.
> Gặp mâu thuẫn hoặc rule không đủ để quyết định: dừng phần bị ảnh hưởng và hỏi người có thẩm quyền, không tự chọn.

1. Trước khi làm: đọc Task và các tài liệu Task chỉ tới; không nạp cả dự án.
2. Chưa có đặc tả và tiêu chí nghiệm thu (AC), hoặc chưa có thiết kế Approved: không code; dừng và báo.
3. Không tự nghĩ ra nghiệp vụ. Điểm chưa rõ và giả định ghi vào danh sách câu hỏi mở (`OQ-<NN>`); không tự trả lời và không triển khai theo phỏng đoán.
4. Không tự chuyển trạng thái tài liệu sang Approved; chỉ người có thẩm quyền làm việc này. Không tự duyệt thay đổi do chính mình viết.
5. Không đổi kiến trúc đã Approved khi chưa được duyệt; đề xuất bằng ADR nháp.
6. Không thêm dependency mới khi chưa ghi lý do trong PR và được duyệt.
7. Mọi thay đổi truy vết được tới một Task đã duyệt; chỉ sửa trong phạm vi Task, theo cấu trúc thư mục hiện có.
8. Tuân thủ mức tự chủ của Task và bản đồ vùng 🟢🟡🔴 của dự án; không tự nâng mức. Vùng 🔴 cần Task riêng và người duyệt.
9. Đổi hành vi hoặc kiến trúc thì cập nhật tài liệu liên quan trong cùng thay đổi.
10. Báo cáo bàn giao nêu rõ giả định, câu hỏi chưa giải quyết và kết quả kiểm tra thật.

## Thang dùng chung

**Mức rủi ro (R)** do Task gán; AI không tự hạ.
- R1: thay đổi cục bộ, dễ hoàn tác, không chạm dữ liệu hay quyền.
- R2: ảnh hưởng nhiều module hoặc hợp đồng API nội bộ.
- R3: chạm phân quyền, tiền, dữ liệu cá nhân, migration hoặc bảo mật; cần hai người duyệt.

**Mức nghiêm trọng (severity)** của lỗi hoặc phát hiện review:
- Critical: mất dữ liệu, lộ bảo mật, hệ thống ngừng hoạt động; chặn phát hành.
- High: sai nghiệp vụ hoặc hỏng chức năng chính, không có cách né; chặn phát hành.
- Medium: hỏng chức năng phụ hoặc có cách né; sửa trong kế hoạch gần.
- Low: lỗi nhỏ, thẩm mỹ, cải tiến; sửa khi thuận tiện.

**Mức dữ liệu (D):** D0 công khai; D1 nội bộ; D2 nhạy cảm (nghiệp vụ, tài chính nội bộ); D3 secret, token, dữ liệu cá nhân.
