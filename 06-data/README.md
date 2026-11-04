# Data and provenance

The unified catalog lists **247 acquired and assessed publications** in the shared theme directories. The working survey selects 245: 244 technical studies and one context review. X01/X15 remain assessed internal references, and all pre-2021 background citations are now internal (see the [refresh integration](../04-analysis/ieee-refresh-integration-2026-11-03.md)). The 48 S-series additions retain 44 strict native pairs, three derived citations and one documented publisher title variant; the 16 K-series review additions retain 15 native pairs and one derived citation (K11). The review-card set contains 23 full assessments and 224 light assessments, comprising 89 historical extract-based assessments and 135 targeted readings. The [workflow](../03-reviews/WORKFLOW.md) and [vocabulary](vocabulary.md) define their evidence limits. Source files retain their original bytes; acquisition and extraction details are recorded in the provenance ledgers below.

| File | Purpose |
|---|---|
| [library-catalog.csv](library-catalog.csv) | Unified catalog of all 247 acquired publications, including source paths, assessment status and current survey selection |
| [evidence-coding/README.md](evidence-coding/README.md) | Evidence-coding layer of the 245-work survey selection: codebook v1.0 with operational definitions, decision rules, the coding unit, double-coding attributes, and the sampling, interface-ranking and sensitivity rules fixed before coding |
| [review-additions-2026-11-04/README.md](review-additions-2026-11-04/README.md) | 16 reviewer-named 2021-2024 works (K01-K16): official pairs, local PyMuPDF4LLM transcriptions (262 pages) and targeted light cards; all 16 are survey selection members |
| [review-additions-2026-11-04/source-reading.json](review-additions-2026-11-04/source-reading.json) | Page scopes and excerpts for the 16 K-series light cards |
| [survey-200plus-2026-11-03/README.md](survey-200plus-2026-11-03/README.md) | All 48 additions registered: 44 strict native pairs, three derived citations, one publisher title variant; 48-work integration stage; current manuscript has 203 references after age-policy filtering |
| [survey-200plus-2026-11-03/manual-import.md](survey-200plus-2026-11-03/manual-import.md) | User-download import and follow-up: original citations preserved; all five remaining records resolved with explicit provenance |
| [survey-200plus-2026-11-03/markdown-coverage.md](survey-200plus-2026-11-03/markdown-coverage.md) | Markdown audit: all 195 files verified; all 48 additions use OXR-1.0/vLLM with page JSON and image assets |
| [survey-200plus-2026-11-03/source-reading.json](survey-200plus-2026-11-03/source-reading.json) | Page scopes, excerpts, mechanisms and transfer judgments for all 48 new light cards |
| [survey-200plus-2026-11-03/integration-verification.json](survey-200plus-2026-11-03/integration-verification.json) | Historical 195-work/211-reference integration stage before the age-policy revision |
| [integration-verification.json](integration-verification.json) | Historical audit of the earlier incorporation, including its public-clone checks |
| [ieee-refresh-2026-11-03/README.md](ieee-refresh-2026-11-03/README.md) | 36 recent IEEE pairs, OXR transcriptions (482 pages) and targeted light cards; all 36 are manuscript members |
| [ieee-refresh-2026-11-03/source-reading.json](ieee-refresh-2026-11-03/source-reading.json) | Page scopes and excerpts for the 36 R-series light cards |
| [survey-inclusion.json](survey-inclusion.json) | Current membership, selection date, and historical baseline hashes/commit |
| [paper-index.csv](paper-index.csv) | 247-paper assessed library index; manuscript inclusion is controlled separately by survey-inclusion.json: IDs, themes, titles, years, DOIs, source/review paths, hashes and comparison coding |
| [corpus-comparison.csv](corpus-comparison.csv) | 247-paper comparison derived from review cards, including `verification_level` |
| [fulltext-manifest.json](fulltext-manifest.json) | Source-text provenance: restoration or parsing source, mode, Markdown SHA-256, and image hashes for the historical 127-paper selection; the IEEE manifest covers the other 20 sources; original source bytes preserved |
| [followup-candidates.csv](followup-candidates.csv) | 79 historical title/abstract-screened rows; identities may repeat or overlap the formal corpus; reasons translated into English |
| [candidate-screening.csv](candidate-screening.csv) | Identity-level follow-up screening and corpus-overlap decisions; does not establish acquisition |
| [followup-shortlist.md](followup-shortlist.md) | User-confirmed fixed selection F01–F15 and original title/abstract screening questions |
| [followup-status.csv](followup-status.csv) | Acquisition, transcription, and review status for the fixed selection, including the resolved manual PDF deliveries |
| [followup-assessment.md](followup-assessment.md) | Selected-page findings against the four follow-up questions, with evidence and access limits kept separate |
| [search-coverage.md](search-coverage.md) | Historical search coverage and evidence boundaries |
| [source-policy.md](source-policy.md) | Source, naming, version, and inclusion rules |
| [ieee-supplement-2026-11-03/README.md](ieee-supplement-2026-11-03/README.md) | Acquisition and reading provenance for 20 publications included in the unified catalog and theme directories |
| [ieee-supplement-2026-11-03/utilization-matrix.csv](ieee-supplement-2026-11-03/utilization-matrix.csv) | One row per supplementary paper: target sections, current comparators, supported use, evidence limits and remaining checks |
| [ieee-supplement-2026-11-03/manual-import.md](ieee-supplement-2026-11-03/manual-import.md) | Seven user-downloaded IEEE pairs matched by DOI and archived with original bytes; source-to-library file map and hashes |

The index, comparison, and follow-up CSV files use UTF-8 with a BOM; `review-corrections.csv` uses UTF-8. The `pdf`, `bibtex`, `markdown`, and `review` fields in `paper-index.csv` are relative to the library root; legacy fields retain historical source paths. PDFs and source Markdown are local, gitignored artifacts, for example `01-papers/<theme>/<folder>/paper.pdf` and `02-fulltext/<theme>/<folder>/paper.md`. PDF pages remain the publication reference for formulas, tables, and layout. E50/E60, F07/F08 and K12/K14 have no DOI and are distinguished using their official PMLR sources and selection IDs; K11 has no DOI and is identified through its official NeurIPS Datasets and Benchmarks page.

`corpus-comparison.csv` and the individual review cards replace the old expansion comparison and evidence tables. Historical files are retained locally at `99-archive/superseded/expansion-comparison.csv`, `99-archive/superseded/expansion-evidence.csv`, `99-archive/superseded/baseline-evidence.jsonl`, and `99-archive/superseded/expansion-summary.json`. These legacy snapshots do not describe the current verification levels. The exact pre-translation candidate CSV is retained at `99-archive/superseded/followup-candidates.original.csv`.

A full card reflects whole-paper verification, including numeric checks against rendered tables. The 89 historical light conversions preserve legacy extractions with mechanical metadata, abstract, and quotation checks; numerical claims were not re-verified. The 135 targeted light cards have no legacy extraction: they log the selected source passages read and check retained excerpts and numbers within that scope. Their transcription-bound validation is separate from whole-paper verification; any survey citation still requires a targeted numerical recheck. A passing checker does not imply whole-paper reading. Neither level proves transfer to the R680. The 79 historical candidate rows and 18 historical key-paper selection remain distinct from the new acquisition and assessment records.

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
