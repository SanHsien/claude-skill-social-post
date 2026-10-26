"""契約測試：check_links 的路徑解析要跟 GitHub 看到的一致。"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_links


@pytest.fixture()
def tree(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    (tmp_path / "target.md").write_text("x", encoding="utf-8")
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "guide(1).md").write_text("x", encoding="utf-8")
    monkeypatch.setattr(check_links, "ROOT", tmp_path.resolve())
    return tmp_path.resolve()


def problems(root: Path, text: str, name: str = "page.md") -> list[str]:
    page = root / name
    page.write_text(text, encoding="utf-8")
    return check_links.check_document(page)


def test_link_with_wrong_case_is_broken_on_github(tree: Path) -> None:
    # Windows 檔案系統不分大小寫，但 GitHub 分；只比對存在會放行 404 連結。
    assert len(problems(tree, "[說明](Target.md)")) == 1
    assert len(problems(tree, "[說明](DOCS/guide(1).md)")) == 1
    assert problems(tree, "[說明](target.md#section)") == []


def test_root_absolute_link_resolves_from_the_repo_root(tree: Path) -> None:
    (tree / "docs" / "inner.md").write_text("x", encoding="utf-8")
    assert problems(tree, "[說明](/target.md)", name="docs/inner.md") == []
    assert len(problems(tree, "[說明](/nope.md)", name="docs/inner.md")) == 1
