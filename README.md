# WHEELTEC Smart Car Literature Library

An evidence library and survey manuscript on wheeled mobile robot autonomy under degradation. The library holds 247 assessed publications with review cards, coded comparison data and source provenance. The manuscript, *Wheeled Mobile Robot Autonomy Under Degradation: A Survey of Methods and Evaluation*, is built from the same data in [05-survey/manuscript/](05-survey/manuscript/README.md).

The library supports research on the WHEELTEC R680 wheeled robot. A robot or computer reported in a paper is not evidence that the method has been deployed on the R680.

**Status (November 5, 2026):** working draft. The survey has not been submitted, and its author information and submission declarations are incomplete. The corpus is a purposive selection, not an exhaustive or systematic search of the field.

## At a glance

| Item | Count |
|---|---|
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

The provenance ledgers record the transcription pipeline of each paper. The 127 papers of the baseline, supplemental, expansion and follow-up batches keep the MinerU precision exports or archived original exports listed in [fulltext-manifest.json](06-data/fulltext-manifest.json). N01-N20 use local PyMuPDF4LLM exports, S01-S48 and R01-R36 use OXR-1.0 through self-hosted vLLM, and K01-K16 use PyMuPDF4LLM 0.2.9. The PDF stays the authority for numbers, tables, equations and page numbers.

## Requirements

- Python 3.11 or later, with `pymupdf` (PDF text, page rendering and figure conversion), `requests` (background-record verification only) and `pytest`. The tools were last run with Python 3.14, PyMuPDF 1.27 and pytest 8.4.
- For the manuscript: a TeX distribution with `latexmk`, IEEEtran, `graphicx` and `xr`, and `pdfinfo` from Poppler on `PATH`.

```shell
python -m pip install pymupdf requests pytest
```

Run every command from the repository root unless a section says otherwise.

## Checks

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

## Citation and license

The survey is unpublished. Until it appears, cite this repository by its URL and the commit you used.

No license file is published yet. `pyproject.toml` declares the MIT license for the Python tools. No license is granted for the review cards, analyses, data or manuscript. Bibliographic metadata and abstracts quoted in the cards remain the property of their publishers and authors.
