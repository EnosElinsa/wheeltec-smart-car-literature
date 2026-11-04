# GNM: A General Navigation Model to Drive Any Robot

## Metadata

| Field | Value |
|---|---|
| ID | K13 |
| Title | GNM: A General Navigation Model to Drive Any Robot |
| Authors | Dhruv Shah, Ajay Sridhar, Arjun Bhorkar, Noriaki Hirose, and Sergey Levine |
| Venue | 2023 IEEE International Conference on Robotics and Automation (ICRA) |
| Year | 2023 |
| Type | conference |
| DOI | [10.1109/icra48891.2023.10161227](https://doi.org/10.1109/icra48891.2023.10161227) |
| Official URL | https://ieeexplore.ieee.org/document/10161227/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2023-GNM-K13/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2023-GNM-K13/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2023-GNM-K13/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: none
- platform_class: differential-drive
- platform: Deployed on a LoCoBot (Kobuki base), a Roomba-based Vizbot, a Clearpath Jackal and a DJI Tello held at 1 m height; quantitative tests use the Jackal and LoCoBot (p. 4).
- boundary_platform: no
- degradation: actuator-fault, sensor-fault
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Monocular RGB cameras (PCB-mounted fisheye on the deployed robots); training data pair images with commanded actions and local odometry (pp. 2, 4)
- compute: Not inspected in this reading.
- compute_location: not-reported
- summary_result: Trained on 60 hours from 6 robots, one GNM policy controls four robots, including two unseen ones, and outperforms single-dataset policies by up to 5x (pp. 1, 4).
- summary_limitation: The model does not account for differences in capabilities and assumes ground robots with a forward-facing RGB camera; the dataset could be much larger (p. 6).
- survey_included: yes
- verification_level: light

## Problem

Learned visual navigation policies are limited by robot-specific training data. GNM trains one goal-conditioned policy on data from many structurally similar robots (p. 1).

## Mechanism

An image-goal navigation policy with temporal context and a standardized action space is trained on pooled trajectories from different robots, cameras and speeds; the authors couple it with topological graphs to scale image-goal navigation to new robots (pp. 2-3).

## Baselines and controls

Policies trained on single datasets and on increasingly diverse subsets (Small, Mid, Large), and visual representations pre-trained on task-agnostic data such as ImageNet (p. 4).

## Platform and setup

Training data: GoStanford, RECON, CoryHall, Berkeley, SCAND, Seattle, TartanDrive and NeBula trajectories from TurtleBot, Jackal, RC car, Spot, Warthog and ATV platforms, with top speeds of 0.2 to 10 m/s (p. 2). Evaluation: zero-shot deployment on four robots and quantitative tests in 20 indoor and outdoor environments on the Jackal and LoCoBot (p. 4). Degradation tests clip the maximum angular velocity, perturb the camera position and damage the robot during navigation (p. 6).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Quantitative tests use the Jackal and the Kobuki-based LoCoBot; the vocabulary counts Kobuki robots as differential drive. Actuation and viewpoint degradation are designed conditions with results per condition (Fig. 5). The provisional module `semantic-language-navigation` is kept with `traversability-planning-control` as secondary: the policy itself is learned image-goal navigation, but it belongs to the foundation-model navigation lineage (K12, K13, K14, K16) that the survey reads together with LeLaN (E50), and LM-Nav (K12) names a general navigation model as the component to swap in.

## Sensors

All platforms use the same sensor type, a monocular RGB camera, with different intrinsics and mounting; the deployed robots carry PCB-mounted fisheye cameras (pp. 2, 4).

## Compute and latency

Not inspected in this reading.

## Key quantitative results

- Training data: 60 hours from 6 robots according to the abstract and text, while the Table I caption reports 70 hours (pp. 1-2).
- Zero-shot deployment on four robots, including two new ones and a quadrotor (pp. 1, 4).
- GNM outperforms single-robot policies on all tested robots, by up to 5x in some cases (p. 4).
- Under clipped angular velocity, GNM takes a longer, smoother path to the goal without localization failures (p. 6; per-condition values in Fig. 5, not re-read).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The system does not account for differences in capabilities and assumes ground robots with a forward-facing RGB camera (p. 6).
- A much larger and broader dataset could enable better generalization (p. 6).

## Transfer conditions

The policy assumes a forward-facing RGB camera and a robot-specific low-level controller for normalized waypoints; capability differences such as traversability are not modeled.

## Code and data

The datasets, code and videos are announced on the project page (p. 1); availability was not checked.

## Version family

Counted once by the registered ICRA 2023 identity. ViNT (K14) and NoMaD (K16) are later works of the same group that build on this training setup; each is a separate library entry.

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

- **p. 2, Sec. III.** "The GNM dataset contains over 60 hours of real-world navigation trajectories: a combination of tele-operated and autonomous navigation behaviors collected across 6 distinct robotic platforms"
  Training data scale and composition.
- **p. 6, Sec. VI.** "Most prominently, our system does not explicitly account for differences in capabilities: we assume all robots are ground robots (though we study generalization to a quadrotor) with a forward-facing RGB camera."
  Author-stated embodiment limit.
- **p. 4, Sec. V-B.** "we quantitatively evaluate the navigation performance of policies trained with heterogeneous datasets in an assortment of 20 indoor and outdoor environments on the Jackal and LoCoBot platforms (Tables III, IV)."
  Quantitative test platforms and environment count.
- **p. 4, Sec. V-A.** "A popular open-source platform based on a Kobuki, equipped with an off-the-shelf PCB-mounted fisheye camera."
  Source for the differential-drive coding of the LoCoBot.

## Survey-usable statements

### Supported

- One image-goal policy trained on pooled data from six robots controlled four robots zero-shot, including two not seen in training.
- Policies trained on heterogeneous data tolerated clipped steering and a perturbed camera better than single-domain policies.

### Not supported

- GNM does not follow language instructions by itself.
- The results do not cover robots whose capabilities or sensors differ from the training robots.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 4, 5, 6; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

Learning provides a powerful tool for vision-based navigation, but the capabilities of learning-based policies are constrained by limited training data. If we could combine data from all available sources, including multiple kinds of robots, we could train more powerful navigation models. In this paper, we study how a general goal-conditioned model for vision-based navigation can be trained on data obtained from many distinct but structurally similar robots, and enable broad generalization across environments and embodiments. We analyze the necessary design decisions for effective data sharing across robots, including the use of temporal context and standardized action spaces, and demonstrate that an omnipolicy trained from heterogeneous datasets outperforms policies trained on any single dataset. We curate 60 hours of navigation trajectories from 6 distinct robots, and deploy the trained GNM on a range of new robots, including an underactuated quadrotor. We find that training on diverse data leads to robustness against degradation in sensing and actuation. Using a pre-trained navigation model with broad generalization capabilities can bootstrap applications on novel robots going forward, and we hope that the GNM represents a step in that direction. For more information on the datasets, code, and videos, please check out our project page [1].
