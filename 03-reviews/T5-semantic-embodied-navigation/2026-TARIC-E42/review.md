# TARIC: Memory-Augmented Traversability-Aware Outdoor VLN Under Interrupted Semantic Cues

## Metadata

| Field | Value |
|---|---|
| ID | E42 |
| Title | TARIC: Memory-Augmented Traversability-Aware Outdoor VLN Under Interrupted Semantic Cues |
| Authors | Tianle Zeng, Hanjing Ye, Jianwei Peng, Jingwen Yu, Hanxuan Chen, and Hong Zhang |
| Venue | IEEE Robotics and Automation Letters, vol. 11, no. 9, pp. 10082-10089 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3707347](https://doi.org/10.1109/lra.2026.3707347) |
| Official URL | https://ieeexplore.ieee.org/document/11578332/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2026-TARIC-E42/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2026-TARIC-E42/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2026-TARIC-E42/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: offboard-compute
- platform_class: wheeled-unspecified
- platform: AgileX Scout Mini (quantitative real-world trials; drive type not recorded in the legacy card); Unitree Go1 (qualitative only); simulated agents in Unreal
- boundary_platform: no
- degradation: none
- degradation_observed: dynamic-objects, terrain
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: front stereo camera, LiDAR, odometry
- compute: external PC with RTX 3090 GPU; Qwen3-VL-4B perception about 2.8 s per update (0.3-0.5 Hz)
- compute_location: offboard-local
- summary_result: Real-world Scout Mini, 40 episodes on two campus routes: combined SR 40.0% versus 17.5% for the strongest baseline (GPT-4o-GeNie).
- summary_limitation: The authors report takeovers caused by pedestrians and other moving agents, memory drift over long cue-free stretches, and traversability misjudgments that cause detours.
- survey_included: yes
- verification_level: light

## Problem

In long-range outdoor vision-language navigation, a distant goal can leave the field of view or be occluded. During the following cue-free phase, the robot must keep an executable goal direction while it detours around non-traversable ground.

## Mechanism

Qwen3-VL-4B splits the instruction into goal and exploration language and scores image patches at several scales. The goal direction is accepted when the peak-to-mean ratio exceeds 1.5; otherwise the exploration cue is used. The VLM also outputs a traversability score for 10 heading sectors, and a mean-minus-standard-deviation risk bound snaps the semantic direction to the nearest feasible sector. A particle filter with 200 particles triangulates focus rays from two frames into a world-frame 3D cue memory, requiring at least 0.5 m between poses. When the target is lost, the memory is reprojected with odometry, and the allowed deviation cone is adjusted by the memory uncertainty (p. 2-5 per the legacy card). The method assumes a static target and depends on pose, calibration, and odometry quality.

## Baselines and controls

NoMaD, NaviLLM, StreamVLN, EzReal, and GPT-4o-GeNie. GPT-4o-GeNie had a GPT-4o perception front end added by the authors, so it is not the unmodified official system. Ablations remove the 3D memory or the traversability grounding. All methods replay the same tasks.

## Platform and setup

- Simulation: two outdoor Unreal scenes built by the authors (Wild and Suburban), 100 start-goal pairs per scene, 3 random seeds, straight-line distances of 600-1000 m. Success requires reaching within 3 m of the goal with the goal not fully occluded.
- Real world: AgileX Scout Mini on two campus routes with 20 start points each, 40 episodes per method; a takeover counts as failure.
- Unitree Go1 demonstrates only qualitatively that the traversability threshold differs by platform (0.7 for the wheeled robot, 0.5 for the quadruped); it is not a second quantitative real-world setting (p. 7 per the legacy card).

## Evidence type and transfer

Closed-loop hardware runs on one wheeled robot over two routes, plus simulation with three seeds. The real-world evidence has no confidence intervals.

## Sensors

The Scout Mini carries a front stereo camera and a LiDAR. The method reads RGB and pose; the low-level LiDAR-inertial dependency remains. The camera and LiDAR models and the full 3D odometry configuration are not reported.

## Compute and latency

Inference runs on an external PC with an RTX 3090 GPU (p. 7). Qwen perception runs at 0.3-0.5 Hz, about 2.8 s per update (p. 7); fusion runs at 1 Hz and Scout low-level control at 50 Hz. The 50 Hz rate applies only to low-level tracking; near-field dynamic risk recognition is still limited by the 2-3 s VLM refresh. Power and Jetson performance are not reported.

## Key quantitative results

- Wild (SR / SPL): TARIC 41 +/- 4% / 0.35 +/- 0.03 versus EzReal 29 +/- 3% / 0.18 +/- 0.03 (Table I, image; no located page).
- Suburban: TARIC 50 +/- 5% / 0.40 +/- 0.03 versus EzReal 33 +/- 4% / 0.34 +/- 0.02 (Table I, image; no located page).
- Wild ablation SR: without 3D memory 30 +/- 4%, without traversability 36 +/- 4%, full 41 +/- 4% (no located page).
- Wild CFSR@50: full 52 +/- 5 versus EzReal 27.3 +/- 5.5. CFSR@D is computed only over failed episodes as the distance still progressed toward the goal after losing it; it is not a success probability over all tasks (no located page).
- Real world (Table III): route 1 SR 35% / SPL 0.28, route 2 45% / 0.36, combined 40.0% / 0.32 over 40 episodes, versus GPT-4o-GeNie 17.5% / 0.26, a 22.5-point SR gain; 60% of episodes still fail (p. 7).

## Stated limitations

- Unexpected interference from pedestrians or other moving agents occasionally forced manual takeovers, which count as failures (p. 8).
- According to the legacy card, the memory drifts when the goal is unobserved for more than 50 m without loop closure, and wet ground, shadows, and low curbs cause traversability misjudgments and detours (p. 8).

## Transfer conditions

Legacy reviewer observations:
- The interface of low-rate semantics, high-rate geometry, and world-frame memory is reusable, but wheeled-road thresholds, extrinsics, emergency stop, and dynamic obstacle avoidance need independent validation.
- The results do not show that safe control is solved: near-field risk depends on a VLM refreshed every 2-3 s.
- The method assumes static targets and good odometry and calibration.

## Code and data

The main text gives no download URL for the code or data of this method; public implementation, logs, and reproducibility were not verified. Open-source baselines do not stand in for the authors' release.

## Version family

EzReal, an earlier method of the same group, is cited and used as a baseline; it is a predecessor, and whether an exact sibling version exists was not checked. TARIC is counted once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Abstract, p. 1 | "Once such cues disappear, agents enter a cue-free phase and often degrade into backtracking, oscillatory headings, or aimless exploration." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. IV-B, p. 7 | "Inference runs on an external PC with an RTX 3090 GPU." |

## Page-cited excerpts

- **p. 7, Sec. IV-B Real-World Experiments.** "Inference runs on an external PC with an RTX 3090 GPU."
  VLM inference ran offboard on a desktop GPU.
- **p. 7, Sec. IV-B Real-World Experiments.** "combined SR of 40.0% over the 40 episodes."
  Combined real-world success rate over the 40 start points.
- **p. 8, Sec. V Limitations and Conclusions.** "unexpected interference from pedestrians or other moving agents occasionally forced us"
  Moving pedestrians occasionally caused manual takeovers.

## Survey-usable statements

### Supported

- On a wheeled robot over two campus routes, traversability-grounded headings with a world-frame cue memory raise real-world success from 17.5% (strongest baseline) to 40.0% over 40 episodes.
- In simulation, removing the 3D memory or the traversability grounding lowers Wild SR (30% and 36% versus 41%).

### Not supported

- Long-range outdoor VLN is solved: 60% of real episodes still fail.
- CFSR@D is a survival or success rate over all tasks: it is computed only over failed episodes.
- The Go1 runs are a quantitative quadruped evaluation: they are qualitative.
- The system handles near-field dynamic hazards at control rate: the VLM refreshes every 2-3 s and pedestrians caused takeovers.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-form card converted to the English template; no legacy quote dropped; Table I and ablation values have no located page (tables are images)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/67f8a95a440cfb9844a3d115/

## Original abstract

Outdoor vision-language navigation (VLN) in longrange, open-world environments is frequently disrupted by semantic-cue interruptions, where informative goal cues become sparse, occluded, or leave the field of view. Once such cues disappear, agents enter a cue-free phase and often degrade into backtracking, oscillatory headings, or aimless exploration. While memory-based methods attempt to bridge these gaps, they often fail under traversability-driven detours: the remembered cue direction may be infeasible, forcing detours that prolong cue-free phases and gradually render robot-centric cues stale and implicit histories blurred. This makes traversability a stability condition for maintaining goal-directed guidance, rather than merely a local safety concern. We propose a unified outdoor VLN framework that survives semantic-cue interruptions by maintaining traversabilityconsistent executable guidance throughout prolonged cue-free phases. Specifically, our method extracts semantic bearings from visibility-gated goal or exploration cues and grounds them into executable headings using a real-time near-field traversability profile, providing goal-consistent feasible guidance beyond reject-only safety filtering. To prevent guidance degradation during detours, we lift intermittent 2D evidence into a world-aligned 3D cue memory with an uncertainty-aware readout mechanism, ensuring guidance remains continuously reachable and stable as the robot moves. We evaluate the framework on quadrupedal and wheeled platforms over 600–1000 m routes. Our method improves simulation success rate by over 10 percentage points over the strongest baseline and achieves a real-world success rate of 40%, compared to 17.5% for the strongest baseline, with substantially higher robustness during prolonged cue-free intervals.
