# CHECKLIST

Hoàn thành checklist tuần tự trước khi bắt đầu.

| # | Việc | File | Người quyết | Điều kiện hoàn thành |
| --- | --- | --- | --- | --- |
| [ ] 1 | Tạo repo từ framework | repo cha | Tech Lead | Repo cha có `.ai/`, `docs/`, `PROJECT.md` |
| [ ] 2 | Đưa mã nguồn vào `project/` | `PROJECT.md` §1 | Tech Lead | Mỗi repo con nằm trong `project/`; dòng Repository ghi đường dẫn |
| [ ] 3 | Dọn chỉ dẫn AI cũ trong repo con | repo con | Tech Lead | Repo con không còn `CLAUDE.md`, `AGENTS.md`, `.cursorrules` trái `.ai/`, hoặc trỏ về repo cha |
| [ ] 4 | Điền vai trò | `PROJECT.md` §5 | Tech Lead | Mọi dòng có tên người hoặc "Không áp dụng" |
| [x] 5 | Chốt mức dữ liệu | `PROJECT.md` §3 | Tech Lead | Bốn mức (công khai, nội bộ, nhạy cảm, bí mật) |
| [x] 6 | Chốt độ nghiêm ngặt và mức ASVS | `PROJECT.md` §4 | Tech Lead | Khác "chuẩn" thì lý do nêu rõ |
| [ ] 7 | Chọn công cụ AI và model/effort | `ai-config.yaml`, `PROJECT.md` §8 | Tech Lead | Công cụ đã khai báo; một Task chỉ sửa tài liệu chạy thử đạt |
| [ ] 8 | Khai stack | `ai-config.yaml` | Tech Lead | Danh sách stack |
| [x] 9 | Đặt ngân sách | `ai-config.yaml` | Tech Lead | Ngân sách mỗi Task đã ghi |
| [x] 10 | Ghi miễn trừ nếu có | `PROJECT.md` §7 | Tech Lead | Mỗi miễn trừ có lý do, người duyệt, hạn, kế hoạch khắc phục; không có thì ghi "Không có" |
| [ ] 11 | Duyệt `PROJECT.md` và `ai-config.yaml` | `PROJECT.md`, `ai-config.yaml` | Tech Lead | Trạng thái Approved |
| [ ] 12 | Lập hồ sơ của module làm đầu tiên | `docs/` | PO/BA, Techlead | Trạng thái Approved. Hồ sơ chưa duyệt vẫn được tạo `SRC-<NN>` bằng cách đăng ký tài liệu vào bảng ở [sources/README.md](docs/00-project-overview/sources/README.md) |

Xong checklist: đọc [.ai/guide/getting-started.md](.ai/guide/getting-started.md) §5 (các giai đoạn) và §6 (giao việc).
