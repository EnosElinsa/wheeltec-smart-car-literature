# Screw-based feature constraint model and degeneracy analysis for robotic state estimation: Theory and experiments

## Metadata

| Field | Value |
|---|---|
| ID | E05 |
| Title | Screw-based feature constraint model and degeneracy analysis for robotic state estimation: Theory and experiments |
| Authors | Jiancheng Wang, Chenyuan Cai, Yifei Wang, Yuxiang Li, Shiwu Zhang, and Haoyao Chen |
| Venue | The International Journal of Robotics Research (online first; volume and pages not yet assigned) |
| Year | 2026 |
| Type | journal |
| DOI | [10.1177/02783649261463720](https://doi.org/10.1177/02783649261463720) |
| Official URL | https://journals.sagepub.com/doi/10.1177/02783649261463720 |
| Theme folder | T1-perception-localization |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T1-perception-localization/2026-Screw-Degeneracy-E05/paper.pdf` and `02-fulltext/T1-perception-localization/2026-Screw-Degeneracy-E05/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2026-Screw-Degeneracy-E05/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: fault-recovery-deployment
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback, simulation
- protocol_caveats: none
- platform_class: mixed
- platform: handheld Livox Avia rig, tracked robot with three Livox MID-360, vehicle with a 128-beam LiDAR, Livox Horizon case; SubT-MRS and heterogeneous-LiDAR public data
- boundary_platform: yes
- degradation: lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, integrity-reliability
- sensors: LiDAR (Livox Avia, Livox MID-360, 128-beam LiDAR, Livox Horizon); UWB and bearing constraints only in the theory
- compute: Intel i9-10900K, 32 GB RAM; module means of about 3.85, 0.72, 0.77, and 0.45 ms per 100 ms LiDAR period
- compute_location: desktop-offline
- summary_result: On a helical tunnel, the IFOE residual is 0.1353 m and 0.0161 rad versus 1.7925 to 1.8331 m and 0.2059 to 0.2103 rad for three degeneracy-detection baselines.
- summary_limitation: The authors exclude total divergence from scope and apply no degeneracy suppression in real tests, where drift corrupts the local feature map and causes missed and false detections.
- survey_included: yes
- verification_level: light

## Problem

Conventional degeneracy detection based on the Fisher information matrix (FIM) mixes translational and rotational scales, depends on the coordinate frame and on feature noise, and has difficulty detecting coupled rotation-translation (helical) degeneracy about axes that do not pass through the robot origin.

## Mechanism

Point-to-plane and point-to-line, range, and bearing constraints are unified with twists, wrenches, and their reciprocal product. Translational degeneracy is found by SVD; 1D helical degeneracy by RANSAC with an adaptive damped Newton method that estimates the axis and pitch; 3D spherical degeneracy has an analytic solution. Outliers are rejected by the feature normal error, constraints are normalized by an upper bound, and a noise-robust criterion separates degenerate cases. Strict PCA plane selection builds a local feature map (LFM) from a history ikd-tree; resampling and asynchronous feature extraction and mapping shorten the latency from scan to detection. The method is a diagnosis and direction-analysis module, not a complete estimator that recovers from degeneracy.

## Baselines and controls

Six-dimensional FIM (Zhang 2016), the three-dimensional split of Tuna 2024 (X-ICP), and Lee 2024 (Switch-SLAM). Threshold comparisons include tuned thresholds and fixed statistical thresholds. LOAM provides the odometry in simulation and KISS-ICP on real data. Scenes: simulated pipes and inner and outer spiral stairs; public SubT-MRS corridors and a heterogeneous-LiDAR shield tunnel; self-collected spiral ramps and a multi-level spiral garage tunnel.

## Platform and setup

Real data come from a handheld Livox Avia in a shield tunnel section, a tracked robot with three MID-360, a vehicle with a 128-beam LiDAR, and a circular-building case with a limited-FOV Livox Horizon; none of them is a synchronized closed-loop autonomous wheeled run. Real-data labels are generated from 30 independent KISS-ICP runs on the same data: Karcher mean and PCA of the SE(3) relative transforms with an empirical time-window threshold. There is no external full-trajectory ground truth.

## Evidence type and transfer

Geometric modeling and conditional theory, detection in simulation, and offline diagnosis on self-collected and public data. Ground vehicles are included, but there is no deployment on the reference platform, no closed-loop state repair, and no multi-robot experiment.

## Sensors

The theory covers LiDAR, 3D ranging (for example UWB), and bearing-camera constraints, but the experimental evidence is mainly LiDAR; LiDAR-UWB-camera fusion on hardware is not shown. The LFM integrates the map from an existing odometry and extracts features where the field of view overlaps the history map. The method assumes smooth instantaneous velocity, convergence of the estimate to a similar degenerate subspace, and a significant degeneracy error.

## Compute and latency

All runs used an Intel i9-10900K with 32 GB RAM; the need for a GPU is not discussed. Fig. 33 gives module means as fractions of the 100 ms LiDAR period: feature analysis 3.85%, LFM construction 0.72%, resampling 0.77%, and detection 0.45%, about 3.85, 0.72, 0.77, and 0.45 ms. The authors report that the latency from scan reception to detection output falls by more than 70% through asynchronous reuse of history features; this is not a 70% reduction of total CPU load or of the full SLAM runtime.

## Key quantitative results

- IFOE residual projected onto the orthogonal complement of the detected degenerate subspace (a diagnostic, not the ATE of a corrected trajectory), helical tunnel: proposed 0.1353 m and 0.0161 rad versus Tuna 1.8226 m and 0.2091 rad, Lee 1.7925 m and 0.2059 rad, and Zhang 1.8331 m and 0.2103 rad (p. 29, Table 2).
- The real-data IFOE also rests on the statistical pseudo-ground truth from repeated KISS-ICP runs (p. 24).
- Overlap of the TND curves for the circular and square rooms: proposed 0.0058 versus Tuna 0.1009, Lee 0.2049, and Zhang 0.2284, that is 17.4 to 39.4 times smaller, which does not support the abstract's "more than two orders of magnitude" (p. 32, Table 3).
- Recall for one outer spiral staircase with RI, PI, UI, and CI initialization: 34.8%, 43.0%, 99.9%, and 100%; recall is not 100% in every scene (p. 34, Table 4).
- Module timing of about 3.85, 0.72, 0.77, and 0.45 ms per 100 ms period (Fig. 33; percentages not located in the PDF text layer; legacy location: page 35).

## Stated limitations

- Total divergence, where the smoothness and local-convergence assumptions are violated, is not discussed (p. 6).
- The 1D helical degeneracy model is non-convex (p. 16).
- Real tests apply no targeted degeneracy suppression to the state estimator; accumulated odometry errors corrupt the LFM and lead to missed and false detections (p. 36).
- Compensation through multi-robot collaboration is future work (p. 37).

## Transfer conditions

Legacy reviewer observations: RANSAC initialization of the non-convex 1D helical problem improves results but gives no global convergence guarantee; closed-form global optima exist only for the translational and 3D subproblems. Real labels are statistics of the same baseline's output, not external physical ground truth. The default value 0.025 works across the tested scenes, but the noise threshold and plane parameters still need tuning. Multi-sensor use in the theory and active-SLAM prediction are not shown experimentally. On a new robot, the detector needs an existing LiDAR odometry and a LiDAR whose field of view overlaps the history map.

## Code and data

The paper links online supplementary videos; the legacy extraction found no repository URL for code or self-collected data. Use of the public SubT-MRS and heterogeneous-LiDAR data does not make all experimental data public. Supplementary material was not watched and code was not run.

## Version family

The paper does not state an earlier conference version. The group's earlier degeneracy-aware and dynamic SLAM works are cited but are separate works, not replications. The method is a detection module and is not counted as a complete SLAM system.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Abstract, p. 1 | "Degeneracy caused by the repetition of geometric features remains a significant bottleneck in robotic state estimation systems like odometry and SLAM." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | qualifies | moderate | p. 36 | "eventually resulting in missed and false detections of degeneracy." |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 6, Scope.** "Hence, the degradation scenario is not discussed in this work."
  Total divergence and unobservable cases are outside the scope.
- **p. 16, Helical model.** "the 1D helical degeneracy model, as formulated in problem (30), exhibits non-convexity"
  No general global guarantee for the 1D helical search.
- **p. 24, Real labels.** "(e.g., K = 30 in our evaluation)"
  Real labels come from 30 repeated KISS-ICP evaluations, not external ground truth.
- **p. 29, Table 2.** "Residual of the IFOE in the orthogonal complement of the degenerate space."
  The residual measures direction fitting, not corrected odometry.
- **p. 32, Table 3.** "Overlap area of TND curves in degenerate/non-degenerate scenarios."
  The 17.4- to 39.4-fold advantage does not reach two orders of magnitude.
- **p. 35, Fig. 33.** "Time comparison of degeneracy analysis."
  Module means per 100 ms period.
- **p. 36, Real tests.** "with no targeted degeneracy suppression optimization"
  Real evaluation feeds KISS-ICP output only; no recovered localization is shown.
- **p. 36, Failure mode.** "eventually resulting in missed and false detections of degeneracy."
  Odometry drift corrupts the LFM.
- **p. 36, Latency.** "The results demonstrate that our method effectively compresses the processing latency from scanned point cloud reception to degeneracy detection result output, achieving a latency reduction of over 70% compared with the SOTA schemes."
  The reduction concerns waiting latency, not total computation.
- **p. 37, Future work.** "optimizing the poses of degenerate robots through multi-robot collaboration."
  Multi-robot repair is not evaluated.

## Survey-usable statements

### Supported

- A screw-theory degeneracy model separates translational and helical degeneracy and estimates the helical axis and pitch, with a much smaller IFOE residual than three FIM-based baselines on a simulated helical tunnel.
- Asynchronous reuse of a history feature map cuts the latency from scan reception to detection output by more than 70%.

### Not supported

- The stability metric beats the baselines by more than two orders of magnitude: Table 3 shows 17.4 to 39.4 times.
- The method improves localization accuracy: no degeneracy suppression was applied and no corrected-trajectory ATE is reported.
- Total computation or SLAM runtime falls by 70%: the figure refers to detection latency.
- Detection recall is 100%: recall depends on initialization (34.8% to 100% in one scene).

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; p. 30 residual-definition quote dropped (PDF text layer splits its words, so it cannot be page-checked); p. 24 and p. 36 quotes trimmed to the parts found on the PDF page
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/b6c1afccc07c673448c4968d/

## Original abstract

Degeneracy caused by the repetition of geometric features remains a significant bottleneck in robotic state estimation systems like odometry and SLAM. To address this challenge, we propose a novel approach based on screw theory to model feature constraints and analyze degeneracy. Unlike conventional methods, our approach derives feature constraint representations via geometric operations rather than by derivative computations, and decouples the cost-function formulation, yielding a more robust and interpretable framework. Initially, a feature constraint model is formulated using the screw representation. Subsequently, a degeneracy analysis model and a judgment formula are presented, both grounded in screw theory and the feature constraint model. The proposed model inherently separates translational and helical degeneracy while accurately estimating environmental parameters, such as the position and pitch of the rotation axis, to reduce assessment errors, enable outlier rejection, and improve the robustness of degeneracy detection. A novel feature extraction and management method is proposed to improve computation efficiency and coverage of the feature in sparsely scanned scenarios. Simulations and real-world experiments show that our approach improves the robustness and accuracy of degeneracy detection while reducing the computation time by more than 70%. A dimensionless stability metric for the judgment formula is proposed, showing that our approach significantly outperforms existing state-of-the-art (SOTA) approaches by more than two orders of magnitude. To date, this study constitutes the first formal endeavor to conceptualize and systematically analyze the problem of helical degeneracy, providing a novel and rigorous perspective on the inherent challenges of robotic state estimation.
