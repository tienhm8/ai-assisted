# Acceptance Criteria

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người phụ trách |  |
| Người duyệt |  |
| Phiên bản · Ngày | 0.1 ·  |
| Tài liệu liên quan | FR/, business-rules.md, ../03-engineering/testing-strategy.md, ../../.ai/rules/testing-rules.md, ../../.ai/skills/requirement-analysis/SKILL.md |

> **Mục đích.** Định nghĩa "làm xong" của từng FR: các điều kiện cụ thể để kiểm thử và nghiệm thu.
>
> - **Đầu vào:** danh sách FR trong phạm vi.
> - **Đầu ra:** mỗi FR có ít nhất một AC viết dạng Given / When / Then, kiểm thử được.
> - **Người quyết định:** PO/BA; QA rà khả năng kiểm thử.
> - **Điều kiện duyệt (G2):** mọi FR trong phạm vi đều có AC; điểm chưa rõ ghi vào [open-questions.md](../00-project-overview/open-questions.md) (`OQ-<NN>`).
> - **Phạm vi file:** dự án nhỏ dùng file này; dự án lớn đặt AC ngay trong `FR/FR-<MODULE>.md` hoặc chia theo module, ghi lựa chọn trong `PROJECT.md`. Một nơi duy nhất cho mỗi AC.
> - **Liên kết BR:** nếu AC kiểm chứng một quy tắc nghiệp vụ thì ghi BR vào cột "BR kiểm chứng"; mỗi BR cần ít nhất một AC kiểm chứng.
> - **Nội dung AC:** ngoài luồng chính, có AC cho trường hợp lỗi và giá trị biên.

| AC ID | FR | BR kiểm chứng | Given / When / Then | Loại test | Test tham chiếu |
| --- | --- | --- | --- | --- | --- |
| FR-AUTH-01-AC1 | FR-AUTH-01 | BR-AUTH-01 | Given … When … Then … | unit / integration / E2E | |

## Lịch sử thay đổi
| Ngày | Thay đổi | Lý do | Người duyệt |
| --- | --- | --- | --- |
