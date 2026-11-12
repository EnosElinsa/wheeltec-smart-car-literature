"""Tests for tools.check_links on a small Git repository under tmp_path."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

from tools import check_links as cl
from tools.common import REPO_ROOT

pytestmark = pytest.mark.skipif(shutil.which("git") is None, reason="git not available")

PAGE = """# Page

[good](docs/a.md) and [dir](docs/) and [fragment](docs/a.md#part) and ![image](docs/fig.png)
[broken](docs/missing.md)
[pdf](01-papers/T1/x/paper.pdf) and [fulltext](02-fulltext/T1/x/paper.md)
[fulltext index](02-fulltext/INDEX.md) [web](https://example.org/x.pdf) [mail](mailto:a@b.c) [anchor](#top)
`[code span](nowhere.md)`
<!-- [comment](nowhere.md) -->

```
[fenced](nowhere.md)
```

[ref-good]: docs/a.md
[ref-bad]: <docs/no such file.md>
[archive](99-archive/history-2026-10-25.zip) [manuscript](05-survey/manuscript/survey.log)
[spaces](docs/with%20space.md) [up](../outside.md)
"""


def write(root: Path, rel: str, text: str = "x\n") -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    root.mkdir()
    shutil.copy(REPO_ROOT / ".gitignore", root / ".gitignore")
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    for rel in ["docs/a.md", "docs/fig.png", "docs/with space.md", "02-fulltext/INDEX.md",
                "01-papers/T1/x/paper.pdf", "02-fulltext/T1/x/paper.md",
                "99-archive/history-2026-10-25.zip", "05-survey/manuscript/survey.log"]:
        write(root, rel)
    write(root, "README.md", PAGE)
    write(root, "05-survey/manuscript/notes.md", "[bad](missing.md)\n")
    return root


def problems(report: cl.Report) -> set[tuple[str, int, str, str]]:
    return {(p.path, p.line, p.kind, p.target) for p in report.problems}


def test_extract_links_skips_code_and_comments():
    targets = [t for _, t in cl.extract_links(PAGE)]
    assert "nowhere.md" not in targets
    assert "docs/no such file.md" in targets
    assert "docs/a.md" in targets


def test_reports_broken_and_local_only_links(repo, capsys):
    report = cl.check_tree(repo)
    assert problems(report) == {
        ("README.md", 4, "broken", "docs/missing.md"),
        ("README.md", 15, "broken", "docs/no such file.md"),
        ("README.md", 16, "local-only", "99-archive/history-2026-10-25.zip"),
        ("README.md", 16, "local-only", "05-survey/manuscript/survey.log"),
        ("05-survey/manuscript/notes.md", 1, "broken", "missing.md"),
        ("README.md", 17, "broken", "../outside.md"),
    }
    assert report.files == 5  # README.md, two docs pages, 02-fulltext/INDEX.md, manuscript notes
    assert cl.main(["--root", str(repo)]) == 1
    out = capsys.readouterr().out
    assert "README.md:4: broken link: docs/missing.md" in out
    assert "broken: 4; local-only: 2" in out


def test_clean_tree_passes(repo, capsys):
    write(repo, "README.md", "[good](docs/a.md)\n[ref]: docs/with%20space.md\n")
    write(repo, "05-survey/manuscript/notes.md", "[good](notes.md)\n")
    assert cl.main(["--root", str(repo)]) == 0
    assert "broken: 0; local-only: 0" in capsys.readouterr().out
