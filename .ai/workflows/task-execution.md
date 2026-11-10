# Task Execution Workflow

> Trạng thái: **Draft**. Quy trình **bắt buộc** áp dụng cho mọi Task giao cho AI.
> Sửa file này thuộc vùng 🔴 (luật chơi của AI): cần Task riêng và người duyệt.

Task được giao theo mẫu Task của dự án. Việc chọn và phối hợp Skill ở các bước 1–8 xem skill-orchestration.md.

| Bước | Tên | Nội dung | Đầu ra |
| --- | --- | --- | --- |
| 1 | Read Context | Đọc Rules, Skills, tài liệu nghiệp vụ và code liên quan | Context set |
| 2 | Analyze Task | Phân tích yêu cầu, xác định phụ thuộc, phát hiện điểm chưa rõ | Danh sách câu hỏi (nếu có) |
| 3 | Create Implementation Plan | Danh sách file dự kiến thay đổi, thiết kế và kế hoạch test | Plan |
| 4 | Human Approval | Con người duyệt kế hoạch nếu có thay đổi kiến trúc, bảo mật, dữ liệu hoặc phạm vi nhạy cảm | Plan được duyệt |
| 5 | Implement | AI thực hiện code theo từng bước nhỏ | Diff |
| 6 | Run Tests | Chạy lint, typecheck, unit, integration và E2E phù hợp | Bằng chứng (output thật) |
| 7 | Self Review | AI kiểm tra lại code, diff, quyền truy cập, lỗi và yêu cầu | Diff đã rà |
| 8 | Human Review | Developer/Reviewer kiểm tra và phê duyệt Pull Request | PR được duyệt |
| 9 | Merge & Deploy | Người merge sau khi PR được duyệt; triển khai theo release-workflow.md. AI chỉ chuẩn bị, không tự merge hay deploy production | Bản phát hành |
| 10 | Update Knowledge | Cập nhật tài liệu, Skill, Rule khi phát hiện quy tắc mới có giá trị lâu dài | Truy vết đóng |

Bước 4 và các điều kiện dừng: AI dừng và hỏi khi thiếu thông tin, mâu thuẫn tài liệu, hoặc việc vượt Scope của Task. Bước 10: sửa Rule/Skill/workflow thuộc vùng 🔴, nên đề xuất thay vì tự sửa.

## Prompt mẫu giao Task cho AI

Thay `[TASK-ID]` bằng ID Task. Task phải có đủ nội dung theo mẫu Task; làm việc trên nhánh riêng.

```text
You are working as a Senior Software Engineer.

Your task is to implement: [TASK-ID]

MANDATORY INSTRUCTIONS:

1. Read project instructions and applicable rules.
2. Read the relevant Skills.
3. Read all related requirements and architecture documents.
4. Inspect existing implementation before modifying files.
5. Identify ambiguities and conflicts.
6. Do not invent business requirements.
7. Prepare an implementation plan before coding.
8. Identify files expected to change.
9. Implement only the approved scope.
10. Write appropriate automated tests.
11. Run all required quality checks.
12. Review your own changes.
13. Update relevant documentation.

Do not:
- Change unrelated modules.
- Bypass authorization.
- Disable tests to make the build pass.
- Modify production data.
- Introduce dependencies without justification.
- Claim successful tests without execution evidence.

If requirements are unclear or conflicting:
STOP and report the issue.

FINAL REPORT:

- Task completed:
- Files changed:
- Technical implementation:
- Tests executed:
- Test results:
- Known issues:
- Documentation updated:
- Risks and recommendations:
```
