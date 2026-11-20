# NestJS + Swagger (`@nestjs/swagger`)

Load for NestJS projects at Procedure step 6. Verify decorator names and options in the installed `@nestjs/swagger` version before use (`project-rules` 16).

Project wrappers first: if the project already wraps Swagger decorators (response helpers, controller or auth decorators), use them; do not mix in raw decorators for the same purpose. Wrappers and security scheme names are project conventions, not defined here.

## 1. Setup (once per project)

- Build the document in `main.ts` before `app.listen`: `DocumentBuilder` (title, servers, auth schemes) → `SwaggerModule.createDocument` → `SwaggerModule.setup`.
- Every auth scheme used by a guard is declared in `DocumentBuilder` (`addBearerAuth`, `addApiKey`) under a name; endpoints reference that name.
- Docs are not public by default: protect them (basic auth or network limit) or disable them in production. Never put real secrets in examples or default values.
- Setup is a 🟡 shared change: only edit it when the Task says so.

## 2. Controllers and endpoints

Every endpoint declares:
- Group: `@ApiTags` on the controller.
- Purpose: `@ApiOperation({ summary })`.
- Auth: `@ApiBearerAuth` / `@ApiSecurity(<scheme name>)` matching the guards actually applied; no doc claiming auth the code does not enforce, and no guarded route left undocumented.
- Inputs: `@ApiParam`, `@ApiQuery` (including pagination, sort, filter fields in the contract).
- Success: `@ApiResponse` / `@ApiOkResponse` with a typed schema, never a bare `any`.
- Errors: one entry per status code and error code in the contract (error-handling §3, §5).

## 3. DTOs

- Every request/response field has `@ApiProperty` / `@ApiPropertyOptional` with type, `required`, enum, format; or enable the Nest CLI Swagger plugin and follow how the project configured it (do not duplicate what the plugin infers).
- Derive DTOs with `PickType`, `OmitType`, `PartialType`, `IntersectionType` imported from `@nestjs/swagger`, not `@nestjs/mapped-types`, or metadata is lost.
- Arrays: `@ApiProperty({ type: [Dto] })`; enums: `enum` + `enumName`.
- Generic envelopes (record, list, page): `ApiExtraModels` + `getSchemaPath` composed in one reusable decorator; do not copy a schema per endpoint.
- Response DTO exposes only contract fields (matches `security-standards` §8).

## 4. Verify

- App builds and starts; the document JSON (`<path>-json`) contains the new endpoint.
- Compare paths, methods, params, status codes, schemas and auth against the api-design contract; any gap is a bug in either doc or code, report which.
- No endpoint in the diff missing tag, operation, response or auth entry.
