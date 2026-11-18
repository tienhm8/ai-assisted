# TEST REPORT: <GOAL>-P<N> hoặc <KEY>-<N> / <Phiên bản>

> Báo cáo cấp Task dùng Task ID; cấp phát hành tổng hợp từ các báo cáo Task. Trạng thái test: pass / fail / skipped / not-run. Không có bằng chứng thì ghi not-run, không ghi pass.

| Mục | Giá trị |
| --- | --- |
| Ngày | |
| Môi trường (local / CI / staging; phiên bản runtime, CSDL) | |
| Commit SHA đầy đủ · Nhánh/worktree | |
| Mức rủi ro (R) · Mức dữ liệu (D) | Mã kèm nghĩa, ví dụ R2 (ảnh hưởng nhiều module) · D1 (nội bộ) |
| Nguồn kết quả | CI (liên kết lượt chạy) / cục bộ |
| Miễn trừ áp dụng (lý do, hạn) | không / có: |
| Người chạy (người/AI, model, phiên) | |

## 1. Kết quả theo cổng và tầng
Mỗi cổng hoặc tầng kiểm tra dự án áp dụng là một dòng (ví dụ build, lint, kiểm tra kiểu, unit, integration, E2E, hồi quy, quét secret, quét lỗ hổng, kiểm tra migration). Dòng không áp dụng ghi N/A kèm lý do.

| Cổng/tầng | Bắt buộc? | Lệnh | Pass | Fail | Skipped | Not-run | Coverage | Bằng chứng (log/output) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Tổng số test:

## 2. Truy vết yêu cầu → test
| AC (`<FR>-AC<N>`, vd FR-XXX-01-AC1) | FR / BR / NFR | Loại test | Test (file::tên) | Kết quả | Bằng chứng |
| --- | --- | --- | --- | --- | --- |

AC không có test phải được liệt kê ở mục 4, không để trống.

## 3. Lỗi tìm thấy
| Mã lỗi | Mức nghiêm trọng | Trạng thái | AC/test phát hiện | Test hồi quy (đã có/chưa) |
| --- | --- | --- | --- | --- |

## 4. Chưa kiểm chứng
| Hạng mục (AC/tầng/test) | Trạng thái (skipped/not-run) | Lý do | Rủi ro còn lại | Kế hoạch · Hạn |
| --- | --- | --- | --- | --- |

Test bị bỏ qua phải có lý do. Không xoá hay làm yếu assertion để qua cổng.

## 5. Kết luận
- [ ] Mọi cổng bắt buộc đạt hoặc có miễn trừ hợp lệ.
- [ ] Mọi AC trong phạm vi có test đạt.
- [ ] Không còn lỗi Critical/High mở.
- [ ] Mỗi kết quả pass đều có bằng chứng thật.

Kết quả: Đạt / Không đạt.
Người chạy: · Người xác nhận (khác người chạy):
