# Open Questions & Assumptions

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | PO |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | vision.md, scope.md, ../01-requirements/ |

> **Mục đích.** Sổ chung của câu hỏi mở, giả định và đầu vào còn thiếu: ghi câu hỏi **cấp dự án** và giữ **mục lục** mọi `OQ-<NN>` của dự án (mã, sổ chứa, trạng thái). Các tài liệu khác chỉ trỏ tới mã `OQ-<NN>`. AI gặp điểm chưa rõ thì ghi vào đúng sổ (bảng dưới), không tự trả lời hay triển khai theo phỏng đoán.
>
> **Ba cấp sổ** (mỗi câu hỏi nằm ở đúng một sổ, theo đối tượng nó hỏi):
>
> | Sổ | Đường dẫn | Chứa câu hỏi về |
> | --- | --- | --- |
> | Sổ chung (file này) | `docs/00-project-overview/open-questions.md` | Vision, scope, BRQ (yêu cầu nghiệp vụ), BRD, NFR, Epic, Goal; đồng thời là mục lục toàn bộ OQ |
> | Sổ Module | `docs/01-requirements/FR/<MODULE>/open-questions.md` | Câu hỏi chung của một Module |
> | Sổ Feature | `docs/01-requirements/FR/<MODULE>/<FEAT-NN>-<tên>/open-questions.md` | Feature, FR, BR, AC thuộc Feature đó |
>
> User Story không có thư mục riêng: câu hỏi về User Story nằm ở sổ của Feature hoặc Module liên quan, mã `US-<MODULE>-<NN>` ghi ở cột "Mã liên quan". Tên thư mục Feature dạng có tên, không dấu, chữ thường, nối bằng gạch ngang (ví dụ `FEAT-03-dang-ky-work-study`).
>
> **Quy tắc mã và mục lục:** mã `OQ-<NN>` duy nhất toàn dự án, chỉ cấp ở sổ chung; sổ con dùng cùng mã, không đánh số riêng. Mục lục bên dưới **bắt buộc cập nhật** mỗi khi thêm OQ hoặc đổi trạng thái; sổ con và mục lục phải khớp.
>
> **Người quyết định:** người ghi ở cột "Người quyết" (thường là PO/BA; câu hỏi kiến trúc là Kiến trúc sư).
>
> **Điều kiện sang cổng tiếp theo:** không còn `Open` chặn phạm vi của cổng; câu hỏi còn lại có người quyết và hạn.

Trạng thái: `Open` chưa có câu trả lời · `Asked` đã gửi cho người trả lời, đang chờ · `Assumption` giả định tạm để đi tiếp, cần xác nhận (bắt buộc có Hạn rà soát ở cột Hạn) · `Closed` đã quyết (ghi quyết định và căn cứ).

Loại: `Input` thiếu tài liệu hoặc dữ liệu (xin bổ sung, không cần quyết) · `Clarify` nội dung nguồn mơ hồ, mâu thuẫn, cần người trả lời giải thích · `Decision` cần người có thẩm quyền chọn phương án.

## Mục lục OQ toàn dự án

Mỗi OQ một dòng, kể cả OQ nằm ở sổ con. Chưa có OQ nào.

| ID | Sổ chứa | Tóm tắt | Trạng thái |
| --- | --- | --- | --- |
| OQ-<NN> | chung · `<MODULE>` · `<MODULE>/<FEAT-NN>-<tên>` | | |

## Câu hỏi cấp dự án (sổ chung)

Cột của bảng này cũng là mẫu cho sổ Module và sổ Feature; "Mã liên quan" ghi mã yêu cầu hoặc `US-<MODULE>-<NN>`.

| ID | Loại | Câu hỏi | Tài liệu / mã liên quan | Ảnh hưởng | Người quyết | Hỏi qua (người · kênh · ngày) | Hạn | Trạng thái | Quyết định (khi Closed) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OQ-<NN> | | | `SRC-<NN>` § / mã yêu cầu / `US-<MODULE>-<NN>` | | | | | | Câu trả lời + `SRC-<NN>` biên bản |

### Hỏi khách hàng qua đầu mối

Dự án có Đại diện khách hàng ([PROJECT.md](../../PROJECT.md) §5) thì AI không hỏi khách hàng trực tiếp:

1. AI ghi OQ (`Open`) vào đúng sổ và thêm dòng vào mục lục, soạn **gói câu hỏi** theo mẫu dưới, gom các OQ cùng chủ đề (thường theo Feature, có thể từ nhiều sổ), gửi đầu mối (BA hoặc PO nội bộ).
2. Đầu mối rà, gửi khách hàng, ghi cột "Hỏi qua", chuyển `Asked` (cập nhật cả sổ con và mục lục).
3. Khách hàng trả lời: đầu mối lưu câu trả lời vào [sources/](sources/README.md) thành `SRC-<NN>`. AI cập nhật OQ: `Input`, `Clarify` → `Closed` kèm mã SRC; `Decision` → `Closed` chỉ khi người quyết (cột Người quyết) xác nhận.
4. Câu trả lời sinh câu hỏi mới: mở OQ mới, không sửa OQ cũ.
5. Mọi lần đổi trạng thái đều cập nhật mục lục ở sổ chung trong cùng thay đổi.

```text
Gửi: <tên khách hàng> · Qua: <đầu mối> · Ngày: <...> · Hạn trả lời: <...>
Chủ đề: <ví dụ: Quy trình đăng ký Work study>

1. [OQ-<NN> · Xin bổ sung tài liệu] Cần: <tài liệu gì> · Để làm: <dùng vào việc gì> · Nếu chưa có: <việc bị chặn>
2. [OQ-<NN> · Làm rõ] Trong <SRC-<NN> §/trang>, "<trích nguyên văn>" có nghĩa là <cách hiểu A> hay <cách hiểu B>?
3. [OQ-<NN> · Cần quyết] <câu hỏi> · Phương án: A <...>, B <...> · Đề xuất: <A/B, lý do> · Nếu chưa quyết: <...>
```

Câu hỏi gửi khách hàng viết bằng ngôn ngữ nghiệp vụ, không dùng mã nội bộ (FR, mức rủi ro, mức tự chủ…) ngoài mã OQ và SRC để đối chiếu.

## Chi tiết câu hỏi
Đặt ở sổ chứa OQ đó (sổ chung, sổ Module hoặc sổ Feature). Bắt buộc cho mọi OQ `Open`, `Asked` hoặc `Assumption` loại `Decision`; đặt ngay dưới bảng. OQ loại `Input`, `Clarify` hoặc chỉ xác nhận một thông tin thì chỉ cần **Bối cảnh** và **Nếu chưa quyết**. Khi `Closed`, ghi lựa chọn vào cột Quyết định và giữ phần chi tiết làm căn cứ.

**Trước khi hỏi người, AI phải tra:** mục lục ở sổ chung, rồi mở sổ con chứa OQ liên quan (Module, Feature). OQ đã `Closed` thì áp dụng quyết định, không hỏi lại. Plan và báo cáo bàn giao ghi `OQ-<NN>` kèm bản tóm tắt đủ để quyết (vấn đề, phương án được/mất, đề xuất, nếu chưa quyết); task-backlog chỉ trỏ mã. Chi tiết và lịch sử chỉ nằm ở sổ chứa OQ; khi `Closed`, quyết định ghi tại sổ đó và trạng thái cập nhật ở mục lục.

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
