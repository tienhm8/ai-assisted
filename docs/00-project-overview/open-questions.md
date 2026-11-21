# Sổ câu hỏi mở cấp dự án

| Thuộc tính | Giá trị |
| --- | --- |
| Người phụ trách | BA |
| Người duyệt | PO |
| Tài liệu liên quan | vision.md, scope.md, sources/README.md, ../01-requirements/README.md, ../../.ai/guide/open-questions.md |

> **Mục đích.** Sổ chứa câu hỏi mở (`OQ-<NN>`) về vision, scope, BRQ, BRD, NFR, Epic, Goal, và câu hỏi không thuộc Module hay Feature nào. Câu hỏi về Module, Feature nằm ở sổ của chúng (xem [FR/README](../01-requirements/FR/README.md)). Mã `OQ-<NN>` duy nhất toàn dự án, tăng dần, không dùng lại.

Trạng thái: `Open` chưa có câu trả lời · `Asked` đã gửi, đang chờ · `Assumption` giả định tạm, cần xác nhận (có hạn rà soát ở cột Hạn) · `Closed` đã quyết (ghi quyết định và căn cứ).

Loại: `Input` thiếu tài liệu hoặc dữ liệu · `Clarify` nội dung nguồn mơ hồ, cần giải thích · `Decision` cần người có thẩm quyền chọn.

## Câu hỏi

Cột của bảng này cũng là mẫu cho sổ Module và sổ Feature. Câu trả lời của khách hàng: lưu thành `SRC-<NN>` ở [sources/](sources/README.md), ghi mã đó vào cột Quyết định.

| ID | Loại | Câu hỏi | Mã liên quan | Ảnh hưởng | Người quyết | Hỏi qua (người · kênh · ngày) | Hạn | Trạng thái | Quyết định (khi Closed) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OQ-<NN> | | | `SRC-<NN>` § / mã yêu cầu / `US-<MODULE>-<NN>` | | | | | | Câu trả lời + `SRC-<NN>` |

## Chi tiết câu hỏi

Bắt buộc cho OQ `Open`, `Asked` hoặc `Assumption` loại `Decision`; đặt dưới bảng. Loại `Input`, `Clarify` chỉ cần Bối cảnh và Nếu chưa quyết. Khi `Closed`, giữ phần chi tiết làm căn cứ.

```text
### OQ-<NN>
- Bối cảnh: <số đo, nguồn, ngày>
- Phương án:
  | | Nội dung | Được | Mất |
  | --- | --- | --- | --- |
  | A | | | |
  | B | | | |
- Đề xuất: <A hoặc B> vì <lý do>
- Nếu chưa quyết: <việc bị chặn, hoặc "không chặn">
```
