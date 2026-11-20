# Backend Development – NestJS

> Áp dụng cho: NestJS 12.x. Project NestJS 11 dùng `nestjs-11.md`.

Project conventions (error-handling, security-standards, module-design) win over anything here.

## 1. Modules and dependencies (steps 2, 3)

- Each provider is declared in `providers` of exactly one module, exported, and consumers import that **module**. Listing the same class in `providers` of a second module creates a second instance with separate state.
- `@Global()` only for cross-cutting infrastructure already global in the codebase; do not make a feature module global to avoid an import.
- A module import cycle means the module boundary is wrong. Do not fix it with `forwardRef()`; check module-design §3 and move the shared part or report it. Use `forwardRef()` only where the codebase already does, with a reason written in place.
- Do not resolve dependencies at runtime with `ModuleRef.get()`/`resolve()` (service locator). Use constructor injection; property injection only for an optional dependency in a base class.
- TypeScript interfaces are erased at runtime and cannot be injection tokens. Use a `Symbol`/string token with `@Inject(TOKEN)` or an abstract class, following what the codebase already uses.

## 2. Provider scope (step 3)

- Default scope is singleton, shared by all concurrent requests: never keep per-request data (user, tenant, correlation ID) in an instance field.
- `Scope.REQUEST` spreads to every provider that injects it, directly or transitively, which then becomes request-scoped too (cost on every request). Before adding it, check what depends on the provider. For request context, use the mechanism the codebase already has; adding a library (for example `nestjs-cls`) falls under `project-rules` 6.

## 3. Lifecycle (step 4)

- An async `onModuleInit`/`onApplicationBootstrap` must `return`/`await` its promise; otherwise the app starts before the resource is ready.
- Constructors stay synchronous and light; I/O goes into lifecycle hooks. Work that needs other modules initialized goes into `onApplicationBootstrap`, not `onModuleInit`.
- `onModuleDestroy`/`beforeApplicationShutdown`/`onApplicationShutdown` only run on SIGTERM/SIGINT when `app.enableShutdownHooks()` is called in bootstrap; check it exists before relying on them to release resources.

## 4. Errors in async work (step 5)

- Exceptions are caught by exception filters only on the request path. Errors in fire-and-forget promises, `@OnEvent`, `@Cron`/`@Interval` must be handled in place per error-handling §4, §7, §8.
- `@OnEvent` handlers (`@nestjs/event-emitter`) default to `suppressErrors: true`: the error is only written to the Nest logger and swallowed, so the caller does not know. Handle errors in the handler (log with correlation ID, retry/compensate per the spec); do not rely on the default.
- Do not leave an un-awaited promise without `.catch()`. In a handler, `return`/`await` the inner async call.
- Exceptions thrown from services follow the project's hierarchy and mapping (error-handling §4, §5); do not choose `HttpException` vs domain exception yourself.

## 5. Input validation and output (step 4)

- Validation per security-standards §5. Check the global `ValidationPipe` config in bootstrap before writing a DTO: without `whitelist`, extra fields pass through to the service (mass assignment); without `transform`, `@Query()`/`@Param()` values stay strings even when typed `number`.
- `transformOptions.enableImplicitConversion` turns the query string `"false"` into `true` for a `boolean` field. For booleans, parse explicitly with `@Transform`.
- `ValidationPipe` skips parameters typed as a primitive (`string`, `number`, `boolean`), `Array`, `Object` or `Date`: `@Param('id') id: string` and `@Body() items: CreateItemDto[]` are not validated at all. Use `ParseUUIDPipe`/`ParseIntPipe`/`ParseBoolPipe` (or a param DTO) for primitives and `ParseArrayPipe({ items: Dto })` or a wrapper DTO for array bodies.
- Nested DTOs need both `@ValidateNested()` and `@Type(() => Child)`; with only one, the child object is not validated.
- Do not return ORM entities from controllers; map to a response DTO per api-design. `ClassSerializerInterceptor` with `@Exclude()` only works on class instances: plain objects (raw queries, spread `{...entity}`) are not filtered unless `@SerializeOptions({ type })` is declared.

## 6. Transactions (step 4)

- Inside a transaction, every write uses the transaction's manager/client (for example `manager` from `DataSource.transaction()`, the Prisma `tx`). An injected repository/service outside the transaction writes on another connection and is not rolled back.
- Do not call external services or publish events inside a DB transaction; do it after commit per error-handling §9.
- Do not enable schema auto-sync (TypeORM `synchronize`, etc.) in any shared environment; schema changes stop per this Skill's Limits.

## 7. Tests (step 8)

- Unit tests build the module with `Test.createTestingModule()` and replace dependencies with `useValue`/`overrideProvider()` using the **same token** as production code; call `compile()` before `get()`.
- Global pipes/filters/interceptors registered with `app.useGlobal*()` in `main.ts` are absent from an app built by `createNestApplication()` in tests, so validation and error mapping silently differ from production. Apply the same setup in the test (reuse the bootstrap setup function if the codebase has one), or rely on enhancers registered as `APP_PIPE`/`APP_FILTER`/`APP_INTERCEPTOR` providers, which come with the imported module.
- Request-scoped/transient providers are fetched with `resolve()`, not `get()`.
- API/integration tests that call the HTTP app use the tool in testing-strategy §4; E2E per `testing-rules` 9 (Playwright). Do not add Supertest when the project has not chosen it.
