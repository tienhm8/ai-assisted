# Đầu vào review: PLAN-001

> Orchestrator soạn cho Run review ở bước 8 (`PLAN-001-REVIEW#1`), thay cho mô tả PR (PR chưa mở). Chỉ ghi sự kiện và bằng chứng, không ghi nhận định của người viết.

## 1. Vấn đề và phạm vi

- **Nguồn:** yêu cầu độc lập của người phát triển khung (PLAN.md, bảng đầu file).
- **Mục tiêu:** khung dễ hiểu, dễ dùng:
  - mã lựa chọn (R1–R3, A0–A4, S1–S3, D0–D3, G0–G7, [01]–[08], T1–T15, M·E) thay bằng từ;
  - `ai-config.yaml` là nguồn duy nhất của model/effort;
  - `CHECKLIST.md`;
  - tài liệu khung chuyển sang `.ai/guide/`;
  - vùng đỏ khai theo thư mục con.
- **Loại thay đổi:** đổi kiến trúc của khung và sửa tài liệu. Không có code chạy được. Không có dữ liệu, schema, API, quyền.
- **Ngoài phạm vi:** PLAN.md §1 "Không làm".
- **Quyết định sau khi Plan được duyệt** (PLAN.md §3, các dòng 2026-11-19 "xem đợt 1"):
  - bỏ `.ai/agents/references/`;
  - khoá `auto_runs`;
  - mức chỉ có model cho công cụ không có effort;
  - FW-4 thêm `ai-config.yaml` vào phạm vi.

## 2. Diff cần review

- Từ commit `226ad76` (Plan được duyệt) đến `HEAD` của nhánh `refactor/AI-framework-refactor`.
- Bỏ qua `.ai/plans/`: đó là Plan, manifest, `runs.md`, `check.py`, là công cụ của Orchestrator, nằm ở vùng xanh.
- Lệnh: `git diff 226ad76 HEAD -- . ':!.ai/plans'` (84 file).
- File chuyển chỗ (`git mv`): xem bằng `git diff -M --name-status 226ad76 HEAD`.

## 3. Task và AC

Mỗi Task có manifest ở `.ai/plans/PLAN-001-framework-refactor/tasks/FW-<n>.yaml`. Các trường `instructions`, `scope.allowed_paths`, `acceptance_criteria` là chuẩn để so.

| Task | Việc | Lần chạy được nhận | Commit |
| --- | --- | --- | --- |
| FW-1 | Từ vựng trong `project-rules`, `task-types`, `task-execution`; thay rule 23 | FW-1#1 | `8b07c11` |
| FW-2 | `CLAUDE.md`, vùng theo thư mục con, worktree ở `.claude/worktrees/`, cây README | FW-2#2, FW-2#3 (`.claude/settings.json` do người tạo, `6ae1b90`) | `0126cff`, `acd8bff` |
| FW-3 | `ai-config.yaml`, rút `model-effort` còn quy tắc, mẫu, Skill chọn reference theo `stack`; bổ sung B (xoá references, mức chỉ model), bổ sung C (`auto_runs`) | FW-3#1, #2, #3 | `4e0ff2e`, `ec36514`, `aa9bab2` |
| FW-4 | Chuyển tài liệu khung sang `.ai/guide/`, tách glossary, `ai-tools` §3–§4 sang `PROJECT.md` | FW-4#1, #2 | `bde0c2f`, `c669351` |
| FW-5 | `CHECKLIST.md`, `PROJECT.md` điền sẵn khuyến nghị | FW-5#1 | `dba33c9` |
| FW-6 | Đổi mã thành chữ trong file cho AI | FW-6#1 | `3f6ba93` |
| FW-7 | Đổi mã thành chữ trong file cho người | FW-7#1 | `49abdcb` |

## 4. Bằng chứng kiểm (Orchestrator chạy trên kết quả gộp `6762829`)

| Kiểm | Lệnh | Kết quả |
| --- | --- | --- |
| Link gãy | `python3 -I .ai/plans/PLAN-001-framework-refactor/check.py links` | 0 |
| Mã lựa chọn sót | `check.py codes .ai/rules .ai/skills .ai/workflows .ai/templates .ai/agents .ai/guide .ai/README.md docs README.md PROJECT.md CHECKLIST.md AGENTS.md CLAUDE.md ai-config.yaml` | 0 (trước Plan: 775) |
| `ai-config.yaml` | `check.py config` | 0 |
| Cây README | `check.py tree` | 0 |
| Lọc loại việc | `check.py types` | 0 |
| Từ vựng thang | `check.py vocab` | 0 |
| AC từng Task | lệnh `acceptance_criteria` của mỗi manifest, chạy lại sau gộp | đạt |

Các kiểm trên chỉ bắt cú pháp: mã sót, link, khoá YAML. **Chúng không kiểm nghĩa.** Nghĩa của rule trước và sau là việc của review này.

## 5. Điểm các lần chạy tự báo là tự chọn cách diễn đạt (cần so nghĩa)

- `project-rules` mục "Shared scales": định nghĩa `lean`/`standard`/`strict`, 8 cổng, 8 giai đoạn. Nguồn gốc: `docs/04-project-management/gates-and-rigor.md` §1–§2 ở commit `226ad76`.
- `project-rules` rule 19: "review per R3" thành "review per the `high`-risk rule".
- `project-rules` rule 23 thay bằng quy tắc dùng từ (PLAN §6.1).
- `model-effort.md` §2–§4 viết lại theo `try`, `high_risk_min`, `auto_runs`. Bản gốc ở `226ad76`, gồm bảng mặc định, `floor`/`ceiling`/`ladder`.
- `workflows/README`: "T1–T15" thành "15 loại". Nhiều chỗ "D0–D3" thành tên bốn mức.
- `.ai/guide/gates-and-rigor.md`: tên cổng, giai đoạn viết lại bằng chữ.
- `CHECKLIST.md` việc 12: "`ai-config.yaml` trạng thái Approved", trong khi file YAML không có dòng trạng thái.
- `.ai/guide/ai-tools.md` §3 "Chạy Task với Claude Code": thay cho `.ai/agents/references/claude-code.md` đã xoá; phần "Cách A: subagent theo vai × mức" không được chuyển.

## 6. Kiểm thử, triển khai, rollback

- Không có test đơn vị (không có code).
- Không triển khai. Repo khung; người phát triển khung merge vào `master`.
- Rollback: revert nhánh.
