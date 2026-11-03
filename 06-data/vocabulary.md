# Controlled vocabulary for review coding

Every `review.md` in `03-reviews/` starts with a **Survey coding** block. The
block uses only the values defined here, so that `tools/build_tables.py` can
turn the reviews into tables and statistics without manual editing.
`tools/review_check.py` rejects any value that is not listed in this file.

Multi-valued fields use comma-separated values in the order given below.

## Fields and allowed values

### `survey_module` (one value) and `secondary_modules` (zero or more)

The module of the autonomy stack that the paper mainly contributes to. The
module decides where the paper is discussed in the survey. It can differ from
the theme folder, which follows the original reading frame.

| Value | Meaning |
|---|---|
| `localization-mapping` | State estimation, odometry, SLAM, relocalization, mapping, datasets for these tasks. |
| `traversability-planning-control` | Traversability, exploration planning, local and global motion planning, tracking control, learned local motion, crowd navigation. |
| `semantic-language-navigation` | Semantic maps, open-vocabulary and language-conditioned navigation, vision-language models in the motion loop, social navigation driven by semantics. |
| `multi-robot` | Multi-robot exploration, collaborative SLAM, map merging, cooperative localization, team task allocation, formation control. |
| `fault-recovery-deployment` | Localization integrity, fault detection and fault-tolerant control, recovery behaviors, runtime monitoring, energy and long-term deployment. |

`secondary_modules` is `none` when the paper has no secondary module.

### `evidence_type` (one value) and `evidence_all` (one or more)

`evidence_type` is the strongest evidence setting that the paper reports, in
this order of strength: `closed-loop-hardware` > `online-hardware` >
`recorded-robot-data` > `dataset-playback` > `simulation` > `numerical` >
`theory-only`. `survey` and `dataset-resource` describe the kind of
contribution instead.

| Value | Meaning |
|---|---|
| `closed-loop-hardware` | The method runs online on a physical robot and its output drives the robot (including autonomous navigation after teleoperated mapping). |
| `online-hardware` | The method runs online on a physical robot while it moves, but the paper does not show that the method's output drives the robot (for example a real-time estimator evaluated beside an existing controller). |
| `recorded-robot-data` | The method runs on sensor data that the authors recorded on their own physical robot or vehicle, with no closed control loop. |
| `dataset-playback` | The method runs only on public datasets recorded by others. |
| `simulation` | Physics or sensor simulation (for example Gazebo, Isaac Sim, Habitat, CARLA). |
| `numerical` | Numerical integration of an abstract model with no sensor simulation. |
| `theory-only` | Analysis or proofs without an experiment. |
| `survey` | The paper is a literature review. |
| `dataset-resource` | The main contribution is a dataset or benchmark. |

### `protocol_caveats` (zero or more)

Conditions that limit what the strongest evidence setting can show. Caveats
apply to the setting that produces the paper's tabulated headline results.
Side demonstrations without metrics (for example a teleoperated long-range
demo or cross-embodiment videos) are described in the prose, not coded here.
Use `none` when no caveat applies.

| Value | Meaning |
|---|---|
| `teleoperated-mapping` | The map or prior was built under teleoperation before the autonomous run. |
| `joystick-driving` | Data were collected while a person drove the robot. |
| `pushed-capture` | The robot or sensor rig was pushed by hand. |
| `video-only-hardware` | Hardware evidence is a video, or figures and plots without tabulated numeric metrics. |
| `motion-capture-pose` | Pose came from motion capture (for example Vicon or OptiTrack). |
| `external-pose-source` | Pose came from a source other than the evaluated method (RTK, external odometry, ground truth). |
| `offboard-compute` | The evaluated computation ran on a remote PC, laptop, or server. |
| `cloud-model` | A cloud-hosted foundation model was queried. |
| `speed-capped` | The physical tests were limited to low speed by design. |
| `scripted-scenario` | Pedestrians, obstacles, or events were scripted or staged. |
| `few-trials` | The hardware result rests on a small number of runs without statistics. |
| `simulated-agents-on-hardware` | Obstacles or agents were virtual while the robot was physical. |

### `platform_class` (one value)

The class of the robot or vehicle, physical or simulated, used in the
strongest evidence setting. When a paper uses several platforms in that
setting, a wheeled ground robot takes precedence; among wheeled classes, the
majority class is used. For dataset-only papers, use the class that carries
the majority of the sequences used; use `mixed` when no class is a majority
or when the carriers are only partly identified.

The drive type must come from the paper's text, from a cited external
source, or from a figure; the review states which ("inferred from Fig. 8").
When the paper shows a wheeled robot but gives no drive type, use
`wheeled-unspecified`.

| Value | Meaning |
|---|---|
| `differential-drive` | Two independently driven wheels (unicycle kinematics), including TurtleBot and Kobuki. |
| `skid-steer` | Four or six wheels steered by speed difference (for example Clearpath Jackal and Husky, AgileX Scout). |
| `ackermann` | Car-like steering (for example small Ackermann research cars). |
| `omnidirectional` | Mecanum or omni wheels. |
| `wheeled-unspecified` | A wheeled ground robot whose drive type the paper does not report. |
| `tracked` | Tracks or flippers. |
| `legged` | Quadruped or other legged robot. |
| `aerial` | Multirotor or other aerial vehicle. |
| `aquatic` | Underwater or surface robot, including a gliding robotic fish; boundary evidence for wheeled-platform transfer. |
| `road-vehicle` | Passenger car, instrumented vehicle, or vehicle roof rack. |
| `handheld` | Handheld sensor rig. |
| `mixed` | Datasets that combine several of the classes above with no single dominant class. |
| `none` | No platform (surveys, pure theory). |

`platform` (free text) names the robot models, for example `Clearpath Jackal`.

### `boundary_platform` (`yes` or `no`)

`yes` when `platform_class` is not a wheeled ground robot
(`tracked`, `legged`, `aerial`, `aquatic`, `road-vehicle`, `handheld`, `mixed`, `none`).
Boundary papers are included only for a transferable mechanism or as the
nearest counterexample, and the survey labels them as such.

### `degradation` and `degradation_observed` (zero or more each)

`degradation` lists the conditions that the evaluation deliberately includes:
designed, injected, varied, or deliberately selected (for example degenerate
sequences chosen for that property), so that the results speak to them.
`degradation_observed` lists conditions that occurred and are reported but
were not designed into the evaluation, as in field studies. A condition that
appears only as motivation is not coded. Each field is `none` when empty.

| Value | Meaning |
|---|---|
| `visual-degradation` | Illumination change, darkness, low texture, motion blur, visual dropout. |
| `lidar-degeneracy` | Geometric degeneracy, sparse or missing LiDAR returns, LiDAR dropout. |
| `gnss-denial` | GNSS outage, multipath, or deliberate disabling. |
| `dynamic-objects` | Pedestrians, vehicles, or other moving obstacles. |
| `scene-change` | Map aging, layout change, object relocation, long-term change. |
| `terrain` | Uneven, rough, sloped, vegetated, or deformable ground; negative obstacles. |
| `wheel-slip` | Wheel slip, skidding, or wheel-ground model mismatch. |
| `actuator-fault` | Loss of actuator effectiveness, bias, saturation, or failure. |
| `sensor-fault` | Sensor failure, bias, corruption, or attack. |
| `data-association-fault` | Wrong or missing feature or landmark association. |
| `communication-delay-loss` | Delay, jitter, or packet loss. |
| `communication-partition` | Loss of connectivity between robots or to a server. |
| `bandwidth-limit` | Limited data rate. |
| `compute-limit` | Limited onboard compute or memory. |
| `model-error` | Errors of learned or foundation models, out-of-distribution inputs. |
| `energy-limit` | Battery and charging constraints. |
| `none` | No condition of this kind. |

### `evaluation_primary` (one value) and `evaluation_all` (one or more)

What the paper treats as its decision-relevant result.

| Value | Meaning |
|---|---|
| `residual` | An estimator or segmenter error: trajectory error, recall, mIoU, map error, runtime of a module. |
| `closed-loop-task` | A mission outcome of the robot: success, collision, coverage, traversal time, interventions. |
| `designed-degradation` | A named operating condition from `degradation` (designed, injected, varied, or deliberately selected) is reported with results per condition (for example map age, slip, communication cutoff). Used in `evaluation_all`; it is `evaluation_primary` only when the condition itself is the result, as in diagnostic datasets. |
| `integrity-reliability` | A probability or detector output about hazardous error, failure, or anomaly that is distinct from a covariance envelope or tracking error. |

### `compute_location` (one value)

Where the evaluated computation ran in the strongest evidence setting.

| Value | Meaning |
|---|---|
| `onboard` | On the robot. |
| `offboard-local` | On a nearby PC, laptop, or server connected to a live robot. |
| `desktop-offline` | On a desktop, workstation, or server that processes recorded data without a live robot. |
| `cloud` | On a remote cloud service. |
| `mixed` | Parts with different roles run in different places (for example onboard control and cloud language queries), or different result tables come from different machines; the Compute section says which. |
| `not-reported` | The paper does not say. |
| `not-applicable` | No computation was evaluated (surveys, theory). |

### `survey_included`

| Value | Meaning |
|---|---|
| `yes` | Reviewed corpus. Counted in statistics and discussed in the survey. |
| `context` | Classic, pre-2021, or survey work cited for background or lineage. Not counted in corpus statistics. |
| `no` | Reviewed but not included (for example a follow-up candidate that fails an inclusion criterion). |

### `verification_level` (one value)

How thoroughly the review was checked against the paper.

| Value | Meaning |
|---|---|
| `full` | The whole paper was read, every number in the review was checked against the paper, and table values were read from rendered page images. |
| `light` | A limited review: either conversion of a legacy extraction, or a new targeted reading whose selected sections/pages are recorded. Metadata, abstract, and excerpts are checked against the sources. It does not imply a whole-paper or complete numeric audit; the survey must re-check cited numbers against the PDF. |

### Free-text coding fields

| Field | Content |
|---|---|
| `platform` | Robot or vehicle names. |
| `sensors` | Sensors used by the method, short form. |
| `compute` | Processor and the main timing number, short form. |
| `summary_result` | One sentence (at most 30 words) with the main quantitative result and its condition, in the order "method versus comparator". |
| `summary_limitation` | One sentence (at most 30 words) that repeats the main limitation stated by the authors, or "No limitation is stated by the authors;" followed by the main scope condition. |

## Claim relations C1 to C6

Each review records how the paper relates to six working claims of the
library. The claims are hypotheses of this project, not findings of the
literature.

| ID | Working claim |
|---|---|
| C1 | The six theme folders are a useful reading frame for wheeled-robot autonomy research. (Reading frame only; no paper is expected to prove it.) |
| C2 | Sensing degradation and dynamic environments degrade localization and navigation. |
| C3 | Learning-based navigation is constrained by sim-to-real transfer, safety, data, and compute. |
| C4 | Multi-robot systems add communication, coordination, scalability, and heterogeneity constraints. |
| C5 | Long-term autonomy needs failure detection, uncertainty estimation, recovery, and system-level evaluation. |
| C6 | Transfer to the reference platform needs a mechanism-level basis and hardware reproducibility. |

| Relation | Meaning |
|---|---|
| `direct-support` | The full text states or shows the claim. |
| `partial-support` | The full text supports part of the claim or supports it under narrower conditions. |
| `qualifies` | The full text limits the scope of the claim. |
| `contradicts` | The full text contradicts the claim. |
| `unset` | The paper does not bear on the claim. |

Strength is `strong`, `moderate`, `weak`, or `n/a` (for `unset`). The excerpt
of a claim row must itself show the chosen relation: a `qualifies` row needs
an excerpt that states a limit, not one that reads as support.

## Inclusion rule for follow-up candidates

A follow-up candidate (`F` series) is included in the survey (`survey_included: yes`)
only when all three conditions hold:

1. The evaluated platform is a wheeled or other ground robot, or the mechanism
   transfers to wheeled robots and the review sets `boundary_platform: yes`.
2. The paper changes or qualifies a specific statement or gap of the survey,
   and the review names it.
3. The paper is not a version of a work that is already in the library
   (conference and journal versions of one work count once).
