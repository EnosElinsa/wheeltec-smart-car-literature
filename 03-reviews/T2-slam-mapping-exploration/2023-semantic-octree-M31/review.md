# Semantic OcTree Mapping and Shannon Mutual Information Computation for Robot Exploration

## Metadata

| Field | Value |
|---|---|
| ID | M31 |
| Title | Semantic OcTree Mapping and Shannon Mutual Information Computation for Robot Exploration |
| Authors | Arash Asgharivaskasi and Nikolay Atanasov |
| Venue | IEEE Transactions on Robotics, vol. 39, no. 3, pp. 1910-1928 |
| Year | 2023 |
| Type | journal |
| DOI | [10.1109/tro.2023.3245986](https://doi.org/10.1109/tro.2023.3245986) |
| Official URL | https://ieeexplore.ieee.org/document/10057106/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T2-slam-mapping-exploration/2023-semantic-octree-M31/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2023-semantic-octree-M31/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2023-semantic-octree-M31/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: localization-mapping, semantic-language-navigation
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, online-hardware, simulation
- protocol_caveats: video-only-hardware
- platform_class: wheeled-unspecified
- platform: unnamed ground wheeled robot with NVIDIA Xavier NX (indoor autonomous exploration); Clearpath Husky (outdoor joystick mapping and Unity simulation)
- boundary_platform: no
- degradation: none
- degradation_observed: model-error
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: Hokuyo UST-10LX 2D LiDAR and Intel RealSense D435i RGB-D (indoor); Ouster OS1-32 3D LiDAR and Intel RealSense D455 (outdoor)
- compute: NVIDIA Xavier NX onboard, segmentation at 9.8 FPS and OctoMap publishing every 0.34 s (indoor); onboard OctoMap update every 0.12 s (outdoor)
- compute_location: onboard
- summary_result: On an indoor Xavier NX wheeled robot, SSMI explored an office over 20 iterations against frontier-based exploration, with segmentation at 9.8 FPS and map publishing every 0.34 s.
- summary_limitation: The authors report that depth noise and classification error in the real office forced revisits and left few safe candidate trajectories; onboard compute limited the camera to 15 Hz.
- survey_included: yes
- verification_level: light

## Problem

The paper addresses active 3D mapping of unstructured, unknown environments
from streaming range and semantic category observations. Mutual information
over binary occupancy ignores the uncertainty of semantic classes. Naive 3D
grids waste memory and make information evaluation over many candidate
trajectories too slow.

## Mechanism

Semantic Shannon mutual information (SSMI) stores a Bayesian categorical
distribution per octree voxel. Updates use octree ray tracing and leaf
merging. A closed-form lower bound of the Shannon mutual information between
the multiclass OctoMap and range-category rays is computed with semantic
run-length encoding. Candidate trajectories are scored by information
against motion cost. Range and class measurements and the pose kinematics
are kept general (ground or aerial robots; camera or LiDAR). Segmentation is
a conventional CNN (FCHarDNet trained on RUGD outdoors; ResNet18 trained on
SUN RGB-D indoors), not a vision-language model.

## Baselines and controls

Simulation compares SSMI with 3D FSMI and TARE. The indoor real-world test
compares SSMI with frontier-based exploration.

## Platform and setup

Simulation used a photorealistic Unity environment with a Husky carrying an
RGB-D sensor, noisy range, and classes with 0.95 accuracy. Outdoors, a
Clearpath Husky with an Ouster OS1-32 and an Intel RealSense D455 ran ROS
and ICP LiDAR localization over about six acres of forested area, driven by
joystick. Indoors, an unnamed ground wheeled robot with an NVIDIA Xavier NX,
a Hokuyo UST-10LX, and a RealSense D435i (15 Hz, 640 × 480) explored an
office autonomously for 20 exploration iterations.

## Evidence type and transfer

The closed-loop evidence is the indoor office exploration on the unnamed
wheeled robot; the paper reports it in plots (Fig. 19). The outdoor Husky
run is onboard mapping under joystick control, not autonomous exploration.
Comparisons against FSMI and TARE are simulation only. The drive type of the
indoor robot is not given in the text found.

## Sensors

Outdoors: Ouster OS1-32 3D LiDAR and RealSense D455 RGB-D. Indoors: Hokuyo
UST-10LX 2D LiDAR and RealSense D435i RGB-D. Localization uses ICP scan
matching.

## Compute and latency

Indoors, all processing ran on the Xavier NX: ResNet18 segmentation with
TensorRT at 9.8 frames per second and semantic OctoMap publishing every
0.34 s. The camera ran at 15 Hz because of limited onboard compute.
Outdoors, the semantic OctoMap was updated every 0.12 s with all computation
on the robot.

## Key quantitative results

- Simulated class accuracy: 0.95 (p. 12).
- Outdoor onboard OctoMap update: every 0.12 s on average, over an approximately six-acre forested area (p. 14).
- Indoor segmentation: 9.8 frames per second on Xavier NX (p. 15).
- Indoor semantic OctoMap publishing: every 0.34 s on average (p. 15).
- Indoor camera rate reduced to 15 Hz due to limited onboard compute (p. 15).

## Stated limitations

- Large depth measurement noise and classification error in the real experiments require revisiting explored areas and leave a small number of safe candidate trajectories (p. 15).
- Limited computational power on the mobile platform forced a lower camera frame rate of 15 Hz (p. 15).

## Transfer conditions

The method needs range plus semantic segmentation, a pose source (ICP scan
matching in the real tests), and a GPU-class embedded computer for
segmentation. The outdoor run was teleoperated. The conclusion claims
efficient exploration under domain shift between classifier training data
and the test scene; the legacy extraction notes that this effect is not
quantified separately in the office trial.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. VII-G, p. 15 | "large depth measurement noise and classification error in the real-world experiments result in 1) the need for revisiting explored areas in order to estimate an accurate map" |
| C3 | direct-support | weak | Sec. VII-G, p. 15 | "Due to limited computational power available on the mobile platform" |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VII-F, p. 14 | "The robot was manually controlled via joystick" |

## Page-cited excerpts

- **p. 15, Sec. VII-G.** "large depth measurement noise and classification error in the real-world experiments result in 1) the need for revisiting explored areas in order to estimate an accurate map"
  Real sensing and classification errors reduce exploration efficiency.
- **p. 15, Sec. VII-G.** "Due to limited computational power available on the mobile platform"
  The start of the sentence that explains the reduced 15 Hz camera rate.
- **p. 14, Sec. VII-F.** "The robot was manually controlled via joystick"
  The outdoor Husky run is teleoperated mapping.
- **p. 16, Sec. VIII.** "Experiments in both simulated and real-world environments showed the scalability of SSMI for large-scale 3-D exploration scenarios."
  The authors' summary claim; the large-scale real run is the joystick-driven outdoor mapping.

## Survey-usable statements

### Supported

- Semantic octree mapping with a Shannon mutual information bound ran fully onboard an Xavier NX wheeled robot for autonomous indoor exploration (numbers from a light review; re-check before citing).
- Depth noise and classification error on real hardware forced revisits during semantic exploration.

### Not supported

- SSMI explored a large outdoor area autonomously: the outdoor run was driven by joystick.
- The benefit under classifier domain shift is quantified on hardware: the legacy extraction notes that it is not quantified separately.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); the legacy card had no verbatim quotes, so excerpts were taken from the conclusion and from Sec. VII sentences located with --find; reviewer remarks moved from Stated limitations to Evidence type and Transfer conditions
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Autonomous robot operation in unstructured and unknown environments requires efficient techniques for mapping and exploration using streaming range and visual observations. Information-based exploration techniques, such as Cauchy–Schwarz quadratic mutual information and fast Shannon mutual information, have successfully achieved active binary occupancy mapping with range measurements. However, as we envision robots performing complex tasks specified with semantically meaningful concepts, it is necessary to capture semantics in the measurements, map representation, and exploration objective. This work presents semantic octree mapping and Shannon mutual information computation for robot exploration. We develop a Bayesian multiclass mapping algorithm based on an octree data structure, where each voxel maintains a categorical distribution over semantic classes. We derive a closed-form efficiently computable lower bound of the Shannon mutual information between a multiclass octomap and a set of range-category measurements using semantic run-length encoding of the sensor rays. The bound allows rapid evaluation of many potential robot trajectories for autonomous exploration and mapping. We compare our method against state-of-the-art exploration techniques and apply it in a variety of simulated and real-world experiments.
