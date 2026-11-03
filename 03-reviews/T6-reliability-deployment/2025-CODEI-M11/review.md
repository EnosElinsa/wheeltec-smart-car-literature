# CODEI: Resource-Efficient Task-Driven Co-Design of Perception and Decision Making for Mobile Robots Applied to Autonomous Vehicles

## Metadata

| Field | Value |
|---|---|
| ID | M11 |
| Title | CODEI: Resource-Efficient Task-Driven Co-Design of Perception and Decision Making for Mobile Robots Applied to Autonomous Vehicles |
| Authors | Dejan Milojevic, Gioele Zardini, Miriam Elser, Andrea Censi, and Emilio Frazzoli |
| Venue | IEEE Transactions on Robotics, vol. 41, pp. 2727-2748 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tro.2025.3552347](https://doi.org/10.1109/tro.2025.3552347) |
| Official URL | https://ieeexplore.ieee.org/document/10930687/ |
| Theme folder | T6-reliability-deployment |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T6-reliability-deployment/2025-CODEI-M11/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-CODEI-M11/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2025-CODEI-M11/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: dataset-playback
- evidence_all: dataset-playback, simulation
- protocol_caveats: none
- platform_class: road-vehicle
- platform: Smart Fortwo, Chrysler Pacifica, and Mercedes-Benz C63 catalog meshes; nuScenes vehicle data
- boundary_platform: yes
- degradation: visual-degradation
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Velodyne and Ouster LiDAR catalog; Basler and FLIR RGB cameras; nuScenes perception data
- compute: ETH Zurich Euler cluster; catalog compute choices range from Jetson Nano to AGX Orin
- compute_location: desktop-offline
- summary_result: Across 205 urban scenarios at 30 and 50 km/h, the legacy extraction records increasing resource demand as task complexity increases.
- summary_limitation: Filtering, sensor fusion, and case studies beyond autonomous vehicles are left for future work.
- survey_included: yes
- verification_level: light

## Problem

Co-design a mobile robot's body, sensing, perception, mounting, motion planner, and compute to make a specified task feasible while minimizing cost, power, computation, and mass. The coupling is between occupancy queries required by sampling-based motion planning and the perception pipeline's performance under geometry, object class, resolution, and environmental conditions.

## Mechanism

CODEI, co-design of embodied intelligence, collects planner occupancy queries in simulation and converts them into perception requirements. False-negative and false-positive rates (FNR/FPR) characterize sensor-detector performance using real nuScenes measurements and pretrained MMDetection3D detectors, with lighting and weather as discrete conditions. A weighted set-cover ILP selects and places sensors; an outer monotone co-design optimization chooses the body, planner, perception pipeline, and computing unit.

## Baselines and controls

The legacy extraction identifies catalog alternatives rather than one external controller baseline: FCOS3D and PointPillars detectors; RRT, RRT*, and lattice+A* planners; multiple bodies, sensors, and compute units. It records resource-prioritization comparisons without extracted numerical scores.

## Platform and setup

This is an urban autonomous-vehicle design case study using Smart Fortwo, Chrysler Pacifica, and Mercedes-Benz C63 meshes from TurboSquid. Sensor options include Velodyne Alpha Prime, HDL-64, HDL-32, Ouster OS2-128/64, and Basler/FLIR cameras. The task comprises 205 CommonRoad urban scenarios with bicycle-model vehicles, nominal speeds of 30 and 50 km/h, and dry/rain and day/night conditions. Occupancy queries and ray-casting occlusion are simulated. No physical robot trial is recorded.

## Evidence type and transfer

Real nuScenes data supplies perception metrics; CommonRoad and simulated geometry supply planner queries and occlusion. This combines dataset playback with simulation in a catalog-design study, rather than a deployed robot operating in rain. The road-vehicle setting is a boundary case for a small wheeled robot.

## Sensors

Velodyne and Ouster LiDAR and Basler/FLIR RGB cameras are catalog choices. FCOS3D and PointPillars provide object detection. Empirical sensor measurements come from nuScenes; no live sensor suite drives a robot in the recorded evaluation.

## Compute and latency

Occupancy-query generation and ray-casting occlusion run on the ETH Zurich Euler cluster. The design catalog spans NVIDIA Jetson Nano through AGX Orin. A deployed onboard latency or end-to-end control rate was not recorded in the legacy extraction.

## Key quantitative results

- The legacy case study evaluates 205 CommonRoad urban scenarios, with nominal speeds of 30 and 50 km/h and dry/rain and day/night conditions (p. 15).
- The legacy extraction records that increasing scenario variety, speed, or reduced prior knowledge raises resource demand; cameras are favored for cost and weight, and LiDAR for compute and energy. Numerical effect sizes were not recorded (p. 20, conclusion).

## Stated limitations

- Filtering and sensor fusion that incorporate time and uncertainty are future work; the present design uses upper bounds on FNR/FPR (p. 20).
- Case studies on tasks and robots beyond autonomous vehicles, and use of state-of-the-art software, are future work (p. 20).

## Transfer conditions

The designer must supply appropriate hardware/software catalogs; the legacy extraction notes that the supplied catalog is not claimed to be state of the art. The assumptions of planner occupancy queries, perception error abstraction, geometry, and environmental conditions need recalibration for another platform. Rain and lighting are design parameters, not evidence of weather-tested robot operation. Catalog feasibility is not a hardware or closed-loop safety validation.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | weak | Abstract, p. 1 | "Sensor and algorithm performance are evaluated using false negative rate and false positive rate across various factors such as geometric relationships, object properties, sensor resolution, and environmental conditions." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VII, p. 20 | "Moreover, we plan to conduct expanded case studies that include a variety of tasks and robots, not limited to AVs, and utilize state-of-the-art perception and decision-making software." |

## Page-cited excerpts

- **p. 1, Abstract.** "Sensor and algorithm performance are evaluated using false negative rate and false positive rate across various factors such as geometric relationships, object properties, sensor resolution, and environmental conditions."
  Environmental conditions enter the perception-performance abstraction; this excerpt alone does not quantify navigation degradation.
- **p. 20, Sec. VII.** "Moreover, we plan to conduct expanded case studies that include a variety of tasks and robots, not limited to AVs, and utilize state-of-the-art perception and decision-making software."
  The stated case-study scope leaves broader robot classes to future work.

## Survey-usable statements

### Supported

- Perception requirements and perception performance can be coupled in an ILP-based hardware/software co-design case study.
- The legacy autonomous-vehicle case study combines real-data perception characterization with simulated planning queries; any numerical survey citation requires rechecking.

### Not supported

- CODEI was validated in closed-loop operation of a physical robot in rain or darkness; the legacy evidence is catalog optimization and dataset/simulation input.
- The optimized catalog is a universal or state-of-the-art component recommendation; catalogs and task assumptions are designer inputs.
- Results establish transfer to a small service robot without recalibrating sensing, kinematics, and resources.

## Verification log

- 2026-11-02 | host: Codex | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: English template conversion; abstract copied verbatim; no legacy verbatim excerpt to retain; C2 narrowed because the excerpt states condition-dependent modeling rather than a measured navigation failure; numbers not re-verified
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

This article discusses the integration challenges and strategies for designing mobile robots, by focusing on the task-driven, optimal selection of hardware and software to balance safety, efficiency, and minimal usage of resources such as costs, energy, computational requirements, and weight. We emphasize the interplay between perception and motion planning in decision-making by introducing the concept of occupancy queries to quantify the perception requirements for sampling-based motion planners. Sensor and algorithm performance are evaluated using false negative rate and false positive rate across various factors such as geometric relationships, object properties, sensor resolution, and environmental conditions. By integrating perception requirements with perception performance, an integer linear programming approach is proposed for efficient sensor and algorithm selection and placement. This forms the basis for a co-design optimization that includes the robot body, motion planner, perception pipeline, and computing unit. We refer to this framework for solving the co-design problem of mobile robots as CODEI, short for co-design of embodied intelligence. A case study on developing an autonomous vehicle for urban scenarios provides actionable information for designers, and shows that complex tasks escalate resource demands, with task performance affecting choices of the autonomy stack. The study demonstrates that resource prioritization influences sensor choice: cameras are preferred for cost-effective and lightweight designs, while lidar sensors are chosen for better energy and computational efficiency.
