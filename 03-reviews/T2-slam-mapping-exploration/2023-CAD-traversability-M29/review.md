# Circular Accessible Depth: A Robust Traversability Representation for UGV Navigation

## Metadata

| Field | Value |
|---|---|
| ID | M29 |
| Title | Circular Accessible Depth: A Robust Traversability Representation for UGV Navigation |
| Authors | Shikuan Xie, Ran Song, Yuenan Zhao, Xueqin Huang, Yibin Li, and Wei Zhang |
| Venue | IEEE Transactions on Robotics, vol. 39, no. 6, pp. 4875-4891 |
| Year | 2023 |
| Type | journal |
| DOI | [10.1109/tro.2023.3308780](https://doi.org/10.1109/tro.2023.3308780) |
| Official URL | https://ieeexplore.ieee.org/document/10242384/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T2-slam-mapping-exploration/2023-CAD-traversability-M29/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2023-CAD-traversability-M29/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2023-CAD-traversability-M29/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, dataset-playback, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: AgileX SCOUT UGV (no drive type found in the text)
- boundary_platform: no
- degradation: dynamic-objects, terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task
- sensors: Velodyne VLP-16 3D LiDAR; WTGAHRS1 IMU and TOP103 GPS on the UGV
- compute: onboard Intel i5-9400H CPU and GTX-1650 GPU, about 60 ms per frame; AMD Ryzen 7 3800X with RTX 2080 Ti for dataset timing
- compute_location: onboard
- summary_result: In four real scenes on an AgileX SCOUT, CAD reports 100% success with zero collisions versus STVL and Autoware (Table IV), at about 60 ms per frame onboard.
- summary_limitation: The authors state that binary traversability limits deployment range, that a relatively expensive LiDAR is required, and that thin structures yield inaccurate predictions.
- survey_included: yes
- verification_level: light

## Problem

The paper addresses LiDAR traversability estimation for unmanned ground
vehicles (UGVs) among irregular and negative obstacles such as curbs,
downward stairs, and unguarded pool or bridge edges. Bird's-eye-view (BEV)
semantic maps handle curbs and negative obstacles poorly because empty LiDAR
returns are unlabeled. Multi-frame fusion leaves trailing shadows of moving
vehicles and pedestrians.

## Mechanism

Circular accessible depth (CAD) predicts, in polar coordinates around the
UGV, the maximum accessible range in each heading as a discrete probability
distribution, using the network CADNet. A stability-attention module (SAM)
fuses several LiDAR frames and down-weights spatially unstable (dynamic)
features. Semi-supervised losses concentrate the distribution, so only a
small labeled set is needed. Downstream navigation runs a timed-elastic-band
(TEB) local planner on the predicted CAD.

## Baselines and controls

Perception baselines are BEV networks: PillarSegNet, MASS, BEVNet, and
PolarNet or Cylinder3D with aggregation. Ablations quantify the CAD loss and
SAM, including the interference by historical dynamic objects (IHD) metric.
Navigation baselines are STVL and Autoware.

## Platform and setup

Perception was evaluated on Semantic KITTI sequences and on an Isaac Sim
dataset with negative obstacles. Real navigation used an AgileX SCOUT with a
Velodyne VLP-16, a WTGAHRS1 IMU, a TOP103 GPS, and an onboard i5-9400H CPU
with a GTX-1650 GPU. About 400 real frames were labeled for training. The
four real scenes were Driveway, Sidewalk, Stairhall, and Corridor, with
static and dynamic obstacles; the UGV followed a preset path.

## Evidence type and transfer

Perception accuracy comes from Semantic KITTI (public data) and Isaac Sim.
Navigation success comes from closed-loop runs on one SCOUT UGV in four
scenes. The legacy extraction notes that the residual effect of dynamic
objects on the SCOUT runs is not quantified separately after SAM.

## Sensors

The method uses a 3D LiDAR (Velodyne VLP-16 on the UGV; the automotive
LiDAR of KITTI in the dataset). The UGV also carries an IMU and a GPS; their
role in the method is not recorded in the legacy extraction.

## Compute and latency

On the UGV, an onboard computer with an i5-9400H CPU and a GTX-1650 GPU
spends about 60 ms per frame. Dataset timings were measured on an AMD Ryzen 7
3800X CPU with an RTX 2080 Ti GPU.

## Key quantitative results

- Onboard processing time: about 60 ms per frame on i5-9400H plus GTX-1650 (p. 14).
- About 400 real-world samples labeled for training CADNet (p. 14).
- Real navigation: CAD reports 100% success and zero collisions in the tabulated runs, versus STVL and Autoware (Table IV).
- Dataset model timing measured on AMD Ryzen 7 3800X with RTX 2080 Ti (p. 10, Table I).

## Stated limitations

- The method requires a LiDAR, which is relatively expensive; cheap depth cameras have too little field of view and range (p. 15).
- The method is not good at predicting thin objects, such as guardrails or table tops parallel to the LiDAR scan layer, which return few points (p. 15).
- The current CAD assumes binary traversability, which limits its deployment range; a multilevel CAD is future work (p. 16).

## Transfer conditions

The method needs a 3D LiDAR with enough field of view and range, a GPU
computer on the robot, and a few hundred labeled real frames. Navigation was
tested along a preset path with a TEB planner on one UGV. SAM reduces, but
was not shown to remove, the effect of dynamic objects on the real runs.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. IV-A, p. 12 | "3) IHD is the interference by historical dynamic objects, as evidenced by two indicators: Number and Ratio." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. IV-C, p. 15 | "First, our method requires a LiDAR sensor, which is relatively expensive." |

## Page-cited excerpts

- **p. 12, Sec. IV-A.** "3) IHD is the interference by historical dynamic objects, as evidenced by two indicators: Number and Ratio."
  Dynamic objects are a named, measured failure mode of multi-frame traversability.
- **p. 15, Sec. IV-C.** "First, our method requires a LiDAR sensor, which is relatively expensive."
  A sensor-cost limit stated by the authors.
- **p. 16, Sec. V.** "Our current design for CAD is based on the premise that traversability is binary, while this limits the deployment range of CAD."
  The representation does not grade traversability.
- **p. 14, Sec. IV-B.** "It spends about 60 ms handling a frame, which satisfies the real-time requirement."
  Onboard timing on the SCOUT computer.

## Survey-usable statements

### Supported

- A polar accessible-depth representation with attention-based multi-frame fusion ran onboard a SCOUT UGV at about 60 ms per frame and was compared with STVL and Autoware in four real scenes (numbers from a light review; re-check before citing).
- Historical points of dynamic objects are a named failure mode of multi-frame LiDAR traversability (IHD metric).

### Not supported

- CAD works with a low-cost depth camera: the authors state that cheap depth cameras do not meet its requirements.
- CAD grades terrain difficulty: the current design is binary.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); the legacy card had no verbatim quotes, so excerpts were taken from the limitations, conclusion, and setup text with --find; Table IV values not located on a page
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

In this article, we present the circular accessible depth (CAD), a robust traversability representation for an unmanned ground vehicle (UGV) to learn traversability in various scenarios containing irregular obstacles. To predict CAD, we propose a neural network, namely CADNet, with an attention-based multiframe point cloud fusion module, stability-attention module (SAM), to encode the spatial features from point clouds captured by LiDAR. CAD is designed based on the polar coordinate system and focuses on predicting the border of traversable area. Since it encodes the spatial information of the surrounding environment, which enables a semisupervised learning for the CADNet, and thus, desirably avoids annotating a large amount of data. Extensive experiments demonstrate that CAD outperforms baselines in terms of robustness and precision. We also implement our method on a real UGV and show that it performs well in real-world scenarios.
