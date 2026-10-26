"""契約測試：check_links 要抓真正斷掉的連結，也不能對合法 Markdown 誤報。"""

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


def test_link_title_is_not_part_of_the_path(tree: Path) -> None:
    assert problems(tree, '[說明](target.md "標題")') == []
    assert problems(tree, "[說明](target.md 'title')") == []


def test_parentheses_inside_a_path_are_kept(tree: Path) -> None:
    assert problems(tree, "[說明](docs/guide(1).md)") == []


def test_example_links_in_code_are_not_checked(tree: Path) -> None:
    assert problems(tree, "```md\n[範例](nope.md)\n```\n") == []
    assert problems(tree, "用 `[範例](nope.md)` 這種寫法") == []


def test_a_real_broken_link_is_still_reported(tree: Path) -> None:
    found = problems(tree, "[壞](nope.md)\n```\n[範例](also-nope.md)\n```\n[壞2](nope2.md)")
    assert len(found) == 2
    assert "nope.md" in found[0] and "nope2.md" in found[1]


def test_a_broken_image_is_reported_once(tree: Path) -> None:
    assert len(problems(tree, "![圖](missing.png)")) == 1


def test_info_string_line_does_not_close_a_fence(tree: Path) -> None:
    text = "```\n```bash\nx\n```\n[壞](nope.md)\n"
    assert len(problems(tree, text)) == 1


def test_long_backtick_run_does_not_hang(tree: Path) -> None:
    import time

    start = time.perf_counter()
    problems(tree, "`" * 20000 + "a [壞](nope.md)")
    assert time.perf_counter() - start < 2


def test_unclosed_code_run_does_not_hide_a_link(tree: Path) -> None:
    assert len(problems(tree, "``a` [壞](nope.md)")) == 1
