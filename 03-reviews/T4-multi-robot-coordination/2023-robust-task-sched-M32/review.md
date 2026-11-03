# Robust Task Scheduling for Heterogeneous Robot Teams Under Capability Uncertainty

## Metadata

| Field | Value |
|---|---|
| ID | M32 |
| Title | Robust Task Scheduling for Heterogeneous Robot Teams Under Capability Uncertainty |
| Authors | Bo Fu, William Smith, Denise M. Rizzo, Matthew Castanier, Maani Ghaffari, and Kira Barton |
| Venue | IEEE Transactions on Robotics, vol. 39, no. 2, pp. 1087-1105 |
| Year | 2023 (online 2022) |
| Type | journal |
| DOI | [10.1109/tro.2022.3216068](https://doi.org/10.1109/tro.2022.3216068) |
| Official URL | https://ieeexplore.ieee.org/document/9942275/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T4-multi-robot-coordination/2023-robust-task-sched-M32/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2023-robust-task-sched-M32/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2023-robust-task-sched-M32/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: none
- evidence_type: simulation
- evidence_all: simulation, numerical
- protocol_caveats: none
- platform_class: mixed
- platform: Simulated heterogeneous agents (ground vehicles, quadcopters, service robots in the pandemic case; capture-the-flag game agents); no physical robot
- boundary_platform: yes
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual
- sensors: None (agent capabilities are modeled as random vectors)
- compute: Intel i7-7660U laptop with Gurobi; mean assignment time 0.04 s for CTAS versus 0.43 s for STRATA in capture-the-flag
- compute_location: desktop-offline
- summary_result: In capture-the-flag simulation, CTAS wins more often than STRATA and needs 0.04 s versus 0.43 s per assignment; pandemic missions scale to 140 agents and 40 tasks.
- summary_limitation: The authors leave a distributed planner for communication constraints and agent loss, and online plan updates, to future work; plans are fixed before the mission.
- survey_included: yes
- verification_level: light

## Problem

For functionally heterogeneous teams, task allocation is coupled: how to decompose a complex task with several possible role structures, whom to assign, and when the agents must arrive together. Agent capabilities and task requirements are uncertain. Earlier models often fix one decomposition, ignore capability risk, or do not scale.

## Mechanism

Capability-based robust task assignment and scheduling (CTAS) is a centralized, pre-mission mixed-integer program. Agent capabilities are random vectors (Gaussian in the tests), and task requirements are checked by a generalizable binary function over cumulative and noncumulative capabilities. The objective trades energy and time against the conditional value at risk (CVaR) of insufficient team capability. Sample average approximation and an L-shaped algorithm yield per-species network flows; a flow-decomposition program then rounds and splits the flows into individual routes that minimize the maximum individual energy. Plans are sent to the agents and do not change during execution. Communication, online recovery, and agent loss are out of scope.

## Baselines and controls

STRATA and random assignment in capture-the-flag; CTAS-D (no risk term) and CTAS-O in the pandemic case. Other controls are not recorded in the legacy extraction; not verified.

## Platform and setup

No physical robot. Three test settings:

1. Randomized flow networks for the decomposition step, up to about 70 tasks and 241 agents.
2. Capture-the-flag in a C++ simulator: 12 agents of four species (speed, view, health, ammunition), CTAS versus STRATA versus random over blocks of 500 games. Scheduling is idle here because roles (attack or defend) are lifelong.
3. Pandemic robotic services: seven species (quadcopter, several vehicle types, guidance, test, and treatment robots) and eight task types on the M3500 city road map with a Gaussian-process viral-exposure cost; missions scale to 140 agents and 40 tasks.

## Evidence type and transfer

All results come from a planner on a laptop and from game or city-routing simulation. There is no onboard execution, localization, or communication trial, so the results speak to plan quality and solve time, not to robot behavior during execution.

## Sensors

None. Capabilities are modeled distributions.

## Compute and latency

Intel i7-7660U laptop with Gurobi. Rounding takes milliseconds; the split step grows to about 197 s at about 70 tasks and 241 agents. Mean assignment time in capture-the-flag is 0.04 s for CTAS versus 0.43 s for STRATA.

## Key quantitative results

- Capture-the-flag mean assignment time: 0.04 s for CTAS versus 0.43 s for STRATA (p. 12).
- Capture-the-flag: CTAS results in a higher win rate than the baselines (p. 12, Fig. 9).
- Flow decomposition: rounding completes within several milliseconds (p. 10, Table III); the split step grows to about 197 s at about 70 tasks and 241 agents (Table III, no page).
- Pandemic services: the framework scales to 140 agents and 40 tasks (p. 13).
- Pandemic services: CTAS adds redundant agents when the CVaR term requires them while still accounting for travel cost; CTAS-D keeps a low optimality gap in the largest cases (no page).

## Stated limitations

- Future work will extend the framework to a distributed planner for scalability and robustness to communication constraints and the loss of agents (p. 16).
- Legacy-recorded future work, not located: online plan updates and recovery, learning capability and requirement parameters from execution, and a tighter energy constraint that preserves scalability.

## Transfer conditions

Legacy reviewer observations: plans are fixed before the mission, there is no onboard fault detection during execution, and the complexity of the mixed-integer program remains exponential. A wheeled-robot team would need capability distributions for each robot and a reliable channel to receive the centralized plan.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | direct-support | strong | Sec. VI, p. 16 | "The framework contributed to a domain-independent representation for complex tasks and heterogeneous agent capabilities that can generalize to multiagent applications where the major goals are satisfying task-required capabilities." |
| C5 | direct-support | strong | Sec. VI, p. 16 | "The uncertainty within the team’s capability was considered through risk minimization, and a robust metric, CVaR, was minimized to ensure the robustness to task completion (enough capability were assigned)." |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 16, Conclusion.** "The framework contributed to a domain-independent representation for complex tasks and heterogeneous agent capabilities that can generalize to multiagent applications where the major goals are satisfying task-required capabilities."
  Task success is defined over complementary heterogeneous capabilities; tests are game and service simulations, not physical multi-robot sensing.
- **p. 16, Conclusion.** "The uncertainty within the team’s capability was considered through risk minimization, and a robust metric, CVaR, was minimized to ensure the robustness to task completion (enough capability were assigned)."
  Plans are scored by task-completion risk; there is no online fault detection or recovery.
- **p. 16, Conclusion.** "Future work will consider an extension of this work to a distributed framework, which could further improve the scalability of the system and the robustness to communication constraints and the loss of agents."
  Communication constraints and agent loss remain open (the legacy card recorded this as a qualifying C4 relation); they are not measured in the experiments.

## Survey-usable statements

### Supported

- A centralized CVaR-based stochastic program jointly solves task decomposition, assignment, and scheduling for heterogeneous teams and scales to 140 agents and 40 tasks in simulation (numbers from a light review; re-check before citing).

### Not supported

- CTAS handles communication loss or agent failure during execution: plans are fixed before the mission and distributed operation is future work.
- CTAS was validated on robots: all tests are laptop solves and simulations.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-form card (Validation, Tags, Real robot, Claim summary, Hardware caveat) converted to the English template; the legacy card had two C4 rows (direct-support and qualifies), kept as one direct-support row with the qualifying quote moved to the excerpts; the 197 s split time and the CTAS-D result have no located page; Year set to 2023 (online 2022) from the publication date on p. 1
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

This article develops a stochastic programming framework for multiagent systems, where task decomposition, assignment, and scheduling problems are simultaneously optimized. The framework can be applied to heterogeneous mobile robot teams with distributed subtasks. Examples include pandemic robotic service coordination, explore and rescue, and delivery systems with heterogeneous vehicles. Owing to their inherent flexibility and robustness, multiagent systems are applied in a growing range of real-world problems that involve heterogeneous tasks and uncertain information. Most previous works assume one fixed way to decompose a task into roles that can later be assigned to the agents. This assumption is not valid for a complex task where the roles can vary and multiple decomposition structures exist. Meanwhile, it is unclear how uncertainties in task requirements and agent capabilities can be systematically quantified and optimized under a multiagent system setting. A representation for complex tasks is proposed: agent capabilities are represented as a vector of random distributions, and task requirements are verified by a generalizable binary function. The conditional value at risk is chosen as a metric in the objective function to generate robust plans. An efficient algorithm is described to solve the model, and the whole framework is evaluated in two different practical test cases: capture-the-flag and robotic service coordination during a pandemic (e.g., COVID-19). Results demonstrate that the framework is generalizable, is scalable up to 140 agents and 40 tasks for the example test cases, and provides low-cost plans that ensure a high probability of success.
