# Adaptive Fault-Tolerant Control of Wheeled Mobile Robots With Multiple Actuator Faults and Saturation

## Metadata

| Field | Value |
|---|---|
| ID | E52 |
| Title | Adaptive Fault-Tolerant Control of Wheeled Mobile Robots With Multiple Actuator Faults and Saturation |
| Authors | Hao Wu, Shuting Wang, Hu Li, Yuanlong Xie, Shiqi Zheng, and Sheng Quan Xie |
| Venue | IEEE Robotics and Automation Letters, vol. 10, no. 4, pp. 4156-4163 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3548505](https://doi.org/10.1109/lra.2025.3548505) |
| Official URL | https://ieeexplore.ieee.org/document/10910118/ |
| Theme folder | T6-reliability-deployment |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T6-reliability-deployment/2025-Adaptive-Fault-Control-E52/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-Adaptive-Fault-Control-E52/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2025-Adaptive-Fault-Control-E52/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, theory-only
- protocol_caveats: scripted-scenario, few-trials
- platform_class: differential-drive
- platform: 120 kg industrial WMR with two driven wheels (legacy description)
- boundary_platform: no
- degradation: actuator-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: wheel encoders and velocity feedback; LiDAR-based localization
- compute: industrial computer, Qt/C++; CPU and control timing not reported
- compute_location: onboard
- summary_result: Under injected faults, maximum mixed tracking-error norms were 31.4 versus 83.2/83.3 on curves and 22.2 versus 96.2/60.9 on straight paths, all multiplied by 10^-3.
- summary_limitation: The controller requires positive remaining actuator effectiveness and a positive lower bound on the effectiveness-saturation product.
- survey_included: yes
- verification_level: light

## Problem

Partial actuator loss of effectiveness, additive bias, saturation, and dead zones make accurate trajectory tracking difficult for industrial wheeled mobile robots.

## Mechanism

Nonsingular terminal sliding mode with piecewise adaptive barrier gains handles additive lock-in-place (LIP) terms and unknown dead zones. Two auxiliary variables estimate a lower bound associated with actuator effectiveness and saturation. The passive adaptive controller achieves finite-time entry into prescribed error/sliding neighborhoods, without separate fault detection or isolation.

## Baselines and controls

RIVFTC (robust intermediate-variable FTC, [17]) and MRAFTC (model-reference adaptive FTC, [20]), with the same initial conditions and injected faults.

## Platform and setup

The 120 kg two-drive-wheel industrial WMR measures 1.1 × 0.72 m, has 0.28 m wheels, and a maximum speed of 1 m/s. Curved-path tests use δ = 0.3 sin(t) + 0.7 and sinusoidal bias; straight-aisle tests use δ = 0.7 and piecewise bias. Saturation limits are 1.08/-1.27 and the dead zone is [-0.1, 0.2]. These legacy setup values were not re-verified.

## Evidence type and transfer

Conditional finite-time neighborhood-stability theory and physical trajectory comparisons under two deliberately injected fault schedules. The hardware supports tracking under those schedules, without random-fault or long-term reliability statistics.

## Sensors

The legacy extraction records 2500 ppr wheel encoders and velocity feedback. Fig. 2 shows LiDAR, IMU, ultrasound, and bumper strip. It also records LiDAR localization variation ±5 mm and QR-camera secondary localization within a ±50 mm field of view; these are inherited setup claims, not re-verified localization benchmarks.

## Compute and latency

An industrial computer runs Qt/C++. CPU model, control frequency, and per-step latency were not recorded in the legacy extraction; not verified.

## Key quantitative results

The following legacy values were located, not re-verified.

- Curved path, maximum mixed tracking-error norm, excluding initial state: proposed 31.4 × 10^-3 versus RIVFTC 83.2 × 10^-3 and MRAFTC 83.3 × 10^-3 (p. 8, Table III).
- Straight path, the same maximum norm: proposed 22.2 × 10^-3 versus RIVFTC 96.2 × 10^-3 and MRAFTC 60.9 × 10^-3 (p. 8, Table III).
- Maximum dynamic-error norm: 123 × 10^-3 on the curve and 90.9 × 10^-3 on the straight path, below prescribed 0.15/0.1 bounds respectively (p. 8, Table III).
- The straight-path mixed tracking-error norm is reported below 0.05; it combines position and attitude and must not be called pure metric position error (p. 7, Sec. IV-B).

## Stated limitations

- Assumption 2 requires 0 < δ ≤ 1, positive saturation factors, and a positive lower bound on their product; complete loss of actuation is outside these conditions (p. 3). This condition is inherited from the legacy extraction.

## Transfer conditions

Legacy reviewer observations: the experiments model LIP as additive bias, rather than recovery from a jammed or unpowered actuator. The barrier bounds tracking/sliding error, rather than an obstacle-collision safe set. Two deterministic schedules provide no random-fault success rate, lifetime, diagnosis-delay, or fault-classification evidence. Some Table III RMSE values were recorded below MAE; definitions/aggregation need clarification before reuse. That observation was not re-verified. Transfer needs compatible wheel dynamics, positive residual actuation, localization, and actuator-limit calibration.

## Code and data

The legacy extraction found no public code/data URL in the paper; availability was not verified.

## Version family

RA-L 2025. The authors' 2024 disturbance-rejection tracking work is background; the legacy extraction records no conference-extension statement or same-work relationship to another selected paper.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | partial-support | moderate | Sec. IV-B, Results Analysis, case 2, p. 7 | "the proposed fault-tolerant controller has tracking error smaller than 0.05." |
| C6 | qualifies | moderate | Abstract, p. 1 | "being confined within a predetermined neighborhood of the origin" |

## Page-cited excerpts

- **p. 7, Sec. IV-B, Results Analysis, case 2.** "the proposed fault-tolerant controller has tracking error smaller than 0.05."
  This is a mixed tracking-error norm under an injected fault schedule.
- **p. 1, Abstract.** "being confined within a predetermined neighborhood of the origin"
  The guarantee concerns an error neighborhood rather than exact zero error or collision avoidance.

## Survey-usable statements

### Supported

- Adaptive FTC maintains bounded tracking under the reported partial-effectiveness, bias, saturation, and dead-zone schedules on an industrial WMR (light review).

### Not supported

- Recovery from zero actuator effectiveness or a fully jammed drive: positive residual effectiveness is required.
- Obstacle-collision safety or long-term reliability: the evidence concerns tracking and two injected fault schedules.
- A pure position error below 0.05 m: the norm mixes position and attitude.

## Verification log

- 2026-11-02 | host: Codex | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format conversion; located legacy quote retained and short abstract excerpt added; legacy numbers and metric caveats not re-verified
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/4eb48e75c8cb2c5b377fcc83/
- Legacy provenance: selection_id 4eb48e75c8cb2c5b377fcc83; PDF SHA-256 7779f424b52edfc7e59ea3ca0256582a7f5e202843ae27e43082d83013c5a18f (inherited, not re-hashed).

## Original abstract

The actuator fault problems under saturation bring significant challenges to the stable and accurate tracking ofwheeled mobile robots (WMRs) in industrial applications. This letter proposes a novel adaptive fault-tolerant control (FTC) method for WMR systems simultaneously considering uncertain multiple actuator faults, namely lock-in-place (LIP) and partial loss-ofeffectiveness (LOE) faults, and saturation. First, a novel barrier function-based nonsingular terminal sliding mode controller is explored to address the actuator LIP failures and unknown dead zones. Then, a two-auxiliary-variable-based adaptive law is designed by estimating the boundary of the actuation effectiveness and saturation coefficient, and uniformly handles the actuator LOE fault and saturation. The adaptive fault-tolerant controller is constructed based on these adaptive laws, achieving the error/sliding variables finite-time convergence and being confined within a predetermined neighborhood of the origin. Finally, practical experiments demonstrate the effectiveness and advantages ofthe designed FTC scheme.
