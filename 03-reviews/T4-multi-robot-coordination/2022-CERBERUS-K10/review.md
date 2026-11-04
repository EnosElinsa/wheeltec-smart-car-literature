# CERBERUS in the DARPA Subterranean Challenge

## Metadata

| Field | Value |
|---|---|
| ID | K10 |
| Title | CERBERUS in the DARPA Subterranean Challenge |
| Authors | Marco Tranzatto, Takahiro Miki, Mihir Dharmadhikari, Lukas Bernreiter, Mihir Kulkarni, Frank Mascarich, Olov Andersson, Shehryar Khattak, Marco Hutter, Roland Siegwart, and Kostas Alexis |
| Venue | Science Robotics |
| Year | 2022 |
| Type | journal |
| DOI | [10.1126/scirobotics.abp9742](https://doi.org/10.1126/scirobotics.abp9742) |
| Official URL | https://www.science.org/doi/10.1126/scirobotics.abp9742 |
| Theme folder | T4-multi-robot-coordination |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T4-multi-robot-coordination/2022-CERBERUS-K10/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2022-CERBERUS-K10/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2022-CERBERUS-K10/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: few-trials
- platform_class: legged
- platform: Four ANYmal C SubT quadrupeds in the winning prize run, aerial scouts, and a tethered wheeled rover that served as a communication hub (pp. 2-3).
- boundary_platform: yes
- degradation: none
- degradation_observed: visual-degradation, terrain, communication-partition
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: LiDAR and Alphasense Core visual-inertial cameras on all ANYmal robots; extra LiDARs, zoom and thermal cameras on Explorer units (p. 2)
- compute: CompSLAM runs onboard each robot; M3RM multi-robot mapping runs centrally on the Base Station (pp. 4-5).
- compute_location: mixed
- summary_result: In the Final Event prize run, the robots walked more than 1.7 km and reported 23 of 40 artifacts, winning on the tiebreaker with CSIRO Data61 (pp. 1-3).
- summary_limitation: Small aerial robots have limited endurance; marsupial ferrying of an aerial robot by ANYmal was finalized only after the competition (p. 5).
- survey_included: yes
- verification_level: light

## Problem

The DARPA SubT Final Event required one supervisor to explore and map an unknown underground course with a robot team under degraded sensing and limited networking. This Viewpoint summarizes Team CERBERUS's winning system (pp. 1-2).

## Mechanism

Legged ANYmal robots and aerial scouts run GBPlanner exploration, a reachability-based navigation planner and a learned perceptive locomotion controller. Each robot localizes onboard with CompSLAM; when in range, robots send odometry and compressed sensor data to the centralized M3RM factor graph at the Base Station. Carrier ANYmal robots deploy Rajant mesh nodes on supervisor command (pp. 2-5).

## Baselines and controls

No controlled baseline; the result is the competition leaderboard (p. 1).

## Platform and setup

The Final Event at the Louisville Mega Cavern in September 2021 gave each team 60 minutes to find 40 artifacts (p. 1). Robots could be tasked to stay in range, to explore beyond range for a time budget and return, or to reach a frontier or waypoint (p. 3).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware` from a single prize run. The exploring agents are legged and aerial; the wheeled rover acted only as a tethered communication hub, so the paper is coded `legged` and treated as boundary evidence. The provisional module `multi-robot` is confirmed. The article is a Viewpoint without a detailed evaluation section.

## Sensors

Both ANYmal types carry a LiDAR for SLAM and an Alphasense Core with three monochrome and four color cameras; Explorer units add two LiDARs and a pan-tilt head with zoom and thermal cameras (p. 2).

## Compute and latency

Each robot estimates pose and map onboard with CompSLAM, and M3RM runs on Base Station computers; the artifact detector runs onboard each robot (pp. 4-5). Timing is not reported in the inspected pages.

## Key quantitative results

- Prize run leaderboard: CERBERUS and CSIRO Data61 23 points each, MARBLE 18, Explorer 17, CoSTAR 13 (p. 1).
- Tiebreaker: CERBERUS reported its last artifact with more than 1 min left, CSIRO Data61 with under 30 s (pp. 1-2).
- The four ANYmal robots walked more than 1.7 km and reported 23 of 40 artifacts (p. 3).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Small aerial robots suffer from limited endurance (p. 5).
- Marsupial ferrying of an aerial robot by ANYmal was finalized only after the competition (p. 5).

## Transfer conditions

The mobility results are legged-robot evidence. The communication design (onboard fallback SLAM, centralized merging when in range, deployable mesh nodes, range-aware task modes) can be compared with wheeled teams, but no wheeled exploration is reported.

## Code and data

Code availability was not checked in this targeted reading.

## Version family

Science Robotics Viewpoint; component methods appear in separate papers cited by the authors, none of which is in the library. Counted once.

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

- **p. 3, Modes of operation.** "If it went beyond the communication range after a certain step, it would backtrack to a point with connectivity."
  Range-aware behavior when a link is lost.
- **p. 5, Resilient localization and mapping.** "When in communication range, individual robots incrementally transferred their odometry estimates and sensor data to create an inter-robot factor graph."
  Map merging happens only in range, at the Base Station.
- **p. 3, Overview of the result.** "Overall, the robots walked for more than 1.7 km and successfully identified and reported 23 of 40 artifacts that were distributed along the course."
  Single prize-run outcome.
- **p. 1, Introduction.** "As both CERBERUS and CSIRO Data61 were tied with 23 points each, the tiebreaker rule had to be invoked"
  The win was decided by a tiebreaker.

## Survey-usable statements

### Supported

- Team CERBERUS won the SubT Final Event with legged and aerial robots, onboard SLAM with a centralized merge, and deployable mesh nodes.
- Robots backtracked to connectivity or returned after a time budget, depending on the task mode.

### Not supported

- A single prize run does not establish reliability statistics.
- The Viewpoint does not provide wheeled-robot evidence.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 4, 5; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.
- abstract-waiver: the Viewpoint prints a lead summary instead of a formal abstract, and the local transcription splits two hyphenated words in it; the lead summary was copied from and checked against the PDF text layer of p. 1.

## Original abstract

This article presents the core technologies and deployment strategies of Team CERBERUS that enabled our winning run in the DARPA Subterranean Challenge finals. CERBERUS is a robotic system-of-systems involving walking and flying robots presenting resilient autonomy, as well as mapping and navigation capabilities to explore complex underground environments.
