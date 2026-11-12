---
name: deployment
description: Chuẩn bị và kiểm tra phát hành (xác nhận sẵn sàng, soạn lệnh, runbook, kế hoạch rollback, release notes, release report); AI không thực thi trên production, việc thực thi do người có quyền làm sau khi Owner duyệt.
---

# Deployment Skill

AI chuẩn bị và kiểm tra bản phát hành; người có quyền thực thi. Ngoài production, AI chỉ chạy khi Task cấp quyền rõ ràng.

## Cổng vào

- Task phát hành nêu phiên bản, môi trường đích, mức rủi ro. Thiếu thì dừng và hỏi.
- Mọi PR trong bản phát hành đã được người merge và đạt cổng kiểm tra; PR chưa đạt thì loại khỏi danh sách và báo.
- Tài liệu vận hành (triển khai, giám sát, sao lưu và khôi phục) đã có ở mục cần dùng; còn trống thì dừng và hỏi.

Đọc: Task phát hành, danh sách Task/PR đã merge, commit hoặc tag; tài liệu vận hành; migration; báo cáo kiểm thử; RELEASE-REPORT-TEMPLATE.

## Quy trình

1. **Xác định** môi trường đích và người có quyền thực thi.
2. **Kiểm tra sẵn sàng:** Task trong phạm vi đã xong, PR đã review và đạt cổng, không còn finding Critical/High mở, kiểm thử đã chạy thật. Cổng nào hỏng thì dừng.
3. **Cấu hình:** liệt kê **tên** biến môi trường và cấu hình cần có ở môi trường đích. Không đọc, tạo, xoay hay ghi giá trị secret.
4. **Migration:** thứ tự, tương thích khi phiên bản ứng dụng và CSDL chồng nhau, thời gian chạy, nguy cơ khoá bảng, có phá huỷ không, backup trước khi chạy, đường quay lui. Rollback code không tự đảo thay đổi CSDL; ghi rõ cách khôi phục dữ liệu.
5. **Chuẩn bị thực thi:** soạn lệnh, runbook từng bước và script migration theo cơ chế triển khai đã duyệt; không tự nghĩ lệnh deploy. Lệnh cắt release, đóng release, hotfix lấy từ `references/gitflow-release.md`.
6. **Release notes** từ các Task đã merge, viết cho người dùng cuối, kèm Task/FR và PR.
7. **Kế hoạch rollback:** điều kiện kích hoạt, các bước, người quyết, đã thử ngoài production chưa.
8. **Kiểm chứng:** chạy hồi quy và smoke test ở staging hoặc local. Sau khi người deploy, đối chiếu health check và giám sát theo ngưỡng của dự án; vượt ngưỡng thì đề nghị rollback.
9. **Điền release report**; Owner duyệt hoặc hoãn.

Trường hợp đặc biệt:
- **Hotfix khẩn:** Task riêng, vẫn qua `code-review`; hồ sơ bổ sung trong thời hạn dự án khai báo, có người duyệt hotfix.
- **Chưa có staging hoặc CI/CD:** làm ở môi trường thay thế đã khai báo và đề nghị miễn trừ có thời hạn.

## Hoàn thành khi

- Lệnh, runbook, release notes, kế hoạch rollback đã soạn; migration đã đánh giá.
- Smoke test và hồi quy đã chạy, có output thật.
- Người có quyền đã xác nhận deploy hoặc Owner đã hoãn; kết quả sau deploy đã ghi vào report.

## Báo cáo

Điền RELEASE-REPORT-TEMPLATE. Việc cần người thực hiện ghi trong báo cáo bàn giao của Task kèm mã release report.
