# Geometrically-Constrained Radar-Inertial Odometry via Continuous Point-Pose Uncertainty Modeling

## Metadata

| Field | Value |
|---|---|
| ID | R01 |
| Title | Geometrically-Constrained Radar-Inertial Odometry via Continuous Point-Pose Uncertainty Modeling |
| Authors | Wooseong Yang, Dongjae Lee, Minwoo Jung, and Ayoung Kim |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3677708](https://doi.org/10.1109/lra.2026.3677708) |
| Official URL | https://ieeexplore.ieee.org/document/11455624/ |
| Theme folder | T1-perception-localization |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2026-Radar-Uncertainty-R01/paper.pdf` and `02-fulltext/T1-perception-localization/2026-Radar-Uncertainty-R01/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2026-Radar-Uncertainty-R01/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: Public 4D-radar datasets HeRCULES and SNAIL-Radar (outdoor vehicle sequences) and HKUST (indoor); carriers not inspected (pp. 5-6).
- boundary_platform: yes
- degradation: none
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: 4D Continental radar and IMU
- compute: Real-time operation and a computational-time analysis are reported (p. 8); processor not inspected in this reading.
- compute_location: desktop-offline
- summary_result: Joint point-pose uncertainty down-weights uninformative radar points; a planarity residual improves odometry only with the uncertainty-filtered map (p. 7).
- summary_limitation: No limitation is stated in the inspected passages; refining local geometric assumptions is left for future work (p. 7).
- survey_included: yes
- verification_level: light

## Problem

Sparse, noisy radar returns and pose drift corrupt scan-to-submap registration and the radar map used for odometry.

## Mechanism

A continuous-trajectory model propagates control-point uncertainty to the pose at each point timestamp; pose and heteroscedastic range/azimuth/elevation uncertainty are combined during projection to weight points, a localizability-constrained IEKF stabilizes the update, and mapping retains low-uncertainty points (pp. 3-5).

## Baselines and controls

State-of-the-art radar-inertial odometry baselines, including EKFRIO-TC, and ablations of uncertainty analysis, planarity constraints and the localizability-constrained update (pp. 6-8).

## Platform and setup

Three public 4D-radar datasets covering indoor and outdoor, structured, unstructured and degenerate sequences (pp. 5-6). Public 4D-radar datasets HeRCULES and SNAIL-Radar (outdoor vehicle sequences) and HKUST (indoor); carriers not inspected (pp. 5-6).

## Evidence type and transfer

Strongest coded setting: `dataset-playback`. Dataset replay only. The results concern odometry and map quality; no navigation controller consumes the estimate.

## Sensors

4D Continental radar and IMU.

## Compute and latency

Real-time operation and a computational-time analysis are reported (p. 8); processor not inspected in this reading.

## Key quantitative results

- Retaining only low-uncertainty returns with a geometric residual improves odometry, whereas a planarity residual on an unfiltered map degrades it (p. 7).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Exploring other scan-wise refinement strategies for the validity of local geometric assumptions is left for future work (p. 7).

## Transfer conditions

The weighting depends on the radar noise model and calibrated time stamps; dataset replay does not test recovery after an estimator failure on a moving robot.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity; no other version is in the library.

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

- **p. 7, Sec. V-D.** "Preserving only low-uncertainty returns and combining them with a geometric residual yields substantial odometry gains, whereas applying a planarity residual directly to an unfiltered map degrades performance because the local planarity assumption is frequently violated."
  Shows that a structural prior is useful only after unreliable radar points are removed.
- **p. 8, Sec. V-E.** "The impact of the constrained update becomes evident in Bridge and 20240123_2, which contain repetitive geometrical features on the bridge and tunnel."
  Locates the benefit of the localizability-constrained update in repetitive geometry.

## Survey-usable statements

### Supported

- Radar weighting that combines pose and measurement uncertainty is a measurement-selection response to sparse returns, evaluated on public datasets.

### Not supported

- The paper does not show that the estimate supports executed navigation or recovery.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 5, 6, 7, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Radar odometry is crucial for robust localization in challenging environments; however, the sparsity of reliable returns and distinctive noise characteristics impede its performance. This paper introduces geometrically-constrained radar-inertial odometry and mapping that jointly consolidates point and pose uncertainty. We employ the continuous trajectory model to estimate the pose uncertainty at any arbitrary timestamp by propagating uncertainties of the control points. These pose uncertainties are continuously integrated with heteroscedastic measurement uncertainty during point projection, thereby enabling dynamic evaluation of observation confidence and adaptive down-weighting of uninformative radar points. By leveraging quantified uncertainties in radar mapping, we construct a high-fidelity map that improves odometry accuracy under imprecise radar measurements. Moreover, we reveal the effectiveness of explicit geometrical constraints in radar-inertial odometry when incorporated with the proposed uncertainty-aware mapping framework. Extensive experiments on diverse real-world datasets demonstrate the superiority of our method, yielding substantial performance improvements in both accuracy and efficiency compared to existing baselines.
