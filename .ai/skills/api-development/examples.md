# API Development – Examples

> Bản nháp (Draft). Ví dụ minh hoạ; thay bằng ví dụ thật của dự án khi có.

## Ví dụ: tạo API đăng tin bất động sản

| Thành phần | Nội dung |
| --- | --- |
| Prompt | Tạo API đăng tin bất động sản. |
| Skill | `api-development` (quy trình này). |
| Rule | API phải kiểm tra quyền ở backend. |
| Documentation | Mô tả nghiệp vụ đăng tin và phân quyền. |

## Ví dụ nội dung từng bước

- **Analyze:** actor, quyền, phạm vi tài nguyên; validation và bất biến nghiệp vụ; tình huống lỗi.
- **Design:** `POST /listings`; schema request/response; mã lỗi; kiểm tra quyền; cần transaction hay không.
- **Implement:** validation → service → handler; kiểm quyền ở backend.
- **Test:** 201 thành công; 400 đầu vào sai; 401 chưa đăng nhập; 403 sai quyền; vi phạm business rule.
- **Review:** lộ dữ liệu, xử lý lỗi và log, hiệu năng truy vấn, trùng logic.

Ghi chú khi áp dụng cho dự án: thay bằng ví dụ thật (request/response, test) sau khi chạy thử trên Task đầu tiên.
