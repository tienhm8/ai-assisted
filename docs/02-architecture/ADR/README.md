# Architecture Decision Records

Lưu các quyết định kiến trúc có ảnh hưởng lớn và lý do chọn. ADR là nơi duy nhất ghi **vì sao** chọn; các tài liệu thiết kế khác chỉ ghi kết quả và trỏ về `ADR-<NNNN>`.

## Khi nào tạo ADR
- Thay đổi phong cách kiến trúc.
- Chọn hoặc thay đổi database.
- Chọn hoặc thay đổi công nghệ cốt lõi.
- Thay đổi cách giao tiếp giữa module, hoặc thay đổi ranh giới module.
- Thay đổi mô hình bảo mật (xác thực, phân quyền).
- Thay đổi mô hình triển khai.
- Thay đổi API phá vỡ tương thích.

Quyết định nhỏ, dễ đảo ngược, nằm gọn trong một module thì ghi ở tài liệu thiết kế tương ứng, không cần ADR.

## Đặt tên
Mã `ADR-<NNNN>` (số tăng dần, không tái sử dụng), file `ADR-<NNNN>-<slug>.md`. Ví dụ: `ADR-0001-use-postgresql.md`.

## Trạng thái
| Trạng thái | Ý nghĩa |
| --- | --- |
| Proposed | Đang đề xuất (AI hoặc người soạn nháp), chưa có hiệu lực |
| Approved | Kiến trúc sư đã duyệt, có hiệu lực |
| Rejected | Đã xem xét và không chọn; giữ lại để không bàn lại từ đầu |
| Superseded by ADR-… | Bị thay thế bởi ADR mới |
| Deprecated | Không còn áp dụng, không có ADR thay thế |

Người duyệt (Kiến trúc sư, và Security khi thuộc diện cần): xem [README](../README.md). Chỉ người duyệt chuyển sang Approved; AI chỉ soạn ở trạng thái Proposed. ADR bị thay thế chuyển `Superseded by ADR-…`, không xoá.

Proposed tương ứng Draft / In Review trong vòng đời tài liệu chung ([README gốc](../../../README.md), mục "Quy ước làm việc với tài liệu"). ADR dùng thêm Rejected và Superseded vì cần giữ lại quyết định đã loại hoặc đã bị thay.

## Cách tạo
1. Sao chép [_template.md](_template.md) thành `ADR-<NNNN>-<slug>.md`.
2. Điền các mục; nêu ít nhất hai phương án, kể cả phương án "không làm gì" nếu phù hợp.
3. Thêm một dòng vào bảng bên dưới (nơi duy nhất liệt kê ADR). Tài liệu thiết kế bị ảnh hưởng chỉ ghi kết quả và trỏ về `ADR-<NNNN>` tại chỗ liên quan.

## Danh mục ADR
| ADR | Tiêu đề | Trạng thái | Ngày |
| --- | --- | --- | --- |
