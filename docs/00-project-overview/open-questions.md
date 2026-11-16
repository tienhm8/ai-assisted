# Open Questions & Assumptions

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | PO |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | vision.md, scope.md, ../01-requirements/ |

> **Mục đích.** Nơi duy nhất ghi câu hỏi mở và giả định của dự án; các tài liệu khác chỉ trỏ tới mã `OQ-<NN>`. AI gặp điểm chưa rõ thì ghi vào đây, không tự trả lời hay triển khai theo phỏng đoán.
>
> **Người quyết định:** người ghi ở cột "Người quyết" (thường là PO/BA; câu hỏi kiến trúc là Kiến trúc sư).
>
> **Điều kiện sang cổng tiếp theo:** không còn `Open` chặn phạm vi của cổng; câu hỏi còn lại có người quyết và hạn.

Trạng thái: `Open` chưa có câu trả lời · `Assumption` giả định tạm để đi tiếp, cần xác nhận (bắt buộc có Hạn rà soát ở cột Hạn) · `Closed` đã quyết (ghi quyết định và căn cứ).

| ID | Câu hỏi | Tài liệu / mã liên quan | Ảnh hưởng | Người quyết | Hạn | Trạng thái | Quyết định (khi Closed) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OQ-<NN> | | | | | | | |

## Chi tiết câu hỏi
Bắt buộc cho mọi OQ `Open` hoặc `Assumption` mà người quyết là người; đặt ngay dưới bảng. OQ chỉ xác nhận một thông tin thì chỉ cần **Bối cảnh** và **Nếu chưa quyết**. Khi `Closed`, ghi lựa chọn vào cột Quyết định và giữ phần chi tiết làm căn cứ.

**Trước khi hỏi người, AI phải tra bảng này:** OQ đã `Closed` thì áp dụng quyết định, không hỏi lại. Plan và báo cáo bàn giao ghi `OQ-<NN>` kèm bản tóm tắt đủ để quyết (vấn đề, phương án được/mất, đề xuất, nếu chưa quyết); backlog chỉ trỏ mã. Chi tiết và lịch sử chỉ nằm ở đây; khi `Closed`, quyết định ghi tại đây.

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

## Lịch sử thay đổi
| Ngày | Thay đổi | Lý do | Người duyệt |
| --- | --- | --- | --- |
