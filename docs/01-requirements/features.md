# Function / Feature

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người duyệt | PO/BA |
| Tài liệu liên quan | BRD.md, FR/, ../../.ai/guide/work-model.md, ../04-project-management/product-backlog.md |

> **Mục đích.** Đặc tả sản phẩm ở mức chức năng: hệ thống cần có chức năng gì. Mỗi Feature được chi tiết hoá bằng nhiều FR (bảng FR ghi Feature của từng FR). Khái niệm và liên kết: [work-model](../../.ai/guide/work-model.md).
>
> **Người duyệt:** PO/BA.

Mã `FEAT-<NN>`. Một Feature có thể đáp ứng nhiều BRQ, một BRQ có thể liên quan nhiều Feature: ghi danh sách mã ở cột BRQ. Tra FR của một Feature thì lọc cột "Feature" của bảng FR; tra User Story chạm Feature thì lọc [product-backlog](../04-project-management/product-backlog.md) §2.

Thêm Feature mới thì trong cùng thay đổi tạo thư mục `FR/<MODULE>/<FEAT-NN>-<tên>/` (chỉ có `open-questions.md` nếu chưa có FR) và thêm một dòng vào bảng tổng hợp ở [FR/README](FR/README.md).

| ID | Tên | Mô tả ngắn | BRQ | Module | Ưu tiên |
| --- | --- | --- | --- | --- | --- |
| FEAT-<NN> |  |  | BRQ-<NN>, … | | |

Ưu tiên: MoSCoW. Trạng thái hoàn thành không ghi ở đây: suy ra từ trạng thái FR. Điểm chưa rõ ghi `OQ-<NN>`, không đoán.

## Lịch sử thay đổi
| Ngày | Feature | Thay đổi | Lý do | Người duyệt |
| --- | --- | --- | --- | --- |
