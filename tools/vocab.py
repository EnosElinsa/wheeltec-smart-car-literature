"""Allowed values for review coding (mirror of 06-data/vocabulary.md).

``tools/tests/test_vocab.py`` checks that every value listed here also appears
in ``06-data/vocabulary.md``, so the two definitions cannot drift apart.
"""

from __future__ import annotations

MODULES = [
    "localization-mapping",
    "traversability-planning-control",
    "semantic-language-navigation",
    "multi-robot",
    "fault-recovery-deployment",
]
EVIDENCE = [
    "closed-loop-hardware",
    "online-hardware",
    "recorded-robot-data",
    "dataset-playback",
    "simulation",
    "numerical",
    "theory-only",
    "survey",
    "dataset-resource",
]
CAVEATS = [
    "teleoperated-mapping",
    "joystick-driving",
    "pushed-capture",
    "video-only-hardware",
    "motion-capture-pose",
    "external-pose-source",
    "offboard-compute",
    "cloud-model",
    "speed-capped",
    "scripted-scenario",
    "few-trials",
    "simulated-agents-on-hardware",
]
PLATFORMS = [
    "differential-drive",
    "skid-steer",
    "ackermann",
    "omnidirectional",
    "wheeled-unspecified",
    "tracked",
    "legged",
    "aerial",
    "aquatic",
    "road-vehicle",
    "handheld",
    "mixed",
    "none",
]
WHEELED = {"differential-drive", "skid-steer", "ackermann", "omnidirectional", "wheeled-unspecified"}
DEGRADATIONS = [
    "visual-degradation",
    "lidar-degeneracy",
    "gnss-denial",
    "dynamic-objects",
    "scene-change",
    "terrain",
    "wheel-slip",
    "actuator-fault",
    "sensor-fault",
    "data-association-fault",
    "communication-delay-loss",
    "communication-partition",
    "bandwidth-limit",
    "compute-limit",
    "model-error",
    "energy-limit",
]
EVALUATION = ["residual", "closed-loop-task", "designed-degradation", "integrity-reliability"]
COMPUTE_LOCATIONS = [
    "onboard",
    "offboard-local",
    "desktop-offline",
    "cloud",
    "mixed",
    "not-reported",
    "not-applicable",
]
INCLUDED = ["yes", "context", "no"]
VERIFICATION_LEVELS = ["full", "light"]
YES_NO = ["yes", "no"]
RELATIONS = ["direct-support", "partial-support", "qualifies", "contradicts", "unset"]
STRENGTHS = ["strong", "moderate", "weak", "n/a"]
CLAIMS = ["C1", "C2", "C3", "C4", "C5", "C6"]

# Field name -> (allowed values, multi-valued, "none" allowed)
CODING_FIELDS: dict[str, tuple[list[str] | None, bool, bool]] = {
    "survey_module": (MODULES, False, False),
    "secondary_modules": (MODULES, True, True),
    "evidence_type": (EVIDENCE, False, False),
    "evidence_all": (EVIDENCE, True, False),
    "protocol_caveats": (CAVEATS, True, True),
    "platform_class": (PLATFORMS, False, False),
    "platform": (None, False, False),
    "boundary_platform": (YES_NO, False, False),
    "degradation": (DEGRADATIONS, True, True),
    "degradation_observed": (DEGRADATIONS, True, True),
    "evaluation_primary": (EVALUATION, False, False),
    "evaluation_all": (EVALUATION, True, False),
    "sensors": (None, False, False),
    "compute": (None, False, False),
    "compute_location": (COMPUTE_LOCATIONS, False, False),
    "summary_result": (None, False, False),
    "summary_limitation": (None, False, False),
    "survey_included": (INCLUDED, False, False),
    "verification_level": (VERIFICATION_LEVELS, False, False),
}

ALL_CONTROLLED_VALUES = sorted(
    {
        v
        for values in (
            MODULES, EVIDENCE, CAVEATS, PLATFORMS, DEGRADATIONS, EVALUATION,
            COMPUTE_LOCATIONS, RELATIONS, VERIFICATION_LEVELS,
        )
        for v in values
    }
)
