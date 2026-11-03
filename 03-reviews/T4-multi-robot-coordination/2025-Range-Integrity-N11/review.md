# Range-Based Multi-Robot Integrity Monitoring For Cyberattacks and Faults: An Anchor-Free Approach

## Metadata

| Field | Value |
|---|---|
| ID | N11 |
| Title | Range-Based Multi-Robot Integrity Monitoring For Cyberattacks and Faults: An Anchor-Free Approach |
| Authors | Vishnu Vijay, Kartik A. Pant, Minhyun Cho, Yifan Guo, James M. Goppert, Inseok Hwang |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3534068](https://doi.org/10.1109/lra.2025.3534068) |
| Official URL | https://ieeexplore.ieee.org/document/10854616/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2025-Range-Integrity-N11/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2025-Range-Integrity-N11/paper.md` (local only); [publisher BibTeX](../../../01-papers/T4-multi-robot-coordination/2025-Range-Integrity-N11/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: fault-recovery-deployment
- evidence_type: online-hardware
- evidence_all: online-hardware, simulation
- protocol_caveats: offboard-compute, motion-capture-pose, simulated-agents-on-hardware
- platform_class: aerial
- platform: Online mixed-reality aerial evaluation tests centralized error monitoring, not physical UWB sensing or a fully distributed wheeled team.
- boundary_platform: yes
- degradation: sensor-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation, integrity-reliability
- sensors: Inter-robot ranges emulated from motion-capture and simulator poses
- compute: Monitor centralized at a ground station in hardware, despite a distributed SCP/ADMM formulation
- compute_location: offboard-local
- summary_result: Range consistency supports shared-state fault reconstruction in a centralized mixed-reality experiment.
- summary_limitation: The hardware implementation is centralized (p. 7); a complete limitations inventory was not assessed.
- survey_included: yes
- verification_level: light

## Problem

Faulty shared localization can be diagnosed through consistency with inter-robot distances.

## Mechanism

The monitor reconstructs localization errors with sequential convex programming and an ADMM-based distributed formulation (pp. 1-2).

## Baselines and controls

The inspected mixed-reality experiment emulates ranges and combines real Crazyflies with virtual PX4 agents (pp. 6-7).

## Platform and setup

Online mixed-reality aerial evaluation tests centralized error monitoring, not physical UWB sensing or a fully distributed wheeled team.

## Evidence type and transfer

The strongest inspected setting is `online-hardware`. Separate formulation, evaluated placement and physical sensing; verify communication costs and actual range faults before transfer.

## Sensors

Inter-robot ranges emulated from motion-capture and simulator poses.

## Compute and latency

Monitor centralized at a ground station in hardware, despite a distributed SCP/ADMM formulation.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 7).

## Stated limitations

A complete author-stated limitation inventory was not assessed in this targeted reading. The inspected implementation and protocol boundaries are recorded under Platform and setup and Transfer conditions.

## Transfer conditions

Separate formulation, evaluated placement and physical sensing; verify communication costs and actual range faults before transfer.

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
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 7, Selected source passage.** "is implemented centrally"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Range consistency supports shared-state fault reconstruction in a centralized mixed-reality experiment.
- Separate formulation, evaluated placement and physical sensing; verify communication costs and actual range faults before transfer.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. The hardware implementation is centralized (p. 7); a complete limitations inventory was not assessed.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 2, 6, 7; Abstract/contributions and selected simulation, emulated sensing and hardware implementation passages. Complete algorithm/proof not audited; no performance numbers retained. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—Coordination of multi-robot systems (MRSs) relies on**
**efficient** **sensing** **and** **reliable** **communication** **among** **the** **robots.**
**However, the sensors and communication channels of these robots**
**are often vulnerable to cyberattacks and faults, which can disrupt**
**their individual behavior and the overall objective of the MRS. In**
**this** **work,** **we** **present** **a** **multi-robot** **integrity** **monitoring** **frame-**
**work that utilizes inter-robot range measurements to (i) detect the**
**presence of cyberattacks or faults affecting the MRS, (ii) identify**
**the affected robot(s), and (iii) reconstruct the resulting localization**
**error of these robot(s). The proposed iterative algorithm leverages**
**sequential convex programming and alternating direction of multi-**
**pliers method to enable real-time and distributed implementation.**
**Our approach is validated using numerical simulations and demon-**
**stratedusingPX4-SiTLinGazeboonanMRS,wherecertainagents**
**deviate from their desired position due to a GNSS spoofing attack.**
**Furthermore, we demonstrate the scalability and interoperability**
**of our algorithm through mixed-reality experiments by forming a**
**heterogeneous** **MRS** **comprising** **real** **Crazyflie** **UAVs** **and** **virtual**
**PX4-SiTL UAVs working in tandem.**
