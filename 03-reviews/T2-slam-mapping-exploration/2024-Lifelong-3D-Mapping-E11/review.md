# Lifelong 3D Mapping Framework for Hand-Held & Robot-Mounted LiDAR Mapping Systems

## Metadata

| Field | Value |
|---|---|
| ID | E11 |
| Title | Lifelong 3D Mapping Framework for Hand-Held & Robot-Mounted LiDAR Mapping Systems |
| Authors | Liudi Yang, Sai Manoj Prakhya, Senhua Zhu, and Ziyuan Liu |
| Venue | IEEE Robotics and Automation Letters, vol. 9, no. 11, pp. 9446-9453 |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2024.3417113](https://doi.org/10.1109/lra.2024.3417113) |
| Official URL | https://ieeexplore.ieee.org/document/10566021/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T2-slam-mapping-exploration/2024-Lifelong-3D-Mapping-E11/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2024-Lifelong-3D-Mapping-E11/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2024-Lifelong-3D-Mapping-E11/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: external-pose-source, scripted-scenario
- platform_class: handheld
- platform: XGrids commercial handheld LiDAR mapping device; public datasets SemanticKITTI, NCLT, LT-ParkingLot, and MulRan (carriers not described in the paper)
- boundary_platform: yes
- degradation: dynamic-objects, scene-change
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: 3D LiDAR point clouds with poses from the source mapping system (XGrids software, SC-LIO-SAM, SC-A-LOAM, or dataset poses)
- compute: AMD Ryzen 9 3900X PC; about 1.5 h for dynamic removal on KITTI 00 (4500 frames); about 3 min alignment grid search for about 10 M points
- compute_location: desktop-offline
- summary_result: Mean F1 of 0.9488 versus 0.9278 for ERASOR over five SemanticKITTI sequences; version control stores 27 NCLT maps in 430.7 MB versus 7440.9 MB.
- summary_limitation: The authors state that about 1-3% of static points remain misclassified as dynamic because not all areas are revisited during mapping.
- survey_included: yes
- verification_level: full

## Problem

Single-session LiDAR maps contain dynamic objects, each session has its own
reference frame, and storing every session costs 10 GB to 200 GB per map
(p. 1). The paper builds an offline lifelong mapping pipeline that cleans,
aligns, compares, and versions multi-session maps from handheld and
robot-mounted LiDAR systems, without depending on a particular sensor setup
or on online pose-graph pruning.

## Mechanism

The pipeline has four modules (pp. 2-4):

- Dynamic object removal: OctoMap produces static, dynamic, and unknown
  points from the scans and their poses. Submaps of about 10-50 frames are
  fitted with RANSAC planes; the largest plane is added back to the static
  map, and further planes are added when their share of submap points passes
  a ratio threshold. Unknown points are labelled by K-NN voting, followed by
  statistical outlier removal and radial filtering. An optional height filter
  reduces compute.
- Multi-session alignment: PCA-SHOT descriptors on keypoints give a RANSAC
  initial alignment (inlier ratio twice the keypoint radius), refined by NDT.
  Six parameters are searched over the grid of Table I (p. 3), and the
  registration with the lowest Chamfer distance is kept (p. 4).
- Change detection: k-NN radius searches split the base map and the new
  session into coexisting, overlapping, and non-overlapping parts; 2D
  bird's-eye-view (BEV) height images of the overlap are compared per pixel to
  find negative (disappeared) and positive (new) differences. A grid
  resolution of 0.05-0.15 m is recommended for precision and 0.5-2 m for
  large maps; multi-layer BEV descriptors are used in indoor car parks
  (p. 4).
- Version control: one base map is kept, together with the stored positive
  and negative differences and each session's convex-hull boundary. Any
  earlier session map is reconstructed by rolling the differences back and
  cropping with the stored hull (Eq. 1, p. 4).

## Baselines and controls

Dynamic removal is compared with ERASOR, Removert, and Ground-Octomap on
SemanticKITTI, with the sequences and scan ranges of the ERASOR setup (p. 5).
ERASOR could only run on four times fewer frames because of its compute and
memory needs (p. 6), so its maps are sparser and its rejection rate is not
computed on the same frames. Alignment is compared with LT-Mapper's
multi-session alignment (labelled LT-SLAM), direct ICP, and direct NDT
(p. 6). Change detection is compared with a K-D tree change detector (KNN)
and the PCL octree change detector (PCL-OC), the latter used as implemented
in PCL (p. 7). There is no ablation of the plane-recovery step or of the BEV
comparison.

## Platform and setup

All experiments process recorded point clouds offline. Two settings are used:

- Public datasets recorded by others: SemanticKITTI (sequences 00, 01, 02,
  05, 07) for dynamic removal (p. 5); LT-ParkingLot (6 maps, poses from
  SC-LIO-SAM and from SC-A-LOAM) and MulRan DCC (3 maps) for alignment; NCLT
  for qualitative alignment and for memory (27 maps) (pp. 6, 8). The paper
  does not describe the carrier of these datasets.
- XGrids sessions: XGrid-Outdoor (6 maps aligned, 3 maps in the memory test)
  and XGrid-Parking (5 maps aligned, 3 in the memory test), captured with a
  commercial handheld XGrids device, with poses from XGrids's proprietary
  software (p. 6).

Change detection is scored on XGrid-Outdoor, XGrid-Parking, MulRan, and
LT-ParkingLot after the authors relocated objects (buildings, cars, trees)
in the maps to obtain ground truth (p. 7). The real car-parking changes,
the real changes in LT-ParkingLot, and the occlusion case of a synthetic
dataset are shown only qualitatively (Figs. 4 and 7). The text states that
alignment was benchmarked on "four datasets", while Table III has five rows
because LT-ParkingLot appears with two SLAM pose sources; the MulRan row is
labelled SC-LIO-LOAM although the text names SC-LIO-SAM and SC-A-LOAM as the
pose sources (p. 6). NCLT is described as collected over a year (p. 6) and
over 1.5 years (p. 8).

## Evidence type and transfer

No robot runs the pipeline and no navigation result is reported. The
XGrids sessions are not cited as a public dataset, and the abstract says
that the experiments were performed using handheld commercial LiDAR mapping
devices (p. 1), so they are coded as the authors' recorded data with a
handheld carrier; the public datasets are dataset playback. The
dynamic-removal scores (Table II) come only from public SemanticKITTI data;
the alignment, change-detection, and memory tables mix both settings. The
paper calls the framework cloud-native, but every timing was measured on a
desktop PC.

## Sensors

The method uses LiDAR point clouds and the per-scan poses delivered by the
source mapping system (XGrids software, SC-LIO-SAM, SC-A-LOAM, or the
dataset). Ground truth for dynamic removal is the SemanticKITTI point labels;
ground truth for change detection is the set of manually relocated objects.

## Compute and latency

All timings come from a PC with an AMD Ryzen 9 3900X CPU (p. 6):

- Dynamic removal takes about 1.5 hours for the 4500 frames of KITTI 00,
  stated as 1.5 times faster than Ground-Octomap (p. 6).
- The alignment grid search takes about 3 minutes for XGrid-Outdoor maps of
  about 10 M points, against over 10 minutes for LT-SLAM (p. 6).
- Change detection takes about 2 minutes on LT-ParkingLot with roughly 10 K
  simulated change points in a 0.8 M point map, similar to PCL-OC and KNN
  (pp. 7-8).

No memory use during processing, GPU, or cloud deployment is reported.

## Key quantitative results

Tables II-V were read from the rendered page images.

- Dynamic removal, mean over five SemanticKITTI sequences: preservation rate 0.9502 versus 0.8874 (ERASOR), 0.9029 (Removert), and 0.7614 (Ground-Octomap); F1 0.9488 versus 0.9278, 0.7865, and 0.7747; rejection rate 0.9479 versus 0.9739 for ERASOR (p. 5, Table II).
- Per sequence, the method has the highest F1 on all five sequences. ERASOR has the higher rejection rate on 02 (0.9911 vs 0.9035), 05 (0.9788 vs 0.9712), and 07 (0.9833 vs 0.9410); Removert has the higher preservation rate on 01 (0.9579 vs 0.9425) and Ground-Octomap on 02 (0.9479 vs 0.9421) (p. 5, Table II).
- Alignment, average Chamfer distance (Ours versus LT-SLAM, ICP, NDT): XGrid-Outdoor 0.0690 vs 0.0862, 0.1389, 0.1342; XGrid-Parking 0.0812 vs fail, fail, 0.1235; LT-ParkingLot with SC-LIO-SAM 0.0329 vs 0.0592, 0.1211, 0.1378; LT-ParkingLot with SC-A-LOAM 0.0173 vs 0.0526, 0.1228, 0.1282; MulRan 0.1004 vs 0.2059, fail, 0.1231 (p. 6, Table III). The units of this mean squared distance are not stated.
- Change detection, mean over four datasets (Ours versus KNN, PCL-OC): positive-difference precision 0.885 vs 0.711, 0.654; negative-difference precision 0.920 vs 0.739, 0.692; positive-difference recall 0.852 vs 0.830, 0.785; negative-difference recall 0.850 vs 0.854, 0.800 (p. 7, Table IV).
- Change-detection counterexamples: KNN has the higher positive-difference precision on MulRan DCC (0.836 vs 0.769); KNN has the higher negative-difference recall on XGrid-Outdoor (0.937 vs 0.798) and XGrid-Parking (0.872 vs 0.848), and PCL-OC on XGrid-Outdoor (0.921 vs 0.798) (p. 7, Table IV).
- Version-control storage (Ours versus all downsampled input maps): XGrid-Outdoor, 3 maps, 27.2 MB vs 45.4 MB (40.1% saving); XGrid-Parking, 3 maps, 31.9 vs 64.3 MB (50.4%); LT-ParkingLot, 6 maps, 129.9 vs 594.1 MB (78.1%); NCLT, 27 maps, 430.7 vs 7440.9 MB (94.2%) (p. 8, Table V).

## Stated limitations

- About 1-3% of static points stay misclassified as dynamic, because not all areas can be revisited during mapping (p. 3).
- The optional height filter may not work directly for drone-based mapping or handheld mapping in multi-storey buildings and may need additional consistency checks (p. 3).
- Most parameter subsets of the alignment grid search fail at the feature-matching stage, because of too few PCA-SHOT correspondences or RANSAC inliers (p. 3).
- Future work: open-world object detection and vision-language models or LLMs for semantic insight from lifelong maps (p. 8).

## Transfer conditions

The pipeline assumes accurate per-scan poses from an upstream SLAM system or
device software; pose errors are not evaluated. Plane recovery assumes that
the static structure is dominated by large planes such as ground and
facades, which the authors state for most scenes (p. 3) but which may not
hold in vegetated or cluttered terrain. "Without manual parameter
fine-tuning" means an exhaustive search over a fixed grid; by this review's
count Table I spans 5 x 4 x 2 x 4 x 4 x 2 = 1280 combinations, and the
Chamfer distance used to select the result is also the evaluation metric of
Table III. The change-detection scores rest on objects relocated by the
authors, not on natural long-term change. Storage savings are measured
against downsampled maps, not raw sessions. A wheeled robot that wants to
use the maintained base map for localization would still need a
relocalization and map-serving layer, which the paper does not evaluate.

## Code and data

The paper links supplementary downloadable material at the DOI (p. 1). It
does not state a code release or the availability of the XGrids sessions;
the supplementary material was not verified.

## Version family

No conference version or extension was found in the library. LT-Mapper,
which the paper uses as its alignment comparator, is not in the library.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | weak | Sec. I, p. 1 | "however continual changes in environment over time, render these maps less useful over time" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | partial-support | weak | Sec. I, p. 1 | "regular map updates via lifelong 3D mapping is crucial for long term robot operation" |
| C6 | qualifies | moderate | Sec. III-B, p. 3 | "However, this height filter may not directly work in the case of drone-based mapping or handheld mapping in multi-storey buildings, and thus may require additional consistency checks to use it." |

## Page-cited excerpts

- **p. 3, Sec. III-B.** "Even after this, there will be about 1–3% of static points misclassified as dynamic points, as all areas cannot be revisited during mapping."
  The authors' own residual-error statement for the removal module.
- **p. 6, Sec. IV-A.** "ERASOR’s computational and memory requirements were so higher that it could only work with 4× lower frames and could not process every frame, resulting in sparse maps."
  The ERASOR comparison in Table II is not run on the same frames.
- **p. 7, Sec. IV-C.** "We manually introduce changes in XGrid-Outdoor, XGrid-Parking, MulRan and LT-ParkingLot datasets by randomly relocating objects such as buildings, cars, and trees, so that we know the ground truth differences/changes."
  Table IV scores injected changes, not natural long-term change.
- **p. 8, Sec. IV-C.** "In Table V, we report the memory required to store all input downsampled maps versus memory utilized by the map version control module that essentially saves the base map, negative & positive differences and boundaries."
  Table V is a storage comparison against downsampled maps, not a runtime memory measurement.

## Survey-usable statements

### Supported

- Storing one base map plus per-session positive and negative differences and convex-hull boundaries reduced storage from 7440.9 MB to 430.7 MB for 27 NCLT sessions, relative to downsampled input maps.
- An OctoMap-based removal pipeline with plane recovery reached a mean F1 of 0.9488 on five SemanticKITTI sequences, above ERASOR, Removert, and Ground-Octomap, without assumptions on sensor height.
- Descriptor-plus-NDT alignment with a grid search gave the lowest Chamfer distance on all five alignment cases, including an indoor car park where LT-SLAM and ICP failed.

### Not supported

- The dynamic removal is best on every metric: ERASOR has the higher rejection rate on 3 of 5 sequences and on the mean, and the preservation rate is beaten on 2 of 5 sequences (Removert on 01, Ground-Octomap on 02).
- The change detection has the higher precision on every dataset: KNN is higher for positive differences on MulRan DCC, and negative-difference recall is lower than KNN on XGrid-Outdoor, XGrid-Parking, and the mean.
- The framework improves robot localization or navigation over time: no localization or navigation run is reported.
- The pipeline runs in the cloud or in real time: all timings are offline on a desktop PC, with 1.5 h for KITTI 00.
- The change-detection accuracy holds for natural long-term change: the scored changes were relocated by the authors.

## Verification log

- 2026-10-26 | host: Kiro | scope: full text read; Tables I-V read from rendered page images (pp. 3, 5-8); timing, protocol, and limitation statements checked on pp. 1, 3, 4, 6-8 | corrections: table number of the SemanticKITTI result; cloud computation replaced by desktop PC; occlusion test is qualitative only; limitations restricted to author statements; counterexamples for removal and change detection added (see tmp/corrections/E11.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/e65b244300e21f242cb42f23/

## Original abstract

We propose a lifelong 3D mapping framework that is modular, cloud-native by design and more importantly, works for both hand-held and robot-mounted 3D LiDAR mapping systems. Our proposed framework comprises of dynamic point removal, multi-session map alignment, map change detection and map version control. First, our sensor-setup agnostic dynamic point removal algorithm works seamlessly with both hand-held and robot-mounted setups to produce clean static 3D maps. Second, the multi-session map alignment aligns these clean static maps automatically, without manual parameter fine-tuning, into a single reference frame, using a two stage approach based on feature descriptor matching and fine registration. Third, our novel map change detection identifies positive and negative changes between two aligned maps. Finally, the map version control maintains a single base map that represents the current state of the environment, and stores the detected positive and negative changes, and boundary information. Our unique map version control system can reconstruct any of the previous clean session maps and allows users to query changes between any two random mapping sessions, all without storing any input raw session maps, making it very unique. Extensive experiments are performed using hand-held commercial LiDAR mapping devices and open-source robot-mounted LiDAR SLAM algorithms to evaluate each module and the whole 3D lifelong mapping framework.
