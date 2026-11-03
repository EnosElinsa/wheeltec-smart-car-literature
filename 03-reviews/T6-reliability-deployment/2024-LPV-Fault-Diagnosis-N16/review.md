# Robust LPV Fault Diagnosis Using the Set-Based Approach for Autonomous Ground Vehicles

## Metadata

| Field | Value |
|---|---|
| ID | N16 |
| Title | Robust LPV Fault Diagnosis Using the Set-Based Approach for Autonomous Ground Vehicles |
| Authors | Shuang Zhang, Vicenç Puig, Sara Ifqir |
| Venue | IEEE Transactions on Intelligent Transportation Systems |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/tits.2024.3394518](https://doi.org/10.1109/tits.2024.3394518) |
| Official URL | https://ieeexplore.ieee.org/document/10528263/ |
| Theme folder | T6-reliability-deployment |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2024-LPV-Fault-Diagnosis-N16/paper.pdf` and `02-fulltext/T6-reliability-deployment/2024-LPV-Fault-Diagnosis-N16/paper.md` (local only); [publisher BibTeX](../../../01-papers/T6-reliability-deployment/2024-LPV-Fault-Diagnosis-N16/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: road-vehicle
- platform: Test-track vehicle data support an offline diagnostic evaluation, rather than onboard control during physical sensor or actuator failures.
- boundary_platform: yes
- degradation: sensor-fault, actuator-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: IMU yaw rate, odometry speed, Correvit sideslip and steering-angle encoder
- compute: MATLAB workstation; observer gains computed offline
- compute_location: desktop-offline
- summary_result: Set-based diagnosis distinguishes detectable from isolable faults in a vehicle-data study.
- summary_limitation: Fault estimation and fault-tolerant control are left for future work (p. 12).
- survey_included: yes
- verification_level: light

## Problem

A fault can be detectable without being distinguishable from another fault class.

## Mechanism

Zonotopic set-membership estimation is combined with invariant-set analysis of minimum detectable and isolable faults under bounded model uncertainty (pp. 2-4).

## Baselines and controls

Diagnosis uses acquired prototype-vehicle measurements and injected fault signals, with workstation computation comparisons (pp. 8-11).

## Platform and setup

Test-track vehicle data support an offline diagnostic evaluation, rather than onboard control during physical sensor or actuator failures.

## Evidence type and transfer

The strongest inspected setting is `recorded-robot-data`. Check lateral-model validity, uncertainty bounds and signal independence; healthy/fault set separation does not imply separation of every pair of fault classes.

## Sensors

IMU yaw rate, odometry speed, Correvit sideslip and steering-angle encoder.

## Compute and latency

MATLAB workstation; observer gains computed offline.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 12).

## Stated limitations

- Fault estimation and fault-tolerant control are left for future work (p. 12).

## Transfer conditions

Check lateral-model validity, uncertainty bounds and signal independence; healthy/fault set separation does not imply separation of every pair of fault classes.

## Code and data

Availability and links beyond the publisher artifacts were not independently verified in this targeted reading.

## Version family

One publisher DOI is counted. A comprehensive preprint/extension-family search was not performed in this targeted reading.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | partial-support | moderate | p. 12 | "authors plan to extend the proposed method for fault estimation and fault tolerant control problems" |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 8, Selected source passage.** "The real data used in the validation process are acquired using a prototype vehicle"
  Interpret within the experimental setting and transfer conditions above.

- **p. 12, Selected source passage.** "authors plan to extend the proposed method for fault estimation and fault tolerant control problems"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Set-based diagnosis distinguishes detectable from isolable faults in a vehicle-data study.
- Check lateral-model validity, uncertainty bounds and signal independence; healthy/fault set separation does not imply separation of every pair of fault classes.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. Fault estimation and fault-tolerant control are left for future work (p. 12).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 2, 3, 4, 8, 9, 10, 11, 12; Selected abstract, lateral model and bounded uncertainty, prototype-data validation setup, injected faults and computation setting, detection/isolation discussion and conclusion. Complete derivations and numerical tables not audited. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **— This paper proposes a robust fault diagnosis method**
**for** **Autonomous** **Ground** **Vehicles** **(AGVs)** **modeled** **as** **a** **Linear**
**Parameter** **Varying** **(LPV)** **system** **with** **bounded** **uncertainties.**
**The** **proposed** **approach** **combines** **the** **zonotope-based** **Set-**
**Membership** **Approach** **(SMA)** **and** **Set** **Invariance** **Approach**
**(SIA).** **Firstly,** **an** **online** **fault** **detection** **strategy** **based** **on**
**zonotopic** **set-membership** **state** **estimation** **is** **introduced,** **where**
**the** **optimal** **observer** **gain** **is** **calculated** **offline** **by** **solving** **LMI**
**optimization** **problems.** **To** **characterize** **the** **Minimum** **Detectable**
**Fault** **(MDF)** **and** **Minimum** **Isolable** **Fault** **(MIF),** **the** **invariant**
**residual sets are first obtained for the system operated in healthy**
**and faulty modes. The proposed method relies on the propagation**
**of** **the** **zonotopic** **state** **estimation** **error** **in** **steady** **state** **based**
**on** **SIA.** **Then,** **MDF** **and** **MIF** **are** **characterized** **for** **several**
**types** **of** **faults** **by** **solving** **optimization** **problems** **subject** **to** **set**
**separation** **conditions.** **Finally,** **experiment** **validations** **using** **a**
**prototype** **vehicle** **are** **performed** **to** **illustrate** **the** **effectiveness**
**of** **the** **proposed** **approach.**
