# IEEE evidence integration and prose audit — November 3, 2026

Historical 147-work/163-reference stage. The latest 195-work/211-reference revision is recorded in [SURVEY-EXPANSION-INTEGRATION.md](SURVEY-EXPANSION-INTEGRATION.md); the delivery record now describes that later revision. Counts and visual checks below describe this earlier stage.

The revision incorporates N01–N20 into comparative arguments in Sections IV–X. The selection now contains 147 publications (144 technical and three context works), with 16 additional background references. Five representative tables retain 52 rows, refreshed to include the new mechanisms. The acquisition narrative remains outside the scholarly manuscript.

## Findings and disposition

| Priority | Location | Finding | Evidence and correction |
|---|---|---|---|
| High | VIII, IX, X | Detection, protective response and mission continuation require different evidence. | N10 stops/relocalizes but can restart the trial; N17 executes embodiment-specific recovery with a remaining human-rescue boundary; N18 tests prediction and rosbag execution. Prose and table entries preserve these distinctions. |
| High | V, VII, VIII, IX | Formulation, actual implementation and guaranteed event can differ. | N11's hardware monitor is centralized with emulated ranges; N14 uses industrial-PC HIL control; N12 assumes terminal separation and leaves explicit input constraints for future work. The corresponding implementation and transfer conditions are explicit. |
| High | III, supplement, generator | Selection membership and assessment counts were frozen to the earlier corpus. | Membership is checked against the evidence library's inclusion record; technical counts, coding attributes, bibliography and supplement are regenerated together. Historical baseline IDs and hashes remain identifiable. |
| Medium | IV–VII | New sources need mechanism comparisons rather than a list of additional references. | Compare weighting with new sensing, planar priors with terrain perturbations, trace/contact observations with their formation conditions, graph objectives with deployment, and semantic allocation with geometric execution. |
| Medium | VIII–IX | Relaxed missions and retained-scenario rates can obscure the success event. | N15's allowed task changes, N13's assumed maintenance, N17's scenario exclusions and N10's restarted attempts remain attached to their outcomes. |
| Medium | IX | Repeated playback can be mistaken for independent mission replication. | N04 repeats the same input; the text distinguishes implementation variability from physical mission variability and determinism from accuracy. N20 separates N/A sensor adaptation, run failure and processing time. |
| Low | Tables III–VII, bibliography | New labels and longer mechanism descriptions can disrupt layout. | Short readable method names, explicit placement qualifiers, stable column structure and a balanced final bibliography retain the existing format. Rendered pages are checked after compilation. |

No new numerical result-table comparison is added to the main paper. The seven existing within-study comparisons retain their source locators and hashes. Newly cited counts and timing statements come from the inspected textual protocol passages: N04's 30 repeated executions and N20's processing time relative to recording duration. N09's review card retains a previously rendered Table I comparison, but the main paper uses its architecture and experimental scope without introducing those values.

## Claim and vocabulary ledger

| Term or claim | Meaning and evidence boundary |
|---|---|
| Recovery | Identify the trigger, executed action and restored condition; restarting a trial, relaxing a requirement and resuming the original mission are distinct outcomes. |
| Detection / isolation | Healthy-set separation can establish detection without pairwise fault-class separation; N16 leaves tolerant control for future work. |
| Implementation repeatability | Repeated executions on one recording measure implementation variability, not independent mission outcomes. |
| HIL | The coarse evidence vocabulary is qualified explicitly; physical architecture components do not establish that all controller computation is onboard. |
| Distributed monitoring | An algorithmic formulation does not determine the placement actually evaluated. |
| Terrain cost / risk | A direction-dependent quasi-static proxy is distinct from a calibrated traversal-failure probability. |
| Maintained representation | Better matching on recorded revisits does not establish uninterrupted autonomous service or the acquisition cost. |
| Technical publications | 144 selected technical studies/resources; the three context works are excluded from evaluation-attribute counts. |

## Notation and artifact ledger

The artifact boundary includes the abstract, eleven sections, supplement, bibliography, included figures/tables, generators and delivery checks. No highlights, cover letter, graphical abstract or response letter is present. All six displayed equations retain their existing hash baseline; notation and labels are preserved. The main document retains three figures, eight tables and 30 unique labels. The supplement retains one figure, two tables and seven labels. Statistical figures and evaluation counts use the expanded selection, with overlapping attributes identified explicitly.

The 20 new cards are targeted light assessments. Overall depth remains 23 full and 124 light reviews: 89 historical conversions and 35 targeted readings. The actual page scopes and source limitations remain in the companion library. Formatting, excerpt checks and file hashes do not establish scientific validity or uniform whole-paper assessment.

## Verification

Both documents are compiled with:

```text
latexmk -pdf -quiet -interaction=nonstopmode -halt-on-error -file-line-error survey.tex
latexmk -pdf -quiet -interaction=nonstopmode -halt-on-error -file-line-error supplement.tex
```

The current build and source audit are recorded in [delivery-verification.json](delivery-verification.json). The evidence-library checks cover all 147 review cards, public links, path policy and catalog regression tests. The matching acquisition/review identity is merged once; conflicting identity or source hashes remain errors. The source audit checks 441 local PDF/BibTeX/Markdown hashes and preserves the original 127 rows' metadata and source identities.

All pages are rendered for an overview; refreshed comparison tables, the selection table, statistics figure and final bibliography receive enlarged inspection. No clipping, overlap or overfull boxes remain. Minor underfull horizontal notices are assessed visually. The seven numerical cases and six equations are checked independently of page count. [Clean-checkout verification](clean-checkout-verification.json) covers regeneration and compilation from public sibling repositories without publisher full texts. The [lexical screen](overlap-report.json) is a project-local phrase check, not an originality determination.

The retained strengths are comparisons tied to concrete information requirements, explicit separation of implementation and theoretical scope, and within-study evidence with conditions. Wider coverage, author declarations and venue-specific submission preparation remain outside this completed incorporation.
