# Optimizing exploration with a new uncertainty framework for active SLAM systems

## Metadata

| Field | Value |
|---|---|
| ID | E12 |
| Title | Optimizing exploration with a new uncertainty framework for active SLAM systems |
| Authors | Sebastian Sansoni, Javier Gimenez, Gastón Castro, Santiago Tosetti, and Flavio Capraro |
| Venue | Robotics and Autonomous Systems, vol. 193, art. 105059 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1016/j.robot.2025.105059](https://doi.org/10.1016/j.robot.2025.105059) |
| Official URL | https://linkinghub.elsevier.com/retrieve/pii/S0921889025001459 |
| Theme folder | T2-slam-mapping-exploration |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T2-slam-mapping-exploration/2025-Active-SLAM-Uncertainty-E12/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2025-Active-SLAM-Uncertainty-E12/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2025-Active-SLAM-Uncertainty-E12/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: localization-mapping
- evidence_type: simulation
- evidence_all: simulation, theory-only
- protocol_caveats: none
- platform_class: differential-drive
- platform: simulated differential-drive robot in Gazebo (drive type from the text, p. 7)
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: simulated 360-degree 2D LiDAR (5 m range, 0.5-degree resolution); landmark-based KF SLAM
- compute: not reported; only complexity orders are given
- compute_location: not-reported
- summary_result: In Gazebo, uncertainty-frontier planning lowers final SiREn dispersion, but with sigma_max 0.6 m and incomplete landmarks the map is not fully explored.
- summary_limitation: The authors assume known orientation and leave a planner that combines UF and SiREn, also for non-landmark SLAM, to future work.
- survey_included: yes
- verification_level: light

## Problem

Exploration coverage and map reconstruction quality cannot be measured by the number of unknown grid cells alone. The paper uses an interpretable uncertainty map and uncertainty frontiers to balance re-observation of mapped areas against exploration of new areas.

## Mechanism

The Uncertainty Map (UM) is built from the dispersion probability that a measurement falls into a cell and a modified log-odds update. Uncertainty Frontiers (UF) come from a threshold on the spatial gradient of the UM. The Signed Relative Entropy (SiREn), taken relative to a maximum admissible uncertainty sigma_max, measures coverage and accuracy together. Appendix A.1 gives the UM as a lower bound of the geometric mean of the measurement standard deviations; this theoretical bound is not an upper bound on a safety probability.

## Baselines and controls

Four planning setups (PPS): PPS1, classic frontiers (CF) with greedy RRT; PPS2, CF with RRT* using an uncertainty cost; PPS3, UF with the same RRT* and sigma_max = 0.6 m; PPS4, UF with sigma_max = 1 m. This is not a common hardware benchmark against complete mainstream active SLAM systems.

## Platform and setup

All experiments are Gazebo simulations of a differential-drive wheeled robot. A rectangular 30 m by 18 m area contains corridors and open spaces. Two initial positions, complete and incomplete landmark layouts, and the four PPS give 16 experiments, each run at least five times. A separate corridor demonstration shows UF behavior.

## Evidence type and transfer

Theory and simplified simulation only. There is no real robot, no replay of real logs, and no closed-loop hardware evidence.

## Sensors

A simulated 360-degree 2D LiDAR with 5 m range and 0.5-degree resolution. A linear Kalman filter estimates position only; orientation is treated as known and there are no matching errors. The low-level controller lets the planning layer treat the nonholonomic robot as omnidirectional.

## Compute and latency

No CPU, GPU, memory, or measured latency is reported. The per-step complexity O(N) and the worst-case O(N^2) for a map assume a dynamic-programming or ray-casting implementation, and a Monte Carlo dispersion-probability evaluation needs O(k d^3) per call. Embedded real-time operation is therefore not shown.

## Key quantitative results

- Final SiREn dispersion is lower with uncertainty frontiers; with the incomplete landmark layout, PPS3 (sigma_max 0.6 m) does not fully explore the map, while PPS4 (sigma_max 1 m) covers more (p. 8, Fig. 8; legacy also cites Fig. 9, p. 9).
- The median UM uncertainty correlates at 97% with the median combined landmark uncertainty, with a fit of 0.971 sigma + 0.00127 (p. 9, Eq. 23). This is a correlation between measures, not a 97% localization accuracy or an error improvement.

## Stated limitations

- Orientation is considered known in the SLAM system used for the experiments (p. 11).
- A planning system that integrates UFs and SiREn and applies to landmark-based and non-landmark-based SLAM is left to future work (p. 10).

## Transfer conditions

Legacy reviewer observations: sigma_max is not a hard planning constraint (legacy location p. 6; not located). Landmark layout and start position strongly affect the outcome, and exhausting the frontiers is not a general guarantee of complete coverage. The derivations were not independently re-checked. A wheeled reuse needs a SLAM back end with orientation uncertainty and data-association errors, which the simulation excludes.

## Code and data

Code: https://github.com/Seba-san/UncertaintyMap (p. 2); not run. The abstract says all generated data are openly available, while the Data availability statement says data will be made available on request (p. 11). The difference is kept; open download is not verified.

## Version family

UncertaintyMap and the UM, UF, and SiREn framework are one work, represented by this 2025 journal paper. It is not in the same family as the confidence-rich UCRMI paper (E14) or FIT-SLAM2 (E13).

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | partial-support | weak | Uncertainty correlation, p. 9 | "measure correlates strongly, at 97%, with the median uncertainty of the entire map" |
| C6 | qualifies | moderate | Evaluation, p. 7 | "All experiments are performed with a differential robot simulated in Gazebo." |

## Page-cited excerpts

- **p. 7, Evaluation.** "All experiments are performed with a differential robot simulated in Gazebo."
  All evidence is wheeled-robot simulation.
- **p. 8, Results (PPS3).** "For PPS3, the map is not fully explored when using an incomplete landmark disposition."
  A counterexample in which uncertainty frontiers stop exploration early.
- **p. 9, Uncertainty correlation.** "measure correlates strongly, at 97%, with the median uncertainty of the entire map"
  The 97% is a correlation between measures, not a localization accuracy.
- **p. 11, A.5 SLAM system.** "orientation is considered known"
  The Kalman filter leaves out orientation uncertainty.
- **p. 11, Data availability.** "Data will be made available on request."
  Data openness cannot be taken from the abstract alone.

## Survey-usable statements

### Supported

- An uncertainty map with uncertainty frontiers and the SiREn measure gives an interpretable exploration-exploitation parameter (sigma_max) in Gazebo simulation of a differential-drive robot.
- The UM median uncertainty correlates at 97% with the median landmark uncertainty in the authors' simulation (number from a light review; re-check before citing).

### Not supported

- Uncertainty frontiers always complete exploration: PPS3 with incomplete landmarks does not fully explore the map.
- The method is validated on a real robot or runs in real time onboard: evidence is simulation only and no timing is reported.
- The 97% figure is a localization accuracy: it is a correlation between uncertainty measures.
- The generated data are openly downloadable: the Data availability statement says on request.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; no legacy quote dropped (double spaces from line breaks normalized); the sigma_max hard-constraint note moved to Transfer conditions because it was not located
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/eab40f811966b8e20e49d43c/

## Original abstract

Accurate reconstruction of the environment is a central goal of Simultaneous Localization and Mapping (SLAM) systems. However, the agent’s trajectory can significantly affect estimation accuracy. This paper presents a new method to model map uncertainty in Active SLAM systems using an Uncertainty Map (UM). The UM uses probability distributions to capture the spatial distribution of map uncertainty, allowing Uncertainty Frontiers (UF) to be defined as key exploration–exploitation objectives and potential stopping criteria. In addition, the method introduces the Signed Relative Entropy (SiREn), based on the Kullback–Leibler divergence, to measure both coverage and uncertainty together. This helps balance exploration and exploitation through an easy-to-understand parameter. Unlike methods that depend on particular SLAM setups, the proposed approach is compatible with different types of sensors, such as cameras, LiDARs, and multi-sensor fusion. It also addresses common problems in exploration planning and stopping conditions. Furthermore, integrating this map modeling approach with a UF-based planning system enables the agent to autonomously explore open spaces, a behavior not previously observed in the Active SLAM literature. Code and implementation details are available as a ROS node, and all generated data are openly available for public use, facilitating broader adoption and validation of the proposed approach.
