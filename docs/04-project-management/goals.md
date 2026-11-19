# Goals

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | Tech Lead (PO quyết Goal nghiệp vụ) |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | ../../.ai/guide/work-model.md, roadmap.md, product-backlog.md, task-backlog.md, ../00-project-overview/vision.md, ../01-requirements/BRD.md, ../../.ai/workflows/task-execution.md |

> **Mục đích.** Nơi duy nhất ghi Goal (Desired Outcome): kết quả đầu ra mà người dùng hoặc tổ chức muốn đạt, trả lời "muốn đạt kết quả gì?". Goal thuộc nhóm A, định nghĩa nghiệp vụ và sản phẩm ([work-model](../../.ai/guide/work-model.md)); cách đạt nằm ở các Plan (`.ai/plans/`), việc cụ thể ở Task ([task-backlog](task-backlog.md)), từng lần thực thi ở `runs.md` của Plan.

## 1. Goal trong mô hình

Ba nhóm khái niệm, từng khái niệm và cách liên kết: [work-model](../../.ai/guide/work-model.md). Điểm riêng của Goal:

- Goal là mục tiêu đầu ra, không phải nhóm công việc (Epic) và không phải kế hoạch (Plan). Không thay Epic bằng Goal.
- **Nguồn của Goal:** BRQ, Outcome (`OUT`), chiến lược kinh doanh, hoặc yêu cầu trực tiếp của người dùng; ghi ở cột "Nguồn". Goal kỹ thuật (hạ tầng, refactor, sửa lỗi lớn) ghi lý do.
- **Không phải cây cha-con:** một Goal có thể cần nhiều Epic và nhiều Plan; một Epic có thể đóng góp vào nhiều Goal (Epic ghi Goal ở [product-backlog](product-backlog.md) §1); một Plan có thể phục vụ nhiều Goal hoặc không thuộc Goal nào (Plan ghi Goal ở PLAN.md). Goal không ghi ngược Epic, Plan; tra bằng cách lọc.
- Mã `GOAL-<NN>` không viết tắt thành `G<N>` để khỏi nhầm với cổng duyệt G0–G7.

| Ví dụ | Mã |
| --- | --- |
| Goal: Rút thời gian xử lý đơn đăng ký từ 5 ngày còn 1 ngày | `GOAL-01` |
| Epic đóng góp: Đăng ký trực tuyến; Duyệt đơn | `EPIC-02`, `EPIC-03` |
| Plan: Phân tích; Thiết kế; Làm tính năng Đăng ký (Nguồn `EPIC-02`, Goals `GOAL-01`) | `PLAN-004`… |
| Task: Thiết kế bảng đơn đăng ký | `WS-3` |

## 2. Khi nào tạo Goal, khi nào tạo Plan

- **Goal mới:** khi kết quả muốn đạt khác hẳn Goal đang có, và có người sở hữu, tiêu chí hoàn thành riêng.
- **Plan không bắt buộc có Goal:** Plan tạo từ Epic, User Story hoặc yêu cầu độc lập thì ghi Nguồn đó; không lập Goal chỉ để có chỗ gắn Plan.
- **Plan mới** (thay vì thêm Task vào Plan có sẵn) khi có ít nhất một điều: mục tiêu đầu ra khác nhau; thực hiện độc lập được; có vòng đời và tiêu chí hoàn thành riêng; cần quản lý tiến độ hoặc quyền truy cập riêng. Mặc định mỗi chặng kết thúc ở một cổng duyệt (phân tích → G2, thiết kế → G3, làm tính năng → G5) là một Plan.
- Việc nhỏ (một Task R1, rủi ro thấp) không cần Goal hay Plan: chạy fast lane, Task ghi User Story/FR hoặc lý do.

## 3. Danh sách Goal

| Goal | Tên | Kết quả mong đợi (đo được) | Nguồn (BRQ/OUT/chiến lược/yêu cầu) | Tiêu chí hoàn thành | Người sở hữu | Trạng thái | Ngày tạo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GOAL-<NN> | | | BRQ-<NN>, … | | | Open | |

Epic và Plan phục vụ một Goal: lọc cột Goal ở [product-backlog](product-backlog.md) §1 và trường Goals của các PLAN.md; không chép vào bảng này.

## 4. Trạng thái

- Goal: `Open` → `In Progress` → `Achieved` / `Dropped` (ghi lý do).
- Plan: `Draft` → `Approved` → `In Progress` → `Done` / `Cancelled` (ở bảng thuộc tính của Plan).
- Task: theo [task-backlog](task-backlog.md) §5.
- Run: `Đạt` / `Không đạt` / `Dừng` (ở `runs.md` của Plan).

Goal chỉ chuyển `Achieved` khi tiêu chí hoàn thành có bằng chứng và người sở hữu xác nhận; AI không tự chuyển.
