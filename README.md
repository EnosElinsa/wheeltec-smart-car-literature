# WHEELTEC Smart Car Literature Library

A theme-organized library of **231 acquired and assessed publications** on wheeled mobile robot autonomy. The current survey manuscript selects 229 of them. All 231 papers have source Markdown. The 84 most recent additions (S01-S48 and R01-R36) were transcribed with OXR-1.0 through self-hosted vLLM; the original 147 transcriptions remain unchanged. Source files, transcriptions and assessments use matching IDs and theme directories.

| Find | Entry point |
|---|---|
| All papers, citations and local PDF paths | [Paper index](01-papers/INDEX.md) |
| Full-text transcriptions and local paths | [Full-text index](02-fulltext/INDEX.md) |
| Review cards | [Review index](03-reviews/INDEX.md) |
| Key papers and reading routes | [Reading guide](READING_GUIDE.md) |
| Cross-paper synthesis | [Evidence synthesis](04-analysis/evidence-synthesis.md) |
| Latest survey review and 36-paper integration | [IEEE refresh integration](04-analysis/ieee-refresh-integration-2026-11-03.md) |
| 36-paper IEEE refresh: selection, acquisition and readings | [Batch guide](06-data/ieee-refresh-2026-11-03/README.md) |
| Earlier 48-paper expansion | [Expansion toward 200 references](06-data/survey-200plus-2026-11-03/README.md) |
| Survey manuscript | [Manuscript guide](05-survey/README.md) |
| Complete catalog, survey coding and source records | [Data guide](06-data/README.md) |

## Organization

- `01-papers/<theme>/<year>-<short-name>-<ID>/`: PDF and a citation, with original publisher exports retained beside any explicitly derived version.
- `02-fulltext/<theme>/<year>-<short-name>-<ID>/`: source transcription and referenced images.
- `03-reviews/<theme>/<year>-<short-name>-<ID>/`: review card.
- `04-analysis/`: comparisons, evidence synthesis and research plans.
- `05-survey/manuscript/`: the survey manuscript (LaTeX sources, SVG/PDF figures, generated tables, bibliography, built PDFs and verification records).
- `06-data/`: the unified catalog, survey coding, reading ledgers and provenance.

Publisher PDFs, transcriptions and extracted images remain local. Public indexes show their paths and link to citation exports, assessments and official sources.

## Assessment and survey coverage

All **231 publications have review cards**: 23 full assessments and 208 light assessments. The light cards comprise 89 historical extract-based assessments and 119 targeted readings with physical-page locators and explicit limits. Targeted reading does not imply whole-paper verification; the [review workflow](03-reviews/WORKFLOW.md) defines assessment depth, and numbers cited in the survey are rechecked against the PDF.

The manuscript cites 229 selected works (228 technical studies and one context review) and 9 background references, for **238 references, all from 2021-2026**. X01 (1999) and X15 (2016) remain internal references, as do the pre-2021 background sources removed from the bibliography. The [selection record](06-data/survey-inclusion.json) holds the current membership and the historical baseline; the [unified catalog](06-data/library-catalog.csv) records each paper's status.

## Maintenance

```shell
python -m tools.build_indexes --strict
python -m tools.locate N02 --info
python -m tools.check_links
python -m tools.check_public_tree --cjk strict
```

The manuscript has its own build and verification steps in [05-survey/manuscript/README.md](05-survey/manuscript/README.md).

[Source policy](06-data/source-policy.md) · [Coding vocabulary](06-data/vocabulary.md) · [Historical archive guide](99-archive/README.md)
