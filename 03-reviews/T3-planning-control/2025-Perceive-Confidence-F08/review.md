# Perceive With Confidence: Statistical Safety Assurances for Navigation with Learning-Based Perception

## Metadata

| Field | Value |
|---|---|
| ID | F08 |
| Title | Perceive With Confidence: Statistical Safety Assurances for Navigation with Learning-Based Perception |
| Authors | Anushri Dixit, Zhiting Mei, Meghan Booker, Mariko Storey-Matsutani, Allen Z. Ren, and Anirudha Majumdar |
| Venue | Proceedings of The 8th Conference on Robot Learning, Proceedings of Machine Learning Research, vol. 270, pp. 2517-2541 |
| Year | 2025 (conference 2024) |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v270/dixit25a.html |
| Theme folder | T3-planning-control |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T3-planning-control/2025-Perceive-Confidence-F08/paper.pdf` and `02-fulltext/T3-planning-control/2025-Perceive-Confidence-F08/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2025-Perceive-Confidence-F08/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: fault-recovery-deployment
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: speed-capped, scripted-scenario
- platform_class: legged
- platform: Unitree Go1 quadruped
- boundary_platform: yes
- degradation: model-error
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: ZED 2i RGB-D point clouds and vision-inertial odometry
- compute: onboard ZED Box, 8-core ARM and 16 GB Orin NX; filter-only runtime 0.00025 s
- compute_location: onboard
- summary_result: PwC was safe in 90% of hardware trials across 30 static chair environments; CP-avg collided in half its trials.
- summary_limitation: The assurance assumes static obstacles and same-distribution environment sampling, with known state and a downstream safe planner.
- survey_included: yes
- verification_level: light

## Problem

A pretrained occupancy model can misdetect objects in new environments. Even calibrating average perception error can fail when the planner changes which states the robot visits. PwC seeks a statistical safety assurance for the combined perception/planning pipeline under those state-distribution changes (pp. 1, 4-5).

## Mechanism

For each calibration environment, PwC computes the bounding-box inflation needed to cover true obstacles over a finite discrete state set, then calibrates an environment-level quantile. The assurance is independent of the downstream policy's visited-state distribution. Online, a non-deterministic filter intersects occupied-space estimates and unions free space. A safe planner uses the resulting map and robot dynamics; experiments use an inevitable-collision-set (ICS) constraint to reject unsafe actions (pp. 4-5).

## Baselines and controls

3DETR perception directly; fine-tuned 3DETR; CP-avg, which calibrates error averaged across environments/states without accounting for closed-loop state shifts; and PwC/PwC-fine-tuned variants. Hardware compares PwC with CP-avg using the simulation-calibrated perception system and the safe-planning pipeline (pp. 5-7). Full parameter parity and every ablation were not audited.

## Platform and setup

PyBullet simulation uses chair scenes and a Go1 dynamical model. Hardware uses a Unitree Go1 quadruped in an 8 × 8 m room with previously unseen static chair layouts: 30 environments and 60 trials total across the two methods. Depth observations reduce the perception sim-to-real gap. The robot executes bounded Cartesian velocity commands; it is not a wheeled platform (pp. 5-7, 17-18).

## Evidence type and transfer

Closed-loop physical navigation and simulated collision/misdetection experiments connect calibrated learned perception to an explicit safe planner. This legged platform is included as boundary evidence for a mechanism that may transfer to wheeled robots after dynamics, pose, sensing, and safety-filter validation. For G2, it supplies a conditional perception-to-collision-constraint interface; no language reasoning or cloud-query policy is implemented.

## Sensors

ZED 2i RGB-D provides point clouds to 3DETR and vision-inertial odometry for pose. The stated field of view is 70 degrees and visibility range [1,5] m. The theoretical safe-planner premise assumes known state, so the practical odometry source must not be read as a proof covering arbitrary pose uncertainty (pp. 5, 18).

## Compute and latency

Fully onboard ZED Box with an 8-core ARM CPU and 16 GB Orin NX GPU. Cartesian velocity commands are capped at 0.8 m/s and sent to the Go1 processor over UDP. The hardware appendix first says replanning every 1 s, then states every 0.5 s on the same page; this review retains that timing inconsistency. The non-deterministic filter alone takes 0.00025 s, which is not end-to-end perception/planning latency (p. 18). No cloud model is part of this pipeline.

## Key quantitative results

Only selected prose values are included; figure/table cells were not independently audited.

- Across 30 static physical environments, PwC is reported safe in 90% of trials, whereas CP-avg collides with a chair in half its trials; both methods account for 60 trials total (p. 7, Sec. 7).
- The hardware test uses the simulation-calibrated target safety rate 1 - epsilon = 0.85; nominal statistical safety is distinct from the measured 90% rate (p. 7).
- The hardware implementation reports 0.00025 s for the non-deterministic filter, alongside inconsistent 1 s/0.5 s replanning descriptions (p. 18).
- Path length in the hardware comparison is averaged only over successful trials; no all-trials path-length improvement is inferred (p. 6, Fig. 4 caption).

## Stated limitations

- Static obstacles are assumed; moving-agent uncertainty and motion-aware planning are future work (p. 8).
- Bounding-box inflation introduces conservatism; richer occupancy representations/nonconformity scores are proposed extensions (p. 8).
- Language-instructed navigation with multimodal foundation models is a future direction rather than a demonstrated component (p. 8).

## Transfer conditions

The environment-level guarantee requires representative, i.i.d. calibration/test environments from the same distribution and expresses confidence over calibration-dataset sampling (pp. 4-5). Robustness to planner-induced state shifts is not robustness to arbitrary new environment distributions. The formulation assumes a finite discrete state set; experiments use sampled configurations (pp. 4, 17). The downstream planner must model robot dynamics, know state, and enforce its safe-action condition in a static environment (p. 5). For a wheeled platform, verify dynamics/braking limits, pose errors, sensing coverage, calibration transfer, and end-to-end timing. Do not convert a probabilistic bound into deterministic collision freedom. G2 is narrowed by this interface, without establishing a global solution for language reasoning, dynamic obstacles, query cost, or model-timeout fallback.

## Code and data

A code/data release URL was not located in the selected sections; availability and execution were not verified.

## Version family

Formal CoRL 2024 proceedings paper, published in PMLR 270 in 2025. No DOI appears in the official citation. Preprint/later-version relationships were not audited; count this proceedings work once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. 9, Limitations and future work, p. 8 | "One limitation of our work is the assumption of static obstacles." |

## Page-cited excerpts

- **p. 7, Sec. 7, Hardware Validation.** "compare our PWC method against CP-avg. (defined in Section 6) across 30 different physical environments (60 trials total)."
  This records the finite hardware evaluation scope.
- **p. 18, Appendix G.1, Hardware.** "We use the Unitree Go1 quadruped robot with fully onboard sensing and computation."
  The hardware is legged and onboard.
- **p. 8, Sec. 9, Limitations and future work.** "One limitation of our work is the assumption of static obstacles."
  The result does not establish dynamic-obstacle safety.
- **p. 5, Sec. 5, Safe planning.** "the assumption of known state and static (but unknown) environment"
  End-to-end safety remains conditional on the safe-planner premises.

## Survey-usable statements

### Supported

- Environment-level conformal perception inflation can be combined with occupancy filtering and a safe planner to obtain conditional statistical safety assurances despite planner-induced state-distribution shifts.
- The mechanism has closed-loop evidence on an onboard-compute quadruped in static chair environments and may inform the corpus G2 interface question after wheeled-platform validation.

### Not supported

- Safety under arbitrary environmental distribution shift or uncertain pose: calibration/test environment sampling and known-state planning assumptions constrain the result.
- Dynamic-crowd safety or language-model navigation: both are future directions.
- Deterministic collision freedom, whole-pipeline 0.00025 s latency, or tested timeout recovery: the evidence supports none of those interpretations.

## Verification log

- 2026-11-02 | host: Codex | scope: targeted new-paper light review of physical PDF pp. 1, 4-8, 17-18, 25; metadata and original abstract checked; excerpts matched on exact cited PDF pages; selected prose numbers read; no whole-paper, proof, or table-cell audit; transcription was pending at drafting | corrections: new English follow-up card; retained legged boundary, calibration/planner premises, static-obstacle scope, and conflicting hardware replanning descriptions
- Source provenance: newly acquired official publisher PDF and unchanged raw publisher BibTeX, followup-2026-11-02; no legacy extraction was used. Identity: https://proceedings.mlr.press/v270/dixit25a.html. PDF SHA-256: fe3e502c22ee88202ac5682cdeb65fd7054b33697542c3fc55e40512b7dbb690.
- Verification level: light is used here for the user-authorized targeted follow-up read, not a full-paper audit; unreviewed sections, proofs, tables, and numerical claims remain unchecked.

- 2026-11-02 | host: Codex | scope: final transcription-bound validation; metadata, original abstract and retained excerpts checked with the PDF-inclusive review checker; original source bytes preserved; targeted light scope retained | corrections: parsing completed; selected excerpts shortened where OCR spacing or mathematical markup prevented matching; no whole-paper or full numeric verification

## Original abstract

Rapid advances in perception have enabled large pre-trained models to be used out of the box for transforming high-dimensional, noisy, and partial observations of the world into rich occupancy representations. However, the reliability of these models and consequently their safe integration onto robots remains unknown when deployed in environments unseen during training. In this work, we address this challenge by rigorously quantifying the uncertainty of pre-trained perception systems for object detection via a novel calibration technique based on conformal prediction. Crucially, this procedure guarantees robustness to distribution shifts in states when perceptual outputs are used in conjunction with a planner. As a result, the calibrated perception system can be used in combination with any safe planner to provide an end-to-end statistical assurance on safety in unseen environments. We evaluate the resulting approach, Perceive with Confidence (PWC), in simulation and on hardware where a quadruped robot navigates through previously unseen indoor, static environments. These experiments validate the safety assurances for obstacle avoidance provided by PWC and demonstrate up to 40% improvements in empirical safety compared to baselines.
