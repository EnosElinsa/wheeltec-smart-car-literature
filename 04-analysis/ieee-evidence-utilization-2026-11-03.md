# Using the supplementary IEEE evidence

Analysis date: November 3, 2026. All 20 sources now have targeted source readings, including the seven manually supplied papers. These are selected-passage assessments, not new full-verification cards. The reviewed index and current manuscript remain at 127 publications.

[20-paper utilization matrix](../06-data/ieee-supplement-2026-11-03/utilization-matrix.csv) · [Page-bound source notes](../06-data/ieee-supplement-2026-11-03/evidence-notes.md) · [Reading ledger](../06-data/ieee-supplement-2026-11-03/source-reading.json) · [Current survey](https://github.com/EnosElinsa/wheeltec-navigation-survey)

## Main value

The strongest contribution is more precise comparison and better-supported limits. Existing recovery integrations, explicit assumptions and negative cases should be incorporated before adding more broad gap statements. The matrix assigns every paper a target subsection, current comparator, supported use, evidence boundary and remaining check. P1 denotes direct value to a central synthesis or evaluation claim; P2 denotes a more specialized extension. These priorities do not rank paper quality.

| Argument to strengthen | Most useful additions | Consequence for the revision |
|---|---|---|
| Localization model and information requirements | N01, N02, N03, N19, N20 | Compare measurement selection, motion priors, terrain observations, contact and dense registration by the information they require and preserve. |
| Information-aware planning and traversability | N05, N07, N08, N12 | Separate graph objectives, terrain heuristics and conditional safety guarantees. N05/N07 belong to a related method family. |
| Implemented recovery and mission continuation | N10, N13, N15, N17, N18 | Identify alarm, response, successful continuation, restart, relaxation and human assistance as distinct outcomes. |
| Semantic/team integration and shared-state faults | N09, N11 | Acknowledge existing integrations; retain actual compute placement, sensor emulation and implementation boundaries. |
| Reproducibility, timing and long-term operation | N04, N06, N14, N16, N20 | Distinguish repeated recordings from missions, optimization updates from end-to-end delay, collected data from online control, and revisits from continuous service. |

## Seven newly read papers: decisive limits

- N02 (pp. 4, 6–8) models departures from SE(2) stochastically and reports possible failure under substantial slope variation. It supports a comparison of model assumptions, not unrestricted rough-terrain robustness.
- N03 (pp. 6–8) requires preserved lug imprints in suitable soil. High slip can destroy the very feature used for estimation; motion-control integration remains future work.
- N04 (pp. 5–8) demonstrates implementation variability under controlled replay. Thirty repeats of a recording assess this variability rather than the frequency of physical mission failures.
- N12 (pp. 2–3, 6–8) provides conditional tube-based safety/timing analysis. Its target separation, input-coupling assumptions and pending explicit input constraints limit transfer to ordinary wheeled platforms. Its mobile-robot hardware and quadrotor simulation must remain distinct.
- N14 (pp. 2, 7–9) assumes low-speed no-slip motion and uses industrial-PC HIL computation. Jetson Nano in the architecture does not establish onboard execution of the entire controller, and sparse updates do not directly measure energy savings.
- N17 (pp. 4–7) implements failure-specific recovery on CENTAURO, while excluding some generated no-plan/slow-plan scenarios and retaining a human-rescue boundary. Its results require the denominator and hybrid motion primitives.
- N20 (pp. 1–2, 5–6) is a dense-estimation comparator with processing time longer than sequence recording duration on the reported desktop. N/A sensor adaptation, run failure and estimation accuracy should be reported separately.

## Revision order

First strengthen Section IX's reproducibility, runtime and denominator discussion using N04, N17 and N20. Then revise Section VIII's detection/response comparison using N10, N13, N15, N17 and N18; this should sharpen the first open question rather than introduce another broad absence claim. Add mechanism comparisons in Sections IV–VII using the remaining rows, retaining N05/N07's relationship and each platform's requirements. Update Section X after those technical comparisons are in place.

Before formal corpus expansion, create consistently scoped review cards and code the new studies using the same vocabulary. Recompute counts, bibliography, tables and supplement together. Current acquisition and selected readings alone do not establish 147 equivalently assessed publications, 20 independent replications or 20 additional hardware validations. No new performance-table values were taken from the seven newly read papers; any later numerical comparison needs a direct PDF table/plot check.
