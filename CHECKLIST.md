# CHECKLIST

Việc cần làm khi áp dụng khung cho một dự án, mới hay cũ. Làm theo thứ tự. Giá trị khuyến nghị đã điền sẵn trong [PROJECT.md](PROJECT.md): mục nào đúng thì giữ.

| # | Việc | File | Người quyết | Điều kiện hoàn thành |
| --- | --- | --- | --- | --- |
| 1 | Tạo repo từ khung | repo mới | Tech Lead | Repo cha mới tồn tại, có `.ai/`, `docs/`, `PROJECT.md` |
| 2 | Đưa mã nguồn vào `project/` | `PROJECT.md` §1 | Tech Lead | Mỗi repo con nằm trong `project/`; dòng Repository ghi đường dẫn |
| 3 | Dọn chỉ dẫn AI cũ trong repo con (không có thì xong) | repo con | Tech Lead | Repo con không còn `CLAUDE.md`, `AGENTS.md`, `.cursorrules` trái `.ai/`, hoặc chỉ còn một dòng trỏ về repo cha |
| 4 | Điền vai trò | `PROJECT.md` §5 | Tech Lead | Mọi dòng có tên người hoặc "Không áp dụng" |
| 5 | Chốt mức dữ liệu | `PROJECT.md` §3 | Tech Lead | Bốn mức (công khai, nội bộ, nhạy cảm, bí mật) có ví dụ của dự án; mức bí mật ghi "Không" được đưa vào AI |
| 6 | Chốt vùng file | `PROJECT.md` §2.2 | Tech Lead | Mỗi vùng (xanh, vàng, đỏ) có đường dẫn thật của dự án |
| 7 | Chốt độ nghiêm ngặt (giữ chuẩn hoặc ghi lý do) | `PROJECT.md` §4 | Tech Lead | Có giá trị và dòng lý do; khác "chuẩn" thì lý do nêu rõ |
| 8 | Chọn công cụ AI và model/effort | `ai-config.yaml`, `PROJECT.md` §8 | Tech Lead | Công cụ đã khai báo; một Task chỉ sửa tài liệu chạy thử đạt |
| 9 | Khai stack và lệnh kiểm tra | `ai-config.yaml` | Tech Lead | Mỗi lệnh kiểm tra chạy được và có kết quả thật |
| 10 | Đặt ngân sách | `ai-config.yaml` | Tech Lead | Ngân sách mỗi Task đã ghi |
| 11 | Ghi miễn trừ nếu có | `PROJECT.md` §7 | Tech Lead | Mỗi miễn trừ có lý do, người duyệt, hạn, kế hoạch khắc phục; không có thì ghi "Không có" |
| 12 | Duyệt `PROJECT.md` và `ai-config.yaml` | `PROJECT.md`, `ai-config.yaml` | Tech Lead | Trạng thái Approved, có tên người duyệt và ngày |
| 13 | Lập hồ sơ của module làm đầu tiên | `docs/` | PO/BA, Kiến trúc sư | Hồ sơ của module đó ở trạng thái Approved |

Xong checklist: đọc [.ai/guide/getting-started.md](.ai/guide/getting-started.md) §5 để giao việc.
