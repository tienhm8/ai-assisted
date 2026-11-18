---
name: refactoring
description: Improve internal code structure (readability, maintainability) while keeping observable behavior unchanged; baseline tests before and compare after; no schema/contract/API changes.
---

# Refactoring Skill

Improve code structure while keeping observable behavior unchanged.

## Entry gate

- The refactor Task states its scope clearly. If missing, stop and ask.
- Task bundled with a bug fix or new feature: split into a separate Task.
- A large refactor needs an approved Plan before editing.

Primary sources: Task and its manifest; existing source code and tests.
If the manifest lacks something, look up only the exact section, do not read the whole file: module-design §3 Phụ thuộc giữa các module, §5 Ranh giới và quyền sở hữu; system-architecture §3.3 Các tầng và trách nhiệm; coding-standards §6 Thực hành lập trình, §7 Kiến trúc và thiết kế trong code, §8 Chất lượng code.

## Procedure

1. **Understand current behavior:** public interface, business rules, dependencies, areas already tested.
2. **Baseline:** take pre-refactor test results from the output of the baseline Task named in `inputs` of the manifest; if none, run relevant tests and record pre-existing failures. Where tests are missing, add tests describing current behavior before editing.
3. **Choose targets:** only issues affecting the Task (duplication, oversized functions or classes, tangled conditionals, tight or circular dependencies, unclear names, hard to test).
4. **Check constraints:** if schema, contract, API, or module boundary changes are needed, stop and report.
5. **Refactor in small steps**, running tests after each step.
6. **Compare with baseline:** inputs/outputs, errors, access permissions, side-effect order unchanged.

## Limits

- Do not add features, change behavior, or bundle bug fixes.
- Do not claim performance improvements without measuring.

## Done when

- Post-refactor tests match the baseline; no test deleted or weakened.
- The project's check gate passes.

## Report

Write in the Task's handoff report: issues addressed, baseline vs. post-refactor results, remaining technical debt.
