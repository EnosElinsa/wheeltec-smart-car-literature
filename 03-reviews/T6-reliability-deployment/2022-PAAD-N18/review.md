# Proactive Anomaly Detection for Robot Navigation With Multi-Sensor Fusion

## Metadata

| Field | Value |
|---|---|
| ID | N18 |
| Title | Proactive Anomaly Detection for Robot Navigation With Multi-Sensor Fusion |
| Authors | Tianchen Ji, Arun Narenthiran Sivakumar, Girish Chowdhary, Katherine Driggs-Campbell |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2022 |
| Type | journal |
| DOI | [10.1109/lra.2022.3153989](https://doi.org/10.1109/lra.2022.3153989) |
| Official URL | https://ieeexplore.ieee.org/document/9720937/ |
| Theme folder | T6-reliability-deployment |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2022-PAAD-N18/paper.pdf` and `02-fulltext/T6-reliability-deployment/2022-PAAD-N18/paper.md` (local only); [publisher BibTeX](../../../01-papers/T6-reliability-deployment/2022-PAAD-N18/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: People reposition the robot after field failures; the monitored output is not shown driving an autonomous recovery response.
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Planned path, RGB images and LiDAR observations
- compute: Streaming rosbag test; physical alert-to-command deployment not established
- compute_location: desktop-offline
- summary_result: Path-conditioned multimodal prediction is evaluated on recorded field navigation, with a separate rosbag timing test.
- summary_limitation: The inspected real-time evaluation is performed on rosbag streams (p. 7); a complete author limitation inventory was not assessed.
- survey_included: yes
- verification_level: light

## Problem

Path-conditioned visual and geometric cues may predict upcoming field-navigation failures.

## Mechanism

PAAD combines the planned path with RGB and LiDAR information for predictive anomaly detection (pp. 1, 3-5).

## Baselines and controls

TerraSentia field data provide prediction examples; the real-time test streams recorded rosbags (p. 7, footnote 3).

## Platform and setup

People reposition the robot after field failures; the monitored output is not shown driving an autonomous recovery response.

## Evidence type and transfer

The strongest inspected setting is `recorded-robot-data`. Measure alert timing and subsequent safe action before inferring closed-loop recovery from predictive detection accuracy.

## Sensors

Planned path, RGB images and LiDAR observations.

## Compute and latency

Streaming rosbag test; physical alert-to-command deployment not established.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 8).

## Stated limitations

A complete author-stated limitation inventory was not assessed in this targeted reading. The inspected implementation and protocol boundaries are recorded under Platform and setup and Transfer conditions.

## Transfer conditions

Measure alert timing and subsequent safe action before inferring closed-loop recovery from predictive detection accuracy.

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

- **p. 7, Selected source passage.** "was performed on streaming data from rosbags"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Path-conditioned multimodal prediction is evaluated on recorded field navigation, with a separate rosbag timing test.
- Measure alert timing and subsequent safe action before inferring closed-loop recovery from predictive detection accuracy.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. The inspected real-time evaluation is performed on rosbag streams (p. 7); a complete author limitation inventory was not assessed.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 3, 4, 5, 7, 8; Selected abstract, method/input and data collection, experimental setup, real-time replay test including footnote 3, limitations and conclusion. Rendered p. 7 checked; no table numbers retained. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—Despite** **the** **rapid** **advancement** **of** **navigation** **algo-**
**rithms, mobile robots often produce anomalous behaviors that can**
**lead to navigation failures. The ability to detect such anomalous be-**
**haviors is a key component in modern robots to achieve high-levels**
**of autonomy. Reactive anomaly detection methods identify anoma-**
**lous task executions based on the current robot state and thus lack**
**the ability to alert the robot before an actual failure occurs. Such an**
**alert delay is undesirable due to the potential damage to both the**
**robotandthesurroundingobjects.Weproposeaproactiveanomaly**
**detection** **network** **(PAAD)** **for** **robot** **navigation** **in** **unstructured**
**and** **uncertain** **environments.** **PAAD** **predicts** **the** **probability** **of**
**future** **failure** **based** **on** **the** **planned** **motions** **from** **the** **predictive**
**controller** **and** **the** **current** **observation** **from** **the** **perception** **mod-**
**ule.** **Multi-sensor** **signals** **are** **fused** **effectively** **to** **provide** **robust**
**anomaly detection in the presence of sensor occlusion as seen in field**
**environments.** **Our** **experiments** **on** **field** **robot** **data** **demonstrates**
**superior failure identification performance than previous methods,**
**and that our model can capture anomalous behaviors in real-time**
**while maintaining a low false detection rate in cluttered fields. Code**
**[is available at https://github.com/tianchenji/PAAD.](https://github.com/tianchenji/PAAD)**
