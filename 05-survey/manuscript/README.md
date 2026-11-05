# Wheeled mobile robot autonomy under degradation

Working survey draft: *Wheeled Mobile Robot Autonomy Under Degradation: A Survey of Methods and Evaluation*.

[Main paper](survey.pdf) · [Supplement](supplement.pdf) · [Revision status](REVISION-REPORT.md) · [Evidence library](../../README.md)

The current paper compares 245 selected publications (244 technical and one context review) with 25 additional background references, for 270 references. All corpus works date from 2021-2026, and seven background references are foundational pre-2021 sources cited for attribution. It compares degradation responses across estimation, planning, semantic navigation, coordination and reliability. Assessment depth and non-exhaustive selection are disclosed in the supplement. N01–N20, S01–S48, R01–R36 and K01–K16 are integrated into the technical comparisons, evaluation discussion and open questions; the S, R and K cards are targeted readings, not whole-paper audits. X01/X15 remain internal library sources.

The main paper has 24 pages, the T-IV maximum, and the supplement 17. [REVIEW-FIXES-6.md](revision/REVIEW-FIXES-6.md) records the current revision: the concise review method of Section III with the selection table in supplement S1, the short AI-use acknowledgment and the redrawn Fig. 2. The [revision evidence guide](revision/README.md) lists every earlier round, and [REVISION-REPORT.md](REVISION-REPORT.md) summarizes the state of the draft and the items open before submission.

This directory is part of the evidence-library repository, which is the project's only repository. The manuscript was a separate Git repository until November 4, 2026. That repository has been deleted from GitHub, and its history is kept in a local backup bundle.

## Layout

| Path | Content |
|---|---|
| `survey.tex`, `supplement.tex`, `survey-format.tex`, `sections/` | LaTeX sources of the main paper and the supplement |
| `survey.pdf`, `supplement.pdf` | Built PDFs |
| `refs.bib`, `ieee-bst-control.bib` | Bibliography written by `scripts/build_data.py`, and the IEEEtran control entry |
| `figures/` | SVG figure sources and the vector PDFs that LaTeX includes |
| `generated/` | Tables, statistics macros and data products written by `scripts/build_data.py` |
| `data/` | Maintained inputs: citation scope, interface decisions, numerical comparisons, equation baseline and related surveys |
| `scripts/` | Data, figure, coding and verification scripts |
| `revision/` | Revision records, audits, verification reports and background source records |
| `notes/` | Planning notes of earlier stages |

## Requirements

- A TeX distribution (TeX Live or MiKTeX) with `latexmk`, IEEEtran, `graphicx`, `xr` and BibTeX.
- Python 3.11 or later with PyMuPDF (`pip install pymupdf`) for the figures.
- `pdfinfo` from Poppler on `PATH` for the verifier.

The scripts run from this directory. They locate the evidence library two levels up (the repository root); set `WHEELTEC_LITERATURE_ROOT` to use another checkout.

## Build

```shell
python scripts/build_data.py
python scripts/build_figures.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error supplement.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error survey.tex
python scripts/verify_delivery.py
```

The committed bibliography, generated tables and figures compile as they are, so the two Python steps are needed only after a change to the library data or a figure. `build_data.py` writes `refs.bib` and everything in `generated/` from the paper index, the selection record, the evidence codes, `data/citation-scope.json` and the background records in `revision/background-sources/`. The main paper cites supplement labels through `xr`, so build the supplement first. After section or supplement edits, `latexmk` can report that the targets are up to date; add `-gg` to force a full rebuild.

## Figures

`figures/*.svg` are the editable figure sources and `figures/*.pdf` the vector files that LaTeX includes. The figures are grayscale with Times text, matching the IEEEtran body font. `scripts/build_figures.py` writes both file types, and `scripts/svgkit.py` holds the drawing helpers. The corpus figure of the supplement reads `generated/corpus-year-module.json`, written by `scripts/build_data.py`. PyMuPDF ignores SVG dash arrays and markers, so the helpers draw dashes and arrowheads as explicit segments and polygons.

## Verification

The verifier requires successful builds and `pdfinfo` on PATH. Its default mode checks public corpus data, citations, labels, equations, generated quantities and PDF diagnostics, and records the repository commit the checked tree is based on. To additionally verify all 741 source artifacts, restore the local PDFs/transcriptions at their indexed paths and run:

```shell
python scripts/verify_delivery.py --sources
```

The public library excludes publisher full texts. Missing local sources must not be interpreted as completed source verification. Original publisher citations are retained in the library; `refs.bib` is the manuscript's derived bibliography, in which `scripts/bib_case.py` brace-protects acronyms and proper names in titles for IEEEtran sentence case and `scripts/build_data.py` capitalizes one lowercase author name of the LM-Nav export. `ieee-bst-control.bib` applies the IEEE rule of listing the first author and "et al." for entries with more than six authors. Numerical comparison locators and source hashes are in `data/`.

## Status and rights

Author details and submission declarations remain incomplete. The public snapshot was authorized by the repository owner; no submission acceptance or venue approval is implied. No license is granted for the manuscript text, figures, generated tables or built PDFs before publication. The scripts in `scripts/` are MIT-licensed, and third-party source material is not covered (see the [license table](../../README.md#license)).

[Refresh integration](revision/IEEE-REFRESH-INTEGRATION.md), [expansion integration audit](revision/SURVEY-EXPANSION-INTEGRATION.md) and [IEEE integration notes](notes/ieee-integration-plan.md) record earlier stages.
