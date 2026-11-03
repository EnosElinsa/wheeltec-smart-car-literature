# Survey coverage and supplementary IEEE evidence

Assessment date: November 3, 2026. This document evaluates coverage and use of sources; it is not manuscript text.

## Adequacy of the current corpus

The 147 selected publications (144 technical studies and three context works) provide sufficient material for a focused narrative survey. There is no universal minimum reference count. Representative mechanisms, counterexamples and supported synthesis matter more than adding citations. The corpus does not justify exhaustive or systematic coverage claims.

The reviewed index contains 127 journal and 20 conference publications; 112 have IEEE DOIs. Assessment depth is uneven: 23 full-verification cards and 124 light cards, including 89 historical conversions and 35 targeted readings. A passing card check is not whole-paper or numerical verification. Priorities are comparison of mechanisms and operating conditions, recognition of existing integrated systems, and separation of component accuracy, task outcomes, degradation tests and formal guarantees.

## Supplementary sources

The [20-source batch](../06-data/ieee-supplement-2026-11-03/README.md) has official PDF/raw-BibTeX pairs and local full-text exports for every source. Seven pairs came from user downloads. Citation bytes and source hashes are preserved. PyMuPDF4LLM extraction is distinct from the original corpus's MinerU transcriptions. The [manifest](../06-data/ieee-supplement-2026-11-03/manifest.json) records acquisition separately from reading depth; the historical 127-paper baseline is identified in [survey-inclusion.json](../06-data/survey-inclusion.json).

## Consequences for the synthesis

- N10 already integrates visual SLAM, NMPC and a safety supervisor. Its stop/relocalize procedure and restart after failed relocalization narrow the question to recovery policy, continuation of the same mission and recovery cost, rather than absence of localization/control integration.
- N09 integrates semantic reasoning and multi-robot allocation. HM3D results, quadruped demonstrations and workstation computation must be distinguished; individual results do not establish superiority in every setting.
- N11 proposes distributed integrity monitoring, but the mixed-reality evaluation uses emulated ranges and central computation. It does not establish a physical UWB implementation on a wheeled team.
- N18 includes real-time rosbag playback. Detection and inference results do not establish that autonomous response reduces mission failures.
- N19 uses teleoperated hardware collisions for localization and a separately simulated active planner. Its information-gathering mechanism does not establish autonomous hardware recovery.
- N07 evaluates prior-graph exploration in simulation; N08 uses a quasi-static terrain heuristic. Approximation results for a planning objective and physical navigation safety are different claims.
- N13 responds to predicted faults by returning simulated robots to a base, where maintenance is assumed. It is an existing task-level response, with repair and physical deployment outside the evidence.

The [source notes](../06-data/ieee-supplement-2026-11-03/evidence-notes.md) retain selected physical-page locators and evidence limits. All 20 sources now have targeted readings. The [utilization analysis](ieee-evidence-utilization-2026-11-03.md) maps them to existing sections and comparators. All 20 are now coded and incorporated into those arguments, with bibliography, counts and supplement synchronized.
