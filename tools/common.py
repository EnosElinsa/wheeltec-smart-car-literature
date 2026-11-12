"""Shared helpers: repository root, git file listing, and text decoding."""

from __future__ import annotations

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

TEXT_SUFFIXES = {
    ".md", ".csv", ".json", ".jsonl", ".tex", ".bib", ".py", ".txt",
    ".yml", ".yaml", ".cff", ".toml", ".cfg", ".ini", ".bst", ".sty",
    ".gitignore", ".gitattributes", ".html", ".js", ".css",
}


def is_text_path(path: Path) -> bool:
    """Return True when the file should be scanned as text."""
    if path.suffix.lower() in TEXT_SUFFIXES:
        return True
    return path.name in {"LICENSE", "LICENSE-CODE", "CITATION.cff", ".gitignore"}


def read_text(path: Path) -> str:
    """Read a text file, tolerating a UTF-8 BOM and undecodable bytes."""
    data = path.read_bytes()
    return data.decode("utf-8-sig", errors="replace")


def git_candidate_files(root: Path = REPO_ROOT) -> list[Path]:
    """List files that are tracked or would be added by ``git add -A``.

    The list contains tracked files plus untracked files that are not ignored,
    which is exactly the set that a commit of the working tree would contain.
    """
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    names = [n for n in result.stdout.decode("utf-8").split("\0") if n]
    files = []
    for name in names:
        path = root / name
        if path.is_file():
            files.append(path)
    return sorted(set(files))
