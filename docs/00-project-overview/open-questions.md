# Open Questions & Assumptions

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người phụ trách |  |
| Người duyệt | PO |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | vision.md, scope.md, ../01-requirements/ |

> **Mục đích.** Nơi duy nhất ghi câu hỏi mở và giả định của dự án; các tài liệu khác chỉ trỏ tới mã `OQ-<NN>`. AI gặp điểm chưa rõ thì ghi vào đây, không tự trả lời hay triển khai theo phỏng đoán.
>
> **Người quyết định:** người ghi ở cột "Người quyết" (thường là PO/BA; câu hỏi kiến trúc là Kiến trúc sư).
>
> **Điều kiện sang cổng tiếp theo:** không còn `Open` chặn phạm vi của cổng; câu hỏi còn lại có người quyết và hạn.

Trạng thái: `Open` chưa có câu trả lời · `Assumption` giả định tạm để đi tiếp, cần xác nhận (bắt buộc có Hạn rà soát ở cột Hạn) · `Closed` đã quyết (ghi quyết định và căn cứ).

| ID | Câu hỏi | Tài liệu / mã liên quan | Ảnh hưởng | Người quyết | Hạn | Trạng thái | Quyết định (khi Closed) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OQ-01 | | | | | | Open | |

## Chi tiết câu hỏi
Bắt buộc cho mọi OQ `Open` hoặc `Assumption` mà người quyết là người; đặt ngay dưới bảng. OQ chỉ xác nhận một thông tin thì chỉ cần **Bối cảnh** và **Nếu chưa quyết**. Khi `Closed`, ghi lựa chọn vào cột Quyết định và giữ phần chi tiết làm căn cứ.

**Trước khi hỏi người, AI phải tra bảng này:** OQ đã `Closed` thì áp dụng quyết định, không hỏi lại. Báo cáo, plan và backlog chỉ trỏ `OQ-<NN>`, không chép lại nội dung chi tiết.

```text
### OQ-<NN>
- Bối cảnh: <số đo, nguồn đo, ngày đo>
- Phương án:
  | | Nội dung | Được | Mất |
  | --- | --- | --- | --- |
  | A | | | |
  | B | | | |
- Đề xuất của AI: <A hoặc B> vì <lý do, tối đa 2 câu>
- Nếu chưa quyết: <việc bị chặn, hoặc "không chặn">
```
