#!/usr/bin/env python3
"""檢查本 fork 維護文件之間的相對連結。

只驗公開入口與 docs。外部網址交給人看。

    python tools/check_links.py
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
# Inline link or image: `[text](target)` / `![alt](target "title")`. The target is
# either `<...>` or a run without spaces that may hold one level of balanced
# parentheses (`guide(1).md`); an optional quoted or parenthesised title follows.
# Images need no pattern of their own: `!` precedes the same `[alt](target)` shape.
LINK_PATTERN = re.compile(
    r"\[[^\]]*\]\(\s*(<[^>]*>|(?:[^()\s]|\([^()\s]*\))+)"
    r"""(?:\s+(?:"[^"]*"|'[^']*'|\([^)]*\)))?\s*\)"""
)
FENCE_PATTERN = re.compile(r"^ {0,3}(`{3,}|~{3,})")
INLINE_CODE_PATTERN = re.compile(r"(?<!`)(`+)(?!`).+?(?<!`)\1(?!`)")
FENCE_CLOSE_PATTERN = re.compile(r"^ {0,3}(`{3,}|~{3,})[ \t]*$")
HTML_SRC_PATTERN = re.compile(r"""(?is)<img[^>]+src=["']([^"']+)["']""")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#")
SKIP_NAMES = {
    "upstream-review-report.md",
    "dependency-freshness-report.md",
}
MAINTAINED_DOCUMENTS = (
    "README.md",
    "README.en.md",
    "FORK.md",
    "NOTICE.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "REVIEW.md",
    "docs/DEVELOPMENT.md",
    "docs/DECISIONS.md",
    "docs/UPSTREAM.md",
    ".github/pull_request_template.md",
)


def iter_documents() -> list[Path]:
    missing = [relative for relative in MAINTAINED_DOCUMENTS if not (ROOT / relative).is_file()]
    if missing:
        raise FileNotFoundError("maintained documents missing: " + ", ".join(missing))
    extra = []
    github = ROOT / ".github"
    if github.is_dir():
        extra.extend(
            path
            for path in github.rglob("*.md")
            if path.is_file() and path.name not in SKIP_NAMES
        )
    required = [ROOT / relative for relative in MAINTAINED_DOCUMENTS]
    seen = {path.resolve() for path in required}
    for path in extra:
        if path.resolve() not in seen:
            required.append(path)
            seen.add(path.resolve())
    return required


def _exists_exact_case(target: Path) -> bool:
    if not target.exists():
        return False
    try:
        parts = target.relative_to(ROOT).parts
    except ValueError:
        return True
    current = ROOT
    for part in parts:
        if part not in os.listdir(current):
            return False
        current = current / part
    return True


def _missing_relative(path: Path, target: str) -> str | None:
    target = target.strip().strip("<>")
    if not target or target.startswith(SKIP_PREFIXES):
        return None
    file_part = unquote(target.split("#", 1)[0])
    if not file_part:
        return None
    # GitHub resolves `/x.md` from the repo root and matches names case-sensitively;
    # a Windows `exists()` does neither, so check both by hand. normpath (not
    # resolve) keeps the spelling as written.
    base = ROOT if file_part.startswith("/") else path.parent
    resolved = Path(os.path.normpath(base / file_part.lstrip("/")))
    if _exists_exact_case(resolved):
        return None
    try:
        shown = resolved.relative_to(ROOT)
    except ValueError:
        shown = resolved
    return f"{target} → 找不到 {shown}"


def _strip_code(text: str) -> str:
    """Drop fenced blocks and inline code: links written there are examples."""
    kept: list[str] = []
    fence = ""
    for line in text.splitlines():
        marker = FENCE_PATTERN.match(line)
        if fence:
            marker = FENCE_CLOSE_PATTERN.match(line)
            if marker and marker.group(1)[0] == fence[0] and len(marker.group(1)) >= len(fence):
                fence = ""
            continue
        if marker:
            fence = marker.group(1)
            continue
        kept.append(INLINE_CODE_PATTERN.sub("", line))
    return "\n".join(kept)


def check_document(path: Path) -> list[str]:
    problems: list[str] = []
    text = _strip_code(path.read_text(encoding="utf-8"))
    for pattern in (LINK_PATTERN, HTML_SRC_PATTERN):
        for match in pattern.finditer(text):
            missing = _missing_relative(path, match.group(1))
            if missing:
                problems.append(missing)
    return problems


def main() -> int:
    documents = iter_documents()
    if not documents:
        print("找不到任何維護用 Markdown 檔")
        return 1

    failures = 0
    for path in documents:
        problems = check_document(path)
        rel = path.relative_to(ROOT)
        if problems:
            failures += 1
            for problem in problems:
                print(f"FAIL {rel}: {problem}")
        else:
            print(f"OK   {rel}")

    print(f"\n共 {len(documents)} 份文件，{failures} 份有斷掉的相對連結。")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
