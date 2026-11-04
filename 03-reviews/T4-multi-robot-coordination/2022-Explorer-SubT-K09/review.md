# Resilient and Modular Subterranean Exploration with a Team of Roving and Flying Robots

## Metadata

| Field | Value |
|---|---|
| ID | K09 |
| Title | Resilient and Modular Subterranean Exploration with a Team of Roving and Flying Robots |
| Authors | Sebastian Scherer, Vasu Agrawal, Graeme Best, Chao Cao, Katarina Cujic, Ryan Darnley, Robert DeBortoli, Eric Dexheimer, Bill Drozd, Rohit Garg, Ian Higgins, John Keller, David Kohanbash, Lucas Nogueira, Roshan Pradhan, Michael Tatum, Vaibhav K. Viswanathan, Steven Willits, Shibo Zhao, Hongbiao Zhu, Dan Abad, Tim Angert, Greg Armstrong, Ralph Boirum, Adwait Dongare, Matthew Dworman, Shengjie Hu, Joshua Jaekel, Ran Ji, Alice Lai, Yu Hsuan Lee, Anh Luong, Joshua Mangelson, Jay Maier, James Picard, Kevin Pluckter, Andrew Saba, Manish Saroya, Emily Scheide, Nathaniel Shoemaker-Trejo, Joshua Spisak, Jim Teza, Fan Yang, Andrew Wilson, Henry Zhang, Howie Choset, Michael Kaess, Anthony Rowe, Sanjiv Singh, Ji Zhang, Geoffrey A. Hollinger, and Matthew Travers |
| Venue | Field Robotics |
| Year | 2022 |
| Type | journal |
| DOI | [10.55417/fr.2022023](https://doi.org/10.55417/fr.2022023) |
| Official URL | https://ieeexplore.ieee.org/document/10876072/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T4-multi-robot-coordination/2022-Explorer-SubT-K09/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2022-Explorer-SubT-K09/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2022-Explorer-SubT-K09/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: wheeled-unspecified
- platform: Custom ground robots R1-R3 with four motor/wheel modules (drive type not stated) and drones; R3 can also take tracks (pp. 19, 28).
- boundary_platform: no
- degradation: none
- degradation_observed: communication-partition, terrain
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Perception payload with LiDAR, cameras (electro-optical, thermal), IMU and RealSense depth; communications node dropper on each ground robot (pp. 5, 7, 19)
- compute: Not inspected in this reading.
- compute_location: not-reported
- summary_result: Tunnel Circuit winner and Urban Circuit runner-up, Team Explorer's two ground robots explored about 2 km and scored 13 artifacts on one tunnel day (pp. 1, 43).
- summary_limitation: Added system complexity can reduce overall reliability; artifacts were missed when not in view of the detection cameras (pp. 51-52).
- survey_included: yes
- verification_level: light

## Problem

Subterranean exploration combines mobility, communication and navigation failures, so the team needs resilient and modular autonomy across tunnel, urban and cave environments (p. 1).

## Mechanism

Wheeled ground robots and drones share Super Odometry state estimation, frontier-based exploration with multi-robot coordination, and a ledger that broadcasts records of submaps (artifacts, explored regions and other map types) and fetches missing submaps from whichever robot holds them. Ground robots drop communication nodes, placed by a prediction approach, to extend the network (pp. 5, 10, 14-21).

## Baselines and controls

Communication-node placement compares a prediction approach, a naive human-centric approach and a simulated greedy connected solution (pp. 18-19); competition results serve as system outcomes (pp. 42-51).

## Platform and setup

Tunnel Circuit (winning result), Urban Circuit (second place) and a self-organized cave test at Brady's Bend (pp. 1, 42-51). On one Tunnel Circuit day, two ground robots explored about 2 km for roughly 40 minutes (p. 43).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware` from competition runs with few repetitions; node placement is also compared in simulation. The ground robots are wheeled, with no drive type stated, so the paper is coded `wheeled-unspecified`; drones are part of the team. The provisional module `multi-robot` is confirmed: the contribution is team exploration under limited communication.

## Sensors

A perception payload combines LiDAR, electro-optical and thermal cameras, an IMU and a RealSense depth camera; LiDAR points localize 2D detections, and the RealSense covers the LiDAR blind side (pp. 5, 7).

## Compute and latency

Not inspected in this reading.

## Key quantitative results

- Tunnel Circuit: winning result; Urban Circuit: second place (p. 1).
- One Tunnel Circuit day: about 2 km explored by two ground robots and 13 correct artifacts (p. 43).
- Last Urban Circuit day: 4 positive detections, which placed the team second overall (p. 49).
- The prediction approach to node placement gives greater communication coverage than the naive approach (pp. 18-19, Table 2; values not re-read).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- More robots, interactions and autonomy increase complexity, which can reduce overall reliability even when peak performance rises (p. 51).
- Artifacts along the flight path were missed when they were outside the field of view of the detection cameras (p. 52).

## Transfer conditions

The ground robots are wheeled, but their drive type and size differ from small research platforms; the communication design (node dropping, ledger muling) transfers more directly than the mobility results. Competition runs give single outcomes per course.

## Code and data

Code availability was not checked in this targeted reading.

## Version family

Counted once by the registered Field Robotics identity in the SubT special issue. SubT-MRS (K01) later released data from the same SubT program.

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

- **p. 19, Sec. 3.3.2.** "The ledger is a record of submaps that gets broadcast over the network."
  Map sharing tolerates intermittent links by advertising and fetching submaps.
- **p. 10, Sec. 3.2.1.** "In one instance specifically, our drone was able to connect with all three of our ground vehicles simultaneously"
  The same sentence notes that R1 was cut off from the basestation by a communications failure; this motivated data muling between robots.
- **p. 19, Sec. 3.4.1.** "Within the frame are four motor/wheel modules, a battery module, and an electronics module."
  Wheeled ground robots; no drive type is stated.
- **p. 49, Sec. 4.2.** "We only scored 4 positive detections on this last day, which placed us in 2nd place overall for the competition."
  Urban Circuit outcome.

## Survey-usable statements

### Supported

- Team Explorer's wheeled ground robots and drones shared maps through a ledger that relays submaps between robots when the base station is out of reach.
- The system won the Tunnel Circuit and placed second at the Urban Circuit.

### Not supported

- The paper gives no repeated-trial statistics for the communication design in the competition runs.
- It does not evaluate how stale submaps are accepted after reconnection.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 5, 7, 10, 14, 15, 18, 19, 20, 42, 43, 49, 51, 52; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

Subterranean robot exploration is difficult, with many mobility, communications, and navigation challenges that require an approach with a diverse set of systems, and reliable autonomy. While prior work has demonstrated partial successes in addressing the problem, here we convey a comprehensive approach to address the problem of subterranean exploration in a wide range of tunnel, urban, and cave environments. Our approach is driven by the themes of resiliency and modularity, and we show examples of how these themes influence the design of the different modules. In particular, we detail our approach to artifact detection, pose estimation, coordination, planning, control, and autonomy, and we discuss our performance in the tunnel, urban, and self-organized cave circuits of the DARPA Subterranean Challenge. Our approach led to a winning result in the tunnel circuit, and placing second in the urban circuit event. We convey lessons learned in designing and testing a resilient system for subterranean exploration that can generalize to a large range of operating conditions, and potential improvements for the future.
