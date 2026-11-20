# Module Design

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Draft |
| Người phụ trách |  |
| Người duyệt (dự án) | Kiến trúc sư |
| Phiên bản · Ngày |  |
| Tài liệu liên quan | system-architecture.md, database-design.md, api-design.md, ../01-requirements/FR/, ../01-requirements/business-rules.md, ../03-engineering/error-handling.md, ADR/, ../../.ai/rules/architecture-rules.md, ../../.ai/skills/backend-development/SKILL.md |

> **Mục đích.** Module Architecture: chia module, trách nhiệm, API nội bộ và chiều phụ thuộc.

## 1. Tổng quan module

### 1.1 Cách phân loại
Chia theo domain hoặc năng lực nghiệp vụ. Mã `<MODULE>` dùng thống nhất với `FR-<MODULE>-<NN>` và `BR-<MODULE>-<NN>`.

Hiện trạng của `aisoft-backend` (NestJS): mỗi thư mục con của `src/modules` là một module Nest (một file `*.module.ts`), cộng `src/cron-manager` và công cụ CLI `lib/@aisoft`. Danh mục này là Inventory mức 1, mỗi module một dòng; hồ sơ sâu để mục 2.

- **Mã module** là **mã tạm**: tên thư mục viết hoa, chưa thống nhất với mã dùng trong mã yêu cầu hay business rule.
- **Mức quan trọng** (Core/Supporting/Optional) là nhận định của người ghi: Core nếu nằm trong `DefaultModules` (`src/config/module/config.ts:36-91`) hoặc được nhiều module khác dùng; Supporting nếu chỉ được `src/app.module.ts:20-39` nạp; Optional nếu không được nạp ở đâu. Không phải kết luận chuẩn.
- Mọi nhận định có nguồn dạng `file:dòng` (đường dẫn từ gốc project `aisoft-backend`); chưa kiểm chứng ghi "giả thuyết".
- Tài liệu Draft; căn cứ chỉ để tham khảo.

### 1.2 Danh sách module
| Mã module (tạm) | Tên | Trách nhiệm | Phụ thuộc | FR phục vụ | Chủ module |
| --- | --- | --- | --- | --- | --- |
| AUDIT-LOG | audit-log | Ghi nhật ký thao tác qua interceptor và queue; có cron dọn dẹp mỗi 12 giờ (`src/modules/audit-log/audit-log.service.ts:37`) | repository (`audit-log.module.ts:1-8`) | Chưa có | Chưa có |
| AUTH | auth | Xác thực; có controller public và controller thường (`src/modules/auth/auth-public.controller.ts:12`, `auth.controller.ts:8`) | repository, user (`auth.module.ts:1-6`) | Chưa có | Chưa có |
| BASE-LOGGER | base-logger | Ghi log chung; `BaseLoggerModule` đang bị comment trong DefaultModules (`src/config/module/config.ts:84`) | Giả thuyết: không phụ thuộc module khác (`base-logger.module.ts:6`) | Chưa có | Chưa có |
| COMMON-PROVIDER | common-provider | Provider dùng chung; nạp ở mức hệ thống (`config.ts:87`) | Giả thuyết: chưa đọc service (`common-provider.module.ts:7`) | Chưa có | Chưa có |
| CORE | core | Cung cấp `CoreInternalService` (`src/modules/core/core.module.ts:5`) | Giả thuyết: chưa đọc service | Chưa có | Chưa có |
| CRON-MANAGER | cron-manager | Quản lý cron (`CronManagerService`, module `@Global`). Có HAI bản module giống nhau: `src/cron-manager/cron-manager.module.ts:4-9` (được nạp, `config.ts:90`) và `src/modules/cron-manager/cron-manager.module.ts:4-9` | Không import module khác | Chưa có | Chưa có |
| DATA-PARTITION | data-partition | Phân vùng dữ liệu theo người dùng (cây thư mục gốc/cây con) (`src/modules/data-partition/controllers/data-partition-internal.controller.ts:23-67`) | repository (Mongo và SQL transaction) (`data-partition.module.ts:1-5`) | Chưa có | Chưa có |
| DATA-PROCESS | data-process | Xử lý dữ liệu; có controller (`src/modules/data-process/data-process.controller.ts:7`) | Giả thuyết: chưa đọc service | Chưa có | Chưa có |
| FILE | file | Quản lý file, có controller public (`src/modules/file/file.controller.ts:24`, `file-public.controller.ts:6`) | repository (`file.module.ts:1-4`) | Chưa có | Chưa có |
| HEALTH | health | Kiểm tra sức khoẻ (`src/modules/health/health.controller.ts:7`) | redis (`health.module.ts:3`) | Chưa có | Chưa có |
| IMPORT-SESSION | import-session | Chỉ có thư mục `entities`; module rỗng `@Module({})` (`src/modules/import-session/import-session.module.ts:3`) | Không có | Chưa có | Chưa có |
| INCREMENT | increment | Bộ đếm tăng dần (`src/modules/increment/increment.module.ts:9`) | repository (`increment.module.ts:1-2`) | Chưa có | Chưa có |
| INTERNAL-HTTP | internal-http | Client HTTP gọi nội bộ, không theo redirect (`src/modules/internal-http/internal-http.module.ts:8`) | `@nestjs/axios` | Chưa có | Chưa có |
| MICROSERVICE | microservice | Client gRPC/TCP, `@Global`, nhúng `TelemetryModule` từ `@aisoft/backend-observer` (`src/modules/microservice/microservice.module.ts:1,17-31`) | `@aisoft/backend-observer` (package ngoài) | Chưa có | Chưa có |
| MINIO | minio | Lưu trữ đối tượng MinIO (`src/modules/minio/minio.controller.ts:3`, `minio.provider.ts`) | Giả thuyết: chưa đọc provider | Chưa có | Chưa có |
| NOTIFICATION | notification | Thông báo (`src/modules/notification/notification.module.ts:13`) | one-signal, repository (`notification.module.ts:1-3`) | Chưa có | Chưa có |
| ONE-SIGNAL | one-signal | Đẩy thông báo qua OneSignal bằng queue Bull (`src/modules/one-signal/one-signal.module.ts:17-26`, `provider/one-signal.process.ts:16`) | auth, topic, repository (`one-signal.module.ts:2-6`) | Chưa có | Chưa có |
| QUY-TAC-MA | quy-tac-ma | Quy tắc mã và hàm sinh mã (`src/modules/quy-tac-ma/quy-tac-ma.module.ts:13-14`) | repository (`quy-tac-ma.module.ts:1-2`) | Chưa có | Chưa có |
| REDIS | redis | Cung cấp Redis client (`src/modules/redis/redis-client.provider.ts`) | Giả thuyết: chưa đọc provider | Chưa có | Chưa có |
| REPOSITORY | repository | Lớp truy cập dữ liệu Mongo và Sequelize, cấu hình kết nối (`src/modules/repository/repository.module.ts:1`; `config.ts:65-80`) | Mongoose, Sequelize | Chưa có | Chưa có |
| SETTING | setting | Cấu hình hệ thống (`src/modules/setting/setting.module.ts:18`) | repository (`setting.module.ts:2-5`) | Chưa có | Chưa có |
| SSO | sso | Đăng nhập một lần (`src/modules/sso/sso.controller.ts:6`) | auth, user, repository (`sso.module.ts:1-4`) | Chưa có | Chưa có |
| TOPIC | topic | Chủ đề và đăng ký chủ đề của người dùng (`src/modules/topic/topic.module.ts:11-12`) | repository (`topic.module.ts:1-2`) | Chưa có | Chưa có |
| USER | user | Quản lý người dùng, có import (`src/modules/user/controller/user.controller.ts:15`, `user-import.controller.ts:8`) | repository (`user.module.ts:1-6`) | Chưa có | Chưa có |
| CRON-MANAGER (src) | src/cron-manager | Xem dòng CRON-MANAGER: bản được nạp vào `DefaultModules` | Không có | Chưa có | Chưa có |
| @AISOFT-CLI | lib/@aisoft (cli) | CLI `aisoft` sinh mã nền (`base-generate`) cho entity và loại repository (`lib/@aisoft/cli/index.ts:8-16`, `bin/aisoft.js`) | Không phụ thuộc module Nest | Chưa có | Chưa có |

**Bảng bổ sung (database, giao tiếp, mức quan trọng).** Một dòng mỗi module, cùng thứ tự.

| Mã module (tạm) | Database | Giao tiếp | Mức quan trọng (nhận định) | Căn cứ mức |
| --- | --- | --- | --- | --- |
| AUDIT-LOG | Mongo (`audit-log.module.ts:34`) | HTTP; queue Bull (`audit-log.process.ts:17`) | Core | Interceptor toàn cục `config.ts:95-97`; nạp ở `app.module.ts:35` |
| AUTH | Mongo (`auth.module.ts:20-21`) | HTTP | Supporting | Chỉ nạp ở `app.module.ts:23`; module khác dùng |
| BASE-LOGGER | Chưa thấy | Chưa thấy | Optional | Bị comment `config.ts:84`; không thấy nạp ở `app.module.ts` |
| COMMON-PROVIDER | Giả thuyết: không | Giả thuyết: không | Core | `config.ts:87` |
| CORE | Giả thuyết: không | Giả thuyết: nội bộ | Core | `config.ts:89` |
| CRON-MANAGER | Không | Cron nội bộ (giả thuyết) | Core | `config.ts:90` |
| DATA-PARTITION | Mongo; SQL (giả thuyết, `data-partition.module.ts:5`) | HTTP; TCP `MessagePattern` (`data-partition-internal.controller.ts:23-67`) | Core | `config.ts:86` |
| DATA-PROCESS | Giả thuyết: không | HTTP | Supporting | `app.module.ts:36` |
| FILE | Mongo (`file.module.ts:26`) | HTTP | Supporting | `app.module.ts:28` |
| HEALTH | Không | HTTP | Core | `config.ts:85` |
| IMPORT-SESSION | Không (chỉ `entities`, chưa kiểm) | Không | Supporting | Nạp `app.module.ts:33` nhưng module rỗng |
| INCREMENT | Mongo (`increment.module.ts:9`) | Không | Supporting | `app.module.ts:32` |
| INTERNAL-HTTP | Không | HTTP client | Core | `config.ts:88` |
| MICROSERVICE | Không | gRPC, TCP (`microservice.controller.ts:11`, `tcp-version.controller.ts:8`); RabbitMQ bị comment (`microservice.module.ts:28-30`) | Core | `config.ts:82` |
| MINIO | Object storage MinIO | HTTP | Core | `config.ts:83` |
| NOTIFICATION | Mongo (`notification.module.ts:13`) | HTTP | Supporting | `app.module.ts:26` |
| ONE-SIGNAL | Mongo (`one-signal.module.ts:36-40`) | HTTP ra ngoài (`one-signal.module.ts:26`); queue Bull | Supporting | `app.module.ts:25` |
| QUY-TAC-MA | Mongo (`quy-tac-ma.module.ts:13-14`) | HTTP (giả thuyết) | Supporting | `app.module.ts:34` |
| REDIS | Redis | Không | Core | `health` import; `app.module.ts:30` |
| REPOSITORY | Mongo, SQL (`config.ts:65-80`) | Không | Core | `config.ts:81` |
| SETTING | Mongo (`setting.module.ts:18`) | HTTP | Supporting | `app.module.ts:29` |
| SSO | Mongo (`sso.module.ts:13-14`) | HTTP | Supporting | `app.module.ts:31` |
| TOPIC | Mongo (`topic.module.ts:11-12`) | HTTP (giả thuyết) | Supporting | `app.module.ts:27` |
| USER | Mongo (`user.module.ts:20`) | HTTP | Core | `auth`, `sso` dùng user (`auth.module.ts:6`, `sso.module.ts:4`) |
| CRON-MANAGER (src) | Không | Không | Core | `config.ts:90` |
| @AISOFT-CLI | Không (sinh file) | CLI | Supporting | Không nằm trong runtime Nest (giả thuyết) |

Mâu thuẫn và điểm chưa khảo sát: có hai bản `cron-manager` giống nhau (chưa rõ bản trong `src/modules` có dùng không); chưa đọc service của core, common-provider, minio, redis, data-process, base-logger; "SQL" của data-partition mới suy từ import.

Ưu tiên không ghi ở đây: ưu tiên yêu cầu theo MoSCoW ở [FR](../01-requirements/FR/README.md), thứ tự làm ở [task-backlog](../04-project-management/task-backlog.md) và [roadmap](../04-project-management/roadmap.md).

## 2. Chi tiết module
Lặp lại mẫu dưới đây cho từng module. Module nhỏ chỉ cần điền các dòng có nội dung; không viết lại nội dung đã có ở tài liệu khác, chỉ dẫn mã và liên kết.

### 2.1 [Mã module] · [Tên module]

| Hạng mục | Nội dung |
| --- | --- |
| Mục đích và trách nhiệm chính |  |
| Phạm vi (làm / không làm) |  |
| Năng lực nghiệp vụ |  |
| FR liên quan | `FR-<MODULE>-<NN>`; yêu cầu ở [FR](../01-requirements/FR/README.md) |
| Business rule áp dụng | `BR-<MODULE>-<NN>`; nội dung ở [business-rules](../01-requirements/business-rules.md), không chép lại |
| Thành phần bên trong |  |
| Dữ liệu sở hữu | Chỉ ghi tại [database-design](database-design.md) §3.2 (cột "Module sở hữu"); mỗi bảng chỉ một module sở hữu |
| Interface cung cấp | API công khai ở [api-design](api-design.md) §1; interface liên module: tên và mục đích nêu tại đây, hợp đồng chi tiết ở [api-design](api-design.md) §2 |
| Phụ thuộc | Module hoặc hệ thống ngoài |
| Xử lý lỗi | Lỗi đặc thù của module; quy ước chung ở [error-handling](../03-engineering/error-handling.md) |
| Phân quyền và bảo mật | Quyền cần có, dữ liệu nhạy cảm; thiết kế chung ở [system-architecture](system-architecture.md) §6 |

## 3. Phụ thuộc giữa các module

### 3.1 Ma trận phụ thuộc
Hàng phụ thuộc cột. Đánh dấu `S` (gọi đồng bộ), `A` (bất đồng bộ/sự kiện), `D` (đọc chung dữ liệu, cần giải thích).
| Module | <MOD-A> | <MOD-B> | <MOD-C> |
| --- | --- | --- | --- |
| <MOD-A> | – | | |
| <MOD-B> | | – | |
| <MOD-C> | | | – |

### 3.2 Sơ đồ phụ thuộc
<!-- Điền theo từng dự án: sơ đồ (Mermaid hoặc ảnh trong repo) -->

### 3.3 Quy tắc phụ thuộc
Chiều phụ thuộc cho phép, cấm vòng phụ thuộc, cấm truy cập trực tiếp dữ liệu của module khác. Ngoại lệ phải có ADR.
<!-- Điền theo từng dự án -->

## 4. Giao tiếp giữa các module
| Kiểu | Khi dùng | Quy ước |
| --- | --- | --- |
| Đồng bộ (gọi interface nội bộ) |  | |
| Bất đồng bộ / sự kiện |  | |

Mẫu giao tiếp mức hệ thống ở [system-architecture](system-architecture.md) §5.2; đặc tả từng điểm tích hợp (hệ thống ngoài và liên module) ở [api-design](api-design.md) §2.

## 5. Ranh giới và quyền sở hữu
Quy tắc nghiệp vụ thuộc module nào (dữ liệu: xem [database-design](database-design.md) §3.2); ai quyết khi thay đổi vượt ranh giới. Thay đổi ranh giới giữa module phải có ADR tại [ADR/](ADR/).
<!-- Điền theo từng dự án -->
