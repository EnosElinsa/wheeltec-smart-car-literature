# Online IMU-Odometer Calibration Using GNSS Measurements for Autonomous Ground Vehicle Localization

## Metadata

| Field | Value |
|---|---|
| ID | S32 |
| Title | Online IMU-Odometer Calibration Using GNSS Measurements for Autonomous Ground Vehicle Localization |
| Authors | Song, Baoshan and Xia, Xiao and Yan, Penggao and Zhong, Yihan and Wen, Weisong and Hsu, Li-Ta |
| Venue | IEEE Transactions on Intelligent Transportation Systems |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tits.2026.3706684](https://doi.org/10.1109/tits.2026.3706684) |
| Official URL | https://ieeexplore.ieee.org/document/11595203/ |
| Theme folder | T1-perception-localization |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2026-IMU-Odometer-Calibration-S32/paper.pdf` and `02-fulltext/T1-perception-localization/2026-IMU-Odometer-Calibration-S32/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2026-IMU-Odometer-Calibration-S32/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, numerical
- protocol_caveats: none
- platform_class: skid-steer
- platform: AgileX Scout-mini ground-robot recordings plus simulated planar motion; skid-steer class follows the named platform (pp. 9-10).
- boundary_platform: no
- degradation: gnss-denial
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Raw rover/base GNSS pseudorange, carrier phase and Doppler; IMU and wheel odometry; separate tactical RTK/INS reference
- compute: Intel NUC 11 with i5-1135G7; sliding-window factor-graph calibration timing is separate from the complete navigation pipeline (p. 10).
- compute_location: desktop-offline
- summary_result: Raw GNSS aids online calibration of observable IMU/odometer parameters under sufficiently exciting motion.
- summary_limitation: Vertical translation is unobservable in the analyzed planar-motion setting; initialization, heading quality and lever-arm error affect calibration (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Wheel scale and IMU/odometer extrinsic errors bias localization; planar motion leaves some parameters unobservable.

## Mechanism

Jointly estimates calibration and navigation states using raw-GNSS-constrained factor graphs, outlier handling and ambiguity resolution (pp. 3-4).

## Baselines and controls

Loosely coupled RTK calibration, GNSS lever-arm variants and simulated initialization perturbations; GPS-only aiding in the field test (pp. 7-10).

## Platform and setup

AgileX Scout-mini ground-robot recordings plus simulated planar motion; skid-steer class follows the named platform (pp. 9-10).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Requires GNSS measurements and adequate acceleration/turning during calibration; it is not a correction mechanism available throughout complete GNSS loss.

## Sensors

Raw rover/base GNSS pseudorange, carrier phase and Doppler; IMU and wheel odometry; separate tactical RTK/INS reference.

## Compute and latency

Intel NUC 11 with i5-1135G7; sliding-window factor-graph calibration timing is separate from the complete navigation pipeline (p. 10).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Vertical translation is unobservable in the analyzed planar-motion setting; initialization, heading quality and lever-arm error affect calibration (p. 8).

## Transfer conditions

Requires GNSS measurements and adequate acceleration/turning during calibration; it is not a correction mechanism available throughout complete GNSS loss.

## Code and data

Availability statements and external repositories were not independently checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity. No separate preprint or conference version is added to the corpus.

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

- **p. 8, Selected source passage.** "the $Z$-axis of $m$-frame is not observable"
  Adds observability-conditioned sensor maintenance to localization comparison rather than treating calibration as a fixed predeployment assumption.

## Survey-usable statements

### Supported

- Raw GNSS aids online calibration of observable IMU/odometer parameters under sufficiently exciting motion. Adds observability-conditioned sensor maintenance to localization comparison rather than treating calibration as a fixed predeployment assumption.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Requires GNSS measurements and adequate acceleration/turning during calibration; it is not a correction mechanism available throughout complete GNSS loss.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 4, 7, 8, 9, 10; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Accurate calibration of intrinsic (odometer scaling factors) and extrinsic parameters (IMU-odometer translation and rotation) is essential for autonomous ground vehicle localization. Existing GNSS-aided approaches often rely on positioning results or raw measurements without ambiguity resolution, and their observability properties remain underexplored. This paper proposes a tightly coupled online calibration method that fuses IMU, odometer, and raw GNSS measurements (pseudo-range, carrier-phase, and Doppler) within an extendable factor graph optimization (FGO) framework, incorporating outlier mitigation and ambiguity resolution. Observability analysis reveals that two horizontal translation and three rotation parameters are observable under general motion, while vertical translation remains unobservable. Simulation and real-world experiments demonstrate superior calibration and localization performance over the state-of-the-art loosely coupled method. Specifically, the IMU-odometer positioning using our calibrated parameters achieves the absolute maximum error of 17.75 m while the one of LC method is 61.51 m, achieving up to 71.14% improvement. To foster further research, we also release the first open-source dataset that combines IMU, 2D odometer, and raw GNSS measurements from both rover and base stations.
