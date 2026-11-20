# Backend Development – Mongoose (ODM) with `@nestjs/mongoose`

> Nguồn: mongoosejs.com/docs/migrating_to_9.html và docs.nestjs.com/techniques/mongodb · Ngày lấy: 2026-11-20 · Áp dụng cho: Mongoose 9.x (đối chiếu kiểu của `mongoose` 9.8.0: `returnDocument`, `Connection.transaction`, `engines.node >=20.19.0`) với `@nestjs/mongoose` 11.x (đối chiếu 11.0.4, `peerDependencies mongoose ^7 || ^8 || ^9`); project aisoft-backend dùng `mongoose ^9.8.0`, `@nestjs/mongoose ^11.0.4`
> Đã điều chỉnh: chỉ giữ thay đổi phá vỡ 8→9 và lỗi AI hay mắc khi viết schema, query, transaction, hook trong NestJS. Bỏ: cú pháp cơ bản của schema và query (kiến thức chung), `MongooseModule.forRoot` và `forRootAsync` (project đã cấu hình ở `src/config/module/config.ts`), discriminator, multi-database, kết nối sự kiện (chưa có Task cần). Không lấy code minh hoạ. Chưa chạy thử bằng Task thật: trạng thái Draft cho tới khi có Task chạy thử (`.ai/guide/external-skills.md` bước 5).

Reference for Skill `backend-development`. Load only when `stack` has `odm: mongoose@9`, and only the section for the current step. Rules (`database-rules`, `security-rules`, `coding-rules`) and error-handling win over anything here; for NestJS wiring see `nestjs-11.md`; for modeling and indexes see `database-design/references/mongodb.md`.

## 1. Version check and schemas (steps 2, 3)

- Read the installed `mongoose` version before using any API; Mongoose 9 needs Node `>=20.19.0`. Follow how the codebase declares schemas: `@Schema()`, `@Prop()`, `SchemaFactory.createForClass()` (user, one-signal) or a raw `Schema` registered through `MongooseModule.forFeature` (`src/modules/repository/mongo/mongoose-model.ts` adds `dataPartitionCode` to every schema in a list). Do not mix styles inside one module.
- `@Prop()` infers the type from TypeScript metadata only for simple types. Arrays, nested objects, `Map`, unions and `ObjectId` references need an explicit type: `@Prop([String])`, `@Prop({ type: Types.ObjectId, ref: 'X' })`. Without it the property becomes `Mixed` or fails at startup.
- `@Schema()` names the collection from the class name, lowercased and pluralized. Set `collection` explicitly when the collection already exists in the database, or Mongoose reads or creates a different one.
- `unique: true`, `index: true` and `sparse` on `@Prop` create indexes through `autoIndex` at startup, not constraints at write time. Index creation is a schema change: check whether `autoIndex` is enabled in the connection config before adding one, and handle it per `database-design`.
- Register every schema in the module that uses it with `MongooseModule.forFeature`, and export it if another module needs the model. A model injected from a module that did not import it fails with an unresolved dependency.
- `UUID` fields come back as `bson.UUID` objects in 9, not strings (JSON output is a hex string). Normalize at the boundary when the contract says string.
- `new mongoose.Types.ObjectId(6)` throws in 9 and `isValidObjectId(6)` is `false`. Validate input ids before casting.

## 2. Queries and updates (step 4)

- `findOneAndUpdate` and `findOneAndReplace` return the **old** document by default. Pass `returnDocument: 'after'` to get the new one. `new` and `returnOriginal` still work in 9.x but are deprecated and log a warning: use `returnDocument` in new code.
- Update pipelines (an array as the update) throw in 9 unless `updatePipeline: true` is passed or set globally. Do not turn the global setting on to silence the error.
- Filters are cast to the schema, but a key that is not in the schema is passed to MongoDB unchanged unless `strictQuery` is enabled (the default is `false` since Mongoose 7; check the connection config). A typo in a filter key therefore returns no rows, and `updateMany`/`deleteMany` with it touches none or, with an empty object, **every** document. Validate filter inputs before bulk writes. Do not build a filter from unvalidated input: operators such as `$ne`, `$gt` in a body field are an injection path (`security-rules` 3).
- `Model.updateMany`, `deleteMany` and `bulkWrite` do not run document middleware (`save` hooks, validators for updates unless `runValidators: true`). Check which hooks the schema has before choosing a bulk write.
- `.lean()` returns plain objects: no getters, virtuals, `id`, defaults applied on read, or methods, and `ObjectId` values stay `ObjectId`. Map to a response DTO either way (`nestjs-11.md` §5).
- Lists use `limit` and a stable `sort` including `_id`; deep `skip` is slow (`database-rules` 9). Select only needed fields with `select` or a projection.
- `populate` runs an extra query per path and returns `null` when the referenced document is missing; it is not a join and does not enforce references. Do not populate in a loop.
- `create()` and `insertOne()` no longer accept a generic parameter in the types; they take `Partial<RawDocType>`. `FilterQuery` is renamed `QueryFilter`. Do not silence type errors with `any`; cast the input once at the boundary.
- Document `id` is a `string` virtual in the types. Use `_id` for the `ObjectId`.

## 3. Transactions (step 4)

- MongoDB transactions need a replica set or sharded cluster; the project's `example.env` uses `replicaSet=rs0`. On a standalone server a transaction fails, so a test that passes locally on standalone proves nothing.
- Use `connection.transaction(async (session) => ...)` (inject the connection with `@InjectConnection()`). It retries on transient errors and ends the session. If you use `startSession()` yourself you must `commitTransaction()` or `abortTransaction()` and `endSession()` in `finally`.
- Pass `{ session }` to **every** read and write inside the callback, including `create([doc], { session })` (the array form is required with a session) and calls made by services the callback invokes. A call without it runs outside the transaction and is not rolled back. Mongoose does not carry the session automatically.
- The callback can run more than once on a transient error: keep it free of side effects (events, emails, cache deletes); do those after commit (`database-rules` 24, error-handling §9).
- MongoDB and Sequelize transactions are separate. A Task that writes to PostgreSQL and MongoDB cannot make both atomic with either API: stop and record an open question per `backend-development` Limits.

## 4. Middleware and hooks (step 4)

- Mongoose 9 pre hooks have no `next()` parameter. Write `schema.pre('save', async function () { ... })` and throw to abort. A hook still taking `next` or using `isAsync` breaks on upgrade.
- Hooks run on custom methods and statics only when they are `async` or return a promise.
- `pre()` and `post()` must be registered **before** the model is compiled. In NestJS use `MongooseModule.forFeatureAsync` and register the hook in the factory; a hook added after `forFeature` compiled the model is ignored.
- A subdocument `deleteOne()` hook fires only when the parent is saved.
- Query middleware (`pre('findOneAndUpdate')`) does not see the document, only the query; document middleware (`pre('save')`) does not run for `updateOne` on a query.

## 5. Errors (step 5)

- Error classes: `MongoServerError` with `code` 11000 for a duplicate key (the field is in `keyPattern`; do not expose `keyValue` in responses), `mongoose.Error.ValidationError`, `CastError` (bad id or type), `DocumentNotFoundError` and `VersionError` (concurrent array edit on `save`), `MongoNetworkError`, `MongoServerSelectionError`.
- Map to the project's codes in one place per error-handling §3, §4. `ValidationError` and `CastError` come from input the service should have validated; a `CastError` reaching the client as 500 is a missing check.
- Do not catch code 11000 to implement "insert if absent" unless the design chose that. Use the unique index as the guard and map the error.
- Without `{ upsert: true }` an update that matches nothing returns a result with `matchedCount: 0` and no error: check it when the AC requires "must exist".

## 6. Tests (step 8)

- Unit tests replace the model with `{ provide: getModelToken(X.name), useValue: mock }`, using the same token as production code (`nestjs-11.md` §7). A Mongoose query is thenable and chainable (`find().sort().lean().exec()`): the mock must return an object with the same chain, or the test passes on a mock that cannot occur.
- Integration tests run on a disposable MongoDB replica set of the project's server version, never on a shared database (`project-rules` 13).
