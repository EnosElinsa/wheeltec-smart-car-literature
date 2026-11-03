# Seeing Danger Before Moving: Learning Environment-Centric Risk for Safe Robot Navigation

## Metadata

| Field | Value |
|---|---|
| ID | E28 |
| Title | Seeing Danger Before Moving: Learning Environment-Centric Risk for Safe Robot Navigation |
| Authors | Palash Yuvraj Ingle and Young-Gab Kim |
| Venue | Robotics: Science and Systems XXII (Sydney, Australia) |
| Year | 2026 |
| Type | conference |
| DOI | [10.15607/rss.2026.xxii.133](https://doi.org/10.15607/rss.2026.xxii.133) |
| Official URL | https://www.roboticsproceedings.org/rss22/p133.pdf |
| Theme folder | T3-planning-control |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T3-planning-control/2026-Env-Risk-Learning-E28/paper.pdf` and `02-fulltext/T3-planning-control/2026-Env-Risk-Learning-E28/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2026-Env-Risk-Learning-E28/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: scripted-scenario, few-trials
- platform_class: wheeled-unspecified
- platform: custom rover with a 3D-printed chassis (wheels visible in Fig. 3, p. 7; drive type not reported)
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: environment-mounted OAK-D Pro RGB-D cameras and seven hazard sensor types; onboard sensing only for localization and motion
- compute: full pipeline 10 Hz, 95 ± 15 ms end to end; processor not reported
- compute_location: not-reported
- summary_result: In a three-corridor physical hazard testbed, EnvGuard reaches success 0.95 with 12.8 s exposure versus 0.90 and 19.8 s for unfiltered probabilistic risk.
- summary_limitation: The authors assume calibrated, sufficiently covering infrastructure sensors and reliable communication, do not model fast-moving people or robots, and fix the transition parameters.
- survey_included: yes
- verification_level: light

## Problem

Hazards such as smoke, heat, water, and structural instability can be observed by environment sensors before the robot comes near. Instantaneous risk estimates are noisy and cause frequent replanning.

## Mechanism

Fixed RGB-D cameras and seven sensor channels are mapped to a grid. A ResNet50 visual encoder and MLP sensor tokens are fused early in a transformer over a 5-frame window with focal loss. A Bayes belief update with fixed p11 = 0.95 and p01 = 0.05 filters the risk, and -log(1 - belief) is added to the static costmap so that a standard planner such as A* replans.

## Baselines and controls

- NoRisk (geometric cost only).
- Reactive (instantaneous threshold).
- Probabilistic (unfiltered probability cost).
- RAMP, EVORA, and Probabilistic Planning appear only as an attribute comparison in Table V; they were not re-implemented or run on the same benchmark.

## Platform and setup

A custom rover with a 3D-printed chassis drives through three geometrically similar modular corridors indoors, over multiple days with different hazard schedules. Hazards are not visible to the rover before it enters. The outdoor and stair capability shown in figures is not part of the controlled hazard trials.

## Evidence type and transfer

The legacy card lists physical multi-hazard testbed logs and executed trajectories, a belief-filtering ablation, and a comparison of navigation strategies. The planner drives the rover, so the evidence is closed-loop hardware in a staged indoor testbed.

## Sensors

Environment side: OAK-D Pro RGB-D at 640 by 480; MQ-2 smoke, DS18B20 temperature, KY-026 flame, HW-038 water, MQ-135 gas, 801S vibration, and MPU6050 tilt. The rover uses onboard sensing only for localization and motion execution.

## Compute and latency

Measured pipeline: 10 Hz, 95 ± 15 ms (p. 7, Table III); encoding 65 ± 8 ms, Bayes filtering 8 ± 2 ms, costmap update 5 ± 1 ms, planning 22 ± 7 ms. No CPU or GPU model is given. The legacy card notes that the component means add up to 100 ms, while the reported total is 95 ms, without explanation.

## Key quantitative results

- Navigation (Table IV): EnvGuard success 0.95, exposure 12.8 s, replans 2.1; versus NoRisk 0.82/42.5/0.4, Reactive 0.88/28.3/4.7, and Probabilistic 0.90/19.8/3.9 (p. 8, Table IV).
- Belief filtering (Table II): filtered versus instantaneous MSE 0.032 versus 0.187, false positives 0.05 versus 0.21, delay 1.1 s versus 0.3 s (p. 7, Table II).
- The warning threshold is crossed 4.2 ± 1.3 s before physical hazard contact (p. 7).

## Stated limitations

- The framework assumes calibrated infrastructure sensors with sufficient coverage and reliable communication; performance may degrade in unobserved areas, under communication delay, or with inaccurate calibration (p. 9).
- Fast-moving obstacles such as people or other robots are not modeled (p. 9).
- The Bayesian transition parameters are fixed from domain knowledge rather than learned (p. 9).

## Transfer conditions

Legacy reviewer observations: the text does not detail the training-set size and split, the number of trials, or paired statistics, so reproducibility and cross-site generalization cannot be claimed from the significance plots. The Table V attributes of earlier methods are the authors' positioning and were not checked; they are not a fair re-implemented benchmark of EVORA or RAMP.

## Code and data

Project page and source code: https://github.com/palashngl/EnvGuard.git (p. 2). No separate dataset download is described. Not run.

## Version family

Official RSS 2026 paper. The authors cite their 2025 multi-sensor fusion paper as background for the projection method but do not declare this paper an extension. The library counts this DOI once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Limitations, p. 9 | "but performance may degrade in unobserved areas, under communication delay, or when camera/sensor calibration is inaccurate." |

## Page-cited excerpts

- **p. 8, V-F Quantitative Comparison, Table IV.** "EnvGuard (Ours) 0.95 12.8 2.1"
  The Table IV row: success 0.95, exposure 12.8 s, 2.1 replans in the physical testbed.
- **p. 7, V-E System Latency.** "The complete pipeline operates at 10 Hz with an average latency of 95 ms"
  End-to-end latency on the physical system; the processor is not named.
- **p. 9, Limitations.** "but performance may degrade in unobserved areas, under communication delay, or when camera/sensor calibration is inaccurate."
  The method depends on infrastructure coverage and communication.
- **p. 9, Limitations.** "does not explicitly model fast-moving obstacles such as people or other robots"
  Dynamic obstacles are outside the scope.

## Survey-usable statements

### Supported

- Filtering environment-sensed risk as a latent Bayesian belief and adding it to the costmap lowers hazard exposure in a staged indoor testbed (12.8 s versus 19.8 s for unfiltered probabilistic risk; number from a light review, re-check before citing).
- Filtering trades a delay of about one second for lower MSE and fewer false positives.

### Not supported

- The method generalizes across sites or to dynamic obstacles: tests use one three-corridor testbed, and people and robots are not modeled.
- EnvGuard outperforms RAMP or EVORA: those methods were not run; Table V compares attributes only.
- Onboard hazard perception: hazards are sensed only by environment-mounted sensors.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; the legacy Table IV quote was found and kept; excerpts added from the latency and limitations text; platform_class wheeled-unspecified from the rendered Fig. 3 (p. 7)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/03ec4222b13ec6023c7bd9b9/

## Original abstract

Hazardous environments are characterized by uncertain, rapidly changing conditions, where autonomous robots are responsible for making safety-critical navigation decisions to ensure a safer path. When navigation relies solely on reactive perception, a robot may encounter dangerous situations before it has sufficient time to respond effectively. In real-world settings, however, hazards such as smoke, heat, flooding, or structural instability can be observed directly by the environment itself through cameras and sensors. This creates an opportunity to anticipate risk in advance, before a robot enters unsafe regions. In this work, we focus on enabling proactive and risk-aware robot navigation through environment-centric perception. We present a unified multimodal spatiotemporal model that estimates navigation risk by fusing environmental visual and sensory data through early integration, producing instantaneous probabilistic risk estimates. To avoid reacting to short-lived disturbances and sensor noise, these estimates are incorporated into a Bayesian filtering process that treats risk as an underlying latent state and maintains a stable belief over evolving environmental hazards. The resulting risk belief is integrated into the robot’s navigation stack as a cost term, guiding the planner toward safer routes and allowing the robot to avoid hazardous areas before reaching them. We evaluate the proposed approach on a physical multi-hazard testbed that includes smoke, heat, water presence, vibration, and structural obstacles. Experimental results show reduced hazard exposure and safer navigation behavior compared to risk-unaware baselines, highlighting the benefits of environmentcentric risk inference for autonomous robot navigation.
