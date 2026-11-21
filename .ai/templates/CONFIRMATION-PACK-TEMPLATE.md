<!-- internal:start -->
# Mẫu Gói xác nhận yêu cầu (gửi khách hàng)

> **Dùng khi:** cần khách hàng xem và chốt phạm vi, quy trình, màn hình, quy tắc, câu hỏi trước khi qua cổng Yêu cầu. AI soạn `Draft` từ `SRC-<NN>`, BA (Đầu mối) rà rồi xuất file gửi khách hàng.
>
> **Nơi lưu:** `docs/00-project-overview/confirmation-packs/GXN-<NN>-<tên-ngắn>.md`, đăng ký ở bảng Danh mục trong [README của thư mục](../../docs/00-project-overview/confirmation-packs/README.md).
>
> **Xuất file:** `python3 -I .ai/scripts/export-pack.py docs/00-project-overview/confirmation-packs/GXN-<NN>-<tên-ngắn>.md --pdf` tạo một file HTML tự chứa (kèm PDF nếu máy có Chrome). Phần nằm giữa hai dấu `internal` (như khối này) bị bỏ khi xuất.
>
> **Viết cho khách hàng:** ngôn ngữ nghiệp vụ, không mã nội bộ (FR, mức rủi ro, mức tự chủ…). Chỉ giữ mã `OQ-<NN>` và `SRC-<NN>` để đối chiếu. Chưa ẩn danh thì không đưa dữ liệu thật vào ví dụ: dùng tên và số giả.
>
> **Mỗi gói một chủ đề** (một quy trình hoặc một nhóm màn hình), để khách hàng trả lời được trong một lượt.

## Cú pháp wireframe

Mỗi màn hình là một khối mã mở bằng ba dấu huyền và chữ `wireframe`. Mỗi dòng `loại: nội dung`.

| Dòng | Ý nghĩa |
| --- | --- |
| `screen:` `id:` `role:` `device:` `style:` | Tên màn hình, mã (`M-01`), người dùng, `desktop` hoặc `mobile`, `wireframe` (bản phác trắng đen) hoặc `mockup` (có màu) |
| `topbar: Tên ; mục ; mục` | Thanh trên cùng |
| `tabs: A* ; B ; C` · `steps: A > B* > C` | Thẻ và các bước; dấu `*` là mục đang chọn |
| `title:` `subtitle:` `text:` `alert:` `divider:` `spacer:` | Tiêu đề, chữ, cảnh báo, kẻ ngang, khoảng trống |
| `input:` `select:` `date:` `textarea:` `upload:` | Ô nhập. Thêm ` = giá trị mẫu`; dấu `*` cuối tên là bắt buộc; `[auto]` là hệ thống tự điền |
| `checkbox: [x] Nội dung` · `radio: (o) Nội dung` | Ô chọn |
| `button: Tên (primary)` | Nút; `(primary)` nút chính, `(danger)` nút nguy hiểm |
| `badge: Chờ duyệt (warn)` | Nhãn trạng thái; `ok`, `warn`, `bad` |
| `table: Cột 1 \| Cột 2` rồi các dòng `tr: ô \| ô` | Bảng; ô có thể là `[Nút]`, `[x]`, `{Nhãn:ok}` (màu `ok`, `warn`, `bad`) |
| `kpi: Tên = 12 ; Tên = 34` · `bar: Tên = 60%` | Thẻ số liệu, thanh tỉ lệ (màn báo cáo) |
| `cols: input: A ; select: B` | Nhiều ô trên một hàng |
| `note: 1 \| Giải thích` | Chú thích cho điểm đánh số; gắn điểm bằng ` #1` ở cuối dòng |

Ví dụ:

```wireframe
screen: Đăng tuyển vị trí
id: M-00
role: Supervisor
device: desktop
style: wireframe
topbar: Work-Study ; Vị trí của tôi ; Hồ sơ
title: Đăng tuyển vị trí mới
cols: select: Vị trí * = PASS Leader #1 ; date: Hạn đăng tuyển * #2
input: Số lượng * = 2
textarea: Mô tả công việc [auto]
alert: Sau khi gửi, Phòng Công tác sinh viên sẽ duyệt trước khi đăng.
button: Gửi duyệt (primary)
button: Lưu nháp
note: 1 | Danh sách vị trí do Phòng Công tác sinh viên khai sẵn.
note: 2 | Hệ thống tự đóng vị trí khi hết hạn.
```

## Trước khi gửi

- [ ] Mỗi màn hình trả lời: ai dùng, làm việc gì, dữ liệu nào tự điền, bước tiếp theo.
- [ ] Mỗi điểm chưa chắc đã đánh số trên màn hình và có câu hỏi ở mục 5.
- [ ] Mọi `OQ-<NN>` trong gói có trong sổ OQ đúng cấp (trạng thái chuyển `Asked` sau khi gửi).
- [ ] Không có họ tên, mã sinh viên, số tài khoản, số giấy tờ thật.
- [ ] Đã xuất thử file, xem lại bằng mắt.

## Truy vết nội bộ (không gửi khách)

| Mục trong gói | Nguồn (`SRC-<NN>`, mục) | `OQ-<NN>` mở ra | FR/BR dự kiến |
| --- | --- | --- | --- |
| | | | |

<!-- internal:end -->

# Gói xác nhận yêu cầu: <Tên quy trình hoặc module>

| Thông tin | Nội dung |
| --- | --- |
| Gửi | <Tên đại diện khách hàng> |
| Người gửi (đầu mối) | <Tên> |
| Ngày gửi · Hạn trả lời | <ngày> · <ngày> |
| Phiên bản gói | <0.1> |
| Căn cứ | <SRC-NN: tên tài liệu>, <SRC-NN: …> |

## 1. Mục đích và cách trả lời

Gói này tóm tắt những gì chúng tôi hiểu về <quy trình>, kèm bản phác màn hình, để anh/chị xác nhận hoặc chỉnh trước khi triển khai.

- Mục 2, 3, 4: đọc và đánh dấu **Đúng**, **Sửa** hoặc **Bỏ** ở cột "Trả lời" của bảng; chỗ sửa ghi ngắn ở cột "Ghi chú".
- Mục 5: trả lời trực tiếp vào cột "Trả lời".
- Số tròn cam trên màn hình (①②…) trỏ tới câu hỏi hoặc chú thích cùng số.
- Màn hình trong gói là **bản phác** về bố cục và nội dung, chưa phải giao diện cuối. Chữ trong ô là ví dụ.
- Trả lời qua <kênh> trước <ngày>. Chỗ nào chưa chắc, ghi "chưa chốt" và ai sẽ quyết.

## 2. Phạm vi đề xuất

| # | Hạng mục | Đề xuất | Trả lời (Đúng / Sửa / Bỏ) | Ghi chú |
| --- | --- | --- | --- | --- |
| 2.1 | <Việc làm trong lần này> | Làm | | |
| 2.2 | <Việc chưa làm trong lần này> | Chưa làm | | |

## 3. Quy trình chúng tôi hiểu

<Một đoạn mô tả ngắn, rồi bảng các bước theo người làm.>

| Bước | Ai làm | Việc | Hệ thống làm gì | Thời hạn | Trả lời (Đúng / Sửa) | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | | |

## 4. Màn hình đề xuất

### M-01 <Tên màn hình>

Ai dùng: <vai>. Khi nào: <tình huống>. Kết quả: <việc xong>.

```wireframe
screen: <Tên màn hình>
id: M-01
role: <vai>
device: desktop
style: wireframe
title: <Tiêu đề>
button: <Nút chính> (primary)
note: 1 | <Giải thích điểm 1>
```

| Điểm | Câu hỏi hoặc điều cần xác nhận | Trả lời | Ghi chú |
| --- | --- | --- | --- |
| ① | <ví dụ: Danh sách này lọc theo tiêu chí nào?> | | |

## 5. Quy tắc nghiệp vụ cần xác nhận

| # | Quy tắc chúng tôi hiểu | Nguồn | Trả lời (Đúng / Sửa / Bỏ) | Ghi chú |
| --- | --- | --- | --- | --- |
| 5.1 | <Thời hạn, tỉ lệ, điều kiện…> | <SRC-NN, mục> | | |

## 6. Câu hỏi cần anh/chị quyết hoặc làm rõ

| # | Mã | Loại | Câu hỏi | Phương án và đề xuất | Nếu chưa quyết | Trả lời |
| --- | --- | --- | --- | --- | --- | --- |
| 6.1 | OQ-<NN> | Làm rõ | <Trích nguyên văn tài liệu và hai cách hiểu> | | | |
| 6.2 | OQ-<NN> | Cần quyết | <Câu hỏi> | A: <…> · B: <…> · Đề xuất: <A/B, lý do> | <việc bị chặn> | |

## 7. Tài liệu và thông tin cần bổ sung

| # | Mã | Cần | Để làm | Nếu chưa có | Hạn |
| --- | --- | --- | --- | --- | --- |
| 7.1 | OQ-<NN> | <Tài liệu, dữ liệu đã ẩn danh> | <Việc> | <Việc bị chặn> | |

## 8. Xác nhận

Chọn một: ☐ Đồng ý nội dung gói này · ☐ Đồng ý sau khi sửa theo các ghi chú ở trên · ☐ Cần trao đổi thêm

| Người xác nhận | Chức vụ | Ngày | Ghi chú |
| --- | --- | --- | --- |
| | | | |
