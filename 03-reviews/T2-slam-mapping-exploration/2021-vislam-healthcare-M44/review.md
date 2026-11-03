# Visual SLAM for robot navigation in healthcare facility

## Metadata

| Field | Value |
|---|---|
| ID | M44 |
| Title | Visual SLAM for robot navigation in healthcare facility |
| Authors | Baofu Fang, Gaofei Mei, Xiaohui Yuan, Le Wang, Zaijun Wang, and Junyang Wang |
| Venue | Pattern Recognition, vol. 113, art. 107822 |
| Year | 2021 |
| Type | journal |
| DOI | [10.1016/j.patcog.2021.107822](https://doi.org/10.1016/j.patcog.2021.107822) |
| Official URL | https://linkinghub.elsevier.com/retrieve/pii/S0031320321000091 |
| Theme folder | T2-slam-mapping-exploration |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T2-slam-mapping-exploration/2021-vislam-healthcare-M44/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2021-vislam-healthcare-M44/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2021-vislam-healthcare-M44/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: semantic-language-navigation
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: video-only-hardware
- platform_class: wheeled-unspecified
- platform: unnamed hospital mapping robot with Microsoft Kinect RGB-D (chassis and drive type not given in the text found); TUM RGB-D dataset
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Microsoft Kinect RGB-D camera
- compute: laptop with Intel i7-8750H and GTX 1060; 17.21 ms per frame for dynamic-object detection and removal
- compute_location: desktop-offline
- summary_result: On TUM RGB-D, ATE gains over ORB-SLAM2 are large on high-dynamic walking sequences and near parity on sitting sequences; dynamic-object removal takes 17.21 ms per frame on a laptop.
- summary_limitation: The authors plan to improve real-time performance and report that Mask R-CNN results are inaccurate around object contours.
- survey_included: yes
- verification_level: light

## Problem

Visual SLAM in hospitals faces people and movable equipment that violate the
static-world assumption of geometric systems such as ORB-SLAM2. Robots also
need semantic maps (object type, size, and pose) for delivery tasks, not
only a camera trajectory.

## Mechanism

The system is an ORB-SLAM2 RGB-D pipeline with an added Mask R-CNN thread. A
hospital knowledge graph encodes moving, movable, and static entities. A
rotation-invariant semantic descriptor around ORB points is combined with the
graph to reject dynamic features, and movable objects when they are near a
moving person. The remaining static points support tracking and a dense,
instance-level semantic point cloud.

## Baselines and controls

ORB-SLAM2 and other dynamic SLAM systems are compared on TUM RGB-D walking
and sitting sequences.

## Platform and setup

Fifteen Kinect image sequences were collected in a hospital (ward, corridor,
nurse station; isolation, buffer, and clean zones), including people walking.
The acknowledgments name the Hospital of the Hefei University of Technology
as the data source. A long-distance mapping of an entire hospital floor is
shown as the trajectory of "our robot"; the chassis is not named.
Quantitative trajectory errors use TUM RGB-D walking and sitting sequences.

## Evidence type and transfer

The hospital evidence is qualitative: semantic maps with dynamic persons
removed and a mapping trajectory, without tabulated metrics. All absolute
trajectory error (ATE) and relative pose error (RPE) numbers come from the
public TUM RGB-D dataset. No closed-loop navigation controller is evaluated.
The coding as a wheeled robot is not verified: the text found names neither
the chassis nor its drive type.

## Sensors

Microsoft Kinect RGB-D camera in the hospital; TUM RGB-D data for the
quantitative evaluation.

## Compute and latency

Timing was measured on a computer with an Intel i7-8750H CPU and a GTX 1060
GPU. Dynamic-object detection and removal took 17.21 ms on average; the
legacy extraction says this excludes network inference, which was not
verified. The stationary-case timing includes network training and is much
slower.

## Key quantitative results

- TUM RGB-D ATE and RPE versus ORB-SLAM2 and other dynamic SLAM systems: large gains on the high-dynamic walking sequences and near parity on the sitting and static sequences; the legacy extraction records no values (pp. 7-9, Tables 1-4).
- Dynamic-object detection and removal: 17.21 ms on average on i7-8750H with GTX 1060 (p. 11).
- Hospital data: 15 Kinect image sequences (p. 6).

## Stated limitations

- Future work is to improve the real-time performance of the system and to investigate other segmentation models considering accuracy and efficiency (p. 11).
- Mask R-CNN results are not accurate around the contours of objects (p. 11).

## Transfer conditions

The method needs an RGB-D camera, a GPU for Mask R-CNN, and a knowledge
graph of which entity classes move. Timing comes from a laptop with a
GTX 1060, not a robot computer. The hospital evidence is map construction,
not closed-loop navigation, and the quantitative accuracy is from TUM, not
from the hospital trajectory. On static or low-dynamic sequences the method
is near parity with ORB-SLAM2.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. 4.2, p. 8 | "Compared with ORB-SLAM2, it is evident that the proposed algorithm gains great improvement in high dynamic scenarios." |
| C3 | direct-support | weak | Sec. 5, p. 11 | "In the future, we plan to improve the real-time performance of the system." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | weak | Sec. 4.1, p. 7 | "We carried out a long-distance mapping of an entire floor in a local hospital." |

## Page-cited excerpts

- **p. 8, Sec. 4.2.** "Compared with ORB-SLAM2, it is evident that the proposed algorithm gains great improvement in high dynamic scenarios."
  Moving people degrade a static-world visual SLAM baseline on TUM walking sequences.
- **p. 11, Sec. 5.** "In the future, we plan to improve the real-time performance of the system."
  Learned semantics remain a real-time bottleneck.
- **p. 11, Sec. 5.** "We also find that the results of MASK R-CNN are not that accurate around the contours of objects."
  A stated accuracy limit of the segmentation front end.
- **p. 7, Sec. 4.1.** "We carried out a long-distance mapping of an entire floor in a local hospital."
  The hospital evidence is mapping, not navigation.

## Survey-usable statements

### Supported

- Rejecting dynamic features with Mask R-CNN semantics and a knowledge graph reduced ATE on TUM high-dynamic walking sequences relative to ORB-SLAM2 (light review; take values from the paper's Table 1 before citing).
- The gain is concentrated in high-dynamic sequences; sitting sequences show near parity.

### Not supported

- The method was validated for hospital navigation: the hospital evidence is qualitative mapping, and no navigation controller is evaluated.
- The method runs in real time on a robot computer: timing is from a GTX 1060 laptop, and the authors list real-time performance as future work.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); the legacy card had no verbatim quotes, so excerpts were taken from the conclusion and from Sec. 4 sentences located with --find; reviewer remarks moved from Stated limitations to Transfer conditions; the hospital name is from the acknowledgments
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

The COVID-19 pandemic has affected many countries, posing a threat to human health and safety, and putting tremendous pressure on the medical system. This paper proposes a novel SLAM technology using RGB and depth images to improve hospital operation efficiency, reduce the risk of doctor-patient cross-infection, and curb the spread of the COVID-19. Most current visual SLAM researches assume that the environment is stationary, which makes handling real-world scenarios such as hospitals a challenge. This paper proposes a method that effectively deals with SLAM problems for scenarios with dynamic objects, e.g., people and movable objects, based on the semantic descriptor extracted from images with help of a knowledge graph. Specifically, our method leverages a knowledge graph to construct a priori movement relationship between entities and establishes high-level semantic information. Built upon this knowledge graph, a semantic descriptor is constructed to describe the semantic information around key points, which is rotation-invariant and robust to illumination. The seamless integration of the knowledge graph and semantic descriptor helps eliminate the dynamic objects and improves the accuracy of tracking and positioning of robots in dynamic environments. Experiments are conducted using data acquired from healthcare facilities, and semantic maps are established to meet the needs of robots for delivering medical services. In addition, to compare with the state-of-the-art methods, a publicly available dataset is used in our evaluation. Compared with the state-of-the-art methods, our proposed method demonstrated great improvement with respect to both accuracy and robustness in dynamic environments. The computational efficiency is also competitive.
