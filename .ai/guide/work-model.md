# Mô hình khái niệm (Work Model)

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (khung) | Tech Lead |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | ../../docs/04-project-management/goals.md, ../../docs/04-project-management/product-backlog.md, ../../docs/04-project-management/task-backlog.md, task-breakdown.md, ../../docs/01-requirements/BRD.md, ../../docs/01-requirements/features.md, ../../docs/00-project-overview/glossary.md, ../../.ai/workflows/task-execution.md |

> **Mục đích.** Nguồn duy nhất mô tả các khái niệm quản lý yêu cầu, công việc và thực thi bằng AI: thuộc nhóm nào, quản lý ở đâu, liên kết với nhau thế nào. Tài liệu khác chỉ trỏ tới đây, không chép lại.

## 1. Ba nhóm khái niệm

| Nhóm | Trả lời | Khái niệm |
| --- | --- | --- |
| A. Định nghĩa nghiệp vụ và sản phẩm | WHAT / WHY | BRD, BRQ, Goal, Epic, Function/Feature, User Story |
| B. Lập kế hoạch và quản lý công việc | HOW | Plan, Task, Subtask, Dependency |
| C. Thực thi bằng AI | DO | Agent, Execution (Run), Model·effort, Tool, Result, Review/Validation |

## 2. Từng khái niệm

| Khái niệm | Nhóm | Ý nghĩa | Trả lời câu hỏi | Mã | Quản lý ở |
| --- | --- | --- | --- | --- | --- |
| BRD | A | Business Requirements Document | Doanh nghiệp cần gì và tại sao? | — | [BRD](../../docs/01-requirements/BRD.md) |
| BRQ | A | Business Requirement: yêu cầu nghiệp vụ cụ thể | Yêu cầu nghiệp vụ cụ thể là gì? | `BRQ-<NN>` | [BRD](../../docs/01-requirements/BRD.md) §3 |
| Goal | A | Desired Outcome: kết quả mong muốn | Muốn đạt kết quả gì? | `GOAL-<NN>` | [goals](../../docs/04-project-management/goals.md) |
| Epic | A | Nhóm chức năng/công việc lớn theo phạm vi sản phẩm, lộ trình | Nhóm công việc lớn nào cần thực hiện? | `EPIC-<NN>` | [product-backlog](../../docs/04-project-management/product-backlog.md) §1 |
| Function / Feature | A | Chức năng hệ thống (đặc tả sản phẩm); chi tiết hoá bằng FR | Hệ thống cần có chức năng gì? | `FEAT-<NN>` | [features](../../docs/01-requirements/features.md) |
| User Story | A | Nhu cầu của người dùng | Người dùng muốn làm gì và vì sao? | `US-<MODULE>-<NN>` | [product-backlog](../../docs/04-project-management/product-backlog.md) §2 |
| Plan | B | Kế hoạch thực hiện một hoặc nhiều công việc | Sẽ thực hiện như thế nào? | `PLAN-<NNN>` | `.ai/plans/PLAN-<NNN>-<slug>/PLAN.md` |
| Task | B | Đơn vị công việc chính thức, có ID, Type, Risk, Autonomy | Cần thực hiện công việc cụ thể nào? | `<KEY>-<N>` | [task-backlog](../../docs/04-project-management/task-backlog.md), [task-breakdown](task-breakdown.md); manifest ở `.ai/plans/<plan>/tasks/` |
| Subtask | B | Bước bên trong một Task; thực thể nội bộ, không có ID riêng | Task gồm những bước nào? | — | Thủ tục của Skill; checklist trong Task Specification ([task-breakdown](task-breakdown.md) §4) |
| Dependency | B | Task phải xong trước Task khác | Làm gì trước? | — | Cột Phụ thuộc ([task-backlog](../../docs/04-project-management/task-backlog.md)), `dependencies` trong manifest |
| Agent | C | Vai thực thi Task | Ai làm? | — | [.ai/agents/](../../.ai/agents/README.md) |
| Execution (Run) | C | Một lần thực thi Task | Đã chạy thế nào? | `<KEY>-<N>#<n>` | `runs.md` của Plan |
| Model·effort | C | Hạng model và mức effort của một Run | Chạy ở mức nào? | `M<N>·E<N>` | [model-effort](../../.ai/workflows/model-effort.md) |
| Tool | C | Công cụ Agent dùng (CLI AI, lệnh, MCP) | Dùng công cụ gì? | — | [ai-tools](ai-tools.md) |
| Result | C | Diff, tài liệu, bằng chứng kiểm tra của một Run | Ra kết quả gì? | — | `runs.md`; báo cáo bàn giao |
| Review / Validation | C | Kiểm tra kết quả: lệnh kiểm AC, review code, người duyệt ở cổng | Kết quả có đúng không? | `PLAN-<NNN>-REVIEW#<n>` | [task-execution](../../.ai/workflows/task-execution.md) bước 6–8 |

## 3. Liên kết, không phải cây cha-con

Các khái niệm **không gộp thành một hệ thống phân cấp**. Ví dụ:

- Một BRQ có thể liên quan nhiều Function; một Function có thể đáp ứng nhiều BRQ.
- Một User Story có thể cần nhiều Task; một Task có thể phục vụ nhiều User Story.
- Một Goal có thể cần nhiều Plan; một Plan có thể chứa nhiều Task.
- Một Epic có thể đóng góp vào nhiều Goal; một Goal có thể cần nhiều Epic.

Vì vậy mỗi liên kết khai **một chiều**, ở đối tượng đứng sau, dưới dạng danh sách mã; tra ngược bằng cách lọc cột. Không khai hai chiều, không lập ma trận truy vết riêng.

| Đối tượng | Khai liên kết tới | Số lượng | Ở đâu |
| --- | --- | --- | --- |
| Goal | Nguồn: BRQ, OUT, chiến lược kinh doanh, hoặc yêu cầu trực tiếp của người dùng | một hoặc nhiều | cột "Nguồn" ở [goals](../../docs/04-project-management/goals.md) |
| Epic | BRQ; Goal mà Epic đóng góp | nhiều; nhiều | [product-backlog](../../docs/04-project-management/product-backlog.md) §1 |
| Function / Feature | BRQ | nhiều | [features](../../docs/01-requirements/features.md) |
| FR | BRQ nguồn; Feature; BR | nhiều; một; nhiều | [bảng FR](../../docs/01-requirements/FR/README.md) |
| User Story | Epic; Feature; FR | một; nhiều; nhiều | [product-backlog](../../docs/04-project-management/product-backlog.md) §2 |
| Plan | Nguồn (Goal, Epic, User Story, hoặc yêu cầu độc lập); Goal (tuỳ chọn) | đúng một; không hoặc nhiều | bảng đầu của PLAN.md |
| Task | Plan; User Story / FR / BR mà Task phục vụ; Task phụ thuộc | một; nhiều; nhiều | [task-backlog](../../docs/04-project-management/task-backlog.md); manifest |
| Run | Task | một | `runs.md` |

```text
 A ─ WHAT/WHY                          B ─ HOW                    C ─ DO
 BRD ─ BRQ ◄──── Goal ◄─────────────── Plan ──< Task ──< Run (Agent, Model·effort, Tool, Result)
        ▲  ▲      ▲  (Goals, tuỳ chọn)  │  ▲     │ ▲              │
        │  │      │                     │  └─────┼─┘ Dependency   Review / Validation
        │  └── Epic ◄─── Source ────────┤        │
        │       ▲                       │        │ phục vụ (nhiều)
   Feature ◄── User Story ◄── Source ───┘        │
     ▲            ▲                              │
     FR ──────────┴──────────────────────────────┘
 (mũi tên: đối tượng khai liên kết → đối tượng được tham chiếu)
```

## 4. Nguyên tắc thiết kế

1. BRD, BRQ, Epic, Function, User Story không phải Goal hoặc Task. Không biến Goal thành cấp thay Epic, không biến Epic thành một loại Plan.
2. Goal có thể được tạo từ BRQ, chiến lược kinh doanh hoặc yêu cầu trực tiếp của người dùng.
3. Plan có thể được tạo từ Goal, User Story, Epic hoặc yêu cầu thực hiện công việc độc lập; mỗi Plan ghi đúng một Nguồn, Goal là tuỳ chọn.
4. Task là đơn vị công việc chính thức có mã `<KEY>-<N>`.
5. Phải lưu được nguồn gốc yêu cầu (traceability) để biết Task được tạo ra nhằm đáp ứng BRQ, User Story hay Goal nào: đi từ Task → Plan (Nguồn, Goal) và Task → User Story/FR → Feature, Epic → BRQ.

Tóm lại: Goal là mục tiêu đầu ra. Epic là nhóm công việc theo phạm vi sản phẩm, lộ trình. Plan là kế hoạch hành động. Task là đơn vị công việc được giao và thực thi.
