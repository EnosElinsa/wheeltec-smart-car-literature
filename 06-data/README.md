# Data and provenance

Public documentation and review cards are in English after the November 2, 2026 maintenance. Source texts and historical records retain their original bytes and language. The reviewed library has **127 papers**, with a review-card total of **23 full verification and 104 light**, comprising 89 historical conversions and 15 targeted readings. All 15 follow-up papers have registered official PDF/raw-BibTeX pairs. The user manually supplied the previously inaccessible F03/F09/F11 PDFs; their identities, authors, DOIs, and volume/issue details were checked before registration. No selected paper lacks a PDF. All 15 additions have MinerU precision transcriptions and targeted light cards; all 127 cards passed `review_check --pdf`. The historical corpus remains 112 papers (45 baseline + 7 neighboring + 60 expansion). The [workflow](../03-reviews/WORKFLOW.md) and [vocabulary](vocabulary.md) define the evidence limits of each level.

| File | Purpose |
|---|---|
| [paper-index.csv](paper-index.csv) | 127 registered papers: IDs, themes, titles, years, DOIs, batches, source/review paths, and hashes |
| [corpus-comparison.csv](corpus-comparison.csv) | 127-paper comparison derived from review cards, including `verification_level` |
| [fulltext-manifest.json](fulltext-manifest.json) | Source-text provenance: restoration or parsing source, mode, Markdown SHA-256, and image hashes for the 127-paper library; original source bytes preserved |
| [followup-candidates.csv](followup-candidates.csv) | 79 historical title/abstract-screened rows; identities may repeat or overlap the formal corpus; reasons translated into English |
| [candidate-screening.csv](candidate-screening.csv) | Identity-level follow-up screening and corpus-overlap decisions; does not establish acquisition |
| [followup-shortlist.md](followup-shortlist.md) | User-confirmed fixed selection F01–F15 and original title/abstract screening questions |
| [followup-status.csv](followup-status.csv) | Acquisition, transcription, and review status for the fixed selection, including the resolved manual PDF deliveries |
| [followup-assessment.md](followup-assessment.md) | Selected-page findings against the four follow-up questions, with evidence and access limits kept separate |
| [search-coverage.md](search-coverage.md) | Historical search coverage and evidence boundaries |
| [source-policy.md](source-policy.md) | Source, naming, version, and inclusion rules |
| [ieee-supplement-2026-11-03/README.md](ieee-supplement-2026-11-03/README.md) | Separate IEEE batch: all 20 PDF/BibTeX pairs and local full-text exports complete; 13 targeted source readings; excluded from the 127-paper reviewed statistics |
| [ieee-supplement-2026-11-03/manual-import.md](ieee-supplement-2026-11-03/manual-import.md) | Seven user-downloaded IEEE pairs matched by DOI and archived with original bytes; source-to-library file map and hashes |

The index, comparison, and follow-up CSV files use UTF-8 with a BOM; `review-corrections.csv` uses UTF-8. The `pdf`, `bibtex`, `markdown`, and `review` fields in `paper-index.csv` are relative to the library root; legacy fields retain historical source paths. PDFs and source Markdown are local, gitignored artifacts, for example `01-papers/<theme>/<folder>/paper.pdf` and `02-fulltext/<theme>/<folder>/paper.md`. PDF pages remain the publication reference for formulas, tables, and layout. E50/E60 and F07/F08 have no DOI and are distinguished using their official PMLR sources and selection IDs.

`corpus-comparison.csv` and the individual review cards replace the old expansion comparison and evidence tables. Historical files are retained locally at `99-archive/superseded/expansion-comparison.csv`, `99-archive/superseded/expansion-evidence.csv`, `99-archive/superseded/baseline-evidence.jsonl`, and `99-archive/superseded/expansion-summary.json`. These legacy snapshots do not describe the current verification levels. The exact pre-translation candidate CSV is retained at `99-archive/superseded/followup-candidates.original.csv`.

A full card reflects whole-paper verification, including numeric checks against rendered tables. The 89 historical light conversions preserve legacy extractions with mechanical metadata, abstract, and quotation checks; numerical claims were not re-verified. The 15 new targeted light cards have no legacy extraction: they log the selected source passages read and check retained excerpts and numbers within that scope. Their transcription-bound validation is separate from whole-paper verification; any survey citation still requires a targeted numerical recheck. A passing checker does not imply whole-paper reading. Neither level proves transfer to the R680. The 79 historical candidate rows and 18 historical key-paper selection remain distinct from the new acquisition and assessment records.

## Claim IDs

| ID | Meaning of the original research claim | Boundary |
|---|---|---|
| C1 | Six themes organize the research | A reading framework, without exhaustive direct support as a taxonomy |
| C2 | Perception degradation and dynamic environments affect localization and navigation | Direct evidence exists in the original baseline corpus |
| C3 | Learned navigation is constrained by sim-to-real transfer, safety, data, and compute | Direct evidence exists in the original baseline corpus |
| C4 | Multiple robots add communication, coordination, scalability, and heterogeneity constraints | Direct evidence and qualifications exist in the original baseline corpus |
| C5 | Long-term autonomy requires detection, uncertainty handling, recovery, and system evaluation | Direct evidence exists in the original baseline corpus |
| C6 | R680 research directions need mechanism evidence and reproducible hardware conditions | A transfer criterion, not evidence that the R680 has been validated |

Original metadata, provenance, parser records, and complete historical scope remain at their original member paths in the [archive](../99-archive/README.md). Historical absolute paths are audit records and should not be used to rerun old tools directly in the reorganized tree.
