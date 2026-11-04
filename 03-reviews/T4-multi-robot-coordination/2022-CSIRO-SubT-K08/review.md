# Heterogeneous Ground and Air Platforms, Homogeneous Sensing: Team CSIRO Data61's Approach to the DARPA Subterranean Challenge

## Metadata

| Field | Value |
|---|---|
| ID | K08 |
| Title | Heterogeneous Ground and Air Platforms, Homogeneous Sensing: Team CSIRO Data61's Approach to the DARPA Subterranean Challenge |
| Authors | Nicolas Hudson, Fletcher Talbot, Mark Cox, Jason Williams, Thomas Hines, Alex Pitt, Brett Wood, Dennis Frousheger, Katrina Lo Surdo, Thomas Molnar, Ryan Steindl, Matt Wildie, Inkyu Sa, Navinda Kottege, Kazys Stepanas, Emili Hernandez, Gavin Catt, William Docherty, Brendan Tidd, Benjamin Tam, Simon Murrell, Mitchell Bessell, Lauren Hanson, Lachlan Tychsen-Smith, Hajime Suzuki, Leslie Overs, Farid Kendoul, Glenn Wagner, Duncan Palmer, Peter Milani, Matthew O'Brien, Shu Jiang, Shengkang Chen, and Ronald C. Arkin |
| Venue | Field Robotics |
| Year | 2022 |
| Type | journal |
| DOI | [10.55417/fr.2022021](https://doi.org/10.55417/fr.2022021) |
| Official URL | https://ieeexplore.ieee.org/document/10876055/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T4-multi-robot-coordination/2022-CSIRO-SubT-K08/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2022-CSIRO-SubT-K08/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2022-CSIRO-SubT-K08/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: few-trials
- platform_class: tracked
- platform: BIA5 ATR, SuperDroid LT2-F and CSIRO DTR tracked UGVs, CSIRO hexapod and Ghost Vision60 quadruped, and Emesent Hovermap UAVs; no wheeled robot (pp. 1-2, 6-7).
- boundary_platform: yes
- degradation: none
- degradation_observed: terrain, communication-delay-loss, communication-partition
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: CatPack spinning-LiDAR payload with cameras on UGVs; Hovermap payload on UAVs; CO2 and Bluetooth/WiFi sensing (pp. 5, 8, 16)
- compute: Each agent solves multi-agent SLAM onboard; ground vehicles run image inference on the NVIDIA Jetson Xavier in the CatPack (pp. 15, 21).
- compute_location: onboard
- summary_result: The team detected 11 of 80 artifacts at the Tunnel Circuit, 15 of 80 at the Urban Circuit and 16 of 44 at its Cave event (pp. 31, 33, 37).
- summary_limitation: At the Cave event, global paths and frontiers did not penalize difficult terrain enough; risk-based selection is follow-on work (pp. 35, 39).
- survey_included: yes
- verification_level: light

## Problem

A single operator must direct a heterogeneous robot team through large subterranean courses where communication degrades. The paper describes Team CSIRO Data61's system across the SubT circuit events (pp. 1-2).

## Mechanism

Homogeneous sensing payloads (CatPack on UGVs, Hovermap on UAVs) let every agent solve the same multi-agent Wildcat SLAM pose graph and share frames, frontiers, artifacts and traversability peer-to-peer. Mule, a disruption-tolerant ROS bridge, stores persistent topics on disk and synchronizes them by manifest exchange, and agents can decide to return to base to deliver data. Tracked UGVs deploy Rajant mesh drop nodes (pp. 5-6, 21-25).

## Baselines and controls

No controlled baseline; the paper compares event results and design changes across the STIX, Tunnel, Urban and Cave events (pp. 28-38).

## Platform and setup

Tunnel Circuit (August 2019), Urban Circuit (February 2020) and a self-organized Cave event (September 2020) (p. 1). Ground robots covered 7902 m over the four Urban runs (p. 33).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware` from competition runs with few repetitions. Communication loss and rough terrain occurred in the field rather than by design. The provisional module `multi-robot` is confirmed: the contribution is team operation under limited communication. All ground platforms are tracked or legged, so the paper is boundary evidence for wheeled transfer.

## Sensors

The CatPack combines a spinning LiDAR with cameras for artifact detection; UAVs use the Hovermap with a gimballed camera; UGVs add a CO2 sensor and Bluetooth/WiFi detection (pp. 5, 8, 12, 16).

## Compute and latency

Multi-agent SLAM is solved on each agent (p. 21); ground vehicles batch images from four cameras through the NVIDIA Jetson Xavier in the CatPack (p. 15). Timing was not inspected.

## Key quantitative results

- Tunnel Circuit: 11 of 80 artifacts correctly detected and located (p. 31).
- Urban Circuit: 15 of 80 artifacts; ground robots traversed 7902 m over four runs (p. 33).
- Cave event: 16 of 44 artifacts across four evaluations, with good communication links throughout (p. 37).
- Urban artifact localization: 0.46 m RMS error for nine UGV camera detections and 2.34 m for UAV reports (p. 16).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The cost of traversing difficult terrain was not sufficiently modeled, so global paths and frontier selection often crossed challenging terrain (p. 35).
- The data-sharing packages used at early events risked losing messages during long disconnections and were replaced (p. 25).
- Follow-on work includes terrain risk in frontier selection and smart nodes that store and forward data between agents (p. 39).

## Transfer conditions

The evidence comes from tracked, legged and aerial agents; a wheeled robot would inherit the communication and map-sharing design, not the mobility results. Competition runs give single outcomes per course.

## Code and data

Code availability was not checked in this targeted reading.

## Version family

Counted once by the registered Field Robotics identity in the SubT special issue. The final-event result is reported in CERBERUS (K10), which records CSIRO Data61 tied on points.

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

- **p. 25, Sec. 4.3.** "This pull-based approach is robust in the face of unreliable network conditions and allows for inter-agent data sharing without requiring end-to-end paths."
  Behavior under link loss: store, synchronize and forward.
- **p. 25, Sec. 4.3.** "This includes synchronization status for each peer, making it possible for agents to decide if they should return to base to deliver mission-critical data, as was done at the Urban and Cave events."
  Agents act on synchronization state, not only on link state.
- **p. 37, Sec. 6.4.** "Consequently, good communications links were maintained throughout; the challenge of the test was extreme traversability rather than scale."
  The Cave event did not stress communication.
- **p. 33, Sec. 6.3.** "A total of 15 out of 80 artifacts were correctly detected and localized over the duration of the event."
  Urban Circuit outcome.

## Survey-usable statements

### Supported

- Team CSIRO Data61 shared a multi-agent SLAM map peer-to-peer and used disruption-tolerant, store-and-forward messaging across tracked, legged and aerial robots.
- Agents could return to base to deliver data when synchronization was incomplete.

### Not supported

- The paper gives no controlled comparison of the communication design against an alternative.
- Its mobility results are not wheeled-robot evidence.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 5, 6, 7, 8, 15, 16, 21, 24, 25, 31, 33, 35, 37, 38, 39; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

Heterogeneous teams of robots, leveraging a balance between autonomy and human interaction, bring powerful capabilities to the problem of exploring dangerous, unstructured subterranean environments. Here we describe the solution developed by Team CSIRO Data61, consisting of CSIRO, Emesent, and Georgia Tech, during the DARPA Subterranean Challenge. These presented systems were fielded in the Tunnel Circuit in August 2019, the Urban Circuit in February 2020, and in our own Cave event, conducted in September 2020. A unique capability of the fielded team is the homogeneous sensing of the platforms utilized, which is used to obtain a decentralized multi-agent SLAM solution on each platform (both ground agents and UAVs) using peer-to-peer communications. This approach enabled a shift in focus from constructing a pervasive communications network to relying on multi-agent autonomy, motivated by experiences in early circuit events. These experiences also showed the surprising capability of rugged tracked platforms for challenging terrain, which in turn led to the heterogeneous team structure based on a BIA5 OzBot Titan ground robot and an Emesent Hovermap UAV, supplemented by smaller tracked or legged ground robots. The ground agents use a common CatPack perception module, which allowed reuse of the perception and autonomy stack across all ground agents with minimal adaptation.
