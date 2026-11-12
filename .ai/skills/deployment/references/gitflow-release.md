# Gitflow: cắt release, phát hành, hotfix

Nạp khi Task phát hành cần cắt release, đóng release hoặc làm hotfix. Lệnh merge, tag và push lên `master`, `develop`, `release/*` do **người** chạy; AI soạn các lệnh này vào runbook.

Ví dụ dưới giả định bản Production hiện tại là `v1.3.0`, sprint này phát hành `v1.4.0`.

## Nhánh và môi trường

| Nhánh | Tách từ | Merge vào | Deploy lên |
| --- | --- | --- | --- |
| `master` | — | — | Production, mỗi commit là một tag |
| `develop` | — | — | Dev |
| `release/X.Y.0` | `develop` | `master` và `develop` | Staging |
| `hotfix/X.Y.Z` | `master` | `master` và `develop` (hoặc `release/*` đang mở) | Staging kiểm nhanh, rồi Production |

## Cắt release

```bash
git checkout develop && git pull
git checkout -b release/1.4.0
git push -u origin release/1.4.0
```

- Deploy `release/1.4.0` lên Staging để QA và UAT.
- Lỗi tìm thấy: nhánh `fix/...` tách từ `release/1.4.0`, PR vào `release/1.4.0`, deploy lại Staging.
- Tính năng của sprint sau vẫn merge vào `develop`, không ảnh hưởng release.

## Phát hành Production

Điều kiện: QA, UAT, regression đạt trên Staging; rollback đã kiểm chứng; Owner phê duyệt.

```bash
git checkout master && git pull
git merge --no-ff release/1.4.0
git tag -a v1.4.0 -m "Release 1.4.0"
git push origin master --tags      # deploy Production từ tag v1.4.0

git checkout develop && git pull
git merge --no-ff release/1.4.0    # đưa các fix trên release về develop
git push origin develop

git branch -d release/1.4.0
git push origin --delete release/1.4.0
```

## Hotfix

Điều kiện: lỗi nghiêm trọng trên Production, Owner đồng ý.

```bash
git checkout master && git pull
git checkout -b hotfix/1.4.1
# ... sửa lỗi, commit

git checkout master
git merge --no-ff hotfix/1.4.1
git tag -a v1.4.1 -m "Hotfix 1.4.1"
git push origin master --tags      # deploy Production

git checkout develop
git merge --no-ff hotfix/1.4.1
git push origin develop
```

Đang có `release/*` mở thì merge hotfix vào `release/*` thay cho `develop`; release sẽ về `develop` khi đóng.

## Điểm dễ sót

- Quên merge ngược release hoặc hotfix về `develop`: lỗi đã sửa sẽ quay lại ở bản sau.
- Xoá nhánh release trước khi merge ngược.
- Deploy Production từ nhánh thay vì từ tag.
