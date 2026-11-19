# Functional Requirements (FR)

Mỗi module một file: `FR-<MODULE>.md` (ví dụ `FR-AUTH.md`). Mã định danh: `FR-<MODULE>-<NN>`; tiêu chí nghiệm thu: `<FR>-AC<N>`.

## Bảng FR (mẫu cho mỗi file module)

| ID | Mô tả | BRQ nguồn | Feature | BR áp dụng | Ưu tiên | Trạng thái | Bằng chứng (plan/Task + commit) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FR-<MODULE>-<NN> |  | BRQ-<NN> | FEAT-<NN> | BR-<MODULE>-<NN> | | ☐ | |

**Ưu tiên (dùng chung BRD, FR, NFR):** MoSCoW — `Must` · `Should` · `Could` · `Won't`.

**Mô tả FR** viết ngắn, một câu, đủ để kiến trúc sư, Tech Lead và developer hiểu hệ thống phải làm gì.

Điểm chưa rõ ghi `OQ-<NN>` ([open-questions.md](../../00-project-overview/open-questions.md)), không đoán.

Trạng thái: `☐` chưa làm · `◐ <lý do>` đang làm/lệch plan · `◐ chưa nghiệm thu` · `☑` có code + test + review theo mức rủi ro.

**Nguồn chính của truy vết:** bảng này giữ liên kết FR → BRQ, FR → Feature ([features](../features.md)) và FR → BR. Một Feature gồm nhiều FR; User Story ghi FR mà nó cần ở [product-backlog](../../04-project-management/product-backlog.md) §2. BRD và business-rules.md chỉ tham chiếu ngược (sinh từ đây), không tự khai báo chiều ngược lại. Acceptance Criteria trỏ tới FR (và BR mà nó kiểm chứng) ở [acceptance-criteria.md](../acceptance-criteria.md).

Trạng thái hoàn thành của FR **chỉ nằm ở bảng này**; nơi khác chỉ tham chiếu (nguyên tắc một nơi). Sửa FR phải có lịch sử thay đổi, không sửa lặng lẽ.

## Chi tiết FR (tuỳ chọn, chỉ cho FR rủi ro cao hoặc mơ hồ)
Đặt ngay dưới bảng trong file module; FR đơn giản thì bỏ qua.

```text
### FR-<MODULE>-<NN>
- Đầu vào / điều kiện tiên quyết:
- Luồng chính:
- Luồng lỗi / ngoại lệ:
- Dữ liệu liên quan (công khai, nội bộ, nhạy cảm hoặc bí mật):
- Điểm chưa rõ: OQ-<NN>
```

## Lịch sử thay đổi
| Ngày | FR | Thay đổi | Lý do | Người duyệt |
| --- | --- | --- | --- | --- |
