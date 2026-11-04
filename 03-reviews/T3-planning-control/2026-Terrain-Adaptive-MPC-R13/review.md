# A Terrain-Adaptive $\epsilon$-Constraint MPC for Uneven Terrain Kinodynamic Planning

## Metadata

| Field | Value |
|---|---|
| ID | R13 |
| Title | A Terrain-Adaptive $\epsilon$-Constraint MPC for Uneven Terrain Kinodynamic Planning |
| Authors | Otobong Jerome, Geesara Kulathunga, and Tiago Nascimento |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3728313](https://doi.org/10.1109/lra.2026.3728313) |
| Official URL | https://ieeexplore.ieee.org/document/11668628/ |
| Theme folder | T3-planning-control |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2026-Terrain-Adaptive-MPC-R13/paper.pdf` and `02-fulltext/T3-planning-control/2026-Terrain-Adaptive-MPC-R13/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2026-Terrain-Adaptive-MPC-R13/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: skid-steer
- platform: Gazebo AgileX Scout Mini on two 3D meshes; physical Scout Mini outdoors and a four-wheeled JetAuto base (pp. 6-7).
- boundary_platform: no
- degradation: terrain, wheel-slip
- degradation_observed: wheel-slip
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Velodyne VLP-16 for terrain perception on the Scout Mini (p. 7)
- compute: Workstation with Intel Core i7, RTX 4050 GPU and 32 GB RAM (p. 7).
- compute_location: not-reported
- summary_result: Terrain-adaptive epsilon-constraint MPC reaches 94% success in simulation and 80% on hardware, where wheel slip and sensor noise reduce success (p. 7).
- summary_limitation: Assumes a static, offline-constructed mesh; dynamic obstacles and semantic terrain properties are future work (pp. 2, 8).
- survey_included: yes
- verification_level: light

## Problem

Path efficiency and pose stability conflict on uneven terrain, and fixed weights cannot balance them across terrains.

## Mechanism

Path length is minimized while pose-stability cost is bounded by an epsilon adjusted online from local terrain descriptors; a semi-parametric model combines car-like kinematics with a sparse GP trained on descriptor-conditioned rollouts; FMM on triangle meshes guides the MPC (pp. 2-6).

## Baselines and controls

MPPI and genetic-algorithm kinodynamic planning (GAKD), with ablations and sensitivity analysis (pp. 6-7).

## Platform and setup

Simulation trials on two meshes and outdoor hardware comparisons (pp. 6-7). Gazebo AgileX Scout Mini on two 3D meshes; physical Scout Mini outdoors and a four-wheeled JetAuto base (pp. 6-7).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Simulation and outdoor hardware with the planner driving the robot; hardware trial counts were not inspected.

## Sensors

Velodyne VLP-16 for terrain perception on the Scout Mini (p. 7).

## Compute and latency

Workstation with Intel Core i7, RTX 4050 GPU and 32 GB RAM (p. 7).

## Key quantitative results

- Success drops from 94% in simulation to 80% on hardware owing to unmodeled wheel slip and sensor noise (p. 7).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The approach assumes a static, offline-constructed mesh (p. 2).
- Failures arise from FMM-unreachable goals, local minima in narrow corridors and stability violations at terrain discontinuities (p. 8).

## Transfer conditions

Needs a prior terrain mesh and descriptor-conditioned GP training on the platform; terrain material is not modeled.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity; no other version is in the library.

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

- **p. 7, Sec. VI-E.** "Real-world results follow the simulation trends: success rate drops from 94% to 80% due to unmodelled effects such as wheel slip and sensor noise, while path-length deviation rises from 8.5 m to 10.8 m as the planner takes more conservative routes under uncertainty."
  Sim-to-real gap attributed to contact and sensing.
- **p. 2, Sec. II.** "The above assumes a static, offline-constructed mesh."
  Map assumption.

## Survey-usable statements

### Supported

- Terrain-conditioned stability bounds in MPC are executed on a wheeled robot with reported sim-to-real degradation.

### Not supported

- The stability bound is not a calibrated tip-over probability.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 4, 6, 7, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Kinodynamic planning for car-like vehicles on uneven terrain requires jointly optimising objectives such as path efficiency and pose stability, which often conflict on challenging terrain. This work formulates the problem as a multi-objective optimisation and solves it using the $\epsilon$-constraint method, a classical technique that minimises one objective while constraining each remaining objective to lie below an upper bound $\epsilon$. The method is embedded in a Model Predictive Control (MPC) framework in which the $\epsilon$ bounds are adjusted online from local terrain descriptors, allowing the planner to explore the Pareto front in real time. The motion of the vehicle over the terrain is captured by a semi-parametric model that combines analytical car-like dynamics with a Sparse Gaussian Process trained on the same terrain descriptors. The proposed $\epsilon$-MPC is evaluated against two sampling-based baselines, Model Predictive Path Integral (MPPI) control and Genetic-Algorithm Kinodynamic (GAKD) planning, achieving a 94% navigation success rate while reducing maximum orientation deviation by up to 24% and improving multi-objective trade-off quality by up to 23% relative to MPPI.
