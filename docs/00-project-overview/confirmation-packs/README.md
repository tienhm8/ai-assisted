# Gói xác nhận yêu cầu

| Thuộc tính | Giá trị |
| --- | --- |
| Người phụ trách | BA |
| Người duyệt | PO |
| Tài liệu liên quan | ../sources/README.md, ../open-questions.md, ../../../.ai/templates/CONFIRMATION-PACK-TEMPLATE.md |

> **Mục đích.** Nơi lưu các Gói xác nhận yêu cầu gửi khách hàng: bản nguồn `.md` do AI soạn, BA rà, và bản xuất HTML/PDF. Gói là bản nháp nội bộ, chưa phải nguồn. Khi khách trả lời hoặc duyệt, Đầu mối lưu câu trả lời thành `SRC-<NN>` ở [sources/](../sources/README.md), không lưu ở đây.

## 1. Quy tắc

- **Mỗi gói một chủ đề** (một quy trình hoặc một nhóm màn hình), theo [mẫu gói](../../../.ai/templates/CONFIRMATION-PACK-TEMPLATE.md).
- **Mỗi gói một mã** `GXN-<NN>`, tăng dần, không dùng lại. File tên `GXN-<NN>-<tên-ngắn>.md`; bản xuất cùng tên, đuôi `.html` hoặc `.pdf`.
- **Xuất file** từ thư mục gốc repo: `python3 -I .ai/scripts/export-pack.py docs/00-project-overview/confirmation-packs/GXN-<NN>-<tên-ngắn>.md --pdf`. Bản xuất nằm cạnh file nguồn.
- **Căn cứ:** ghi các `SRC-<NN>` làm căn cứ ở đầu gói. Mọi `OQ-<NN>` trong gói phải có trong sổ OQ đúng cấp; sau khi gửi, chuyển OQ sang `Asked`.
- **Không đưa dữ liệu thật** (họ tên, mã sinh viên, số tài khoản, số giấy tờ) vào gói; dùng tên và số giả.

## 2. Danh mục

| Mã | Chủ đề | Căn cứ (`SRC-<NN>`) | Ngày gửi | Trạng thái | Câu trả lời (`SRC-<NN>`) |
| --- | --- | --- | --- | --- | --- |
| GXN-<NN> | | | | Draft / Đã gửi / Đã trả lời | |

<!-- Điền theo từng dự án: mỗi gói một dòng; xoá dòng mẫu. -->
