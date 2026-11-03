# WHEELTEC Smart Car Literature Library

Historical organization and key-paper selection date: October 25, 2026. English review and documentation maintenance: November 2, 2026. PDFs, source Markdown, and review cards are stored separately and matched by paper ID.

## Reading entry points

| Purpose | Entry point |
|---|---|
| Start with the key papers and reading order | [READING_GUIDE.md](READING_GUIDE.md) |
| Find PDF locations and original BibTeX | [01-papers/INDEX.md](01-papers/INDEX.md) |
| Find source Markdown locations | [02-fulltext/INDEX.md](02-fulltext/INDEX.md) |
| Read individual English review cards | [03-reviews/INDEX.md](03-reviews/INDEX.md) |
| Read the evidence synthesis and R680 research plan | [evidence-synthesis.md](04-analysis/evidence-synthesis.md) · [r680-research-roadmap.md](04-analysis/r680-research-roadmap.md) |
| Collect a baseline or study VINS | [r680-baseline.md](04-analysis/r680-baseline.md) · [vins-principles.md](04-analysis/vins-principles.md) |
| Read the existing survey and writing notes | [05-survey/README.md](05-survey/README.md) |
| Compare papers and check provenance | [06-data/README.md](06-data/README.md) |
| Track the confirmed 15-paper follow-up and completion | [followup-shortlist.md](06-data/followup-shortlist.md) · [followup-status.csv](06-data/followup-status.csv) · [followup-assessment.md](06-data/followup-assessment.md) |
| Inspect the supplementary IEEE source batch | [IEEE reading list and acquisition status](06-data/ieee-supplement-2026-11-03/README.md) · [Selected-source notes](06-data/ieee-supplement-2026-11-03/evidence-notes.md) |

## Directory layout

- **01-papers/**: local PDFs and original `citation.bib` files.
- **02-fulltext/**: local source `paper.md` files and their referenced `images/`.
- **03-reviews/**: individual English `review.md` cards.
- **04-analysis/**: English evidence synthesis, research plans, baseline, and principles.
- **05-survey/**: existing survey PDF, LaTeX, references, and writing notes.
- **06-data/**: paper index, corpus comparison, provenance, corrections, and follow-up screening.
- **99-archive/**: historical materials and organization records.

The first three directories share the same `theme/year-short-name-ID` path. For example, E01 uses `T1-perception-localization/2026-LODESTAR-E01/` in each directory. Source PDFs, source Markdown, and the historical archive are local, gitignored artifacts; their paths are shown as code in the indexes.

## Scope and evidence status

The reviewed library contains **127 papers**, with a review-card total of **23 full-verification cards and 104 light cards**. The light cards comprise 89 historical conversions and 15 new targeted readings. All 15 additions have MinerU precision transcriptions and targeted light cards; all 127 cards passed `review_check --pdf`. A passing structural/source check does not change the reading scope recorded in each card.

The historical corpus contains **112 papers**: 45 baseline journal papers, 7 classic or neighboring works, and 60 expansion papers (45 journal papers and 15 conference papers). Each has a local PDF, BibTeX, source Markdown, and an English review card. The reading guide retains the 18 key papers selected on October 25.

The historical review set has **23 full-verification cards and 89 light-conversion cards**. Full verification reads the whole paper and checks numbers, including tables in rendered PDF pages. Light conversion translates and restructures the legacy extraction and mechanically checks metadata, the abstract, and quotations; its numerical claims have not been re-verified. New targeted light cards instead read selected passages for a stated follow-up question, log their physical PDF pages, and check retained excerpts and selected numerical claims. Neither light procedure is whole-paper verification. Recheck any number from a light card against the PDF before citing it in the survey. The [review workflow](03-reviews/WORKFLOW.md) and [coding vocabulary](06-data/vocabulary.md) define these levels.

The user confirmed a fixed **15-paper follow-up selection, F01–F15**, on November 2. All 15 official PDF/raw-BibTeX pairs are registered. F03/F09/F11 were initially blocked by PDF access; the user manually supplied their official PDFs, whose identities, authors, DOIs, and volume/issue details were checked before registration. No selected paper now lacks a PDF. F11 has a formal publication year of 2026 and an online publication year of 2025; its raw publisher BibTeX is preserved unchanged. Source access does not change the fixed selection or its IDs.

The 79 historical follow-up rows remain screening records, including repeated identities and overlaps with the original corpus. Acquisition status and selected-page evidence are separate: the [status ledger](06-data/followup-status.csv) records source/review completion, while the [follow-up assessment](06-data/followup-assessment.md) records what the reading adds to the four corpus-scoped questions. Neither coverage of those questions nor a gap in this library establishes an exhaustive gap in the research field.

Historical source Markdown was restored from historical files or existing parser caches without regenerating or rewriting the source text. New follow-up transcriptions are bound to their source PDFs and retain their parser provenance. The revised survey covers all 127 selected works, with 124 technical studies and three context works. The supplementary IEEE batch of November 3 now has all 20 PDF/BibTeX pairs and local full-text exports, including seven user-downloaded pairs. All 20 now have targeted source readings, separate from the reviewed index and manuscript statistics. A [utilization analysis](04-analysis/ieee-evidence-utilization-2026-11-03.md) maps them to existing arguments and evidence limits. See the [manual import receipt](06-data/ieee-supplement-2026-11-03/manual-import.md) for the new file map. R680 hardware experiments have not been conducted.

[Archive guide](99-archive/README.md) · [Organization log](99-archive/organization-log.md) · [Source and naming policy](06-data/source-policy.md)
