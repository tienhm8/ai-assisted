# Gitflow Workflow

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | Approved |
| Người phụ trách |  |
| Người duyệt | Tech Lead |
| Phiên bản · Ngày | 0.1 · 2026-11-12 |
| Tài liệu liên quan | deployment.md, ../../.ai/rules/git-workflow-rules.md |

> **Mục đích.** Mô tả cách áp dụng mô hình Gitflow của Vincent Driessen (nvie) cho dự án, kèm luồng ví dụ end-to-end. Staging là **môi trường**, không phải nhánh dài hạn.
>
> Template dùng chung: điền số version, tên môi trường và người phụ trách khi áp dụng. **AI không tự merge vào `master`/`develop` và không tự deploy production.**

## 1. Nhánh

| Nhánh | Dài hạn | Tách từ | Merge vào | Deploy lên |
| --- | --- | --- | --- | --- |
| `master` | Có | - | - | **Prod** (mỗi commit là một tag `vX.Y.Z`) |
| `develop` | Có | - | - | **Dev** |
| `feature/*` | Không | `develop` | `develop` | - |
| `release/X.Y.0` | Không | `develop` | `master` và `develop` | **Staging** |
| `hotfix/X.Y.Z` | Không | `master` | `master` và `develop` (hoặc `release/*` đang mở) | Staging (kiểm nhanh) rồi Prod |

Ngoài `feature/*`, các loại `fix`, `refactor`, `docs`, `chore` theo [git-workflow-rules](../../.ai/rules/git-workflow-rules.md) cũng tách từ `develop` và merge lại vào `develop`. Riêng `fix/*` sửa lỗi QA trong lúc release đang mở thì tách từ `release/*` và merge lại vào `release/*`.

## 2. Nhịp phát hành

| Môi trường | Tần suất | Nguồn deploy | Mục đích |
| --- | --- | --- | --- |
| Dev | Hằng ngày | `develop` | Tích hợp code mới |
| Staging | 1-2 lần/tuần, không cố định | `release/*` (hoặc `develop` tạm khi cần kiểm trước khi cắt release) | QA, UAT, regression |
| Prod | 2 tuần/lần theo sprint, có thể điều chỉnh | `master` (tag) | Phát hành tính năng mới |
| Hotfix | Khi cần | `hotfix/*` → `master` | Xử lý lỗi nghiêm trọng |

Release cắt theo thời điểm chốt sprint, không theo lịch cứng.

## 3. Luồng ví dụ end-to-end

Giả định: bản Prod hiện tại `v1.3.0`, sprint kết thúc sẽ phát hành `v1.4.0`.

### 3.1 Làm tính năng (hằng ngày)

```bash
git checkout develop && git pull
git checkout -b feature/PRJ-12-export-report
# ... commit theo Angular convention: feat(report): thêm xuất CSV (PRJ-12)
git push -u origin feature/PRJ-12-export-report
# Mở PR vào develop, CI xanh, có review → người duyệt merge (--no-ff)
```

Sau khi merge, `develop` tự deploy lên **Dev**.

### 3.2 Cắt release (cuối sprint)

```bash
git checkout develop && git pull
git checkout -b release/1.4.0
git push -u origin release/1.4.0
```

- Deploy `release/1.4.0` lên **Staging** để QA/UAT.
- Chỉ sửa lỗi trên nhánh release (`fix/...` tách từ `release/1.4.0`, PR vào `release/1.4.0`). **Không thêm tính năng mới.**
- Mỗi lần có fix, deploy lại Staging (đây là các lần "1-2 lần/tuần").
- Tính năng của sprint sau tiếp tục merge vào `develop` bình thường, không ảnh hưởng release.

### 3.3 Phát hành Production

Điều kiện: QA/UAT/regression đạt, rollback dùng được, **Owner phê duyệt** (xem [deployment §13](deployment.md)).

```bash
git checkout master && git pull
git merge --no-ff release/1.4.0
git tag -a v1.4.0 -m "Release 1.4.0"
git push origin master --tags      # deploy Prod từ tag v1.4.0

git checkout develop && git pull
git merge --no-ff release/1.4.0    # đưa các fix trên release về develop
git push origin develop

git branch -d release/1.4.0
git push origin --delete release/1.4.0
```

### 3.4 Hotfix (lỗi nghiêm trọng trên Prod)

```bash
git checkout master && git pull
git checkout -b hotfix/1.4.1
# ... fix(auth): sửa lỗi ... (PRJ-99)

git checkout master
git merge --no-ff hotfix/1.4.1
git tag -a v1.4.1 -m "Hotfix 1.4.1"
git push origin master --tags      # deploy Prod

git checkout develop
git merge --no-ff hotfix/1.4.1     # BẮT BUỘC, tránh lỗi quay lại ở release sau
git push origin develop
```

Nếu lúc đó đang có `release/*` mở thì merge hotfix vào `release/*` thay cho `develop` (release sẽ về `develop` khi đóng).

## 4. Quy ước

- **Merge dùng `--no-ff`** để giữ lịch sử nhánh.
- **Tag**: `vMAJOR.MINOR.PATCH`. Release sprint tăng MINOR, hotfix tăng PATCH; thay đổi phá vỡ tương thích tăng MAJOR.
- **Bảo vệ nhánh** `master`, `develop` (và `release/*` khi đang mở): bắt buộc PR, có review, CI pass; cấm force-push.
- **Hotfix và release** luôn phải merge ngược về `develop`.
- Commit message theo Angular convention, nêu `TASK-ID` (xem [git-workflow-rules](../../.ai/rules/git-workflow-rules.md)).
- Release/hotfix và tag do **người** thực hiện sau khi được duyệt; AI chỉ soạn và đề xuất.

## 5. Checklist

**Cắt release**
- [ ] Tất cả tính năng của sprint đã vào `develop`, CI xanh
- [ ] Đã tạo `release/X.Y.0` và deploy Staging

**Đóng release**
- [ ] QA/UAT/regression đạt trên Staging
- [ ] Kế hoạch rollback đã kiểm chứng
- [ ] Owner phê duyệt
- [ ] Đã merge vào `master`, gắn tag, deploy Prod, smoke test đạt
- [ ] Đã merge ngược về `develop`, xóa nhánh release

**Hotfix**
- [ ] Xác nhận là lỗi nghiêm trọng, Owner đồng ý
- [ ] Đã merge vào `master` (tag) và `develop`/`release/*`

## 6. Tham chiếu
- [deployment.md](deployment.md) (§6 quy trình phát hành, §10 rollback, §13 checklist)
- [git-workflow-rules](../../.ai/rules/git-workflow-rules.md)
- Vincent Driessen, "A successful Git branching model" (nvie.com, 2010)
