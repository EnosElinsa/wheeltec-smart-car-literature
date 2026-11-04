"""Draw the manuscript figures as SVG sources and convert them to vector PDF.

Outputs ``figures/<name>.svg`` (editable source) and ``figures/<name>.pdf``
(included by LaTeX). The corpus figure reads ``generated/corpus-year-module.json``
written by ``scripts/build_data.py``.
"""
from __future__ import annotations

import json
from pathlib import Path

from svgkit import ALERT, FUNCTION, INK, MUTED, PANEL, RULE, Canvas, svg_to_pdf, width, wrap

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


def fig_taxonomy() -> Canvas:
    W, margin, gap = 516.0, 2.0, 6.0
    cw = (W - 2 * margin - 4 * gap) / 5
    pad = 4.0
    c = Canvas(W, 10)
    # Measure every column so that rows align across columns.
    head_lines = [wrap(title, cw - 22, 7.2, 'bold') for _, title, _ in TAXONOMY]
    head_h = max(len(h) for h in head_lines) * 8.6 + 8
    cells = []
    for _, _, mechs in TAXONOMY:
        col = []
        for name, methods in mechs:
            n = wrap(name, cw - 2 * pad, 6.8, 'bold')
            m = wrap(methods, cw - 2 * pad, 6.0, 'normal', 'italic')
            col.append((n, m, len(n) * 8.0 + len(m) * 7.1 + 6))
        cells.append(col)
    row_h = [max(cells[k][r][2] for k in range(5)) for r in range(4)]

    root_y, root_h = 4.0, 17.0
    root_w = 250.0
    c.rect((W - root_w) / 2, root_y, root_w, root_h, fill=INK, rx=3)
    c.text(W / 2, root_y + 11.6, 'Responses to degradation in wheeled navigation', 8.0, 'bold',
           anchor='middle', fill='#FFFFFF')
    bus_y = root_y + root_h + 7
    head_y = bus_y + 7
    xs = [margin + k * (cw + gap) for k in range(5)]
    c.polyline([(W / 2, root_y + root_h), (W / 2, bus_y)], stroke=RULE, sw=0.8)
    c.polyline([(xs[0] + cw / 2, bus_y), (xs[4] + cw / 2, bus_y)], stroke=RULE, sw=0.8)
    for k, (sec, _, _) in enumerate(TAXONOMY):
        dark, tint = FUNCTION[sec]
        x = xs[k]
        c.arrow([(x + cw / 2, bus_y), (x + cw / 2, head_y)], stroke=RULE, sw=0.8, head=3.4)
        c.rect(x, head_y, cw, head_h, fill=dark, rx=2.5)
        c.text(x + 5, head_y + 11, sec, 7.4, 'bold', fill='#FFFFFF')
        c.lines(x + 21, head_y + 10.6, head_lines[k], 7.2, 8.6, weight='bold', fill='#FFFFFF')
        y = head_y + head_h + 4
        for r, (n, m, _) in enumerate(cells[k]):
            c.rect(x, y, cw, row_h[r], fill=tint, stroke=dark, sw=0.5, rx=2)
            c.rect(x + 0.3, y + 0.3, 2.2, row_h[r] - 0.6, fill=dark, rx=0)
            yy = c.lines(x + pad + 1, y + 9.2, n, 6.8, 8.0, weight='bold', fill=INK)
            c.lines(x + pad + 1, yy + 0.4, m, 6.0, 7.1, style='italic', fill=MUTED)
            y += row_h[r] + 3
    body_bottom = y + 1

    # Evaluation and open interfaces.
    band_y = body_bottom + 6
    c.polyline([(margin, band_y - 3), (W - margin, band_y - 3)], stroke=RULE, sw=0.5)
    left_w = 214.0
    dark, tint = FUNCTION['N']
    band_h = 53.0
    c.rect(margin, band_y, left_w, band_h, fill=tint, stroke=dark, sw=0.5, rx=2)
    c.text(margin + 5, band_y + 10, 'IX  Evaluation practice', 7.2, 'bold', fill=INK)
    axes = [('Measurement level', 'component vs. task outcome'),
            ('Test conditions', 'onset, severity, duration'),
            ('Risk and diagnostic claims', 'event, calibration, assumptions')]
    cx = margin + 5
    chip_w = (left_w - 10 - 2 * 4) / 3
    for title, sub in axes:
        c.rect(cx, band_y + 15, chip_w, band_h - 19, fill='#FFFFFF', stroke=RULE, sw=0.5, rx=2)
        rows = wrap(title, chip_w - 6, 6.4, 'bold')
        yy = c.lines(cx + 3.5, band_y + 23, rows, 6.4, 7.4, weight='bold')
        c.lines(cx + 3.5, yy, wrap(sub, chip_w - 6, 5.9, style='italic'), 5.9, 6.8, style='italic', fill=MUTED)
        cx += chip_w + 4
    rx0 = margin + left_w + 6
    rw = W - margin - rx0
    c.rect(rx0, band_y, rw, band_h, fill='#FFFFFF', stroke=ALERT, sw=0.6, rx=2)
    c.text(rx0 + 5, band_y + 10, 'X  Open interfaces between functions', 7.2, 'bold', fill=INK)
    col_w = (rw - 10) / 2
    for i, (num, label) in enumerate(CHALLENGES):
        px = rx0 + 5 + (i % 2) * col_w
        py = band_y + 25 + (i // 2) * 16
        c.marker(px + 5, py - 2.4, num)
        c.text(px + 14, py, label, 6.6, fill=INK)
    c.h = band_y + band_h + 2
    return c


# ---------------------------------------------------------------------------
# Fig. 2: navigation stack, degradation entry points, and open interfaces
# ---------------------------------------------------------------------------
def box(c, x, y, w, h, sec, title, sub):
    dark, tint = FUNCTION[sec]
    c.rect(x, y, w, h, fill=tint, stroke=dark, sw=0.7, rx=2.5)
    c.rect(x, y, w, 12.5, fill=dark, rx=2.5)
    c.rect(x, y + 8, w, 4.5, fill=dark, rx=0)
    c.text(x + 4, y + 9, title, 6.9, 'bold', fill='#FFFFFF')
    yy = c.lines(x + 4, y + 21.5, sub, 6.2, 7.3, fill=INK)
    if sec != 'N':
        c.text(x + w - 4, y + h - 3.5, f'Sec. {sec}', 5.6, 'bold', anchor='end', fill=dark)


def source_tag(c, x, y, title, detail, align='left'):
    w = max(width(title, 6.4, 'bold'), width(detail, 5.8, style='italic')) + 25
    if align == 'right':
        x = x - w
    c.rect(x, y, w, 21, fill='#FFFFFF', stroke=INK, sw=0.6, rx=10.5)
    c.hazard(x + 9.5, y + 10.5, 7.2)
    c.text(x + 17, y + 9, title, 6.4, 'bold')
    c.text(x + 17, y + 17, detail, 5.8, style='italic', fill=MUTED)
    return x, w


def fig_stack() -> Canvas:
    W = 516.0
    c = Canvas(W, 10)
    bw, bh = 86.0, 46.0
    gap = (W - 8 - 5 * bw) / 4
    xs = [4 + k * (bw + gap) for k in range(5)]
    my = 94.0
    specs = [('N', 'Measurements', ['Cameras, LiDAR, radar,', 'IMU, wheels, GNSS, UWB']),
             ('IV', 'State estimation', ['Pose, covariance,', 'validity, measurement age']),
             ('IV', 'Representation', ['Geometry, terrain,', 'semantics, persistence']),
             ('V', 'Planning', ['Route, trajectory,', 'risk and feasibility']),
             ('V', 'Control', ['Feasible wheel commands', 'under actuator limits'])]
    for x, (sec, title, sub) in zip(xs, specs):
        box(c, x, my, bw, bh, sec, title, sub)
    flow_y = my + 27
    for k in range(4):
        c.arrow([(xs[k] + bw, flow_y), (xs[k + 1], flow_y)], sw=0.9, head=4.6)

    # Upper row: teammates and task interpretation.
    ty, th = 28.0, 42.0
    box(c, xs[2], ty, bw, th, 'VII', 'Teammates', ['Shared maps, poses,', 'allocations'])
    box(c, xs[3], ty, bw, th, 'VI', 'Task interpretation', ['Goals, language,', 'social preferences'])
    tm_x, ti_x = xs[2] + bw / 2, xs[3] + bw / 2
    c.arrow([(tm_x, ty + th), (tm_x, my)], dash=(2.6, 1.8), sw=0.8, both=True, head=4.0)
    c.arrow([(ti_x, ty + th), (ti_x, my)], dash=(2.6, 1.8), sw=0.8, head=4.0)

    # Supervision row.
    sy, sh = my + bh + 22, 27.0
    sx0, sx1 = xs[1], xs[4] + bw
    dark, tint = FUNCTION['VIII']
    c.rect(sx0, sy, sx1 - sx0, sh, fill=tint, stroke=dark, sw=0.7, rx=2.5)
    c.rect(sx0, sy, 118, sh, fill=dark, rx=2.5)
    c.text(sx0 + 5, sy + 11, 'Supervision and recovery', 6.9, 'bold', fill='#FFFFFF')
    c.text(sx0 + 5, sy + 21, 'Sec. VIII', 5.8, 'bold', fill='#FFFFFF')
    c.text(sx0 + 126, sy + 11.5, 'Monitor assumptions and integrity; request information;', 6.2)
    c.text(sx0 + 126, sy + 20.5, 'slow, stop, reinitialize, replan, reassign, or escalate', 6.2)
    est_x = xs[1] + bw / 2
    c.arrow([(est_x, my + bh), (est_x, sy)], dash=(2.6, 1.8), sw=0.8, head=4.0)
    for x in (xs[3] + bw / 2, xs[4] + bw / 2):
        c.arrow([(x, sy), (x, my + bh)], dash=(2.6, 1.8), sw=0.8, head=4.0)

    # Physical feedback loop.
    ly = sy + sh + 11
    c.arrow([(xs[4] + bw, flow_y), (W - 1.5, flow_y), (W - 1.5, ly), (xs[0] + bw / 2, ly), (xs[0] + bw / 2, my + bh)],
            sw=0.9, head=4.6)
    label = 'Executed motion changes the next observations'
    lw = width(label, 6.3, style='italic') + 10
    c.rect(W / 2 - lw / 2, ly - 5, lw, 10, fill='#FFFFFF', rx=0)
    c.text(W / 2, ly + 2.2, label, 6.3, style='italic', anchor='middle', fill=MUTED)

    # Degradation entry points.
    sx, sw_ = source_tag(c, 4, 58, 'Sensing and estimation', 'texture, geometry, bias, association')
    c.arrow([(xs[0] + bw / 2, 79), (xs[0] + bw / 2, my)], sw=0.7, head=3.8)
    c.arrow([(sx + sw_, 68.5), (xs[1] + 22, 68.5), (xs[1] + 22, my)], sw=0.7, head=3.8)
    ex, ew = source_tag(c, 4, 28, 'Environment and map change', 'moving agents, aged or moved structure')
    c.arrow([(ex + ew, 38.5), (xs[2] - 6, 38.5), (xs[2] - 6, my + 7), (xs[2], my + 7)], sw=0.7, head=3.8)
    cx_, cw_ = source_tag(c, W - 4, 2, 'Communication and compute', 'loss, delay, deadlines, memory', align='right')
    drop_t, drop_m = xs[3] + bw - 16, xs[2] + bw - 16
    c.polyline([(cx_, 12.5), (drop_m, 12.5)], sw=0.7)
    c.arrow([(drop_t, 12.5), (drop_t, ty)], sw=0.7, head=3.8)
    c.arrow([(drop_m, 12.5), (drop_m, ty)], sw=0.7, head=3.8)
    rx_, rw_ = source_tag(c, W - 4, 56, 'Terrain and mobility', 'slope, slip, material, actuation', align='right')
    c.arrow([(xs[4] + bw / 2, 77), (xs[4] + bw / 2, my)], sw=0.7, head=3.8)

    # Open interfaces of Section X.
    c.marker(est_x + 10, (my + bh + sy) / 2, '1')
    c.marker(ti_x + 10, (ty + th + my) / 2, '2')
    c.marker((xs[2] + bw + xs[3]) / 2, flow_y - 10, '3')
    c.marker(tm_x + 10, (ty + th + my) / 2, '4')

    # Legend.
    gy = ly + 20
    x = 4.0
    c.polyline([(x, gy - 2.4), (x + 18, gy - 2.4)], sw=0.9)
    c.polygon([(x + 22, gy - 2.4), (x + 17.5, gy - 4.3), (x + 17.5, gy - 0.5)], fill=INK)
    items = ['Main information flow', 'Exchange or supervision', 'Degradation source and entry point',
             'Open interface examined in Sec. X (numbering as in Fig. 1)']
    c.text(x + 26, gy, items[0], 6.2, fill=MUTED)
    x += 26 + width(items[0], 6.2) + 14
    c.polyline([(x, gy - 2.4), (x + 22, gy - 2.4)], sw=0.8, dash=(2.6, 1.8))
    c.text(x + 26, gy, items[1], 6.2, fill=MUTED)
    x += 26 + width(items[1], 6.2) + 14
    c.hazard(x + 4, gy - 2.6, 7.0)
    c.text(x + 11, gy, items[2], 6.2, fill=MUTED)
    x += 11 + width(items[2], 6.2) + 14
    c.marker(x + 4, gy - 2.4, '1', r=4.6)
    c.text(x + 11, gy, items[3], 6.2, fill=MUTED)
    c.h = gy + 4
    return c


# ---------------------------------------------------------------------------
# Fig. 3: joint evaluation of detection and response in one episode
# ---------------------------------------------------------------------------
def fig_evaluation() -> Canvas:
    import math
    W = 516.0
    c = Canvas(W, 10)
    x0, x1 = 112.0, 510.0
    t_on, t_det, t_act, t_reloc, t_rec, t_off = 212.0, 262.0, 292.0, 342.0, 394.0, 368.0
    lanes = [('Operating condition', 'Test conditions', 34),
             ('Internal signals', 'Component and diagnostic measures', 48),
             ('Executed response', 'Response mechanism', 30),
             ('Task outcome', 'Task measures', 40)]
    y = 4.0
    tops = []
    for title, tag, h in lanes:
        c.rect(4, y, W - 8, h, fill=PANEL, rx=2)
        c.text(10, y + h / 2 - 1, title, 7.0, 'bold')
        c.text(10, y + h / 2 + 7.5, tag, 6.0, style='italic', fill=MUTED)
        tops.append((y, h))
        y += h + 4
    axis_y = y + 2
    events = [(t_on, 'onset'), (t_det, 'alarm'), (t_act, 'action'), (t_rec, 'recovered')]
    for t, _ in events:
        c.polyline([(t, tops[0][0] + 2), (t, axis_y)], stroke=RULE, sw=0.5, dash=(1.6, 1.6))

    # Lane 1: degraded interval.
    yy, h = tops[0]
    sens, sens_tint = FUNCTION['IV']
    c.rect(x0, yy + 7, x1 - x0, h - 14, fill='#FFFFFF', stroke=RULE, sw=0.4, rx=1)
    c.rect(t_on, yy + 7, t_off - t_on, h - 14, fill=sens_tint, stroke=sens, sw=0.6, rx=1)
    label = 'degraded interval: source, severity, duration'
    lw = width(label, 6.0) + 8
    c.rect((t_on + t_off) / 2 - lw / 2, yy + h / 2 - 5, lw, 10, fill=sens_tint, rx=1)
    c.text((t_on + t_off) / 2, yy + h / 2 + 2.1, label, 6.0, anchor='middle', fill=sens)
    c.text(x0 + 5, yy + h / 2 + 2.2, 'nominal', 6.2, style='italic', fill=MUTED)
    c.text(t_off + 6, yy + h / 2 + 2.2, 'nominal', 6.2, style='italic', fill=MUTED)

    # Lane 2: monitor statistic (crosses the threshold at the alarm) and pose error.
    yy, h = tops[1]
    base = yy + h - 7
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

    c.polyline([(x0, thr), (x1, thr)], stroke=ALERT, sw=0.6, dash=(3, 2))
    c.text(x1 - 2, thr - 2.5, 'alarm threshold', 5.8, anchor='end', fill=ALERT)
    c.polyline(curve(err), stroke=INK, sw=0.9)
    c.polyline(curve(stat), stroke=sens, sw=0.9)
    c.text(x0 + 4, base - 8, 'monitor statistic', 5.8, fill=sens)
    c.text(x1 - 2, base + 5.5, 'pose error against the reference', 5.8, anchor='end', fill=INK)
    c.polygon([(t_det, thr - 1), (t_det - 3.4, thr - 7), (t_det + 3.4, thr - 7)], fill=ALERT)
    fa = base - 5 - 21.0
    c.polygon([(174, fa - 1.5), (170.6, fa - 7.5), (177.4, fa - 7.5)], fill='#FFFFFF', stroke=ALERT, sw=0.7)
    c.text(174, fa - 10, 'false alarm', 5.8, anchor='middle', fill=ALERT)

    # Lane 3: executed actions.
    yy, h = tops[2]
    v8, v8t = FUNCTION['VIII']
    segs = [(x0, t_act, 'nominal plan', '#FFFFFF', RULE), (t_act, t_reloc, 'slow and stop', v8t, v8),
            (t_reloc, t_rec, 'relocalize', v8t, v8), (t_rec, x1, 'resume task', '#FFFFFF', RULE)]
    for a, b, label, fill, stroke in segs:
        c.rect(a + 0.8, yy + 6, b - a - 1.6, h - 12, fill=fill, stroke=stroke, sw=0.6, rx=1.5)
        c.text((a + b) / 2, yy + h / 2 + 2.2, label, 6.2, anchor='middle')

    # Lane 4: task progress.
    yy, h = tops[3]
    lo, hi = yy + h - 6, yy + 7
    rate = (lo - hi) / (x1 - x0) * 1.3

    def prog(t):
        if t < t_act:
            return lo - (t - x0) * rate
        if t < t_rec:
            return lo - (t_act - x0) * rate - (t - t_act) * rate * 0.05
        return max(lo - (t_act - x0) * rate - (t_rec - t_act) * rate * 0.05 - (t - t_rec) * rate, hi)
    v5 = FUNCTION['V'][0]
    c.polyline(curve(prog), stroke=v5, sw=1.0)
    c.text(x0 + 4, hi + 3, 'progress toward the goal', 5.8, fill=v5)
    c.text(x1 - 2, lo - 0.5, 'completion, contacts, interventions, time', 5.8, anchor='end', fill=MUTED)

    # Time axis and derived intervals.
    c.arrow([(x0, axis_y), (x1, axis_y)], sw=0.7, head=3.8)
    c.text(x1, axis_y + 9, 'time', 6.0, anchor='end', fill=MUTED)
    for t, name in events:
        c.polyline([(t, axis_y - 2), (t, axis_y + 2)], sw=0.7)
        c.text(t, axis_y + 9, name, 6.0, anchor='middle')
    spans = [(t_on, t_det, 'detection delay', 19), (t_det, t_act, 'response delay', 28), (t_on, t_rec, 'recovery time', 37)]
    for a, b, label, dy in spans:
        yb = axis_y + dy - 3
        c.arrow([(a, yb), (b, yb)], stroke=MUTED, sw=0.6, head=2.8, both=True)
        c.text(b + 4, yb + 2.1, label, 5.9, fill=MUTED)
    c.text(10, axis_y + 9, 'Report per episode', 6.4, 'bold')
    c.lines(10, axis_y + 18, ['trial unit, reference source,', 'alarms, actions, censoring'], 6.0, 7.6,
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
    bar_w = step * 0.6
    for v in range(0, ymax + 1, 10):
        yv = top + plot_h - plot_h * v / ymax
        c.polyline([(left, yv), (W - right, yv)], stroke='#E3E7EB', sw=0.5)
        c.text(left - 3.5, yv + 2.2, str(v), 6.0, anchor='end', fill=MUTED)
    secs = ['IV', 'V', 'VI', 'VII', 'VIII']
    for i, year in enumerate(years):
        xb = left + i * step + (step - bar_w) / 2
        yb = top + plot_h
        for m, sec in zip(modules, secs):
            v = counts[m][i]
            if v:
                hgt = plot_h * v / ymax
                c.rect(xb, yb - hgt, bar_w, hgt, fill=FUNCTION[sec][0], stroke='#FFFFFF', sw=0.4, rx=0)
                yb -= hgt
        c.text(xb + bar_w / 2, yb - 2.5, str(totals[i]), 6.2, 'bold', anchor='middle')
        c.text(xb + bar_w / 2, top + plot_h + 9, str(year), 6.3, anchor='middle')
    c.polyline([(left, top), (left, top + plot_h), (W - right, top + plot_h)], sw=0.6)
    c.text(left - 20, top - 5, 'Publications', 6.0, fill=MUTED)
    lx, ly = left + 8, top + 8
    lbox_w = max(width(l, 6.2) for l in labels) + 20
    c.rect(lx - 4, ly - 7, lbox_w, len(labels) * 9.2 + 5, fill='#FFFFFF', stroke='#E3E7EB', sw=0.5, rx=1.5)
    for k, (label, sec) in enumerate(zip(labels, secs)):
        y = ly + k * 9.2
        c.rect(lx, y - 5.2, 6.5, 6.5, fill=FUNCTION[sec][0], rx=1)
        c.text(lx + 10, y + 0.4, label, 6.2)
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
