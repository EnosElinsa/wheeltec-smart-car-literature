# iMESA: Incremental Distributed Optimization for Collaborative Simultaneous Localization and Mapping

## Metadata

| Field | Value |
|---|---|
| ID | E40 |
| Title | iMESA: Incremental Distributed Optimization for Collaborative Simultaneous Localization and Mapping |
| Authors | Daniel McGann and Michael Kaess |
| Venue | Proceedings of Robotics: Science and Systems (RSS 2024), Delft, Netherlands, paper 85 |
| Year | 2024 |
| Type | conference |
| DOI | [10.15607/rss.2024.xx.085](https://doi.org/10.15607/rss.2024.xx.085) |
| Official URL | https://roboticsconference.org/2024/program/papers/85/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T4-multi-robot-coordination/2024-iMESA-E40/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2024-iMESA-E40/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2024-iMESA-E40/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: dataset-playback
- evidence_all: dataset-playback, numerical
- protocol_caveats: none
- platform_class: mixed
- platform: carriers not named in the paper; public Nebula Autonomy multi-robot LiDAR pose graphs (LAMP 2.0) and synthetic 2D and 3D factor graphs
- boundary_platform: yes
- degradation: communication-delay-loss, communication-partition
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: back-end inputs only: odometry and inter-robot relative-pose, bearing+range, or range factors (synthetic); LiDAR-derived LAMP 2.0 pose graphs (Nebula)
- compute: GTSAM iSAM2 per robot; average iteration below 0.04 s at 10k poses, computation only, network time excluded; processor not reported
- compute_location: desktop-offline
- summary_result: On four Nebula datasets replayed with simulated 100 m pairwise communication, iMESA's summed translational iATE was 1.46/1.20/0.65/3.14 m versus 1.48/1.20/0.53/3.05 m for centralized iSAM2.
- summary_limitation: The authors state that iMESA is sensitive to outliers, needs every started two-stage exchange to finish, has no convergence guarantee, and onboard field operation is future work.
- survey_included: yes
- verification_level: full

## Problem

A collaborative SLAM (C-SLAM) back-end has to give every robot an accurate,
up-to-date, and consistent estimate at each timestep while measurements keep
arriving. The paper assumes an ad-hoc network that is bandwidth limited, time
varying, and frequently disconnected, in which each robot may communicate
pairwise with only one other robot per timestep (p. 2). Centralized and
decentralized back-ends need a connected network and much traffic, batch
distributed solvers need hundreds to thousands of iterations (p. 3), and the
incremental distributed methods DDF-SAM2 and DLGBP lose accuracy through
inconsistent linearization points or windowing (p. 3).

## Mechanism

iMESA is an incremental version of MESA, the authors' batch consensus-ADMM
back-end with edge variables and geodesic on-manifold constraints (pp. 3-4).
Each robot keeps its own factor graph in an iSAM2 solver and adds "biased
priors" on variables it shares with other robots; the priors pull the local
solution toward edge variables, and dual variables tighten the equality
constraints over time (pp. 4-5). The key idea is to amortize the constraint
tightening of MESA over time, whenever communication happens (p. 4).

- Update (Alg. 2): new factors, new shared variables (Alg. 1 bookkeeping), and
  cached biased priors enter one iSAM2 update; variables whose edge or dual
  values changed are forced to re-eliminate through the GTSAM iSAM2 interface
  (p. 5). Caching delays the effect of a communication until the next update
  (p. 5).
- Communication (Alg. 3): two stages. The pair first exchanges the shared
  variables known to only one of them, then exchanges estimates of all jointly
  shared variables and updates edge variables (spherical/linear interpolation
  with factor 0.5) and dual variables (pp. 4, 6).
- Penalty parameter: 1e-4 for uninitialized biased priors and a constant 1.0
  after the first exchange (p. 5); only dual variables tighten constraints,
  because a growing penalty cannot be relaxed when new loop closures arrive
  (p. 6). Pose priors use sigma_r = 0.1 and sigma_t = 1 for numerical
  stability (p. 6).

## Baselines and controls

Prior incremental distributed back-ends: DDF-SAM2, implemented by the authors
with the Naive-Bayes approximation; DLGBP with the original authors' code; and
Windowed DLGBP with window size 30 (p. 6). Baselines: a centralized iSAM2
solver over all measurements, and independent iSAM2 per robot without
inter-robot collaboration (p. 6). Batch MESA is run once on a single
10k-pose dataset as a cost reference (p. 8). All methods share the same
simulated communication model in each experiment.

## Platform and setup

No robot runs in this paper. The four experiment series on synthetic data use
2D and 3D graphs built from random odometry (1 m forward or ±90° turns),
intra-robot loop closures within 2 m added with probability 0.4, and
inter-robot loop closures every 5 timesteps between robots within 30 m (p. 7):

- Measurement models (Sec. VI-B): 2D PGO, 3D PGO, 2D bearing+range, and 2D
  range-only inter-robot factors; 20 datasets each, 5 robots × 1000 poses
  (p. 7).
- Problem scale (Sec. VI-C): 5, 10, 25, and 50 robots; 20 2D PGO datasets per
  size, 500 poses per robot (p. 7).
- Long-term operation (Sec. VI-D): 5 robots, trajectories of 500 to 10000
  poses, 20 2D PGO datasets per length (pp. 7-8).
- Delayed communication (Sec. VI-E): 8 robots × 500 poses, 20 PGO datasets,
  communication only every other timestep, failure rate 0.4, and a maximum
  information delay of 0, 4, 8, or 12 timesteps (p. 9).

The real-data series replays the open-source Nebula Autonomy multi-robot
datasets (tunnel, urban, finals, KU), LiDAR 3D pose graphs produced by LAMP 2.0
in subterranean environments, with a communication range of 100 m; outlier
loop closures were removed beforehand (p. 9). The paper does not name the
robots that recorded these datasets, so platform_class is `mixed` under the
dataset rule.

Communication is simulated in every experiment: one pairwise exchange per
timestep with a robot in range (30 m, or 100 m on Nebula), and 10% of attempts
dropped "to simulate instability in robots establishing a connection" (p. 7).
The range limit creates designed disconnections (`communication-partition`)
and the drops and delays are designed (`communication-delay-loss`). The
one-exchange-per-timestep rule limits the number of messages, not a data
rate, so `bandwidth-limit` is not coded.

## Evidence type and transfer

The strongest evidence is incremental replay of public pose graphs recorded by
others (Table I), and the synthetic experiments are numerical factor graphs
without sensor simulation. The results show back-end accuracy and computation
under a modeled communication schedule. They do not show radio behavior,
message sizes, onboard timing, or any effect on navigation. Table I gives one
run per dataset; the synthetic results are box plots of 20 trials. iATE is
the incremental ATE of each robot summed over the team (p. 7), so it grows
with team size and is not a per-robot final error.

## Sensors

The back-end consumes factors, not raw sensor data. Synthetic factors are
odometry, relative-pose loop closures, and bearing+range or range inter-robot
measurements with stated noise (for example odometry 1° and 0.05 m) (p. 7).
The Nebula pose graphs come from LiDAR via LAMP 2.0 (p. 9); front-end loop
detection is outside the paper.

## Compute and latency

The implementation uses GTSAM's iSAM2 (p. 5). The processor and memory are
not reported. Iteration runtime in Fig. 7 includes update computation and the
computation during any communication, but not network transmission time; it
is averaged across robots for the distributed methods and is the single
solver's time for the centralized method (p. 8). Fig. 5 reports total runtime
averaged over trials (p. 7).

## Key quantitative results

- Nebula iATE (translation m, rotation rad), iMESA versus centralized iSAM2: tunnel 1.46, 0.091 versus 1.48, 0.093; urban 1.20, 0.071 versus 1.20, 0.076; finals 0.65, 0.094 versus 0.53, 0.096; KU 3.14, 0.117 versus 3.05, 0.118 (p. 9, Table I).
- Other Nebula rows: DLGBP 1.91, 0.093 (tunnel) and 3.37, 0.120 (KU), no values on urban and finals, where it diverged; Windowed DLGBP 1.71, 0.086 / 1.23, 0.075 / 0.85, 0.142 / 4.85, 0.140; DDF-SAM2 1.59, 0.095 / 1.63, 0.094 / 0.65, 0.094 / 3.00, 0.117; independent 1.64, 0.102 / 1.38, 0.083 / 0.71, 0.099 / 3.71, 0.124 (p. 9, Table I).
- Among the distributed methods, iMESA is uniquely lowest on 3 of the 8 Table I entries, tied with DDF-SAM2 on 3 (finals translation and rotation, KU rotation), and beaten on 2: tunnel rotation (Windowed DLGBP 0.086 versus iMESA 0.091) and KU translation (DDF-SAM2 3.00 versus iMESA 3.14) (p. 9, Table I). The authors explain that distributed results can beat the centralized optimum on real data because that optimum is not the ground truth (p. 9).
- Synthetic measurement models: the authors state that iMESA outperforms all prior works in all four formulations and is closest to centralized; in the range-only case iMESA, Windowed DLGBP, and DDF-SAM2 had outlier trials (p. 7, Fig. 3; box plots only, no tabulated values).
- Team size 5 to 50 robots: iMESA again closest to centralized in the box plots; centralized total runtime rises from about 1.7 s to about 30 s while iMESA stays below about 1 s (read from the log-scale plot) (pp. 7-8, Figs. 4 and 5).
- Long-term operation: DLGBP and Windowed DLGBP degrade with trajectory length (p. 8); at 5000 and 10000 poses both have higher translational iATE boxes than the independent baseline (read from p. 8, Fig. 6).
- Iteration runtime at 10k poses: iMESA averages less than 0.04 s, slightly more than independent iSAM2; DLGBP's final iterations take well over 1 s; Windowed DLGBP is fastest. Batch MESA needed over 800 pairwise communications and over 2 minutes of computation per robot to optimize only the final step (p. 8, Fig. 7).
- Delays of 0, 4, 8, and 12 timesteps (failure rate 0.4, every other timestep): iMESA's iATE is nearly unchanged across delays, about 2.4 m translation versus about 1.9 m centralized and about 8 m independent (read from p. 9, Fig. 8); the gap to centralized is larger than in the other experiments (p. 9).

## Stated limitations

- iMESA, like other NLS-based C-SLAM solvers, is sensitive to outlier
  measurements; robustness to local and inter-robot outliers is future work
  (p. 9). The Nebula outliers were removed for this reason (p. 9).
- The two-stage communication must be fully completed once started, and
  robustness to dropout during the exchange is future work (p. 9).
- iMESA does not guarantee convergence, because MESA has no formal convergence
  proof (pp. 4, 6); theoretical guarantees are future work (p. 9).
- Running iMESA onboard multi-robot teams in the field is future work (p. 9).
- The constant penalty of 1 can cause numerical stability issues in edge cases
  such as bearing+range inter-robot measurements (p. 6).
- Iteration runtimes exclude network transmission time (p. 8).
- The cause of DLGBP's degradation on long trajectories was not studied
  (p. 8), and the DLGBP divergence on urban and finals was the only such
  observation (p. 9).

## Transfer conditions

A wheeled team would supply its own front end: odometry, inter-robot loop
closures or range/bearing measurements, and identities of shared variables,
with outliers already rejected. No message size or data rate is reported;
only the content of a message (shared-variable sets and their estimates) is
described, so link budgets on a real radio must be measured. The
communication model is simulated, with drops at connection set-up only. The
processor behind the runtimes is unknown, and the runtime of the centralized
method is not averaged across robots, so Fig. 7 compares a single solver with
per-robot averages. Summed iATE values depend on team size and trajectory
length and cannot be compared with per-robot ATE from other papers. The code
depends on GTSAM's iSAM2 with forced re-elimination (p. 5).

## Code and data

Source code is linked as https://github.com/rpl-cmu/imesa (p. 1, footnote);
availability not verified. The Nebula Autonomy datasets are described as open
source (p. 9); no URL is given in the text.

## Version family

iMESA builds on MESA by the same group, cited as an arXiv preprint
(arXiv:2310.12320, reference [6]); MESA is not in the library. iDFGO
(Matsuka and Chung, reference [51]) is concurrent independent work, not a
version (p. 3). No other version of iMESA is in the library.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | direct-support | moderate | Sec. VI-C, p. 7 | "Here, we can see that unlike the distributed methods, the centralized baseline computational requirements scale very poorly with team size." |
| C5 | partial-support | weak | Sec. VII, p. 9 | "iMESA, like other NLS based C-SLAM solvers, is sensitive to outlier measurements" |
| C6 | qualifies | moderate | Sec. VII, p. 9 | "However, iMESA requires additional work to see success in the real-world." |

## Page-cited excerpts

- **p. 9, Sec. VI-F.** "We replay these pose-graphs incrementally for the algorithms investigated in this work"
  The real-data evidence is replay of recorded pose graphs, not a robot run.
- **p. 9, Sec. VI-F.** "In this work we do not focus on handling outliers and instead preprocess datasets to remove outlier measurements."
  Table I says nothing about false loop closures.
- **p. 7, Sec. VI-A3.** "Additionally, we randomly drop 10% of communications to simulate instability in robots establishing a connection."
  The loss model is configured at connection set-up, not measured packet loss.
- **p. 8, Sec. VI-D.** "However, it does not include network transmission time that would be required during actual communication."
  The 0.04 s figure is computation only.
- **p. 6, Sec. V-B.** "Given that MESA does not come with any convergence guarantees (See Remark 3), iMESA also does not guarantee convergence."
  Accuracy close to centralized is empirical only.
- **p. 9, Sec. VI-F.** "Interestingly, we found that DLGBP diverged on the urban and finals dataset."
  Explains the missing DLGBP cells in Table I.

## Survey-usable statements

### Supported

- With simulated single pairwise exchanges per timestep inside 30 m and 10%
  dropped connection attempts, iMESA's summed iATE was closest to centralized
  iSAM2 among the tested incremental distributed back-ends on synthetic 2D/3D
  PGO, bearing+range, and range problems (box plots, 20 trials each).
- iMESA's average iteration computation stayed below 0.04 s at 10k poses,
  excluding network time, while batch MESA needed over 800 pairwise
  communications to optimize the final step of one 10k-pose dataset.
- In synthetic 2D PGO, centralized iSAM2 runtime grew strongly with team size
  (5 to 50 robots) while the distributed back-ends stayed nearly flat.
- On outlier-free Nebula pose graphs replayed with simulated 100 m
  communication, iMESA's translational iATE was within 0.12 m of centralized
  iSAM2 on every dataset (Table I).

### Not supported

- iMESA is the most accurate distributed back-end on every Nebula entry: it is
  beaten on 2 of 8 entries (tunnel rotation by Windowed DLGBP, KU translation
  by DDF-SAM2) and tied with DDF-SAM2 on 3 (Table I).
- iMESA matches or beats centralized accuracy on real data: centralized is
  lower in translation on finals (0.53 versus 0.65 m) and KU (3.05 versus
  3.14 m).
- iMESA runs in real time onboard robots: runtimes exclude network time, the
  processor is not reported, and onboard operation is future work.
- iMESA reduces bandwidth by a measured amount: no bytes or data rates are
  reported.
- iMESA tolerates link loss in the middle of an exchange or outlier loop
  closures: both are named as open problems, and outliers were removed.
- iMESA has a convergence guarantee: the authors state it has none.

## Verification log

- 2026-10-27 | host: Kiro | scope: full text read (pp. 1-9 and reference list entries [6], [27], [51]); Table I and Figs. 3-8 read from rendered page images (pp. 7-9); all numbers and excerpts located with tools.locate | corrections: English template rebuild; Table I counterexamples to "best on every dataset" added; long-term experiment corrected from replay to synthetic data; reviewer observations moved out of stated limitations; coding added (details in tmp/corrections/E40.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/4a697e2a2c3c950d44b62ba2/

## Original abstract

This paper introduces a novel incremental distributed back-end algorithm for Collaborative Simultaneous Localization and Mapping (C-SLAM). For real-world deployments, robotic teams require algorithms to compute a consistent state estimate accurately, within online runtime constraints, and with potentially limited communication. Existing centralized, decentralized, and distributed approaches to solving C-SLAM problems struggle to achieve all of these goals. To address this capability gap, we present Incremental Manifold Edgebased Separable ADMM (iMESA) a fully distributed C-SLAM back-end algorithm that can provide a multi-robot team with accurate state estimates in real-time with only sparse pair-wise communication between robots. Extensive evaluation on real and synthetic data demonstrates that iMESA is able to outperform comparable state-of-the-art C-SLAM back-ends.
