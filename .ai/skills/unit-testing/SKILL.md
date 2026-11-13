---
name: unit-testing
description: Thiết kế, viết và chạy unit test cô lập cho logic nghiệp vụ, hàm, service và component, truy vết về AC, báo cáo bằng TEST-REPORT-TEMPLATE.
---

# Unit Testing Skill

Chứng minh từng đơn vị code chạy đúng ở điều kiện bình thường, biên và lỗi; mỗi test truy vết về một AC.

## Cổng vào

- Task có AC. Thiếu thì dừng và hỏi.
- Framework test của dự án đã xác định; chưa có thì ghi câu hỏi mở, không tự chọn.

Nguồn chính: plan (AC → test); mã cần test và cấu trúc test hiện có.
Plan thiếu thì tra đúng mục, không đọc cả file: testing-strategy §4 Các tầng test, §6 Thiết kế test, §9 Cổng chất lượng (Quality Gates).

## Quy trình

1. **Xác định đối tượng test** từ AC: hàm thuần, service nghiệp vụ, validation, biến đổi trạng thái, component.
2. **Liệt kê kịch bản:** bình thường, biên, đầu vào sai/rỗng/null, lỗi, vi phạm quy tắc nghiệp vụ, bị từ chối quyền (nếu logic có kiểm quyền).
3. **Thiết kế test** theo Arrange / Act / Assert: một mục đích, tên mô tả, xác định, độc lập, kiểm hành vi quan sát được chứ không kiểm chi tiết cài đặt. Tên hoặc chú thích ghi ID AC.
4. **Mock** chỉ phụ thuộc ngoài: mạng, dịch vụ ngoài, thời gian, CSDL.
5. **Viết test** theo quy ước, vị trí file và tiện ích dùng chung của dự án.
6. **Chạy:** test nhắm mục tiêu, rồi bộ test liên quan, rồi toàn bộ unit khi cần.
7. **Coverage:** đối chiếu ngưỡng trong testing-strategy. Ưu tiên phủ hành vi và quy tắc nghiệp vụ hơn con số.

## Giới hạn

- Không sửa code production chỉ để test qua.

## Hoàn thành khi

- Mỗi AC trong phạm vi có test đạt; AC chưa có test được ghi là còn thiếu.
- Test không phụ thuộc thứ tự chạy.
- Coverage không dưới ngưỡng của dự án.

## Báo cáo

Điền TEST-REPORT-TEMPLATE: test đã thêm hoặc sửa (file::tên) và AC tương ứng, coverage so với ngưỡng.
