# Ba cấp sổ câu hỏi mở

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người duyệt | Tech Lead |
| Tài liệu liên quan | ../../docs/00-project-overview/vision.md, ../../docs/00-project-overview/scope.md, ../../docs/01-requirements/README.md, ../../docs/01-requirements/FR/README.md |

> **Mục đích.** Giải thích cách chọn sổ chứa cho một câu hỏi mở (`OQ-<NN>`): ba cấp sổ, câu hỏi chạm nhiều nơi thì nằm ở đâu, và đặt tên thư mục Feature thế nào. Tài liệu cho người đọc; AI không nạp file này khi làm Task.

## 1. Ba cấp sổ

Mỗi câu hỏi nằm ở đúng một sổ chứa, theo đối tượng nó hỏi. Nơi khác liên quan chỉ được nhắc ở cột "Mã liên quan".

| Sổ | Đường dẫn | Chứa câu hỏi về |
| --- | --- | --- |
| Sổ Module | `docs/01-requirements/FR/<MODULE>/open-questions.md` | Câu hỏi chung của một Module |
| Sổ Feature | `docs/01-requirements/FR/<MODULE>/<FEAT-NN>-<tên>/open-questions.md` | Feature, FR, BR, AC thuộc Feature đó |

## 2. Chọn sổ khi câu hỏi chạm nhiều nơi

- Chạm từ hai Feature trở lên trong cùng Module → sổ Module.
- BR (mã theo Module, nằm ở `business-rules.md`) áp cho FR của nhiều Feature → sổ Module.
- BR chỉ phục vụ một Feature → sổ Feature.

Các Feature, Module, US liên quan ghi ở cột "Mã liên quan" của sổ đã chọn.

## 3. Câu hỏi về User Story

User Story không có thư mục riêng. Câu hỏi về User Story nằm ở sổ của Feature hoặc Module liên quan, mã `US-<MODULE>-<NN>` ghi ở cột "Mã liên quan".

## 4. Tên thư mục Feature

Tên thư mục Feature dạng có tên, không dấu, chữ thường, nối bằng gạch ngang, ví dụ `FEAT-03-dang-ky-work-study`. Quy tắc tạo thư mục Feature nằm ở [FR/README](../../docs/01-requirements/FR/README.md).
