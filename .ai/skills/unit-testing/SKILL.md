---
name: unit-testing
description: Thiết kế, viết và chạy unit test cô lập cho logic nghiệp vụ, hàm, service và component, truy vết về AC, báo cáo bằng TEST-REPORT-TEMPLATE.
---

# Unit Testing Skill

## 1. Mục tiêu

Chứng minh từng đơn vị code chạy đúng ở điều kiện bình thường, biên và lỗi, mỗi test truy vết được về một AC.

## 2. Cổng vào

- Task có AC (ID dạng `<FR>-AC<N>`) và mức rủi ro; thiếu thì dừng và hỏi.
- Đã xác định framework test của dự án; chưa có thì ghi câu hỏi mở, không tự chọn.

## 3. Đầu vào

- Task và AC (acceptance-criteria), FR/BR liên quan
- testing-strategy (tầng, công cụ, ngưỡng coverage của dự án)
- Rules: testing-rules, coding-rules
- Mã nguồn cần test và cấu trúc test hiện có

## 4. Quy trình

1. **Xác định đối tượng test** từ AC: hàm thuần, service nghiệp vụ, validation, biến đổi trạng thái, component.
2. **Liệt kê kịch bản** cho từng đối tượng: bình thường, biên, đầu vào sai/rỗng/null, lỗi, vi phạm quy tắc nghiệp vụ, ca bị từ chối quyền (nếu logic có kiểm quyền).
3. **Thiết kế test** theo Arrange / Act / Assert: một mục đích, tên mô tả, xác định, độc lập, kiểm hành vi quan sát được. Tên hoặc chú thích test ghi ID AC.
4. **Mock** chỉ phần phụ thuộc ngoài (mạng, dịch vụ ngoài, thời gian, CSDL trong unit test). Không mock chính hành vi đang test.
5. **Viết test** theo quy ước, vị trí file, tiện ích dùng chung của dự án.
6. **Chạy**: test nhắm mục tiêu, bộ test liên quan, rồi toàn bộ unit khi cần. Chưa có CI thì chạy tại máy và ghi miễn trừ có thời hạn.
7. **Coverage**: đối chiếu với ngưỡng trong testing-strategy; không hạ ngưỡng. Ưu tiên phủ hành vi/quy tắc nghiệp vụ hơn con số.
8. **Sửa lỗi (regression test)**: viết test tái hiện, chạy thấy đỏ trước khi sửa, sửa rồi chạy xanh; ghi output cả hai lần.

## 5. Checklist

- [ ] Mỗi AC trong phạm vi có test, test mang ID AC.
- [ ] Có ca bình thường, biên, đầu vào sai, lỗi, từ chối quyền (nếu áp dụng).
- [ ] Test độc lập, xác định, không phụ thuộc thứ tự.
- [ ] Assertion kiểm hành vi thật, không kiểm chi tiết cài đặt.
- [ ] Coverage đạt ngưỡng của dự án.
- [ ] Kết quả có lệnh và output thật.

## 6. Việc không được làm

- Sửa code production chỉ để test sai được qua.
- Xoá, tắt, làm yếu assertion hoặc hạ ngưỡng coverage để qua cổng.
- Bỏ qua test lỗi mà không ghi lý do; để skipped không báo.
- Khẳng định pass khi chưa chạy.
- Lạm dụng mock đến mức test không còn kiểm gì.

## 7. Tiêu chí hoàn thành (DoD)

- Mọi AC trong phạm vi có test đạt; AC chưa có test ghi vào "Còn thiếu" của báo cáo.
- Test đã chạy, lỗi đã điều tra, coverage không dưới ngưỡng.
- Không có test skipped nào chưa được báo cáo.

## 8. Báo cáo bàn giao

Điền TEST-REPORT-TEMPLATE, gồm:
- Test đã thêm/sửa (file::tên) và AC tương ứng
- Lệnh đã chạy và output thật; trạng thái pass / fail / skipped / not-run, mỗi mục skipped/not-run kèm lý do
- Coverage so với ngưỡng
- Với regression: output đỏ trước và xanh sau
- Còn thiếu và rủi ro còn lại
