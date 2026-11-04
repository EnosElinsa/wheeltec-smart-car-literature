# Source and naming policy

Historical organization date: October 25, 2026. English maintenance date: November 2, 2026. File and directory names use English ASCII. Public review cards, analysis and navigation documents are in English. The manuscript is maintained in this repository under `05-survey/manuscript/`; only its self-authored sources, figures, generated data and built PDFs are public. Original historical records retain their audit conclusions and journal-ranking classifications.

## Storage layout

Paths follow `section/theme/year-short-name-ID`. Each paper uses the same theme, short directory name, and ID in three sections:

- `01-papers/`: local `paper.pdf` and `citation.bib`; user-authorized derived citations retain their original `citation-original.bib` or `citation.ris` alongside.
- `02-fulltext/`: local source `paper.md` and its referenced `images/`.
- `03-reviews/`: `review.md`, kept separate from the source text.

PDFs, BibTeX, source Markdown, and source images retain their source bytes. Review cards can be corrected and updated. Relative image paths inside source Markdown are preserved, with required images in their original relative locations; unreferenced temporary image copies are excluded from reading directories. Source PDFs, Markdown, and historical ZIP files are local, gitignored artifacts; public navigation shows their paths as code rather than repository links.

## IDs and scope

- `M01`–`M45`: the original baseline journal corpus, retaining its themes, selection years, and IDs.
- `X01`/`X04`/`X07`/`X08`/`X12`/`X13`/`X15`: seven classic or neighboring supplemental papers.
- `E01`–`E60`: the expansion corpus of 45 journal papers and 15 formal conference papers, ten per theme.
- `F01`–`F15`: the fixed user-confirmed follow-up selection of November 2, 2026; IDs remain unchanged as source access is resolved.
- `N01`–`N20`: the supplementary IEEE source batch of November 3, 2026, tracked in its own [manifest](ieee-supplement-2026-11-03/manifest.json). All 20 now have targeted light review cards and are included in the survey selection. Acquisition alone did not establish inclusion; the [selection record](survey-inclusion.json) records the subsequent assessment.
- `S01`–`S48`: the fixed November 3 selection for [expansion toward 200 references](survey-200plus-2026-11-03/README.md). All 48 additions are registered: 44 strict native pairs, three user-authorized derived citations and one documented publisher title variant. The catalog exposes citation and identity status; see the [resolution evidence](survey-200plus-2026-11-03/evidence-notes.md). All 48 are now manuscript members after targeted source assessment; acquisition alone did not establish inclusion.

- `R01`-`R36`: the recent [IEEE refresh](ieee-refresh-2026-11-03/README.md), with 36 user-supplied official PDF/native-BibTeX pairs and OXR-1.0/vLLM transcriptions. All 36 have targeted light review cards and are manuscript members. R23 (riMESA) directly extends E40 (iMESA); both are kept as separate method entries with the relation stated on both cards.

All 231 acquired publications share the same six theme directories and the [unified catalog](library-catalog.csv). Acquisition manifests preserve provenance; they are not separate paper stores. `paper-index.csv` holds all 231 assessed library sources and coding; `survey-inclusion.json` selects 229 manuscript members and retains X01/X15 internally, while `library-catalog.csv` includes every acquired source and its assessment status. `tools.build_indexes` regenerates the catalog and theme indexes together; sources without transcriptions appear only in the paper index. `tools.locate` searches all registered sources.

All 20 supplementary pairs are acquired. N02, N03, N04, N12, N14, N17, and N20 were supplied by the user as IEEE Xplore downloads and retain `manual_publisher_download` provenance; the other 13 retain their automatic publisher-export provenance. Each PDF and native BibTeX file is copied without rewriting its bytes. Downloads originals are preserved, and the [manual import receipt](ieee-supplement-2026-11-03/manual-import.md) records the correspondence. All 20 supplementary full texts use local PyMuPDF4LLM extraction, distinct from the original corpus's MinerU transcriptions. All 20 now have targeted source readings with physical-page locators. The subsequent light cards retain those reading limits and do not establish whole-paper verification.

Short names aid navigation. Formal titles and DOIs follow `paper-index.csv` and official sources. `selection_year` and `bibliographic_year` are separate so that online-first and final volume/year differences remain visible. Original publisher BibTeX is preserved without rewriting it to match an assigned volume year. For example, F14's raw export retains `year="2025"` and its online publication date, while the PDF assigns volume 50, article 7 to 2026; the card and index expose that formal/online distinction. F11 likewise has a formal publication year of 2026 and an online publication year of 2025; its raw publisher BibTeX is preserved unchanged. Formal conference papers without a DOI are identified through their official pages and `selection_id`; F07/F08 use PMLR v270, whose publication year is 2025 for CoRL 2024.

The reviewed library contains 231 papers: **23 full assessments and 208 light cards**, comprising 89 historical conversions and 119 targeted readings. The current manuscript selects 229 works, excluding X01/X15; its 206 light cards comprise 87 historical conversions and 119 targeted readings. The manuscript cites only 2021-2026 work; pre-2021 sources remain internal references. The November 2 selection of 127 remains identifiable through its commit and source-index hashes in [survey-inclusion.json](survey-inclusion.json). The F01–F15 transcriptions use MinerU precision; N01–N20 use the explicitly recorded local PyMuPDF4LLM extraction. Full assessment covers whole-paper reading and rendered-table checks; light assessment covers the scope recorded on each card. A passing format/excerpt check does not imply whole-paper verification or hardware validation. Consult the [workflow](../03-reviews/WORKFLOW.md) before using a light card in the survey. The 18 historical key papers remain the reading-guide selection.

The 79 historical follow-up rows are preserved in their original order with the same identity, theme, title, status, and source-review fields; only their reasons are translated. Their exact original bytes are stored at `99-archive/superseded/followup-candidates.original.csv`. Follow-up screening deduplicates identities and identifies corpus overlaps separately; a recommendation is not an acquisition or full-text verification record.

On November 2, 2026, the user confirmed a fixed follow-up selection, F01–F15, from that screening queue. All 15 official PDF/raw-BibTeX pairs are now registered. F03/F09/F11 were initially blocked by PDF access; the user manually supplied their official PDFs, and their identities, authors, DOIs, and volume/issue details were checked before registration. No selected paper now lacks a PDF. The selection and IDs did not change when access was resolved. [Follow-up status](followup-status.csv) records acquisition, transcription, and review separately; an approved paper joins the reviewed library only after its source and review are complete. The [assessment](followup-assessment.md) records evidence against the follow-up questions, not a new exhaustive search. The historical 112-paper corpus and its 18 key-paper reading selection remain identifiable as the pre-follow-up baseline.

S24-S26 are user-authorized citation exceptions: their working `citation.bib` is derived, and original exports remain unchanged. S24 uses the evidenced 2026 early-access year; S25 uses the final 2026 issue year while retaining its 2025 online date. S41 preserves the native PMLR citation and documents the title in its linked PDF. [Resolution evidence](survey-200plus-2026-11-03/evidence-notes.md) records the field changes and identity comparison.

S01-S48 now have OXR-1.0 transcriptions produced through self-hosted vLLM 0.25.1 and the OXR D-FINE layout model. All 802 physical PDF pages, per-page JSON and referenced images are archived locally. Separate extraction receipts bind PDF, Markdown and image hashes without changing the original acquisition provenance. The earlier local comparison exports remain private. Extraction does not establish review completion or survey inclusion. See [Markdown coverage](survey-200plus-2026-11-03/markdown-coverage.md).

## Themes

| Theme | Focus |
|---|---|
| T1-perception-localization | Fusion, odometry, degradation, and integrity |
| T2-slam-mapping-exploration | Dynamic/long-term mapping, exploration, and traversability |
| T3-planning-control | Trajectories, MPC, safety constraints, and learned control |
| T4-multi-robot-coordination | Communication, map merging, collaborative localization, and tasks |
| T5-semantic-embodied-navigation | Language, open vocabulary, memory, and social constraints |
| T6-reliability-deployment | Faults, recovery, resources, and long-term autonomy |

Each paper keeps one primary theme from the original classification. The six themes organize reading and are not an exhaustive taxonomy. Historical journal/conference admission criteria, eight excluded extras, user exclusions, and unreviewed records retain their original audit scope in the archive.
