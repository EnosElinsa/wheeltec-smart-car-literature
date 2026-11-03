# WHEELTEC Smart Car Literature Library

A theme-organized library of **147 publications** on wheeled mobile robot autonomy. Every paper uses the same ID and theme directory for its source files, transcription and assessment.

| Find | Entry point |
|---|---|
| All papers, citations and local PDF paths | [Paper index](01-papers/INDEX.md) |
| Full-text transcriptions and local paths | [Full-text index](02-fulltext/INDEX.md) |
| Existing review cards | [Review index](03-reviews/INDEX.md) |
| Key papers and reading routes | [Reading guide](READING_GUIDE.md) |
| Cross-paper synthesis | [Evidence synthesis](04-analysis/evidence-synthesis.md) |
| Use of newly assessed evidence | [Integration analysis](04-analysis/ieee-evidence-utilization-2026-11-03.md) |
| Survey manuscript | [Manuscript guide](05-survey/README.md) |
| Complete catalog, survey coding and source records | [Data guide](06-data/README.md) |

## Organization

- `01-papers/<theme>/<year>-<short-name>-<ID>/`: PDF and original publisher BibTeX.
- `02-fulltext/<theme>/<year>-<short-name>-<ID>/`: source transcription and referenced images.
- `03-reviews/<theme>/<year>-<short-name>-<ID>/`: review card, where completed.
- `04-analysis/`: comparisons, evidence synthesis and research plans.
- `05-survey/`: guide to the separately maintained manuscript repository.
- `06-data/`: the unified catalog, survey coding, reading ledgers and provenance.

Publisher PDFs, transcriptions and extracted images remain local. Public indexes show their paths and link to citation exports, assessments and official sources.

## Assessment and survey coverage

Of the 147 registered publications, **127 have review cards**: 23 full-verification cards and 104 light cards. The light cards comprise 89 historical extract-based assessments and 15 targeted readings. The other **20 have targeted source notes**, with physical-page locators and explicit limits, and appear alongside all other papers in the theme indexes.

The current survey uses the 127-paper reviewed selection, comprising 124 technical publications and three context works. Library registration and manuscript inclusion are different statuses. Targeted reading does not imply whole-paper verification; numerical claims need checks against the original PDF. The [review workflow](03-reviews/WORKFLOW.md) defines assessment depth, and the [unified catalog](06-data/library-catalog.csv) records each paper's status.

## Maintenance

```shell
python -m tools.build_indexes --strict
python -m tools.locate N02 --info
python -m tools.check_links
python -m tools.check_public_tree --cjk strict
```

[Source policy](06-data/source-policy.md) · [Coding vocabulary](06-data/vocabulary.md) · [Historical archive guide](99-archive/README.md)
