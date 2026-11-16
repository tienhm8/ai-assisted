# Coding Rules

> Status: **Approved**. Mandatory Rule, language-neutral.

## Design principles (Nguyên tắc thiết kế)

1. **Clean Code.** Names state intent. Functions are short, do one thing, have no hidden side effects. Comments only explain why, not repeat what the code says. Leave no unused imports or dead code.
2. **SOLID.**
   - Single Responsibility: each function, class, file has one responsibility; if a second job must be added, split.
   - Open/Closed: add behavior variants by extending through existing extension points, not by changing working code across the board.
   - Liskov Substitution: a subtype can replace its supertype without the caller having to know or check the concrete type.
   - Interface Segregation: interfaces are small, shaped by consumer needs; do not force consumers to depend on methods they do not call.
   - Dependency Inversion: depend on abstractions, injected via parameters or interfaces; do not instantiate dependencies internally, do not use global state.
3. **DRY.** Business logic is defined in only one place. Before writing new code, find and reuse existing functions, components, utilities. Extract shared parts only when there is real repetition.
4. **KISS.** Choose the simplest approach that meets the AC; write the way the surrounding code does.
5. **YAGNI.** Do not write code, abstraction layers, config parameters, or extension points for needs not in the Task.
6. **Separation of Concerns.** Do not mix UI, business logic, and data access in the same code unit.

When two principles conflict, KISS and YAGNI win: do not add abstraction to achieve SOLID or DRY when the Task does not need it yet.

## Conventions and error handling

7. Follow the language, version, naming, and lint/type-check tools fixed for the project. If an item is not fixed: stop and ask; do not choose yourself.
8. Check-relaxing mechanisms (type ignores, disabling lint...) may be used only with a reason written in place and reviewer acceptance.
9. Do not swallow errors (catch and ignore); every error must be handled, logged, or rethrown.
10. Classify errors and use the project's shared error codes; error responses must not expose stack traces, queries, or internal paths.
11. Every outbound call (DB, API, queue) has a timeout; retry only transient errors and idempotent operations.
12. Logs include a correlation ID.
13. Release resources (connections, files, locks) even on error.
14. Validate input at the system boundary.
15. Source files are at most 500 lines, excluding generated files; if exceeded, split by responsibility. Applies to new files and files modified in the Task; existing files already over the limit are split only when the Task touches them.
