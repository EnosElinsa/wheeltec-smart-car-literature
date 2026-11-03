# Learning Self-Supervised Traversability With Navigation Experiences of Mobile Robots: A Risk-Aware Self-Training Approach

## Metadata

| Field | Value |
|---|---|
| ID | M23 |
| Title | Learning Self-Supervised Traversability With Navigation Experiences of Mobile Robots: A Risk-Aware Self-Training Approach |
| Authors | Ikhyeon Cho and Woojin Chung |
| Venue | IEEE Robotics and Automation Letters, vol. 9, no. 5, pp. 4122-4129 |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2024.3376148](https://doi.org/10.1109/lra.2024.3376148) |
| Official URL | https://ieeexplore.ieee.org/document/10468651/ |
| Theme folder | T6-reliability-deployment |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T6-reliability-deployment/2024-SS-traversability-M23/paper.pdf` and `02-fulltext/T6-reliability-deployment/2024-SS-traversability-M23/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2024-SS-traversability-M23/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: joystick-driving
- platform_class: differential-drive
- platform: Unnamed two-wheeled differential-drive urban robot (text, p. 5)
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Downward-tilted Velodyne VLP-16; LIO-SAM footprint projection; proprioceptive label consistency
- compute: Not recorded in the legacy extraction; not verified.
- compute_location: not-reported
- summary_result: The legacy experiments use about ten minutes of manually driven training per site at a mean 0.9 m/s; performance values were not extracted.
- summary_limitation: Highly unstructured terrain is beyond the experimental robot’s operational capability.
- survey_included: yes
- verification_level: light

## Problem

Learn robot-specific outdoor traversability from limited driving experience. Safety-conscious operators undersample risky terrain, so self-supervised learners can overfit easy surfaces, while manual labels do not scale. Physics-simulation transfer is described as difficult motivation, not the method's training pipeline.

## Mechanism

A 2.5-D elevation map has 120 by 120 cells at 0.1 m resolution. Five geometric attributes—step height, slope, roughness, curvature, and elevation variance—support traversable/non-traversable classification. Footprints projected through LIO-SAM label traversed cells; a height threshold supplies obstacle weak labels. Risk-aware instance weighting prioritizes scarce high-risk cells, confidence-regularized self-training generates pseudo-labels for unvisited cells, and exteroceptive/proprioceptive consistency removes noisy weak labels.

## Baselines and controls

The legacy extraction records conventional learning and non-learning comparators, including self-training [4] as the pseudo-label ablation. Further comparator names and numerical performance scores were not recorded in the legacy extraction; not verified.

## Platform and setup

Outdoor experiments use an unnamed two-wheeled differential-drive robot intended for urban living, with a Velodyne VLP-16 tilted downward by 30 degrees. Training uses about ten minutes of manual driving at each site, averaging 0.9 m/s. The urban campus is approximately 510 m by 460 m with 17 m elevation change and a maximum slope of 14 degrees; surfaces include asphalt, damaged pavement, and cobblestones. The second setting is unpaved farm roads. Highly unstructured terrain is outside the platform's capability.

## Evidence type and transfer

The legacy record describes terrain-classification experiments from a real robot and manually driven training data. It does not establish that the learned traversability output drives an autonomous closed loop, so the conservative coding is recorded-robot-data with joystick-driving. Transfer concerns the robot-specific terrain model and empirical labeling pipeline.

## Sensors

A downward-tilted Velodyne VLP-16 updates the elevation map. LiDAR-based SLAM (LIO-SAM) projects footprints. Proprioceptive consistency is used to clean labels; a specific proprioceptive sensor model was not recorded.

## Compute and latency

Not recorded in the legacy extraction; not verified.

## Key quantitative results

- Training collection lasts about ten minutes per environment at a mean linear velocity of 0.9 m/s (p. 6).
- The urban campus spans approximately 510 m by 460 m, with 17 m maximum elevation change and a maximum terrain inclination of 14 degrees (p. 6).
- The local elevation map comprises 120 by 120 cells at 0.1 m resolution (p. 5).
- The legacy extraction reports real-world traversability comparisons and a self-training ablation but records no numerical classifier or navigation-performance values.

## Stated limitations

- Highly unstructured terrain is beyond the experimental robot's operational capabilities (p. 5).

## Transfer conditions

A robot-specific elevation map, footprint projection, weak-label threshold, and fresh driving experience are required. Training data can remain biased toward easy surfaces because risky regions are avoided. Statements about human-label burden, sim-to-real difficulty, and bad pseudo-labels in previous approaches are motivation or comparator discussion, not new limitations of a deployed system. The hardware evidence does not justify operation on terrain beyond this robot's capability.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | direct-support | moderate | Abstract, p. 1 | "However, providing sufficient and diverse experience to the robot is difficult in many practical applications." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. IV-A, p. 5 | "However, highly unstructured terrains are beyond the robot’s operational capabilities." |

## Page-cited excerpts

- **p. 1, Abstract.** "However, providing sufficient and diverse experience to the robot is difficult in many practical applications."
  The learning problem has an explicit experience-diversity constraint.
- **p. 5, Sec. IV-A.** "However, highly unstructured terrains are beyond the robot’s operational capabilities."
  The physical platform limits terrain-transfer claims.

## Survey-usable statements

### Supported

- Risk-aware weighting and confidence-regularized self-training address scarce high-risk terrain experience in robot-specific traversability learning.
- The legacy real-robot experiments use short manually driven training in urban and agricultural environments; numerical details require rechecking before citation.

### Not supported

- The paper establishes autonomous navigation driven by the learned output; the legacy extraction records terrain estimation and manual driving, without a demonstrated closed loop.
- The method requires no robot-specific data or supports arbitrarily rough terrain; local driving experience is used and highly unstructured terrain exceeds the platform's capability.
- The proposed pipeline is a sim-to-real method; simulation-transfer difficulty is background motivation.

## Verification log

- 2026-11-02 | host: Codex | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: English template conversion; no legacy verbatim excerpts to retain; actual abstract and platform-limit excerpts located; C3 strength narrowed to its data constraint; motivation separated from author-stated platform limitation; performance numbers absent in legacy remain absent
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Mobile robots operating in outdoor environments face the challenge of navigating various terrains with different degrees of difficulty. Therefore, traversability estimation is crucial for safe and efficient robot navigation. Current approaches utilize a robot’s driving experience to learn traversability in a self-supervised fashion. However, providing sufficient and diverse experience to the robot is difficult in many practical applications. In this paper, we propose a self-supervised traversability learning method that adapts to challenging terrains with limited prior experience. One key aspect is to enable prioritized learning of scarce yet high-risk terrains by using a risk-sensitive approach. To this end, we train a neural network through a risk-aware instance weighting scheme. Another key aspect is to leverage traversability pseudo-labels on the basis of a self-training scheme. The proposed confidence-regularized self-training generates high-quality pseudo-labels, thereby achieving reliable data augmentation for unexperienced terrains. The effectiveness of the proposed method is verified in extensive real-world experiments, ranging from structured urban environments to complex rugged terrains.
