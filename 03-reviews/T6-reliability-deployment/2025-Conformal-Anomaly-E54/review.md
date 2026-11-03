# Uncertainty-Aware Real-Time Visual Anomaly Detection With Conformal Prediction in Dynamic Indoor Environments

## Metadata

| Field | Value |
|---|---|
| ID | E54 |
| Title | Uncertainty-Aware Real-Time Visual Anomaly Detection With Conformal Prediction in Dynamic Indoor Environments |
| Authors | Arya Saboury and Mustafa Kemal Uyguroglu |
| Venue | IEEE Robotics and Automation Letters, vol. 10, no. 5, pp. 4468-4475 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3552318](https://doi.org/10.1109/lra.2025.3552318) |
| Official URL | https://ieeexplore.ieee.org/document/10930535/ |
| Theme folder | T6-reliability-deployment |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T6-reliability-deployment/2025-Conformal-Anomaly-E54/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-Conformal-Anomaly-E54/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2025-Conformal-Anomaly-E54/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: none
- evidence_type: online-hardware
- evidence_all: online-hardware, recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Scout Mini Pro in a university hallway; drive type not recorded
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: integrity-reliability
- evaluation_all: residual, integrity-reliability
- sensors: Intel RealSense D435 RGB; mounted Velodyne LiDAR not fused
- compute: NVIDIA Jetson Xavier AGX; measured FPS, latency, and memory not recorded
- compute_location: onboard
- summary_result: At alpha = 0.05, the hallway detector reports precision 0.9505, recall 0.3097, and false-positive rate 0.0308 on the local test set.
- summary_limitation: The conformal guarantee assumes exchangeability and controls normal-sample false alarms, rather than anomaly recall.
- survey_included: yes
- verification_level: light

## Problem

Hallway anomaly detection needs low false-alarm rates and explicit uncertainty quantification.

## Mechanism

A four-layer convolutional autoencoder (128/256/512/1024 channels) trains on normal data using 256 × 256 RGB inputs. MAE+MSE reconstruction losses form the anomaly score. Five hundred normal images calibrate p = (number of calibration scores exceeding the test score + 1)/(n + 1); observations with p ≤ α are flagged and logged.

## Baselines and controls

MSE-only autoencoder loss ablation. The legacy extraction records no common-data experiment against named external systems such as EfficientAD.

## Platform and setup

Scout Mini Pro in a university hallway. Of 2500 normal images, 1600/400/500 are for training/validation/calibration. The separate test set has 1100 normal and 800 anomalous images, collected using the robot's initial classifications and manually relabeled. These legacy counts were not re-verified.

## Evidence type and transfer

Local hallway image classification/calibration and real-robot deployment with logging, without a recorded closed-loop obstacle-avoidance test. Detection metrics do not establish collision avoidance or cross-site transfer. The legacy extraction does not identify a specific designed degradation category, so none is coded.

## Sensors

Intel RealSense D435 RGB supplies detector input. The mounted Velodyne LiDAR is not fused into the anomaly score. Depth/multisensor fusion is listed as future work.

## Compute and latency

Jetson Xavier AGX, Ubuntu/ROS Noetic, PyTorch/Python. The legacy extraction records a real-time claim but no measured FPS, latency, or memory; the processor model alone does not establish timing.

## Key quantitative results

The following legacy values were located, not re-verified.

- Local test-set AUC is 0.8174, with 95% confidence interval [0.7995, 0.8341] (p. 6, Sec. V-B).
- At α = 0.05, precision/recall/F1/FPR/FNR are 0.9505/0.3097/0.4671/0.0308/0.6903 (p. 6, Table III).
- At α = 0.1, recall/F1/FPR are 0.4905/0.6422/0.0706; at α = 0.3, recall/FPR are 0.6844/0.2722 (p. 6, Table III).
- At α = 0.05, normal-sample coverage is 0.9692 versus nominal 0.95 (p. 7).
- At α = 0.1, combined-loss F1 is 0.6422 versus MSE-only 0.7056, so the proposed loss is not best at every operating point (p. 6, loss ablation).

## Stated limitations

- The conformal guarantee relies on exchangeable observations and bounds false alarms on normal behavior (p. 4, Sec. III). Exact theorem conditions were not independently re-proved in this light conversion.

## Transfer conditions

Legacy reviewer observations: exchangeability under temporally correlated video and domain shift is not validated. False-positive control does not guarantee anomaly recall or collision avoidance; the recorded α = 0.05 point has approximately 69% false negatives. Close training/validation curves do not establish cross-site generalization. One hallway and the data-selection process restrict the tested distribution. Fig. 4's local p-value boxes are supplementary visualization rather than a separately validated object-localization method. Reuse needs a representative normal calibration set and safety handling for missed anomalies.

## Code and data

IEEE DOI supplementary material is mentioned, but no code/data-download URL was recorded in the legacy extraction. Availability was not verified.

## Version family

RA-L 2025; no explicit conference extension or same-batch version relationship was recorded.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | partial-support | moderate | Sec. III, Theoretical Guarantees, p. 4 | "This theorem guarantees that the probability of falsely flagging normal behavior as anomalous is bounded by the chosen significance level α [7], [34]." |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 6, Sec. V-B, Area Under the Curve.** "The model achieved an AUC of 0.8174"
  This is a local image-detection result, not a closed-loop safety result.
- **p. 6, Sec. V-A, Evaluating Loss Functions and Justification of Selection.** "In contrast, the MSE + MAE approach improved recall and provided more stable performance"
  This is the located part of the authors comparison; the inherited results still include an operating point where MSE-only has higher F1.
- **p. 4, Sec. III, Theoretical Guarantees.** "This theorem guarantees that the probability of falsely flagging normal behavior as anomalous is bounded by the chosen significance level α [7], [34]."
  The guarantee concerns normal-sample false alarms under the exchangeability premise, rather than anomaly recall.

## Survey-usable statements

### Supported

- Autoencoder scores can be calibrated by conformal prediction for normal-sample false-alarm control under exchangeability, with local hallway detection and robot-logging evidence (light review).

### Not supported

- A 95% anomaly detection rate at α = 0.05: recorded precision is 0.9505, while recall is 0.3097.
- Combined loss is best at every operating point: at α = 0.1 its F1 is 0.6422 versus MSE-only 0.7056.
- Guaranteed collision avoidance, cross-site validity, or measured real-time throughput: these evaluations were not recorded.

## Verification log

- 2026-11-02 | host: Codex | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format conversion; two legacy quotes shortened and theorem quote copied from its exact transcription; exchangeability and recall caveats retained
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/830cdba33b85748d191da0c8/
- Legacy provenance: selection_id 830cdba33b85748d191da0c8; PDF SHA-256 e120f10b0a4722931dd0738d1eeea0cf28ea5ce95a8d345649efe881b07374ea (inherited, not re-hashed).

## Original abstract

This letter presents an efficient visual anomaly detection framework designed for safe autonomous navigation in dynamic indoor environments, such as university hallways. The approach employs an unsupervised autoencoder method within deep learning to model regular environmental patterns and detect anomalies as deviations in the embedding space. To enhance reliability and safety, the system integrates a statistical framework, conformal prediction, that provides uncertainty quantification with probabilistic guarantees. The proposed solution has been deployed on a real-time robotic platform, demonstrating efficient performance under resource-constrained conditions. Extensive hyperparameter optimization ensures the model remains dynamic and adaptable to changes, while rigorous evaluations confirm its effectiveness in anomaly detection. By addressing challenges related to real-time processing and hardware limitations, this work advances the state-of-the-art in autonomous anomaly detection. The probabilistic insights offered by this framework strengthen operational safety and pave the way for future developments, such as richer sensor fusion and advanced learning paradigms. This research highlights the potential of uncertainty-aware deep learning to enhance safety monitoring frameworks, thereby enabling the development of more reliable and intelligent autonomous systems for real-world applications.
