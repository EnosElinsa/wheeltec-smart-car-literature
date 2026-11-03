# Sensor-based distributionally robust control for safe robot navigation in dynamic environments

## Metadata

| Field | Value |
|---|---|
| ID | M03 |
| Title | Sensor-based distributionally robust control for safe robot navigation in dynamic environments |
| Authors | Kehan Long, Yinzhuang Yi, Zhirui Dai, Sylvia Herbert, Jorge Cortés, and Nikolay Atanasov |
| Venue | The International Journal of Robotics Research, vol. 45, no. 2, pp. 328-351 |
| Year | 2026 (online 2025) |
| Type | journal |
| DOI | [10.1177/02783649251352000](https://doi.org/10.1177/02783649251352000) |
| Official URL | https://journals.sagepub.com/doi/10.1177/02783649251352000 |
| Theme folder | T2-slam-mapping-exploration |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T2-slam-mapping-exploration/2025-DR-safe-nav-M03/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2025-DR-safe-nav-M03/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2025-DR-safe-nav-M03/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: none
- platform_class: differential-drive
- platform: ClearPath Jackal, described as differential-drive in the text (p. 19); Gazebo simulation
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: 3D LiDAR (Ouster OS1-32); 9-axis IMU (UM7)
- compute: Intel i7-9700TE with 32 GB RAM onboard; CLF-DR-CBF QP at 50 Hz, A* reference path at 5 Hz
- compute_location: onboard
- summary_result: In Gazebo with pedestrians, the CLF-DR-CBF QP reaches 93.2% success and 1.7% collision, the highest success and lowest collision of three methods.
- summary_limitation: The authors state that the theory assumes valid relative-degree-1 CBFs, which can be nontrivial to find, and that evaluations use one differential-drive model.
- survey_included: yes
- verification_level: light

## Problem

Safe navigation in unknown, dynamically changing environments when LiDAR measurements and state estimates are noisy. Standard CLF-CBF quadratic programs assume known barrier functions and do not treat sensor and state uncertainty as a first-class constraint.

## Mechanism

A distributionally robust control barrier function (DR-CBF) folds noisy CBF samples from onboard sensing into a distributionally robust safety constraint, without reconstructing an explicit map or quantifying a precise uncertainty model. Coupled with a control Lyapunov function for path following, the resulting CLF-DR-CBF QP runs at 50 Hz; A* supplies a 5 Hz reference path. The formulation is written for control-affine dynamics and robots of arbitrary planar shape; the evaluations use a signed-distance CBF on a differential-drive model.

## Baselines and controls

Nominal CLF-CBF QP and a GP-CBF baseline. Other controls are not recorded in the legacy extraction; not verified.

## Platform and setup

Gazebo static scenes and pedestrian scenes with a social-force model. Real indoor lab tests on a ClearPath Jackal with an Ouster OS1-32 LiDAR, a UM7 9-axis IMU, and an Intel i7-9700TE with 32 GB RAM. Real tasks include thin chair legs, narrow passages, and approaching pedestrians.

## Evidence type and transfer

The tabulated success and collision rates come from Gazebo. The hardware runs close the loop on a Jackal in an indoor lab with pedestrians, not outdoor crowds. Trial counts and metrics of the hardware runs are not recorded in the legacy extraction.

## Sensors

3D LiDAR (Ouster OS1-32) and a 9-axis IMU (UM7).

## Compute and latency

Onboard Intel i7-9700TE with 32 GB RAM. The QP runs at 50 Hz and the A* reference path at 5 Hz. Per-solve latency is not recorded in the legacy extraction.

## Key quantitative results

- Gazebo with pedestrians: 93.2% success and 1.7% collision for the CLF-DR-CBF QP, the highest success and lowest collision among the three methods; the nominal CLF-CBF QP has more collisions and the GP-CBF baseline is slower (p. 18, Table 4).
- Control rates: CLF-DR-CBF QP at 50 Hz and A* reference path at 5 Hz (p. 15).

## Stated limitations

- The general framework assumes that valid CBFs with relative degree 1 exist, and identifying them can be nontrivial for complex or high-dimensional systems (p. 21).
- The evaluations use a signed distance function as a CBF on one differential-drive robot model (p. 21).
- Extensions to mobile manipulators and humanoids, and high-order CBFs, are left to future work (p. 21).

## Transfer conditions

Legacy reviewer observations: discrete-rate QP execution and the CLF slack trade safety against tracking (not located). The hardware is a specific differential-drive LiDAR stack with an i7-class computer, tested indoors. A wheeled robot with a 2D LiDAR or weaker compute needs its own CBF sampling and solver timing check.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. 10, p. 20 | "We introduced a novel strategy for ensuring safety of mobile robots navigating autonomously in unknown dynamically changing environments." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | direct-support | moderate | Sec. 10, p. 20 | "Our approach underscores the efficiency and effectiveness of employing sensor-based DR-CBF constraints to handle uncertainty in measurements and state estimates." |
| C6 | qualifies | moderate | Sec. 9.3, p. 19 | "The robot was equipped with an Intel i7-9700TE CPU with 32 GB RAM, an Ouster OS1-32 LiDAR, and a UM7 9-axis IMU" |

## Page-cited excerpts

- **p. 20, Conclusion and future work.** "We introduced a novel strategy for ensuring safety of mobile robots navigating autonomously in unknown dynamically changing environments."
  Unknown, dynamically changing environments are the designed operating condition.
- **p. 20, Conclusion and future work.** "Our approach underscores the efficiency and effectiveness of employing sensor-based DR-CBF constraints to handle uncertainty in measurements and state estimates."
  The safety constraint is built on measurement and state-estimate uncertainty; this is a robust CBF, not a fault-detection state machine.
- **p. 21, Conclusion and future work.** "However, identifying such functions can be nontrivial, particularly for complex or high-dimensional systems."
  The authors' limitation on the existence of valid CBFs.
- **p. 21, Conclusion and future work.** "we employed a signed distance function as a CBF for a differential-drive robot in Section 8 and conducted our evaluations on this specific model."
  All evaluations use one robot model.
- **p. 18, Results and discussion.** "The proposed CLF-DR-CBF QP approach achieves the highest success rate (93.2%) and the lowest collision rate (1.7%) among the three methods."
  The headline result is from Gazebo.
- **p. 19, Real-world experiments.** "The robot was equipped with an Intel i7-9700TE CPU with 32 GB RAM, an Ouster OS1-32 LiDAR, and a UM7 9-axis IMU"
  The hardware stack behind the real tests.

## Survey-usable statements

### Supported

- A sensor-based DR-CBF in a CLF-DR-CBF QP at 50 Hz navigated a Jackal among pedestrians indoors and reached 93.2% success with 1.7% collision in Gazebo (numbers from a light review; re-check before citing).

### Not supported

- The method is validated in outdoor crowds: the real tests are indoor lab pedestrians.
- The method applies to any robot without CBF design: the authors state that valid relative-degree-1 CBFs are assumed and evaluations use one differential-drive model.
- The method detects sensor faults: it is a robust safety constraint, not a fault detector.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-form card (Validation, Tags, Claim summary, Hardware caveat) converted to the English template; the legacy card had no verbatim quotes, so excerpts were taken from the conclusion and from sentences located for legacy facts (p. 18, p. 19); the discrete-rate and CLF-slack note moved from limitations to Transfer conditions because it was not located; Year set to the bibliographic year 2026 with online 2025
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

We introduce a novel methodfor mobile robot navigation in dynamic, unknown environments, leveraging onboard sensing and distributionally robust optimization to impose probabilistic safety constraints. Our method introduces a distributionally robust control barrier function (DR-CBF) that directly integrates noisy sensor measurements and state estimates to define safety constraints. This approach is applicable to a wide range ofcontrol-affine dynamics, generalizable to robots with complex geometries, and capable of operating at real-time control frequencies. Coupled with a control Lyapunovfunction (CLF)for pathfollowing, the proposed CLF-DR-CBF control synthesis method achieves safe, robust, and efficient navigation in challenging environments. We demonstrate the effectiveness and robustness ofour approachfor safe autonomous navigation under uncertainty and dynamic obstacles in simulations and real-world experiments with differential-drive robots
