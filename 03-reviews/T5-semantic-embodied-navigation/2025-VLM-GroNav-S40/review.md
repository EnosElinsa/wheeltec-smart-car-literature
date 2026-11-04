# VLM-GroNav: Robot Navigation Using Physically Grounded Vision-Language Models in Outdoor Environments

## Metadata

| Field | Value |
|---|---|
| ID | S40 |
| Title | VLM-GroNav: Robot Navigation Using Physically Grounded Vision-Language Models in Outdoor Environments |
| Authors | Elnoor, Mohamed and Weerakoon, Kasun and Seneviratne, Gershom and Xian, Ruiqi and Guan, Tianrui and M Jaffar, Mohamed Khalid and Rajagopal, Vignesh and Manocha, Dinesh |
| Venue | 2025 IEEE International Conference on Robotics and Automation (ICRA) |
| Year | 2025 |
| Type | conference |
| DOI | [10.1109/icra55743.2025.11128264](https://doi.org/10.1109/icra55743.2025.11128264) |
| Official URL | https://ieeexplore.ieee.org/document/11128264/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-VLM-GroNav-S40/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-VLM-GroNav-S40/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2025-VLM-GroNav-S40/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: cloud-model
- platform_class: skid-steer
- platform: Clearpath Husky and Ghost Vision60 on deformable/slippery outdoor terrain (pp. 3, 5).
- boundary_platform: no
- degradation: terrain, wheel-slip
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: RGB, 3D LiDAR, IMU, GPS, aerial imagery; wheel odometry for wheeled proprioception
- compute: GPT-4o API reasoning/global planning and local CLIP/DWA; Husky laptop i9/RTX2080, legged onboard NUC11 (pp. 4-5).
- compute_location: mixed
- summary_result: Physical feedback updates semantic terrain costs during outdoor navigation.
- summary_limitation: Accurate GPS, visibility and VLM processing remain constraints; alternative sensing and faster inference are future work (p. 6).
- survey_included: yes
- verification_level: light

## Problem

Appearance alone does not establish terrain deformability or slipperiness.

## Mechanism

Builds in-context exemplars from time-aligned visual/proprioceptive feedback, revises global waypoints and adds frontier traversability cost to DWA (pp. 4-5).

## Baselines and controls

DWA, GA-Nav, CoNVOI and ViNT in outdoor task comparisons (p. 5).

## Platform and setup

Clearpath Husky and Ghost Vision60 on deformable/slippery outdoor terrain (pp. 3, 5).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Grounding a semantic estimate in interaction data is not a calibrated friction or collision-risk guarantee.

## Sensors

RGB, 3D LiDAR, IMU, GPS, aerial imagery; wheel odometry for wheeled proprioception.

## Compute and latency

GPT-4o API reasoning/global planning and local CLIP/DWA; Husky laptop i9/RTX2080, legged onboard NUC11 (pp. 4-5).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Accurate GPS, visibility and VLM processing remain constraints; alternative sensing and faster inference are future work (p. 6).

## Transfer conditions

Grounding a semantic estimate in interaction data is not a calibrated friction or collision-risk guarantee.

## Code and data

Availability statements and external repositories were not independently checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity. No separate preprint or conference version is added to the corpus.

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

- **p. 6, Selected source passage.** "VLM-GroNav relies on accurate GPS for global localization"
  Connects language models to terrain consequences while retaining GPS, cloud and response-time dependencies.

## Survey-usable statements

### Supported

- Physical feedback updates semantic terrain costs during outdoor navigation. Connects language models to terrain consequences while retaining GPS, cloud and response-time dependencies.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Grounding a semantic estimate in interaction data is not a calibrated friction or collision-risk guarantee.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 4, 5, 6; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

We present a novel autonomous robot navigation algorithm for outdoor environments that is capable of handling diverse terrain traversability conditions. Our approach, VLM-GroNav, uses vision-language models (VLMs) and integrates them with physical grounding that is used to assess intrinsic terrain properties such as deformability and slipperiness. We use proprioceptive-based sensing, which provides direct measurements of these physical properties, and enhances the overall semantic understanding of the terrains. Our formulation uses in-context learning to ground the VLM's semantic understanding with proprioceptive data to allow dynamic updates of traversability estimates based on the robot's real-time physical interactions with the environment. We use the updated traversability estimations to inform both the local and global planners for real-time trajectory replanning. We validate our method on a legged robot (Ghost Vision 60) and a wheeled robot (Clearpath Husky), in diverse real-world outdoor environments with different deformable and slippery terrains. In practice, we observe significant improvements over state-of-the-art methods by up to 50% increase in navigation success rate.
