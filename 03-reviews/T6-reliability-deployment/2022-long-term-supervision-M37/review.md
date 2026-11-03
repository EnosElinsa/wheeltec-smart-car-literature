# User feedback and remote supervision for assisted living with mobile robots: A field study in long-term autonomy

## Metadata

| Field | Value |
|---|---|
| ID | M37 |
| Title | User feedback and remote supervision for assisted living with mobile robots: A field study in long-term autonomy |
| Authors | Matteo Luperto, Marta Romeo, Javier Monroy, Jennifer Renoux, Alessandro Vuono, Francisco-Angel Moreno, Javier Gonzalez-Jimenez, Nicola Basilico, and N. Alberto Borghese |
| Venue | Robotics and Autonomous Systems, vol. 155, article 104170 |
| Year | 2022 |
| Type | journal |
| DOI | [10.1016/j.robot.2022.104170](https://doi.org/10.1016/j.robot.2022.104170) |
| Official URL | https://linkinghub.elsevier.com/retrieve/pii/S0921889022000963 |
| Theme folder | T6-reliability-deployment |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T6-reliability-deployment/2022-long-term-supervision-M37/paper.pdf` and `02-fulltext/T6-reliability-deployment/2022-long-term-supervision-M37/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2022-long-term-supervision-M37/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: offboard-compute
- platform_class: wheeled-unspecified
- platform: Giraff-X socially assistive robot (MoveCare system), 10 robots analyzed in older adults' apartments in Milan and Badajoz
- boundary_platform: no
- degradation: none
- degradation_observed: visual-degradation, dynamic-objects, scene-change, actuator-fault, sensor-fault, communication-delay-loss, communication-partition, energy-limit
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Hokuyo URG 2D LiDAR (navigation), two Orbbec RGB-D cameras (obstacle avoidance and user detection), visual docking landmark; home IoT PIRs, door sensor, and room microphones
- compute: on-board computer and NVIDIA Jetson TX2 labeled in Fig. 3; onboard navigation assumed; not described; VC, speech services, and MLS run in the cloud over MQTT; no runtimes reported; MLS snapshots every 30 min
- compute_location: mixed
- summary_result: Across 10 homes and 132 robot-weeks, 86.46% of attempted WM, SQ, and REM interventions succeeded, and the robots lost localization 455 times over 13883.42 m.
- summary_limitation: Autonomous recovery from idle-time events was often impossible, causes of lost localization were not ascertained, and unstable home internet delayed speech and caused the only drop-out.
- survey_included: yes
- verification_level: full

## Problem

Socially assistive robots (SARs) in older adults' private apartments face
unstructured and dynamic homes, where intricate corridors, narrow doorways,
and movable objects degrade performance or cause failures that need costly
recovery by trained personnel (p. 1). The authors argue that the list of
troublesome situations is too broad to elicit in laboratory tests, so remote
control and supervision become key functions, and that users lose trust when
they do not understand the robot's behavior (p. 2). The paper asks how a
remote Monitoring and Logging System (MLS) and a feedback loop between older
adults, caregivers, and technicians affect the reliability and acceptance of
autonomous SARs, and reports a multi-month field deployment in the H2020
MoveCare project.

## Mechanism

The MoveCare system combines the Giraff-X robot with an IoT network (PIR
motion sensors, a door contact sensor, smart microphones in each room, and
active sensors such as a weight scale), a Community Based Activity Center
reached through a tablet or TV, and a cloud Virtual Caregiver (VC) that
orchestrates the scenarios over MQTT (pp. 3, 6). An intervention follows
eight steps: the robot receives the request by MQTT, undocks, navigates to the
user location estimated from the IoT network, searches the house if the user
is not there, approaches the user, runs the interaction, reports to the VC,
and returns to the docking station (pp. 3-4). Table 2 lists the intervention
types, including reminders (REM), spot questions (SQ), weight measurement
(WM), neuropsychological tests, call for help (CH), find lost object,
teleoperation, go dock, and talk (p. 5).

Navigation uses a 2D static map built at installation, with poses inserted
manually in each room as navigation targets, and the ROS navigation stack;
point clouds from two RGB-D cameras are used for obstacle avoidance and user
detection, and a navigation assistant inserts waypoints in narrow doorways or
corridors (p. 4). Navigation is based on a 2D LiDAR, while autonomous docking
observes a visual landmark on top of the docking station (p. 4).

Self-management keeps the battery above a healthy threshold even without
connectivity, and the localization estimate is reset every time the robot
reaches the known location of the docking station, to stop localization
errors from accumulating (pp. 4-5). When a task cannot be completed, the robot
informs the VC and returns to the dock; after three failed docking attempts it
asks the user for help by voice, and if nobody responds it continues its
recovery behaviors until the battery reaches a critical level (<10%), then
shuts down (p. 5).

The user search starts at the room estimated by the VC from PIR data, then
visits all rooms in an order sent by the VC, reaching every pose in a room and
turning 360 degrees at each pose; it ends when the user is found, the
intervention is canceled, or a timeout is reached (p. 5). The interaction
uses cloud speech services with red and green buttons as a fallback, and
repeats a question once after 30 s without an answer before the interaction
counts as unsuccessful (p. 5). The VC schedules interventions only between
9:00 and 19:00, and the robot independently refuses interventions between
22:00 and 8:00, with call for help as the only exception (p. 6); Table A.2
gives 22:00 to 9:00 for the robot rule (p. 16).

The MLS is a cloud web application that receives the MQTT messages of all
components, updates their status, forwards it in real time to every client
watching the same user, and stores the events in a database (p. 6). Its
interface shows the IoT status, the map with the live robot position, the
robot status (pose, battery charge and voltage, goal, navigation progress),
and the VC state (p. 6). Every 30 min it stores a snapshot of all installed
systems, which supports replay on an interactive timeline at 1x to 20x speed
to retrace the chain of events before an anomaly (p. 7). The MLS performs no
automatic anomaly detection: the authors only provided an interface for
logged data (p. 13), and people diagnose failures by inspecting it.

## Baselines and controls

The paper has no baseline system, no ablation, and no deployment without the
MLS, so the effect of remote supervision on acceptance is not measured against
a control. Table 1 compares MoveCare qualitatively with Hobbit, SYMPARTNER,
SERROGA, CompanionAble, EnrichMe, Fiorini et al., and Giraffplus on pilot
size, duration, proactivity, user search, IoT integration, remote
supervision, and autonomous navigation (p. 3). The intervention statistics
are restricted to SQ, WM, and REM, chosen because they are the most
frequent, need user search and interaction, have comparable duration, and are
triggered by the VC (p. 10). Four of the 14 participants were excluded for
reasons outside the reference scenario (p. 8). Questionnaire answers were
compared between countries with a Mann-Whitney U test (p. 12).

## Platform and setup

Robot. Giraff-X is described as an enhanced and autonomous version of the
Giraff teleoperated robot developed for ambient assisted living (p. 3). Fig. 3
(p. 4) labels its parts: a robotic wheeled platform, an on-board computer, an
NVIDIA Jetson TX2, a Hokuyo URG laser scanner, two Orbbec RGB-D cameras, a
fish-eye webcam, a touchscreen, a microphone and speaker, an RF-ID module with
antennas, action buttons, and an emergency button. Neither the text nor Fig. 3
gives the drive type, wheel layout, dimensions, or speed. The paper refers to
[33] (ECMR 2019) for the robot setup; that reference is not in this library
and was not checked. The platform class is therefore coded as
wheeled-unspecified, with the wheeled base taken from the Fig. 3 label. The
authors mention "the size of the robot" when discussing intrusiveness
(p. 12).

Laboratory tests and prepilots. Lab tests of navigation, autonomous docking,
and speech recognition reached success rates well above 90% (p. 7). The
first prepilot was a 9-day trial in a Milan apartment with approximately
65 m2 of free area and 3 furnished rooms, where a single user received 116
interventions; 3 failed and needed manual recovery, 22 docking attempts
failed, and passages with less than 70 cm of free space slowed navigation
(p. 7). The second prepilot installed the full system in one apartment of a
care facility in Extremadura, where 7 residents tested manually triggered
scenarios (p. 8).

Field study. Participants had to be over 65, without cognitive impairment,
and living independently on their own, and apartments could not have pets,
rugs, or stairs (p. 8). Of 14 selected older adults (average age 76.86), 7
lived in Milan (ITA) and 7 in Badajoz (ESP); 3 ITA participants lived in an
assisted living facility (p. 8). The campaign ran in two rounds, September
to December 2019 and January to April 2020; the fleet was active for 132
weeks in total, and each included participant accrued at least 10 weeks
(p. 8). Table 3 gives per-user durations from 10 to 23 weeks (p. 10). Results
come from 10 users (average age 75.3). The 4 excluded users were an ESP user
who dropped out because of poor internet, an ESP user whose robot could not
move for almost the whole pilot because of internet problems, a 92-year-old
ITA user who kept the system off, and an ITA user whose facility turned the
robot off during the COVID-19 lockdown (p. 8). Maps covered only the rooms
where the robot was meant to operate; bathrooms were excluded by agreement
with the Ethics Committee, and users could exclude further rooms (p. 8). The
robots stayed on day and night, and users could disable the system with a
wireless button or the emergency stop (p. 8). Three robots were replaced after
failures of the motor control board and battery, with approximately 2 weeks
per repair not counted as pilot time (p. 9). Most of the second round took
place during the COVID-19 lockdown without in-place support (p. 12). The
Italian pilot was run by researchers who designed the system, the Spanish
pilot by external contractors briefed in a couple of sessions (p. 13). The
robot questionnaire was given approximately a week after uninstallation by a
team member not involved with the user or the pilot (p. 8).

Field conditions. No operating condition was designed, injected, or varied in
the pilot. The following conditions occurred and are reported, and they are
coded as observed: darkness, in which the visual docking of the ITA-1 robot
failed and the robot shut down to preserve its batteries (p. 11; Table A.2,
p. 16); users who blocked the robot's path or changed location before the
approach (pp. 11, 14); objects or furniture that were frequently moved in
areas of lost localization (p. 14); the motor control board and battery
failures that required replacing three robots (p. 9); an IoT microphone that
wrongly detected a call for help at midnight, an IoT sensor fault discovered
through the MLS, and microphones that triggered too many calls for help
(p. 11; Table A.2, p. 16); speech delays caused by unstable internet (p. 13);
the system being offline because of user disabling or internet problems,
which left about 7% of interventions not performed (p. 11); and critical
battery levels after navigation or docking failures (p. 11; Table A.2,
p. 16). No results are reported per condition.

Count inconsistencies. The abstract reports a 130-week study (p. 1) and the
introduction "more than 130 weeks" (p. 2), while Sec. 6.1 gives 132 weeks
(p. 8). Table 1 lists the MoveCare pilot with 13 users and 10-16 w (p. 3),
which matches neither the 14 selected users, the 10 analyzed users, nor the
23-week duration of ESP-1 in Table 3 (p. 10).

## Evidence type and transfer

The robots navigated autonomously in occupied homes and executed
VC-triggered interventions, so the results are closed-loop hardware evidence
of a complete assistive system. The VC, the speech services, and the MLS ran
in the cloud, so every intervention depended on home internet (coded as
offboard-compute). Because nothing was designed or varied, degradation is
coded as none; the field conditions above are coded as degradation_observed.
The MLS itself is a human-in-the-loop supervision tool: the reliability and
acceptance gains attributed to it rest on case studies (Sec. 6.3) and a
post-pilot questionnaire of 10 users, with no condition without the MLS.
Localization is not measured against ground truth; trajectories and
lost-localization counts are the robot's own estimates (p. 9), and the causes
of failed searches cannot be separated (p. 10). The homes were screened for
navigation (no pets, rugs, or stairs) and bathrooms were not mapped, so the
numbers describe preselected indoor apartments. The authors report that the
robots caused no damage to furniture and did not collide with users (p. 9);
this is an observation without a stated counting protocol.

## Sensors

Robot: a 2D LiDAR used for navigation, which Fig. 3 labels as a Hokuyo URG
laser scanner; two RGB-D cameras, labeled Orbbec in Fig. 3, for obstacle
avoidance and user detection; a visual landmark on the docking station for
docking, with the observing camera not named; voice through cloud speech
services; and red and green buttons (pp. 4-5, Fig. 3). Fig. 3 also shows a
fish-eye webcam, a touchscreen, a microphone and speaker, and an RF-ID module
with antennas, and marks the Hokuyo scanner, the Orbbec cameras, the RF-ID
module, the emergency button, and the Jetson TX2 as added in Giraff-X (p. 4).
Environment: PIR sensors that give the VC a room-level user location, a door
contact sensor, smart microphones in each room for commands and calls for
help, a connected weight scale, and RFID tags for the find lost object
scenario (pp. 3, 5-6). No ground-truth sensor for robot or user position was
used (p. 9).

## Compute and latency

The text does not describe the robot's processor, onboard software, or
timing. Fig. 3 labels an on-board computer and an NVIDIA Jetson TX2 on the
robot (p. 4), but the paper does not say which software runs on either, and
no per-module runtime is reported. compute_location is coded as mixed:
onboard navigation assumed; not described. The robot exchanges JSON messages
over MQTT with a shared cloud platform (p. 6), the VC and the speech module
run as cloud services (pp. 5-6), and the MLS is a cloud web application
(p. 6). The only timing parameters are the 30 s answer timeout (p. 5), the
30 min MLS snapshot interval, and the 1x to 20x replay speed (p. 7). Internet
problems added a substantial delay to speech recognition (p. 13), reflected
in low scores for Q15; no latency values are given.

## Key quantitative results

- The 10 analyzed robots covered 13883.42 m in total (mean 1388.34 m per robot) and moved for 488.095 h (mean 48.81 h per robot) (p. 10, Table 3).
- Table 3 lists the ITA distance as 7571 (M = 5110.77) and the ESP distance as 6312 (M = 1514.2); the ITA rows sum to 7571 m (mean 1514.2 m) and the ESP rows to 6312.42 m (mean 1262.5 m), so 1514.2 is the ITA mean and both printed means are misplaced or wrong (p. 10, Table 3).
- The robots were idle at the docking station 97.98% of the time on average according to the text, while Table 3 lists 97.97% for all users (pp. 9-10, Table 3).
- The robots were active for approximately 1000 days but performed at least one complete intervention on only 534 days, because of the low-intrusion VC policy and users being away during the 9:00 to 19:00 window (pp. 9-10, Table 3).
- The robots reported 455 lost-localization events in total, a mean of 45.5 per robot (p. 10, Table 3).
- ITA-1 lost localization 50 times in 1767 m and ESP-3 79 times in 1337 m, with failures for ESP-3 mostly in the central room with a dining table and chairs (p. 9, Figs. 9 and 10).
- ESP-1 lost localization 68 times in 1440 m, repeatedly in an area around a table and chairs (p. 14, Fig. 14).
- The robots found the user in 660 of 869 searches (75.95%), excluding cases where the user was already in front of the robot and no search started; Fig. 11 labels the 209 failed searches as 25.05%, while 209 of 869 is 24.05% (p. 10, Fig. 11).
- Of 1151 interactions after the user was found, an answer was obtained in 98.09%: users went ahead with the interaction in 1016 (88.27% of all interactions), asked for "Later" in 113 (9.81%), and gave no answer in 22 (1.91%); the text calls 88.27% and 9.81% shares of the answered cases, but the Fig. 12 counts make them shares of all 1151 (p. 10, Fig. 12).
- Of 1539 requested SQ, WM, and REM interventions, 1130 succeeded, 177 failed, and 232 were not performed; the reported success rate of 86.46% is the share of successes among the 1307 attempted interventions (successful plus failed) (p. 10, Table 3).
- The text states that the robots tried to complete 72.42% of requested interventions, but Table 3 lists 73.42% as Performed (%) for all users, and its Performed (%) values equal N Successful divided by N Total; the attempted share computed from Table 3 is 84.93% (1307 of 1539) (p. 10, Table 3).
- Approximately 7% of interventions were not performed because the system was offline (user disabling or internet problems) and 4.56% because the IoT system signaled the user as outdoors (p. 11, Fig. 13).
- In approximately 10% of cases the robot failed to approach a located user (user moved, navigation failure, or localization failure), in 1.5% it never found the user, and in 1.5% the speech interaction failed (p. 11, Fig. 13).
- In failed interventions the robots almost never detected or approached the user but spent a lot of time navigating (pp. 14-15, Fig. 15).
- Questionnaire medians on the 1 to 5 Likert scale were 5 for Q1, Q2, Q4, and Q5 (safety and comfort during navigation and approach), 2.5 for easy interaction through vocal commands (Q13), and 2 for not perceiving delays (Q15); Q6 differed most by country (median 1 ITA, 4 ESP), and a Mann-Whitney U test found no significant country effect (pp. 12-13, Table 4).

## Stated limitations

- Idle time dominates long-term operation and raises the chance of unexpected events such as undocking or power and internet outages, which are hard to foresee, model, and detect; autonomous recovery from them is often impossible in practice, and most critical user reports concerned such events (p. 13).
- Unstable home internet delayed speech recognition, led to the only drop-out, and was not fully solved by the countermeasures (p. 13).
- Recovery behaviors after lost localization were mostly insufficient, so the robot had to ask its user for help, and the specific reasons for the lost localization were not ascertained (p. 14).
- The causes of failed searches (IoT user localization, camera detection, or both) cannot be determined, and failed interventions are costly because the robot travels far; the authors suggest dropping an intervention after a predetermined time (p. 14).
- The conservative navigation policy adopted for user comfort increased the chances of the robot getting stuck during navigation (p. 14).
- Rare combinations of events, such as the night failure, did not occur in the prepilots, and well-defined methods for such combinations remain an open problem (p. 13).
- The country comparison of questionnaire answers rests on a very small sample (5 Italian and 5 Spanish users), and Q6 was ambiguous in translation (p. 12).
- Two fixes in Table A.2 (a light with movement sensors on the docking station and a "Come here" voice command) were implemented and tested but not deployed during the pilot for safety reasons during the COVID-19 pandemic (p. 16).
- Online anomaly detection and learning from robot experience are left to future work (p. 15).
- Data harvesting by the MLS raises ethical challenges; the MLS performed no additional reasoning or pattern analysis on the logs (p. 13).

## Transfer conditions

Before reusing these results on another wheeled robot, a reader must check
the environment (indoor apartments screened for pets, rugs, and stairs, with
unmapped bathrooms), the localization scheme (2D static map, ROS navigation
stack, and a reset at a known docking pose, which still left 455
lost-localization events), the dependence on home internet (the orchestrator,
speech services, and MLS run in the cloud), and the human side (diagnosis
relied on researchers or briefed contractors inspecting the MLS). The paper
gives no drive type, size, or speed for the robot, and it names the onboard
computers (an on-board computer and an NVIDIA Jetson TX2, Fig. 3) without
saying what runs on them, so kinematic and compute transfer cannot be
assessed from it. The visual docking depended on light: it failed in a dark
house (p. 11), and the docking-station light listed as a fix was not deployed
(p. 16). The success rates also depend on the IoT user-location network and
on the participants. For a small research platform, the transferable parts
are the supervision design (an MQTT status stream from every component, an
event database with periodic snapshots, and a replay timeline) and the
recovery rules of Table A.2, such as multiple docking attempts after
timeouts, a keepalive connectivity check, shutdown at critical battery level,
and localization reinitialization at the docking station (p. 16).

## Code and data

The anonymized data are available on request from the corresponding author
and are not public because they could compromise participant privacy; the
code is available upon request (p. 15). No public repository is named. Not
verified elsewhere.

## Version family

A preliminary version, Luperto et al., "What is my robot doing? Remote
supervision to support robots for older adults independent living: a field
study", ECMR 2021 (reference [10]), describes the MLS; this article adds a
substantially improved evaluation, discussion, and lessons learned (p. 2).
The robot setup and the first prepilot are described in [33] (ECMR 2019), and
the system functionalities in [9,11]. The ECMR versions are not separate
entries in 01-papers/INDEX.md; the library counts this work once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Sec. 7.5, p. 14 | "Specifically, these were regions with dynamic features (objects or furniture that was frequently moved) or parts of the maps that were very similar to others." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | direct-support | strong | Sec. 7.2, p. 13 | "These findings highlight the importance of not only developing the intended tasks of the system but also explicitly modelling for unexpected events and carefully devising robust recovery behaviours." |
| C6 | qualifies | moderate | Sec. 6.1, p. 8 | "To provide well-suited conditions for robot navigation, the apartments had to satisfy some selection criteria too." |

## Page-cited excerpts

- **p. 6, Sec. 4.** "Due to all of this, the MLS allowed us to remotely handle most of the issues that arose during the pilot experimental campaign, effectively reducing the number of maintenance interventions on site."
  The main claim for remote supervision; no count of remote versus on-site interventions is reported.
- **p. 9, Sec. 6.2.** "Another trend emerging from the stats is that the robots were idle at the docking station most of the time, 97.98% on average."
  Motion is a small share of deployment time, so robustness during idle time matters for long-term autonomy.
- **p. 9, Sec. 6.2.** "Note that, as we do not have the exact localisation of the robot, we rely on and plot the estimated position made available by the robot itself."
  Trajectories and lost-localization counts are self-reported; there is no ground truth.
- **p. 11, Sec. 6.2.2.** "Overall, robots performance was satisfactory, as they were able to carry out the assigned intervention successfully in 86.46% of the cases (Success Rate in Table 3)."
  The rate counts successful over attempted (successful plus failed) SQ, WM, and REM interventions; interventions not performed are excluded.
- **p. 13, Sec. 7.1.** "We did not perform any additional reasoning or pattern analysis, but only provided an interface for logged data."
  The MLS is a logging and replay interface for human operators, not an automatic fault detector.
- **p. 13, Sec. 7.2.** "Interestingly, we noted that most of the critical problems reported by the users were related precisely to such unexpected events."
  Supports designing for idle-time events; the statement is qualitative, without a count of reports.
- **p. 13, Sec. 7.2.** "This issue was particularly critical (leading to the only drop-out from the study) as it was not under our control and, consequently, not fixable."
  Home internet is an external dependency of the cloud-based architecture.
- **p. 14, Sec. 7.5.** "Although the location is clearly identifiable, the actual specific reasons for the lost localisation are not ascertained."
  The link between dynamic furniture or map aliasing and lost localization is a hypothesis, not a measured cause.
- **p. 14, Sec. 7.6.** "In general, if the intervention has to fail, it is better for it to fail quickly."
  A design lesson for recovery behavior; the proposed timeout rule was not evaluated.
- **p. 16, Table A.2.** "Items signalled implemented and tested but not deployed during pilot for safety reasons during the COVID-19 pandemic, as they were designed as later improvements for the last part of the pilot."
  Two listed fixes were not part of the evaluated pilot.

## Survey-usable statements

### Supported

- In a closed-loop field deployment of 10 Giraff-X robots in older adults' apartments over two rounds in 2019 and 2020, 86.46% of attempted SQ, WM, and REM interventions succeeded, and the user search succeeded in 75.95% of cases.
- Over 13883.42 m of autonomous travel the robots reported 455 lost-localization events despite a localization reset at the docking station, so long-term home navigation needs localization recovery beyond a docking reset.
- The robots spent 97.98% of the time idle at the dock, and the authors report that most critical user-reported problems arose from unexpected events during idle time.
- A cloud logging and replay system let operators explain anomalies to users and fix issues remotely, including during the COVID-19 lockdown; the evidence is a set of case studies.

### Not supported

- Remote supervision measurably increased acceptance or reliability: no deployment without the MLS was run, and acceptance comes from a post-pilot questionnaire of 10 users.
- The MLS detects faults automatically: it provides an interface for logged data, and online anomaly detection is future work.
- Dynamic furniture or map aliasing caused the lost localization: the authors state that the specific reasons were not ascertained, and no ground truth was recorded.
- The robots navigated collision-free under a defined metric: the absence of damage and user collisions is reported as an observation without a counting protocol.
- The results hold for unscreened homes or other robots: apartments without pets, rugs, or stairs were selected, the robot's drive type is not reported, and the paper does not say what runs on the onboard computers.
- The pilot measured robustness to darkness, sensor faults, or connectivity loss: these conditions occurred in the field, but no results are reported per condition.

## Verification log

- 2026-10-26 | host: Kiro | scope: full text read (Secs. 1-8, data statement, Appendix Tables A.1-A.2); Tables 1, 3, 4 and Figs. 9-15 captions checked against PDF pages 3 and 9-16 | corrections: abstract replaced (legacy used the journal highlights); rebuilt in template format with vocabulary coding; navigation assistant moved from self-management to navigation; COVID-19 deployment limitation reworded from the Table A.2 footnote; C2 lowered to partial-support; count inconsistencies (130 vs 132 weeks, Table 1 users, 72.42% vs 73.42%) recorded (details in 06-data/review-corrections.csv)
- 2026-10-26 | host: Kiro | scope: revision after an independent fact-check; Table 3 and Figs. 11-12 read from the rendered PDF page 10; Fig. 3 read from the figure image (PDF page 4); Table A.2 checked against the PDF text of page 16; Secs. 6.2-6.3 and 7.2-7.5 rechecked for field conditions | corrections: platform_class changed to wheeled-unspecified (Fig. 3 label, no drive type); degradation recoded to none, with field conditions in degradation_observed; Fig. 12 shares restated as shares of all 1151 interactions; misplaced Table 3 ITA and ESP distance means and the Fig. 11 percentage noted; "attempted" used throughout; onboard computers and sensors named from Fig. 3; compute_location qualified; American spelling in review prose
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

In an ageing society, the at-home use of Socially Assistive Robots (SARs) could provide remote monitoring of their users’ well-being, together with physical and psychological support. However, private home environments are particularly challenging for SARs, due to their unstructured and dynamic nature which often contributes to robots’ failures. For this reason, even though several prototypes of SARs for elderly care have been developed, their commercialisation and wide-spread at-home use are yet to be effective. In this paper, we analyse how including the end users’ feedback impacts the SARs reliability and acceptance. To do so, we introduce a Monitoring and Logging System (MLS) for remote supervision, which increases the explainability of SAR-based systems deployed in older adults’ apartments, while also allowing the exchange of feedback between caregivers, technicians, and older adults. We then present an extensive field study showing how long-term deployment of autonomous SARs can be accomplished by relying on such a feedback loop to address any potential issue. To this end, we provide the results obtained in a 130-week long study where autonomous SARs were deployed in the apartments of 10 older adults, with the aim of possibly serving and assisting future practitioners, with the knowledge collected from this extensive experimental campaign, to fill the gap that currently exists for the widespread adoption of SARs.
