# REVIEW.md

全庫風險快照。記錄本 fork 當前已知架構風險、邊界與接受之取捨。

## 結論

本專案核心為社群貼文生成、聲線學習與受控留言操作之 Skill。本 fork 建立 Windows-first 純原生維護體系，以非侵入方式保留上游完整歷史與核心邏輯，並以機械閘門杜絕誤推上游或未授權自動發布之風險。經全庫靜態分析與契約測試，全庫無語法錯誤、未定義變數或例外吞噬等缺陷；歷史舊標籤已完成清理，僅保留最新版本 `v2.5.0`。

## 已修 findings

- 建立完整的 Windows 原生 CI 工作流程（`windows-latest` Python 3.10–3.14 矩陣），支援純 Windows 開發與自動化驗收。
- 設定 `gh repo set-default SanHsien/claude-skill-social-post` 與 `.cursor/rules/no-upstream-pr.mdc` 硬閘門，解決預設推送上游的嚴重風險。
- 建立離線相對連結檢查器、上游水位檢查器與依賴新鮮度監控。
- 升級 `tools/test_product.ps1` 產品驗證執行器，全面涵蓋 Python 綱要驗證、特徵覆蓋以及 4 項 Node.js Chrome/JS 架構門禁測試。
- 清理本地與遠端 `origin` 上 47 個歷史舊標籤（`v0.2` ~ `v2.4.0`），使發布標籤體系保持單一清晰（僅保留 `v2.5.0`）。
- 審查上游分支 `fix/m10-metric-correction` 與 PR #4、#5，確認所有改動已 100% 併入 `main`。
- 修復 CodeQL Alert #1（CWE-367 / js/file-system-race）：在 `comment_chrome_fixture_evidence_testonly.mjs` 透過檔案描述符校驗 `(dev, ino)` 防範路徑置換競態，並同步更新 JS 架構門禁契約（2026-09-28）。
- 修復 CodeQL Alert #4（CWE-312 / py/clear-text-storage-sensitive-data）：重構 `self_test.py` 測試樣例變數名稱與測試特徵字串，消除 CodeQL 污點分析敏感資訊識別特徵（2026-09-28）。

## 接受、不改契約

| 編號 | 項目 | 風險評估 | 當前防護與取捨 | 狀態 |
|---|---|---|---|---|
| R-01 | Live Meta 回覆未全面解鎖 | FB / Threads 原生 live 回覆尚未完成三平台 canary 驗收 | 上游保持 `live_browser_actuation_enabled: false`，預設為唯讀 intake 與 target-only 模式。 | 接受、不改契約 |
| R-02 | Chrome 操作與 DOM 改版脆弱性 | 社群平台（FB/IG/Threads）前端 UI 改版可能導致 selector 失效 | 上游採 exact-tab 重用、節點雜湊與多維語意識別；禁止裸 selector 覆蓋核准證據。 | 接受、不改契約 |
| R-03 | 跨平台成效歸因偏差 | 發文時間與流量可能受諸多外部變因干擾 | 系統設定 `causal_claim_allowed: false`，僅支援同平台、同 maturity、同內容類型比較。 | 接受、不改契約 |

## 尚未宣稱範圍

- 尚未宣稱完成所有平台之 live browser 留言全面自動化發布（上游保持關閉狀態）。
- 尚未宣稱提供第三方雲端代管服務；本專案為完全本機執行的 Skill 工具。