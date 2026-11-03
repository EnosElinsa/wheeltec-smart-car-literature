# Uncertainty-Aware Autonomous Robot Exploration Using Confidence-Rich Localization and Mapping

## Metadata

| Field | Value |
|---|---|
| ID | E14 |
| Title | Uncertainty-Aware Autonomous Robot Exploration Using Confidence-Rich Localization and Mapping |
| Authors | Yang Xu, Ronghao Zheng, Senlin Zhang, Meiqin Liu, and Junzhi Yu |
| Venue | IEEE Transactions on Automation Science and Engineering, vol. 22, pp. 1124-1138 |
| Year | 2025 (online 2024) |
| Type | journal |
| DOI | [10.1109/tase.2024.3360442](https://doi.org/10.1109/tase.2024.3360442) |
| Official URL | https://ieeexplore.ieee.org/document/10422987/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T2-slam-mapping-exploration/2025-Confidence-Rich-Exploration-E14/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2025-Confidence-Rich-Exploration-E14/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2025-Confidence-Rich-Exploration-E14/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: localization-mapping
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, dataset-playback, simulation
- protocol_caveats: few-trials
- platform_class: differential-drive
- platform: Turtlebot2 (Kobuki base); simulated robot in a cave map; Deutsches Museum laser dataset
- boundary_platform: no
- degradation: lidar-degeneracy
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: 2D LiDAR (SLAMTEC A2M8), reduced to 40 beams and 8 m range on the real robot
- compute: Intel i5-4210M 2.6 GHz laptop with 16 GB RAM; no per-step latency reported
- compute_location: not-reported
- summary_result: In five real Turtlebot2 office explorations per function, UCRMI needs 19.66% more time than CRMI but lowers overall uncertainty by about 32.85%.
- summary_limitation: The authors state that larger environments need more particles, which raises the computational cost of weight updates and resampling and may compromise RBPF-CLAM.
- survey_included: yes
- verification_level: light

## Problem

Active exploration should control map uncertainty and localization uncertainty together instead of planning on a fixed map information gain alone.

## Mechanism

RBPF-CLAM is a Rao-Blackwellized particle filter with a continuous confidence-rich occupancy map and closed-form measurement-likelihood particle weights. The entropy of the weighted particle trajectories is combined with confidence-rich mutual information (CRMI) into uncertain CRMI (UCRMI). An incremental information gathering (IIG) sampling planner uses a weight alpha to balance localization and mapping.

## Baselines and controls

OGMI and CRMI run with Gmapping; GPVR and UGPVR run with PoseSLAM; UCRMI runs with RBPF-CLAM. Ablations vary alpha and the map resolution. All information functions use the same IIG stopping criterion.

## Platform and setup

Localization replay on the Deutsches Museum dataset (5522 laser frames). A 20 m by 20 m cave simulation with 20 runs. Online ROS exploration of a 60 m office corridor with a Turtlebot2 (Kobuki base), five runs per information function.

## Evidence type and transfer

Online exploration on a real ground robot, public dataset replay, and simulation. The real robot is a Turtlebot2, not the reference platform.

## Sensors

2D SLAMTEC A2M8 LiDAR. On the real robot the scan is reduced from 760 beams and 12 m to 40 beams and 8 m. Localization uses 100 particles and every 13th beam. The simulation uses 10 beams and 5 m range.

## Compute and latency

Intel i5-4210M at 2.6 GHz with 16 GB RAM, on a laptop running ROS with Python and C++. Larger environments with more particles and denser maps raise the cost. Whether the laptop rode on the robot is not recorded in the legacy extraction.

## Key quantitative results

- Localization RMSE: about 44.7% average improvement of RBPF-CLAM over the state-of-the-art RBPF localization method on the dataset; the reference trajectory comes from a particle filter with more than 1000 particles on the full data (p. 9; reference setup p. 8).
- Real-world exploration, UCRMI versus CRMI: 19.66% more time, about 32.85% lower overall uncertainty (p. 11, Fig. 9(a) and Fig. 10(b)). Overall uncertainty is the paper's combined metric, not a ground-truth localization error along the run.
- Real-world exploration, UCRMI versus UGPVR: 25.36% less time (p. 11).

## Stated limitations

- In larger environments more particles are needed, which increases the computational cost of weight updates and resampling, so the performance of RBPF-CLAM may be compromised (p. 12).

## Transfer conditions

Legacy reviewer observations: the localization reference comes from a high-precision particle filter, not from measurement-grade ground truth. The information functions are compared with different SLAM back ends, so the differences cannot be attributed to the utility function alone. A too-small alpha stalls exploration, and the recommended range 0.5 to 0.9 comes from this setup only (not located). More scenes remain to be tested. A reuse on another wheeled robot needs a 2D LiDAR and re-tuned particle counts for the available compute.

## Code and data

The text gives a CRMI example at https://github.com/Shepherd-Gregory/CRMI (p. 4). Whether the complete UCRMI implementation is public was not checked; no code was run.

## Version family

The 2024 online article and the 2025 issue are the same work. The IROS 2022 paper on confidence-rich particle-filter localization and mapping is a predecessor in the same family, so it is not independent repeated evidence.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | direct-support | moderate | Abstract, p. 1 | "most MI-based exploration methods assume known poses or use inaccurate pose uncertainty approximation, which may lead to deviation or even failure when exploring prior unknown environments." |
| C6 | qualifies | weak | Real-world experiments, p. 11 | "We run 5 times independent trials for each function." |

## Page-cited excerpts

- **p. 8, Localization reference.** "we apply a high-precision particle filter containing over 1000 particles and use full data to generate a trajectory as the ground truth for comparison."
  The reference trajectory comes from an estimator, not from an external measurement.
- **p. 11, Real-world experiments.** "We run 5 times independent trials for each function."
  The real online exploration rests on a small sample.
- **p. 11, Exploration trade-off.** "UCRMI increases by 19.66% time cost than CRMI (see Fig. 9(a)) but reduces about 32.85% overall uncertainty (see Fig. 10(b))."
  The 19.66% extra time must be reported together with the 32.85% uncertainty reduction.
- **p. 1, Abstract.** "most MI-based exploration methods assume known poses or use inaccurate pose uncertainty approximation, which may lead to deviation or even failure when exploring prior unknown environments."
  The authors' motivation for including pose uncertainty in the utility.

## Survey-usable statements

### Supported

- Adding particle-based pose uncertainty to a confidence-rich mutual information utility trades exploration time for lower overall uncertainty on a real Turtlebot2 (19.66% more time, 32.85% lower uncertainty than CRMI, five runs; numbers from a light review; re-check before citing).

### Not supported

- UCRMI explores faster than CRMI: it takes 19.66% more time.
- The 44.7% RMSE improvement is against ground truth: the reference is a 1000-particle filter on full data.
- The gain comes from the utility function alone: the compared functions run on different SLAM back ends.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese card converted to the English template; no legacy quote dropped; reviewer observations moved from limitations to Transfer conditions
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/67da472cc962de0664a02438/

## Original abstract

Information-based autonomous robot exploration methods, aiming to maximize the exploration rewards, e.g., mutual information (MI), get more prevalent in field robotics applications. However, most MI-based exploration methods assume known poses or use inaccurate pose uncertainty approximation, which may lead to deviation or even failure when exploring prior unknown environments. In this paper, we explicitly consider full-state (pose & map) uncertainty for balancing exploration and localizability, i.e., avoiding the robot guiding itself to complex scenes with high exploration rewards but hard to localize. We first propose a Rao-Blackwellized particle filterbased localization and mapping framework (RBPF-CLAM) for a dense environmental map with continuous occupancy distribution. Then we develop a new closed-form particle weighting method to improve the localization accuracy and robustness. We further use these weighted particles to approximate the unknown pose uncertainty and combine it with our previous confidence-rich mutual information (CRMI) metric to evaluate the expected information utility of the robot’s new control actions. This new information metric is called uncertain CRMI (UCRMI). Dataset experiments show our RBPF-CLAM improves about 44.7% average root mean square error than the state-of-the-art RBPF localization method, and real-world experimental results show that our UCRMI reduces the pose uncertainty about 32.85% more than CRMI and 25.36% time cost than UGPVR in the exploration of unknown and unstructured scenes given sparse measurements, which shows better performance than other stateof-the-art information metrics.
