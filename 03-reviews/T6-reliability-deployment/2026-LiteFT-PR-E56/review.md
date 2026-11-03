# LiteFT-PR: Lightweight and Fault-Tolerant LiDAR-Camera Fusion Network for Robust Place Recognition via Model Distillation

## Metadata

| Field | Value |
|---|---|
| ID | E56 |
| Title | LiteFT-PR: Lightweight and Fault-Tolerant LiDAR-Camera Fusion Network for Robust Place Recognition via Model Distillation |
| Authors | Zihang Wang, Xu Li, Guanyu Zong, Xieyuanli Chen, Dong Kong, Yiming Peng, Wenkai Zhu, and Kaiyi Wang |
| Venue | IEEE Robotics and Automation Letters, vol. 11, no. 4, pp. 4267-4274 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3662634](https://doi.org/10.1109/lra.2026.3662634) |
| Official URL | https://ieeexplore.ieee.org/document/11373724/ |
| Theme folder | T6-reliability-deployment |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T6-reliability-deployment/2026-LiteFT-PR-E56/paper.pdf` and `02-fulltext/T6-reliability-deployment/2026-LiteFT-PR-E56/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2026-LiteFT-PR-E56/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: fault-recovery-deployment
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: campus UGV; drive type not recorded
- boundary_platform: no
- degradation: visual-degradation, lidar-degeneracy, sensor-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: surround-view RGB and LiDAR; RTK ground truth for campus data
- compute: Intel i9-12900K, 32 GB RAM, RTX 2080 Ti; reported runtime 12.72 ms
- compute_location: desktop-offline
- summary_result: On corrupted nuScenes BS/SON, LiteFT-PR Recall@1 is 97.26%/96.38% versus LCPR 80.55%/82.59%, while clean-data comparisons favor LCPR.
- summary_limitation: Explicit author limitations were not recorded; the legacy review restricts timing evidence to desktop GPU retrieval rather than onboard closed-loop navigation.
- survey_included: yes
- verification_level: light

## Problem

LiDAR/camera corruption degrades multimodal place recognition, while a strong teacher is too costly for resource-limited deployment.

## Mechanism

A ResNet18+VCTF teacher trains on corrupted data. A lightweight ResNet18 student uses vertical channel/spatial/pixel attention (VCAF) and layerwise VC-NetVLAD descriptor KL distillation. With teacher frozen, the student trains on complete dual-modal data using triplet loss plus PRMFKD. Reliability labels supervise the teacher quality head.

## Baselines and controls

NetVLAD, OverlapTransformer, AdaFusion, PIC-Net, MinkLoc++, and LCPR. Ablations include concatenation, VCAF-only, and PRMFKD-only.

## Platform and setup

nuScenes Boston trains/evaluates the model, with Singapore SON for generalization. CorrScenes artificially corrupts real source data, approximately 765 scenes/30,600 keyframes. A 4.3 km campus UGV recording uses four cameras, Pandar64P LiDAR, and RTK, with covered cameras and sprayed-water/reflective LiDAR conditions. Night images are diffusion-generated and dual-modal snow is simulated. Counts/distances are inherited, not re-verified.

## Evidence type and transfer

Offline public-data retrieval, artificial corruption stress tests, and evaluation on self-recorded physical UGV data. This is not a closed-loop navigation or SLAM-safety experiment. Desktop GPU timing is not onboard embedded timing.

## Sensors

Standard inputs use six RGB views at 3 × 704 × 256 and a 1 × 32 × 1056 LiDAR range image, synchronized after a 50 ms sliding window. Self-recorded data use four cameras, requiring reproduction of cross-configuration details. RTK supplies campus ground truth.

## Compute and latency

Intel i9-12900K, 32 GB RAM, RTX 2080 Ti. Legacy values: 7.24 M student parameters, 9686 database samples, 12.72 ms total, 7.84 ms descriptors, 4.09 ms top-20 retrieval; teacher 29.13 M parameters/32.72 ms (p. 8). The reported components sum to 11.93 ms rather than the stated total; the legacy arithmetic caveat is retained without re-verifying values or deriving a new speedup.

## Key quantitative results

The following legacy values were located, not re-verified.

- Corrupted nuScenes BS/SON Recall@1: LiteFT-PR 97.26%/96.38% versus LCPR 80.55%/82.59%; SC-01/02: 91.69%/88.58% versus 75.46%/73.87% (p. 7, Table I).
- Clean nuScenes BS/SON Recall@1: LiteFT-PR 96.78%/96.02% versus LCPR 97.34%/99.40%; these are two counterexamples to all-conditions superiority (p. 7, Table I).
- Wet-ground/night/dual-snow Recall@1: 90.7%/88.6%/85.2% (p. 8, Table II).
- CorrScenes BS ablation Recall@1: full model 97.3% versus concatenation 89.3% (p. 8, Table III).
- Student runtime 12.72 ms with 7.24 M parameters versus teacher 32.72 ms with 29.13 M parameters, under the specified desktop/database conditions (p. 8, Sec. IV-F).

## Stated limitations

Not recorded in the legacy extraction; not verified.

## Transfer conditions

Legacy reviewer observations: fault tolerance means retrieval robustness to sensing corruption, rather than fault diagnosis/isolation/reconstruction or a closed-loop SLAM guarantee. A prebuilt database is still required. Synthetic night, snow, and corruption are substantial; unseen sites and real extreme dual-sensor failures need validation. Runtime components differ from the total and the teacher-relative percentage text has arithmetic ambiguity; retain reported numbers without new speedup claims. CorrScenes is described as six categories earlier and eight in experiments, including high noise. CPU-only/small-board performance was not recorded.

## Code and data

CorrScenes and campus data are constructed, but no code/data-download URL was recorded. A proposed benchmark does not establish a public release; availability was not verified.

## Version family

RA-L 2026; VCTF comes from LCPR and distillation is inspired by xMUDA. No explicit conference-extension statement is recorded. Count this DOI once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Abstract, p. 1 | "camera overexposure and LiDAR beam missing, which degrade the performance of traditional PR systems." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 8, Sec. IV-F, Runtime and Memory Consumption.** "9,686 database samples, LiteFT-PR achieves an average runtime of 12.72 ms with 7.24 M parameters, including 7.84 ms for descriptor generation and 4.09 ms for retrieval, demonstrating real-time capability for online autonomous driving."
  The runtime is conditioned on the desktop GPU/database, rather than an embedded CPU or closed-loop task.
- **p. 1, Abstract.** "camera overexposure and LiDAR beam missing, which degrade the performance of traditional PR systems."
  The abstract states the sensing-corruption motivation; evaluation remains subject to the recorded data conditions.

## Survey-usable statements

### Supported

- Teacher-student distillation with LiDAR-camera attention fusion is evaluated for corrupted-input place recognition on public/self-recorded data with reported desktop timing (light review).

### Not supported

- Best Recall@1 everywhere: clean BS and SON favor LCPR, 97.34%/99.40% versus LiteFT-PR 96.78%/96.02%.
- Closed-loop fault recovery, SLAM safety, or embedded CPU timing: evidence is offline retrieval on the specified desktop.
- Confirmed public benchmark release: no release URL was recorded.

## Verification log

- 2026-11-02 | host: Codex | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format conversion; exact legacy runtime quote retained and short abstract excerpt added; clean-data counterexamples and runtime arithmetic caveat retained
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/949b9bab24df1cf33844239b/
- Legacy provenance: selection_id 949b9bab24df1cf33844239b; PDF SHA-256 c06c359dfc926cb099fba4fb2a75fb82b89f6cc3b055d59fd133b94dc07b8ef4 (inherited, not re-hashed).

## Original abstract

Place recognition (PR) is a key component of simultaneous localization and mapping (SLAM) in autonomous vehicles and robotics. By efficiently matching descriptors generated from the current scene with a prebuilt reference database, existing PR methods enable accurate vehicle re-localization. However, achieving robust and efficient PR remains challenging, particularly in scenarios with sensor corruptions, such as camera overexposure and LiDAR beam missing, which degrade the performance of traditional PR systems. To address this issue, we propose LiteFT-PR, a fault-tolerant and lightweight LiDAR-camera fusion PR network. To balance accuracy and efficiency under extreme conditions, we adopt a knowledge distillation framework for PR tasks: the teacher network learns robust representations under corrupted sensing, while the student distills and inherits this knowledge for lightweight deployment. In addition, we design efficient multimodal fusion mechanisms for both networks, enabling robust place recognition under various sensor corruption scenarios while significantly reducing computational overhead. To meet real-world deployment needs, we build a dataset covering multiple types of sensor failures and conduct extensive field experiments. Experimental results demonstrate that LiteFT-PR, with only 7.24 M of parameters, outperforms state-of-the-art PR methods in both accuracy and efficiency.
