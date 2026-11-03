# Indoor Visual Re-Localization for Long-Term Autonomous Robots Based on Object-Level Features and Semantic Relationships

## Metadata

| Field | Value |
|---|---|
| ID | M34 |
| Title | Indoor Visual Re-Localization for Long-Term Autonomous Robots Based on Object-Level Features and Semantic Relationships |
| Authors | Yuanyan Xie, Yu Guo, Zhenqiang Mi, Xiaokun Wang, Yang Yang, and Mohammad S. Obaidat |
| Venue | IEEE Robotics and Automation Letters, vol. 8, no. 2, pp. 840-847 |
| Year | 2023 (online 2022) |
| Type | journal |
| DOI | [10.1109/lra.2022.3233235](https://doi.org/10.1109/lra.2022.3233235) |
| Official URL | https://ieeexplore.ieee.org/document/10003641/ |
| Theme folder | T1-perception-localization |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T1-perception-localization/2023-object-relocalization-M34/paper.pdf` and `02-fulltext/T1-perception-localization/2023-object-relocalization-M34/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2023-object-relocalization-M34/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: scripted-scenario
- platform_class: wheeled-unspecified
- platform: TurtleBot3 with Kinect V2 (IndoorVR-OC); OpenLORIS-Scene and InteriorNet datasets
- boundary_platform: no
- degradation: scene-change, visual-degradation
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: RGB-D camera (Kinect V2 on TurtleBot3; OpenLORIS RGB-D cameras)
- compute: not recorded in the legacy extraction
- compute_location: not-reported
- summary_result: Under object changes, the scene-graph method loses less Recall@5 than DBoW3 and NetVLAD; under illumination change it performs comparably; values not recorded.
- summary_limitation: Featureless corridors are out of scope, and real-time operation for rigorous robotic applications is left to future work.
- survey_included: yes
- verification_level: light

## Problem

Indoor long-term visual relocalization is dominated by object-layout change
from human interaction, not only by day-night or weather change. DBoW3 and
NetVLAD, which succeed in static rooms, degrade when objects move or the
lighting changes.

## Mechanism

Each scene is a graph of object-level nodes plus semantic relationships
(prior knowledge plus the current layout). Relocalization is graph matching
with random-walk object association and a feature-reweighting step that
down-weights outliers. A pose counts as correct when the translation error is
below 0.25 m and the orientation error below 5 degrees.

## Baselines and controls

The comparators are DBoW3, NetVLAD, and an object-plus-topology baseline.
The ablation removes the scene-graph model or the feature reweighting.

## Platform and setup

Three data sources: OpenLORIS-Scene RGB-D (corridors excluded as
featureless); InteriorNet synthetic indoor scenes with controllable lights
and layouts; and the authors' IndoorVR-OC dataset, collected with a
TurtleBot3 and a Kinect V2, with objects moved, replaced, or deformed under
fixed lighting.

## Evidence type and transfer

The strongest setting is RGB-D data recorded with the authors' TurtleBot3
and evaluated offline. The object changes in IndoorVR-OC were made by the
authors, so the changes are staged rather than observed in long-term use.
The drive type of the TurtleBot3 is not recorded in the legacy extraction,
so the platform is coded as wheeled-unspecified.

## Sensors

RGB-D cameras: the OpenLORIS RGB-D cameras and a Kinect V2 on the
TurtleBot3.

## Compute and latency

Not recorded in the legacy extraction; not verified. The authors state that
real-time operation is future work.

## Key quantitative results

- Correct-pose threshold: translation error below 0.25 m and orientation error below 5 degrees (p. 6).
- Recall@5 and precision-recall: DBoW3 and NetVLAD stay high in static scenes but drop sharply under object or illumination change; the scene-graph method degrades less and beats the object-plus-topology baseline; the abstract describes performance under illumination change as comparable to the state of the art; the legacy extraction records no values (p. 7).
- Ablation without the scene-graph model or without feature reweighting lowers recall; no values and no page recorded.

## Stated limitations

- Featureless corridors are out of scope (p. 6).
- Real-time onboard use is deferred: future work will speed up the method for more rigorous robotic applications, building on the authors' cloud-robotics work (p. 8).

## Transfer conditions

The TurtleBot3 RGB-D capture is used to build a dataset; the authors still
treat real-time onboard relocalization as unmet. The object changes were
staged by the authors, and featureless corridors were excluded.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | strong | Sec. V-B, p. 7 | "The results show that DBoW3 and NetVLAD can re-localize query images with high recalls in static environments, but suffer drastic performance degradation in changing environments." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VI, p. 8 | "In the future, we will focus on the optimization of our relocalization method and speed up our approaches to satisfy the real-time requirements for more rigorous robotic applications based on our previous work on cloud robotics [29]." |

## Page-cited excerpts

- **p. 7, Sec. V-B.** "The results show that DBoW3 and NetVLAD can re-localize query images with high recalls in static environments, but suffer drastic performance degradation in changing environments."
  Scene change degrades appearance-based relocalization baselines.
- **p. 8, Sec. VI.** "In the future, we will focus on the optimization of our relocalization method and speed up our approaches to satisfy the real-time requirements for more rigorous robotic applications based on our previous work on cloud robotics [29]."
  The method does not yet meet real-time requirements.

## Survey-usable statements

### Supported

- Object-level scene graphs with graph matching make indoor relocalization less sensitive to object rearrangement than DBoW3 and NetVLAD on staged changes.
- Appearance-based relocalization (DBoW3, NetVLAD) degrades sharply under object and illumination change.

### Not supported

- The method runs in real time on a robot: the authors leave real-time operation to future work.
- The method works in featureless corridors: corridors were excluded.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); no legacy quote dropped; staged object changes moved from Stated limitations to Evidence type and Transfer conditions as a reviewer observation
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Visual re-localization has become one of the key technologies for long-term autonomous robots. Existing methods, mostly focusing on addressing day-night, weather, and seasonal changes, are not applicable in indoor scenarios. At the same time, the layouts of objects in indoor scenes are highly dynamic over time due to human interactions with the environment, which makes indoor re-localization challenging. This letter presents a novel indoor visual re-localization method for long-term autonomous robots. First, a scene graph model is proposed, incorporating object-level features and semantic relationships, which overcomes the influence of dynamic objects by understanding the interactions among objects. Then, a visual re-localization method is developed based on the proposed scene graph model. It adopts graph matching technologies to incorporate pairwise object interactions as important features for re-localization, and designs a feature reweighting strategy to further reduce the impact of outliers in dynamic scenes. The proposed re-localization method has been verified in both photorealistic simulation environments and real-world scenarios. The results show that our approach exhibits higher robustness to diverse object changes and performs comparably to the state-of-the-art methods when illumination changes occur.
