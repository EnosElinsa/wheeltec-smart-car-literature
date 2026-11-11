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

- `K01`-`K16`: the [review additions](review-additions-2026-11-04/README.md) of November 4, 2026, 16 formally published 2021-2024 works that an internal simulated review of an earlier draft named as missing; the user confirmed the selection. All 16 have official PDF/BibTeX pairs, local PyMuPDF4LLM 0.2.9 transcriptions and targeted light review cards, and all are survey selection members. K11 (HM3D) uses a user-authorized derived citation that replaces only the unparsable key of the official export; see the [identity notes](review-additions-2026-11-04/evidence-notes.md).

All 479 active sources share the same six theme directories and the [unified catalog](library-catalog.csv), with 479 transcribed reading sets. The catalog also retains 171 excluded/background and no pending records; their original files are stored separately from admitted sources. Acquisition manifests preserve provenance; they are not separate paper stores. `paper-index.csv` holds all 247 assessed library sources and coding; `survey-inclusion.json` selects 245 survey members and retains X01/X15 internally, while `library-catalog.csv` is the single registry of 650 distinct works and preserves acquisition, scope and assessment status separately. `tools.build_indexes` regenerates the catalog and theme indexes together; sources without transcriptions appear only in the paper index. `tools.locate` searches all registered sources.

All 20 supplementary pairs are acquired. N02, N03, N04, N12, N14, N17, and N20 were supplied by the user as IEEE Xplore downloads and retain `manual_publisher_download` provenance; the other 13 retain their automatic publisher-export provenance. Each PDF and native BibTeX file is copied without rewriting its bytes. Downloads originals are preserved, and the [manual import receipt](ieee-supplement-2026-11-03/manual-import.md) records the correspondence. All 20 supplementary full texts use local PyMuPDF4LLM extraction, distinct from the original corpus's MinerU transcriptions. All 20 now have targeted source readings with physical-page locators. The subsequent light cards retain those reading limits and do not establish whole-paper verification.

Short names aid navigation. Formal titles and DOIs follow `paper-index.csv` and official sources. `selection_year` and `bibliographic_year` are separate so that online-first and final volume/year differences remain visible. Original publisher BibTeX is preserved without rewriting it to match an assigned volume year. For example, F14's raw export retains `year="2025"` and its online publication date, while the PDF assigns volume 50, article 7 to 2026; the card and index expose that formal/online distinction. F11 likewise has a formal publication year of 2026 and an online publication year of 2025; its raw publisher BibTeX is preserved unchanged. Formal conference papers without a DOI are identified through their official pages and `selection_id`; F07/F08 use PMLR v270, whose publication year is 2025 for CoRL 2024, and K12 uses PMLR v205, whose publication year is 2023 for CoRL 2022. Derived citations are explicit, user-authorized exceptions: S24-S26 and K11 retain their original export beside the derived `citation.bib`, and their provenance records each change.

The reviewed library contains 247 papers: **23 full assessments and 224 light cards**, comprising 89 historical conversions and 135 targeted readings. The current survey selection has 245 works, excluding X01/X15; its 222 light cards comprise 87 historical conversions and 135 targeted readings. Every corpus work cited by the manuscript dates from 2021-2026. The manuscript also cites seven foundational pre-2021 sources as background references outside the corpus, listed in its [citation scope](../05-survey/manuscript/data/citation-scope.json), while the pre-2021 library papers X01 and X15 remain internal references. The November 2 selection of 127 remains identifiable through its commit and source-index hashes in [survey-inclusion.json](survey-inclusion.json). The F01–F15 transcriptions use MinerU precision; N01–N20 and K01–K16 use the explicitly recorded local PyMuPDF4LLM extraction. Full assessment covers whole-paper reading and rendered-table checks; light assessment covers the scope recorded on each card. A passing format/excerpt check does not imply whole-paper verification or hardware validation. Consult the [workflow](../03-reviews/WORKFLOW.md) before using a light card in the survey. The 18 historical key papers remain the reading-guide selection.

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

## Flagship-only acquisition expansion

H01-H60 reserve the sixty fixed selections of the [flagship expansion](flagship-expansion-2026-11-10/README.md). At the historical first delivery, 46 official publisher PDF/native-BibTeX pairs were registered; 14 acquisitions remained unresolved with their IDs retained in the batch register. RA-L is excluded from this expansion at the user's request. At that stage these sources had no transcriptions, review cards, coding or survey membership; the later completion and extraction stage is recorded below. Public registration contains source hashes and official URLs; raw acquisition state stays private.

## Consolidated additions and venue admission

The SC-series IDs retain their original local source identity. MS01-MS06 are user-requested supplemental surveys. The 110 verified official SC additions and six surveys are filed by primary task in T1-T6; filing does not create a review card, evidence coding or survey membership. Their PDFs, native citations, transcriptions and extraction assets retain their bytes. Excluded or pending source files remain under `99-archive/local/background-and-pending/` and their catalog status remains visible. The local reading view and `tools.locate` use the same catalog; `tools.build_indexes` preserves these records when rebuilding indexes.

The recovered journal whitelist has 17 venues. The following publisher/ISSN identity table preserves the historical registry checks dated September 17, 2026; it is an admission list, not a permanent journal-ranking claim.

| Journal | Abbreviation | ISSN | Publisher |
|---|---|---|---|
| The International Journal of Robotics Research | IJRR | 0278-3649; 1741-3176 | SAGE Publications |
| IEEE Transactions on Robotics | T-RO | 1552-3098; 1941-0468; 1546-1904 | IEEE |
| IEEE Robotics and Automation Letters | RA-L | 2377-3766 | IEEE |
| Journal of Field Robotics | JFR | 1556-4959; 1556-4967 | Wiley |
| Robotics and Autonomous Systems | RAS | 0921-8890 | Elsevier |
| Autonomous Robots | AURO | 0929-5593; 1573-7527 | Springer |
| Science Robotics | SciRob | 2470-9476 | AAAS |
| IEEE Transactions on Automation Science and Engineering | T-ASE | 1545-5955; 1558-3783 | IEEE |
| Automatica | Automatica | 0005-1098 | Elsevier |
| IEEE Transactions on Automatic Control | T-AC | 0018-9286; 1558-2523; 2334-3303 | IEEE |
| IEEE Transactions on Cybernetics | T-CYB | 2168-2267; 2168-2275 | IEEE |
| Control Engineering Practice | CEP | 0967-0661 | Elsevier |
| Information Fusion | InfFus | 1566-2535 | Elsevier |
| Pattern Recognition | PR | 0031-3203 | Elsevier |
| IEEE Transactions on Image Processing | T-IP | 1057-7149; 1941-0042 | IEEE |
| IEEE Transactions on Intelligent Transportation Systems | T-ITS | 1524-9050; 1558-0016 | IEEE |
| IEEE Transactions on Intelligent Vehicles | T-IV | 2379-8858; 2379-8904 | IEEE |

The conference supplement admits ICRA, IROS, RSS and CoRL. Venue identity is necessary but not sufficient: the title and abstract must establish a relevant mobile-robot task. Road-driving, generic control or visual methods require direct wheeled-robot transfer evidence or an explicit counterexample purpose. An absent abstract remains pending.

Prefer official publisher PDFs and raw publisher BibTeX exports to preprints. A formal citation alone does not establish the PDF version. Registry metadata is discovery evidence, not a native citation or verified publisher artifact. The 116 active additions use verified official pairs; the formal SC-M062 pair is retained as method background. MS01 (TNNLS), MS04 (TIM) and MS06 (TSMC: Systems) are explicit background exceptions outside the whitelist; MS02/MS03 concern road-driving planning; MS05 is an object-goal survey in T-ASE. All six retain supplemental status and a scope reason in the catalog. They do not expand the original main-library admission rule.

Frozen selections and raw extraction receipts remain unchanged in the private `06-data/provenance/` evidence folder. Historical input paths inside those records are original run bindings; the current catalog and extraction index resolve current locations. OCR language data lives under `.local/ocr/tessdata/`; `tmp/` contains only regenerable work. Source-drive hashes are historical when the external drive is unavailable.

The manual completion of November 9 resolved the three former pending records using publisher abstracts and targeted source passages. SC-M028 (RAS, frontier exploration with real-robot experiments) and SC-M126 (RAS, navigation-oriented shared control review) enter the main library with source-only status. SC-M062 has its final IEEE issue PDF, native citation and 16-page OXR transcription, but its grid-world LTL/MDP evaluations remain method background without established wheeled-robot transfer. The current library has 363 active reading sets and one additional formal background reading set. None of these actions creates review cards or expands the 245-work survey selection. Duplicate S25/S26 PDFs and native RIS exports, the SC-M101 citation, and the S24 original export are unchanged; S24's new PDF differs only in the institutional download-date watermark. The four documented derived working citations remain explicit exceptions.

## November 11 source completion and journal expansion

[This stage](journal-completion-2026-11-11/README.md) registers 13 supplied H-series papers (8 native pairs and 5 explicitly authorized Crossref citations), 20 additional J-series journal pairs, and OXR transcriptions for 59 H-series and 20 J-series sources. J01-J30 reserve the reviewed journal list, including unresolved acquisitions. RA-L is excluded. Historical batch counts remain dated evidence. All new sources remain outside the assessed corpus and survey selection.

## Current acquisition rule (November 11, 2026)

The owner now requires **at least JCR Q1** for new journal downloads. Record the JCR edition/year, subject category, identity and verifiable source before selecting a new journal paper. Hold unverified rankings; do not substitute CAS divisions, SJR/CiteScore or journal reputation. RA-L, Autonomous Robots and Journal of Field Robotics are excluded from new acquisition. Earlier admission lists and batch snapshots are historical and do not override this rule. Existing sources remain available. Conferences have a separate admission policy. See [the policy](acquisition-policy.json) and [current work](current-work.md).

[Two Annual Reviews supplied by the owner](annual-review-completion-2026-11-11/README.md) completed J01/J02 with 49 OXR pages; the original journal batch retains its frozen selection and historical delivery totals.

## DRL navigation implementations

D01-D11 are the [eleven conference additions](drl-open-source-2026-11-11/README.md) with verified official PDF/native-BibTeX pairs, OXR transcriptions and public author implementations. They add no review cards, coding or survey selections. New journal candidates remain subject to the JCR Q1 policy above.

## Six-theme conference addition

V01-V24 are the [24 ICRA/IROS 2025 additions](coverage-expansion-2026-11-11/README.md), with official native pairs and OXR transcriptions. Journal nominations remain unselected pending JCR edition/category Q1 evidence. The 247 assessments and 245 survey selections are unchanged.
