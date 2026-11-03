# ProbPer-LiLo: Probabilistic Persistency Modeling for Life-Long Mapping

## Metadata

| Field | Value |
|---|---|
| ID | E16 |
| Title | ProbPer-LiLo: Probabilistic Persistency Modeling for Life-Long Mapping |
| Authors | Waqas Ali, Yixi Cai, Patric Jensfelt, and Thien-Minh Nguyen |
| Venue | IEEE Robotics and Automation Letters, vol. 11, no. 3, pp. 2530-2537 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3653311](https://doi.org/10.1109/lra.2026.3653311) |
| Official URL | https://ieeexplore.ieee.org/document/11345986/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-ProbPer-LiLo-E16/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-ProbPer-LiLo-E16/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2026-ProbPer-LiLo-E16/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: MCD campus sequences (KTH and NTU) and the authors' MCDll extension; carriers not recorded in the legacy extraction
- boundary_platform: yes
- degradation: dynamic-objects, scene-change
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: 3D LiDAR (Ouster 64-beam at KTH; Ouster 128-beam old and Livox Mid-360 new at NTU); point-wise semantic labels as input
- compute: not reported
- compute_location: not-reported
- summary_result: On experiment E6, ProbPer-LiLo reaches 0.485 m AWD versus 1.045 m for ELite and 1.112 m for LT-mapper, with 77.40% completeness versus 33.36% and 5.47%.
- summary_limitation: The authors assume that the clustering is correct and that both maps contain point-wise semantic labels.
- survey_included: yes
- verification_level: light

## Problem

In LiDAR maps that span years, quasi-static objects appear and disappear, which harms map completeness and localization. Binary map replacement carries no persistence or semantic information.

## Mechanism

A discrete factor graph jointly models cluster-level semantics and cross-session persistence with an exponential survival prior. Voxel geometry, normals, and semantics sort changes into five classes, and persistence-filtered and persistence-merged (PF/PM) maps with time weights fuse the new and old maps.

## Baselines and controls

LT-mapper and ELite; six experiments with different priors and update settings; map metrics AWD, CD, AC, and COM.

## Platform and setup

Old MCD maps of the KTH and NTU campuses and three newly collected MCDll sequences more than two years later. Replay of the two campus datasets; the two NTU updates are about four months apart (legacy statement; not located).

## Evidence type and transfer

Map updates on real point-cloud maps that span years. There is no new closed-loop robot deployment and no end-to-end navigation success rate.

## Sensors

KTH: Ouster 64-beam LiDAR. NTU: Ouster 128-beam in the old sessions and Livox Mid-360 in the new ones. The input maps are aligned and carry point-wise semantic labels; labels of the new map can be inherited from neighbors.

## Compute and latency

The text reports no CPU or GPU model, runtime, or peak memory, so embedded real-time operation cannot be claimed.

## Key quantitative results

- Experiment E6, ProbPer-LiLo versus ELite and LT-mapper: AWD 0.485 m versus 1.045 m and 1.112 m; CD 0.960 versus 5.461 and 12.77; COM 77.40% versus 33.36% and 5.47% (legacy location: Table II, page 7; the table values are not in the PDF text layer).
- Counterexamples: in E1 the CD of ProbPer-LiLo (0.345) is worse than ELite (0.234); in E6 the AC of ProbPer-LiLo (0.086) is worse than LT-mapper (0.060), whose completeness is low (legacy location: Table II, page 7; not in the PDF text layer).

## Stated limitations

- Both input maps are assumed to contain point-wise semantic labels (p. 3).
- The persistence model assumes that the clustering is correct (p. 5).

## Transfer conditions

Legacy reviewer observations: the method depends on aligned input maps and semantic labels, and segmentation or association failures would corrupt the survival estimates. The evaluation covers two campuses and few sessions across years, and computational scaling is not quantified. The supplementary material was not read. A wheeled reuse needs a semantic LiDAR segmentation front end and aligned sessions.

## Code and data

The text promises that code and resources will be released. Reference [40] on p. 8 gives a supplementary PDF at https://github.com/KTH-RPL/LifelongProbMapper/blob/main/Supplementary.pdf, which identifies the repository; code availability and reproduction were not checked. MCD is public; the release status of the extension dataset was not checked.

## Version family

ProbPer-LiLo is an independent work. ELite (E18) and the lifelong mapping work used as baselines are not versions of it.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Abstract, p. 1 | "Change is an ever-persistent force in our world and with the evolution of a scene its 3D map becomes outdated." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | weak | Input assumptions, p. 3 | "We assume that both maps contain point-wise semantic labels." |

## Page-cited excerpts

- **p. 3, Input assumptions.** "We assume that both maps contain point-wise semantic labels."
  The method needs point-wise semantics as input.
- **p. 5, Persistence assumptions.** "We assume that the clustering is correct"
  The persistence model is correct only under correct clustering.
- **p. 6, Datasets.** "There is a time gap of more than two years between the MCD dataset and MCDll dataset."
  The span of real long-term change in the data.
- **p. 1, Abstract.** "Change is an ever-persistent force in our world and with the evolution of a scene its 3D map becomes outdated."
  The authors' motivation: maps age with scene change.

## Survey-usable statements

### Supported

- Probabilistic persistence modeling of quasi-static clusters updates campus LiDAR maps across a gap of more than two years, with better AWD, CD, and completeness than ELite and LT-mapper in experiment E6 (numbers from a light review; re-check before citing).

### Not supported

- ProbPer-LiLo is best on every metric: in E1 its CD is worse than ELite, and in E6 its AC is worse than LT-mapper.
- The method improves navigation of a deployed robot: no closed-loop deployment or navigation metric is reported.
- The method runs in real time onboard: no runtime or hardware is reported.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese card converted to the English template; no legacy quote dropped; Table II values kept without a page because they are not in the PDF text layer; reviewer observations moved from limitations to Transfer conditions
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/a9e709525d4ae8ad7dce4ea0/

## Original abstract

3D mapping is vital for a broad range of applications that rely on a consistent and accurate representation of the environment. Change is an ever-persistent force in our world and with the evolution of a scene its 3D map becomes outdated. Thus, a mapping framework that can adapt and refine the 3D maps with the changes in the scene is necessary. In this letter, we propose a lifelong mapping framework where map maintenance is based on two objectives including the preservation of static structures and the refinement of the 3D map. To preserve only the static structures, we classify the object’s state and remove the dynamic objects and the quasi-static objects, i.e., objects which temporarily appear static. For classifying the state of objects, we propose a discrete probabilistic solution utilizing a factor graph. Using this classification, we generate static maps from multiple sessions which are used for map refinement. The refinement is based on change detection and map update, leveraging semantic and geometric information. For the evaluation, we collect a multi-campus lifelong dataset as an extension of the MCD datasets from KTH and NTU campuses. The proposed approach is capable of accurately detecting quasi-static objects even in highly dynamic environments. Our system demonstrates state of the art performance in large scale environments. Furthermore, our approach can handle both SLAM-generated and survey-grade maps.
