# WHEELTEC Smart Car Literature Library

[![Checks](https://github.com/EnosElinsa/wheeltec-smart-car-literature/actions/workflows/checks.yml/badge.svg)](https://github.com/EnosElinsa/wheeltec-smart-car-literature/actions/workflows/checks.yml)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE-MIT)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE-CC-BY-4.0)

An evidence library and survey manuscript on wheeled mobile robot autonomy under degradation. The library holds 247 assessed publications with review cards, coded comparison data and source provenance. The manuscript, *Wheeled Mobile Robot Autonomy Under Degradation: A Survey of Methods and Evaluation*, is built from the same data in [05-survey/manuscript/](05-survey/manuscript/README.md).

The library supports research on the WHEELTEC R680 wheeled robot. A robot or computer reported in a paper is not evidence that the method has been deployed on the R680.

**Unified library:** 650 distinct records: 247 assessed publications, 226 unassessed source additions, six supplemental surveys and 171 excluded/background references. All 479 active sources have transcribed reading sets in the six theme directories in [the catalog](06-data/library-catalog.csv). Open the local `INDEX.html` to search and read them. The 232 active additions remain unassessed and outside the survey selection. [Latest addition](06-data/coverage-expansion-2026-11-11/README.md): 24 ICRA/IROS 2025 papers across six themes, with 176 OXR pages. Future journal downloads require JCR Q1; RA-L, AURO and JFR are excluded from new acquisition. See [current work](06-data/current-work.md).

**Status (November 5, 2026):** working draft. The survey has not been submitted, and its author information and submission declarations are incomplete. The corpus is a purposive selection, not an exhaustive or systematic search of the field.

## At a glance

| Item | Count |
|---|---|
| Acquired sources | 479 transcribed reading sets in six themes; one additional formal reading set is retained as method background |
| Assessed publications | 247 (203 journal articles, 44 conference papers) in six themes |
| Review cards | 247: 23 full assessments and 224 light assessments (89 historical conversions, 135 targeted readings) |
| Survey selection | 245 works from 2021-2026 (244 technical studies, one context review). X01 (1999) and X15 (2016) stay internal |
| Manuscript references | 270: the 245 selected works and 25 background references, 7 of them foundational pre-2021 sources |
| Manuscript length | 24-page main paper and 17-page supplement |

Assessment depth differs between cards. A full card records a whole-paper reading with numbers checked against the rendered PDF. A light card records the scope that was read, and every number the survey takes from a light card is rechecked against the PDF. The [review workflow](03-reviews/WORKFLOW.md) defines both levels.

## Where to start

| Goal | Entry point |
|---|---|
| Read the survey | [Main paper (PDF)](05-survey/manuscript/survey.pdf) · [Supplement (PDF)](05-survey/manuscript/supplement.pdf) · [Revision status](05-survey/manuscript/REVISION-REPORT.md) |
| Read the key papers in order | [Reading guide](READING_GUIDE.md) (18 key papers and two reading routes) |
| Browse all review cards | [Review index](03-reviews/INDEX.md) |
| Find a paper, its citation and its local files | [Paper index](01-papers/INDEX.md) · [Full-text index](02-fulltext/INDEX.md) |
| Use the data tables and evidence codes | [Data guide](06-data/README.md) · [Evidence coding](06-data/evidence-coding/README.md) |
| Look up a coding value | [Controlled vocabulary](06-data/vocabulary.md) |
| Trace an earlier stage | [Analysis records](04-analysis/README.md) · [Manuscript revision records](05-survey/manuscript/revision/README.md) · [Changelog](CHANGELOG.md) |

## Repository layout

```text
01-papers/<theme>/<year>-<short-name>-<ID>/    citation.bib and provenance (PDF local only)
02-fulltext/<theme>/<year>-<short-name>-<ID>/  source transcription and images (local only)
03-reviews/<theme>/<year>-<short-name>-<ID>/   review.md, one card per paper
04-analysis/                                   dated cross-paper analyses and research plans
05-survey/manuscript/                          LaTeX sources, figures, generated tables, built PDFs, revision records
06-data/                                       catalog, paper index, evidence codes, batch provenance
99-archive/                                    archive guide (the archive itself is local)
tools/                                         Python checks and index generators, with tests
```

A paper keeps the same theme, folder name and ID in `01-papers/`, `02-fulltext/` and `03-reviews/`. The ID prefix names the acquisition batch, for example M for the baseline journal corpus and K for the review additions. The [source policy](06-data/source-policy.md) lists every batch and the six themes.

## Public and local content

The repository publishes only self-authored material: review cards, analyses, data tables, citation exports and provenance records, indexes, tools, and the manuscript sources, figures and built PDFs. Publisher PDFs, full-text transcriptions, extracted figures and the historical archive stay on the maintainer's machine for copyright reasons. Public pages show their paths as code, not as links. `tools.check_public_tree` enforces this rule, together with the English-only rule and the absence of local absolute paths and secrets.

The provenance ledgers record the transcription pipeline of each paper. The 127 papers of the baseline, supplemental, expansion and follow-up batches keep the MinerU precision exports or archived original exports listed in [fulltext-manifest.json](06-data/fulltext-manifest.json). N01-N20 use local PyMuPDF4LLM exports, S01-S48, R01-R36 and D01-D11 use OXR-1.0 through self-hosted vLLM, and K01-K16 use PyMuPDF4LLM 0.2.9. The PDF stays the authority for numbers, tables, equations and page numbers.

## Requirements

- Python 3.11 or later, with `pymupdf` (PDF text, page rendering and figure conversion), `requests` (background-record verification only) and `pytest`. The tools were last run with Python 3.14, PyMuPDF 1.27 and pytest 8.4.
- For the manuscript: a TeX distribution with `latexmk`, IEEEtran, `graphicx` and `xr`, and `pdfinfo` from Poppler on `PATH`.

```shell
python -m pip install pymupdf requests pytest
```

Run every command from the repository root unless a section says otherwise.

## Checks

The [Checks workflow](.github/workflows/checks.yml) runs every check below that needs no local sources, on each push to `main` and on pull requests, with Python 3.11 and 3.14. It fails when a check fails or when the regenerated indexes or tables differ from the committed files.

| Command | What it checks | Needs local sources |
|---|---|---|
| `python -m pytest` | Unit tests of the tools (`tools/tests`) | No |
| `python -m tools.build_indexes --strict` | Regenerates the indexes and the catalog from the paper index and the cards; fails on cards without coding | No |
| `python -m tools.build_tables --strict` | Rebuilds the coding columns of the paper index and `corpus-comparison.csv` from the cards | No |
| `python -m tools.check_links` | Relative links in all tracked Markdown files; flags links to local-only files | No |
| `python -m tools.check_public_tree --cjk strict` | Public-tree policy: no publisher files, no CJK text, no local paths, no secrets | No |
| `python -m tools.review_check --all --pdf` | Card structure, vocabulary and excerpts against the PDF pages | Yes |
| `python -m tools.locate <ID> --info` | Paths, DOI, URL and page count of one paper (`--find`, `--page` and `--render` read the PDF) | Yes, except `--info` |

The manuscript has its own build and verification steps, described in the [manuscript guide](05-survey/manuscript/README.md).

## Contributing

The repository is maintained by its owner. [CONTRIBUTING.md](CONTRIBUTING.md) describes the conventions, the procedure for adding a batch of papers and the checks to run before a commit. Corrections to a card or a data value are welcome as GitHub issues that name the paper ID and the PDF page.

## Citation

The survey is unpublished. Until it appears, cite this repository as described in [CITATION.cff](CITATION.cff), which GitHub shows under "Cite this repository", and name the commit you used.

## License

| Material | Paths | Terms |
|---|---|---|
| Code | `tools/`, `05-survey/manuscript/scripts/`, `.github/` | [MIT](LICENSE-MIT) |
| Review cards, analyses, data, provenance records, indexes and documentation | `03-reviews/`, `04-analysis/`, `06-data/`, the provenance files in `01-papers/`, and the Markdown files outside `05-survey/manuscript/` | [CC BY 4.0](LICENSE-CC-BY-4.0) |
| Survey manuscript | `05-survey/manuscript/` except `scripts/`: LaTeX sources, figures, generated tables, built PDFs and revision records | No license is granted before publication. All rights are reserved |
| Third-party material | Publisher citation exports (`*.bib` and `*.ris` files in `01-papers/` and `06-data/`), Crossref and catalogue records, and the abstracts and excerpts quoted in the cards | Not covered by these licenses. The rights stay with their owners |

To attribute CC BY 4.0 material, name Zhiyuan Cai and the WHEELTEC Smart Car Literature Library, link this repository, and state any changes you made.
