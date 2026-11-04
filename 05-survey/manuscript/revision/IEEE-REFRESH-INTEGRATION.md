# IEEE refresh integration and survey review - November 3, 2026

The manuscript now selects **229 works** (228 technical and one context review) and cites **5 background references**, for **234 references, all from 2021-2026**. All 36 refresh papers (R01-R36) appear in substantive prose. The main paper compiles to 36 pages and the supplement to three.

## Content changes

- Localization adds radar uncertainty weighting and self-supervised radar odometry, range-aided multi-vehicle correction, ground-factor and wheel-inertial priors, cross-modal camera-LiDAR and open-vocabulary localization, closed-loop LiDAR-teach/radar-repeat navigation, prior-map change detection, multi-session radar maps, illumination-robust visual SLAM and evidential semantic maps.
- Planning adds terrain-adaptive constraint MPC and implicit traversability fields with their hardware failure causes, stochastic occupancy prediction, a heterogeneous crowd-interaction policy and a learned clearance-risk MPC.
- Semantic navigation adds moved-object search, game-theoretic target disambiguation, generate-and-select outdoor navigation, embodiment affordance re-ranking, language-derived costmap layers and distilled social reasoning.
- Coordination adds regional exploration abstractions, iMESA-to-riMESA progression, asynchronous ADMM pose graphs, layered bandwidth allocation, co-optimized rendezvous, entropy-field rendezvous and compensation-based team MPC.
- Reliability adds simulation-based failure prediction and repair, active view planning, failure-aware team search, joint mechanical/computing energy control, recharging-constrained monitoring and cloud-edge deployment.
- Evaluation and open challenges use these papers for sim-to-real gaps, communication-model assumptions, small trial counts, failure censoring, low-rate high-level inference and embodiment transfer.

## Citation policy

The five pre-2021 foundational references (Campion 1996, DWA 1997, TEB 2013, CBF 2017, Nav2 2020) are excluded from the bibliography on the user's instruction and retained in `revision/background-sources/`. The background now introduces DWA, TEB and CBF through recent studies that use them. [citation-scope.json](../data/citation-scope.json) records each exclusion; the five-exception requirement in the selection text and supplement was removed.

## Style revision

Sections I-XI were revised to remove semicolons, `, but` clause joins, `so`, `because` and first-person contributions from running prose, and figure captions no longer join clauses with semicolons. Measured on the flattened body, the mean sentence length moved from 17.7 to 17.0 words and the share under 12 words from 18% to 23%, still outside the team band (21.4-23.8 words; 9%-14%). A merge pass remains open.

## Open issues

Follow-up, November 4, 2026: [FIGURES-AND-CONDENSATION.md](FIGURES-AND-CONDENSATION.md) reduces the main paper to 26 pages and brings the rhythm into the team band, and [PAGE-LIMIT-AND-FIGURE-STYLE.md](PAGE-LIMIT-AND-FIGURE-STYLE.md) brings it to 23 pages, within the T-IV maximum. The items below describe the state on November 3.

- Length: IEEE T-IV surveys may run 18 pages plus at most 6 paid pages. The current 36 pages need a length decision before submission.
- Rhythm: see above.
- Depth: the 36 new cards are targeted light readings; numbers reported from them were located in the PDF text, without rendered-table audits.

## Verification

Both PDFs compile with `latexmk`. [delivery-verification.json](delivery-verification.json) records 234 resolved references, 229 corpus prose citations, 693 matching source artifacts, 30 main labels, seven supplement labels, six unchanged equations, seven retained numerical cases, no overfull boxes and no LaTeX warnings. The main log has 13 underfull horizontal boxes and the supplement one. No human final review or clean public-clone build is claimed.
