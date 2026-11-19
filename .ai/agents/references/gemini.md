# Model và effort cho Gemini CLI

> Dùng khi phiên chạy trong Gemini CLI. **§1 là khối `sessions`/`tasks`** của Gemini CLI: đổi công cụ sang Gemini CLI thì chép khối này vào [ai-config.yaml](../../../ai-config.yaml); quy tắc chọn mức nằm ở [model-effort.md](../../workflows/model-effort.md).
> Tên model theo tài liệu geminicli.com (cập nhật: 2026-11). Tài liệu đó chỉ nêu hai dòng Pro và Flash nên Gemini CLI chỉ có hai model thật: model nhẹ và model chuẩn dùng chung Flash. Tài liệu cũng ghi Gemini CLI đã được thay bằng Antigravity CLI từ 2026-06-18 và chưa tối ưu cho Gemini 4; nếu dự án dùng Antigravity CLI hoặc Gemini 4, đối chiếu lại bảng này.

## 1. Model theo loại việc

Model: `gemini-3-flash-preview` thay cho `haiku` và `sonnet`; `gemini-3-pro-preview` thay cho `opus`. Gemini CLI không có effort: mỗi mức chỉ ghi tên model, không ghi "/effort". Vì không có effort nên `try` chỉ còn các model khác nhau, bỏ phần tử trùng.

```yaml
sessions:
  orchestrator: gemini-3-pro-preview
  review:       gemini-3-pro-preview
tasks:
  - for: [lookup]
    try: [gemini-3-flash-preview]
  - for: [documentation]
    try: [gemini-3-flash-preview]
  - for: [unit-testing, integration-testing, e2e-testing]
    try: [gemini-3-flash-preview, gemini-3-pro-preview]
  - for: [backend-development, api-development, frontend-development]
    try: [gemini-3-flash-preview, gemini-3-pro-preview]
  - for: [refactoring, caching, deployment, requirement-review, continuous-improvement]
    try: [gemini-3-flash-preview, gemini-3-pro-preview]
  - for: [bug-fixing]
    try: [gemini-3-flash-preview, gemini-3-pro-preview]
  - for: [product-discovery, requirement-analysis, architecture-design, database-design, task-planning, incident-analysis, code-review]
    try: [gemini-3-pro-preview]
  - for: [authentication-rbac, security-review]
    try: [gemini-3-pro-preview]
```

Lưu ý:
- Thứ tự ưu tiên chọn model: cờ `--model` > biến môi trường `GEMINI_MODEL` > `model.name` trong `settings.json` > mặc định (Auto). **Không dùng Auto** cho Task cần hạng tối thiểu: đặt model tường minh.
- Đổi trong phiên bằng `/model`.
- Model thiếu hạng yêu cầu: dừng và hỏi người, đừng tự hạ.

## 2. Mặc định cho repo

`.gemini/settings.json` (định dạng lồng nhau ở bản mới; bản cũ dùng chuỗi phẳng, kiểm tra theo phiên bản):

```json
{
  "model": { "name": "gemini-3-flash-preview" }
}
```

## 3. Vai (agent)

Mở phiên mới cho Reviewer/Security, chọn model theo `sessions.review` của `ai-config.yaml`, mở đầu bằng "Bạn giữ vai Reviewer trong .ai/agents/README.md. Nạp .ai/skills/code-review/SKILL.md." (tương tự Security với `security-review`).

**Chạy Task theo manifest:** công cụ này không có subagent khai báo được model theo repo, nên Orchestrator không tự gửi Task. Orchestrator soạn manifest và câu mở phiên cho từng Run; người mở phiên mới, chọn model theo mức hiện tại của manifest, dán câu mở phiên, rồi đưa báo cáo bàn giao về phiên Orchestrator để đánh giá. Nâng mức: mở phiên mới ở bậc kế. Có thể mở phiên bằng `gemini --model <model>`. Effort không áp dụng: ghi "không áp dụng: effort" trong Run.
