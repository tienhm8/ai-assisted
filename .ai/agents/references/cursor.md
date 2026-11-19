# Model và effort cho Cursor

> Dùng khi phiên chạy trong Cursor. **§1 là khối `sessions`/`tasks`** của Cursor: đổi công cụ sang Cursor thì chép khối này vào [ai-config.yaml](../../../ai-config.yaml); quy tắc chọn mức nằm ở [model-effort.md](../../workflows/model-effort.md).
> Dùng model do Cursor cung cấp (Composer, Grok), như Claude Code dùng họ Claude. Tài liệu cursor.com/docs/models không xếp hạng chất lượng; phân hạng dưới đây suy từ giá theo token (Composer 2.5 rẻ nhất, Grok 4.7 đắt nhất), nên Tech Lead đo trên Task thật trước khi chốt. Model đổi thường xuyên, kiểm tra lại trước khi áp dụng (cập nhật: 2026-11).

## 1. Model theo loại việc

Model: Composer 2.5 thay cho `haiku`; Grok 4.6 thay cho `sonnet`; Grok 4.7 thay cho `opus`. Cursor không có effort: mỗi mức chỉ ghi tên model, không ghi "/effort". Vì không có effort nên `try` chỉ còn các model khác nhau, bỏ phần tử trùng.

```yaml
sessions:
  orchestrator: grok-4.7      # Plan có đổi kiến trúc: vẫn grok-4.7
  review:       grok-4.7
tasks:
  - for: [lookup]
    try: [composer-2.5, grok-4.6]
  - for: [documentation]
    try: [grok-4.6]
  - for: [unit-testing, integration-testing, e2e-testing]
    try: [grok-4.6, grok-4.7]
  - for: [backend-development, api-development, frontend-development]
    try: [grok-4.6, grok-4.7]
  - for: [refactoring, caching, deployment, requirement-review, continuous-improvement]
    try: [grok-4.6, grok-4.7]
  - for: [bug-fixing]
    try: [grok-4.6, grok-4.7]
  - for: [product-discovery, requirement-analysis, architecture-design, database-design, task-planning, incident-analysis, code-review]
    try: [grok-4.7]
  - for: [authentication-rbac, security-review]
    try: [grok-4.7]
```

Lưu ý:
- Chọn model **thủ công** trong model picker của chat/agent trước khi bắt đầu phiên; không dùng chế độ tự chọn (Auto) cho Task cần model mạnh theo [model-effort.md](../../workflows/model-effort.md).
- Chưa xác nhận được cách đặt model hay effort mặc định cho repo qua `.cursor/rules`. Không giả định có.
- Model thiếu hạng yêu cầu: dừng và hỏi người, đừng tự hạ.

## 2. Vai (agent)

Cursor không dùng `.claude/agents`. Vai Reviewer, Security: mở phiên mới, chọn model theo `sessions.review` của `ai-config.yaml`, mở đầu bằng "Bạn giữ vai Reviewer trong .ai/agents/README.md. Nạp .ai/skills/code-review/SKILL.md." (tương tự cho Security với `security-review`).

**Chạy Task theo manifest:** công cụ này không có subagent khai báo được model theo repo, nên Orchestrator không tự gửi Task. Orchestrator soạn manifest và câu mở phiên cho từng Run; người mở phiên mới, chọn model theo mức hiện tại của manifest, dán câu mở phiên, rồi đưa báo cáo bàn giao về phiên Orchestrator để đánh giá. Nâng mức: mở phiên mới ở bậc kế. Effort không áp dụng: ghi "không áp dụng: effort" trong Run.
