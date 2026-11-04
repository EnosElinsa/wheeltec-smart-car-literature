"""Draw the manuscript figures as SVG sources and convert them to vector PDF.

Outputs ``figures/<name>.svg`` (editable source) and ``figures/<name>.pdf``
(included by LaTeX). The corpus figure reads ``generated/corpus-year-module.json``
written by ``scripts/build_data.py``. All figures are grayscale line drawings
set in Times, so they print and photocopy without loss.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import csv

from project_paths import literature_root
from svgkit import FILL, FILL_LIGHT, GRAYS, HAIR, INK, MUTED, RULE, WHITE, Canvas, svg_to_pdf, width, wrap

M = Path(__file__).resolve().parents[1]
OUT = M / 'figures'
OUT.mkdir(exist_ok=True)

CHALLENGES = [
    ('1', 'Localization-triggered recovery'),
    ('2', 'Semantic reasoning with fallback'),
    ('3', 'Pose uncertainty in terrain decisions'),
    ('4', 'Reconnection and shared-state acceptance'),
]


# ---------------------------------------------------------------------------
# Fig. 1: taxonomy of responses to degradation
# ---------------------------------------------------------------------------
TAXONOMY = [
    ('IV', 'Localization and mapping', [
        ('Selective updates and conditioning', 'LODESTAR, Switch-SLAM, DR-ICP, DCReg'),
        ('Complementary sensing', 'LiDAR-radar-inertial fusion, Super4DR, RaLI-Multi, LiDAR-teach/radar-repeat'),
        ('Motion priors and contact', 'SE2-LIO, WING, ToF-wheel odometry, DURAL'),
        ('Map revision and relocalization', 'ELite, Chamelion, NeuSE, CMRNext, OMCL'),
    ]),
    ('V', 'Traversability, planning, and control', [
        ('Terrain cost and risk', 'CADNet, SPARTA, terrain-adaptive MPC, TRAIL'),
        ('Information-aware exploration', 'FIT-SLAM 2, LRAE, SLAM-aware graph planning'),
        ('Prediction and learned policies', 'SCOPE, HEIGHT, prescient MPC, homotopy MPC'),
        ('Safety constraints and risk bounds', 'Safe Horizon MPC, MonoMPC, Perceive With Confidence'),
    ]),
    ('VI', 'Semantic and language-guided navigation', [
        ('Semantic scene memory', 'HOV-SG, OpenIN, osmAG-LLM, VLN-Game'),
        ('Geographic grounding and learned actions', 'OPEN, CAUSALNAV, LeLaN, Uni-NaVid'),
        ('Candidate selection and embodiment filters', 'VL-TGS, Sem-NaVAE, VAMOS'),
        ('Social and behavioral constraints', 'GSON, NORM-Nav, OLiVia-Nav, SocialNav-SUB'),
    ]),
    ('VII', 'Multi-robot coordination', [
        ('Allocation and spatial responsibility', 'CURE, URGE, TAPM-IVP'),
        ('Compact sharing under bandwidth limits', 'MR-TopoMap, bandwidth-efficient C-SLAM, layered transmission'),
        ('Distributed estimation', 'iMESA, riMESA, Multi-Proxy, Swarm-SLAM'),
        ('Rendezvous and reconnection', 'CoCoPlan, MEF-Explore, correlation-aware map repair'),
    ]),
    ('VIII', 'Fault tolerance, recovery, and deployment', [
        ('Diagnosis and tolerant control', 'Set-based LPV diagnosis, kinematic residuals, prescribed-performance control'),
        ('Integrity and runtime monitoring', 'Reliable MCL, EKF-SLAM integrity, Sentinel, RADIUM'),
        ('Executed recovery', 'GP-based recovery, RTEB, CARE, active view planning'),
        ('Resources and sustained service', 'Energy co-management, persistent charging, cloud-edge offloading, LiReN'),
    ]),
]


# Corpus codes of the Fig. 1 examples; examples whose coding sets boundary_platform get a dagger.
EXAMPLE_CODES = {
 'LODESTAR': 'E01', 'Switch-SLAM': 'F04', 'DR-ICP': 'S24', 'DCReg': 'S37', 'LiDAR-radar-inertial fusion': 'E09',
 'Super4DR': 'R12', 'RaLI-Multi': 'R02', 'LiDAR-teach/radar-repeat': 'R11', 'SE2-LIO': 'N02', 'WING': 'R04',
 'ToF-wheel odometry': 'E02', 'DURAL': 'E03', 'ELite': 'E18', 'Chamelion': 'R07', 'NeuSE': 'S34', 'CMRNext': 'R06',
 'OMCL': 'R10', 'CADNet': 'M29', 'SPARTA': 'S45', 'terrain-adaptive MPC': 'R13', 'TRAIL': 'R15', 'FIT-SLAM 2': 'E13',
 'LRAE': 'M14', 'SLAM-aware graph planning': 'N05', 'SCOPE': 'R18', 'HEIGHT': 'R16', 'prescient MPC': 'M30',
 'homotopy MPC': 'S09', 'Safe Horizon MPC': 'E25', 'MonoMPC': 'R14', 'Perceive With Confidence': 'F08',
 'HOV-SG': 'E48', 'OpenIN': 'E44', 'osmAG-LLM': 'R27', 'VLN-Game': 'R28', 'OPEN': 'M10', 'CAUSALNAV': 'E45',
 'LeLaN': 'E50', 'Uni-NaVid': 'E49', 'VL-TGS': 'F05', 'Sem-NaVAE': 'R25', 'VAMOS': 'R26', 'GSON': 'F06',
 'NORM-Nav': 'R30', 'OLiVia-Nav': 'R29', 'SocialNav-SUB': 'S44', 'CURE': 'M17', 'URGE': 'R22', 'TAPM-IVP': 'F09',
 'MR-TopoMap': 'M36', 'bandwidth-efficient C-SLAM': 'S29', 'layered transmission': 'R21', 'iMESA': 'E40',
 'riMESA': 'R23', 'Multi-Proxy': 'R20', 'Swarm-SLAM': 'S10', 'CoCoPlan': 'R19', 'MEF-Explore': 'R24',
 'correlation-aware map repair': 'F03', 'Set-based LPV diagnosis': 'N16', 'kinematic residuals': 'E51',
 'prescribed-performance control': 'M15', 'Reliable MCL': 'M35', 'EKF-SLAM integrity': 'X07', 'Sentinel': 'F07',
 'RADIUM': 'R36', 'GP-based recovery': 'E59', 'RTEB': 'S16', 'CARE': 'S47', 'active view planning': 'R33',
 'Energy co-management': 'R32', 'persistent charging': 'E58', 'cloud-edge offloading': 'R31', 'LiReN': 'S41',
}


def boundary_codes() -> set[str]:
    path = literature_root(M) / '06-data/corpus-comparison.csv'
    return {r['code'] for r in csv.DictReader(path.open(encoding='utf-8-sig')) if r['boundary_platform'] == 'yes'}


def mark_boundary(methods: str, boundary: set[str]) -> str:
    names = methods.split(', ')
    assert all(n in EXAMPLE_CODES for n in names), [n for n in names if n not in EXAMPLE_CODES]
    return ', '.join(n + ('\u2020' if EXAMPLE_CODES[n] in boundary else '') for n in names)


def fig_taxonomy() -> Canvas:
    W, margin, gap = 516.0, 0.5, 6.0
    cw = (W - 2 * margin - 4 * gap) / 5
    indent, pad = 8.0, 3.4
    box_w = cw - indent
    c = Canvas(W, 10)

    heads = [wrap(f'{sec}. {title}', cw - 8, 7.4, 'bold') for sec, title, _ in TAXONOMY]
    head_h = max(len(h) for h in heads) * 8.8 + 6.5
    cells = []
    boundary = boundary_codes()
    for _, _, mechs in TAXONOMY:
        col = []
        for name, methods in mechs:
            n = wrap(name, box_w - 2 * pad, 7.0)
            m = wrap(mark_boundary(methods, boundary), box_w - 2 * pad, 6.3, style='italic')
            col.append((n, m, len(n) * 8.2 + len(m) * 7.3 + 5.2))
        cells.append(col)
    row_h = [max(cells[k][r][2] for k in range(5)) for r in range(4)]

    title = 'Responses to degradation in wheeled navigation'
    root_w, root_h, root_y = width(title, 8.2, 'bold') + 26, 16.0, 0.5
    c.rect((W - root_w) / 2, root_y, root_w, root_h, fill=FILL, stroke=INK, sw=0.7)
    c.text(W / 2, root_y + 11.2, title, 8.2, 'bold', anchor='middle')
    xs = [margin + k * (cw + gap) for k in range(5)]
    bus_y = root_y + root_h + 6
    head_y = bus_y + 6
    c.polyline([(W / 2, root_y + root_h), (W / 2, bus_y)], sw=0.6)
    c.polyline([(xs[0] + cw / 2, bus_y), (xs[4] + cw / 2, bus_y)], sw=0.6)

    y = head_y
    for k in range(5):
        x = xs[k]
        c.polyline([(x + cw / 2, bus_y), (x + cw / 2, head_y)], sw=0.6)
        c.rect(x, head_y, cw, head_h, fill=FILL, stroke=INK, sw=0.7)
        c.lines(x + 4, head_y + 10.2, heads[k], 7.4, 8.8, weight='bold')
        spine_x = x + 4.0
        y = head_y + head_h + 5
        last_mid = y
        for r, (n, m, _) in enumerate(cells[k]):
            bx = x + indent
            c.rect(bx, y, box_w, row_h[r], fill=WHITE, stroke=RULE, sw=0.5)
            mid = y + 6.5
            c.polyline([(spine_x, mid), (bx, mid)], stroke=RULE, sw=0.5)
            last_mid = mid
            yy = c.lines(bx + pad, y + 8.4, n, 7.0, 8.2)
            c.lines(bx + pad, yy + 0.2, m, 6.3, 7.3, style='italic', fill=MUTED)
            y += row_h[r] + 3.5
        c.polyline([(spine_x, head_y + head_h), (spine_x, last_mid)], stroke=RULE, sw=0.5)
    body_bottom = y

    # Evaluation axes (Section IX) and open interfaces (Section X).
    band_y, band_h = body_bottom + 6, 49.0
    # The right box is sized to its two label columns; the left box takes the rest.
    col1 = max(width(CHALLENGES[i][1], 7.0) for i in (0, 2)) + 22
    col2 = max(width(CHALLENGES[i][1], 7.0) for i in (1, 3)) + 16
    rw = col1 + col2 + 8
    left_w = W - 2 * margin - gap - rw
    c.rect(margin, band_y, left_w, band_h, fill=WHITE, stroke=INK, sw=0.7)
    c.text(margin + 5, band_y + 10, 'IX. Evaluation practice', 7.4, 'bold')
    c.polyline([(margin + 5, band_y + 14), (margin + left_w - 5, band_y + 14)], stroke=HAIR, sw=0.4)
    axes = [('Measurement level', 'component error vs. task outcome'),
            ('Test conditions', 'onset, severity, duration'),
            ('Risk and diagnostic claims', 'event, calibration, assumptions')]
    for i, (name, sub) in enumerate(axes):
        ay = band_y + 24.5 + i * 9.4
        c.text(margin + 5, ay, name + ':', 7.0)
        c.text(margin + 9 + width(name + ':', 7.0), ay, sub, 6.6, style='italic', fill=MUTED)
    rx0 = margin + left_w + gap
    c.rect(rx0, band_y, rw, band_h, fill=WHITE, stroke=INK, sw=0.7)
    c.text(rx0 + 5, band_y + 10, 'X. Open interfaces between functions', 7.4, 'bold')
    c.polyline([(rx0 + 5, band_y + 14), (rx0 + rw - 5, band_y + 14)], stroke=HAIR, sw=0.4)
    for i, (num, label) in enumerate(CHALLENGES):
        px = rx0 + 5 + (i % 2) * col1
        py = band_y + 27 + (i // 2) * 12.5
        c.marker(px + 4.6, py - 2.4, num)
        c.text(px + 12.5, py, label, 7.0)
    c.h = band_y + band_h + 0.5
    return c


# ---------------------------------------------------------------------------
# Fig. 2: navigation stack, degradation entry points, and open interfaces
# ---------------------------------------------------------------------------
def box(c, x, y, w, h, sec, title, sub, fill=WHITE):
    c.rect(x, y, w, h, fill=fill, stroke=INK, sw=0.7)
    c.text(x + 4, y + 10, title, 7.2, 'bold')
    c.polyline([(x + 4, y + 13.5), (x + w - 4, y + 13.5)], stroke=HAIR, sw=0.4)
    c.lines(x + 4, y + 22, sub, 6.6, 7.6)
    if sec:
        c.text(x + w - 4, y + h - 3.6, f'Sec. {sec}', 6.2, style='italic', anchor='end', fill=MUTED)


def source_tag(c, x, y, title, detail, align='left'):
    w = max(width(title, 6.8, 'bold'), width(detail, 6.2, style='italic')) + 10
    if align == 'right':
        x = x - w
    c.rect(x, y, w, 21, fill=FILL_LIGHT, stroke=INK, sw=0.6, dash=(2.2, 1.4))
    c.text(x + 5, y + 9, title, 6.8, 'bold')
    c.text(x + 5, y + 17.2, detail, 6.2, style='italic', fill=MUTED)
    return x, w


def fig_stack() -> Canvas:
    W = 516.0
    c = Canvas(W, 10)
    bw, bh = 86.0, 46.0
    gap = (W - 8 - 5 * bw) / 4
    xs = [4 + k * (bw + gap) for k in range(5)]
    my = 94.0
    specs = [(None, 'Measurements', ['Cameras, LiDAR, radar,', 'IMU, wheels, GNSS, UWB']),
             ('IV', 'State estimation', ['Pose, covariance,', 'validity, measurement age']),
             ('IV', 'Representation', ['Geometry, terrain,', 'semantics, persistence']),
             ('V', 'Planning', ['Route, trajectory,', 'risk and feasibility']),
             ('V', 'Control', ['Feasible wheel commands', 'under actuator limits'])]
    for x, (sec, title, sub) in zip(xs, specs):
        box(c, x, my, bw, bh, sec, title, sub)
    flow_y = my + 27
    for k in range(4):
        c.arrow([(xs[k] + bw, flow_y), (xs[k + 1], flow_y)], sw=0.9, head=4.2)

    # Upper row: information from teammates and from task interpretation.
    ty, th = 28.0, 42.0
    box(c, xs[2], ty, bw, th, 'VII', 'Teammates', ['Shared maps, poses,', 'allocations'], fill=FILL_LIGHT)
    box(c, xs[3], ty, bw, th, 'VI', 'Task interpretation', ['Goals, language,', 'social preferences'], fill=FILL_LIGHT)
    tm_x, ti_x = xs[2] + bw / 2, xs[3] + bw / 2
    c.arrow([(tm_x, ty + th), (tm_x, my)], dash=(2.6, 1.6), sw=0.7, both=True, head=3.6)
    c.arrow([(ti_x, ty + th), (ti_x, my)], dash=(2.6, 1.6), sw=0.7, head=3.6)

    # Supervision row.
    sy, sh = my + bh + 22, 27.0
    sx0, sx1 = xs[1], xs[4] + bw
    c.rect(sx0, sy, sx1 - sx0, sh, fill=FILL, stroke=INK, sw=0.7)
    c.polyline([(sx0 + 112, sy), (sx0 + 112, sy + sh)], stroke=INK, sw=0.5)
    c.text(sx0 + 5, sy + 11, 'Supervision and recovery', 7.2, 'bold')
    c.text(sx0 + 5, sy + 21, 'Sec. VIII', 6.2, style='italic', fill=MUTED)
    c.text(sx0 + 120, sy + 11.5, 'Monitor assumptions and integrity, request information,', 6.6)
    c.text(sx0 + 120, sy + 20.5, 'slow, stop, reinitialize, replan, reassign, or escalate', 6.6)
    est_x = xs[1] + bw / 2
    c.arrow([(est_x, my + bh), (est_x, sy)], dash=(2.6, 1.6), sw=0.7, head=3.6)
    for x in (xs[3] + bw / 2, xs[4] + bw / 2):
        c.arrow([(x, sy), (x, my + bh)], dash=(2.6, 1.6), sw=0.7, head=3.6)

    # Physical feedback loop.
    ly = sy + sh + 11
    c.arrow([(xs[4] + bw, flow_y), (W - 1.5, flow_y), (W - 1.5, ly), (xs[0] + bw / 2, ly), (xs[0] + bw / 2, my + bh)],
            sw=0.9, head=4.2)
    label = 'Executed motion changes the next observations'
    lw = width(label, 6.6, style='italic') + 10
    c.rect(W / 2 - lw / 2, ly - 5, lw, 10, fill=WHITE)
    c.text(W / 2, ly + 2.2, label, 6.6, style='italic', anchor='middle', fill=MUTED)

    # Degradation sources and their entry points.
    sx, sw_ = source_tag(c, 4, 58, 'Sensing and estimation', 'texture, geometry, bias, association')
    c.arrow([(xs[0] + bw / 2, 79), (xs[0] + bw / 2, my)], stroke=RULE, sw=0.6, head=3.4)
    c.arrow([(sx + sw_, 68.5), (xs[1] + 22, 68.5), (xs[1] + 22, my)], stroke=RULE, sw=0.6, head=3.4)
    ex, ew = source_tag(c, 4, 28, 'Environment and map change', 'moving agents, aged or moved structure')
    c.arrow([(ex + ew, 38.5), (xs[2] - 6, 38.5), (xs[2] - 6, my + 7), (xs[2], my + 7)], stroke=RULE, sw=0.6, head=3.4)
    cx_, cw_ = source_tag(c, W - 4, 2, 'Communication and computation', 'loss, delay, deadlines, memory', align='right')
    drop_t, drop_m = xs[3] + bw - 16, xs[2] + bw - 16
    c.polyline([(cx_, 12.5), (drop_m, 12.5)], stroke=RULE, sw=0.6)
    c.arrow([(drop_t, 12.5), (drop_t, ty)], stroke=RULE, sw=0.6, head=3.4)
    c.arrow([(drop_m, 12.5), (drop_m, ty)], stroke=RULE, sw=0.6, head=3.4)
    source_tag(c, W - 4, 56, 'Terrain and mobility', 'slope, slip, material, actuation', align='right')
    c.arrow([(xs[4] + bw / 2, 77), (xs[4] + bw / 2, my)], stroke=RULE, sw=0.6, head=3.4)

    # Open interfaces of Section X.
    c.marker(est_x + 10, (my + bh + sy) / 2, '1')
    c.marker(ti_x + 10, (ty + th + my) / 2, '2')
    c.marker((xs[2] + bw + xs[3]) / 2, flow_y - 10, '3')
    c.marker(tm_x + 10, (ty + th + my) / 2, '4')

    # Legend.
    gy = ly + 20
    x = 4.0
    items = ['Information flow', 'Exchange or supervision', 'Degradation source and entry point',
             'Open interface examined in Sec. X (numbering as in Fig. 1)']
    c.arrow([(x, gy - 2.4), (x + 22, gy - 2.4)], sw=0.9, head=4.2)
    c.text(x + 26, gy, items[0], 6.6, fill=MUTED)
    x += 26 + width(items[0], 6.6) + 14
    c.arrow([(x, gy - 2.4), (x + 22, gy - 2.4)], sw=0.7, dash=(2.6, 1.6), head=3.6)
    c.text(x + 26, gy, items[1], 6.6, fill=MUTED)
    x += 26 + width(items[1], 6.6) + 14
    c.rect(x, gy - 7, 10, 9, fill=FILL_LIGHT, stroke=INK, sw=0.6, dash=(2.2, 1.4))
    c.arrow([(x + 11, gy - 2.4), (x + 25, gy - 2.4)], stroke=RULE, sw=0.6, head=3.4)
    c.text(x + 29, gy, items[2], 6.6, fill=MUTED)
    x += 29 + width(items[2], 6.6) + 14
    c.marker(x + 4.6, gy - 2.4, '1')
    c.text(x + 12.5, gy, items[3], 6.6, fill=MUTED)
    c.h = gy + 4
    return c


# ---------------------------------------------------------------------------
# Fig. 3: joint evaluation of detection and response in one episode
# ---------------------------------------------------------------------------
def fig_evaluation() -> Canvas:
    W = 516.0
    c = Canvas(W, 10)
    x0, x1 = 112.0, 510.0
    t_on, t_det, t_act, t_reloc, t_rec, t_off = 212.0, 262.0, 292.0, 342.0, 394.0, 368.0
    lanes = [('Operating condition', 'test conditions', 30),
             ('Internal signals', 'component and diagnostic measures', 50),
             ('Executed response', 'response mechanism', 28),
             ('Task outcome', 'task measures', 40)]
    top = 2.0
    tops, y = [], top
    for _, _, h in lanes:
        tops.append((y, h))
        y += h
    bottom = y
    # Degraded interval shaded across all lanes.
    c.rect(t_on, top, t_off - t_on, bottom - top, fill='#ECECEC')
    for (title, tag, _), (yy, h) in zip(lanes, tops):
        c.text(6, yy + h / 2 - 0.5, title, 7.2, 'bold')
        c.text(6, yy + h / 2 + 8, tag, 6.4, style='italic', fill=MUTED)
    for (yy, h) in tops[1:]:
        c.polyline([(4, yy), (W - 4, yy)], stroke=HAIR, sw=0.4)
    c.polyline([(4, top), (W - 4, top)], sw=0.8)
    c.polyline([(4, bottom), (W - 4, bottom)], sw=0.8)
    axis_y = bottom + 8
    events = [(t_on, 'onset'), (t_det, 'alarm'), (t_act, 'action'), (t_rec, 'recovered')]
    for t, _ in events:
        c.polyline([(t, top + 1), (t, axis_y)], stroke=RULE, sw=0.45, dash=(1.2, 1.4))

    # Lane 1: operating condition.
    yy, h = tops[0]
    c.text((t_on + t_off) / 2, yy + h / 2 + 2.3, 'degraded interval: source, severity, duration', 6.6,
           style='italic', anchor='middle')
    c.text(x0 + 5, yy + h / 2 + 2.3, 'nominal', 6.6, style='italic', fill=MUTED)
    c.text((t_rec + x1) / 2, yy + h / 2 + 2.3, 'nominal', 6.6, style='italic', anchor='middle', fill=MUTED)

    # Lane 2: monitor statistic (crosses the threshold at the alarm) and pose error.
    yy, h = tops[1]
    base = yy + h - 8
    thr = base - 23
    tau = (t_det - t_on) / math.log(34 / (34 - 18))

    def curve(f, step=1.5):
        pts, t = [], x0
        while t <= x1 + 0.01:
            pts.append((t, f(t)))
            t += step
        return pts

    def stat(t):
        bump = 21.0 * math.exp(-((t - 174) / 5) ** 2)
        if t < t_on:
            return base - 5 - bump
        rise = lambda s: 34 * (1 - math.exp(-(s - t_on) / tau))
        if t < t_reloc:
            return base - 5 - rise(t)
        return base - 5 - rise(t_reloc) * math.exp(-(t - t_reloc) / 10)

    def err(t):
        if t < t_on:
            return base - 1.5
        rise = lambda s: 17 * (1 - math.exp(-(s - t_on) / 45))
        if t < t_reloc:
            return base - 1.5 - rise(t)
        return base - 1.5 - rise(t_reloc) * math.exp(-(t - t_reloc) / 14)

    c.polyline([(x0, thr), (x1, thr)], stroke=RULE, sw=0.6, dash=(3.2, 1.8))
    c.text(x1 - 2, thr - 2.6, 'alarm threshold', 6.4, style='italic', anchor='end', fill=MUTED)
    c.polyline(curve(err), stroke=INK, sw=0.8, dash=(2.4, 1.5))
    c.polyline(curve(stat), stroke=INK, sw=0.9)
    c.text(x0 + 4, base - 8, 'monitor statistic', 6.4, style='italic')
    c.text(x1 - 2, base + 6, 'pose error against the reference', 6.4, style='italic', anchor='end')
    c.polygon([(t_det, thr - 1), (t_det - 3.2, thr - 6.6), (t_det + 3.2, thr - 6.6)], fill=INK)
    fa = base - 5 - 21.0
    c.polygon([(174, fa - 1.5), (170.8, fa - 7.1), (177.2, fa - 7.1)], fill=WHITE, stroke=INK, sw=0.6)
    c.text(174, fa - 9.6, 'false alarm', 6.4, style='italic', anchor='middle')

    # Lane 3: executed actions.
    yy, h = tops[2]
    segs = [(x0, t_act, 'nominal plan', WHITE), (t_act, t_reloc, 'slow and stop', FILL),
            (t_reloc, t_rec, 'relocalize', FILL), (t_rec, x1, 'resume task', WHITE)]
    for a, b, label, fill in segs:
        c.rect(a + 0.8, yy + 6, b - a - 1.6, h - 12, fill=fill, stroke=INK, sw=0.5)
        c.text((a + b) / 2, yy + h / 2 + 2.3, label, 6.8, anchor='middle')

    # Lane 4: task progress.
    yy, h = tops[3]
    lo, hi = yy + h - 6, yy + 8
    rate = (lo - hi) / (x1 - x0) * 1.3

    def prog(t):
        if t < t_act:
            return lo - (t - x0) * rate
        if t < t_rec:
            return lo - (t_act - x0) * rate - (t - t_act) * rate * 0.05
        return max(lo - (t_act - x0) * rate - (t_rec - t_act) * rate * 0.05 - (t - t_rec) * rate, hi)
    c.polyline(curve(prog), stroke=INK, sw=0.9)
    c.text(x0 + 4, hi + 2, 'progress toward the goal', 6.4, style='italic')
    c.text(x1 - 2, lo - 1, 'completion, contacts, interventions, time', 6.4, style='italic', anchor='end', fill=MUTED)

    # Time axis and derived intervals.
    c.arrow([(x0, axis_y), (x1, axis_y)], sw=0.6, head=3.6)
    c.text(x1, axis_y + 9.5, 'time', 6.6, style='italic', anchor='end', fill=MUTED)
    for t, name in events:
        c.polyline([(t, axis_y - 2), (t, axis_y + 2)], sw=0.6)
        c.text(t, axis_y + 9.5, name, 6.6, anchor='middle')
    spans = [(t_on, t_det, 'detection delay', 19), (t_det, t_act, 'response delay', 28),
             (t_on, t_rec, 'recovery time', 37)]
    for a, b, label, dy in spans:
        yb = axis_y + dy - 3
        c.arrow([(a, yb), (b, yb)], stroke=MUTED, sw=0.5, head=2.8, both=True)
        c.text(b + 4, yb + 2.2, label, 6.4, style='italic', fill=MUTED)
    c.text(6, axis_y + 9.5, 'Report per episode', 6.8, 'bold')
    c.lines(6, axis_y + 18.5, ['trial unit, reference source,', 'alarms, actions, censoring'], 6.4, 7.6,
            style='italic', fill=MUTED)
    c.h = axis_y + 42
    return c


# ---------------------------------------------------------------------------
# Fig. S1: corpus by year and principal function
# ---------------------------------------------------------------------------
def fig_corpus() -> Canvas:
    data = json.loads((M / 'generated/corpus-year-module.json').read_text(encoding='utf-8'))
    years, modules, counts, labels = data['years'], data['modules'], data['counts'], data['labels']
    W, H = 252.0, 150.0
    c = Canvas(W, H)
    left, right, top, bottom = 24.0, 4.0, 14.0, 16.0
    totals = [sum(counts[m][i] for m in modules) for i in range(len(years))]
    ymax = ((max(totals) + 9) // 10) * 10
    plot_h, plot_w = H - top - bottom, W - left - right
    step = plot_w / len(years)
    bar_w = step * 0.58
    for v in range(0, ymax + 1, 10):
        yv = top + plot_h - plot_h * v / ymax
        if v:
            c.polyline([(left, yv), (W - right, yv)], stroke=HAIR, sw=0.35, dash=(1.2, 1.4))
        c.polyline([(left - 2, yv), (left, yv)], sw=0.5)
        c.text(left - 3.5, yv + 2.3, str(v), 6.6, anchor='end')
    for i, year in enumerate(years):
        xb = left + i * step + (step - bar_w) / 2
        yb = top + plot_h
        for k, m in enumerate(modules):
            v = counts[m][i]
            if v:
                hgt = plot_h * v / ymax
                c.rect(xb, yb - hgt, bar_w, hgt, fill=GRAYS[k], stroke=INK, sw=0.35)
                yb -= hgt
        c.text(xb + bar_w / 2, yb - 2.6, str(totals[i]), 6.6, 'bold', anchor='middle')
        c.text(xb + bar_w / 2, top + plot_h + 9.5, str(year), 6.8, anchor='middle')
    c.polyline([(left, top - 2), (left, top + plot_h), (W - right, top + plot_h)], sw=0.6)
    c.text(9.0, top + plot_h / 2, 'Publications', 6.8, anchor='middle', rotate=-90)
    lx, ly = left + 8, top + 7
    lbox_w = max(width(l, 6.6) for l in labels) + 21
    c.rect(lx - 4, ly - 7, lbox_w, len(labels) * 9.4 + 4.5, fill=WHITE, stroke=HAIR, sw=0.5)
    for k, label in enumerate(labels):
        y = ly + k * 9.4
        c.rect(lx, y - 5.4, 7.5, 6.5, fill=GRAYS[k], stroke=INK, sw=0.35)
        c.text(lx + 11, y + 0.4, label, 6.6)
    return c


FIGURES = {'fig-taxonomy': fig_taxonomy, 'fig-stack': fig_stack, 'fig-evaluation': fig_evaluation,
           'fig-corpus': fig_corpus}


def main() -> None:
    for name, build in FIGURES.items():
        canvas = build()
        svg = canvas.svg()
        (OUT / f'{name}.svg').write_text(svg, encoding='utf-8', newline='\n')
        svg_to_pdf(svg, OUT / f'{name}.pdf')
        print(f'{name}: {canvas.w:.0f} x {canvas.h:.0f} pt')


if __name__ == '__main__':
    main()
