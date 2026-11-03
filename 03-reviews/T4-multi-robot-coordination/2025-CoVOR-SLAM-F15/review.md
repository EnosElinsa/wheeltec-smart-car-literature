# CoVOR-SLAM: Cooperative SLAM Using Visual Odometry and Ranges for Multi-Robot Systems

## Metadata

| Field | Value |
|---|---|
| ID | F15 |
| Title | CoVOR-SLAM: Cooperative SLAM Using Visual Odometry and Ranges for Multi-Robot Systems |
| Authors | Young-Hee Lee, Chen Zhu, Thomas Wiedemann, Emanuel Staudinger, Siwei Zhang, and Christoph Günther |
| Venue | IEEE Transactions on Intelligent Transportation Systems, 26(7), 9358–9369 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tits.2025.3566633](https://doi.org/10.1109/tits.2025.3566633) |
| Official URL | https://ieeexplore.ieee.org/document/11005631/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T4-multi-robot-coordination/2025-CoVOR-SLAM-F15/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2025-CoVOR-SLAM-F15/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2025-CoVOR-SLAM-F15/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: multi-robot
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: DLR Rover-1 (moving camera/UWB) and Rover-2 (stationary UWB anchor); KITTI car data split into four virtual agents
- boundary_platform: no
- degradation: communication-partition
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: camera, UWB inter-rover ranges; GNSS RTK and INS for ground truth
- compute: Intel Core i7-7700HQ laptop for per-keyframe comparison; live estimator latency not reported
- compute_location: desktop-offline
- summary_result: In recorded two-rover data, CoVOR-SLAM reportedly reduced pose error versus monocular VO; numeric table values remain unverified in this light review.
- summary_limitation: The authors state that constant visual-odometry weighting may be suboptimal when it differs from true measurement covariance.
- survey_included: yes
- verification_level: light

## Problem

Inter-agent visual loop closure can improve cooperative SLAM but requires exchanging features and maps, substantial computation, and overlapping or revisited views (pp. 1–2). This paper tests whether sparse inter-agent or anchor ranges can correct visual-odometry drift and monocular scale without that exchange. It adds a concrete alternative to the survey's feature/map-exchange budget discussion while qualifying the evidence for live cooperative navigation.

## Mechanism

Each agent estimates local visual odometry; graph-based fusion exchanges keyframe poses and covariances, inter-agent ranges, and optional anchor ranges instead of feature or map points (pp. 2–3). Poses use Sim(3), retaining scale so ranges can correct monocular scale and drift. Updated keyframe poses can be returned to local maps. The architecture permits centralized or decentralized placement; the recorded-data evaluation does not establish onboard deployment (pp. 3, 6, 11).

## Baselines and controls

Recorded rover trajectories are compared with monocular VO, stereo VO, and, on football-field data only, monocular VO plus loop closure (pp. 7–8). Non-fusion VO trajectories were manually scaled using ground truth (pp. 7–8). A Kimera comparison runs VIR-SLAM and CoVOR-SLAM with the same VINS; ranges are generated from a UWB error model (pp. 8–9). The four-agent KITTI communication comparison uses CCM-SLAM and dSLAM curves, not four simultaneously driven cars (pp. 9–11).

## Platform and setup

DLR recorded football-field and gravel-pit data. Moving Rover-1 had a Bumblebee2 camera at 20 fps and DW1000-based UWB; Rover-2 remained fixed as a UWB anchor. GNSS RTK/INS supplied Rover-1 ground truth (p. 6). The paper does not specify rover drive type. Public Kimera Campus-Outdoor and KITTI sequence 00 provide supplementary playback; the single-car KITTI sequence is split into four virtual agents, with simulated ranges and a modeled 200 m cutoff (pp. 8–9).

## Evidence type and transfer

The strongest direct sensor evidence is recorded camera/UWB data from two physical rovers, one stationary. This establishes an estimation comparison, not a controller driven by the estimator or a moving four-robot team. Kimera and KITTI add public-data playback and simulated ranges, not measured four-robot link reliability (pp. 6–9).

## Sensors

The rover test fuses camera-based odometry and UWB range; optional anchor-to-agent ranges enter the graph (pp. 2–3, 6). GNSS RTK and INS provide ground truth rather than fusion input (p. 6). Kimera/KITTI range streams are modeled (pp. 8–9).

## Compute and latency

Section III compares per-keyframe module times on an Intel Core i7-7700HQ laptop with Ubuntu 20.04.2 (p. 8). The paper describes an onboard-capable architecture and simulated neighbor scaling, neither of which confirms recorded-data compute placement or end-to-end live latency (pp. 3, 6, 8). Timing table cells were not independently checked.

## Key quantitative results

- The football-field comparison reportedly places CoVOR-SLAM below monocular VO in position RMSE and near loop closure; exact Table II values were not independently checked (p. 8, Table II).
- The authors report lower transmitted data than dSLAM in a four-virtual-agent comparison; Figure 21 curves were not re-measured (pp. 10–11, Fig. 21).
- Public-data comparisons assume a 200 m link cutoff rather than measured four-rover links (p. 9).

## Stated limitations

- A constant VO weighting matrix was used because an accurate error model was difficult to obtain; the authors state that covariance mismatch can make performance suboptimal (p. 6).
- Loop closure could be compared only on football-field data because the gravel-pit rover did not revisit a recognizable place (p. 8).

## Transfer conditions

Check VO quality and scale behavior, camera–UWB calibration, range bias/multipath, anchor availability, actual communication budgets, and live compute. The four-agent result assumes simultaneous agents created from one car trajectory; it is not a real multi-car coordination trial (p. 9). An onboard-capable architecture is not evidence of measured onboard operation.

## Code and data

The paper identifies ORB-SLAM source for rover VO and VIR-SLAM as open-source, but a CoVOR-SLAM repository or rover-data release was not verified in the targeted pages (pp. 7–8). Kimera and KITTI are named public datasets.

## Version family

The authors call this an extension of their earlier 2D camera-ranging studies [17, 18] and 3D studies [19–21] (p. 1). This library counts this journal article once as F15; a duplicate library version was not identified in this light check.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | direct-support | moderate | Introduction, p. 1 | "substantial communication bandwidth is necessary to exchange large volumes of visual measurements between robots." |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. V, p. 9 | "We divided the dataset into four segments of equal duration, assuming that each segment was simultaneously collected by four cars" |

## Page-cited excerpts

- **p. 1, Introduction.** "vehicles only need to exchange their pose estimates, covariances (uncertainty) of those estimates, and inter-agent range measurements."
  This identifies the message-level mechanism, not live bandwidth.
- **p. 6, Sec. III-A.** "Experimental data was collected on a football field and in a gravel pit using multiple rovers with heterogeneous deployment."
  This is recorded sensor evidence, not a closed-loop trial.
- **p. 9, Sec. V.** "We divided the dataset into four segments of equal duration, assuming that each segment was simultaneously collected by four cars"
  This identifies the virtual-agent construction.

## Survey-usable statements

### Supported

- CoVOR-SLAM replaces inter-agent feature/map exchange with pose, covariance, and ranging exchange, and tests estimation on recorded two-rover data (pp. 1–3, 6).
- Four-agent results rely on one KITTI car sequence split into virtual simultaneous agents and simulated ranges (p. 9).

### Not supported

- CoVOR-SLAM is not shown closing a live navigation loop on physical rovers or operating on four simultaneous vehicles.
- Laptop per-keyframe comparisons do not establish measured onboard end-to-end latency.

## Verification log

- 2026-11-02 | host: Codex | scope: light targeted PDF read of physical pp. 1–3, 6–11; publisher BibTeX and excerpts checked; table cells and full paper not verified | corrections: new F15 review; recorded-data and virtual-agent boundaries explicit.
- Legacy extraction: none; new follow-up paper reviewed directly from publisher PDF.

- 2026-11-02 | host: Codex | scope: final transcription-bound validation; metadata, original abstract and retained excerpts checked with the PDF-inclusive review checker; original source bytes preserved; targeted light scope retained | corrections: parsing completed; selected excerpts shortened where OCR spacing or mathematical markup prevented matching; no whole-paper or full numeric verification

## Original abstract

A swarm of robots offers significant advantages over a single robot, enabling faster exploration of larger areas and enhanced robustness against single-point failures. Accurate relative positioning is critical for executing collaborative missions without collisions. When Visual Simultaneous Localization and Mapping (VSLAM) is employed to estimate each robot’s poses, the inter-agent loop closing method is commonly used to improve relative positioning accuracy by refining pose estimates and merging local maps based on shared feature points. However, this approach demands considerable computational and communication resources. In this paper, we introduce Collaborative SLAM using Visual Odometry and Ranges (CoVOR-SLAM) to address these challenges. CoVOR-SLAM significantly reduces both the amount of data transmitted between robots and their computational loads, as it requires only pose estimates, covariances, and range measurements instead of feature or map points for inter-agent loop detection. The necessary range measurements can be derived from pilot signals within the communication system, eliminating the need for complex additional infrastructure. We evaluated CoVOR-SLAM using real images and ultra-wideband range data collected from two rovers, as well as in a larger multi-agent setup utilizing public image datasets and realistic simulations. The results demonstrate that CoVOR-SLAM accurately estimates robot poses while requiring considerably less computational power and communication capacity than inter-agent loop closing techniques.
