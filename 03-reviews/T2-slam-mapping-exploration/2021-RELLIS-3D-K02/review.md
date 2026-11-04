# RELLIS-3D Dataset: Data, Benchmarks and Analysis

## Metadata

| Field | Value |
|---|---|
| ID | K02 |
| Title | RELLIS-3D Dataset: Data, Benchmarks and Analysis |
| Authors | Peng Jiang, Philip Osteen, Maggie Wigness, and Srikanth Saripalli |
| Venue | 2021 IEEE International Conference on Robotics and Automation (ICRA) |
| Year | 2021 |
| Type | conference |
| DOI | [10.1109/icra48506.2021.9561251](https://doi.org/10.1109/icra48506.2021.9561251) |
| Official URL | https://ieeexplore.ieee.org/document/9561251/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T2-slam-mapping-exploration/2021-RELLIS-3D-K02/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2021-RELLIS-3D-K02/paper.md` (local only); [citation.bib](../../../01-papers/T2-slam-mapping-exploration/2021-RELLIS-3D-K02/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: dataset-resource
- evidence_all: dataset-resource, recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Clearpath Robotics Warthog on the Rellis Campus of Texas A&M University; drive type not stated in the inspected pages (pp. 1-2).
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: Ouster OS1 64-channel and Velodyne Ultra Puck LiDARs, Basler RGB camera, Nerian stereo camera, Vectornav VN-300 GNSS/INS (p. 2)
- compute: Two onboard computers for control and data collection (p. 2); benchmark training hardware not inspected.
- compute_location: not-reported
- summary_result: Off-road benchmarks give 50.13% mIoU for GSCNN versus 74.7% on Cityscapes and 40.20% for SalsaNext versus 59.5% on SemanticKITTI (p. 5).
- summary_limitation: All data come from a single outdoor facility, which limits diversity across splits; traversability labels are future work (p. 6).
- survey_included: yes
- verification_level: light

## Problem

Off-road semantic segmentation lacks multimodal training data with point-wise LiDAR labels. The paper releases annotated camera and LiDAR data from an off-road site and benchmarks segmentation models on it (pp. 1-2).

## Mechanism

Five ROS-bag sequences with synchronized LiDAR, camera, stereo and GNSS/INS data are released, with 6,235 pixel-wise image annotations, 13,556 annotated LiDAR scans, and fixed training, validation and test splits (pp. 1-2).

## Baselines and controls

Image segmentation with HRNet+OCR and GSCNN; point-cloud segmentation with SalsaNext and KPConv; each is compared with its published urban result (p. 5).

## Platform and setup

Data were recorded with a Clearpath Warthog on runways, aprons, forest, bushes, pastures and lakes of one campus facility (p. 1). The point-cloud split has 7,800 training, 2,413 validation and 3,343 test scans and uses 16 classes (p. 5).

## Evidence type and transfer

Strongest coded setting: `dataset-resource` with the authors' recorded robot data. Evaluation is segmentation error only; no planner or controller is evaluated. The provisional module `traversability-planning-control` is confirmed: the labels describe terrain classes that feed traversal decisions, and the authors discuss traversable bushes, water and hidden fences as navigation cases (pp. 5-6).

## Sensors

Ouster OS1 (64 channels), Velodyne Ultra Puck (32 channels), Nerian Karmin2 stereo camera, Basler acA1920-50gc RGB camera and Vectornav VN-300 GNSS/INS. PTP synchronizes all sensors except the GNSS/INS, which is matched by nearest timestamp (p. 2).

## Compute and latency

The Warthog carries a navigation computer and a vision computer running ROS Kinetic (p. 2). Training hardware for the benchmarks was not inspected.

## Key quantitative results

- Annotations: 6,235 images and 13,556 LiDAR scans across five sequences (pp. 1-2).
- Image segmentation: GSCNN 50.13% mIoU versus 74.7% on Cityscapes; HRNet+OCR 48.83% versus 81.1% (p. 5).
- Point-cloud segmentation: SalsaNext 40.20% and KPConv 18.07% mIoU versus 59.5% and 58.8% on SemanticKITTI (p. 5).
- Label-distribution sampling raised KPConv by only 0.6% mIoU (p. 5).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- All data were collected in a single outdoor facility, so diversity across the splits is limited (p. 6).
- Labels are object classes without traversable or non-traversable attributes; such higher-order labels are planned (p. 6).
- Extreme class imbalance and unclear class boundaries reduce segmentation accuracy (p. 5).

## Transfer conditions

The terrain classes come from one site and one vehicle; a smaller wheeled robot needs its own mapping from classes to traversability. No closed-loop navigation is evaluated.

## Code and data

The dataset is announced at https://github.com/unmannedlab/RELLIS-3D (p. 1); availability was not checked.

## Version family

Counted once by the registered ICRA 2021 identity; no other version is in the library. GA-Nav (M40) benchmarks on RELLIS-3D, and TartanDrive (K04) contrasts its interaction volume with RELLIS-3D.

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

- **p. 6, Sec. VI.** "Since the data was collected all in a single outdoor facility, maintaining diversity across the train/test/val set is a challenge."
  Author-stated scope limit of the dataset.
- **p. 5, Sec. V-D.** "From the experimental results, we see that extreme class imbalance in off-road environments presents challenges for current semantic segmentation algorithms."
  The benchmark result is a segmentation-error finding, not a navigation outcome.
- **p. 1, Sec. I.** "we present RELLIS-3D, a novel dataset captured from a Clearpath Robotics Warthog platform (shown in Fig. 1)."
  Identifies the carrier; the drive type is not stated.

## Survey-usable statements

### Supported

- RELLIS-3D supplies point-wise off-road LiDAR labels and pixel-wise image labels from one wheeled platform.
- Urban-trained segmentation architectures lose accuracy on these off-road labels.

### Not supported

- The dataset does not by itself show that semantic classes improve closed-loop off-road navigation.
- Results from one facility do not establish cross-site generalization.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 5, 6; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

Semantic scene understanding is crucial for robust and safe autonomous navigation, particularly so in off-road environments. Recent deep learning advances for 3D semantic segmentation rely heavily on large sets of training data, however existing autonomy datasets either represent urban environments or lack multimodal off-road data. We fill this gap with RELLIS-3D, a multimodal dataset collected in an off-road environment, which contains annotations for 13,556 LiDAR scans and 6,235 images. The data was collected on the Rellis Campus of Texas A&M University, and presents challenges to existing algorithms related to class imbalance and environmental topography. Additionally, we evaluate the current state of the art deep learning semantic segmentation models on this dataset. Experimental results show that RELLIS-3D presents challenges for algorithms designed for segmentation in urban environments. This novel dataset provides the resources needed by researchers to continue to develop more advanced algorithms and investigate new research directions to enhance autonomous navigation in off-road environments. RELLIS-3D is available at https://github.com/unmannedlab/RELLIS-3D
