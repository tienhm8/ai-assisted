# Code Review – Checklist for correctness, tests, placement (priorities 1–3)

## Priority 1: Does the code do the right thing?

- Where in the code each AC is met; which AC has no place meeting it.
- Edge cases and duplicate data.
- State transitions: are invalid transitions blocked?
- Error handling: errors are not swallowed; errors are classified per error-handling; error messages do not leak internal details.
- Data types: money and numbers needing precision do not use floating point; time zones and time formats are consistent; rounding follows business rules.
- Transaction boundaries: are writes that must succeed or fail together in one atomic unit?
- Business rules come from FR/BR, not invented by the code; if unclear, record an open question.

## Priority 2: Are there tests proving it?

- Check tests in the diff against `testing-rules` 1–5; each AC has real test output.
- Tests check behavior, not implementation details; no empty assertions or assertions that only check "does not throw".

## Priority 3: Is the code in the right place?

Take the layer and responsibility map from the project's architecture docs; do not impose your own layer model. Check against these general responsibilities:

| Responsibility | Question |
| --- | --- |
| Request boundary (handler, controller, resolver, CLI, UI component) | Does it only orchestrate (receive request → call business logic → return result), or does it contain business rules or direct data access? |
| Input validation and authorization | Done at the system boundary, via the project's shared mechanism, not scattered in business logic? Accepts only allowed fields (whitelist), not assigning all input to the object? |
| Business logic (service, use case) | Are business rules here and in only one place? |
| Domain (entity, model, value object) | Is behavior tightly bound to data (invariant checks, state transitions) kept with its object? |
| Data access (repository, DAO, query) | Upper layers do not build queries bypassing the layer; no access to another module's data outside its public interface? |
| Async and side effects (job, event, consumer, notifications, external system calls) | Are slow or irreversible side effects separated from the main flow and from the transaction? |
| Output formatting | Returns the data shape defined for external use, not raw internal objects? |

Signals to examine (not laws; concrete thresholds per the project's coding-standards): function or class over size threshold; one function doing many things; deeply nested conditions; too many dependencies; one unit changed for many different reasons; circular dependencies; duplicated logic.
