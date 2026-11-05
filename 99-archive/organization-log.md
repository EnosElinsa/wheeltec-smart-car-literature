# Organization log

> **Stage record, October 25, 2026.** Its counts and statuses describe that date and are not updated. Current totals are in the [repository README](../README.md). The maintenance section dates from November 2, 2026.

Historical organization date: October 25, 2026. At the user's request, source Markdown was restored and stored separately, and all files/directories received English names. Document bodies retained their original language at that time.

Maintenance date: November 2, 2026. Public navigation documents and review cards are now in English. The original 18 key-paper selections are retained, with paper-specific evidence and platform/compute boundaries in the reading guide. The 112 cards comprise 23 full verifications and 89 light conversions; light-card numbers must be rechecked against the PDF before survey citation. `04-analysis/` remains in Chinese, and the existing survey manuscript is unchanged.

## Current layout

- `01-papers/`: 112 local PDFs and original BibTeX files.
- `02-fulltext/`: 112 local `paper.md` files and 2,200 referenced source images.
- `03-reviews/`: 112 separate English `review.md` cards.
- `04-analysis/`, `05-survey/`, and `06-data/`: research synthesis, survey sources, and unified data.
- `99-archive/`: the local historical archive and verification records.

Markdown for the baseline 45 + 7 papers was restored from the historical archive using SHA-256 checks. The 60 expansion texts were restored from the original MinerU precision cache, with PDF and Markdown hashes checked against parsing receipts. All `paper.md` files retain their source bytes and relative image references; their bodies were not regenerated. Unreferenced temporary image copies were excluded from reading directories.

Directories, data tables, cross-document links, and VINS source references were updated together during organization. PDFs, BibTeX, and the existing survey PDF/TeX/references/figures retained their original bytes. After restoring source texts and images, the previous 370-file total no longer described the library; navigation remained organized by section and theme.

Historical integrity, image-link, English-name, and archive checks are recorded in [organization-verification.json](organization-verification.json).

## Historical verification recorded on October 25

These are the recorded results of the October 25 organization, rather than a new November 2 verification run:

- All 112 PDF/BibTeX pairs and 112 Markdown files matched their source hashes.
- All 2,200 referenced source-image hashes passed; 5,635 local links were checked with zero broken links.
- Current file/directory names and archive member names used English ASCII.
- All original 4,842 files could be recovered from the historical archive and current formal originals, with individual hash checks passing; the ZIP CRC check passed.
- The existing survey PDF and source files retained their original bytes.

## November 2 data maintenance

`06-data/corpus-comparison.csv` and the current review cards replace the old comparison/evidence snapshots. Their historical copies are stored locally at `99-archive/superseded/expansion-comparison.csv`, `99-archive/superseded/expansion-evidence.csv`, `99-archive/superseded/baseline-evidence.jsonl`, and `99-archive/superseded/expansion-summary.json`. The active `06-data/fulltext-manifest.json` remains byte-preserved provenance.

The 79 historical candidate rows retain their order, identity, theme, title, status, and source-review fields; their reasons are translated into English. The exact original table is preserved at `99-archive/superseded/followup-candidates.original.csv`. Separate follow-up screening handles duplicate identities and formal-corpus overlaps without claiming candidate acquisition or full-text verification.
