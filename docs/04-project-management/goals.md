# Goals

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | Tech Lead (PO quyết Goal nghiệp vụ) |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | roadmap.md, backlog.md, task-breakdown.md, ../00-project-overview/vision.md, ../01-requirements/BRD.md, ../../.ai/workflows/task-execution.md |

> **Mục đích.** Nơi duy nhất ghi Goal: kết quả đầu ra mà người dùng hoặc tổ chức muốn đạt. Goal trả lời "cuối cùng muốn đạt gì?"; cách đạt nằm ở các Plan (`.ai/plans/`), việc cụ thể ở Task (backlog, task-breakdown), từng lần thực thi ở `runs.md` của Plan.

## 1. Mô hình

```text
Goal (1) ──< Plan (N) ──< Task (N) ──< Run (N)
 WHAT         HOW          WHAT TO DO    DO
```

| Cấp | Trả lời | Ví dụ | Mã |
| --- | --- | --- | --- |
| Goal | Muốn đạt được điều gì? | Xây dựng hệ thống CRM | `GOAL-<NN>` |
| Plan | Thực hiện bằng cách nào? | Phân tích; Thiết kế; Làm tính năng Khách hàng; Triển khai | `<GOAL>-P<N>` |
| Task | Công việc cụ thể cần làm? | Thiết kế database khách hàng | `<KEY>-<N>` |
| Run | Thực thi như thế nào? | Agent gọi công cụ với model, effort; chạy SQL; kiểm tra kết quả | `<KEY>-<N>#<n>` |

- Plan không đồng nghĩa với Task; Task không đồng nghĩa với Agent. Plan: AI suy nghĩ và chia nhỏ mục tiêu. Task: đơn vị công việc có đầu vào, đầu ra, trạng thái rõ ràng. Agent: chủ thể thực thi Task. Tool: công cụ Agent dùng.
- Mã `GOAL-<NN>` không viết tắt thành `G<N>` để khỏi nhầm với cổng duyệt G0–G7.
- Quan hệ với các khái niệm có sẵn: Goal truy vết lên Outcome (`OUT`) hoặc yêu cầu nghiệp vụ (`BRQ`) nếu có; một Goal có thể thuộc một Epic (nhóm theo mốc ở [roadmap](roadmap.md)); Goal kỹ thuật (hạ tầng, refactor, sửa lỗi lớn) ghi lý do thay cho truy vết.

## 2. Khi nào tạo Goal, khi nào tạo Plan

- **Goal mới:** khi kết quả muốn đạt khác hẳn Goal đang có, và có người sở hữu, tiêu chí hoàn thành riêng.
- **Plan mới** (thay vì thêm Task vào Plan có sẵn) khi có ít nhất một điều: mục tiêu đầu ra khác nhau; thực hiện độc lập được; có vòng đời và tiêu chí hoàn thành riêng; cần quản lý tiến độ hoặc quyền truy cập riêng. Mặc định mỗi chặng kết thúc ở một cổng duyệt (phân tích → G2, thiết kế → G3, làm tính năng → G5) là một Plan.
- Việc nhỏ (một Task R1, rủi ro thấp) vẫn gắn vào một Goal có sẵn; không lập Goal chỉ cho một Task.

## 3. Danh sách Goal

| Goal | Tên | Kết quả mong đợi (đo được) | Truy vết (OUT/BRQ/Epic) | Tiêu chí hoàn thành | Người sở hữu | Plan | Trạng thái | Ngày tạo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GOAL-<NN> | | | | | | <GOAL>-P1, <GOAL>-P2 | Open | |

## 4. Trạng thái

- Goal: `Open` → `In Progress` → `Achieved` / `Dropped` (ghi lý do).
- Plan: `Draft` → `Approved` → `In Progress` → `Done` / `Cancelled` (ở bảng thuộc tính của Plan).
- Task: theo [backlog](backlog.md) §5.
- Run: `Đạt` / `Không đạt` / `Dừng` (ở `runs.md` của Plan).

Goal chỉ chuyển `Achieved` khi tiêu chí hoàn thành có bằng chứng và người sở hữu xác nhận; AI không tự chuyển.
