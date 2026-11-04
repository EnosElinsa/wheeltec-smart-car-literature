# Degradation-evidence codebook

Version 1.0, 2026-11-04. Machine-readable form: `06-data/evidence-coding/codebook.json`. Both files state the same rules. A mechanical check (`python scripts/coding.py --check-codebook`, run in `05-survey/manuscript`) compares the attribute summary below with the JSON file.

## 1. Purpose

This codebook defines how each publication of the survey selection is coded for the degradation evidence it reports. It covers 245 works: 244 technical works and one context review. The codes feed the evidence map, the degradation-source by function matrix, the function-pair co-occurrence matrix, the interface ranking and the sensitivity analyses of the survey. A separate coder applies the same rules to a stratified random sample of 40 technical works, and agreement is computed per attribute.

All counts derived from these codes describe a purposively selected sample. They are not estimates of how often a practice occurs in the literature.

## 2. Evidence base

Codes rest on three sources per work:

- the review card, `03-reviews/<theme>/<folder>/review.md`,
- the transcription of the publication, `02-fulltext/<theme>/<folder>/paper.md` (kept locally),
- the publication PDF, `01-papers/<theme>/<folder>/paper.pdf` (kept locally).

The primary coder may also read the batch reading records `06-data/<batch>/source-reading.json`.

Each card records a `verification_level`. A **full** card reflects whole-paper reading with every number checked against the paper. A **light** card reflects a targeted reading or a converted legacy extraction. A light card supports a categorical code only through a recorded locator (Section 15). The codes themselves are categorical. Any number later taken from a light card is cited only after a page-located check against the PDF.

The card block **Survey coding** holds earlier controlled-vocabulary fields. Its fields `secondary_modules`, `degradation`, `degradation_observed` and `evaluation_all` serve as candidate values only. They do not separate the three evidence classes of Section 9, and they do not test whether a degradation condition and a task outcome come from the same experiment. Each value of this codebook is decided from the card text, the transcription or the PDF. The card blocks most often needed are Problem, Mechanism, Baselines and controls, Platform and setup, Evidence type and transfer, Key quantitative results, Stated limitations and Transfer conditions.

## 3. Coding unit

The **publication** is the coding unit. Each work receives one row of codes. Every attribute summarizes all experiments that the publication reports, and where an attribute has an order the strongest value over the experiments is coded.

An **experiment** is a set of runs or evaluations of one system configuration family under one protocol whose results the paper reports together in a table, a figure or a numbered result paragraph.

Two attributes, `deg_task_class` and `deg_task_setting`, record a conjunction. They count only when a named degradation condition and a task outcome occur **in the same experiment**: the same trial set, results table or results figure. Their locator names that table, figure or trial set. A sensitivity analysis (`S-unit-any`, Section 18) relaxes this rule and lets the two parts come from different experiments.

## 4. Attribute summary

Kinds: **given** values are copied from the library index and never coded. **Derived** values are fixed mappings of card fields. **Coded** values are decided by reading. Form `set` lists zero or more ids joined with `|` in the canonical order of the value list, with `none` for the empty set. Form `one-or-two` holds one id or two distinct ids joined with `|`.

| Attribute | Kind | Form | Allowed values | Double-coded |
|---|---|---|---|---|
| `code` | given | one | library code of the work | no |
| `principal_section` | given | one | `IV`, `V`, `VI`, `VII`, `VIII`, `context` | no |
| `stage` | given | one | `baseline-2026-09-18`, `supplemental`, `expansion-2026-10-24`, `followup-2026-11-02`, `ieee-supplement-2026-11-03`, `survey-200plus-2026-11-03`, `ieee-refresh-2026-11-03`, `review-additions-2026-11-04` | no |
| `depth` | given | one | `full`, `light-legacy`, `light-targeted` | no |
| `functions` | coded | set | `LOC`, `PLN`, `SEM`, `MRC`, `REL`, `none` | yes |
| `src_addressed` | coded | set | `PER`, `SFA`, `TER`, `ACT`, `DYN`, `MAP`, `MOD`, `COM`, `RES`, `none` | yes |
| `response_family` | coded | one-or-two | `IV-A`, `IV-B`, `IV-C`, `IV-D`, `IV-E`, `IV-F`, `V-A`, `V-B`, `V-C`, `V-D`, `V-E`, `VI-A`, `VI-B`, `VI-C`, `VI-D`, `VII-A`, `VII-B`, `VII-C`, `VII-D`, `VIII-A`, `VIII-B`, `VIII-C`, `VIII-D`, `resource`, `context` | yes |
| `src_manipulated` | coded | set | `PER`, `SFA`, `TER`, `ACT`, `DYN`, `MAP`, `MOD`, `COM`, `RES`, `none` | yes |
| `src_selected` | coded | set | `PER`, `SFA`, `TER`, `ACT`, `DYN`, `MAP`, `MOD`, `COM`, `RES`, `none` | yes |
| `src_incidental` | coded | set | `PER`, `SFA`, `TER`, `ACT`, `DYN`, `MAP`, `MOD`, `COM`, `RES`, `none` | yes |
| `nominal_control` | coded | one | `yes`, `no`, `na` | yes |
| `single_level_injection` | coded | one | `yes`, `no` | yes |
| `task_setting` | coded | one | `none`, `simulation`, `physical`, `both` | yes |
| `deg_task_class` | coded | one | `none`, `D1`, `D2` | yes |
| `deg_task_setting` | coded | one | `none`, `simulation`, `physical` | yes |
| `level_strongest` | derived | one | `P`, `O`, `R`, `D`, `S`, `N`, `T`, `X` | no |
| `level_degradation` | coded | one | `P`, `O`, `R`, `D`, `S`, `N`, `T`, `X`, `none` | yes |
| `integrity` | derived | one | `yes`, `no` | no |
| `placement_reported` | derived | one | `yes`, `no` | no |
| `platform_group` | derived | one | `WHL`, `ROAD`, `GND`, `OTH` | no |
| `mixed_wheeled` | coded | one | `yes`, `no`, `na` | no |
| `drivetrain` | derived | one | `differential`, `skid-steer`, `ackermann`, `omnidirectional`, `unspecified`, `na` | no |
| `drivetrain_effect` | coded | one | `yes`, `no` | yes |
| `transfer_basis` | coded | one | `mechanism`, `counterexample`, `na` | no |
| `notes` | coded | text | short English text | no |

The given and derived attributes are filled from the library index for every row:

- `code`: the library code listed in `06-data/survey-inclusion.json`.
- `principal_section`: the card field `survey_module` mapped as in Section 5. The context review takes `context`.
- `stage`: the selection stage, the field `source_batch` of `06-data/paper-index.csv`.
- `depth`: `full` when `verification_level` is full. `light-legacy` when the card is light and its stage is `baseline-2026-09-18`, `supplemental` or `expansion-2026-10-24`, whose cards convert legacy extractions. `light-targeted` for every other light card.
- `level_strongest`: the card field `evidence_type` mapped as in Section 12.
- `integrity`: `yes` when the card field `evaluation_all` contains `integrity-reliability`.
- `placement_reported`: `yes` when the card field `compute_location` is neither `not-reported` nor `not-applicable`.
- `platform_group` and `drivetrain`: the card field `platform_class` mapped as in Section 13.

A coder who finds a derived value contradicted by the paper keeps the derived value and describes the discrepancy in `notes`. Card corrections follow the library's own correction process.

The survey names the selection stages as follows. The publisher of each work, used for the venue mix per stage, follows its DOI prefix, or the official URL host for works without a DOI (`publisher_prefixes` and `publisher_hosts` in the JSON file).

| Stage | Label in the survey |
|---|---|
| `baseline-2026-09-18` | Initial sample |
| `supplemental` | Complementary publications |
| `expansion-2026-10-24` | Thematic sample |
| `followup-2026-11-02` | Integration questions |
| `ieee-supplement-2026-11-03` | Targeted IEEE coverage |
| `survey-200plus-2026-11-03` | Further targeted coverage |
| `ieee-refresh-2026-11-03` | Recent IEEE coverage |
| `review-additions-2026-11-04` | Coverage additions |

## 5. Functions and the principal section

The five functions follow the five method sections of the survey.

| Id | Section | Card `survey_module` | Scope |
|---|---|---|---|
| `LOC` | IV | `localization-mapping` | State estimation, odometry, SLAM, relocalization, map building and map maintenance, and datasets for these tasks |
| `PLN` | V | `traversability-planning-control` | Traversability assessment, exploration planning, global and local motion planning, tracking control, learned local motion and crowd navigation |
| `SEM` | VI | `semantic-language-navigation` | Semantic maps and memory, open-vocabulary and language-conditioned navigation, vision-language models in the motion loop, and semantically driven social navigation |
| `MRC` | VII | `multi-robot` | Two or more robots that exchange information or coordinate: exploration, collaborative SLAM, map merging, cooperative localization, task allocation and formation control |
| `REL` | VIII | `fault-recovery-deployment` | Localization integrity, fault detection and isolation, fault-tolerant control, recovery behaviors, runtime monitoring, energy and long-term deployment |

**Principal section.** The principal section is the card field `survey_module` mapped through this table. A work keeps exactly one principal section. It decides where the survey discusses the work and which column of the source-by-function matrix the work occupies.

**`functions`.** The list always contains the principal function. Another function is added when at least one of these holds:

1. The work contributes or modifies a component that performs the function.
2. The mechanism takes the output quality, uncertainty or failure state of the function as an explicit input and changes its behavior accordingly. A planner that widens its margins with the pose covariance codes `LOC`.
3. The evaluation reports a measure of the function as an outcome of the mechanism. A recovery method judged by relocalization success codes `LOC`.

An unmodified off-the-shelf module that the experiment needs only to run does not count. Neither does a function named only as motivation or future work. `MRC` requires two or more robots that exchange information or coordinate inside the mechanism. A single robot among people is not multi-robot coordination. The context review codes `none`.

**One paper in several cells.** A work occupies one matrix cell for every source in `src_addressed`, all of them in the column of its principal section. In the function-pair co-occurrence matrix it counts once in every unordered pair of distinct functions of its `functions` list. Cell totals therefore exceed the number of works, and each work still has one principal section.

## 6. Degradation sources

Nine sources cover the conditions that the survey treats as degradation. Each source belongs to one of five source groups and violates one navigation assumption (Section 7). The vocabulary column maps the card field values of `degradation` and `degradation_observed` onto the sources.

| Id | Source | Group | Assumption | Card vocabulary values |
|---|---|---|---|---|
| `PER` | Perceptual degradation | `G1` Sensing and estimation | `A1` | `visual-degradation`, `lidar-degeneracy`, `gnss-denial` |
| `SFA` | Sensor fault and false association | `G1` Sensing and estimation | `A1` | `sensor-fault`, `data-association-fault` |
| `TER` | Terrain and wheel-ground contact | `G2` Terrain and mobility | `A2` | `terrain`, `wheel-slip` |
| `ACT` | Actuator fault and saturation | `G2` Terrain and mobility | `A6` | `actuator-fault` |
| `DYN` | Moving agents | `G3` Environment and map change | `A3` | `dynamic-objects` |
| `MAP` | Map and scene change | `G3` Environment and map change | `A3` | `scene-change` |
| `MOD` | Learned and semantic inference error | `G4` Learned and semantic inference | `A4` | `model-error` |
| `COM` | Communication loss, delay and bandwidth | `G5` Communication and computation | `A5` | `communication-delay-loss`, `communication-partition`, `bandwidth-limit` |
| `RES` | Computation and energy limits | `G5` Communication and computation | `A6` | `compute-limit`, `energy-limit` |

Decision rules per source:

- **`PER`**: the environment makes measurements uninformative. Examples are illumination change, darkness, low texture, motion blur, glare, smoke, dust, fog, rain or snow that degrade sensing, geometric degeneracy, sparse or missing returns, GNSS outage or multipath, and a sensor dropout whose cause the paper does not state.
- **`SFA`**: a sensor or an association step produces wrong data. Examples are sensor failure, bias, drift beyond specification, frozen or corrupted output, spoofing or another attack, and wrong or missing feature, landmark or place association. A dropout that the paper attributes to a failed sensor is `SFA`. A dropout caused by the scene, or of unstated cause, is `PER`. GNSS outage and multipath are `PER`, and GNSS spoofing is `SFA`.
- **`TER`**: the ground departs from flat, rigid support with known contact. Examples are uneven, rough, sloped, vegetated or deformable ground, negative obstacles, wheel slip, skidding and wheel-ground model mismatch.
- **`ACT`**: commanded motion is not delivered. Examples are loss of actuator effectiveness, actuator bias, saturation, and a stuck or failed wheel, motor or steering unit.
- **`DYN`**: pedestrians, vehicles, animals or uncoordinated robots move in the scene, and the study treats them as a disturbance, predicts or avoids them, or varies them. Robots that the evaluated method itself coordinates are not moving agents of this source. Static obstacles are part of the nominal scene.
- **`MAP`**: a map or prior no longer matches the scene. Examples are map aging, layout change, relocated semi-static objects, seasonal or long-term change and a deliberately altered prior map. Exploring an unknown but static scene is not map change. A moving person is `DYN`, while a parked object that has moved between sessions is `MAP`.
- **`MOD`**: a learned or foundation model gives wrong output. Examples are misclassification, misgrounding, a wrong or invented language-model response, unreliable learned predictions and out-of-distribution inputs. Using a learned model does not by itself code this source. It is addressed when the mechanism estimates, detects, bounds or recovers from such errors (uncertainty of learned predictions, response validation, fallback, novelty or out-of-distribution detection, grounding checks). It is a named condition only when the evaluation constructs, injects or separately reports inputs that produce such errors.
- **`COM`**: information between robots, or between a robot and a server or cloud service, arrives late, out of order, incompletely or not at all. Examples are delay, jitter, packet loss, partition or disconnection and limited data rate.
- **`RES`**: limited onboard processing, memory or inference time, and battery or charging constraints. The time that a remote model needs to answer once a request has arrived is `RES`. Network transfer time is `COM`. Reporting a runtime is not a named condition. `RES` is named when the compute or energy budget is varied, or deliberately restricted and reported as such.

A source that appears only as motivation, related work or future work is not coded in any source attribute.

**`src_addressed`.** This attribute lists every source whose degradation the mechanism, or the resource, is designed to tolerate, detect, bound or recover from, as the problem statement, the mechanism or the contribution list states. It also contains every source of `src_manipulated` and `src_selected`, since a named condition is addressed by definition. It is the degradation source coded for every work. `none` is expected only for the context review and for a dataset or benchmark resource that targets no source. Any other `none` needs a note that names the stated problem and why no source applies.

## 7. Navigation assumptions

The survey lists six navigation assumptions once. Each source violates exactly one of them. The response families named here are the links stated before coding. The links drawn in the survey figure are recounted from coded works as pairs of an addressed source and the work's primary response family, and a link appears only when at least one coded work supports it.

| Id | Assumption | Sources | Response families linked before coding |
|---|---|---|---|
| `A1` | Measurements are informative and correctly associated | `PER`, `SFA` | `IV-A`, `IV-B`, `IV-E`, `VIII-B` |
| `A2` | Wheels roll on supporting ground with known contact | `TER` | `IV-C`, `V-A`, `V-E` |
| `A3` | The mapped scene is static or persistent | `DYN`, `MAP` | `IV-D`, `V-C`, `V-D`, `VI-A` |
| `A4` | Learned and semantic inference is valid | `MOD` | `VI-B`, `VI-C`, `VI-D`, `VIII-B` |
| `A5` | Shared information is timely and consistent | `COM` | `V-E`, `VII-B`, `VII-C` |
| `A6` | Actuation, computation and energy remain available | `ACT`, `RES` | `VIII-A`, `VIII-C`, `VIII-D` |

## 8. Response families

A response family groups works by the response they contribute. The families follow the subsections of the survey's method sections.

| Id | Family | Scope |
|---|---|---|
| `IV-A` | Localizability and selective measurement updates | Detect uninformative or degenerate measurements and condition, weight, select or skip the update |
| `IV-B` | Complementary sensing | Add, switch or reweight sensing modalities so that another modality covers a degraded one |
| `IV-C` | Motion priors, contact and adaptation | Kinematic, contact or slip models and their online adaptation inside estimation |
| `IV-D` | Dynamic geometry and persistent maps | Remove or track moving geometry, estimate persistence and maintain maps over time |
| `IV-E` | Prior-map and cross-modal localization | Localize or relocalize against a prior, cross-modal or global map |
| `IV-F` | Cooperative estimates and uncertain maps | Estimation that uses other agents' estimates, external infrastructure or map priors with explicit uncertainty |
| `V-A` | Terrain support and traversability costs | Estimate support, traversability, terrain cost or terrain risk for planning |
| `V-B` | Exploration with information and geometry | Exploration planners driven by information gain, frontier structure or geometry |
| `V-C` | Learning, prediction and interaction | Learned planners or policies, prediction of other agents and interaction-aware planning |
| `V-D` | Safety filters and explicit risk conditions | Barrier functions, chance or risk constraints and other explicit safety conditions on motion |
| `V-E` | Tracking, mission costs and network support | Tracking control with learned or adapted dynamics, delay-aware or networked control and mission-level costs |
| `VI-A` | Semantic memory and scene structure | Build, update and query semantic maps, scene graphs or object memory |
| `VI-B` | Geographic grounding, priors and learned actions | Ground instructions in maps or geography, use semantic priors, or let a learned model output actions |
| `VI-C` | Candidate selection and behavioral constraints | A model selects among candidates that geometric modules generate or check, or social and behavioral constraints shape motion |
| `VI-D` | Memory, timing and embodied execution | Query timing, latency handling, memory horizons and execution of model decisions on a robot |
| `VII-A` | Task allocation and spatial responsibility | Assign tasks, regions or goals among robots |
| `VII-B` | Compact sharing and distributed estimation | Select, compress or schedule shared data and estimate jointly with distributed inference |
| `VII-C` | Rendezvous, disconnection and conditional repair | Plan reconnection, operate through partitions and repair shared estimates after faults or reconnection |
| `VII-D` | Motion interaction and persistent service | Formation, inter-robot motion coordination and persistent multi-robot service |
| `VIII-A` | Fault estimation and tolerant control | Estimate faults and keep control performance under them |
| `VIII-B` | Integrity and failure monitoring | Bound hazardous error, predict or detect failure and monitor runtime validity |
| `VIII-C` | From diagnosis to an executed response | Select and execute a recovery or fallback action after a detected failure |
| `VIII-D` | Resources and sustained operation | Energy, charging, service scheduling and long-duration deployment |
| `resource` | Dataset or benchmark resource | The main contribution is a dataset or benchmark (card `evidence_type` is `dataset-resource`) |
| `context` | Context review | The single literature review kept for context |

**`response_family`.** The primary family comes from the principal section and matches the response the work contributes. When two families of that section fit, the main claim of the abstract or the contribution list decides, and the other family may follow as the secondary value. An optional secondary family may come from any section and differs from the primary. A dataset or benchmark resource takes `resource` as its primary family, and the context review takes `context`.

## 9. Degradation-evidence classes

Each source that an evaluation contains is assigned one of three classes.

- **D1, injected or varied degradation with a comparator.** The authors inject, impose, remove or vary the condition while the task setup stays otherwise the same (same course, scene, sequence or simulated world). They report the same system at a second level of the condition, either nominal or another severity. A with-and-without comparison also qualifies: the same system with and without the evaluated response under the same injected condition.
- **D2, deliberately selected difficult condition without manipulation.** The authors include the condition on purpose for its difficulty without controlling its level. Examples are chosen sequences, sites, routes or crowds and a dataset built to contain the condition. An injected or imposed condition that is reported for the same system at one level only, with no with-and-without comparison, is also D2 and sets `single_level_injection` to `yes`.
- **D3, incidental degradation.** The condition occurred during an experiment and the paper reports it, for example in a failure analysis, field notes or a limitation that refers to observed runs. The evaluation did not include it on purpose.

Decision rules:

1. **One class per source.** Each source enters at most one of `src_manipulated` (D1), `src_selected` (D2) and `src_incidental` (D3), namely the strongest class it reaches in any experiment (D1 > D2 > D3).
2. **Publication class.** The class of the publication is the strongest class over its sources (D1 > D2 > D3 > none). It is derived and never coded separately.
3. **Named condition.** A source coded D1 or D2 is a named degradation condition.
4. **Comparator.** A comparison against other methods at one level of an injected condition is not a comparator. A baseline counts as the same system without the response when the paper states that the proposed system is that baseline plus the response, as in an ablation or when the method extends a named base pipeline.
5. **Simulation.** Injection or variation in simulation or in a numerical model is D1 when the comparator rule holds. The setting is recorded in `level_degradation` and `deg_task_setting`, never in the class.
6. **Different sites or sequences.** Results on different sites, routes or sequences chosen for different conditions are D2, also when a nominal sequence is reported beside them, since other factors change with the condition. A recording counts as controlled only when the authors, or the documented design of the dataset, changed the condition alone between the compared recordings (same route, rig and scene).
7. **Domain shift of learned models.** A sim-to-real or cross-domain test of a learned model is D2 for `MOD` when its results are reported separately. A standard held-out test split is not a named condition.
8. **Resources.** A dataset or benchmark built to contain a condition codes that condition D2, also without an evaluated method.
9. **Moving agents.** Moving agents are D1 when their number, density, speed or behavior is varied with a comparator, D2 when a crowded site or scripted crossing is chosen without a comparator, and D3 when passers-by occur in a run and the paper reports their effect.
10. **Not coded.** A condition that appears only as motivation, related work, future work or a hypothetical limitation is not coded.

**`nominal_control`.** `yes` when at least one D1 comparison includes a level at which the condition is absent. `no` when every D1 comparison is between non-nominal levels or is a with-and-without-response comparison under the injected condition. `na` when `src_manipulated` is `none`.

**`single_level_injection`.** `yes` when the authors inject or impose a condition but report the same system at that one level only, with no with-and-without-response comparison, so that the source is coded D2. Otherwise `no`.

## 10. Task outcomes and the same-experiment rule

A **task outcome** is a mission-level result of closed-loop execution: success or failure, goal arrival, collisions or safety-constraint violations, coverage or explored area, completion or traversal time, distance travelled, interventions or service availability. Estimation, tracking and prediction errors are component measures, also when they are measured in closed loop.

**`task_setting`.** The settings in which the work reports a task outcome: `none`, `simulation`, `physical` or `both`. `physical` needs a numeric outcome from physical runs in the text or a table, such as a success count or rate, collisions, interventions, completion time, distance or coverage. A video, or a plot without stated numbers, does not establish a physical task outcome, and the coder notes it. Physics simulation and closed-loop numerical models count as `simulation`.

**`deg_task_class`.** The strongest class of a named condition that occurs in the same experiment as a task outcome. `D1` when the task outcome itself is reported for the same system at two levels of a manipulated condition, or with and without the response under it. `D2` when the task outcome is reported under a selected condition, or under a manipulated condition without a task-level comparator. `none` when no experiment contains both parts.

**`deg_task_setting`.** `physical` when at least one same-experiment conjunction counted in `deg_task_class` ran on a physical robot, otherwise `simulation`. It is `none` exactly when `deg_task_class` is `none`. The two attributes may rest on different experiments of the same work, for example a D1 conjunction in simulation and a D2 conjunction on hardware give `D1` and `physical`. Each has its own locator.

## 11. Integrity and placement

`integrity` and `placement_reported` are derived from the card (attribute summary). `integrity` marks a probability or detector output about hazardous error, failure or anomaly that is distinct from a covariance envelope or tracking error. `placement_reported` marks a work that states where its evaluated computation ran.

## 12. Evidence levels

| Id | Card `evidence_type` | Rank | Shade step | Level |
|---|---|---|---|---|
| `P` | `closed-loop-hardware` | 7 | 3 | Physical closed loop: the method runs online on a physical robot and its output drives the robot |
| `O` | `online-hardware` | 6 | 2 | Online estimate on hardware without closing the loop |
| `R` | `recorded-robot-data` | 5 | 2 | Data that the authors recorded on their own robot or vehicle |
| `D` | `dataset-playback` | 4 | 1 | Public datasets recorded by others |
| `S` | `simulation` | 3 | 1 | Physics or sensor simulation |
| `N` | `numerical` | 2 | 1 | Numerical integration of an abstract model |
| `T` | `theory-only` | 1 | 0 | Analysis or proof without an experiment |
| `X` | `dataset-resource`, `survey` | 0 | 1 | Resource or review without a ranked setting |

The shade steps of the source-by-function matrix are 0 (no named condition), 1 (replay, simulation, numerical model or resource), 2 (recorded data or online hardware) and 3 (physical closed loop).

**`level_strongest`** is derived from the card. **`level_degradation`** is the level of the strongest experiment that reports a result under a named condition (D1 or D2). It takes `X` for a resource that contains the condition without an evaluated method, and `none` when no source is coded D1 or D2. A resource that evaluates baseline methods on its own recordings takes `R`. A physical run without a stated result (video only) does not raise `level_degradation`.

## 13. Platform, drivetrain and transfer

**`platform_group`** maps the card field `platform_class` onto four groups. The mark is the symbol the survey's matrix and module tables use for the group.

| Id | Group | Mark | Card `platform_class` values |
|---|---|---|---|
| `WHL` | Target wheeled robot | none | `differential-drive`, `skid-steer`, `ackermann`, `omnidirectional`, `wheeled-unspecified` |
| `ROAD` | Road vehicle | R | `road-vehicle` |
| `GND` | Other ground robot | G | `legged`, `tracked` |
| `OTH` | Non-ground, handheld, mixed-carrier or no platform | N | `aerial`, `aquatic`, `handheld`, `mixed`, `none` |

**`mixed_wheeled`** (single-coded). `yes` when a work whose `platform_class` is `mixed` includes a wheeled ground robot among its carriers. `no` when it does not, or when the carriers are unidentified. `na` for every other platform class. It is used only in a sensitivity row.

**`drivetrain`** (derived). `differential`, `skid-steer`, `ackermann`, `omnidirectional` or `unspecified` for the target wheeled group, following `platform_class`. `na` outside that group.

**`drivetrain_effect`.** `yes` when the paper states or shows that a degradation effect, or the feasibility of a response, depends on the wheel arrangement or steering geometry of a wheeled platform. Examples are skid-steer slip in turns, the minimum turning radius or non-holonomic limits of car-like steering, lateral motion of omnidirectional bases, reversing limits, rotation in place and footprint. The statement may appear in the design rationale, the results or the limitations. Naming the drivetrain, or using a generic kinematic model without a reported effect, is `no`. The attribute is coded for every work, including works outside the target wheeled group that report such an effect for a wheeled carrier.

**`transfer_basis`** (single-coded). For works outside the target wheeled group, three transfer criteria are checked:

1. The inputs of the mechanism exist on a wheeled ground robot.
2. The assumptions of the mechanism do not rest on the other embodiment (legs, flight, water, a handheld carrier or road-vehicle infrastructure).
3. The evaluation isolates the mechanism from the platform-specific parts of the system.

`mechanism` when all three hold. `counterexample` when the work shows where a wheeled transfer would break, with a note that names the failed criterion. `na` for target wheeled works and the context review.

## 14. Notes

`notes` holds short English text without quotations of publisher text. It records uncertainty, discrepancies with derived values and the reason for an unusual `none`. The tag `human-assistance` marks a work whose response or evaluation relies on human intervention, takeover or remote supervision. The interface ranking counts this tag (Section 17).

## 15. Locators

Every coded value that asserts presence needs a locator row with the fields `code`, `attribute`, `value`, `source`, `locator` and `note`. A locator is required for:

- every function in `functions` other than the principal one,
- every source in `src_addressed`, `src_manipulated`, `src_selected` and `src_incidental`,
- every family in `response_family`,
- `nominal_control` = `yes`, `single_level_injection` = `yes`, `drivetrain_effect` = `yes` and `mixed_wheeled` = `yes`,
- any value other than `none` of `task_setting`, `deg_task_class`, `deg_task_setting` and `level_degradation`,
- any value other than `na` of `transfer_basis`.

For a multi-valued attribute the row names one id. For a single-valued attribute it names the coded value.

Allowed `source` values are `card`, `transcription`, `pdf` and `source-reading`. The independent coder uses `card`, `transcription` and `pdf`. Locator formats:

- `pdf`: `PDF p. N`, the physical page of the PDF file counted from 1, optionally followed by a table, figure or section label, as in `PDF p. 7, Table II`.
- `card`: `card: <block name>`, optionally with the page that the card cites, as in `card: Baselines and controls, p. 6`.
- `transcription`: `transcription: <section heading, table or figure label>`.
- `source-reading`: `source-reading: <page scope or excerpt label of the batch reading record>`.

For a light card, a card locator suffices only when the cited card passage names a page. A light-legacy card always needs a `pdf` or `transcription` locator for each value. Locators and notes paraphrase and never copy publisher text.

## 16. Consistency rules

| Id | Rule |
|---|---|
| `CR01` | `functions` contains the principal function. It is `none` only for the context review. |
| `CR02` | `src_addressed` contains every source of `src_manipulated` and `src_selected`. |
| `CR03` | `src_manipulated`, `src_selected` and `src_incidental` share no source. |
| `CR04` | `nominal_control` is `na` exactly when `src_manipulated` is `none`. |
| `CR05` | `single_level_injection` = `yes` requires a source in `src_selected`. |
| `CR06` | `deg_task_class` = `D1` requires a source in `src_manipulated`. `D2` requires a source in `src_manipulated` or `src_selected`. |
| `CR07` | `deg_task_setting` is `none` exactly when `deg_task_class` is `none`. |
| `CR08` | `deg_task_setting` = `physical` requires `task_setting` `physical` or `both`. `simulation` requires `task_setting` `simulation` or `both`. |
| `CR09` | `level_degradation` is `none` exactly when `src_manipulated` and `src_selected` are both `none`. |
| `CR10` | `deg_task_setting` = `physical` requires `level_degradation` = `P`. |
| `CR11` | `level_degradation` does not outrank `level_strongest` unless `level_strongest` is `X`. |
| `CR12` | The primary response family belongs to the principal section, or is `resource` for a resource or `context` for the context review. A secondary family differs from the primary. |
| `CR13` | `src_addressed` = `none` for a technical work that is not a resource needs a note. |
| `CR14` | `mixed_wheeled` is `na` exactly when the card `platform_class` is not `mixed`. |
| `CR15` | `transfer_basis` is `na` exactly when `platform_group` is `WHL` or the work is the context review. |
| `CR16` | Given and derived attributes equal their derivation. |
| `CR17` | Every value that Section 15 lists has a locator row. For a light-legacy work at least one of them has source `pdf` or `transcription`. |
| `CR18` | Multi-valued fields list each id once, in canonical order. |
| `CR19` | The context review codes `none` or `na` in every coded attribute except `response_family` = `context` and `drivetrain_effect` = `no`. |

## 17. Derived measures, matrices and the interface ranking

These definitions are fixed before coding.

**Derived measures.**

- Named sources: the union of `src_manipulated` and `src_selected`.
- Publication class: D1 when `src_manipulated` is not `none`, else D2 when `src_selected` is not `none`, else D3 when `src_incidental` is not `none`, else none.
- Task outcome: `task_setting` is not `none`.
- **Headline measure**: `deg_task_class` is `D1` or `D2`, meaning that a named degradation condition and a task outcome occur in the same experiment.
- Direct joint wheeled evidence: `deg_task_class` is `D1` or `D2`, `deg_task_setting` is `physical` and `platform_group` is `WHL`.
- Shares are reported per principal section (function) over the technical works of that section, and pooled over all technical works. Every share is a statistic of the purposively selected sample.

**Source-by-function matrix.** Rows are the nine sources grouped by assumption `A1`-`A6`. Columns are the principal sections IV-VIII. A cell reports a = works of the column with the source in `src_addressed`, n = works with the source among the named sources, m = works with the source in `src_manipulated`, k = target wheeled works among the a works, and the counts of the a works in `ROAD`, `GND` and `OTH` under their marks. The shade of a cell is the shade step of the strongest `level_degradation` among its n works. Occupancy follows the rule of Section 5.

**Function-pair co-occurrence matrix.** For every unordered pair {a, b} of distinct functions:

- works: works whose `functions` contain both a and b,
- joint_named_same: of these, works with `deg_task_class` `D1` or `D2`,
- joint_manipulated_same: of these, works with `deg_task_class` `D1`,
- joint_physical_named: of these, works with `deg_task_class` `D1` or `D2` and `deg_task_setting` `physical`,
- direct_wheeled_joint: of these, joint_physical_named works in `WHL`,
- wheeled_works: works of the pair in `WHL`,
- strongest_level: the strongest `level_degradation` among the works of the pair.

**Interface ranking.** A candidate is an unordered pair of distinct functions {f, g} with one coupling source s. Its identifier is `<f>-<g>:<s>`, with f before g in the order LOC, PLN, SEM, MRC, REL. Its works W are the works whose `functions` contain f and g and whose `src_addressed` or `src_incidental` contains s. A candidate is eligible when W holds at least 3 works. Metrics:

- n: the number of works in W,
- j: works of W with direct joint wheeled evidence,
- w: works of W in `WHL`,
- safety relevance: `PLN` or `REL` is one of f and g,
- gap = n - j, and gap share = 1 - j/n.

Candidates are sorted by gap (descending), then safety relevance (relevant first), then w (descending), then identifier (ascending). The survey's four interfaces own these admissible cells, and an interface's rank is the best rank among its eligible cells:

| Interface | Pairs | Coupling sources |
|---|---|---|
| 1. Localization-triggered navigation recovery | {LOC, REL} | `PER`, `SFA` |
| 2. Resource-constrained semantic reasoning and fallback | {PLN, SEM}, {SEM, REL} | `MOD`, `RES` |
| 3. Pose uncertainty in wheeled terrain decisions | {LOC, PLN} | `TER`, `PER` |
| 4. Disconnection, reconnection and corrupted shared information | {LOC, MRC} | `COM` |

Alternatives named before coding are ranked and reported in the same way: map change forcing plan re-validation ({LOC, PLN} with `MAP`), perception latency affecting control ({PLN, REL} with `RES`) and energy or computation limits on planning ({PLN, REL} with `RES`). Human assistance falls outside the function-pair scheme and is reported as the number of works whose notes carry the tag `human-assistance`.

Two sensitivity rankings follow the same rules. The first drops the works of the integration-questions stage (`followup-2026-11-02`), which was acquired for the four interfaces. The second sorts by gap share instead of gap.

Every candidate that ranks above the lowest-ranked developed interface is listed with a reason for not developing it. If the four interfaces are not the four highest-ranked candidates, the survey says so and keeps them as an agenda proposed by this survey.

## 18. Sensitivity analyses and robustness findings

Each row reports the numerator, the denominator, the pooled share and the share per function (LOC, PLN, SEM, MRC, REL). Definition and coding-unit rows use all technical works. Subset rows apply the headline measure to a subset.

| Id | Kind | Definition or subset |
|---|---|---|
| `S-def-headline` | definition | `deg_task_class` `D1` or `D2` |
| `S-def-D1` | definition | `deg_task_class` `D1` |
| `S-def-D1-nominal` | definition | `deg_task_class` `D1` and `nominal_control` `yes` (publication-level control, whose nominal level may belong to another experiment) |
| `S-def-physical` | definition | `deg_task_class` `D1` or `D2` and `deg_task_setting` `physical` |
| `S-def-with-incidental` | definition | headline, or `src_incidental` not `none` in a work that reports a task outcome |
| `S-unit-any` | coding unit | named sources not `none` and `task_setting` not `none`, without the same-experiment rule |
| `S-card-round3` | definition | card coding of the previous revision: `evaluation_all` contains both `designed-degradation` and `closed-loop-task` |
| `S-depth-full` | depth | `depth` = `full` |
| `S-depth-light-legacy` | depth | `depth` = `light-legacy` |
| `S-depth-light-targeted` | depth | `depth` = `light-targeted` |
| `S-depth-no-legacy` | depth | `depth` `full` or `light-targeted` |
| `S-stage-out-<stage>` | leave one stage out | all technical works except one stage, one row per stage |
| `S-year-<band>` | year | publication year in 2021-2023, 2024, 2025 or 2026, one row per band |
| `S-quota` | stage group | quota stages `expansion-2026-10-24` and `ieee-refresh-2026-11-03`, whose selection fixed an equal number of works per theme |
| `S-non-quota` | stage group | all other stages |
| `S-quota-theme-<T>` | theme | quota stages and one theme folder T1-T6, one row per theme |
| `S-no-ieee-only` | stage group | without the IEEE-only stages `ieee-supplement-2026-11-03` and `ieee-refresh-2026-11-03` |
| `S-no-coverage` | stage group | without the coverage-additions stage `review-additions-2026-11-04` |
| `S-platform-WHL` | platform | `platform_group` = `WHL` |
| `S-platform-WHL-mixed` | platform | `platform_group` = `WHL`, or `mixed_wheeled` = `yes` |
| `S-platform-non-WHL` | platform | `platform_group` `ROAD`, `GND` or `OTH` |

Robustness findings, stated before coding:

| Id | Finding | Test |
|---|---|---|
| `RF1` | LOC has the lowest headline share among the five functions | share(LOC) <= share(f) for every other function f, ties reported |
| `RF2` | REL has the highest headline share among the five functions | share(REL) >= share(f) for every other function f, ties reported |
| `RF3` | Task outcomes appear in at least 90% of PLN works and of SEM works | task-outcome share >= 0.90 in PLN and in SEM |
| `RF4` | Task outcomes appear in at most 5% of LOC works | task-outcome share <= 0.05 in LOC |

A robustness row states for each subset and definition whether each finding holds. A finding is reported as n/a in a subset where a function it compares has fewer than 3 works. Definition rows change only `RF1` and `RF2`.

## 19. Double coding and agreement

A second, independent coder codes a stratified random sample of 40 technical works. The second coder is a language-model session on a different model from the primary coder, with no access to the primary codes. It codes the attributes marked **double-coded** in the attribute summary and writes notes.

The given and derived attributes are not double-coded, since they copy or map card fields that both coders read and their agreement would be trivial. `mixed_wheeled` and `transfer_basis` are single-coded descriptors of the platform.

Agreement units:

- `functions`: Cohen's kappa per function over the sampled works whose principal function differs from it, and exact-set agreement over all sampled works,
- `src_addressed`: kappa per source flag and exact-set agreement,
- `response_family`: kappa of the primary family,
- named sources (D1 or D2): kappa per source flag and exact-set agreement,
- `src_manipulated`: pooled kappa over the nine source flags of every sampled work, and exact-set agreement,
- publication class (D1, D2, D3, none): kappa,
- `nominal_control`, `single_level_injection`, `task_setting`, `deg_task_class`, `deg_task_setting`, `level_degradation` and `drivetrain_effect`: kappa each.

`src_selected` and `src_incidental` enter the agreement through the named-source flags and the publication class.

Kappa is unweighted Cohen's kappa, (po - pe) / (1 - pe), where po is the observed and pe the chance agreement. It is undefined when pe = 1, which happens when both coders use one category. The report then gives n/a together with percent agreement and the prevalence of each value. Percent agreement is the share of units on which both coders give the same value.

Both coders are language-model sessions that read the same review cards, and these cards were themselves prepared with language-model tools. The statistic therefore measures agreement in applying this codebook to shared evidence. It is not human inter-rater reliability.

The primary codes are frozen with a SHA-256 record before agreement is computed. Every disagreement is resolved by re-reading the source at both coders' locators and is logged with the resolved value, the resolution (`primary-kept`, `second-adopted` or `both-revised`), a short reason and the deciding locator. A rule that causes disagreement in three or more sampled works is clarified in a new codebook version, and the pattern is rechecked across all works with every change logged. Corrections after the freeze go through the adjudication log only.

## 20. Sampling

- Population: the technical works of the selection. The context review is excluded.
- Strata: principal section (IV-VIII) by assessment depth (full, light-legacy, light-targeted), with selection stage as a coverage constraint.
- Size: 40 works, 8 per principal section.
- Allocation within a section: min(2, full works of the section) full works. The remaining seats are split between light-legacy and light-targeted by the largest-remainder method over their counts in the section. A tie in remainders goes to light-legacy, and no stratum receives more seats than it has works.
- Seed: 20261105.
- Draw: attempt k = 0, 1, 2, ... uses one generator `random.Random(20261105 + k)` of Python. The generator serves the strata in section order and, within a section, in depth order. Each stratum is drawn with `random.Random.sample` over its codes sorted in ascending order.
- Stage coverage: every selection stage with at least 4 technical works must appear at least once. An attempt that misses one is rejected, and k increases by 1.
- Implementation: `05-survey/manuscript/scripts/coding.py`, function `draw_sample`.
- Record: the attempt index k, every rejected attempt with its missing stages, the allocation, and per work its stratum and draw order are published after the independent coding is complete. The sample list is not part of this codebook.

## 21. Instructions for the independent coder

**Inputs.** The independent coder receives this codebook (`codebook.md`) and a list of works (`sample.json`) in one folder. Each entry of the list gives the library code, the citation key, bibliographic metadata and the paths of the work's review card, transcription and PDF.

**Independence.**

- Code each listed work from this codebook and that work's review card, transcription and PDF only. The repository tool `python -m tools.locate CODE --find "phrase"`, `--page N` or `--render N`, run from the repository root, may be used to search or render the listed work's own PDF and transcription. The page images that `--render` writes to the tool's own scratch folder are not coding output.
- Do not open other files. In particular, do not open other files of `06-data/evidence-coding/`, anything under `05-survey/manuscript/` (sections, generated data, survey sources and PDFs), the review cards of works that are not listed, any sampling record, any local review report, any other coder's output or version-control history.
- Do not edit any repository file. Write only `codes.json` and `notes.md` in the folder that holds the received codebook.
- Do not quote publisher text in codes, locators or notes.

**Procedure.**

1. Compute the SHA-256 of the received `codebook.md` and record it.
2. For each listed work, read its card, then check the deciding passages in the transcription or the PDF. The principal section follows from the card field `survey_module` (Section 5).
3. Code every double-coded attribute, using only allowed values. Join multi-valued fields with `|` in the canonical order of the value list, and write `none` for an empty set.
4. Add a locator row for every value that Section 15 lists. Record the physical PDF page for every value that the card does not locate on a page. For a light-legacy card, give a `pdf` or `transcription` locator for every value.
5. When the sources do not settle a value, apply the decision rules to the available evidence and record the uncertainty in `notes`. Code every listed work.

**Output schema of `codes.json`.** One `works` entry per listed work, in the order of the list, with exactly the fields of the example. One `locators` entry per value that needs a locator. Z98 and Z99 are fictional codes and describe no corpus work. Z98 is a dust-tolerant LiDAR-inertial odometry method on a skid-steer robot that feeds its own local planner, driven on one course with no dust, light dust and dense dust, with trajectory error and course completion reported per level. Z99 is a LiDAR odometry method evaluated only on public tunnel and corridor sequences chosen for their degeneracy, against other methods, with trajectory error as its only measure.

```json
{
  "schema_version": 1,
  "codebook_sha256": "<SHA-256 of codebook.md as received>",
  "coder": "second",
  "works": [
    {"code": "Z98", "functions": "LOC|PLN", "src_addressed": "PER", "response_family": "IV-A", "src_manipulated": "PER", "src_selected": "none", "src_incidental": "none",
     "nominal_control": "yes", "single_level_injection": "no", "task_setting": "physical", "deg_task_class": "D1",
     "deg_task_setting": "physical", "level_degradation": "P", "drivetrain_effect": "no", "notes": ""},
    {"code": "Z99", "functions": "LOC", "src_addressed": "PER", "response_family": "IV-A", "src_manipulated": "none", "src_selected": "PER", "src_incidental": "none",
     "nominal_control": "na", "single_level_injection": "no", "task_setting": "none", "deg_task_class": "none",
     "deg_task_setting": "none", "level_degradation": "D", "drivetrain_effect": "no", "notes": ""}
  ],
  "locators": [
    {"code": "Z98", "attribute": "functions", "value": "PLN", "source": "pdf", "locator": "PDF p. 4, Sec. III-C", "note": "planner consumes the odometry health flag"},
    {"code": "Z98", "attribute": "src_addressed", "value": "PER", "source": "card", "locator": "card: Problem, p. 1", "note": ""},
    {"code": "Z98", "attribute": "response_family", "value": "IV-A", "source": "pdf", "locator": "PDF p. 3, Sec. III-B", "note": ""},
    {"code": "Z98", "attribute": "src_manipulated", "value": "PER", "source": "pdf", "locator": "PDF p. 6, Table III", "note": "three dust densities on one course"},
    {"code": "Z98", "attribute": "nominal_control", "value": "yes", "source": "pdf", "locator": "PDF p. 6, Table III", "note": "no-dust runs"},
    {"code": "Z98", "attribute": "task_setting", "value": "physical", "source": "pdf", "locator": "PDF p. 6, Table III", "note": ""},
    {"code": "Z98", "attribute": "deg_task_class", "value": "D1", "source": "pdf", "locator": "PDF p. 6, Table III", "note": "completion per dust level"},
    {"code": "Z98", "attribute": "deg_task_setting", "value": "physical", "source": "pdf", "locator": "PDF p. 6, Table III", "note": ""},
    {"code": "Z98", "attribute": "level_degradation", "value": "P", "source": "pdf", "locator": "PDF p. 6, Table III", "note": ""},
    {"code": "Z99", "attribute": "src_addressed", "value": "PER", "source": "card", "locator": "card: Problem, p. 1", "note": ""},
    {"code": "Z99", "attribute": "response_family", "value": "IV-A", "source": "pdf", "locator": "PDF p. 3, Sec. III-B", "note": ""},
    {"code": "Z99", "attribute": "src_selected", "value": "PER", "source": "pdf", "locator": "PDF p. 7, Table II", "note": "sequences chosen for geometric degeneracy"},
    {"code": "Z99", "attribute": "level_degradation", "value": "D", "source": "pdf", "locator": "PDF p. 7, Table II", "note": ""}
  ]
}
```

**Content of `notes.md`.** A session statement (host, model as the session configuration states it, date), start and end time, the SHA-256 of `codebook.md` as received, every file opened, every rule found ambiguous with the way it was applied, and no quotation of publisher text.

## 22. Worked boundary examples

All examples are hypothetical and describe no corpus work.

| Case | Codes |
|---|---|
| A visual odometry method is evaluated on night sequences of a public dataset and, separately, on its day sequences. | `PER` in `src_selected` (D2, rule 6). The day sequences differ in route and traffic, so they are no comparator. `level_degradation` `D`. |
| The same method is run on the night sequences with the camera stream blanked for 5 s, and with no blanking. | `PER` in `src_manipulated` (D1), `nominal_control` `yes`, `level_degradation` `D`. |
| A multi-robot mapping method is simulated with 30% packet loss only and compared with two other methods. | `COM` in `src_selected` (D2), `single_level_injection` `yes`, `nominal_control` `na`. |
| A recovery module is tested on hardware under one injected wheel-motor fault, with the module enabled and disabled, and mission success is counted per run. | `ACT` in `src_manipulated` (D1), `nominal_control` `no`, `task_setting` `physical`, `deg_task_class` `D1`, `deg_task_setting` `physical`, `level_degradation` `P`. |
| A tracking controller is simulated numerically with and without a 40% loss of wheel effectiveness, and only tracking error is reported. | `ACT` in `src_manipulated` (D1), `nominal_control` `yes`, `task_setting` `none` (tracking error is a component measure), `deg_task_class` `none`, `level_degradation` `N`. |
| The same controller study also reports safe-set violations per fault level. | `task_setting` `simulation`, `deg_task_class` `D1`, `deg_task_setting` `simulation`. |
| A crowd-navigation planner is simulated with 0, 10 and 20 pedestrians and success rates per density. | `DYN` in `src_manipulated` (D1, rule 9), `nominal_control` `yes`, `deg_task_class` `D1`, `deg_task_setting` `simulation`, `level_degradation` `S`. |
| A field deployment reports two stops caused by passers-by in its failure analysis, and the method does not address moving people. | `DYN` in `src_incidental` (D3), not in `src_addressed`. |
| A vision-language navigation method is tested on the standard unseen-scene split of a benchmark. | `MOD` is not named (rule 7). It is addressed only when the mechanism checks or bounds model errors. |
| A learned terrain-cost model trained in simulation is driven on a real robot, and real-world results are reported separately. | `MOD` in `src_selected` (D2, rule 7), and `TER` in `src_selected` when the test terrain was chosen for its difficulty. |
| Hardware runs under a named condition are shown only as a video. | The runs do not establish a physical task outcome or raise `level_degradation`. The coder notes the video. |
| A local planner uses an unmodified localization package. | `LOC` is not added to `functions`. If the planner widens its margins with the reported pose covariance, `LOC` is added. |
| Robots of one team avoid each other during coordinated exploration. | No `DYN`. Coordinated team members are not moving agents of this source. |
| An exploration planner maps an unknown static building. | No `MAP`. An unknown but static scene is not map change. |
| A cloud language model answers in 2 s, of which 1.5 s is network transfer. | Network transfer is `COM`, model inference time is `RES`. Each is coded only when addressed or named. |
| A benchmark contributes recordings built to contain smoke and dust, with no evaluated method. | `PER` in `src_selected` (D2, rule 8), `level_degradation` `X`, primary `response_family` `resource`. |
| An odometry paper on a skid-steer robot models lateral slip in turns and reports larger errors in tight turns. | `drivetrain_effect` `yes`. A paper that only names its differential-drive base codes `no`. |
| A terrain-mapping method on a legged robot uses depth and odometry inputs, and its evaluation measures map error independently of foothold planning. | `transfer_basis` `mechanism`. A method whose benefit comes from foothold selection codes `counterexample`, with criterion 2 named in the notes. |
| A mixed dataset combines aerial and handheld recordings with an unidentified carrier. | `mixed_wheeled` `no`. With one wheeled carrier among the recordings it is `yes`. |

## 23. Versions

- 1.0 (2026-11-04): first version, fixed before any work was coded.
