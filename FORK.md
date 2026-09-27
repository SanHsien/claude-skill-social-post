# Fork 維護說明

本 repo fork 自 [`Hao0321/claude-skill-social-post`](https://github.com/Hao0321/claude-skill-social-post)，
沿用 MIT License 與完整 Git 歷史。

## 為什麼維護 fork

- 保留原作者駱君昊（Hao0321）持續驗證與更新的 Claude Code / Codex 社群貼文自動化 Skill、本機聲線學習、成效追蹤與受控 Chrome 留言管理。
- 採 Windows-first 維護：Windows 11 + PowerShell 是主要開發、除錯與完整驗收環境。
- 公開入口維持繁體中文為主，英文鏡像放 `README.en.md`。
- 建立可重現的 Windows 開發 gate、Windows CI job，以及逐筆審查的上游追蹤（涵蓋 commit、PR 與 issue 水位）。
- 產品執行路徑以上游為準；本線不發佈第三方套件或變更上游授權。

**回貢判準：修的是上游的 bug 就送回去；這裡獨創的文件／Windows 維護骨架留在這裡。**
回貢前必須在當次對話取得維護者明確同意；「fork」「建開發環境」「開 PR」都不是同意。

## 與上游的差異

| 項目 | 說明 |
|---|---|
| `README.md` | 繁中主檔；加入 fork 維護資訊與快速入口 |
| `README.en.md` | 英文鏡像；加入 fork 維護資訊與上游原始說明 |
| `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` | 本 fork 的 AI 維護單一真相源 |
| `NOTICE.md` / `FORK.md` / `LICENSE` | 來源、授權與同步說明 |
| `tools/dev_check.ps1` | Windows 本機一鍵 gate（維護工具，不安裝重型依賴） |
| `tools/bootstrap_dev.ps1` | Windows 本機一鍵初始化與驗收（支援虛擬環境與門禁） |
| `tools/test_product.ps1` | Windows 原生產品測試執行腳本（驗證 self_test 等） |
| `requirements-dev.txt` | 維護依賴清單（pytest, ruff） |
| `.github/workflows/ci.yml` | 純 Windows 原生 CI (windows-latest Python 3.10–3.14 矩陣)：compile / ruff / 維護測試 / 連結檢查 |
| `.github/workflows/upstream-check.yml` | 每週對 `upstream/main` 做未審查 commit、PR、issue 水位檢查 |
| `.github/workflows/dependency-freshness.yml` | 每月依賴新鮮度檢查 |
| `.github/workflows/codeql.yml` | CodeQL 安全掃描工作流程 |
| `docs/DECISIONS.md`、`docs/UPSTREAM.md`、`docs/DEVELOPMENT.md` | fork 維護文件 |
| `REVIEW.md` | 全庫風險快照 |

核心腳本與 Skill 在 `social-post/`，以上游為準。

## 分支與 remote

- `origin/main`：SanHsien 維護線，也是唯一長期分支。
- 日常修改在本機跑 gate 後直接推 `origin/main`。
- `upstream/main`：Hao0321 原始專案，只追蹤、不推送。
- Dependabot 或外部 fork 的變更走 PR，讀 diff 並通過 CI 後再合併。

不要 `git push upstream`。同步方式見 [`docs/UPSTREAM.md`](docs/UPSTREAM.md)。

上游更新 `README.md` 時，把新內容併進本 fork 對應檔案。

## 換一台電腦怎麼開發

```powershell
git clone https://github.com/SanHsien/claude-skill-social-post.git
cd claude-skill-social-post
# `gh repo clone` 已會加上 `upstream` remote；若沒有：
# git remote add upstream https://github.com/Hao0321/claude-skill-social-post.git
pwsh -NoProfile -File tools\bootstrap_dev.ps1
```

要實際使用 Skill 與 Chrome 留言管理，見 [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md)。