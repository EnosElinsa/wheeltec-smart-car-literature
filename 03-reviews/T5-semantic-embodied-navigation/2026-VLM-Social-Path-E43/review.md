# From Obstacles to Etiquette: Robot Social Navigation With VLM-Informed Path Selection

## Metadata

| Field | Value |
|---|---|
| ID | E43 |
| Title | From Obstacles to Etiquette: Robot Social Navigation With VLM-Informed Path Selection |
| Authors | Zilin Fang, Anxing Xiao, David Hsu, and Gim Hee Lee |
| Venue | IEEE Robotics and Automation Letters, vol. 11, no. 4, pp. 3947-3954 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3662586](https://doi.org/10.1109/lra.2026.3662586) |
| Official URL | https://ieeexplore.ieee.org/document/11373887/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2026-VLM-Social-Path-E43/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2026-VLM-Social-Path-E43/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2026-VLM-Social-Path-E43/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: offboard-compute, scripted-scenario, few-trials
- platform_class: legged
- platform: Boston Dynamics Spot
- boundary_platform: yes
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: ELP fisheye RGB camera, Hesai JT16 mechanical LiDAR, Spot native odometry
- compute: Jetson Orin onboard for navigation excluding the VLM; fine-tuned Qwen2.5-VL-7B served on an H100; end-to-end latency not reported
- compute_location: mixed
- summary_result: Over four staged Spot scenarios with 3 trials per method, the method has zero social-zone intrusion in all four and personal-space violation 0 s in three (0.33 s queueing).
- summary_limitation: The authors list three failure types: no memory beyond the current frame, ambiguous intent in concurrent activities, and post-processing that may exclude the ideal path.
- survey_included: yes
- verification_level: light

## Problem

In low- to medium-density crowds, a geometrically collision-free path can still interrupt people taking photos, talking, queueing, or working on a ladder. The paper asks how to add situational etiquette to local path selection.

## Mechanism

YOLOv10 and ByteTrack fuse LiDAR depth and odometry into human tracks, and a neural Markov random field predicts 20 human trajectories over 2.4 s, which are fused into the costmap. A* with Poisson-style anchor sampling generates detours, and Hausdorff clustering keeps 3-6 candidates. The candidates are projected onto the RGB image, and a fine-tuned Qwen2.5-VL-7B selects one. The output is only a reference: when the low-rate model answer arrives, the nearest current candidate is taken, and a modified ORCA produces velocities and avoids obstacles (p. 3-6 per the legacy card). The legacy card notes that this propose-and-select split depends on the candidates covering a suitable option, which is not guaranteed in every scene.

## Baselines and controls

G-MPC, AttnGraph-RL, ViNT, VLM-Social-Nav, and GSON. VLM-Social-Nav planning was reproduced from its paper, but its perception was replaced by this paper's perception. An ablation of candidate generation runs offline with ground-truth human positions and groups (10 scenes, 50 runs per horizon); it is not an additional hardware success trial (p. 6-7 per the legacy card).

## Platform and setup

- Training data: SCAND point clouds lack camera extrinsics, so the training data use an approximate calibration with GPT-4o labels; 4851 training and 574 validation image-choice pairs; full fine-tuning on 2 H100 GPUs and 4-bit vLLM deployment (p. 5).
- Hardware: Boston Dynamics Spot in four controlled scenarios (wall-washing ladder, walking and talking, photography, queueing), 3 trials per method and scenario. People played the situations from preset positions and orientations (p. 6).
- No autonomous simulation navigation results.

## Evidence type and transfer

Closed-loop hardware on a legged robot in staged scenarios with three trials each. No wheeled-robot hardware test.

## Sensors

ELP fisheye RGB camera and Hesai JT16 mechanical LiDAR, with Spot's native odometry (p. 6).

## Compute and latency

Jetson Orin runs the onboard navigation processing, excluding the VLM; the Qwen model is served from an H100 (p. 6). Training hours, inference latency, and model refresh rate are not reported, and the "real-time" statement lacks an end-to-end latency table (legacy card).

## Key quantitative results

- Navigation time NT (s) for the method in ladder, walking-and-talking, photography, and queueing scenarios: 28.48 / 28.49 / 40.15 / 26.14 (Table I, image; no located page).
- SIT and Max. SIR are 0 in all four scenarios; PSV is 0 / 0 / 0 / 0.33 s; TFP is 0 / 1.80 / 4.32 / 2.70 s (Table I, image; no located page).
- Counterexamples to "best everywhere": photography NT 40.15 s is slower than VLM-Social-Nav 27.01 s; walking-and-talking TFP 1.80 s is higher than AttnGraph-RL 1.66 s; queueing TFP 2.70 s is higher than GSON 2.36 s (Table I, image; no located page).
- Some ViNT, AttnGraph-RL, and VLM-Social-Nav NT entries marked with an asterisk are 90 s timeouts, not normal arrival times. Values are means of 3 trials without variance, confidence intervals, or a significance test (Table I, image; no located page).

## Stated limitations

- The method uses only the current frame without memory, so it fails, for example, when a long queue leaves the view (p. 7 per the legacy card).
- Intent is ambiguous when activities happen concurrently (p. 7 per the legacy card).
- Post-processing may exclude the ideal path (p. 7).

## Transfer conditions

Legacy reviewer observations:
- PSV uses a 0.25 m human-distance threshold, TFP counts only a 30-degree cone within 3 m, and SIR uses Spot's 0.5 x 1.1 m footprint; a wheeled robot needs its own footprint and dynamics.
- The costmap, trajectory-prediction, and candidate-selection interfaces are portable; ORCA suits an omnidirectional base, but a differential-drive base must respect nonholonomic constraints.
- Zero social-zone intrusion holds for these 12 staged trials per method only; it is not a collision-free guarantee or a standard for all crowds. No subjective user study, unconstrained crowds, or high density were tested. The metrics are operational definitions of robot paths, not inferences about human mental states.

## Code and data

Project page https://path-etiquette.github.io/ (p. 1). Availability of weights, code, and logs, and their reproducibility, were not verified.

## Version family

The RA-L paper and its project page are counted once. VL-TGS, which the paper cites, is a different earlier work and is not merged with this one despite the similar propose-and-select design.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | partial-support | moderate | Sec. V-A, p. 6 | "onboard navigation processing, excluding the VLM." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. V-B, p. 6 | "with 3 trials per scenario:" |

## Page-cited excerpts

- **p. 6, Sec. V-A Platform Description.** "onboard navigation processing, excluding the VLM."
  The Orin does not run the VLM.
- **p. 6, Sec. V-B Experimental Setup.** "with 3 trials per scenario:"
  Each method has only three trials per scenario.
- **p. 7, Sec. VI Conclusion and Limitation.** "post-processing may exclude the ideal path"
  Candidate post-processing can remove the ideal path.

## Survey-usable statements

### Supported

- In four staged scenarios on Spot, VLM selection among geometrically feasible candidate paths avoided social-zone intrusion in all trials and gave the lowest personal-space violation overall.
- A fine-tuned 7B VLM can act as a low-rate path selector above a geometric planner and ORCA, with the VLM served offboard.

### Not supported

- The method is best on every metric: it is slower in photography and has higher TFP in walking-and-talking and queueing than one baseline each.
- The full VLM runs onboard the Jetson Orin: it is served from an H100.
- The results are statistically established: 3 trials per method and scenario without variance.
- The method is validated on wheeled robots: only Spot was tested.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-form card converted to the English template; no legacy quote dropped; Table I values have no located page (table is an image)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/e037608d354a3874c82dd452/

## Original abstract

Navigating socially in human environments requires more than satisfying geometric constraints, as collision-free paths may still interfere with ongoing activities or conflict with social norms. Addressing this challenge calls for analyzing interactions between agents and incorporating common-sense reasoning into planning. This paper presents a social robot navigation framework that integrates geometric planning with contextual social reasoning. The system first extracts obstacles and human dynamics to generate geometrically feasible candidate paths, then leverages a fine-tuned vision-language model (VLM) to evaluate these paths, informed by contextually grounded social expectations, selecting a socially optimized path for the controller. This task-specific VLM distills social reasoning from large foundation models into a smaller and efficient model, allowing the framework to perform real-time adaptation in diverse human–robot interaction contexts. Experiments in four social navigation contexts demonstrate that our method achieves the best overall performance with the lowest personal space violation duration, the minimal pedestrian-facing time, and no social zone intrusions.
