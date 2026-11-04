"""Locate the evidence library that contains this manuscript."""
import os
from pathlib import Path


def literature_root(manuscript: Path) -> Path:
    """Return WHEELTEC_LITERATURE_ROOT if set, else the repository holding 05-survey/manuscript."""
    configured = os.environ.get("WHEELTEC_LITERATURE_ROOT")
    candidate = Path(configured).expanduser() if configured else manuscript.parents[1]
    if (candidate / "06-data/paper-index.csv").is_file():
        return candidate.resolve()
    raise FileNotFoundError(
        "Evidence library not found. Run the manuscript scripts inside the "
        "wheeltec-smart-car-literature repository or set WHEELTEC_LITERATURE_ROOT."
    )
