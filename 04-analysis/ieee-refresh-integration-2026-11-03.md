# Integration of the 36-paper IEEE refresh

> **Stage record, November 3, 2026.** Its counts and statuses describe that date and are not updated. Current totals are in the [repository README](../README.md).

The working survey now cites **229 selected works** (228 technical studies and one context review) and **5 background references**, for **234 resolved references**. Every cited work dates from 2021-2026. All R01-R36 received targeted light cards and appear in substantive section prose. The main paper compiled to 36 pages and the supplement to three at the time of this record.

Follow-up, November 4, 2026: the [figures and condensation revision](../05-survey/manuscript/revision/FIGURES-AND-CONDENSATION.md) reduced the main paper to 26 pages with all 229 works still cited, brought the sentence rhythm into the team band (mean 23.0 words, 13% under 12 words) and moved the manuscript into this repository. The [page-limit revision](../05-survey/manuscript/revision/PAGE-LIMIT-AND-FIGURE-STYLE.md) then moved the five module tables to the supplement and reduced the main paper to 23 pages, within the 24-page T-IV maximum. The [evidence-map revision](../05-survey/manuscript/revision/EVIDENCE-MAP-AND-PROSE.md) added a function-by-attribute evidence map and brought it to 24 pages, and the [roadmap and audit revision](../05-survey/manuscript/revision/ROADMAP-AUDIT-AND-SURVEYS.md) added four related surveys (238 references) and checked the critical characterizations against the sources.

## Survey review findings and responses

| Finding | Response in this revision | Remaining decision |
|---|---|---|
| Five pre-2021 foundational references (1996-2020) remained in the bibliography. | Moved to the internal library on the user's instruction. DWA, TEB and CBF are now introduced through recent studies that apply them. | A reviewer may still expect the original DWA/TEB/CBF citations; restoring them is a one-line policy change in `data/citation-scope.json`. |
| The main paper exceeds the venue length. IEEE T-IV allows 18 survey pages plus at most 6 paid pages ([author information](https://ieee-itss.org/pub/t-iv/author/)). | Not resolved: the draft grew from 33 to 36 pages. | Choose a target venue and length, then cut sections or move per-paper detail to the supplement. |
| Running prose broke the team style: 86 semicolons, 30 `, but` clauses, 7 `so`, 2 `because` and first-person contributions. | Rewritten in Sections I-XI; no semicolon, `but`, `so`, `because`, `e.g.` or `we` remains in running prose. | None for banned constructions. |
| Sentence rhythm is over-split: mean 17.7 words and 18% of sentences under 12 words before this revision (team band 21.4-23.8 words and 9%-14%). | Banned clause joins were split and runs of three short sentences merged; the body now measures 17.0 words and 23%. | A dedicated merge pass, ideally combined with the length reduction, is needed to reach the band. |
| Many paragraphs read as annotated paper lists with one limitation sentence per paper. | New papers are placed inside existing comparisons rather than as new paragraphs where possible. | Consolidating per-paper caveats into comparative sentences would also save pages. |
| Methodology and supplement still described five foundational exceptions. | Updated, with the new selection stage added to the supplement table. | None. |
| riMESA (R23) directly extends iMESA (E40). | Both kept as separate methods; the prose and both cards state the relation. | None. |

Numbers that the survey reports from new light cards were located on their PDF pages: R05, R07, R11, R13, R14, R19, R24, R25, R26, R27, R32, R33 and R36. Earlier numerical cases (E01, E13, E25, E50, M37, N04, N20, F09) were spot-checked against their PDF text and matched.

## Assessment and provenance

Each card records the physical pages read: identity, abstract, method, setup, evaluation and limitation passages. Retained excerpts match both the OXR Markdown and the PDF text layer; table values were not re-read from rendered pages. This is not whole-paper verification. The library now holds 23 full and 208 light cards (89 legacy conversions and 119 targeted readings).

[Reading ledger](../06-data/ieee-refresh-2026-11-03/source-reading.json) · [Selection and acquisition](../06-data/ieee-refresh-2026-11-03/README.md) · [Citation scope](../06-data/survey-inclusion.json) · [Manuscript guide](../05-survey/README.md)

## Paper-to-argument map

| ID | Pages inspected | Section | Survey use and card |
|---|---|---|---|
| R01 | 1, 2, 5, 6, 7, 8 | IV | [Radar weighting that combines pose and measurement uncertainty is a measurement-selection response to sparse returns, evaluated on public datasets.](../03-reviews/T1-perception-localization/2026-Radar-Uncertainty-R01/review.md) |
| R02 | 1, 2, 3, 6, 7, 8, 10, 11, 13 | IV | [Directional range correction after explicit degeneracy detection is evaluated on a wheeled multi-vehicle team.](../03-reviews/T1-perception-localization/2026-RaLI-Multi-R02/review.md) |
| R03 | 1, 2, 7, 8, 10, 11 | IV | [A ground-geometry prior reduces vertical drift with sparse-channel LiDAR on recorded ground-robot data.](../03-reviews/T1-perception-localization/2025-Ground-Constrained-SLAM-R03/review.md) |
| R04 | 1, 2, 4, 9, 10, 11, 12 | IV | [A learned wheel-inertial fallback with a ground prior improves interoceptive odometry on public data.](../03-reviews/T1-perception-localization/2025-WING-R04/review.md) |
| R05 | 1, 10, 13, 16, 17 | IV | [Learned point-line features with map reuse address illumination change at embedded rates.](../03-reviews/T1-perception-localization/2025-AirSLAM-R05/review.md) |
| R06 | 1, 2, 7, 8, 10, 15, 17 | IV | [Cross-modal camera-to-LiDAR-map matching transfers across sensor setups without retraining.](../03-reviews/T1-perception-localization/2025-CMRNext-R06/review.md) |
| R07 | 1, 2, 5, 6, 7, 8 | IV | [Learned change detection can maintain a prior LiDAR map under construction-site change.](../03-reviews/T2-slam-mapping-exploration/2026-Chamelion-R07/review.md) |
| R08 | 1, 2, 3, 5, 6, 7, 8 | IV | [Semantic map uncertainty can be modeled jointly with geometry for outdoor robots.](../03-reviews/T2-slam-mapping-exploration/2026-E2-BKI-R08/review.md) |
| R09 | 1, 2, 3, 5, 6, 7 | IV | [Radar maps can be aligned across sessions and maintained for long-term localization on public vehicle data.](../03-reviews/T2-slam-mapping-exploration/2026-Radar-Long-Term-R09/review.md) |
| R10 | 1, 2, 4, 5, 6, 7 | IV | [Open-vocabulary features can serve as a cross-modal localization likelihood.](../03-reviews/T2-slam-mapping-exploration/2026-OMCL-R10/review.md) |
| R11 | 1, 2, 12, 14, 15, 16, 17, 18, 19 | IV | [Cross-modal teach-and-repeat with label-free adaptation sustains closed-loop wheeled navigation over months under sensing degradation.](../03-reviews/T2-slam-mapping-exploration/2026-LiDAR-Teach-Radar-Repeat-R11/review.md) |
| R12 | 1, 2, 9, 10, 13, 16, 19 | IV | [Radar-centric self-supervised odometry and map completion extend adverse-condition sensing.](../03-reviews/T2-slam-mapping-exploration/2026-Super4DR-R12/review.md) |
| R13 | 1, 2, 4, 6, 7, 8 | V | [Terrain-conditioned stability bounds in MPC are executed on a wheeled robot with reported sim-to-real degradation.](../03-reviews/T3-planning-control/2026-Terrain-Adaptive-MPC-R13/review.md) |
| R14 | 1, 3, 5, 6, 7, 8 | V | [A learned clearance distribution can be used directly as a risk constraint on a wheeled robot.](../03-reviews/T3-planning-control/2026-MonoMPC-R14/review.md) |
| R15 | 1, 2, 4, 6, 7 | V | [Continuous traversability gradients can jointly optimize route and speed in executed off-road navigation.](../03-reviews/T3-planning-control/2026-TRAIL-R15/review.md) |
| R16 | 1, 4, 5, 9, 12, 13, 15, 18 | V | [A graph policy that distinguishes humans from static constraints transfers to wheeled hardware in everyday scenes.](../03-reviews/T3-planning-control/2026-HEIGHT-R16/review.md) |
| R17 | 1, 2, 8, 10, 11 | VII | [Online model-discrepancy compensation can be combined with barrier constraints in team MPC.](../03-reviews/T3-planning-control/2025-Compensation-MPC-R17/review.md) |
| R18 | 1, 4, 6, 9, 12, 15, 17 | V | [Predicted occupancy uncertainty can be inserted into existing costmap planners at embedded rates.](../03-reviews/T3-planning-control/2025-SCOPE-R18/review.md) |
| R19 | 1, 2, 3, 6, 8 | VII | [Reconnection can be planned jointly with task allocation rather than imposed as a fixed schedule.](../03-reviews/T4-multi-robot-coordination/2026-CoCoPlan-R19/review.md) |
| R20 | 1, 2, 4, 6, 7, 8 | VII | [Asynchronous distributed optimization tolerates modeled packet loss and latency in collaborative LiDAR SLAM.](../03-reviews/T4-multi-robot-coordination/2026-Multi-Proxy-R20/review.md) |
| R21 | 1, 2, 5, 6, 8 | VII | [Prioritized layered transmission can preserve useful map content under bandwidth limits in replay.](../03-reviews/T4-multi-robot-coordination/2026-Hierarchical-Transmission-R21/review.md) |
| R22 | 1, 2, 4, 11, 14, 15, 18 | VII | [Compact regional abstractions with a deterministic merge rule support decentralized exploration on hardware.](../03-reviews/T4-multi-robot-coordination/2026-URGE-R22/review.md) |
| R23 | 1, 2, 3, 9, 11, 16, 18 | VII | [Consensus ADMM provides an outlier-robust, asynchronous C-SLAM back end under modeled communication failures.](../03-reviews/T4-multi-robot-coordination/2026-riMESA-R23/review.md) |
| R24 | 1, 2, 3, 7, 13, 14, 15 | VII | [Exploration objectives can induce rendezvous for map merging on wheeled hardware.](../03-reviews/T4-multi-robot-coordination/2025-MEF-Explore-R24/review.md) |
| R25 | 1, 2, 4, 5, 6, 8 | VI | [Semantic selection over geometrically filtered candidates is executed on a wheeled robot outdoors.](../03-reviews/T5-semantic-embodied-navigation/2026-Sem-NaVAE-R25/review.md) |
| R26 | 1, 3, 4, 5, 6, 8 | VI | [An embodiment-specific feasibility filter can reject infeasible semantic plans on a wheeled robot.](../03-reviews/T5-semantic-embodied-navigation/2026-VAMOS-R26/review.md) |
| R27 | 1, 3, 4, 5, 6, 7, 8 | VI | [Semantic search that expects moved objects outperforms static dense maps in the tested building.](../03-reviews/T5-semantic-embodied-navigation/2026-osmAG-LLM-R27/review.md) |
| R28 | 1, 2, 9, 11, 13 | VI | [Game-theoretic VLM disambiguation improves simulated language-goal navigation.](../03-reviews/T5-semantic-embodied-navigation/2026-VLN-Game-R28/review.md) |
| R29 | 1, 2, 4, 5, 6 | VI | [Distilling VLM social reasoning into lightweight encoders addresses query latency on a wheeled robot.](../03-reviews/T5-semantic-embodied-navigation/2025-OLiVia-Nav-R29/review.md) |
| R30 | 1, 2, 5, 6, 7, 8 | VI | [Language constraints can enter standard costmaps as directional and speed layers.](../03-reviews/T5-semantic-embodied-navigation/2026-NORM-Nav-R30/review.md) |
| R31 | 1, 2, 9, 10, 11, 15, 17, 19 | VIII | [Cloud-edge partitioning can keep tracking and local avoidance onboard while offloading mapping and planning.](../03-reviews/T6-reliability-deployment/2026-Cloud-Edge-System-R31/review.md) |
| R32 | 1, 2, 3, 4, 5, 7, 11, 12 | VIII | [Speed and processor settings jointly determine energy use on a wheeled robot running vision workloads.](../03-reviews/T6-reliability-deployment/2025-Mechanical-Compute-Energy-R32/review.md) |
| R33 | 1, 2, 4, 5, 13, 14, 15 | VIII | [Learning view-planning actions from human demonstrations reduces predictable visual tracking failures in simulation.](../03-reviews/T6-reliability-deployment/2025-Help-Me-Through-R33/review.md) |
| R34 | 1, 3, 4, 12, 15, 16 | VIII | [Recharging constraints can be built into multirobot persistent-monitoring routes with approximation guarantees.](../03-reviews/T6-reliability-deployment/2025-Recharge-Monitoring-R34/review.md) |
| R35 | 1, 2, 5, 10, 13, 15 | VIII | [Team policies can be trained to remain effective when members fail without notification.](../03-reviews/T6-reliability-deployment/2025-R-FAC-R35/review.md) |
| R36 | 1, 2, 3, 7, 8, 11, 12, 13 | VIII | [Simulation-based failure prediction can repair controllers before deployment.](../03-reviews/T6-reliability-deployment/2025-RADIUM-R36/review.md) |
