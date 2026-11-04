# RADIUM: Predicting and Repairing End-to-End Robot Failures Using Gradient-Accelerated Sampling

## Metadata

| Field | Value |
|---|---|
| ID | R36 |
| Title | RADIUM: Predicting and Repairing End-to-End Robot Failures Using Gradient-Accelerated Sampling |
| Authors | Charles Dawson, Anjali Parashar, and Chuchu Fan |
| Venue | IEEE Transactions on Robotics |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tro.2025.3551198](https://doi.org/10.1109/tro.2025.3551198) |
| Official URL | https://ieeexplore.ieee.org/document/10925872/ |
| Theme folder | T6-reliability-deployment |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2025-RADIUM-R36/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-RADIUM-R36/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2025-RADIUM-R36/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: ackermann
- platform: Simulated swarm search, formation control, power-grid, AV, drone and grasp problems; a 1/10th-scale car with vision in the loop (pp. 2, 11).
- boundary_platform: no
- degradation: model-error, dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Simulated and real camera for the vision-in-the-loop car
- compute: Threadripper 3990X CPU and RTX A4000 for rollouts (p. 8, Table I).
- compute_location: desktop-offline
- summary_result: Sampling failures from a failure posterior and repairing the policy yields up to five times higher hardware robustness of a vision-in-the-loop controller (p. 2).
- summary_limitation: Requires a simulator with enough fidelity; failures not modeled by the simulator cannot be predicted (p. 13).
- survey_included: yes
- verification_level: light

## Problem

Pre-deployment testing must find diverse failure modes and repair the controller before real testing.

## Mechanism

Environmental parameters are sampled by MCMC from a posterior conditioned on failure, and policy parameters are fine-tuned on discovered failures; differentiable simulation and rendering provide gradients, with a gradient-free variant (pp. 3-6).

## Baselines and controls

Gradient-based and gradient-free falsification and repair methods including L2C (pp. 7-10).

## Platform and setup

Simulated benchmarks with and without vision in the loop and hardware transfer of repaired policies (pp. 7-12). Simulated swarm search, formation control, power-grid, AV, drone and grasp problems; a 1/10th-scale car with vision in the loop (pp. 2, 11).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Simulation benchmarks and sim-to-real hardware demonstrations on a small car.

## Sensors

Simulated and real camera for the vision-in-the-loop car.

## Compute and latency

Threadripper 3990X CPU and RTX A4000 for rollouts (p. 8, Table I).

## Key quantitative results

- Differentiable simulation yields up to ten times lower cost and two times fewer iterations than gradient-free techniques (p. 1).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The method cannot predict failures not modeled by the simulator, such as dropped packets or optical glare (p. 13).

## Transfer conditions

Covers failures representable in simulation; online detection and response are outside the method.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

The article lists its differences from a conference version (p. 2); that version is not in the library, and this journal article is counted once.

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

- **p. 13, Sec. VIII-A.** "The main limitation of our approach is that it requires a simulator with enough fidelity to predict the failures of interest."
  Author-stated limit.
- **p. 13, Sec. VIII-A.** "This means that our method cannot predict any failures not modeled by the simulator."
  Scope of predicted failures.

## Survey-usable statements

### Supported

- Simulation-based failure prediction can repair controllers before deployment.

### Not supported

- Runtime faults outside the simulator model are not addressed.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 7, 8, 11, 12, 13; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Before deploying autonomous systems in safety-critical applications, we must be able to understand and verify the safety of these systems. For cases where the risk or cost of real-world testing is prohibitive, we propose a simulation-based framework for 1) predicting ways in which an autonomous system is likely to fail and 2) automatically adjusting the system’s design and control policy to preemptively mitigate those failures. Existing tools for failure prediction struggle to search over high-dimensional environmental parameters, cannot efficiently handle end-to-end testing for systems with vision in the loop, and provide little guidance on how to mitigate failures once they are discovered. We approach this problem through the lens of approximate Bayesian inference, using differentiable simulation and rendering for efficient failure case prediction and repair (and providing a gradient-free version of our algorithm for cases where a differentiable simulator is not available). We include a theoretical and empirical evaluation of the tradeoffs between gradient-based and gradient-free methods, applying our approach to a range of robotics and control problems, including optimizing search patterns for robot swarms, UAV formation control, and robust network control. Compared to optimization-based falsification methods, our method predicts a more diverse, representative set of failure modes, and we find that our use of differentiable simulation yields solutions that have up to 10x lower cost and requires up to 2x fewer iterations to converge relative to gradient-free techniques. In hardware experiments, we find that repairing control policies using our method leads to a 5x robustness improvement.
