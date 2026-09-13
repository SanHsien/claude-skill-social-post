# 安全政策

## 支援範圍

安全修正以本 fork 的最新 `main` 為主；上游版本的問題也會視需要回報原作者。

## 私下回報

若發現針對本 fork 維護骨架或衍生程式的安全漏洞，請使用 GitHub Security Advisories 的 **Report a vulnerability** 私下回報：
<https://github.com/SanHsien/claude-skill-social-post/security/advisories/new>。
若該入口不可用，請透過 GitHub 個人檔案聯絡維護者，不要先建立公開 Issue。

若問題屬於上游核心邏輯，亦可向原作者駱君昊通報。

回報請包含影響範圍、重現步驟、受影響版本與最小必要證據。請勿在回報中附上真實 API key、token、社群 cookies、個人機密文件或帳密。

## 特別注意

- **社群憑證與 Cookie 隔離**：Chrome 自動化回覆操作會連接既有使用者設定檔或本機瀏覽器。絕不可將 Chrome 使用者資料目錄、登入 session、cookie 或 token 提交到 Git。
- **發布安全確認**：貼文與留言發布必須在當輪對話取得人類明確確認後才能執行，預設 `live_browser_actuation_enabled` 為 `false`。
- **本專案範圍**：不要將真實個人資料、私人帳本（`data/`）、含憑證的設定檔提交進 repository。