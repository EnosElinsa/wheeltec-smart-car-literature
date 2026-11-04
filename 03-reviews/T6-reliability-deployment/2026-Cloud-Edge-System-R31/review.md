# Design and Implementation of Cloud–Edge Collaborative Mapping and Control System for Mobile Robots

## Metadata

| Field | Value |
|---|---|
| ID | R31 |
| Title | Design and Implementation of Cloud–Edge Collaborative Mapping and Control System for Mobile Robots |
| Authors | Chao Wang, Runze Gao, Jinshi Liu, Qiwen Li, Moqin Li, Xinyu Tao, Jinhui Liu, Yu Deng, Zhenglin Zou, and Yuanqing Xia |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tase.2026.3699533](https://doi.org/10.1109/tase.2026.3699533) |
| Official URL | https://ieeexplore.ieee.org/document/11550187/ |
| Theme folder | T6-reliability-deployment |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2026-Cloud-Edge-System-R31/paper.pdf` and `02-fulltext/T6-reliability-deployment/2026-Cloud-Edge-System-R31/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2026-Cloud-Edge-System-R31/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: multi-robot
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: ackermann
- platform: AgileX Hunter SE Ackermann robots with Jetson Orin NX over 5G; Kubernetes cluster for cloud services; Gazebo simulation (p. 11).
- boundary_platform: no
- degradation: compute-limit
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual
- sensors: Onboard LiDAR and chassis data through ROS
- compute: Cloud: four servers with AMD EPYC 7742 CPUs and two RTX 4080S GPUs; edge: Jetson Orin NX (p. 11).
- compute_location: mixed
- summary_result: Offloading map construction and trajectory generation to a Kubernetes cloud while keeping MPC tracking and local avoidance onboard supports outdoor two-robot coordination and scaling (pp. 15-17).
- summary_limitation: Planning and control algorithms are basic implementations; adaptive point-cloud transmission is future work (p. 19).
- survey_included: yes
- verification_level: light

## Problem

Multi-robot mapping and control need computation and bandwidth beyond small onboard computers.

## Mechanism

Containerized control services run under Kubernetes with Ceph-backed state recovery; robots connect through cloud discovery, cloud relay, leader discovery or WLAN fallback with heartbeat monitoring; the edge runs an MPC lateral controller and local collision avoidance (pp. 4-10).

## Baselines and controls

System-level performance and scaling tests rather than algorithmic baselines (pp. 14-17).

## Platform and setup

Gazebo dual-robot and platoon scenarios using the same cloud interfaces, and outdoor experiments (pp. 11-19). AgileX Hunter SE Ackermann robots with Jetson Orin NX over 5G; Kubernetes cluster for cloud services; Gazebo simulation (p. 11).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Closed-loop outdoor hardware with mixed cloud and onboard computation.

## Sensors

Onboard LiDAR and chassis data through ROS.

## Compute and latency

Cloud: four servers with AMD EPYC 7742 CPUs and two RTX 4080S GPUs; edge: Jetson Orin NX (p. 11).

## Key quantitative results

- Total system capacity is reported to scale linearly with added hardware resources (p. 15).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The planning and control algorithms are basic implementations (p. 19).

## Transfer conditions

Safety during network loss rests on the onboard controller; the fallback modes are not tested under induced outages in the inspected passages.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity; no other version is in the library.

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

- **p. 11, Sec. V-A.** "The robot base for the experiment is AgileX Hunter SE, an Ackermann mobile robot equipped with a battery pack."
  Platform.
- **p. 9, Sec. IV-B.** "If the discovery module fails to establish connections within a specified timeout, the system falls back to forming an edge LAN led by the designated edge leader."
  Connection fallback design.

## Survey-usable statements

### Supported

- Cloud-edge partitioning can keep tracking and local avoidance onboard while offloading mapping and planning.

### Not supported

- Operation through induced network outages is not demonstrated in the inspected passages.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 9, 10, 11, 15, 17, 19; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

With the increasing complexity of mobile robot systems, multi-robot collaboration has become essential. However, such collaboration places heavy demands on both computational power and communication bandwidth. Cloud computing offers elastic and scalable infrastructure, allowing robotic functions to be encapsulated and delivered as on-demand services. Meanwhile, edge computing provides low-latency processing near the data source. The integration of these paradigms enables efficient coordination between cloud and edge infrastructures, forming a solution for real-time, scalable, and intelligent robotic control. This paper presents a cloud-edge collaborative system for mobile robots. Based on cloud-native technologies, the cloud control platform is implemented on Kubernetes (K8s) to orchestrate containerized control services, enabling dynamic resource allocation and automated deployment. An edge offloading mechanism is designed to support real-time data exchange and task coordination between robots and the cloud. Furthermore, a collaborative mapping and control framework is developed, where computationally intensive tasks such as map construction and trajectory generation are offloaded to the cloud, while real-time control and data pre-processing are executed at the edge. Experimental results in outdoor environments verify that the proposed framework significantly enhances system scalability and performance. These findings confirm the feasibility and generality of the proposed approach, highlighting its strong potential for large-scale deployment in cloud-based robotic systems.
