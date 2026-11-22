# 決策紀錄

長期架構決策與取捨。上游審查清冊在 [`UPSTREAM.md`](UPSTREAM.md)。

## D-01: Windows 11 原生維護優先 (2026-09-13)

- **脈絡**：本 fork 主要開發、除錯與日常驗收環境為 Windows 11 原生 PowerShell，非 WSL 或 POSIX。
- **決定**：
  - 維護工具統一使用 PowerShell 7 (`pwsh`) 腳本與跨平台 Python 腳本。
  - 明確設定 `$env:PYTHONUTF8 = "1"` 與 `$env:PYTHONIOENCODING = "utf-8"`。
  - GitHub Actions CI 採用 `windows-latest` 執行 Python 3.10–3.14 測試矩陣。
- **後果**：保證在 Windows 原生環境下無編碼錯誤或路徑斜線問題。

## D-02: 保持上游 Skill 核心純粹與非侵入性維護 (2026-09-13)

- **脈絡**：上游 `Hao0321/claude-skill-social-post` 已具備完整的聲線學習、成效追蹤與 Chrome 留言合約。
- **決定**：
  - 不對 `social-post/` 的核心邏輯進行格式化重構或破壞性重寫。
  - 所有維護工具、文件契約測試與 CI 設定均集中於根目錄、`docs/`、`tools/` 與 `.github/`。
- **後果**：未來與上游同步（`upstream/main`）時產生衝突的機率降至最低。

## D-03: 防誤開 PR 至上游的硬閘門機制 (2026-09-13)

- **脈絡**：GitHub CLI 在 fork 專案中預設將 upstream 作為 default repository，極易誤開 PR 到原作者倉庫。
- **決定**：
  - 設定 `gh repo set-default SanHsien/claude-skill-social-post`。
  - 在 `.cursor/rules/no-upstream-pr.mdc` 與所有 AI 入口文件嚴格明文規範（2026-10 起 `CLAUDE.md`、`GEMINI.md`
    已併入 `AGENTS.md`，只保留這一份）。
- **後果**：杜絕意外向上游推送或誤開 PR 的風險。

## D-04: 上游分支、PR 與 Issue 審查清冊 (2026-09-13)

- **脈絡**：需要全面評估上游是否有可引進之分支、未處理 PR 或未關閉之 Issue。
- **決定**：
  - 審查上游分支 `fix/m10-metric-correction`：比對結果顯示所有 commit 已於 2026-07-16 透過 PR #4 完全併入 `main`，無額外獨立代碼。
  - 審查上游 PR：PR #4 (`修正第一篇爆款數據為 FB 洞察最終真值 (M10)`) 與 PR #5 (`v2.0.0: add structured outcome learning`) 均已合併入 `main`。目前無 Open PR。
  - 審查上游 Issues：上游目前無任何未處理之 Issue（Open: 0）。
- **後果**：當前 `main` 分支已涵蓋上游全部有效代碼，基線水位設定為 PR 5、Issue 5。

## D-05: 歷史標籤清理，僅保留最新版本 v2.5.0 (2026-09-13)

- **脈絡**：Fork 專案預設繼承了上游 47 個歷史演進標籤（`v0.2` 至 `v2.4.0`），干擾版本發布清晰度。
- **決定**：
  - 本地與 `origin` 刪除 `v0.2` 至 `v2.4.0` 之 47 個舊 tag。
  - 僅保留最新穩定版本標籤 `v2.5.0`。
- **後果**：遠端與本地標籤體系保持最精簡狀態。
## D-06: 上游審查 3 commit（0c7b53f..c2641ba，2026-09-30）

- **範圍**：3 個 commit、0 個新 PR（水位 #5）、0 個新 issue（水位 #5）。三筆同日進入上游 `main`。
- **決定**：
  - `c2641ba`（新增 `chatgpt-socialpost/`）：not-applicable，ChatGPT Chat 專用入口，本 fork 面向 Claude Code；不引進。
  - `ddb0897`（ChatGPT 降階流程、未校準 voice 防護，3 檔）：not-applicable，內容為 ChatGPT 無 shell 情境；
    通用條款（修稿保留使用者已刪格式）待日後語氣流程調整時再抽。
  - `f2ba749`（X For You 演算法文件＋Instagram 選取、CUA runtime、Threads 讀取器等 29 檔 +1379/-132）：
    **adoption pending：** 涉及已登入瀏覽器實機操作的留言自動化，行數大、無法在本機驗證實際平台行為；
    本 fork 另有 CodeQL 修補（`comment_js_architecture_*`、`self_test.py`），與其重疊。
    已驗證 `git apply --check`（僅 `social-post/`、`chatgpt-socialpost/`）可乾淨套用；README 有衝突。
- **觸發條件**：要用 Instagram／Threads 留言自動化，或 X 演算法文件被需要時，套用該 patch 並跑
  `tools\test_product.ps1`（含 Node 測試）後再採用。
- **後果**：baseline 推進到 `c2641ba`，代表已審查，不代表已合併。

## D-07: 上游審查 4 commit（c2641ba..e0720ed，2026-10-09）

- **範圍**：上游 `main` 的 4 個 commit；PR 以 `--state all` 檢查至 #5，issue 以 `--state all` 檢查沒有項目；
  分支 `fix/m10-metric-correction` 相對 main 沒有獨立 commit。
- **決定**：
  - `1d0a60f`（公開貢獻制度）：**reject**。它的 `CODEOWNERS`、治理文件、Hao 專屬審核權與 Ubuntu
    Python 3.10/3.13 CI 不適用於本 fork；本 fork 已有維護者直接推送、繁中 `CONTRIBUTING.md` 與 Windows
    Python 3.10–3.14 gate。日後若本 fork 改成接受外部 PR，才以 SanHsien 的治理者與 Windows gate 重新設計，
    不照搬上游身分與 CI。
  - `9f944e0`（本機 Workbench 與 AI handoff）：**defer**。它新增 loopback UI、資料 store、Node renderer
    tests 與 Skill 路由，是完整新產品面，不是本 fork 現有缺陷的修正；目前也沒有使用者要求啟動此 UI。
    觸發條件是使用者明確要求本機 Workbench，屆時以整個功能群組採用、跑產品與 Workbench tests，並另做程式碼審查。
  - `46392bd`（Workbench listener/session 修正）：**not-applicable**。此修正只作用於前項尚未引入的
    `workbench.py`／`workbench_test.py`；隨 Workbench 採用時一併重審，不能單獨移植。
  - `e0720ed`（social learning 與寫作契約治理）：**defer**。它與 Workbench、JSONL learning、immutable
    author contracts 及既有 `social_data.py`／`social_validation.py` 成套耦合，會碰觸本 fork 先前的
    comment-security hardening。沒有可證明仍存在於本 fork 的獨立漏洞；若要採用，必須連同相依 feature、
    privacy regression 與完整產品 gate 一起評估，不可只挑文件或單一 helper。
- **後果**：baseline 推進到 `e0720ed` 表示四筆均已審查，不表示已合併。上游新的 commit、PR/issue 編號、
  分支 head 或明確 Workbench 需求會重新觸發審查。

## D-08: 上游審查 3 commit（e0720ed..c22737a，2026-10-25）

- **範圍**：上游 `main` 的 3 個 commit 與 PR #6（已合併，head `9aa920b`）。issue 水位 #5 以上沒有新項目
  （2026-10-24 Upstream check 以 token 查證）；`git ls-remote` 無編號大於 #6 的 PR ref。分支
  `fix/coherent-learning-snapshots-20261015` 為 `main` 的祖先，`fix/m10-metric-correction` 無獨立 commit。
- **決定**：
  - `bedeae8`（成效讀取一致快照）：**adopt（移植）**。本 fork 的 `validate_store`、`feature_matrix`、
    `feature_coverage_report`、`series_summary` 逐檔讀五本 JSONL，`commit_records` 逐檔換檔，讀者可能
    拿到混合時點資料並蓋上較新的 revision；`log_outcome.prepare_records` 的 base revision 與資料分兩次讀。
    新增 `social_snapshot.py`／`social_snapshot_test.py`，`social_store`、`log_outcome` 與上游一致；
    `social_data.py` 只移植快照讀取，不帶入延後中的 media family／owner scope（e0720ed）；
    `workbench_service.py` 與 README 段落隨 Workbench（D-07）延後。
  - `9aa920b`（v2.5.1：Threads canary 測試模組拆分、`audit.config.json`）：**defer**。只是測試重組，
    且拆分的對象是 D-06 尚未採用的 `f2ba749` Threads 讀取器版本，本 fork 套不上也沒有對應缺陷。
    觸發條件同 D-06：採用 `f2ba749` 時一併套用並跑 `tools\test_product.ps1`。
  - `c22737a`（PR #6 merge commit）：無內容，隨上兩項處理。
- **後果**：baseline 推進到 `c22737a`、PR #6；不代表已合併 `9aa920b`。

## D-09: Ruff 0.17.3 新鮮度裁決（2026-11-05）

- **脈絡**：PyPI Ruff 已由既有延後紀錄的 0.17.2 更新到 0.17.3；`ruff>=0.16` 是相容性下限，並非精確釘版。
- **決定**：採逐版延後裁決，將 `.github/dependency-deferrals.json` 的 `deferredLatest` 更新為 0.17.3；不調高下限。已檢視 [官方發布說明](https://github.com/astral-sh/ruff/releases/tag/0.17.3) 與 [PyPI Python 需求](https://pypi.org/project/ruff/0.17.3/)（>=3.7），並使用 Ruff 0.17.3 通過完整 Windows 維護 gate。
- **後果**：保留既有相容性承諾與 E9/F 檢查範圍；PyPI 超過 0.17.3 時此裁決自動失效並重新審查。本機 pytest 使用 worktree 內的獨立暫存目錄，避免共用暫存目錄權限衝突。

## D-10: SKILL.md 開頭的 P5 狀態快照改為指向 adapter（2026-11-22）

- **脈絡**：`social-post/SKILL.md` 開頭把 2026-09-05 那一輪的 canary／ledger 狀態（`needs_reconcile`、Chrome 連線中斷等）寫進每次都會載入的 skill 本文，與 `references/chrome-comment-adapter.md` 的同一段重複；狀態一變兩份就會矛盾。
- **決定**：照上游 `c22737a` 的寫法縮成一段沒有日期的現況摘要，送出實證與 ledger 結算只留在 adapter。上游那段的平台狀態（Threads 已對帳、CUA IG 已接入）與本 fork 的 adapter 不同，所以只採寫法、不照抄事實；其餘上游 SKILL.md 改動仍依 D-07 延後。
- **後果**：日後採用上游 SKILL.md 時，這一行以上游版為準並重新核對 adapter 現況。

## D-11: 上游審查 PR #8、#9 與 Issue #7、#10（c22737a，2026-11-22）

- **範圍**：上游 `main` 自 `c22737a` 後無新增 commit；PR 檢查至 `#9`（#8、#9 皆為 `open`），Issue 檢查至 `#10`（#7、#10 皆為 `open`）。
- **決定**：
  - **Issue #7**（Windows 全新 Python 缺 `tzdata` 時誤判 `'Asia/Taipei'` 為不認得的時區）與 **PR #8**（`357406603815d2eabd5b67691bd38088d451e653`，`open`）：**部分採用（移植核心修正與測試；不採冗餘設定；PR #8 釘入 `monitored`）**。
    - 採用：`social-post/scripts/social_validation.py` 在 `(ZoneInfoNotFoundError, ValueError)` 且 `not available_timezones()` 時保持 fail-closed 並提示缺少 IANA 時區資料庫與 `python -m pip install tzdata`；`social-post/scripts/social_test_schema_time_validation.py` 新增 `check_missing_timezone_database` 與 `Asia/Taipe` 測試；`docs/setup.md` Windows 段落補上 `python -m pip install tzdata` 說明（未帶入 PR #8 的 `\r` 轉義筆誤）。
    - 不採／跳過：PR #8 新增 `requirements.txt`、修改 `CONTRIBUTING.md` 及新增 `.github/workflows/ci.yml` job——本 fork 已有 `requirements-dev.txt`（含 `tzdata>=2024.1`）、`tools/bootstrap_dev.ps1` 與 Python 3.10–3.14 `windows-latest` CI（D-01）。
    - 重看條件：PR #8 合併進上游 `main`、head SHA 變動或關閉時，核對最終合入內容；Issue #7 若補充額外行為需求時再重審。
  - **PR #9**（`Add read-only Social Post outcome intake review`，head `671cdc63a2d76765e81c47045a5e6b7bc7549d96`，`open`）：**延後（釘入 `monitored`）**。
    - 理由：尚未合併進上游 `main`，且 `review_outcome_intakes.py` 依賴的 `social_primitives`、`owner_scope` 與 `data/outcome_intakes.jsonl` 屬 D-07 已延後之 `e0720ed` 範圍，本 fork 無該前置模組，亦非現存缺陷修正；diff（7 檔 +483/-1）無安全拒收項。
    - 重看條件：PR #9 合併進上游 `main`、head SHA 變動，或本 fork 依 D-07 決定引進 `e0720ed` 相關結構時重審並跑 `tools\test_product.ps1`。
  - **Issue #10**（`你的技能《claude-skill-social-post》的 1VR 体检报告 + 设计伙伴邀请`，`open`）：**拒絕（不追）**。
    - 理由：外部推廣與設計夥伴邀請，推銷未經審查的第三方套件（`silicon-teahouse`）與外部 API 端點（`1vr.com`），僅匹配 README 的 `git clone` 指令，非程式碼缺陷報告；不引入第三方網路端點或安裝其提及之套件。
    - 重看條件：無需重看（除非上游作者日後針對本體另開實質程式碼 Issue，依新編號評估）。
- **後果**：`tools/upstream_baseline.json` 更新 `reviewed_date` 為 `2026-11-22`、`reviewed_through` 維持 `c22737a33d6cf09c48690f8be076b28bffc43a67`、`reviewed_pr_through` 推進至 `9`、`reviewed_issue_through` 推進至 `10`，並以 `monitored` 追蹤未合併 PR `#8` 與 `#9`。
