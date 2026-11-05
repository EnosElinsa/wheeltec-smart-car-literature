# Current revision status - November 5, 2026

The [main survey](survey.pdf) has 24 pages, 270 references, three figures and eight tables, which is the maximum length of IEEE T-IV surveys. The [supplement](supplement.pdf) has 17 pages, 228 references, one figure and 13 tables. All 245 selected publications appear in substantive main-text prose, and every corpus work dates from 2021-2026. Seven of the 25 background references are foundational pre-2021 sources cited for attribution. Evaluation counts cover 244 technical publications and exclude the context review.

The latest revisions are as follows.
- [REVIEW-FIXES-4.md](revision/REVIEW-FIXES-4.md) codes all 245 works with a published codebook and a language-model second coding of 40 sampled works (median kappa 0.81 before adjudication, not human inter-rater reliability). Task outcomes under a named degradation condition in the same experiment now cover 80 of the 244 technical publications (33%), from 1 of 67 localization to 36 of 56 planning studies. Fig. 1 becomes a degradation-source by function matrix, the four interfaces are placed in a pre-registered ranking, and Section I positions the survey against automated-driving standards. The second part adds the reporting checklist (Table VII), applies the minor items B10-B21, names the AI tools in the acknowledgment and reruns the audits.

- [ROADMAP-AUDIT-AND-SURVEYS.md](revision/ROADMAP-AUDIT-AND-SURVEYS.md) adds Table V, a research roadmap for the four open interfaces. It also adds condition-based guidance to the section syntheses, tightens the abstract, and checks the critical characterizations of Sections IV-X against the review cards and transcriptions, which corrected five wordings. Four related surveys join Table I.
- [CONTRIBUTIONS-AUDIT-AND-REVIEW.md](revision/CONTRIBUTIONS-AUDIT-AND-REVIEW.md) states the evidence finding and the roadmap in the contribution list. It adds platform coverage to Table IV, since 36 of the 66 localization and mapping studies do not evaluate on a wheeled robot. It also checks all 22 numerical result sentences against the sources with no mismatch, verifies a clean build from a fresh GitHub clone, and reports a simulated two-reviewer review (both reviewers: major revision).
- [REVIEW-FIXES-1.md](revision/REVIEW-FIXES-1.md) applies the review items that need no author decision. It corrects the descriptions of eight studies, qualifies the 26% figure, recasts the interfaces as a proposed agenda, flags non-wheeled evidence, defines the Table IV rows and the Fig. 3 scoring, and adds an AI-use acknowledgment.
- [REVIEW-FIXES-2.md](revision/REVIEW-FIXES-2.md) cites foundational pre-2021 sources as background references outside the corpus and moves the selection-stage table into Section III with the screening facts.
- [REVIEW-FIXES-3.md](revision/REVIEW-FIXES-3.md) condenses Sections IV-VIII by 21% and adds 16 works from 2021-2024 that the internal review of an earlier draft named as missing, as a separate coverage-additions stage, together with three related surveys. Task outcomes under a named degradation condition now cover 61 of the 244 technical publications (25%), against 59 of 228 (26%) without the additions. The pose-uncertainty and reconnection gap claims are qualified for STEP, Kimera-Multi and LAMP 2.0.

Earlier records cover the [evidence map of Table IV](revision/EVIDENCE-MAP-AND-PROSE.md), the [page limit, synthesis table and grayscale figures](revision/PAGE-LIMIT-AND-FIGURE-STYLE.md), the [SVG figures and condensation](revision/FIGURES-AND-CONDENSATION.md), and the [refresh integration](revision/IEEE-REFRESH-INTEGRATION.md) of R01-R36 with the removal of pre-2021 references.

Assessment remains uneven: 23 full reviews and 222 light reviews in the manuscript selection, comprising 87 historical conversions and 135 targeted readings. The evidence-map coding and the claim audit rest on these cards and on the local transcriptions. Neither is a re-reading of every paper. Seven numerical examples and six displayed equations retain their checked source and baseline records. The source-hash audit covers 741 PDF/BibTeX/Markdown artifacts.

Open before submission:

- The main paper is at the 24-page maximum. The last page balances at 658 and 667 pt with `\IEEEtriggeratref{256}`.
- The review proposed restructuring Sections IV-VIII. This revision condensed them instead. Further works named by the review were not acquired; NeBula exists only as a preprint.
- The author must confirm the acknowledgment wording. [REVIEW-FIXES-4.md](revision/REVIEW-FIXES-4.md) lists its uncertainties and the pre-existing Crossref reference lists of fifteen background records.
- Author information and submission declarations are incomplete.
- This is a working draft with non-exhaustive coverage and no new robot experiments.

[Current revision](revision/REVIEW-FIXES-4.md) · [Evidence guide](revision/README.md) · [Build instructions](README.md)
