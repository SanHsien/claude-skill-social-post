# 開發環境

維護者與 AI 接手用的開發文件。產品使用方式在 [`README.md`](../README.md)；上游同步在 [`UPSTREAM.md`](UPSTREAM.md)；決策在 [`DECISIONS.md`](DECISIONS.md)。

## 架構

```text
social-post/
  ├── SKILL.md                 Skill 核心入口與規範
  ├── references/              各平台（FB、IG、Threads、X、YouTube）發布與回覆規範
  ├── scripts/                 成效分析、驗證、Chrome 自動化回覆驅動與自測腳本
  ├── style_profile.example.md 聲線設定範本
  └── voice_quick.md           聲線快速指引
docs/                          fork 維護與治理文件
tools/                         fork 維護工具（Windows gate、上游檢查、相對連結檢查、依賴新鮮度）
  └── tests/                   維護契約測試
.github/                       GitHub Actions 工作流程與維護模板
```

## 本機開發（Windows 11 原生）

### 維護骨架（必跑）

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-dev.txt
$env:PYTHONUTF8 = "1"
pwsh -NoProfile -File tools\dev_check.ps1
```

等價一鍵指令：

```powershell
pwsh -NoProfile -File tools\bootstrap_dev.ps1
```

### 執行產品測試

本 repo 提供專用 Windows 原生產品測試腳本 `tools/test_product.ps1`：

```powershell
pwsh -NoProfile -File tools\test_product.ps1
```

## Canonical Gate

`tools\dev_check.ps1` 會依序執行：

1. `compileall`：編譯維護 Python 腳本（`tools/`）。
2. `ruff`：以 `--select E9,F` 檢查語法錯誤與未定義變數。
3. `pytest`：執行 `tools/tests/` 下的維護契約測試。
4. `check_links.py`：檢查所有維護 Markdown 之間的相對連結是否正確。