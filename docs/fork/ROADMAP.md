# 路線圖

> 本 repo 後續工作的單一真相源。做完一項，就在同一個 commit 刪掉那一列；新工作只加在這裡。
> 現況段的數字是 2026-10-29 依 `main` `859081fe823a` 查的快照，開工前先重查 GitHub。

## 現況

這是社群聲線學習、內容規劃、成效分析與受控 Chrome 留言管理的 Windows 維護 fork，外部發布仍須當輪明確確認（repo 根目錄 `AGENTS.md:7-18`、`README.md:5,18-20`；以下檔案位置皆以 repo 根目錄為準）。2026-10-29 快照 open PR、安全告警均為 0，CI、CodeQL、Dependency freshness、Upstream check 最近結果為 success；issue 因停用而未查到，上游比較因無共同祖先未查到差距，不視為歷史缺陷（2026-10-29 `gh` 查詢，`859081fe823a`）。已審 baseline 與延後採用項目見 `tools/upstream_baseline.json`、`docs/DECISIONS.md` D-06～D-08；live 留言全面自動化尚未宣稱（`REVIEW.md`〈尚未宣稱範圍〉）。

## 近期：可以直接動手

| 項目 | 為什麼 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 無：維持現狀 | 維護工具缺陷與一致快照問題已修；沒有可直接啟動的新產品需求，不能把延後採用當未修漏洞 | 開工重查 `gh pr list --repo SanHsien/claude-skill-social-post`、安全告警與 Actions；有新缺陷才新增近期工作 | 維護者 | 深掃報告（2026-10-26）〈缺陷與修復〉；`30128ba`、`3d73f69`；2026-10-29 `gh` 查詢 |

## 中期：等條件成立再做

| 項目 | 觸發條件 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 增量審查上游 | 超過 baseline 的 commit／PR／issue，或已審分支／PR head 改變 | 執行 `python tools/check_upstream_updates.py --strict`，逐筆核對 diff 與本 fork 安全修補，記錄取捨；Windows gate 及受影響產品測試通過才推進水位 | Codex | `tools/upstream_baseline.json:2-8`；`AGENTS.md:41-50`；`docs/UPSTREAM.md` |
| 採用 Instagram／Threads 留言功能群組 | 維護者明確需要該平台留言操作或相關 X 演算法資料 | 依 D-06 重審 `f2ba749` 及 D-08 的 `9aa920b`，保留既有安全修補；`tools/test_product.ps1` 含 Node 測試通過，先唯讀／dry-run，外部送出另取當輪確認 | Codex | `docs/DECISIONS.md` D-06、D-08；`REVIEW.md` R-01、R-02 |
| 評估本機 Workbench 與 social learning 整套採用 | 維護者明確要求啟動本機 Workbench UI | 依 D-07 成套評估 UI、store、session 與 learning 相依項；產品／Workbench tests、privacy regression 與程式碼審查通過，不單挑耦合 helper | Claude Opus | `docs/DECISIONS.md` D-07（`9f944e0`、`46392bd`、`e0720ed`） |
| 補 Windows symlink 路徑的產品驗收 | 取得可建立 symlink 的 Windows 測試環境，或修改相關檔案安全邊界 | 重跑對應產品案例，確認 symlink／路徑置換防護；該項需有實跑結果，不能把 NOT_CHECKED 當通過 | 維護者 | 接續開發報告（2026-10-25）〈做了什麼〉；`tools/test_product.ps1`；`REVIEW.md` 的檔案競態修補 |

## 刻意不做

| 不做什麼 | 理由 | 什麼情況下重新考慮 |
| --- | --- | --- |
| 解鎖全面 live 回覆或無確認發文 | 現有安全契約維持關閉及 target-only；理由見 `REVIEW.md` R-01、R-02 與 `README.md:18-20` | 平台逐一完成核准範圍內 canary，且維護者明確授權對外操作 |
| 為上游版號另打本 fork v2.5.1 tag，或強推修共同祖先 | 版號不能代表未採用的測試群組；歷史已壓縮，差距比較失敗不是待修產品缺陷 | 已採用所需功能並通過發版驗收，或維護者另行提出精確歷史處理需求 |
| 為罕見 Markdown 寫法擴大解析器 | 目前沒有實際文件觸發；限制見深掃報告〈刻意不修〉 | 出現巢狀括號、圖片外層連結或清單內 fence 的可重現漏檢／誤報 |

## 維護方式

每週按 `docs/UPSTREAM.md`、baseline 與 D-06～D-08 的條件做增量審查；已審水位不是合併清單，保留 Windows 與 comment-security 邊界。
每月查 Dependency freshness 與安全告警；產品修改跑 `tools/test_product.ps1`，維護修改跑 Windows gate，其他文件只連結這份 fork 路線圖。
