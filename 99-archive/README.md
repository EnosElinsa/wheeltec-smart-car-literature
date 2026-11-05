# Archive

The local archive `99-archive/history-2026-10-25.zip` preserves original discovery, screening, audits, metadata/provenance, old reports, scripts, logs, earlier versions, and excluded papers. Archive member names use English; the original file manifest is `original-file-manifest.json` inside the ZIP.

The archive covers the 112 papers of the October 25, 2026 organization, which have local PDF/BibTeX files in `01-papers/`, source Markdown in `02-fulltext/`, and English review cards in `03-reviews/`. Later batches are listed in the [changelog](../CHANGELOG.md) and keep their provenance in `06-data/`. The archive retains the baseline corpus's original Markdown and images for traceability. Parsed Markdown for the 60 expansion papers was restored from the original cache to `02-fulltext/` with hash checks and no longer depends solely on that machine cache.

The archived `original-file-manifest.json` records 4,842 files and their hashes before reorganization. The `legacy_paper_dir` and current paths in [paper-index.csv](../06-data/paper-index.csv) match the formal PDFs/BibTeX files; [fulltext-manifest.json](../06-data/fulltext-manifest.json) records source-text restoration provenance and SHA-256 hashes. Extract historical materials into a separate directory to avoid overwriting current files.

The original frozen ledgers, hash differences, and absolute paths remain historical records; they were not rewritten to make old tools pass. Use the root README and current data tables for active filenames and paths.

The November 2, 2026 maintenance translates public documentation and review cards while retaining October 25 as the historical organization and key-paper selection date. At that maintenance the 112 cards comprised 23 full verifications and 89 light conversions. Historical screening records should not be read as proof of uniform full verification.

Superseded data snapshots are retained locally as `99-archive/superseded/expansion-comparison.csv`, `99-archive/superseded/expansion-evidence.csv`, `99-archive/superseded/baseline-evidence.jsonl`, and `99-archive/superseded/expansion-summary.json`. The current `06-data/corpus-comparison.csv` and individual review cards replace them. `99-archive/superseded/followup-candidates.original.csv` preserves the exact candidate-table bytes before its reasons were translated into English. Follow-up screening does not establish acquisition or add candidates to the formal corpus. The active `06-data/fulltext-manifest.json` remains byte-preserved provenance.

The gitignored folder `99-archive/local/` holds later local-only material, for example the backup bundle of the former manuscript repository and the reports of the simulated manuscript reviews.

[Organization log](organization-log.md)
