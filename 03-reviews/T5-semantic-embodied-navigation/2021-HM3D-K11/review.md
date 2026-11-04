# Habitat-Matterport 3D Dataset (HM3D): 1000 Large-scale 3D Environments for Embodied AI

## Metadata

| Field | Value |
|---|---|
| ID | K11 |
| Title | Habitat-Matterport 3D Dataset (HM3D): 1000 Large-scale 3D Environments for Embodied AI |
| Authors | Santhosh Kumar Ramakrishnan, Aaron Gokaslan, Erik Wijmans, Oleksandr Maksymets, Alexander Clegg, John Turner, Eric Undersander, Wojciech Galuba, Andrew Westbury, Angel Chang, Manolis Savva, Yili Zhao, and Dhruv Batra |
| Venue | Neural Information Processing Systems Track on Datasets and Benchmarks |
| Year | 2021 |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/34173cb38f07f89ddbebc2ac9128303f-Abstract-round2.html |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2021-HM3D-K11/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2021-HM3D-K11/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2021-HM3D-K11/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: dataset-resource
- evidence_all: dataset-resource, simulation
- protocol_caveats: none
- platform_class: none
- platform: Simulated Habitat PointNav-v1 agent with RGB-D input, GPS+Compass localization and discrete 0.25 m and 10-degree actions; scans from a tripod-mounted Matterport Pro2 (pp. 4, 7).
- boundary_platform: yes
- degradation: none
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task
- sensors: Matterport Pro2 tripod-based depth sensor for the scans; the simulated agent receives 256 x 256 RGB-D and GPS+Compass readings (pp. 4, 7)
- compute: PointNav agents trained with DD-PPO for 1.5 billion frames (p. 7); hardware not inspected.
- compute_location: not-reported
- summary_result: HM3D has 1,000 scenes and 112.5k square meters of navigable space; HM3D-trained PointNav agents reach 100% performance on the Gibson test set (pp. 1-2).
- summary_limitation: Object semantics and physical attributes are left to future extensions, which would enable ObjectGoal navigation and rearrangement (p. 10).
- survey_included: yes
- verification_level: light

## Problem

Embodied AI agents are trained in reconstructed indoor scenes, and existing building-scale datasets are small or incomplete. HM3D offers 1,000 building-scale reconstructions for training and evaluation in Habitat (pp. 1-2).

## Mechanism

Real-world interiors were scanned with a Matterport Pro2 tripod-based depth sensor and reconstructed into textured meshes by the Matterport pipeline; volunteer annotators rated scene quality, reconstruction artifacts and furnishing before release (p. 4). The paper compares scale, completeness and visual fidelity with Replica, MP3D, Gibson and ScanNet and trains PointNav agents on each dataset (pp. 5-9).

## Baselines and controls

Replica, RoboTHOR, MP3D, Gibson (including its 4+ quality subset) and ScanNet; PointNav agents trained on each dataset and evaluated across datasets (pp. 5-9).

## Platform and setup

PointNav-v1: an agent is spawned in a novel scene with a relative goal coordinate, receives RGB-D and GPS+Compass readings, and succeeds within 0.2 m after executing STOP (p. 7). Agents are trained with DD-PPO for 1.5 billion frames (p. 7).

## Evidence type and transfer

Strongest coded setting: `dataset-resource` with simulation experiments. The PointNav agent has perfect GPS+Compass localization and discrete actions, so the platform is coded `none`. The provisional module `semantic-language-navigation` is confirmed: in this library HM3D serves as the scene source for the object-goal and language-goal navigation benchmarks of VLN-Game (R28), osmAG-LLM (R27) and DualMap (M02).

## Sensors

Scans: Matterport Pro2 tripod-based depth sensor (p. 4). Simulated agent: 256 x 256 RGB-D and GPS+Compass readings (p. 7).

## Compute and latency

PointNav agents are trained with DD-PPO for 1.5 billion frames (p. 7). Hardware and training time were not inspected.

## Key quantitative results

- Scale: 1,000 scenes and 112.5k square meters of navigable space, 1.4 to 3.7 times larger than other building-scale datasets (p. 1).
- Fidelity: rendered images have 20-85% higher visual fidelity, and meshes have 34-91% fewer artifacts from incomplete reconstruction (p. 1).
- HM3D-trained PointNav agents achieve 100% performance on the Gibson test set (p. 2).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Object semantics and physical attributes are left to future extensions, which would enable ObjectGoal navigation and object rearrangement (p. 10).

## Transfer conditions

Scenes are static reconstructions of private interiors without moving objects, and the PointNav agent localizes perfectly through GPS+Compass. Success in HM3D therefore says nothing about map aging, dynamic obstacles or pose error on a physical robot.

## Code and data

The dataset, analysis code and pre-trained models are announced at https://aihabitat.org/datasets/hm3d/ (p. 2); availability was not checked.

## Version family

NeurIPS 2021 Datasets and Benchmarks Track paper (round 2); counted once. The registered citation is a derived citation that replaces only the unparsable key of the official export (see the batch evidence notes).

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

- **p. 4, Sec. 3.** "All spaces were scanned using a Matterport Pro2 tripod-based depth sensor."
  Scan source of the dataset.
- **p. 7, Sec. 4.1.** "RGB-D visual inputs, and GPS+Compass readings for localization."
  The benchmark agent receives perfect localization.
- **p. 10, Sec. 5.** "Extension of HM3D with object semantics and physical attributes in future work will enable even more embodied AI tasks such as ObjectGoal navigation and object rearrangement."
  Author-stated scope of the release.
- **p. 2, Abstract.** "HM3D-trained PointNav agents achieve 100% performance on Gibson-test dataset, suggesting that it might be time to retire that episode dataset."
  Headline cross-dataset result.

## Survey-usable statements

### Supported

- HM3D provides 1,000 building-scale indoor reconstructions that are larger and more complete than earlier academic datasets.
- PointNav agents trained on HM3D transfer across Gibson and MP3D test sets in simulation.

### Not supported

- HM3D results are not hardware evidence and do not include moving objects or localization error.
- The release itself contains no object semantics.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 4, 5, 7, 10; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

We present the Habitat-Matterport 3D (HM3D) dataset. HM3D is a large-scale dataset of 1,000 building-scale 3D reconstructions from a diverse set of real-world locations. Each scene in the dataset consists of a textured 3D mesh reconstruction of interiors such as multi-floor residences, stores, and other private indoor spaces. HM3D surpasses existing datasets available for academic research in terms of physical scale, completeness of the reconstruction, and visual fidelity. HM3D contains 112.5k m^2 of navigable space, which is 1.4 - 3.7x larger than other building-scale datasets such as MP3D and Gibson. When compared to existing photorealistic 3D datasets such as Replica, MP3D, Gibson, and ScanNet, images rendered from HM3D have 20 - 85% higher visual fidelity w.r.t. counterpart images captured with real cameras, and HM3D meshes have 34 - 91% fewer artifacts due to incomplete surface reconstruction. The increased scale, fidelity, and diversity of HM3D directly impacts the performance of embodied AI agents trained using it. In fact, we find that HM3D is 'pareto optimal' in the following sense - agents trained to perform PointGoal navigation on HM3D achieve the highest performance regardless of whether they are evaluated on HM3D, Gibson, or MP3D. No similar claim can be made about training on other datasets. HM3D-trained PointNav agents achieve 100% performance on Gibson-test dataset, suggesting that it might be time to retire that episode dataset. The HM3D dataset, analysis code, and pre-trained models are publicly released: https://aihabitat.org/datasets/hm3d/.
