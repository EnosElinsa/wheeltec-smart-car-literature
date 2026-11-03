# SysNav: Multi-Level Systematic Cooperation Enables Real-World, Cross-Embodiment Object Navigation

## Metadata

| Field | Value |
|---|---|
| ID | E41 |
| Title | SysNav: Multi-Level Systematic Cooperation Enables Real-World, Cross-Embodiment Object Navigation |
| Authors | Haokun Zhu, Zongtai Li, Zihan Liu, Kevin Guo, Zhengzhi Lin, Yuxin Cai, Guofei Chen, Chen Lv, Wenshan Wang, Jean Oh, and Ji Zhang |
| Venue | IEEE Robotics and Automation Letters, vol. 11, no. 9, pp. 10577-10584 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3713730](https://doi.org/10.1109/lra.2026.3713730) |
| Official URL | https://ieeexplore.ieee.org/document/11610867/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2026-SysNav-E41/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2026-SysNav-E41/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2026-SysNav-E41/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: cloud-model
- platform_class: omnidirectional
- platform: custom Mecanum-wheeled robot (quantitative trials); Unitree Go2 quadruped and Unitree G1 humanoid (qualitative trials only)
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Livox Mid-360 LiDAR, Ricoh Theta Z1 panoramic camera
- compute: laptop with i9-14900HX CPU and RTX 4090 GPU; Gemini-2.5-flash queries average 1.15 s
- compute_location: mixed
- summary_result: Real-world hard ObjectNav on the Mecanum robot: SR 98.3% versus 37.2% for InstructNav and 25.6% for VLFM, under shared sensing and low-level stack.
- summary_limitation: The authors state that SysNav targets structured indoor environments and relies on room-level structure, so it may fail outdoors.
- survey_included: yes
- verification_level: light

## Problem

Object navigation in unknown real indoor environments, including targets with color, state, and object-relation constraints, needs semantic reasoning, long-horizon planning, and motion control at once. The paper asks how to divide these roles between a vision-language model (VLM), a planner, and embodiment-specific low-level control.

## Mechanism

SysNav builds an online three-level graph of rooms, viewpoints, and objects, with connection, containment, visibility, and on-demand relation edges. Rooms are segmented from wall planes fitted to LiDAR data, objects come from YOLO-World and SAM, and the VLM judges attributes and relations on demand. Gemini-2.5-flash only decides whether to stop exploring the current room early and which room to visit next. Inside a room, a TARE-style exploration with coverage-gain sampling and local and global TSP plans the viewpoints. Embodiment-specific low-level autonomy stacks handle obstacle avoidance, traversability, and waypoint following (p. 3-5 per the legacy card). The VLM does not command velocities directly.

## Baselines and controls

VLFM and InstructNav were re-implemented by the authors with the same point cloud and panoramic inputs and the same low-level stack as SysNav (p. 7). Simulation comparisons include ApexNav, MTU3D, and VLFM.

## Platform and setup

- Real world: 190 episodes, of which 78 are qualitative and 112 quantitative; not all 190 are comparison trials (p. 5).
- Qualitative episodes span 15 scenes: 4 floor-scale episodes, 41 on the wheeled robot, 19 on Go2, and 14 on G1. The legacy card notes that 4 + 41 + 19 + 14 = 78 and that the floor-scale episodes are listed separately, so they should not be assigned to the wheeled robot. The floor-scale episodes average 1007.21 m² and a shortest geodesic distance of 84.43 m (p. 6).
- Quantitative episodes use only the Mecanum-wheeled robot, three difficulty levels and 10 target classes: easy 24, medium 40, hard 48 episodes, with timeouts of 3, 4, and 4 minutes.
- Simulation: 8,195 episodes on four benchmarks (HM3D-v1, HM3D-v2, MP3D, HM3D-OVON) with 640 x 480 RGB-D converted to point clouds and discrete 25 cm / 30 degree actions, which differ from the continuous velocities of the real robots (p. 5).

## Evidence type and transfer

The quantitative real-world comparison is closed-loop on one Mecanum-wheeled robot. Go2 and G1 appear only in qualitative episodes. Simulation results use discrete actions and do not show real-world transfer by themselves.

## Sensors

Each embodiment carries a Livox Mid-360 LiDAR and a Ricoh Theta Z1 panoramic camera; on Go2 and G1 the built-in LiDAR also serves motion control (p. 5).

## Compute and latency

SysNav runs on a laptop with an i9-14900HX CPU and an RTX 4090 GPU (p. 5). Gemini queries average 1.15 s at 6.4 queries per minute (p. 7). The legacy card states that the total API network budget, the policy under network loss, and the overall CPU and GPU load are not reported. It does not record whether the laptop rides on the robot.

## Key quantitative results

- Real-world easy (SR % / SPT % / mean time of successful episodes in s): SysNav 100 / 83.8 / 29.1 versus VLFM 58.3 / 40.3 / 52.1 (Table II, image; no located page).
- Real-world medium: SysNav 97.5 / 67.9 / 72.8 versus InstructNav 55 / 27.8 / 84.6 (Table II, image; no located page).
- Real-world hard: SysNav 98.3 / 71.8 / 67.6 versus InstructNav 37.2 / 20.7 / 103.4 and VLFM 25.6 / 12.9 / 97.4; SR is 61.1 points above the best baseline, and the time is 29.8 s below the fastest baseline (VLFM), counted over successful episodes only (Table II, image; no located page).
- The legacy card notes that 98.3% of 48 hard episodes is not a whole-number ratio; the number of repetitions and the aggregation denominator are unclear, so success counts should not be back-computed.
- Simulation (SR / SPL): HM3D-v1 63.7 / 30.5, HM3D-v2 80.8 / 37.2, MP3D 50.7 / 18.1, HM3D-OVON 54.9 / 26.1 (Table I, image; no located page).
- ApexNav reaches 59.6 / 33.0 on HM3D-v1 and 76.2 / 38.0 on HM3D-v2, so SysNav has higher SR but lower SPL on these two benchmarks. On HM3D-OVON, SR is 14.1 points above MTU3D (40.8) and SPL 6.5 points above VLFM (19.6) (Table I, image; no located page).
- Gemini queries: mean 1.15 s, 6.4 queries per minute (p. 7).

## Stated limitations

- SysNav targets structured indoor environments and relies on room-level structure, so the authors expect it may fail outdoors (p. 7).

## Transfer conditions

Legacy reviewer observations:
- The room-level semantics and the low-level ROS autonomy stack can be reused on a Mecanum robot, but they need a 3D point cloud and a 360-degree camera; a 2D laser scanner or a plain USB camera is not shown to be equivalent.
- The evidence uses an RTX 4090 laptop and a cloud VLM; there is no Jetson-class evidence.
- The success distance threshold is defined symbolically but its value is not given in the main text; collision rate, confidence intervals, random seeds, and API cost are not reported.
- Room mis-segmentation and semantic hallucination have no separate failure statistics or ablation.

## Code and data

Project page https://cmu-vln.github.io/ (p. 1, 7) and chassis autonomy stack https://github.com/jizhang-cmu/autonomy_stack_mecanum_wheel_platform (p. 8). The completeness of the released code and logs and their reproducibility were not verified.

## Version family

The RA-L paper is counted once. The paper cites the same group's STRIVE preprint; the legacy card did not treat it as a version of this work, and the lineage was not checked further.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VI, p. 7 | "Limitation: SysNav targets structured indoor environments and relies on room-level structure for" |

## Page-cited excerpts

- **p. 5, Sec. V-A Experiment Setup.** "In real-world, we conduct 190 episodes,"
  The 190 real episodes include 78 qualitative and 112 quantitative ones.
- **p. 5, Sec. V-A Experiment Setup.** "SysNav runs on a laptop with an i9-14900HX CPU and an RTX-4090"
  Laptop-class GPU compute; no Jetson evidence.
- **p. 7, Sec. V-C Quantitative Results in Real-World.** "all baselines share the same point cloud and panoramic inputs and low-level"
  VLFM and InstructNav were re-implemented on the same sensing and low-level stack.
- **p. 7, Sec. VI Conclusion.** "Limitation: SysNav targets structured indoor environments and relies on room-level structure for"
  The system depends on indoor room structure.

## Survey-usable statements

### Supported

- On one Mecanum-wheeled robot with a shared sensing and low-level stack, room-level VLM guidance with in-room geometric exploration reaches higher real-world ObjectNav success than re-implemented VLFM and InstructNav at all three difficulty levels.
- Restricting VLM calls to room-level decisions keeps query latency (mean 1.15 s) out of the motion loop.

### Not supported

- SysNav outperforms all baselines on every metric: ApexNav has higher SPL on HM3D-v1 and HM3D-v2.
- All 190 real episodes are comparison trials: 78 are qualitative.
- The quadruped and humanoid results are quantitative: Go2 and G1 appear only in qualitative episodes.
- The system works outdoors or in unstructured spaces: the authors state that it relies on room-level structure.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-form card converted to the English template; the legacy p. 5 quote "including 78 episodes ... 112 episodes for quantitative evaluation." was replaced by "In real-world, we conduct 190 episodes," because the PDF text layer drops the word spaces; Table I and II values have no located page (tables are images)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/d3266440b9dd1c34b93f5542/

## Original abstract

Object navigation (ObjectNav) in real-world environments is a complex problem that requires simultaneously addressing multiple challenges, including spatial structure complexity, long-horizon planning and semantic understanding. Recent advances in Vision-Language Models (VLMs) offer promising capabilities for semantic understanding, yet effectively integrating them into real-world navigation systems remains a non-trivial challenge. In this work, we formulate real-world ObjectNav as a system-level problem and introduce SysNav, a three-level Object-Nav system designed for real-world cross-embodiment deployment. SysNav decouples semantic reasoning, navigation planning and motion control to ensure robustness and generalizability. At the high-level, we summarize the environment into a structured scene representation and leverage VLMs to provide semantic-grounded navigation guidance. At the mid-level, we introduce a hierarchical room-based navigation strategy that reserves VLM guidance for room-level decisions, which effectively utilizes its reasoning ability while ensuring system efficiency. At the low-level, planned waypoints are executed through different embodiment-specific motion control modules. We deploy our system on three embodiments, a custom-built wheeled robot, the Unitree Go2 quadruped and the Unitree G1 humanoid, and conduct 190 real-world experiments. Our system achieves substantial improvements in both success rate and navigation efficiency. To the best of our knowledge, SysNav is the first system capable of reliably and efficiently completing floor-scale long-range object navigation in complex real-world environments. Furthermore, extensive experiments on four simulation benchmarks demonstrate state-of-the-art performance.
