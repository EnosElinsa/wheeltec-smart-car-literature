# Extended Range of Localization Services via Formation-Controlled Mobile Ultra-Wideband Anchors

## Metadata

| Field | Value |
|---|---|
| ID | S28 |
| Title | Extended Range of Localization Services via Formation-Controlled Mobile Ultra-Wideband Anchors |
| Authors | Liu, Jinxin and Hu, Guoqiang |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tase.2025.3630274](https://doi.org/10.1109/tase.2025.3630274) |
| Official URL | https://ieeexplore.ieee.org/document/11237184/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Mobile-UWB-Anchors-S28/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Mobile-UWB-Anchors-S28/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-Mobile-UWB-Anchors-S28/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, numerical
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Pioneer3-AT mobile anchors with a nonholonomic differential-motion control model; precise drivetrain classification not audited here (p. 11).
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual, designed-degradation
- sensors: Nooploop P-B UWB and relative geometry; formation/target observations
- compute: Onboard i7-8550U/8 GB, WiFi and ROS Noetic (p. 11).
- compute_location: onboard
- summary_result: Controlled anchor motion extends the localization region under the inspected planar setup.
- summary_limitation: Height differences and uneven ground degrade planar localization; node limits and anomalous-range rejection remain issues (p. 12).
- survey_included: yes
- verification_level: light

## Problem

Fixed UWB anchors restrict the usable localization area and unfavorable anchor geometry magnifies error.

## Mechanism

Auto-calibrates mobile-anchor geometry, maintains a well-conditioned formation around a moving target, and trades obstacle clearance against formation quality (pp. 3, 11).

## Baselines and controls

Static/mobile geometry, sensor-height and formation/obstacle-gain sensitivity comparisons (pp. 11-12).

## Platform and setup

Pioneer3-AT mobile anchors with a nonholonomic differential-motion control model; precise drivetrain classification not audited here (p. 11).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Maintaining localization geometry consumes robot motion and clearance; planar radio geometry and reliable ranges need validation on uneven terrain.

## Sensors

Nooploop P-B UWB and relative geometry; formation/target observations.

## Compute and latency

Onboard i7-8550U/8 GB, WiFi and ROS Noetic (p. 11).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Height differences and uneven ground degrade planar localization; node limits and anomalous-range rejection remain issues (p. 12).

## Transfer conditions

Maintaining localization geometry consumes robot motion and clearance; planar radio geometry and reliable ranges need validation on uneven terrain.

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

- **p. 12, Selected source passage.** "anomalous distance measurements, particularly those arising from complex environmental interference."
  Makes active geometry a coordination objective and reveals a clearance-versus-information tradeoff.

## Survey-usable statements

### Supported

- Controlled anchor motion extends the localization region under the inspected planar setup. Makes active geometry a coordination objective and reveals a clearance-versus-information tradeoff.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Maintaining localization geometry consumes robot motion and clearance; planar radio geometry and reliable ranges need validation on uneven terrain.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 11, 12; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Conventional ultra-wideband device-based localization schemes predominantly depend on static anchors, which restrict localization services to predefined areas. This paper presents a novel localization scheme employing mobile ultra-wideband anchors, significantly extending the scope of localization services. These mobile anchors have the capability to auto-calibrate in real time, relative to each other, while simultaneously delivering localization services to the target. We delve into the effects of disparities in tag heights and variations in anchor formation shapes on localization accuracy. To maintain the target within the high-quality localization service range, we devise formation control algorithms for the mobile anchors. These algorithms ensure the anchors attain the desired formation and preclude mutual collisions, underpinned by robust mathematical proofs. Both simulations and experiments corroborate the theoretical conclusions and the localization scheme proposed in this paper.
