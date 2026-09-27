# social-post skill（Windows 原生維護 Fork）

[English Documentation](README.en.md) · [Fork 維護說明](FORK.md)

一個可安裝到 Claude Code 或 Codex 的社群內容 Skill：學習本機個人聲線、規劃 14 天內容日曆、撰寫跨平台（FB / IG / Threads / X / YouTube）貼文、經當輪明確確認後發布，並以受控已登入 Chrome 管理社群留言，把跨平台成效洞察保存成可驗證的結構化資料。

本倉庫為 [`Hao0321/claude-skill-social-post`](https://github.com/Hao0321/claude-skill-social-post) 的 **Windows-first 維護型 Fork**，保留上游完整歷史，在 Windows 11 原生 PowerShell 與 GitHub Actions CI 嚴格驗證。

目前穩定標籤：**v2.5.0**；`main` 已同步 **Unreleased candidate**。

---

## 專案亮點與實證

- **爆款流量實證（Mega-viral Validated）**：經過 4 個月大量實測驗證，首篇貼文即達成 80K 觸及、448 讚、500+ 留言。包含爆紅拆解與第二天下跌復盤紀錄。
- **聲線學習（P1 Learn Voice）**：深度分析個人過往爆款貼文的文字韻律、開場 Hook、用詞偏好與段落結構，在本機建立專屬風格設定檔，不洩漏任何私人訓練資料。
- **14 天排程規劃（P0 Plan）**：結合內容漏斗與跨平台發文矩陣，系統化規劃主題、平台屬性與實驗變因。
- **跨平台撰稿與安全發布（P2 Draft / Publish）**：針對 Facebook、Instagram、Threads、X、YouTube 的演算法與讀者閱讀習慣量身定做文案。**強制發布安全閘**：未經使用者當輪明確許可絕不自動送出。
- **成效帳本與深度分析（P3 / P4）**：採 Append-only 帳本記錄原文 SHA、確定性字數長度、版型排版、標點符號與成效指標，支援對齊 maturity 後的跨篇與跨平台客觀對比。
- **受控 Chrome 留言管理（P5 Comment Ops）**：採模組化 live-DOM actuator contract，支援指定留言讀取、來源憑證比對與安全 dry-run。預設 `live_browser_actuation_enabled: false`，絕不進行無邊界或未審核的自動操作。

---

## 安裝與快速開始

### 1. 安裝 Skill 至 AI 工具

Clone 本專案：

```powershell
git clone https://github.com/SanHsien/claude-skill-social-post.git
```

#### 安裝到 Codex（Windows PowerShell）

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse ".\claude-skill-social-post\social-post" "$env:USERPROFILE\.codex\skills\social-post"
```

#### 安裝到 Claude Code（Windows PowerShell）

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse ".\claude-skill-social-post\social-post" "$env:USERPROFILE\.claude\skills\social-post"
```

### 2. 建立本機個人檔案

在安裝後的 `social-post/` 目錄中：

```powershell
Copy-Item style_profile.example.md style_profile.md
Copy-Item content_plan.example.md content_plan.md
```

> **注意**：個人聲線檔 `style_profile.md`、內容計畫 `content_plan.md` 與產生的 `data/` 均為本機私有資料，已加入 `.gitignore`，請勿提交至公開倉庫。

### 3. 指令模式快速指引

在 Claude Code 或 Codex 對話中直接下達指令：
- `幫我學 FB 風格`：進入 P1 聲線學習
- `幫我排 14 天社群內容`：進入 P0 內容日曆規劃
- `今天發一篇`：進入 P2 撰稿模式，產出草稿後等待確認

---

## 六大操作模式（Six Modes）

| Mode | 模式名稱 | 核心功能 |
|---|---|---|
| **P0** | **Plan** | 規劃內容方向、主題分類與跨平台發布實驗 |
| **P1** | **Learn Voice** | 從已授權樣本提煉個人真實聲線、節奏與開場 Hook |
| **P2** | **Draft / Publish** | 撰寫各平台貼文；當輪對話確認後才允許發布 |
| **P3** | **Log Outcome** | 保存貼文快照、觸及數據、互動指標與修正記錄 |
| **P4** | **Optimize Patterns** | 在對齊 maturity 與內容類型的前提下進行成效交叉分析 |
| **P5** | **Comment Ops** | 以受控 Chrome 進行安全掃描、草擬與留言管理 |

詳細留言操作流程見 [`comment-operations.md`](social-post/references/comment-operations.md)，Chrome 轉接器規格見 [`chrome-comment-adapter.md`](social-post/references/chrome-comment-adapter.md)。

---

## Windows 本機維護與開發門禁

本 fork 維護者請使用一鍵初始化腳本驗證本機環境：

```powershell
pwsh -NoProfile -File tools\bootstrap_dev.ps1
```

執行開發門禁（語法檢查、Ruff、契約測試、相對連結檢查）：

```powershell
pwsh -NoProfile -File tools\dev_check.ps1
```

更多開發細節與架構說明請參閱：
- [本機開發指引](docs/DEVELOPMENT.md)
- [決策紀錄](docs/DECISIONS.md)
- [上游同步指引](docs/UPSTREAM.md)
- [全庫風險快照](REVIEW.md)
- [貢獻守則](CONTRIBUTING.md)
- [安全政策](SECURITY.md)

---

## 授權與上游聲明

本專案基於 [MIT](LICENSE) 授權開源。
原作者：駱君昊（Hao0321）與 [`Hao0321/claude-skill-social-post`](https://github.com/Hao0321/claude-skill-social-post) 貢獻者。
維護維度與差異說明詳見 [FORK.md](FORK.md) 與 [NOTICE.md](NOTICE.md)。