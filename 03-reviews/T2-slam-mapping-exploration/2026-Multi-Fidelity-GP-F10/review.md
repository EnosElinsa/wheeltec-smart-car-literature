# Adaptive exploration under localization uncertainty using multi-fidelity Gaussian processes

## Metadata

| Field | Value |
|---|---|
| ID | F10 |
| Title | Adaptive exploration under localization uncertainty using multi-fidelity Gaussian processes |
| Authors | Demetris Coleman, Shaunak D. Bopardikar, Vaibhav Srivastava, and Xiaobo Tan |
| Venue | Autonomous Robots, vol. 50, article 10 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1007/s10514-025-10235-2](https://doi.org/10.1007/s10514-025-10235-2) |
| Official URL | https://link.springer.com/article/10.1007/s10514-025-10235-2 |
| Theme folder | T2-slam-mapping-exploration |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-Multi-Fidelity-GP-F10/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-Multi-Fidelity-GP-F10/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2026-Multi-Fidelity-GP-F10/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: external-pose-source, offboard-compute
- platform_class: aquatic
- platform: Miniglider miniature gliding robotic fish
- boundary_platform: yes
- degradation: none
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: APDS-9960 light sensor; pressure sensor, IMU, onboard camera; overhead cameras and AprilTags for external pose
- compute: Python; planner approximately 45 s per round; laptop Intel Core i5-8250U/12 GB for simulation GP training
- compute_location: mixed
- summary_result: In a miniature-fish tank experiment, the multi-fidelity GP reduced field-reconstruction WMSE versus a single-fidelity model that ignored localization uncertainty; numerical effect not rechecked.
- summary_limitation: Online hyperparameter optimization, trajectory refinement, fidelity-level selection, and analysis of the trajectory-selection heuristic remain future work.
- survey_included: yes
- verification_level: light

## Problem

Reconstruct a quasi-stationary environmental field from robot samples whose input locations have localization uncertainty, while selecting informative trajectories under a resource budget. The experiment measures light intensity in a water tank; it is not wheeled-terrain traversability.

## Mechanism

The multi-fidelity GP separates samples into datasets according to localization uncertainty. A sampling-based planner optimizes information-gain or ergodic field-reconstruction objectives under a modeled energy budget. The selected prereview did not inspect full derivations or theorem conditions.

## Baselines and controls

Hardware evaluation crosses a single- or multi-fidelity GP with information-gain or ergodic planning objectives; six trials per scenario. The single-fidelity baseline ignores localization uncertainty. Simulation adds a noisy-input single-fidelity model; its WMSE is slightly lower than the proposed method in the reported setting (p. 14).

## Platform and setup

A miniature Miniglider robotic fish explores a 4.6 m by 3.1 m by 1.2 m indoor tank with LED-generated light field. It uses overhead cameras and AprilTags for tank positioning, plus depth sensing. Hardware trials collect position and light samples at 0.5 Hz. Simulation evaluates the GP separately from physical exploration.

## Evidence type and transfer

The fish performs an adaptive exploration loop in hardware, with an external overhead-camera/AprilTag positioning system and a model-derived ground-truth field. It is aquatic boundary evidence and does not validate wheeled terrain, wheel slip, or outdoor ground navigation.

## Sensors

The measured field is blue-channel light from an Arduino BLE Sense/APDS-9960. The platform also has a pressure sensor, onboard camera, and IMU. Overhead cameras and AprilTags supply external position and yaw. The prereview did not establish which sensor signals drive every planner state estimate.

## Compute and latency

The Python planner receives approximately 45 s per graph/trajectory planning round (p. 12). Simulation GP training on roughly 2000 points uses a laptop with Intel Core i5-8250U and 12 GB RAM: seconds to a few minutes for the multi-fidelity model versus about 5-10 minutes for the custom noisy-input baseline (p. 14). Those are simulation/model-training timings, not measured onboard end-to-end latency; host allocation for every physical trial was not established.

## Key quantitative results

- Hardware trials use six trials per scenario and collect samples at 0.5 Hz (p. 12).
- The planner is allotted approximately 45 s per graph generation and trajectory-selection round (p. 12).
- Simulation training on roughly 2000 points takes seconds to a few minutes for the multi-fidelity GP versus about 5-10 minutes for the custom noisy-input GP on the cited laptop (p. 14). Values are reported in the paper but not independently rechecked here.
- The conclusion reports lower WMSE than the single-fidelity model that ignores localization error; numerical effect sizes were not re-read from figures (p. 15).

## Stated limitations

- Online hyperparameter optimization, improved trajectory estimates using smoothing or motion tomography, fidelity-level selection, and analysis of the trajectory-selection heuristic are future work (p. 15).
- The simulation comparison reports a slightly lower WMSE for the noisy-input single-fidelity model than the proposed model in that evaluated case (p. 14).

## Transfer conditions

The method relies on calibrated localization-uncertainty levels, GP hyperparameters, field-measurement assumptions, and planning objectives. In the tank setup, external pose aids localization and a GP model from manually collected samples serves as the reference field. The text states that tail energy is artificially inflated and measured power use remains future work (pp. 11-12). The experiment does not establish operation without external pose or actual energy-optimal planning.

## Code and data

The abstract links the accompanying code at https://github.com/colem404/Adaptive-Exploration-Under-Localization-Uncertainty-Using-Multi-fidelity-Gaussian-Processes/tree/main (p. 1). Repository status and reproducibility were not checked.

## Version family

The publisher PDF and BibTeX identify the 2026 Autonomous Robots volume 50 article 10, published online February 6, 2026. No version-family relationship was checked in this targeted prereview.

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

- **p. 1, Abstract.** "The proposed approach is experimentally evaluated using a miniature gliding robotic fish that measures light intensity in a large indoor tank."
  The hardware evidence concerns aquatic field reconstruction, not a wheeled terrain platform.
- **p. 11, Section 7.1.** "The depth and velocity measurements are assumed to be always known."
  The experiment uses a specific assumed depth-and-velocity availability model.
- **p. 12, Section 7.2.** "The planner is allotted approximately 45 s to generate the graph and select a trajectory."
  This is a planning-round budget, not a high-rate controller timing result.
- **p. 15, Section 9.** "the approach resulted in much smaller weighted mean squared error compared to an approach that ignores localization error"
  The conclusion's comparison is restricted to this aquatic field-reconstruction experiment.
- **p. 1, Abstract.** "accounting for data with uncertain input."
  The paper identifies input-location uncertainty as a GP reconstruction constraint.

## Survey-usable statements

### Supported

- Multi-fidelity Gaussian-process field reconstruction can account for localization uncertainty in an adaptive exploration experiment with a miniature gliding fish.
- The hardware result is aquatic and uses external pose support; numeric gains require rechecking the figures.

### Not supported

- The study validates wheeled-robot traversability or wheel-slip robustness; no ground robot is tested.
- The proposed GP dominates every uncertain-input baseline; the simulation reports a slightly lower WMSE for the noisy-input baseline.
- Energy savings or onboard real-time execution are established; power is modeled with artificial inflation and hardware execution latency was not verified.

## Verification log

- 2026-11-02 | host: Codex | scope: targeted light reading of selected PDF passages: PDF p. 1 identity/abstract/publication notice; p. 17 last page layout check only; pp. 10-12 Sections 7.1-7.2 and start of 7.3; p. 14 Section 8 targeted compute/comparison passage; p. 15 Section 9 conclusion/future work. Bounded heading/phrase scan located passages. No whole-paper, all-number, or rendered-table verification.; excerpts matched to the cited physical PDF pages; no whole-paper or complete numerical verification | corrections: targeted light prereview; aquatic boundary and external pose made explicit; no whole-paper verification; figures and numeric effects not re-read
- New follow-up acquisition; no legacy extraction. Metadata checked against the publisher PDF and unmodified publisher BibTeX. The original MinerU transcription is preserved. Its dropped letter in "difficulty" is not copied into the review; the excerpt uses an unchanged contiguous phrase and the abstract retains the publisher wording.

- 2026-11-02 | host: Codex | scope: final transcription-bound validation; metadata, original abstract and retained excerpts checked with the PDF-inclusive review checker; original source bytes preserved; targeted light scope retained | corrections: parsing completed; selected excerpts shortened where OCR spacing or mathematical markup prevented matching; no whole-paper or full numeric verification

## Original abstract

This paper considers a robot moving in a 3D environment that is tasked with estimating a quasi-stationary environmental field (e.g., temperature, concentration of a chemical pollutant, or distribution of light radiation density) in the presence of localization uncertainties, as is typical in underwater or other GPS-denied environments. Gaussian process regression has been widely adopted to model environmental fields. However, a drawback of Gaussian process regression is its difficulty in accounting for data with uncertain input. This work proposes a novel multi-fidelity Gaussian process-based regression approach to address the challenge by splitting the data collected by the robot into different datasets corresponding to the amount of input (localization) uncertainty. Furthermore, a sampling-based trajectory planning algorithm is proposed for adaptive robot exploration that optimizes a field-reconstruction objective function while accommodating resource constraints. The proposed approach is experimentally evaluated using a miniature gliding robotic fish that measures light intensity in a large indoor tank. The adaptive exploration algorithm is tested using both a multi-fidelity Gaussian process model and a baseline single-fidelity model. Two objective functions, based on the information gain and an ergodic metric, respectively, are adopted in the evaluation. The experiments show that, for both objective functions, using multi-fidelity Gaussian process reduces the weighted mean squared error between the model prediction and the ground-truth field compared to using the baseline single-fidelity model that ignores localization uncertainty. Accompanying code available at Coleman (Adaptive exploration under localization uncertainty using multi-fidelity Gaussian processes, 2025, https://github.com/colem404/Adaptive-Exploration-Under-Localization-Uncertainty-Using-Multi-fidelity-Gaussian-Processes/tree/main).
