"""Tests for the pre-publication guard.

Sample violations are assembled at run time so that this file itself stays
free of CJK text, credentials, and local absolute paths.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

from tools import check_public_tree as cpt
from tools.common import REPO_ROOT, git_candidate_files

CJK_SAMPLE = chr(0x4E2D) + chr(0x6587)
WIN_USER_PATH = "C:" + "\\" + "Users" + "\\" + "someone" + "\\" + "file.txt"
FAKE_TOKEN = "ghp" + "_" + "a1B2" * 10


def write(root: Path, rel: str, text: str = "ok\n") -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def scan(root: Path, rels: list[str], **kwargs) -> cpt.Report:
    return cpt.scan_files(root, [root / r for r in rels], **kwargs)


def test_clean_tree_passes(tmp_path):
    write(tmp_path, "03-reviews/T1/x/review.md", "# Title\nPlain English text.\n")
    write(tmp_path, "06-data/table.csv", "a,b\n1,2\n")
    report = scan(tmp_path, ["03-reviews/T1/x/review.md", "06-data/table.csv"])
    assert report.findings == []
    assert not cpt.failed(report, "strict")


@pytest.mark.parametrize(
    "rel",
    [
        "01-papers/T1/x/paper.pdf",
        "02-fulltext/T1/x/paper.md",
        "02-fulltext/T1/x/images/a.jpg",
        "05-survey/manuscript/figures/sub/copied.pdf",
        "99-archive/history.zip",
        "99-archive/superseded/old.csv",
        ".env",
    ],
)
def test_forbidden_paths_fail(tmp_path, rel):
    write(tmp_path, rel)
    report = scan(tmp_path, [rel])
    assert report.by_check("forbidden-path")
    assert cpt.failed(report, "report")


@pytest.mark.parametrize("rel", ["02-fulltext/INDEX.md", "05-survey/README.md", "99-archive/README.md",
                                 "05-survey/manuscript/survey.tex", "05-survey/manuscript/survey.pdf",
                                 "05-survey/manuscript/figures/fig-taxonomy.pdf"])
def test_allowed_index_paths(tmp_path, rel):
    write(tmp_path, rel)
    assert not scan(tmp_path, [rel]).by_check("forbidden-path")


def test_absolute_path_detected(tmp_path):
    write(tmp_path, "06-data/m.json", '{"origin": "%s"}\n' % WIN_USER_PATH.replace("\\", "\\\\"))
    write(tmp_path, "04-analysis/a.md", "see " + WIN_USER_PATH + "\n")
    report = scan(tmp_path, ["06-data/m.json", "04-analysis/a.md"])
    assert len(report.by_check("absolute-path")) == 2


def test_relative_archive_reference_is_not_absolute(tmp_path):
    write(tmp_path, "03-reviews/r.md", "99-archive/history-2026-10-25.zip::papers/16-T1/x.md\n")
    assert not scan(tmp_path, ["03-reviews/r.md"]).by_check("absolute-path")


def test_secret_detected_without_echo(tmp_path):
    write(tmp_path, "tools/conf.txt", "token line " + FAKE_TOKEN + "\n")
    report = scan(tmp_path, ["tools/conf.txt"])
    findings = report.by_check("secret")
    assert len(findings) == 1
    assert FAKE_TOKEN not in cpt.format_report(report, "strict")


def test_word_token_in_prose_is_not_a_secret(tmp_path):
    write(tmp_path, "03-reviews/r.md", "The language model encodes each token once.\n")
    assert not scan(tmp_path, ["03-reviews/r.md"]).by_check("secret")


def test_cjk_report_versus_strict(tmp_path):
    write(tmp_path, "03-reviews/r.md", "Title\n" + CJK_SAMPLE + "\n")
    report = scan(tmp_path, ["03-reviews/r.md"])
    assert report.by_check("cjk")
    assert not cpt.failed(report, "report")
    assert cpt.failed(report, "strict")


def test_localized_interface_keeps_all_nonlanguage_guards(tmp_path):
    rel = 'tools/local_index.html'
    write(tmp_path, rel, CJK_SAMPLE + '\n' + WIN_USER_PATH + '\n' + FAKE_TOKEN)
    report = scan(tmp_path, [rel])
    assert not report.by_check('cjk')
    assert report.by_check('absolute-path')
    assert report.by_check('secret')
    assert cpt.failed(report, 'strict')
    write(tmp_path, 'tools/other.html', CJK_SAMPLE)
    assert scan(tmp_path, ['tools/other.html']).by_check('cjk')


def test_size_limit(tmp_path):
    path = write(tmp_path, "06-data/big.csv", "x" * 2048)
    report = cpt.scan_files(tmp_path, [path], size_limit=1024)
    assert report.by_check("size")


def test_tool_sources_are_clean():
    files = sorted((REPO_ROOT / "tools").rglob("*.py"))
    report = cpt.scan_files(REPO_ROOT, files)
    assert report.findings == []


@pytest.mark.skipif(shutil.which("git") is None, reason="git not available")
def test_repository_gitignore_excludes_local_material(tmp_path):
    shutil.copy(REPO_ROOT / ".gitignore", tmp_path / ".gitignore")
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    keep = [
        "02-fulltext/INDEX.md",
        "05-survey/README.md",
        "01-papers/T1/x/citation.bib",
        "03-reviews/T1/x/review.md",
        "99-archive/README.md",
        "05-survey/manuscript/survey.tex",
        "05-survey/manuscript/survey.pdf",
        "05-survey/manuscript/figures/fig-taxonomy.pdf",
    ]
    drop = [
        "01-papers/T1/x/paper.pdf",
        "02-fulltext/T1/x/paper.md",
        "02-fulltext/T1/x/images/a.jpg",
        "05-survey/manuscript/survey.log",
        "99-archive/history-2026-10-25.zip",
        "99-archive/superseded/old.csv",
        ".env",
    ]
    for rel in keep + drop:
        write(tmp_path, rel)
    listed = {p.relative_to(tmp_path).as_posix() for p in git_candidate_files(tmp_path)}
    for rel in keep:
        assert rel in listed, rel
    for rel in drop:
        assert rel not in listed, rel
