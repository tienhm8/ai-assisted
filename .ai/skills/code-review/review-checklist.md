# Code Review – Checklist

> Bản nháp (Draft). Làm rõ dần theo Task thật.

## Phạm vi và yêu cầu
- [ ] Đáp ứng acceptance criteria.
- [ ] Không có thay đổi ngoài phạm vi mà không khai báo.
- [ ] Không tự suy diễn quy tắc nghiệp vụ.

## Rule
- [ ] Coding · Architecture · Database · Security · Testing rules.

## Bảo mật
- [ ] Phân quyền kiểm tra ở backend.
- [ ] Validate đầu vào; chống SQL injection, XSS.
- [ ] Không lộ secret hoặc dữ liệu nhạy cảm; log sự kiện bảo mật.

## Chất lượng
- [ ] Xử lý lỗi tường minh.
- [ ] Không trùng logic, không dead code, không `any` thiếu lý do.
- [ ] Hiệu năng truy vấn hợp lý.

## Kiểm thử
- [ ] Có test cho tính năng mới và regression test cho bug fix.
- [ ] Có bằng chứng test đã chạy; test fail/skip được báo rõ.
