---
name: deployment
description: Chuẩn bị và kiểm tra phát hành (xác nhận sẵn sàng, soạn lệnh, runbook, kế hoạch rollback, release notes, release report); AI không thực thi trên production, việc thực thi do người có quyền làm sau khi Owner duyệt.
---

# Deployment Skill

## 1. Mục tiêu

**AI chuẩn bị và kiểm tra; người có quyền thực thi.** Skill giúp phát hành ít rủi ro: xác nhận bản phát hành sẵn sàng, soạn lệnh và runbook, soạn release notes và kế hoạch rollback, điền release report. AI chỉ hỗ trợ thực thi ở môi trường ngoài production khi Task cấp quyền rõ ràng.

## 2. Cổng vào

- Có Task phát hành, nêu phiên bản, môi trường đích và mức rủi ro. Thiếu thì dừng và hỏi.
- Mọi PR trong bản phát hành đã merge (do người) và đạt cổng kiểm tra; PR chưa đạt thì loại khỏi danh sách phát hành và báo.
- Tài liệu vận hành của dự án (triển khai, giám sát, sao lưu và khôi phục) còn Draft hoặc trống ở mục cần dùng: dừng và hỏi, không tự giả định.

## 3. Đầu vào

- Task phát hành, danh sách Task/PR đã merge, commit hoặc tag.
- Tài liệu vận hành của dự án (triển khai, giám sát, sao lưu và khôi phục), mốc trong roadmap.
- Migration và kế hoạch rollback; báo cáo kiểm thử (TEST-REPORT).
- RELEASE-REPORT-TEMPLATE.

## 4. Quy trình

1. **Xác định môi trường đích** (local, staging, production) và người có quyền thực thi.
2. **Kiểm tra sẵn sàng:** mọi Task trong phạm vi đã Done, PR đã review và đạt cổng, không còn finding Critical/High mở, kiểm thử đã chạy thật. Gate nào hỏng thì dừng, không bỏ qua.
3. **Kiểm tra cấu hình:** liệt kê **tên** biến môi trường và cấu hình cần có so với môi trường đích. AI không đọc, tạo, xoay hay đổi giá trị secret; không đưa giá trị vào log hay báo cáo.
4. **Kiểm tra migration:** thứ tự, tương thích ngược khi phiên bản ứng dụng và CSDL chồng nhau, thời gian chạy, nguy cơ khoá bảng, có phá huỷ không, có backup trước khi chạy, có đường quay lui. Rollback code không tự đảo thay đổi CSDL; ghi rõ cách khôi phục dữ liệu.
5. **Chuẩn bị thực thi:** soạn lệnh, runbook từng bước và script migration theo cơ chế triển khai đã duyệt của dự án; không tự nghĩ lệnh deploy production. **Thực thi** (merge, deploy, chạy migration production) do người có quyền làm sau khi Owner duyệt. Ngoài production, AI chạy khi Task cấp quyền.
6. **Soạn release notes** từ các Task đã merge, bằng ngôn ngữ người dùng cuối, kèm Task/FR và PR tương ứng.
7. **Kế hoạch rollback:** điều kiện kích hoạt, các bước, người quyết định, đã thử ngoài production chưa.
8. **Kiểm chứng:** chạy hồi quy và smoke test ở staging hoặc local; ghi kết quả thật (pass/fail/skipped/not-run). Sau khi người deploy, hỗ trợ đối chiếu health check và giám sát theo ngưỡng của dự án; vượt ngưỡng thì đề nghị rollback, người quyết định.
9. **Điền release report** theo RELEASE-REPORT-TEMPLATE; Owner duyệt hoặc hoãn.

Trường hợp đặc biệt:
- **Hotfix khẩn:** là Task riêng, vẫn qua code-review; phân tích tối thiểu, hồ sơ bổ sung trong thời hạn dự án khai báo, có người duyệt hotfix.
- **Chưa có server, staging hoặc CI/CD:** làm các bước ở máy cục bộ hoặc môi trường thay thế đã khai báo, ghi miễn trừ có thời hạn và người duyệt; không bỏ qua âm thầm.

## 5. Checklist

- [ ] Môi trường đích và người thực thi đã xác định.
- [ ] Mọi PR trong bản phát hành đã đạt cổng; không còn finding Critical/High mở.
- [ ] Cấu hình: chỉ liệt kê tên biến, không có giá trị secret nào trong báo cáo.
- [ ] Migration đã đánh giá (thứ tự, phá huỷ, backup, quay lui).
- [ ] Lệnh, runbook, release notes, kế hoạch rollback đã soạn.
- [ ] Smoke test và hồi quy đã chạy, kết quả có bằng chứng.
- [ ] Release report đã điền đủ mục theo template.

## 6. Việc không được làm

- AI không deploy production, không chạy migration production, không truy cập CSDL production; chỉ người có quyền thực hiện sau khi Owner duyệt.
- Không đọc, tạo, xoay hoặc đổi giá trị secret; không ghi giá trị secret vào log hay báo cáo.
- Không sửa dữ liệu production trực tiếp; không chạy migration phá huỷ khi chưa có duyệt.
- Không bỏ qua cổng kiểm tra không đạt.
- Không giả định rollback an toàn khi chưa đánh giá; không báo phát hành thành công khi chưa có kiểm chứng.

## 7. Tiêu chí hoàn thành (DoD)

- Release report đã soạn đủ, gồm release notes, thay đổi cần lưu ý, kiểm chứng, rollback, kế hoạch theo dõi.
- Người có quyền đã xác nhận deploy (hoặc Owner đã quyết định hoãn); kết quả kiểm chứng sau deploy được ghi vào report.
- Vấn đề đã biết và rủi ro còn lại được nêu.

## 8. Báo cáo bàn giao

Điền RELEASE-REPORT-TEMPLATE; không tạo định dạng khác. Phần việc AI đã làm, việc cần người thực hiện (duyệt, merge, deploy, cấp quyền), giả định và câu hỏi mở (`OQ-<NN>`) ghi trong báo cáo bàn giao của Task (DELIVERY-REPORT-TEMPLATE), tóm tắt và nhắc mã release report.
