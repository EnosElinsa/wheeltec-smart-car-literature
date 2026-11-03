# NAMR-RRT: Neural Adaptive Motion Planning for Mobile Robots in Dynamic Environments

## Metadata

| Field | Value |
|---|---|
| ID | M08 |
| Title | NAMR-RRT: Neural Adaptive Motion Planning for Mobile Robots in Dynamic Environments |
| Authors | Zhirui Sun, Bingyi Xia, Peijia Xie, Xiaoxiao Li, and Jiankun Wang |
| Venue | IEEE Transactions on Automation Science and Engineering, vol. 22, pp. 13087-13100 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tase.2025.3551464](https://doi.org/10.1109/tase.2025.3551464) |
| Official URL | https://ieeexplore.ieee.org/document/10926876/ |
| Theme folder | T3-planning-control |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T3-planning-control/2025-NAMR-RRT-M08/paper.pdf` and `02-fulltext/T3-planning-control/2025-NAMR-RRT-M08/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2025-NAMR-RRT-M08/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: unnamed 0.45 m x 0.45 m x 1.23 m wheeled robot
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Ouster OS0-32 LiDAR, Intel RealSense D435i
- compute: onboard i7-1165G7 CPU and NVIDIA GTX 2060 GPU; planning times not recorded in the legacy extraction
- compute_location: onboard
- summary_result: Over 100 simulated runs per setting on three maps with pedestrians, NAMR-RRT outperformed Risk-RRT, Bi-Risk-RRT, Multi-Risk-RRT, and NMR-RRT; the legacy extraction records no values.
- summary_limitation: No limitation is stated by the authors; evidence is three simulated maps with dataset pedestrian trajectories plus indoor trials with moving obstacles on one unnamed robot.
- survey_included: yes
- verification_level: light

## Problem

Risk-based RRT planners in dynamic, crowded scenes waste search effort in
irrelevant regions. Bi-directional and multi-directional variants still
explore broadly, and the nonholonomic two-point boundary value problem makes
tree connection expensive.

## Mechanism

NAMR-RRT uses a PointNet++ network to generate a heuristic region and updates
the heuristic region and the sampling rate adaptively during the search. It
combines this guidance with multi-directional, risk-aware tree growth.
NMR-RRT is the ablation with a fixed heuristic region and sampling rate.

## Baselines and controls

The comparators are Risk-RRT, Bi-Risk-RRT, Multi-Risk-RRT, and NMR-RRT
(fixed heuristic region and sampling rate).

## Platform and setup

PointNet++ was trained offline on 10000 synthetic 2D maps with A* path labels
(AMD EPYC MILAN 7413 CPU and NVIDIA RTX A6000 GPU). Simulation uses three maps with
static obstacles and pedestrian trajectories taken from a public dataset;
results are averaged over 100 runs. Real indoor trials use static boxes and
moving cylinders on an unnamed 0.45 m x 0.45 m x 1.23 m robot.

## Evidence type and transfer

The comparative numbers come from simulation with replayed pedestrian
trajectories. The real indoor trials run the planner on the robot. The legacy
extraction notes that the conclusion does not separate simulated pedestrian
playback from physical moving obstacles. It does not record whether the
hardware trials report tabulated metrics, so no hardware caveat is coded; not
verified. The chassis make and drive type are not named, so the platform is
coded as wheeled-unspecified.

## Sensors

Ouster OS0-32 LiDAR and Intel RealSense D435i camera.

## Compute and latency

Training ran offline on an AMD EPYC MILAN 7413 CPU with an NVIDIA RTX A6000 GPU.
The robot carries an onboard computer with an i7-1165G7 CPU and an NVIDIA GTX
2060 GPU. Planning times are not recorded in the legacy extraction.

## Key quantitative results

- Simulation results are averaged over 100 independent runs on three maps (p. 9).
- The PointNet++ training set has 10000 random 2D environments (p. 8).
- NAMR-RRT outperforms the risk-based planners and NMR-RRT in the simulation comparison; the legacy extraction records no values (p. 13).

## Stated limitations

- Future work will develop neural networks that generate more refined heuristic regions and add imperative learning so the planner learns from past searches (p. 13).

## Transfer conditions

The real trials use an unnamed indoor robot with a 32-beam LiDAR, an RGB-D
camera, and a laptop-class GTX 2060 GPU. A reader must check the GPU budget
for PointNet++ inference and the robot kinematics before reuse. The
pedestrian evidence in simulation is trajectory playback, so reactive human
behavior is not tested there.

## Code and data

The abstract gives a project website at https://sites.google.com/view/namr-rrt.
Code and data release are not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Abstract, p. 1 | "Traditional risk-based motion planning algorithms face challenges in such scenarios due to the lack of a well-defined search region" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Experiment platform, p. 9 | "operating on an onboard computer powered by an i7-1165G7 CPU and an NVIDIA GTX 2060 GPU." |

## Page-cited excerpts

- **p. 13, Sec. VII.** "The experiment results demonstrate that NAMR-RRT consistently outperforms traditional methods and NMR-RRT, a neural network-based method, which operates with a fixed heuristic region and sampling rate."
  The authors' summary claim; it does not separate simulation from hardware results.
- **p. 9, Experiment platform.** "operating on an onboard computer powered by an i7-1165G7 CPU and an NVIDIA GTX 2060 GPU."
  The hardware trials need a discrete GPU onboard; the chassis is not named.
- **p. 13, Sec. VII.** "Future work will investigate advanced neural network models for generating more refined heuristic regions while integrating imperative learning to enable the algorithm to learn from past experiences and enhance the search process."
  The authors' stated direction for future work.

## Survey-usable statements

### Supported

- Learned heuristic regions with adaptive updates of region and sampling rate improve risk-based RRT planning in simulated dynamic scenes against fixed-region and non-learned variants (100 runs per setting; numbers from a light review; re-check before citing).
- The planner ran on a real indoor robot with an onboard GTX 2060 GPU.

### Not supported

- Quantitative hardware superiority: the legacy extraction records no hardware metrics.
- Robustness to reactive pedestrians: simulated pedestrians replay dataset trajectories.
- Transfer to a named commercial chassis: the robot base is not named.

## Verification log

- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); legacy C2 excerpt replaced by an abstract sentence because it does not show the claim and its PDF text differs (ligature); legacy C6 excerpt kept as a page-cited excerpt and replaced in the claim row by the platform sentence; abstract copied from the transcription, which drops the "ff" and "fi" ligatures ("eficient"), and the Note to Practitioners is omitted
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Robots are increasingly deployed in dynamic and crowded environments, such as urban areas and shopping malls, where eficient and robust navigation is crucial. Traditional risk-based motion planning algorithms face challenges in such scenarios due to the lack of a well-defined search region, leading to ineficient exploration in irrelevant areas. While bi-directional and multi-directional search strategies can improve eficiency, they still result in significant unnecessary exploration. This article introduces the Neural Adaptive Multi-directional Risk-based Rapidly-exploring Random Tree (NAMR-RRT) to address these limitations. NAMR-RRT integrates neural network-generated heuristic regions to dynamically guide the exploration process, continuously refining the heuristic region and sampling rates during the planning process. This adaptive feature significantly enhances performance compared to neural-based methods with fixed heuristic regions and sampling rates. NAMR-RRT improves planning eficiency, reduces trajectory length, and ensures higher success by focusing the search on promising areas and continuously adjusting to environments. The experiment results from both simulations and real-world applications demonstrate the robustness and efectiveness of our proposed method in navigating dynamic environments. A website about this work is available at https://sites.google.com/view/namr-rrt.
