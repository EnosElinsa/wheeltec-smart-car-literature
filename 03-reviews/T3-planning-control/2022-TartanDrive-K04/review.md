# TartanDrive: A Large-Scale Dataset for Learning Off-Road Dynamics Models

## Metadata

| Field | Value |
|---|---|
| ID | K04 |
| Title | TartanDrive: A Large-Scale Dataset for Learning Off-Road Dynamics Models |
| Authors | Samuel Triest, Matthew Sivaprakasam, Sean J. Wang, Wenshan Wang, Aaron M. Johnson, and Sebastian Scherer |
| Venue | 2022 International Conference on Robotics and Automation (ICRA) |
| Year | 2022 |
| Type | conference |
| DOI | [10.1109/icra46639.2022.9811648](https://doi.org/10.1109/icra46639.2022.9811648) |
| Official URL | https://ieeexplore.ieee.org/document/9811648/ |
| Theme folder | T3-planning-control |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T3-planning-control/2022-TartanDrive-K04/paper.pdf` and `02-fulltext/T3-planning-control/2022-TartanDrive-K04/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2022-TartanDrive-K04/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: dataset-resource
- evidence_all: dataset-resource, recorded-robot-data
- protocol_caveats: joystick-driving
- platform_class: road-vehicle
- platform: Modified Yamaha Viking ATV with throttle and steering servos driven by joystick; a human driver controls the brakes (p. 3).
- boundary_platform: yes
- degradation: terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Seven sensing modalities, including RGB images, heightmaps, IMU, shock travel and wheel RPM (pp. 1, 3)
- compute: Not inspected in this reading.
- compute_location: not-reported
- summary_result: About 200,000 interactions in 630 trajectories; vision-based modalities help dynamics prediction more on a separate, more uneven evaluation set (pp. 1, 3, 6).
- summary_limitation: Whether the improved dynamics prediction suffices for navigation over rough terrain remains to be seen; integration into a navigation stack is future work (p. 6).
- survey_included: yes
- verification_level: light

## Problem

Learning off-road dynamics needs far more interaction data than scene-understanding datasets provide. TartanDrive records actions and multi-modal observations for dynamics prediction (pp. 1-2).

## Mechanism

A latent-space dynamics model takes the initial state, an action sequence and multi-modal observations and predicts future states; the benchmark varies input modalities and training objectives (pp. 4-6).

## Baselines and controls

Time-series models from proprioception and latent-space models with image, map and proprioceptive inputs; auxiliary reconstruction losses are ablated (p. 6).

## Platform and setup

Teleoperated driving through tall grass, rocks and mud; 630 trajectories, five hours of data at 10 Hz; each trajectory ends when the driver brakes (p. 3). A separate evaluation set in more uneven terrain has a median difficulty of 0.2253 m/s versus 0.0866 m/s for the original set (p. 6).

## Evidence type and transfer

Strongest coded setting: `dataset-resource` from the authors' recorded vehicle data. Results are open-loop prediction errors; no planner uses the models. The two evaluation sets differ by a named terrain difficulty, so `designed-degradation` is coded. The provisional module `traversability-planning-control` is confirmed: the data target learned dynamics for off-road planning. The ATV carries passengers and follows the Polaris RZR precedent (S46), so it is coded `road-vehicle` and treated as boundary evidence.

## Sensors

Seven sensing modalities, among them RGB images, heightmaps and RGB maps, IMU, shock position and wheel RPM; wheel data are upsampled from 50 Hz to 200 Hz (pp. 1, 3).

## Compute and latency

Not inspected in this reading.

## Key quantitative results

- About 200,000 off-road driving interactions with seven sensing modalities (p. 1).
- 630 trajectories equivalent to five hours of data, recorded at 10 Hz (p. 3).
- RELLIS-3D, by comparison, has about 20 minutes or 12,000 datapoints of trajectory data (p. 2).
- In the uneven evaluation set, 87% of trajectories exceed the median difficulty of the original set (p. 6).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Incorporating the models into a navigation stack is future work; whether the improved prediction suffices for intelligent navigation over rough terrain remains to be seen (p. 6).
- Future observations are hard to predict without mapping and prior traversal, so auxiliary sensory prediction yields little gain (p. 6).

## Transfer conditions

The data come from a passenger ATV with human braking; a small wheeled robot has different dynamics and sensor heights. No closed-loop use is shown.

## Code and data

The dataset is announced at https://github.com/castacks/tartan_drive (p. 1); availability was not checked.

## Version family

Counted once by the registered ICRA 2022 identity. GNM (K13) uses TartanDrive as one of its training datasets.

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

- **p. 3, Sec. III-A.** "For safety reasons, the brakes were controlled directly by a human driver."
  Human-in-the-loop data collection behind the joystick-driving caveat.
- **p. 3, Sec. III-B.** "In total, we collected 630 trajectories equivalent to five hours of data."
  Data volume of the release.
- **p. 6, Sec. VI.** "An obvious direction for future work is the incorporation of these models into a navigation stack."
  No closed-loop use of the learned dynamics is reported.
- **p. 6, Sec. V.** "Overall, we observe that the additional vision-based modalities are more beneficial in the more challenging scenarios."
  The benefit of exteroception depends on terrain difficulty.

## Survey-usable statements

### Supported

- TartanDrive provides about 200,000 off-road interactions for learning vehicle dynamics, recorded on a passenger ATV.
- Exteroceptive inputs improve open-loop dynamics prediction more on uneven terrain.

### Not supported

- The paper does not show that the learned models improve closed-loop navigation.
- Results do not transfer directly to small wheeled robots.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 4, 6; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

We present TartanDrive, a large scale dataset for learning dynamics models for off-road driving. We collected a dataset of roughly 200,000 off-road driving interactions on a modified Yamaha Viking ATV with seven unique sensing modalities in diverse terrains. To the authors' knowledge, this is the largest real-world multi-modal off-road driving dataset, both in terms of number of interactions and sensing modalities. We also benchmark several state-of-the-art methods for model-based reinforcement learning from high-dimensional observations on this dataset. We find that extending these models to multi-modality leads to significant performance on off-road dynamics prediction, especially in more challenging terrains. We also identify some shortcomings with current neural network architectures for the off-road driving task. Our dataset is available at https://github.com/castacks/tartan_drive.
