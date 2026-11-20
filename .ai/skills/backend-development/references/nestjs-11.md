# Backend Development – NestJS 11

> Nguồn: github.com/kadajett/agent-nestjs-skills, skill `nestjs-best-practices` v1.2.0 @ 3986e0c · Ngày lấy: 2026-11-14 · Áp dụng cho: NestJS 11.x (đối chiếu lại ngày 2026-11-20 với mã `@nestjs/core` và `@nestjs/common` 11.1.29, `@nestjs/event-emitter` 3.0.1, `@nestjs/sequelize` 11.0.1; project aisoft-backend dùng `@nestjs/core ^11.2.7`)
> Đã điều chỉnh: chỉ giữ lỗi AI hay mắc riêng của NestJS (module, DI, scope, lifecycle, event, validation, serialize, transaction, test). Bỏ: kiến thức chung (feature module, SRP, ISP, LSP, N+1); phần trái `docs/`, Rule (ném `HttpException` từ service, cache bằng `CacheModule`, `console.log`, Supertest cho E2E, gọi dịch vụ ngoài trong transaction); phần là quyết định kiến trúc/hạ tầng hoặc thêm dependency (repository pattern, event-driven, JWT, throttler, sanitize HTML, microservice, queue, health check, versioning, config, logging). Sửa: handler `@OnEvent` lỗi không làm sập process mà bị nuốt lỗi (mặc định `suppressErrors: true`). Không lấy script build và code minh hoạ. Đối chiếu 2026-11-20: các mục §1–§7 giữ nguyên nội dung vì đã kiểm đúng trên 11.1.29 (`ValidationPipe.toValidate` bỏ qua String, Boolean, Number, Array, Object, Buffer, Date; `@OnEvent` mặc định `suppressErrors ?? true` ở event-emitter 3.0.1). Thêm §0 (khác biệt 11 so với 12 và 10) và sửa §2, §7 theo `package.json` của project.
> Nguồn: github.com/affaan-m/ecc, skill `nestjs-patterns` @ d2ef268 · Ngày lấy: 2026-11-14 · Áp dụng cho: NestJS 11.x (đối chiếu như trên)
> Đã điều chỉnh: chỉ lấy 2 điểm chưa có ở trên: `ValidationPipe` bỏ qua tham số kiểu nguyên thuỷ và mảng (§5), pipe/filter global khai báo ở `main.ts` không có trong app test (§7). Bỏ: cấu trúc thư mục, repository, config/env, production defaults (quyết định kiến trúc/hạ tầng); exception filter `@Catch()` và ném framework exception cho lỗi client (trái error-handling §4, §5); guard/role (thuộc security-standards §4, Skill `authentication-rbac`); kiến thức chung (controller mỏng, DTO `class-validator`, response DTO đã có ở §5). Không lấy code minh hoạ.
> Nguồn: docs.nestjs.com, `migration.md` của NestJS 11 (tag 11.0.0) và trang migration-guide v12 · Ngày lấy: 2026-11-20 · Áp dụng cho: NestJS 11.x. Đã điều chỉnh: chỉ lấy thay đổi phá vỡ 10→11 (§0.1) và điểm khác 11↔12 (§0.2) mà AI hay làm sai; bỏ GraphQL, NATS, Terminus, Webpack/rspack vì project không dùng hoặc chưa kiểm.

Reference for Skill `backend-development`. Load only when `stack` has `backend: nestjs@11`, and only the section for the current step. Project conventions (error-handling, security-standards, module-design) win over anything here; where a section says "per the project", look it up there.

## 0. Version notes (steps 2, 3)

Do not copy patterns from NestJS 12 documentation or from `nestjs-12.md` examples into this project without checking them here.

### 0.1 Changed from NestJS 10 to 11 (still applies to code in this project)

- **Express 5 is the default platform.** Route wildcards must be named: `/*splat` or `/{*splat}`, not `/*`. The optional `?` is gone (use braces `/users{/:id}`). Characters `( ) [ ] ? + !` are reserved and need `\`. Applies to `@Get()`, `@All()`, `forRoutes()` and `MiddlewareConsumer`. A legacy path like `forRoutes('*')` or `'/files/*'` fails or matches differently: check before copying.
- **Dynamic module identity is by object reference**, not by a hash of its options. Calling `XModule.forRoot(opts)` in two places creates two module instances (two copies of its providers). Assign the result to one variable and import that variable, or follow what the codebase already does.
- **Termination hooks run in reverse order of init hooks** (`onModuleDestroy`, `beforeApplicationShutdown`, `onApplicationShutdown`). A resource opened first closes last; do not rely on the old order.
- **`Reflector`:** `getAllAndOverride` returns `T | undefined`, so handle `undefined`; `getAllAndMerge` returns an object, not a one-element array, when the only metadata is an object.
- **`@nestjs/cache-manager` moved to Keyv.** The `store: redisStore` option no longer works; use `stores: [new KeyvRedis(...)]`. The project does not list `@nestjs/cache-manager`; Redis caching follows the `caching` Skill, not `CacheModule`.
- **`@nestjs/config` 4:** values set by `registerAs`/`load` take precedence over `process.env`. `ignoreEnvVars` is deprecated (use `validatePredefined`).
- **Node.js 20 or higher.** The project requires `>=24`.

### 0.2 Differs from NestJS 12 (do not apply 12 advice here)

- In 12, init and shutdown hooks run by component hierarchy level, which can change their order. Do not reorder code for 12 behavior, and do not assume the 12 order.
- In 12, `@Optional()` is not inherited by a subclass that redeclares its constructor and Nest throws `UnknownDependenciesException`. Declare `@Optional()` on the subclass constructor parameter too, so the code works on both versions.
- 12 requires Joi 18 for `@nestjs/config` schemas and removes legacy Terminus `HealthIndicator`/`HealthCheckError`; with `@nestjs/terminus ^11.1.1` the legacy API still exists.
- `@nestjs/event-emitter` is 3.x for NestJS 11 (12.x for NestJS 12); `@nestjs/sequelize` 11.x and `@nestjs/mongoose` 11.x for 11. Never bump a `@nestjs/*` package to 12 inside a feature Task (`project-rules` 6).
- `ConsoleLogger` structured params are the default only in 12.
- 12 packages are ESM-only and Jest loads them only on Node 24.9+. This is a 12 upgrade concern, not part of a feature Task.

## 1. Modules and dependencies (steps 2, 3)

- Each provider is declared in `providers` of exactly one module, exported, and consumers import that **module**. Listing the same class in `providers` of a second module creates a second instance with separate state.
- `@Global()` only for cross-cutting infrastructure already global in the codebase; do not make a feature module global to avoid an import.
- A module import cycle means the module boundary is wrong. Do not fix it with `forwardRef()`; check module-design §3 and move the shared part or report it. Use `forwardRef()` only where the codebase already does, with a reason written in place.
- Do not resolve dependencies at runtime with `ModuleRef.get()`/`resolve()` (service locator). Use constructor injection; property injection only for an optional dependency in a base class.
- TypeScript interfaces are erased at runtime and cannot be injection tokens. Use a `Symbol`/string token with `@Inject(TOKEN)` or an abstract class, following what the codebase already uses.

## 2. Provider scope (step 3)

- Default scope is singleton, shared by all concurrent requests: never keep per-request data (user, tenant, correlation ID) in an instance field.
- `Scope.REQUEST` spreads to every provider that injects it, directly or transitively, which then becomes request-scoped too (cost on every request). Before adding it, check what depends on the provider. For request context, use the mechanism the codebase already has: aisoft-backend lists `nestjs-cls` in `package.json`; find where it is configured before adding another mechanism (a new library falls under `project-rules` 6).

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
- API/integration tests that call the HTTP app use the tool in testing-strategy §4; E2E per `testing-rules` 9 (Playwright). `supertest` is in the project's devDependencies; use it only as testing-strategy §4 says.
