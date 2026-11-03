# Search coverage and boundaries

This records the historical discovery and screening scope, preserved during the November 2, 2026 English maintenance. The old archive was screened first, followed by 2025–2026 corpus discovery across 17 journals. Each of the six themes used four search rounds: terminology, scenarios/mechanisms, citations, and counterevidence. Keywords only nominated candidates; acceptance reasons were recorded separately through title/abstract judgments.

The initial 34 journal/year slices had statuses `{'complete': 27, 'failed': 6, 'partial': 1}`. An independent bounded retry returned the seven remaining slices, giving a merged historical status of `{'complete': 34}`. Here, `complete` means that the provider's enumeration cursor was exhausted in that run; it does not establish that the publisher's entire catalog was retrieved without omissions.

| Journal | Year | Merged status | Records | Run |
|---|---:|---|---:|---|
| Automatica | 2025 | complete | 577 | journals-2025-2026 |
| Automatica | 2026 | complete | 637 | journals-2025-2026 |
| Autonomous Robots | 2025 | complete | 48 | journals-2025-2026 |
| Autonomous Robots | 2026 | complete | 37 | journals-2025-2026 |
| Control Engineering Practice | 2025 | complete | 412 | journals-2025-2026 |
| Control Engineering Practice | 2026 | complete | 527 | journals-2025-2026 |
| IEEE Robotics and Automation Letters | 2025 | complete | 1727 | journals-2025-2026 |
| IEEE Robotics and Automation Letters | 2026 | complete | 1931 | journals-2025-2026 |
| IEEE Transactions on Automatic Control | 2025 | complete | 773 | journal-coverage-retry |
| IEEE Transactions on Automatic Control | 2026 | complete | 910 | journals-2025-2026 |
| IEEE Transactions on Automation Science and Engineering | 2025 | complete | 1893 | journal-coverage-retry |
| IEEE Transactions on Automation Science and Engineering | 2026 | complete | 1379 | journals-2025-2026 |
| IEEE Transactions on Cybernetics | 2025 | complete | 546 | journals-2025-2026 |
| IEEE Transactions on Cybernetics | 2026 | complete | 672 | journals-2025-2026 |
| IEEE Transactions on Image Processing | 2025 | complete | 624 | journal-coverage-retry |
| IEEE Transactions on Image Processing | 2026 | complete | 798 | journal-coverage-retry |
| IEEE Transactions on Intelligent Transportation Systems | 2025 | complete | 1717 | journals-2025-2026 |
| IEEE Transactions on Intelligent Transportation Systems | 2026 | complete | 1183 | journal-coverage-retry |
| IEEE Transactions on Intelligent Vehicles | 2025 | complete | 481 | journal-coverage-retry |
| IEEE Transactions on Intelligent Vehicles | 2026 | complete | 145 | journal-coverage-retry |
| IEEE Transactions on Robotics | 2025 | complete | 372 | journals-2025-2026 |
| IEEE Transactions on Robotics | 2026 | complete | 246 | journals-2025-2026 |
| Information Fusion | 2025 | complete | 730 | journals-2025-2026 |
| Information Fusion | 2026 | complete | 1024 | journals-2025-2026 |
| Journal of Field Robotics | 2025 | complete | 277 | journals-2025-2026 |
| Journal of Field Robotics | 2026 | complete | 230 | journals-2025-2026 |
| Pattern Recognition | 2025 | complete | 900 | journals-2025-2026 |
| Pattern Recognition | 2026 | complete | 2641 | journals-2025-2026 |
| Robotics and Autonomous Systems | 2025 | complete | 277 | journals-2025-2026 |
| Robotics and Autonomous Systems | 2026 | complete | 485 | journals-2025-2026 |
| Science Robotics | 2025 | complete | 132 | journals-2025-2026 |
| Science Robotics | 2026 | complete | 96 | journals-2025-2026 |
| The International Journal of Robotics Research | 2025 | complete | 124 | journals-2025-2026 |
| The International Journal of Robotics Research | 2026 | complete | 96 | journals-2025-2026 |

The initial 21,400 records were merged cross-source candidates, including years outside the broad search scope, rather than 21,400 relevant papers. Of these, 10,692 awaited semantic review, 8,532 awaited metadata, and 2,176 failed hard eligibility criteria. Among 43 newly discovered records in targeted supplementary screening, 36 had abstracts and seven awaited them; 33 entered the follow-up full-text queue without joining the frozen 60-paper expansion corpus. The detailed historical audit is in the local archive `99-archive/history-2026-10-25.zip`.

Conference coverage: CoRL was checked against the formal PMLR volume indexes, v270 (CoRL 2024, published in 2025) and v305 (CoRL 2025). RSS was checked against its 2024/2025/2026 formal indexes and selected paper pages. For ICRA/IROS, selected DOIs, main-conference venues, and official publisher records were checked individually; all main-conference papers in each year were not enumerated. Complete enumeration of a formal CoRL 2026 volume was not established. These scopes were not recorded as exhaustive conference coverage.

| Theme | Four-round search and coverage record inside the archive |
|---|---|
| T1 perception, fusion, and localization | `expansions/2026-10-24/reviews/T1/discovery-review-report.md` |
| T2 SLAM, mapping, and exploration | `expansions/2026-10-24/reviews/T2/discovery-review-report.md` |
| T3 planning and control | `expansions/2026-10-24/discovery/T3/search-coverage-report.md` |
| T4 multi-robot coordination | `expansions/2026-10-24/reviews/T4/coverage-and-gaps.md` |
| T5 semantic and embodied navigation | `expansions/2026-10-24/reviews/T5/coverage-and-gaps.md` |
| T6 reliability and deployment | `expansions/2026-10-24/discovery/T6/search-coverage-report.md` |

Provider failures/rate limits, missing abstracts, and omissions from formal catalogs remain in the original diagnostics. Merging and supplementary searches did not rewrite the old frozen discovery results. Gaps in the follow-up queue indicate only what this library has not covered.

The 79-row historical candidate table can contain duplicate identities and overlaps with the original 112-paper corpus. English translation and title/abstract screening alone do not establish acquisition or full-text verification. The fixed F01–F15 follow-up selection was confirmed on November 2, 2026; [its status ledger](followup-status.csv) distinguishes an approved lead from an acquired, transcribed, and reviewed paper. These additions do not retroactively change the historical search coverage or the 18 key papers selected from the original corpus. The original 112 cards comprised 23 full-verification and 89 light-conversion cards; that distinction supersedes any implication that historical screening was a uniform deep verification of all papers.

All 15 selected papers now have registered official PDF/raw-BibTeX pairs. F03/F09/F11 were initially blocked by PDF access; the user manually supplied their official PDFs, whose identities, authors, DOIs, and volume/issue details were checked before registration. No selected paper lacks a PDF. At completion of F01–F15, the reviewed library contained **127 papers**, with a review-card total of **23 full + 104 light** (89 historical conversions + 15 targeted readings). All 15 additions have MinerU precision transcriptions and targeted light cards; all 127 cards passed `review_check --pdf`. The [follow-up assessment](followup-assessment.md) uses selected passages to evaluate four corpus-scoped questions; the earlier access limits were acquisition limits, not evidence that a mechanism was absent. Passing source/format checks does not imply uniform whole-paper verification. The follow-up did not repeat the 17-journal enumeration, exhaust the 79-row queue, or establish a new field-wide research gap.

## Historical member paths

The local archive is `99-archive/history-2026-10-25.zip`. Extract it into a separate directory and use these original member paths:

- `expansions/2026-10-24/discovery/T3/search-coverage-report.md`
- `expansions/2026-10-24/discovery/T6/search-coverage-report.md`
- `expansions/2026-10-24/discovery/new-corpus-coverage-audit.md`
- `expansions/2026-10-24/reviews/T1/discovery-review-report.md`
- `expansions/2026-10-24/reviews/T2/discovery-review-report.md`
- `expansions/2026-10-24/reviews/T4/coverage-and-gaps.md`
- `expansions/2026-10-24/reviews/T5/coverage-and-gaps.md`

The subsequent N01–N20 assessment brings the current selection to 147 publications (23 full and 124 light cards). The [selection record](survey-inclusion.json) preserves the historical baseline and current membership.
