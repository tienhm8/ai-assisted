# Authentication & RBAC – NestJS guards

> Áp dụng cho: NestJS 11.x, 12.x. Trạng thái: Approved (2026-11-20), chưa chạy thử bằng Task thật.

The approved policy and permission matrix win over anything here; verify decorator and metadata names in the codebase.

## 1. Deny by default is not the framework default (step 3)

- A NestJS guard that finds no metadata decides for itself. In aisoft-backend, `SystemRoleGuard` returns `true` when the route and its controller declare no role, so a controller carrying only `@Authorization()` is open to **every authenticated user**. A guard that reads metadata must treat "metadata missing" as the policy says; if the policy is deny by default, report that the guard allows by default instead of working around it in each controller.
- A new controller or route is protected only when it states its roles or permission explicitly (in aisoft-backend `@AllowSystemRoles(...)`, or the factory default of `BaseControllerFactory`). Before writing one, read how the codebase declares roles; do not assume the composite decorator (`@Authorization()`) restricts anyone beyond logging in.
- Changing a shared guard so that a missing declaration denies is a change to the permission policy and an existing-behavior break for routes that rely on it: stop and report (Entry gate: Tech Lead and Security approval). Do not edit it inside a feature Task.
- Destructive or bulk routes (rewriting data across collections, import, delete-many) always need an explicit narrowest role, not "any logged-in user".

## 2. Where guards read metadata (step 3)

- `Reflector.get(key, handler) || Reflector.get(key, class)` lets an empty array on the handler fall through to the class: `[]` is truthy, so check the code reads handler first and that `undefined` and `[]` mean what the policy says. Prefer `getAllAndOverride`, which returns `undefined` when absent (handle it, `nestjs-11.md` §0.1).
- Metadata lookups use string keys (`'system-roles'`). A typo in the key silently yields `undefined` and therefore, with §1, allows access. Use the exported constant, never a literal.
- Guard order is the order given to `@UseGuards(...)`; authentication guard first, so role and ownership guards can rely on `request.user`.
- Guards run before pipes: a guard must not trust `body`, `query` or `params` shape (`nestjs-11.md` §7). Resource ownership checks that need a record id read it from the validated service layer, not from a raw header or body field the client controls.
- A guard written with `switchToHttp()` does not work for TCP or gRPC handlers (no HTTP request). If the controller is also exposed through a microservice, check how the transport authenticates (`nestjs-microservices.md` §3) before relying on the HTTP guard.

## 3. Public and internal routes (step 3)

- Marking a controller public or internal (for example `PublicController`, `InternalController` with an API-key guard) removes or replaces the user guards. Check what the decorator actually applies before adding a route to it, and never move an existing authenticated route into a public controller to avoid a guard failure.
- A guard that compares a shared header value (API key) is authentication of a service, not of a user. Compare in constant time and never log the value (`security-standards` §9); where the key is not defined in the approved policy, stop and record an open question.

## 4. Test cases (step 6)

Add to the cases the Skill already lists:
- A route in the diff with no role declaration: the test must show the response for an authenticated user with the lowest role, and the result must match the permission matrix.
- A guard unit test that builds the guard with a `Reflector` and an `ExecutionContext` whose handler has no metadata, with an empty array, and with each allowed role.
- Run the guard in the real module (e2e or integration) rather than only with a mocked `Reflector`: `app.useGlobal*()` enhancers from `main.ts` are not present in tests (`nestjs-11.md` §8).
