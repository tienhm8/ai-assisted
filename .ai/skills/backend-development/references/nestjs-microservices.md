# Backend Development – NestJS microservices (hybrid app, TCP, gRPC) and scheduled jobs

> Áp dụng cho: `@nestjs/microservices` 11.x (TCP, gRPC), `@nestjs/schedule` 6.x. Trạng thái: Approved (2026-11-20), chưa chạy thử bằng Task thật.

Transport choice, ports and message patterns are project decisions in the architecture docs, not made in a feature Task. Verify option names in the installed package types.

## 1. Hybrid application (steps 2, 3)

- One process can serve HTTP and one or more microservices (`app.connectMicroservice()` then `app.startAllMicroservices()`). They share one DI container: a provider is a single instance for HTTP, gRPC and TCP handlers alike. Per-request data must not live in an instance field (`nestjs-11.md` §2); the same applies across transports.
- Check how the entrypoint wires the transports (`main.ts`) before adding a handler. Do not add a second `connectMicroservice` call or change `deferInitialization`/`registerListeners()`/`setIsInitialized()` ordering inside a feature Task: it decides whether lifecycle hooks run again on the shared container. That is an architecture change (`project-rules` 5).
- `startAllMicroservices()` must come before `listen()` completes in the order the codebase already uses; a handler registered after start is not bound.

## 2. Global enhancers do not carry over (steps 4, 5)

- Pipes, guards, interceptors and filters set with `app.useGlobal*()` apply to HTTP only. A microservice connected without `inheritAppConfig: true` gets its own empty configuration, so validation, response transform, audit and error mapping silently do not run for TCP or gRPC handlers. Check that the entrypoint calls `microservice.useGlobal*()` for each one the transport needs; aisoft-backend does this for TCP in `main.ts` (payload transform interceptor, audit-log interceptor, common exception filter) and does not for gRPC.
- A new handler on a transport therefore needs: input validation on its own (`@UsePipes(new ValidationPipe(...))` or the transport's pipe, since the HTTP global pipe is absent), error mapping through the transport's filter (HTTP exception filters do not format RPC errors), and its own authentication. Do not copy a controller's HTTP decorators onto a handler.
- Guards that call `switchToHttp()` fail in an RPC context. Use `switchToRpc()` or `context.getType()` to branch, per the transport's authentication scheme in the architecture docs.
- Throw `RpcException` (or the project's transport error type) from message handlers, not `HttpException`; follow error-handling §4, §5 for the mapping. Do not choose the error shape yourself.

## 3. Message patterns and contracts (step 4)

- `@MessagePattern` (request/response) and `@EventPattern` (fire-and-forget) are different: an event handler's return value and thrown error never reach the sender. Do not use `@EventPattern` for something the caller needs a result or an error from.
- The pattern string and payload shape are a contract with other services: add fields compatibly, never rename or remove one without an Approved contract change (api-design §2 Integration Specification). The project's wrapper may add metadata to the payload (aisoft-backend wraps `__auth`/`__payload` and a trace context); use the existing client and serializer, do not send raw messages around them.
- Authentication on TCP is project-defined (a shared token in the payload when enabled). It is service authentication, not user authentication: see `authentication-rbac`; do not treat a valid service token as a user's permission.
- Clients (`ClientProxy`) calls need a timeout (`timeout()` from rxjs) and follow error-handling §8 for retry; a call without a timeout waits as long as the socket stays open. Do not call another service inside a DB transaction (`nestjs-11.md` §6).
- gRPC: edit the `.proto` only with an Approved contract; keep field numbers stable, never reuse a removed number. The generated types and the proto path are listed in the project config, do not hand-edit generated files.

## 4. Scheduled jobs (steps 3, 4)

- `@Cron`/`@Interval`/`@Timeout` run in **every** instance of the app. With two replicas a job runs twice. Check how the project makes a job single-run (aisoft-backend: `CronManagerService.isCronLeader(...)` guard at the top of the method, leader chosen through Redis) and use that; do not add another coordination mechanism (new dependency or architecture decision).
- Leader election does not make the job idempotent: a leader can change between runs or during one. Write the job so a repeat or an overlap is harmless (`bull-4.md` §1).
- Handle errors inside the method: an exception from a scheduled method is only logged by the scheduler and does not reach an exception filter (`nestjs-11.md` §4). Keep the work short or put it on a queue (`bull-4.md`) and return.
- The cron expression, time zone and frequency come from the Task or Plan; do not pick them. State the time zone when the expression is time-of-day sensitive.
- Two copies of the same module (aisoft-backend has `src/cron-manager` and `src/modules/cron-manager`) mean only one is wired: find the imported one before editing, and report the duplicate in the handoff rather than deleting it (`project-rules` 17).

## 5. Tests (step 8)

- Handler unit tests call the method with a plain payload and a fake context, no socket. Test the transport wiring (validation, filter, interceptor) through an app built the same way as `main.ts`, because a test app made with `createNestApplication()` has none of it (`nestjs-11.md` §8); a TCP integration test needs a free port from the test environment, not the production one.
- Cron: call the method directly with the leader check faked both ways (leader and not leader) and assert the work runs only for the leader. Do not wait for real time to pass.
