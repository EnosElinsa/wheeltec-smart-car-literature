"""Tests for tools.review_check using a synthetic paper and review."""

from __future__ import annotations

from pathlib import Path

import pytest

from tools import review_check as rc

FULL_TEXT = """# A Test Paper on Slip-Aware Estimation

Abstract\u2014We propose a slip-aware estimator for wheeled robots. Experiments on gravel and asphalt show consistent speed estimates under combined slip.

## I. Introduction

Wheel odometry breaks under combined slip on loose surfaces.

## IV. Experiments

The estimator runs in real time on a Clearpath Jackal at 50 Hz. The mean RMSE is 6.2% at low speed.
Future work is the integration with visual-inertial navigation.
"""

ABSTRACT = (
    "We propose a slip-aware estimator for wheeled robots. Experiments on gravel and asphalt "
    "show consistent speed estimates under combined slip."
)

CODE = "M99"
THEME = "T1-perception-localization"
FOLDER = "2022-test-M99"


def make_review(**overrides) -> str:
    parts = {
        "title": "A Test Paper on Slip-Aware Estimation",
        "doi": "[10.1109/test.2022.1](https://doi.org/10.1109/test.2022.1)",
        "module": "localization-mapping",
        "boundary": "no",
        "excerpt": "Future work is the integration with visual-inertial navigation.",
        "result": "- Mean RMSE 6.2% at low speed (p. 6, Table II).",
        "log": "- 2026-10-26 | host: Kiro | scope: full text read | corrections: none",
        "abstract": ABSTRACT,
        "extra": "",
        "level": "full",
    }
    parts.update(overrides)
    return f"""# {parts['title']}

## Metadata

| Field | Value |
|---|---|
| ID | {CODE} |
| Title | {parts['title']} |
| Authors | A. Author and B. Author |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2022 |
| Type | journal |
| DOI | {parts['doi']} |
| Official URL | https://ieeexplore.ieee.org/document/1 |
| Theme folder | {THEME} |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/{THEME}/{FOLDER}/paper.pdf` and `02-fulltext/{THEME}/{FOLDER}/paper.md` (local only); [BibTeX](../../../01-papers/{THEME}/{FOLDER}/citation.bib) |

## Survey coding

- survey_module: {parts['module']}
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: none
- platform_class: skid-steer
- platform: Clearpath Jackal
- boundary_platform: {parts['boundary']}
- degradation: wheel-slip, terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: wheel encoders, IMU
- compute: onboard computer, 50 Hz
- compute_location: onboard
- summary_result: Mean speed RMSE 6.2% at low speed on mixed surfaces.
- summary_limitation: Not coupled to visual-inertial navigation.
- survey_included: yes
- verification_level: {parts['level']}

## Problem

Wheel odometry fails under slip.

## Mechanism

A wheel-level observer.

## Baselines and controls

A switching observer.

## Platform and setup

Jackal indoor and outdoor.

## Evidence type and transfer

Closed-loop hardware.

## Sensors

Encoders and IMU.

## Compute and latency

50 Hz onboard.

## Key quantitative results

{parts['result']}

## Stated limitations

- No visual coupling (p. 7).

## Transfer conditions

Needs wheel torque data.

## Code and data

Not stated.

## Version family

None found.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | strong | Sec. I, p. 1 | "Wheel odometry breaks under combined slip on loose surfaces." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 7, Conclusion.** "{parts['excerpt']}"
  Coupling is future work.

## Survey-usable statements

### Supported

- Slip is estimated online.

### Not supported

- Full 6-DoF localization.

## Verification log

{parts['log']}
- Legacy extraction: automated reviewer (codex), baseline batch.
{parts['extra']}

## Original abstract

{parts['abstract']}
"""


@pytest.fixture
def library(tmp_path, monkeypatch):
    monkeypatch.setattr(rc, "REPO_ROOT", tmp_path)
    review_dir = tmp_path / "03-reviews" / THEME / FOLDER
    review_dir.mkdir(parents=True)
    md_dir = tmp_path / "02-fulltext" / THEME / FOLDER
    md_dir.mkdir(parents=True)
    (md_dir / "paper.md").write_text(FULL_TEXT, encoding="utf-8")
    bib_dir = tmp_path / "01-papers" / THEME / FOLDER
    bib_dir.mkdir(parents=True)
    (bib_dir / "citation.bib").write_text("@article{x}\n", encoding="utf-8")
    index = {
        CODE: {
            "code": CODE,
            "title": "A Test Paper on Slip-Aware Estimation",
            "doi": "10.1109/test.2022.1",
            "official_url": "https://ieeexplore.ieee.org/document/1",
            "pdf": f"01-papers/{THEME}/{FOLDER}/paper.pdf",
            "markdown": f"02-fulltext/{THEME}/{FOLDER}/paper.md",
        }
    }

    def check(text: str) -> rc.Result:
        path = review_dir / "review.md"
        path.write_text(text, encoding="utf-8")
        return rc.check_review(path, index, rc.FullTextCache())

    return check


def checks(result: rc.Result) -> set[str]:
    return {issue.check for issue in result.issues}


def test_valid_review_passes(library):
    result = library(make_review())
    assert result.ok, result.issues


def test_codex_verification_log_preserves_actual_host(library):
    result = library(make_review(
        log="- 2026-11-02 | host: Codex | scope: excerpts checked | corrections: none"
    ))
    assert result.ok, result.issues


def test_bad_vocabulary_value(library):
    result = library(make_review(module="perception"))
    assert "coding" in checks(result)


def test_boundary_flag_must_match_platform(library):
    result = library(make_review(boundary="yes"))
    assert "coding" in checks(result)


def test_doi_mismatch(library):
    result = library(make_review(doi="[10.1109/other](https://doi.org/10.1109/other)"))
    assert "metadata" in checks(result)


def test_fabricated_excerpt_fails(library):
    result = library(make_review(excerpt="The robot drives safely in all conditions without error."))
    assert "excerpts" in checks(result)


def test_ellipsis_excerpt_fails(library):
    result = library(make_review(excerpt="Future work is ... navigation."))
    assert "excerpts" in checks(result)


def test_result_without_page_fails(library):
    result = library(make_review(result="- Mean RMSE 6.2% at low speed."))
    assert "results" in checks(result)


def test_light_review_passes(library):
    result = library(make_review(level="light"))
    assert result.ok, result.issues
    assert not result.warnings


def test_light_result_without_page_warns(library):
    result = library(make_review(level="light", result="- Mean RMSE 6.2% at low speed."))
    assert result.ok, result.issues
    assert any(w.check == "results" for w in result.warnings)


def test_light_review_keeps_other_errors(library):
    fabricated = make_review(level="light", excerpt="The robot drives safely in all conditions without error.")
    assert "excerpts" in checks(library(fabricated))
    no_log = make_review(level="light", log="- 2026-09-18 | host: codex | scope: legacy | corrections: none")
    assert "log" in checks(library(no_log))
    wrong = "Highlights: robots are useful. Apartments are hard. Remote supervision helps users a lot."
    assert "abstract" in checks(library(make_review(level="light", abstract=wrong)))
    assert "language" in checks(library(make_review(level="light", extra="- note " + chr(0x4E2D))))


def test_verification_level_is_required(library):
    text = make_review().replace("- verification_level: full\n", "")
    assert "coding" in checks(library(text))
    assert "coding" in checks(library(make_review(level="partial")))


def test_missing_kiro_log_fails(library):
    result = library(make_review(log="- 2026-09-18 | host: codex | scope: legacy | corrections: none"))
    assert "log" in checks(result)


def test_cjk_fails(library):
    result = library(make_review(title="A Test Paper on Slip-Aware Estimation", extra="- note " + chr(0x4E2D)))
    assert "language" in checks(result)


def test_legacy_evidence_path(library):
    bad = make_review(extra="- evidence/T1-T2/abc/parse-local-result.json")
    good = make_review(extra="- 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/abc/x.json")
    assert "legacy-path" in checks(library(bad))
    assert "legacy-path" not in checks(library(good))


def test_wrong_abstract_needs_waiver(library):
    wrong = "Highlights: robots are useful. Apartments are hard. Remote supervision helps users a lot."
    assert "abstract" in checks(library(make_review(abstract=wrong)))
    waived = make_review(abstract=wrong, extra="- abstract-waiver: publisher abstract differs from PDF")
    assert "abstract" not in checks(library(waived))


def test_link_to_local_only_file_fails(library):
    text = make_review(extra=f"- [PDF](../../../01-papers/{THEME}/{FOLDER}/paper.pdf)")
    assert "links" in checks(library(text))


def test_large_review_warns_but_passes(library):
    assert not any(w.check == "size" for w in library(make_review()).warnings)
    result = library(make_review(extra="- note " + "x" * rc.MAX_REVIEW_BYTES))
    assert result.ok, result.issues
    assert any(w.check == "size" for w in result.warnings)


def test_missing_section_fails(library):
    text = make_review().replace("## Transfer conditions\n\nNeeds wheel torque data.\n\n", "")
    assert "sections" in checks(library(text))
