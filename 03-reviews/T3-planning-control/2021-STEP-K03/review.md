# STEP: Stochastic Traversability Evaluation and Planning for Risk-Aware Off-road Navigation

## Metadata

| Field | Value |
|---|---|
| ID | K03 |
| Title | STEP: Stochastic Traversability Evaluation and Planning for Risk-Aware Off-road Navigation |
| Authors | David D. Fan, Kyohei Otsu, Yuki Kubo, Anushri Dixit, Joel Burdick, and Ali-akbar Agha-mohammadi |
| Venue | Robotics: Science and Systems |
| Year | 2021 |
| Type | conference |
| DOI | [10.15607/rss.2021.xvii.021](https://doi.org/10.15607/rss.2021.xvii.021) |
| Official URL | https://www.roboticsproceedings.org/rss17/p021.html |
| Theme folder | T3-planning-control |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T3-planning-control/2021-STEP-K03/paper.pdf` and `02-fulltext/T3-planning-control/2021-STEP-K03/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2021-STEP-K03/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: wheeled-unspecified
- platform: Clearpath Husky in an abandoned subway (two levels, about 200 m x 100 m) and Boston Dynamics Spot in a lava tube; the simulation uses a differential-drive model (pp. 7-8).
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Three Velodyne VLP-16 LiDARs on the Husky; one VLP-16 fused with Spot's RealSense data; LiDAR SLAM localization (p. 8)
- compute: Entire autonomy stack on an onboard Intel Core i7 CPU; the traversability stack uses about one core (p. 8).
- compute_location: onboard
- summary_result: In 50 Monte Carlo simulations, higher CVaR risk levels give longer paths with lower peak risk; Spot traverses 420 m of lava tube in 24 minutes (pp. 7-8).
- summary_limitation: The authors name robustification of subcomponents and extension to higher speeds as future work (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Off-road traversal decisions depend on uncertain elevation maps, and minimizing the mean cost ignores rare but severe events. STEP plans under tail risk measured by CVaR (pp. 1-2).

## Mechanism

A 2.5D grid map stores elevation statistics. Each risk factor (collision, step, tip-over, contact loss, slippage, negative obstacles, sensor uncertainty) is modeled as a normal random variable, and the factors are aggregated into a CVaR risk map. A geometric planner finds a CVaR-minimizing path, and an SQP-based MPC refines a kinodynamically feasible trajectory with relaxed risk constraints (pp. 2-6). The variance of the collision risk comes from the elevation-map variance, which the authors describe as mainly a function of localization error (p. 5).

## Baselines and controls

The simulation compares STEP at different risk levels; no external planner is benchmarked in the inspected pages (p. 7).

## Platform and setup

Simulation: 50 Monte Carlo runs with random maps, random traversability costs and goals 8 m away, assuming no localization error, no tracking error and a simplified perception model (p. 7). Hardware: a Husky running JPL NeBula autonomy explored two levels of an abandoned subway, and Spot explored Valentine Cave (p. 8).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`, but the hardware runs report coverage and distance without repeated trials; the quantitative risk-distance trade-off comes from simulation. The provisional module `traversability-planning-control` is confirmed: the contribution is a risk-aware traversability planner. The Husky is coded `wheeled-unspecified` because its drive type is not stated; Spot is the legged comparison.

## Sensors

The Husky uses three Velodyne VLP-16 LiDARs and onboard LiDAR SLAM; Spot fuses one VLP-16 with its internal RealSense data (p. 8).

## Compute and latency

The entire autonomy stack runs on an Intel Core i7 CPU, and the traversability stack uses about one core (p. 8). Planning rates were not inspected.

## Key quantitative results

- Simulation: 50 Monte Carlo runs; low risk levels give shorter paths and high levels long detours (p. 7, Figs. 7-8; values in plots only).
- Husky: explored two levels of an approximately 200 m x 100 m subway environment (p. 8).
- Spot: navigated 420 m over 24 minutes, covering 1205 square meters of rough terrain in the lava tube (p. 8).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Future work includes robustification of subcomponents and extension to higher speeds (p. 8).
- The simulation study assumes no localization error, no tracking error and a simplified perception model (p. 7).

## Transfer conditions

Pose uncertainty enters the risk map only through elevation-map variance; it is not propagated into the footprint or the MPC state. The simulation excludes localization error, so the hardware runs are the only evidence under real pose error, and they report no failure rates.

## Code and data

Code availability was not checked; the paper links a video (p. 1).

## Version family

Counted once by the registered RSS 2021 identity; no other version is in the library.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 2, Sec. I, contributions.** "Uncertainty-aware 2.5D traversability evaluation which accounts for localization error, sensor noise, and occlusion, and combines multiple sources of traversability risk."
  States that localization error enters the traversability evaluation.
- **p. 5, Sec. IV-B.** "collision risk is determined by checking for points above the elevation map, and the variance is derived from the elevation map variance, which is mainly a function of localization error."
  Names the path by which pose uncertainty enters the risk: the variance of the elevation map.
- **p. 7, Sec. V-A.** "The following assumptions are made: 1) no localization error, 2) no tracking error, and 3) a simplified perception model with artificial noise."
  The quantitative simulation excludes the localization error that the method accounts for.
- **p. 8, Sec. V-B.** "STEP navigates 420 meters over 24 minutes, covering 1205 square meters of rough terrain."
  Single legged-robot field run without failure statistics.

## Survey-usable statements

### Supported

- STEP propagates localization error into terrain decisions through the variance of the elevation map behind its CVaR collision risk.
- STEP ran onboard a wheeled Husky and a legged Spot at subterranean field sites.

### Not supported

- The simulation does not test how localization error changes risk or outcomes, because it assumes none.
- The field runs provide neither failure rates nor comparisons with another planner.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 4, 5, 7, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.
- abstract-waiver: the local two-column transcription interleaves the abstract with the Fig. 1 caption on p. 1; the abstract was copied from and checked against the PDF text layer of p. 1.

## Original abstract

Although ground robotic autonomy has gained widespread usage in structured and controlled environments, autonomy in unknown and off-road terrain remains a difficult problem. Extreme, off-road, and unstructured environments such as undeveloped wilderness, caves, and rubble pose unique and challenging problems for autonomous navigation. To tackle these problems we propose an approach for assessing traversability and planning a safe, feasible, and fast trajectory in real-time. Our approach, which we name STEP (Stochastic Traversability Evaluation and Planning), relies on: 1) rapid uncertainty-aware mapping and traversability evaluation, 2) tail risk assessment using the Conditional Value-at-Risk (CVaR), and 3) efficient risk and constraint-aware kinodynamic motion planning using sequential quadratic programming-based (SQP) model predictive control (MPC). We analyze our method in simulation and validate its efficacy on wheeled and legged robotic platforms exploring extreme terrains including an abandoned subway and an underground lava tube.
