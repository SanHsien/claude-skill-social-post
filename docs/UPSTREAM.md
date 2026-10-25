# 上游同步指引

記錄如何安全、可重複地追蹤 [`Hao0321/claude-skill-social-post`](https://github.com/Hao0321/claude-skill-social-post) 的更新。

當前審查基準 Commit 為 `c22737a` (2026-10-25)。

## Remote 設定

```powershell
git remote -v
# 應包含：
# origin    https://github.com/SanHsien/claude-skill-social-post.git (fetch & push)
# upstream  https://github.com/Hao0321/claude-skill-social-post.git (fetch & push)
```

## 上游分支與 PR 審查清冊 (2026-10-09 基準)

| 上游對象 | 類別 | 狀態 | 審查評估結論 |
|---|---|---|---|
| `main` | 主分支 | 正常同步 | 已同步至本 fork `origin/main` |
| `fix/m10-metric-correction` | 分支 | 已合併落後 | 所有 commits 早已併入 `main`，無需引進 |
| `#4` | Pull Request | 已合併 (2026-07-16) | 修正第一篇爆款數據為 FB 洞察真值 (M10)，已包含於主線 |
| `#5` | Pull Request | 已合併 (2026-08-11) | v2.0.0: 結構化成效學習引擎，已包含於主線 |
| Issues | 議題追蹤 | 0 open | 上游目前無任何未結議題 |

## 2026-10-09：`c2641ba..e0720ed` 審查

Live inventory：上游 `main` 為 `e0720ed`；PR 使用 `--state all` 檢查到 #4、#5，均已合併，沒有編號大於
watermark #5 的項目；issue 使用 `--state all` 檢查沒有項目；除 `main` 外只剩
`fix/m10-metric-correction`，其相對 `main` 為 behind 49、ahead 0，沒有獨立 commit。fork 沒有 open PR 或
active workflow。四筆 main commit 的結論與可重審條件記在 [`DECISIONS.md`](DECISIONS.md#d-07-上游審查-4-commitc2641bae0720ed2026-10-09)。

## 2026-10-25：`e0720ed..c22737a` 審查

上游 `main` 為 `c22737a`（PR #6 merge）；PR ref 最大為 #6，issue 沒有大於 #5 的項目；
`fix/coherent-learning-snapshots-20261015` 已併入 `main`。`bedeae8` 移植、`9aa920b` 延後，見
[`DECISIONS.md`](DECISIONS.md#d-08-上游審查-3-commite0720edc22737a2026-10-25)。

## 檢查新更新

執行上游水位檢查工具：

```powershell
python tools/check_upstream_updates.py
```

或嚴格模式（若有未審查內容回傳非零退出碼）：

```powershell
python tools/check_upstream_updates.py --strict
```

## 同步標準流程

1. `git fetch upstream main`
2. 執行檢查工具查看上游變更清單。
3. 評估上游變更：
   - 若為 bug 修正或 Skill 增強：以 `git merge upstream/main` 或 `git cherry-pick` 引入。
   - 若涉及 README，需同步整理至 `README.md`（繁中）與 `README.en.md`。
4. 執行 Windows 門禁驗收：
   ```powershell
   pwsh -NoProfile -File tools\dev_check.ps1
   ```
5. 將同步決策記錄於 [`docs/DECISIONS.md`](DECISIONS.md)。
6. 推進 [`tools/upstream_baseline.json`](../tools/upstream_baseline.json) 的 commit sha 與 PR/Issue 水位。
