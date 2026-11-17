# Model and effort by Task type

> Status: **Approved**. Changing this file requires a dedicated Task and a reviewer. Load only at step 3 or when the Tech Lead configures it.

The "Model · Effort" column in [task-types.md](task-types.md) §1 is the default per Task type: "plan" is the session for steps 1–4, "execution" is steps 5–7; step 8 uses row T9. The Tech Lead finalizes it by editing that column and filling in the mapping table below; declare nowhere else.

- **Model tier:** M1 light (lookups, summaries, template work) · M2 standard (everyday code, tests, docs) · M3 strong (design, review, security, incidents).
- **Effort:** E1 low · E2 medium · E3 high · E4 very high.
- R3 Tasks, or steps using `authentication-rbac` or `security-review`: at least M3·E3.
- If the session model is below the required tier, no model of the right tier exists, or quota runs out: stop and ask a human to change it; do not downgrade yourself.

**Mapping to real tools:** read the reference file for the AI tool the session runs in, section §1 (M1–M3 → model, E1–E4 → effort). Do not copy the tables here.

| Tool | Reference |
| --- | --- |
| Claude Code | [claude-code.md](../agents/references/claude-code.md) |
| Cursor | [cursor.md](../agents/references/cursor.md) |
| GitHub Copilot | [copilot.md](../agents/references/copilot.md) |
| Gemini CLI | [gemini.md](../agents/references/gemini.md) |
| Codex (ChatGPT) | [codex.md](../agents/references/codex.md) |

Cursor, Copilot and Gemini CLI have no confirmed effort parameter: for them only the model tier (M1–M3) applies and the E level is ignored. R3 Tasks still need at least M3.

A tool not listed: add a reference file under `.ai/agents/references/` with the same §1 and add a row here.
