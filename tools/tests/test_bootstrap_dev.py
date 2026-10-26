"""bootstrap_dev.ps1 must not announce success when the gate it runs failed."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parents[1]
PWSH = shutil.which("pwsh")


@pytest.mark.skipif(PWSH is None, reason="pwsh not installed")
def test_failing_gate_fails_the_bootstrap(tmp_path: Path) -> None:
    (tmp_path / "tools").mkdir()
    shutil.copy(TOOLS / "bootstrap_dev.ps1", tmp_path / "tools" / "bootstrap_dev.ps1")
    (tmp_path / "requirements-dev.txt").write_text("", encoding="utf-8")
    shim = tmp_path / "shim"
    shim.mkdir()
    (shim / "pwsh.cmd").write_text("@echo off\r\nexit /b 1\r\n", encoding="ascii")
    env = {
        **os.environ,
        "PATH": f"{shim}{os.pathsep}{os.environ['PATH']}",
        "PIP_NO_INDEX": "1",
        "PIP_DISABLE_PIP_VERSION_CHECK": "1",
    }
    result = subprocess.run(
        [PWSH, "-NoProfile", "-File", str(tmp_path / "tools" / "bootstrap_dev.ps1")],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        env=env, timeout=240, check=False,
    )
    assert result.returncode != 0, result.stdout + result.stderr
    assert "維護環境可用" not in result.stdout
