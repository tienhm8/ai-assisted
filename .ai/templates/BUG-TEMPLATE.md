# BUG: <KEY>-<N> — <Tên ngắn>

> Mẫu báo lỗi giao cho AI. Lỗi là sai khác so với yêu cầu và tiêu chí nghiệm thu đã duyệt. Nếu lỗi do yêu cầu sai hoặc thiếu, dừng và chuyển sang đổi yêu cầu, không sửa tại đây.

## 1. Mô tả
Lỗi là gì, ảnh hưởng ai.

## 2. Liên kết
- FR: `FR-<MODULE>-<NN>`
- BR: `BR-<MODULE>-<NN>` (nếu có)
- AC bị vi phạm: `<FR>-AC<N>` (không có thì ghi lý do)
- ADR liên quan (nếu có): `ADR-<NNNN>`
- Task sửa lỗi: `<KEY>-<N>`
- Task/PR gây lỗi (nếu biết):

## 3. Phân loại
- Mức nghiêm trọng: Critical / High / Medium / Low
- Mức rủi ro: R1 / R2 / R3 (lấy từ Task, không tự gán)
- Mức tự chủ AI: lấy từ Task, không tự nâng
- Môi trường phát hiện: local / staging / production
- Nguồn phát hiện: cổng kiểm tra / review / sau phát hành
- Liên quan phân quyền: có / không
- Mở lại từ lỗi cũ: có (mã) / không

## 4. Các bước tái hiện
1.
2.

## 5. Kết quả mong đợi

## 6. Kết quả thực tế
Kèm thông báo lỗi, log, stack trace (đã che dữ liệu nhạy cảm, không dán dữ liệu production thật).

## 7. Giả thuyết và tác động
- Vị trí nghi ngờ (nếu có):
- Tác động (module, vai trò, dữ liệu, bảo mật):

## 8. Phạm vi sửa
- In scope:
- Out of scope:

## 9. Điều kiện hoàn thành
- [ ] Có test tái hiện lỗi, đỏ trước và xanh sau (kèm output thật).
- [ ] Hồi quy liên quan đã chạy.
- [ ] Nguyên nhân gốc đã ghi; không tìm ra thì dừng và báo.
- [ ] Không sửa ngoài phạm vi; không làm yếu test; không tự suy ra nghiệp vụ.
- [ ] Không vượt giới hạn vòng sửa (`project-rules` 18).

## 10. Báo cáo bàn giao (AI điền)
- Nguyên nhân gốc:
- Test hồi quy (tên) và kết quả trước/sau:
- AC được phủ lại:
- File đã sửa:
- Tài liệu cần cập nhật:
- Rủi ro còn lại:

## 11. Duyệt
- Người duyệt bản sửa (bắt buộc nếu R3 hoặc Critical):
- Người xác nhận đóng lỗi:
