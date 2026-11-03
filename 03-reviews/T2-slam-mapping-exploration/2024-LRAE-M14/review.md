# LRAE: Large-Region-Aware Safe and Fast Autonomous Exploration of Ground Robots for Uneven Terrains

## Metadata

| Field | Value |
|---|---|
| ID | M14 |
| Title | LRAE: Large-Region-Aware Safe and Fast Autonomous Exploration of Ground Robots for Uneven Terrains |
| Authors | Qingchen Bi, Xuebo Zhang, Shiyong Zhang, Runhua Wang, Lun Li, and Jing Yuan |
| Venue | IEEE Robotics and Automation Letters, vol. 9, no. 12, pp. 11186-11193 |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2024.3486229](https://doi.org/10.1109/lra.2024.3486229) |
| Official URL | https://ieeexplore.ieee.org/document/10734213/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T2-slam-mapping-exploration/2024-LRAE-M14/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2024-LRAE-M14/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2024-LRAE-M14/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: speed-capped, few-trials
- platform_class: skid-steer
- platform: AgileX Scout 2.0 (text: "four-wheel differential drive robot", p. 5)
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Velodyne HDL-32 3D LiDAR (simulation); Livox MID360 3D LiDAR (field)
- compute: Intel NUC with Core i7-1165G7 and 32 GB RAM (field); laptop with Core i7-11800H and 16 GB RAM (simulation); no timing recorded
- compute_location: not-reported
- summary_result: Up to 45.3% higher exploration efficiency and 38.8% lower travel cost than FAEL and TARE in simulation; one field run explored 954 m² in 487 s.
- summary_limitation: No author-stated limitation is recorded in the legacy extraction; the field run was capped at 0.5 m/s on one bounded site.
- survey_included: yes
- verification_level: light

## Problem

The paper addresses autonomous exploration by a ground robot on continuously
undulating, uneven terrain. Earlier elevation or mesh traversability modules
mislabel undulating ground as non-traversable, so unknown regions (frontiers)
near slopes are missed. Exploration utilities that ignore safety, or that
greedily chase large information gain, leave coverage incomplete and make the
robot travel back and forth.

## Mechanism

LRAE maintains a global traversability map, built from the slope and
roughness of locally fitted planes on SLAM point clouds. It extracts unknown
regions (not only frontiers) and scores each one as high, medium, or low
exploration safety. A large-region-aware route optimization prefers large
unknown patches while still visiting nearby small ones, with the safety
levels as weights in the objective. Low-safety regions are deferred. The
local planner and path tracker are the same for LRAE and the comparators
FAEL and TARE.

## Baselines and controls

The comparators are FAEL and TARE, run with the same local planner and path
tracker. The legacy extraction does not record the ablation variants.

## Platform and setup

Simulation ran on a laptop (Intel Core i7-11800H, 16 GB RAM) with a Scout
2.0 model carrying a Velodyne HDL-32, A-LOAM SLAM, a 20 m × 20 m local map,
and a maximum speed of 1.0 m/s. Each method ran five times per scene, until
95% of the traversable area was explored. The field test used a Scout 2.0
with a Livox MID360 and FAST-LIO on wild uneven terrain, with a maximum
speed of 0.5 m/s and a bounded 45 m × 25 m site.

## Evidence type and transfer

The comparison numbers come from simulation. The real-world evidence is a
single closed-loop exploration run on one bounded site, at a safety speed
cap of 0.5 m/s; it shows feasibility, not a statistical comparison. The
paper describes the Scout 2.0 as a four-wheel differential drive robot,
which this library codes as skid-steer.

## Sensors

The method uses a 3D LiDAR: Velodyne HDL-32 in simulation and Livox MID360
in the field. SLAM is A-LOAM in simulation and FAST-LIO in the field.

## Compute and latency

The field computation ran on an Intel NUC (Core i7-1165G7, 32 GB RAM);
whether the NUC was mounted on the robot is not recorded in the legacy
extraction. Simulation ran on a laptop (Core i7-11800H, 16 GB RAM). Planner
timing is not recorded in the legacy extraction; not verified.

## Key quantitative results

- Exploration efficiency improved by up to 45.3% versus the state-of-the-art comparators (simulation) (p. 1).
- Travel consumption (path cost) reduced by up to 38.8% versus the comparators (simulation) (p. 2).
- Field run: exploration finished in 487 s with 954 m² of traversable area explored (p. 7).
- Field run speed cap: 0.5 m/s; simulation maximum speed 1.0 m/s (p. 7 and p. 5).
- Simulation protocol: five runs per method, terminated at 95% of the traversable area (p. 5).

## Stated limitations

No author-stated limitation is recorded in the legacy extraction; not
verified. The legacy limitations (geometric scope of the labeling problem,
speed cap, no claim about sensor faults) are reviewer observations and are
moved to Transfer conditions.

## Transfer conditions

The method needs a 3D LiDAR, LiDAR SLAM, and a traversability map built from
point clouds. The misidentification problem it solves is geometric terrain
labeling, not pedestrians or other dynamic objects. The field test was
capped at 0.5 m/s with a 20 m local map on an i7 NUC. The legacy extraction
records no claim of robustness to sensor faults beyond terrain-label errors.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. I, p. 1 | "They are prone to misidentify undulating terrains as non-traversable regions" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | weak | Sec. IV-B, p. 7 | "Considering safety, the maximum linear speed of the robot is set to 0.5 m/s." |

## Page-cited excerpts

- **p. 1, Sec. I.** "They are prone to misidentify undulating terrains as non-traversable regions"
  Terrain-sensing errors of earlier traversability modules are the failure mode that the paper targets.
- **p. 7, Sec. IV-B.** "Considering safety, the maximum linear speed of the robot is set to 0.5 m/s."
  The hardware evidence is speed-capped by design.
- **p. 1, Abstract.** "The results show that our method can safely explore uneven terrains and improve exploration efficiency by up to 45.3% compared with state-of-the-art methods."
  The headline number is an upper bound over the compared scenes, not an average.

## Survey-usable statements

### Supported

- Using traversability information to extract unknown regions and to weight exploration routes improved exploration efficiency by up to 45.3% over FAEL and TARE in simulation (numbers from a light review; re-check before citing).
- LRAE ran closed-loop on a real Scout 2.0 with a Livox MID360 on wild uneven terrain at 0.5 m/s.

### Not supported

- LRAE is faster than FAEL and TARE by 45.3% in general: this is the best case over the simulated scenes ("up to").
- LRAE is validated at speed or over many field runs: the field evidence is one run at 0.5 m/s on one site.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); the legacy card had no verbatim quotes, so excerpts were taken from the abstract and from sentences located with --find; legacy stated limitations moved to Transfer conditions
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Ground robot autonomous exploration for uneven terrains is still challenging since the rugged terrain structures not only degrade the exploration performance but also threaten the navigation safety of the robot. In this letter, a novel exploration planner is proposed for safe and fast exploration in uneven terrains. To obtain high exploration efficiency, we propose a large-region-aware exploration route optimization strategy that prioritizes exploring large regions while also considering exploring nearby small regions. To safely and completely explore uneven terrains, our planner fully introduces traversability information to extract unknown regions and assess exploration safety levels. The safety levels are then integrated into the design of the exploration strategy to ensure safe robotic exploration. We validate our method in various challenging simulation scenes and real-world wild uneven terrains. The results show that our method can safely explore uneven terrains and improve exploration efficiency by up to 45.3% compared with state-of-the-art methods.
