# LAMP 2.0: A Robust Multi-Robot SLAM System for Operation in Challenging Large-Scale Underground Environments

## Metadata

| Field | Value |
|---|---|
| ID | K07 |
| Title | LAMP 2.0: A Robust Multi-Robot SLAM System for Operation in Challenging Large-Scale Underground Environments |
| Authors | Yun Chang, Kamak Ebadi, Christopher E. Denniston, Muhammad Fadhil Ginting, Antoni Rosinol, Andrzej Reinke, Matteo Palieri, Jingnan Shi, Arghya Chatterjee, Benjamin Morrell, Ali-akbar Agha-mohammadi, and Luca Carlone |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2022 |
| Type | journal |
| DOI | [10.1109/lra.2022.3191204](https://doi.org/10.1109/lra.2022.3191204) |
| Official URL | https://ieeexplore.ieee.org/document/9830862/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T4-multi-robot-coordination/2022-LAMP2-K07/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2022-LAMP2-K07/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2022-LAMP2-K07/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Team CoSTAR datasets from Husky robots (described as wheeled, drive type not stated) and Spot quadrupeds; Huskies carry the majority of the four datasets (p. 5).
- boundary_platform: no
- degradation: data-association-fault
- degradation_observed: lidar-degeneracy
- evaluation_primary: residual
- evaluation_all: residual
- sensors: Three Velodyne LiDARs or a Hovermap on the Husky; one LiDAR or a Hovermap on Spot; LOCUS or Hovermap odometry (p. 5)
- compute: Experiments ran on a laptop with an Intel i7-8750H (12 cores); during SubT the base station was an AMD Threadripper 3990X workstation (p. 5).
- compute_location: desktop-offline
- summary_result: On four subterranean datasets of up to 6 km combined, LAMP 2.0 achieves map errors below 4 m, and GNC rejects outliers more reliably than ICM (pp. 5-7).
- summary_limitation: No limitation is stated by the authors; the evaluation replays recorded team data on a laptop running the centralized base-station software.
- survey_included: yes
- verification_level: light

## Problem

Heterogeneous robot teams in large underground spaces need one consistent map despite perceptual aliasing, varied odometry sources and intermittent links (p. 1).

## Mechanism

Each robot sends pose-graph segments and keyed scans to a centralized base station. A scalable front-end prioritizes loop-closure candidates and registers them with TEASER++ or SAC-IA initialization; the back-end rejects outliers with incremental consistency maximization (ICM) or with GNC inside Levenberg-Marquardt (pp. 2-5). Data from robots out of range are queued and sent in a batch when the link returns (p. 4).

## Baselines and controls

LAMP 1.0, no outlier rejection, odometry only, and ICM versus GNC (pp. 5-7).

## Platform and setup

Four datasets collected by Team CoSTAR: Tunnel (two Huskies, up to 2.5 km combined), Urban (two Huskies and a Spot, up to 1.5 km), Finals (three Spots and a Husky, up to 1.2 km) and Kentucky Underground (four Huskies, up to 6 km) (p. 5).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`; the letter evaluates the system offline on recorded datasets. Outlier rejection is ablated per method, not per named condition, so only `residual` is coded. Featureless narrow tunnels occur in the field data and are coded as observed. The provisional module `multi-robot` is confirmed.

## Sensors

Husky robots carry three Velodyne LiDARs or a Hovermap; Spot robots carry one LiDAR or a Hovermap; odometry comes from LOCUS or the Hovermap (p. 5).

## Compute and latency

The experiments ran on a laptop with an Intel i7-8750H processor with 12 cores; during the SubT Challenge the base station was a portable workstation with an AMD Ryzen Threadripper 3990X (p. 5).

## Key quantitative results

- Datasets: Tunnel up to 2.5 km, Urban up to 1.5 km, Finals up to 1.2 km and Kentucky Underground up to 6 km combined (p. 5).
- GNC is more robust than ICM, which failed to reject some outliers in Tunnel and was too conservative in Kentucky Underground (p. 6).
- Map errors are below 4 m on all four datasets (p. 7).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The authors state no limitation in the inspected pages.

## Transfer conditions

Inter-robot loop closures are accepted at the base station by ICM consistency checks or GNC inlier decisions. Batched data after a reconnection pass through the same checks; the letter does not evaluate stale or biased batches separately.

## Code and data

The paper releases LAMP 2.0 and a dataset; the repository https://github.com/NeBula-Autonomy/LAMP is printed on p. 2. Availability was not checked.

## Version family

Extends LAMP, the authors' earlier system (p. 1); that version is not in the library. Counted once.

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

- **p. 4, Sec. II-B.** "When a robot moves out of communication range, the pose graph and keyed scans are queued up and are then sent as a batch to the base-station when the communication is re-established."
  Behavior under link loss: data are delayed, not discarded.
- **p. 4, Sec. II-D.** "To safeguard against erroneous loop closures, our multi-robot back-end includes two outlier rejection options"
  Acceptance of inter-robot measurements relies on outlier rejection at the base station.
- **p. 5, Sec. III-A.** "The experiments in this letter ran on a laptop with Intel i7-8750H processor with 12 cores."
  Offline evaluation hardware.
- **p. 7, Sec. III-D.** "We are able to achieve map errors below 4 m in these different large-scale and challenging environments."
  Headline map accuracy.

## Survey-usable statements

### Supported

- LAMP 2.0 queues data during link loss, sends them in a batch on reconnection, and filters loop closures with ICM or GNC at a central base station.
- On recorded CoSTAR data, map errors stay below 4 m.

### Not supported

- The letter does not show how batched, stale data affect the map after a partition.
- Offline replay on a laptop is not evidence of closed-loop team navigation.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 4, 5, 6, 7; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

Search and rescue with a team of heterogeneous mobile robots in unknown and large-scale underground environments requires high-precision localization and mapping. This crucial requirement is faced with many challenges in complex and perceptually-degraded subterranean environments, as the onboard perception system is required to operate in off-nominal conditions (poor visibility due to darkness and dust, rugged and muddy terrain, and the presence of self-similar and ambiguous scenes). In a disaster response scenario and in the absence of prior information about the environment, robots must rely on noisy sensor data and perform Simultaneous Localization and Mapping (SLAM) to build a 3D map of the environment and localize themselves and potential survivors. To that end, this letter reports on a multi-robot SLAM system developed by team CoSTAR in the context of the DARPA Subterranean Challenge. We extend our previous work, LAMP, by incorporating a single-robot front-end interface that is adaptable to different odometry sources and lidar configurations, a scalable multi-robot front-end to support inter- and intra-robot loop closure detection for large scale environments and multi-robot teams, and a robust back-end equipped with an outlier-resilient pose graph optimization based on Graduated Non-Convexity. We provide a detailed ablation study on the multi-robot front-end and back-end, and assess the overall system performance in challenging real-world datasets collected across mines, power plants, and caves in the United States. We also release our multi-robot back-end datasets (and the corresponding ground truth), which can serve as challenging benchmarks for large-scale underground SLAM.
