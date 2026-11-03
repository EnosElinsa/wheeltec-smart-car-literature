# GA-Nav: Efficient Terrain Segmentation for Robot Navigation in Unstructured Outdoor Environments

## Metadata

| Field | Value |
|---|---|
| ID | M40 |
| Title | GA-Nav: Efficient Terrain Segmentation for Robot Navigation in Unstructured Outdoor Environments |
| Authors | Tianrui Guan, Divya Kothandaraman, Rohan Chandra, Adarsh Jagan Sathyamoorthy, Kasun Weerakoon, and Dinesh Manocha |
| Venue | IEEE Robotics and Automation Letters, vol. 7, no. 3, pp. 8138-8145 |
| Year | 2022 |
| Type | journal |
| DOI | [10.1109/lra.2022.3187278](https://doi.org/10.1109/lra.2022.3187278) |
| Official URL | https://ieeexplore.ieee.org/document/9810192/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T2-slam-mapping-exploration/2022-GA-Nav-M40/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2022-GA-Nav-M40/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2022-GA-Nav-M40/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, dataset-playback
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Clearpath Jackal and Clearpath Husky (no drive type found in the text)
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: Intel RealSense RGB camera (70-degree field of view); Velodyne 3D LiDAR for localization and elevation map
- compute: Alienware laptop (Intel i9, NVIDIA RTX 2080) mounted on the robot
- compute_location: onboard
- summary_result: Average mIoU gains of 13.47% on RUGD and 10.54% on RELLIS-3D; on Jackal and Husky, off-road success 71% versus 62% for TERP (Table V).
- summary_limitation: The authors state that the work focuses on perception, that labels must be correct and consistent, and that drastic elevation changes and extreme weather remain open.
- survey_included: yes
- verification_level: light

## Problem

The paper identifies safe, navigable terrain in unstructured outdoor scenes
from RGB images. Terrain classes look alike and have weak boundaries (water
versus puddle, grass versus dirt). Fine-grained segmentation is
computationally heavy and more detailed than navigation needs, and
mislabeling forbidden regions is unsafe. Elevation-only planners cannot tell
apart surfaces of similar height.

## Mechanism

GA-Nav is a group-wise attention segmentation head. It extracts multi-scale
features per terrain group and predicts coarse navigability classes (smooth,
rough, bumpy, forbidden, obstacle, background) at reduced spatial
resolution. The group-attention loss can be attached to standard backbones.
The segmentation is projected by homography into a cost map and added to the
point-cloud elevation cost of TERP, which plans least-cost outdoor
trajectories. This is CNN- and transformer-style segmentation combined with
an existing learning-based planner, not a vision-language model.

## Baselines and controls

Segmentation is compared with prior segmentation networks on RUGD and
RELLIS-3D. Navigation is compared with DWA, TERP, and planners based on
OCRNet and SegFormer.

## Platform and setup

Dataset benchmarks used RUGD and RELLIS-3D. Real navigation used a Clearpath
Jackal and a Clearpath Husky with an Intel RealSense camera (70-degree field
of view), a Velodyne 3D LiDAR for localization and elevation mapping, and an
Alienware laptop (Intel i9, RTX 2080) mounted on the robot. Trials covered a
campus walkway, a trail, a dirt road, and off-road terrain, with at least 10
trials each according to the legacy extraction.

## Evidence type and transfer

Segmentation accuracy comes from public off-road datasets. Navigation
success comes from closed-loop runs on two robots, reported per terrain type
(Table V). The authors' sentence that the work "focuses on perception"
conflicts with the reported navigation trials; the legacy extraction reads it
as an awkward self-limitation, not as absence of trials.

## Sensors

The method uses an RGB camera (Intel RealSense). A Velodyne 3D LiDAR
provides localization and the elevation map used by TERP.

## Compute and latency

GA-Nav ran on an Alienware laptop with an Intel i9 CPU and an NVIDIA RTX 2080
GPU mounted on the robot, not on a small single-board computer. Inference
timing is not recorded in the legacy extraction; not verified.

## Key quantitative results

- RUGD: average mIoU improvement of 13.47% over prior segmentation methods (p. 6).
- RELLIS-3D: average mIoU improvement of 10.54% (p. 6).
- Off-road success rate: GA-Nav 71% versus TERP 62% (Table V).
- Dirt road: trajectory selection 2% worse than TERP, attributed to drastic elevation changes with less terrain diversity (p. 7).
- Camera field of view: 70 degrees (p. 7).

## Stated limitations

- The current work focuses on perception and integrates with a learning-based planner for real-world scenarios instead of navigation (p. 8).
- The data must be labeled correctly and consistently (p. 8).
- More navigation metrics are needed, and drastic elevation changes and extreme weather conditions remain to be handled (p. 8).

## Transfer conditions

The method needs an RGB camera, a 3D LiDAR for localization and elevation,
consistent terrain labels, and a laptop-class GPU on the robot. Where
elevation dominates (the dirt road), the segmentation adds little over the
elevation-based TERP.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | weak | Sec. V, p. 8 | "like drastic elevation changes and extreme whether conditions" |
| C3 | direct-support | moderate | Sec. V, p. 8 | "In addition, we need to make sure that the data is labeled correctly and consistently." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. V, p. 8 | "Our approach has some limitations. For example, our current work focuses on perception and integrates with a learning-based planner implementation for real-world scenarios instead of navigation." |

## Page-cited excerpts

- **p. 8, Sec. V.** "Our approach has some limitations. For example, our current work focuses on perception and integrates with a learning-based planner implementation for real-world scenarios instead of navigation."
  The authors' own scope limit; it contains the legacy quote.
- **p. 8, Sec. V.** "In addition, we need to make sure that the data is labeled correctly and consistently."
  Learned segmentation depends on label quality.
- **p. 8, Sec. V.** "like drastic elevation changes and extreme whether conditions"
  Open off-road conditions; "whether" is the paper's spelling.

## Survey-usable statements

### Supported

- Coarse group-wise terrain segmentation added to an elevation-based planner raised off-road success on Jackal and Husky from 62% (TERP) to 71% (numbers from a light review; re-check before citing).
- Navigation results are reported per terrain type (walkway, trail, dirt road, off-road).

### Not supported

- GA-Nav selects better trajectories on every terrain: on the dirt road it is 2% worse than TERP.
- GA-Nav handles extreme weather or drastic elevation changes: the authors list both as open.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); the one legacy quote was found and kept inside a longer conclusion excerpt; other excerpts taken from the conclusion; Table V success values not located on a page
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

We propose GA-Nav, a novel group-wise attention mechanism to identify safe and navigable regions in unstructured environments from RGB images. Our group-wise attention method extracts multi-scale features from each type of terrain independently and classifies terrains based on their navigability levels using coarse-grained semantic segmentation. Our novel loss can be embedded within any backbone network to explicitly focus on the different groups’ features, at a low spatial resolution. Our design leads to efficient inference while maintaining a high level of accuracy compared to existing SOTA methods. Our extensive evaluations on the RUGD and RELLIS-3D datasets shows that GA-Nav achieves the state-of-the-art performance on RUGD and RELLIS-3D datasets. We interface GA-Nav with a deep reinforcement learning-based navigation algorithm and highlight its benefits in terms of navigation in real-world unstructured terrains. We integrate our GA-Nav-based navigation algorithm with ClearPath Jackal and Husky robots, and observe an improvement in terms of navigation success rate and better trajectory selections.
