# Điều kiện nạp Rule và Skill

> Trạng thái: **Approved**. Sửa file này cần Task riêng và người duyệt.

Tách từ [task-types.md](task-types.md) để chỉ nạp khi cần: §1 khi chọn Rule ở bước 1, §2 khi chốt chuỗi Skill ở bước 3 ([task-execution.md](task-execution.md)).

## 1. Điều kiện nạp Rule

| Rule | Nạp khi |
| --- | --- |
| git | Task có commit hoặc PR |
| coding | Có sửa code, kể cả code test |
| testing | Có sửa code, viết hoặc chạy test, hoặc phải báo kết quả kiểm tra |
| architecture | Thiết kế; chạm ranh giới module, tầng, API contract; thêm module hoặc dependency; ảnh hưởng NFR |
| database | Chạm schema, migration, query, transaction, seed hoặc dữ liệu test trong CSDL, xoá dữ liệu |
| cache | Thêm, sửa hoặc đọc cache; đổi dữ liệu đang được cache |
| document-database | Rule `database` đã thoả và hệ quản trị là CSDL tài liệu (MongoDB, NoSQL) |
| security | Task R3; chạm xác thực, phiên, phân quyền; dữ liệu D2/D3; input từ ngoài, upload; tích hợp bên thứ ba; thêm hoặc đổi dependency; secret, cấu hình bảo mật; phát hành |

Rule đã thoả điều kiện thì không bỏ, kể cả với Task R1. Mức rủi ro chỉ đổi độ sâu kiểm tra, không đổi bộ Rule.

## 2. Điều kiện dùng Skill có điều kiện

| Skill | Dùng khi |
| --- | --- |
| product-discovery | Chưa có vision, scope |
| authentication-rbac | Task có đăng nhập, phiên, vai trò, quyền hoặc truy cập theo tài nguyên. Làm xong luôn kèm `security-review` và `integration-testing` |
| integration-testing | Chạm CSDL, giao tiếp giữa module, API hoặc dịch vụ ngoài |
| e2e-testing | Có hành trình người dùng quan trọng hoặc đổi luồng nhiều màn hình |
| security-review | Thoả điều kiện nạp Rule `security` ở §1. Bắt buộc với Task R3 |
| documentation | Đổi hành vi, API, schema, kiến trúc hoặc cách vận hành |
| architecture-design (soạn ADR) | Thiết kế dữ liệu cần partition, sharding, tách CSDL, đổi hệ quản trị hoặc chọn mẫu đa tenant |
