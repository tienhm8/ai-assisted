# Tài liệu nguồn

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách | BA |
| Người duyệt (dự án) | PO |
| Tài liệu liên quan | ../open-questions.md, ../vision.md, ../../01-requirements/README.md, ../../../PROJECT.md §3 |

> **Mục đích.** Nơi lưu và đánh mã tài liệu đầu vào do khách hàng, PO hoặc bên liên quan cung cấp (quy trình nghiệp vụ, biểu mẫu, biên bản họp, câu trả lời làm rõ). Yêu cầu trong `docs/` trỏ về mã `SRC-<NN>` để truy được nguồn. AI chỉ đọc tài liệu đã có trong bảng dưới, không lấy nguồn ngoài bảng.

## 1. Quy tắc

- **Mỗi tài liệu một mã** `SRC-<NN>`, tăng dần, không dùng lại. Bản sửa của cùng tài liệu: mã mới, ghi "Thay cho SRC-<NN>".
- **Lưu file** trong thư mục này, tên `SRC-<NN>-<tên-ngắn>.<đuôi>`. Tài liệu không được lưu vào repo (dung lượng, hợp đồng): ghi đường dẫn nơi lưu ở cột "Vị trí".
- **Ẩn danh trước khi lưu và trước khi đưa vào AI.** Tài liệu có dữ liệu mức D3 (bí mật, dữ liệu cá nhân như họ tên, mã sinh viên, số điện thoại, hoàn cảnh tài chính) thì người cung cấp hoặc BA thay bằng dữ liệu giả, giữ nguyên cấu trúc. Chưa ẩn danh thì ghi "Chưa ẩn danh" ở cột Mức dữ liệu; AI không mở file đó.
- **Kết quả khách hàng duyệt tài liệu là nguồn.** Ghi tài liệu nào, phiên bản/commit nào, duyệt hay yêu cầu sửa, ngày; Đầu mối dùng mã đó khi chuyển `Approved`.
- **Câu trả lời của khách hàng là nguồn.** Trả lời qua chat, email, họp cho một `OQ-<NN>` thì chép nguyên văn (đã ẩn danh) vào một tài liệu biên bản, đánh `SRC-<NN>`, rồi ghi mã đó vào cột Quyết định của OQ.
- **Tài liệu nguồn không phải yêu cầu.** Nội dung chỉ thành FR, BR khi đã qua phân tích và người duyệt đồng ý.

## 2. Danh mục

| Mã | Tên tài liệu | Loại | Người cung cấp | Ngày nhận | Vị trí | Mức dữ liệu | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-<NN> | | Quy trình / Biểu mẫu / Biên bản / Trả lời OQ / Kết quả duyệt / Khác | | | | D0–D2, hoặc "Chưa ẩn danh" | |

<!-- Điền theo từng dự án: mỗi tài liệu nhận được một dòng; xoá dòng mẫu. -->
