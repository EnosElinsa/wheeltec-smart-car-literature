# Decentralized multi-robot exploration under low-bandwidth communications

## Metadata

| Field | Value |
|---|---|
| ID | F14 |
| Title | Decentralized multi-robot exploration under low-bandwidth communications |
| Authors | Jan Bayer and Jan Faigl |
| Venue | Autonomous Robots, vol. 50, article 7 |
| Year | 2026 (online 2025) |
| Type | journal |
| DOI | [10.1007/s10514-025-10234-3](https://doi.org/10.1007/s10514-025-10234-3) |
| Official URL | https://link.springer.com/article/10.1007/s10514-025-10234-3 |
| Theme folder | T4-multi-robot-coordination |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Cross-Rank-F14/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Cross-Rank-F14/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2026-Cross-Rank-F14/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: legged
- platform: Three Boston Dynamics Spot quadrupeds (p. 17)
- boundary_platform: yes
- degradation: communication-delay-loss, bandwidth-limit
- degradation_observed: communication-delay-loss
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Ouster OS0-128 LiDAR, 10 Hz; onboard localization; 868/915 MHz radios
- compute: Onboard Intel NUC10i7FNK/i7-10710U, 32 GB; nine-robot simulation used desktop i9-14900K/128 GB
- compute_location: mixed
- summary_result: One outdoor three-Spot mission lasted 575 s despite about 75% packet loss; the limited hardware run did not rank methods.
- summary_limitation: Shared-frame localization, adequate position updates, and similar robot speeds are needed; simulated drift beyond 1.5% impaired coordination.
- survey_included: yes
- verification_level: light

## Problem

Coordinate exploration across multiple robots when low-bandwidth, unreliable communication prevents sharing dense maps and waypoint sets. The target is subterranean missions, while the reported hardware demonstration is outdoors.

## Mechanism

Cross-rank uses shared position histories to favor under-visited directions at intersections. Variants combine rank with approximate route distance or TSP waypoint ordering. Each robot retains a local map and navigation system.

## Baselines and controls

Twelve coordination methods share a common navigation framework. They range from map/waypoint/position exchange to position-only methods and independent exploration. The three fastest overall methods use all three shared-data types; Cross-rank is a bandwidth/performance tradeoff.

## Platform and setup

Five simulated subterranean environments use teams of three and five; scalability simulations use seven and nine. Simulation includes unicycle motion, collisions, LiDAR raycasting, sensor noise, and action noise, but supplies pose directly. One outdoor deployment uses three Boston Dynamics Spot quadrupeds with 1 Hz position broadcasts.

## Evidence type and transfer

One physical closed-loop mission tests a position-only variant on quadrupeds, with intermittent packets and a combined map generated after the mission. Simulation tests subterranean geometry and larger teams but bypasses the localization stack. This is a legged boundary case for wheeled robots.

## Sensors

The physical payload uses an Ouster OS0-128 LiDAR at 10 Hz and 868/915 MHz communication modules. The simulator raycasts LiDAR returns and supplies robot pose directly.

## Compute and latency

On each physical robot an Intel NUC10i7FNK with i7-10710U and 32 GB RAM handles localization, navigation, and coordination. A different i9-14900K/128 GB desktop supports nine-robot simulation at real-time factor one. No onboard component or control latency was verified.

## Key quantitative results

- One hardware mission lasted 575 s with three quadrupeds, 1 Hz position broadcasts, and approximately 75% average packet loss (pp. 18-19); individual Table 7 values were not audited.
- Five simulated environments use three and five robots; scalability reaches seven and nine robots in simulation only (pp. 12-15).
- Drift above 1.5% lowers Cross-rank below independent exploration in the reported simulation (p. 19); this is not a universal threshold.
- The three fastest overall methods share maps, waypoints, and positions; Cross-rank is favored when only positions fit the bandwidth (pp. 19-20); rankings were not rechecked against rendered tables.

## Stated limitations

- Setup assumes a common coordinate frame, sufficiently wide corridors, and similar sensor characteristics (p. 5).
- Position updates must become more frequent as robot speed rises; sparse histories impair turn selection (p. 19).
- Drift over 1.5% and unequal robot speeds degrade results in the evaluated scenarios (pp. 17, 19). Heterogeneous-speed and drift improvements are future work (p. 20).

## Transfer conditions

A wheeled team needs its own local mapping/navigation stack, shared-frame localization, adequate corridor width, and enough communication for useful position histories. Temporary outages are anticipated but the physical mission still receives intermittent packets; sustained partition handling is unproved in the passages read.

## Code and data

Not established in the targeted reading; not verified.

## Version family

The current PDF and volume metadata identify Autonomous Robots 50:7 (2026). The unmodified publisher BibTeX uses its December 29, 2025 online year. Related versions were not checked.

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

- **p. 1, Abstract.** "Therefore, we propose a coordination method that satisfies low-bandwidth constraints by sharing only the robot’s positions."
  Position-only messaging is the coordination mechanism, not operation without communication.
- **p. 17, Section 7.2.** "All the robots are identical quadruped platforms, Spot by Boston Dynamics, equipped with a custom payload as depicted in Fig. 14."
  Physical evidence is legged, not wheeled.
- **p. 20, Section 9.** "However, it performs best when the bandwidth is limited to only sharing the robots’ positions."
  The advantage is conditional on the bandwidth regime.
- **p. 19, Section 8.1.1.** "Moreover, based on the reported empirical results, when the localization drift exceeds 1.5 %, the performance of the proposed method decreases below the level of independently exploring robots."
  The coordination result depends on localization quality.

## Survey-usable statements

### Supported

- Position-only Cross-rank reduces message content while retaining local mapping and navigation.
- The hardware run demonstrates one three-quadruped mission with intermittent position messages.

### Not supported

- Cross-rank is fastest at every bandwidth: the top overall methods share more data.
- The demonstrated mission is subterranean or wheeled: the hardware mission used quadrupeds outdoors.
- The run proves sustained complete-partition tolerance: messages still arrived intermittently.

## Verification log

- 2026-11-02 | host: Codex | scope: targeted light reading of selected PDF passages: PDF p. 1 identity/abstract/date; p. 27 last-page layout; selected passages pp. 2, 5, 8, 12-13, 15, 17-20. No whole-paper, full-table, or all-figure verification.; excerpts matched to the cited physical PDF pages; no whole-paper or complete numerical verification | corrections: targeted light prereview; online/bibliographic year distinction retained; legged hardware and pose/bandwidth assumptions explicit; table numbers not rechecked
- New follow-up acquisition; no legacy extraction. Metadata checked against the publisher PDF and unmodified publisher BibTeX. The original MinerU transcription is preserved; final transcription-bound validation is recorded below.

- 2026-11-02 | host: Codex | scope: final transcription-bound validation; metadata, original abstract and retained excerpts checked with the PDF-inclusive review checker; original source bytes preserved; targeted light scope retained | corrections: parsing completed; selected excerpts shortened where OCR spacing or mathematical markup prevented matching; no whole-paper or full numeric verification

## Original abstract

In this paper, we address the problem of coordinating multiple robots to explore large-scale underground areas covered with low-bandwidth communication. Based on the evaluation of existing coordination methods, we found that well-performing methods rely on exchanging significant amounts of data, including maps. Such extensive data exchange becomes infeasible using only low-bandwidth communication, which is suitable for underground environments. Therefore, we propose a coordination method that satisfies low-bandwidth constraints by sharing only the robot's positions. The proposed method employs a fully decentralized principle called Cross-rank that computes how to distribute robots uniformly at intersections and subsequently orders exploration waypoints based on the traveling salesman problem formulation. The proposed principle has been evaluated based on exploration time, traveled distance, and coverage in five large-scale simulated subterranean environments and a real-world deployment with three quadruped robots. The results suggest that the proposed approach provides a suitable tradeoff between the required communication bandwidth and the time needed for exploration.
