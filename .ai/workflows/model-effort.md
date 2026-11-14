# Model and effort by Task type

> Status: **Approved**. Changing this file requires a dedicated Task and a reviewer. Load only at step 3 or when the Tech Lead configures it.

The "Model · Effort" column in [task-types.md](task-types.md) §1 is the default per Task type: "plan" is the session for steps 1–4, "execution" is steps 5–7; step 8 uses row T9. The Tech Lead finalizes it by editing that column and filling in the mapping table below; declare nowhere else.

- **Model tier:** M1 light (lookups, summaries, template work) · M2 standard (everyday code, tests, docs) · M3 strong (design, review, security, incidents).
- **Effort:** E1 low · E2 medium · E3 high · E4 very high.
- R3 Tasks, or steps using `authentication-rbac` or `security-review`: at least M3·E3.
- If the session model is below the required tier, no model of the right tier exists, or quota runs out: stop and ask a human to change it; do not downgrade yourself.

**Mapping to real tools** (example: [claude-code.md](../agents/examples/claude-code.md)):

| Tier / level | Real model or parameter (name · version) |
| --- | --- |
| M1 · Light | |
| M2 · Standard | |
| M3 · Strong | |
| E1 · Low | |
| E2 · Medium | |
| E3 · High | |
| E4 · Very high | |
