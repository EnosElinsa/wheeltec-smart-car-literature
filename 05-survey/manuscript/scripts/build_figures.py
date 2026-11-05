"""Draw the manuscript figures as SVG sources and convert them to vector PDF.

Outputs ``figures/<name>.svg`` (editable source) and ``figures/<name>.pdf``
(included by LaTeX). The matrix and corpus figures read
``generated/degradation-function-matrix.json`` and ``generated/corpus-year-module.json``,
written by ``scripts/build_data.py``. All figures are grayscale line drawings
set in Times, so they print and photocopy without loss.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

from svgkit import FILL, FILL_LIGHT, GRAYS, HAIR, INK, MUTED, RULE, WHITE, Canvas, svg_to_pdf, width, wrap

M = Path(__file__).resolve().parents[1]
OUT = M / 'figures'
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# Fig. 1: degradation-source x function evidence matrix
# ---------------------------------------------------------------------------
# Short labels of the response families listed for each assumption (codebook 'assumptions').
FAMILY_LABELS = {
    'IV-A': 'selective updates', 'IV-B': 'complementary sensing', 'IV-C': 'contact priors',
    'IV-D': 'persistent maps', 'IV-E': 'relocalization', 'V-A': 'terrain risk', 'V-C': 'prediction',
    'V-D': 'risk constraints', 'V-E': 'tracking, delay', 'VI-A': 'semantic memory', 'VI-B': 'learned actions',
    'VI-C': 'candidate selection', 'VI-D': 'decision timing', 'VII-B': 'distributed estimation',
    'VII-C': 'rendezvous, repair', 'VIII-A': 'tolerant control', 'VIII-B': 'integrity monitors',
    'VIII-C': 'executed recovery', 'VIII-D': 'resource management',
}
COLUMN_NAMES = {'IV': 'Localization', 'V': 'Planning', 'VI': 'Semantic', 'VII': 'Multi-robot', 'VIII': 'Faults'}
SHADES = [WHITE, FILL_LIGHT, '#DCDCDC', '#C4C4C4']
LEGEND_LABELS = ['none', 'replay, simulation, model, or resource', 'hardware or recorded data',
                 'physical closed loop']


def fig_matrix() -> Canvas:
    data = json.loads((M / 'generated/degradation-function-matrix.json').read_text(encoding='utf-8'))
    sources = {s['id']: s for s in data['sources']}
    cells = {(x['source'], x['section']): x for x in data['cells']}
    sections = [f['section'] for f in data['functions']]
    marks = [(g['mark'], {'ROAD': 'road', 'GND': 'other_ground', 'OTH': 'non_ground'}[g['id']])
             for g in data['platform_groups'] if g['mark']]
    W, x0 = 516.0, 0.5
    a_w, s_w, cell_w, gap = 96.0, 80.0, 46.0, 3.0
    r_w = W - 2 * x0 - a_w - s_w - 5 * cell_w - 3 * gap
    xa, xs = x0, x0 + a_w + gap
    xc = xs + s_w + gap
    xr = xc + 5 * cell_w + gap
    fs, lead, pad = 7.0, 7.6, 2.3
    c = Canvas(W, 10)

    # Header.
    top = 0.5
    head_h = 2 * lead + 5
    c.polyline([(x0, top), (W - x0, top)], sw=0.8)
    for x, w, label in ((xa, a_w, 'Violated assumption'), (xs, s_w, 'Degradation source'),
                        (xr, r_w, 'Response families')):
        c.text(x + pad, top + head_h - 6, label, fs, 'bold')
    for k, sec in enumerate(sections):
        cx = xc + k * cell_w + cell_w / 2
        c.text(cx, top + lead + 1, f'Sec. {sec}', fs, 'bold', anchor='middle')
        c.text(cx, top + 2 * lead + 1, COLUMN_NAMES[sec], fs, anchor='middle')
    y = top + head_h
    c.polyline([(x0, y), (W - x0, y)], sw=0.6)

    for a in data['assumptions']:
        rows = a['sources']
        a_lines = wrap(f"{a['id']}. {a['statement'].rstrip('.')}", a_w - 2 * pad, fs)
        fam = [f'{f} {FAMILY_LABELS[f]}' for f in a['response_families']]
        s_lines = {s: wrap(sources[s]['name'], s_w - 2 * pad, fs) for s in rows}
        need = max(len(a_lines), len(fam)) * lead + 2 * pad
        heights = [max(2 * lead + 2 * pad, len(s_lines[s]) * lead + 2 * pad) for s in rows]
        extra = max(0.0, need - sum(heights))
        heights = [h + extra / len(rows) for h in heights]
        block = sum(heights)
        c.lines(xa + pad, y + pad + fs, a_lines, fs, lead)
        c.lines(xr + pad, y + pad + fs, fam, fs, lead)
        yy = y
        for s, h in zip(rows, heights):
            c.lines(xs + pad, yy + (h - len(s_lines[s]) * lead) / 2 + fs - 0.6, s_lines[s], fs, lead)
            for k, sec in enumerate(sections):
                cell = cells[(s, sec)]
                cx = xc + k * cell_w
                c.rect(cx, yy, cell_w, h, fill=SHADES[cell['shade']], stroke=HAIR, sw=0.4)
                mid = cx + cell_w / 2
                if not cell['addressed']:
                    c.text(mid, yy + h / 2 + 2.4, '\u2013', fs, anchor='middle', fill=MUTED)
                    continue
                c.text(mid, yy + h / 2 - 1.2, f"{cell['addressed']}/{cell['named']}/{cell['manipulated']}", fs,
                       anchor='middle')
                groups = [f"W{cell['wheeled_addressed']}"] + [f'{m}{cell[key]}' for m, key in marks if cell[key]]
                c.text(mid, yy + h / 2 + lead - 1.2, ' '.join(groups), fs, anchor='middle', fill=MUTED)
            if s != rows[-1]:
                c.polyline([(xs, yy + h), (xc, yy + h)], stroke=HAIR, sw=0.4)
            yy += h
        y += block
        c.polyline([(x0, y), (W - x0, y)], sw=0.8 if a is data['assumptions'][-1] else 0.5)

    # Shading legend.
    gy = y + 11.5
    x = x0 + pad
    title = 'Strongest setting with a named condition:'
    c.text(x, gy, title, fs, 'bold')
    x += width(title, fs, 'bold') + 8
    assert len(data['shade_steps']) == len(LEGEND_LABELS)
    for shade, label in enumerate(LEGEND_LABELS):
        c.rect(x, gy - 6.6, 10, 8, fill=SHADES[shade], stroke=INK, sw=0.5)
        c.text(x + 13, gy, label, fs)
        x += 13 + width(label, fs) + 10
    c.h = gy + 3.5
    return c


# ---------------------------------------------------------------------------
# Fig. 2: navigation stack, degradation entry points, and open interfaces
# ---------------------------------------------------------------------------
def box(c, x, y, w, h, sec, title, sub, fill=WHITE):
    c.rect(x, y, w, h, fill=fill, stroke=INK, sw=0.7)
    c.text(x + 4, y + 10, title, 7.2, 'bold')
    c.polyline([(x + 4, y + 13.5), (x + w - 4, y + 13.5)], stroke=HAIR, sw=0.4)
    c.lines(x + 4, y + 22.5, sub, 7.0, 8.0)
    if sec:
        c.text(x + w - 4, y + h - 3.6, f'Sec. {sec}', 7.0, style='italic', anchor='end', fill=MUTED)


def source_tag(c, x, y, title, detail, align='left'):
    w = max(width(title, 7.0, 'bold'), width(detail, 7.0, style='italic')) + 10
    if align == 'right':
        x = x - w
    c.rect(x, y, w, 22, fill=FILL_LIGHT, stroke=INK, sw=0.6, dash=(2.2, 1.4))
    c.text(x + 5, y + 9.2, title, 7.0, 'bold')
    c.text(x + 5, y + 18.2, detail, 7.0, style='italic', fill=MUTED)
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
             ('IV, V', 'Representation', ['Geometry, terrain,', 'semantics, persistence']),
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
    c.text(sx0 + 5, sy + 21.5, 'Sec. VIII', 7.0, style='italic', fill=MUTED)
    c.text(sx0 + 120, sy + 11.5, 'Monitor assumptions and integrity, request information,', 7.0)
    c.text(sx0 + 120, sy + 21, 'slow, stop, reinitialize, replan, reassign, or escalate', 7.0)
    est_x = xs[1] + bw / 2
    c.arrow([(est_x, my + bh), (est_x, sy)], dash=(2.6, 1.6), sw=0.7, head=3.6)
    for x in (xs[3] + bw / 2, xs[4] + bw / 2):
        c.arrow([(x, sy), (x, my + bh)], dash=(2.6, 1.6), sw=0.7, head=3.6)

    # Physical feedback loop.
    ly = sy + sh + 11
    c.arrow([(xs[4] + bw, flow_y), (W - 1.5, flow_y), (W - 1.5, ly), (xs[0] + bw / 2, ly), (xs[0] + bw / 2, my + bh)],
            sw=0.9, head=4.2)
    label = 'Executed motion changes the next observations'
    lw = width(label, 7.0, style='italic') + 10
    c.rect(W / 2 - lw / 2, ly - 5, lw, 10, fill=WHITE)
    c.text(W / 2, ly + 2.4, label, 7.0, style='italic', anchor='middle', fill=MUTED)

    # Degradation sources and their entry points.
    sx, sw_ = source_tag(c, 4, 58, 'Sensing and estimation', 'texture, geometry, bias, association')
    c.arrow([(xs[0] + bw / 2, 80), (xs[0] + bw / 2, my)], stroke=RULE, sw=0.6, head=3.4)
    c.arrow([(sx + sw_, 69), (xs[1] + 22, 69), (xs[1] + 22, my)], stroke=RULE, sw=0.6, head=3.4)
    ex, ew = source_tag(c, 4, 28, 'Environment and map change', 'moving agents, aged or moved structure')
    c.arrow([(ex + ew, 39), (xs[2] - 6, 39), (xs[2] - 6, my + 7), (xs[2], my + 7)], stroke=RULE, sw=0.6, head=3.4)
    cx_, cw_ = source_tag(c, 4, 2, 'Communication and computation', 'loss, delay, deadlines, memory')
    drop_t, drop_m = xs[3] + 16, xs[2] + bw - 16
    c.polyline([(cx_ + cw_, 13), (drop_t, 13)], stroke=RULE, sw=0.6)
    c.arrow([(drop_t, 13), (drop_t, ty)], stroke=RULE, sw=0.6, head=3.4)
    c.arrow([(drop_m, 13), (drop_m, ty)], stroke=RULE, sw=0.6, head=3.4)
    lx_, lw_ = source_tag(c, W - 4, 2, 'Learned and semantic inference', 'wrong output, misgrounding', align='right')
    entry_t = xs[3] + bw - 10
    c.arrow([(lx_, 17), (entry_t, 17), (entry_t, ty)], stroke=RULE, sw=0.6, head=3.4)
    side_x = (xs[3] + bw + xs[4]) / 2
    c.arrow([(side_x, 23), (side_x, my - 8), (entry_t, my - 8), (entry_t, my)], stroke=RULE, sw=0.6, head=3.4)
    source_tag(c, W - 4, 56, 'Terrain and mobility', 'slope, slip, material, actuation', align='right')
    c.arrow([(xs[4] + bw / 2, 78), (xs[4] + bw / 2, my)], stroke=RULE, sw=0.6, head=3.4)

    # Interface 3: pose covariance passed from state estimation to planning.
    cov_y = my + bh + 9
    cov_a, cov_b = xs[1] + bw - 12, xs[3] + 18
    c.polyline([(cov_a, my + bh), (cov_a, cov_y), (cov_b, cov_y)], stroke=INK, sw=0.7, dash=(2.6, 1.6))
    c.arrow([(cov_b, cov_y), (cov_b, my + bh)], dash=(2.6, 1.6), sw=0.7, head=3.6)

    # Open interfaces of Section X.
    c.marker(est_x + 10, (my + bh + sy) / 2, '1')
    c.marker(ti_x + 10, (ty + th + my) / 2, '2')
    c.marker(xs[2] + bw / 2, cov_y, '3')
    c.marker(tm_x + 10, (ty + th + my) / 2, '4')

    # Legend.
    gy = ly + 20
    x = 4.0
    items = ['Information flow', 'Exchange or supervision', 'Degradation source and entry point',
             'Open interface examined in Sec. X']
    c.arrow([(x, gy - 2.4), (x + 22, gy - 2.4)], sw=0.9, head=4.2)
    c.text(x + 26, gy, items[0], 7.0, fill=MUTED)
    x += 26 + width(items[0], 7.0) + 14
    c.arrow([(x, gy - 2.4), (x + 22, gy - 2.4)], sw=0.7, dash=(2.6, 1.6), head=3.6)
    c.text(x + 26, gy, items[1], 7.0, fill=MUTED)
    x += 26 + width(items[1], 7.0) + 14
    c.rect(x, gy - 7, 10, 9, fill=FILL_LIGHT, stroke=INK, sw=0.6, dash=(2.2, 1.4))
    c.arrow([(x + 11, gy - 2.4), (x + 25, gy - 2.4)], stroke=RULE, sw=0.6, head=3.4)
    c.text(x + 29, gy, items[2], 7.0, fill=MUTED)
    x += 29 + width(items[2], 7.0) + 14
    c.marker(x + 4.6, gy - 2.4, '1')
    c.text(x + 12.5, gy, items[3], 7.0, fill=MUTED)
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
        c.text(6, yy + h / 2 + 8.4, tag, 7.0, style='italic', fill=MUTED)
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
    c.text((t_on + t_off) / 2, yy + h / 2 + 2.3, 'degraded interval: source, severity, duration', 7.0,
           anchor='middle')
    c.text(x0 + 5, yy + h / 2 + 2.3, 'nominal', 7.0, fill=MUTED)
    c.text((t_rec + x1) / 2, yy + h / 2 + 2.3, 'nominal', 7.0, anchor='middle', fill=MUTED)

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
    c.text(x1 - 2, thr - 2.6, 'alarm threshold', 7.0, anchor='end', fill=MUTED)
    c.polyline(curve(err), stroke=INK, sw=0.8, dash=(2.4, 1.5))
    c.polyline(curve(stat), stroke=INK, sw=0.9)
    c.text(x0 + 4, base - 8.5, 'monitor statistic', 7.0)
    c.text(x1 - 2, base + 6.2, 'pose error against the reference', 7.0, anchor='end')
    c.polygon([(t_det, thr - 1), (t_det - 3.2, thr - 6.6), (t_det + 3.2, thr - 6.6)], fill=INK)
    fa = base - 5 - 21.0
    c.polygon([(174, fa - 1.5), (170.8, fa - 7.1), (177.2, fa - 7.1)], fill=WHITE, stroke=INK, sw=0.6)
    c.text(174, fa - 9.8, 'false alarm', 7.0, anchor='middle')

    # Lane 3: executed actions.
    yy, h = tops[2]
    segs = [(x0, t_act, 'nominal plan', WHITE), (t_act, t_reloc, 'slow and stop', FILL),
            (t_reloc, t_rec, 'relocalize', FILL), (t_rec, x1, 'resume task', WHITE)]
    for a, b, label, fill in segs:
        c.rect(a + 0.8, yy + 6, b - a - 1.6, h - 12, fill=fill, stroke=INK, sw=0.5)
        c.text((a + b) / 2, yy + h / 2 + 2.4, label, 7.0, anchor='middle')

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
    c.text(x0 + 4, hi + 2.2, 'progress toward the goal', 7.0)
    c.text(x1 - 2, lo - 8.6, 'completion, contacts,', 7.0, anchor='end', fill=MUTED)
    c.text(x1 - 2, lo - 0.6, 'interventions, time', 7.0, anchor='end', fill=MUTED)

    # Time axis and derived intervals.
    c.arrow([(x0, axis_y), (x1, axis_y)], sw=0.6, head=3.6)
    c.text(x1, axis_y + 9.5, 'time', 7.0, anchor='end', fill=MUTED)
    for t, name in events:
        c.polyline([(t, axis_y - 2), (t, axis_y + 2)], sw=0.6)
        c.text(t, axis_y + 9.5, name, 7.0, anchor='middle')
    spans = [(t_on, t_det, 'detection delay', 19.5), (t_det, t_act, 'response delay', 29),
             (t_on, t_rec, 'recovery time', 38.5)]
    for a, b, label, dy in spans:
        yb = axis_y + dy - 3
        c.arrow([(a, yb), (b, yb)], stroke=MUTED, sw=0.5, head=2.8, both=True)
        c.text(b + 4, yb + 2.4, label, 7.0, fill=MUTED)
    c.text(6, axis_y + 9.5, 'Report per episode', 7.0, 'bold')
    c.lines(6, axis_y + 18.8, ['trial unit, reference source,', 'alarms, actions, censoring'], 7.0, 8.2,
            fill=MUTED)
    c.h = axis_y + 43.5
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
        c.text(left - 3.5, yv + 2.3, str(v), 7.0, anchor='end')
    for i, year in enumerate(years):
        xb = left + i * step + (step - bar_w) / 2
        yb = top + plot_h
        for k, m in enumerate(modules):
            v = counts[m][i]
            if v:
                hgt = plot_h * v / ymax
                c.rect(xb, yb - hgt, bar_w, hgt, fill=GRAYS[k], stroke=INK, sw=0.35)
                yb -= hgt
        c.text(xb + bar_w / 2, yb - 2.6, str(totals[i]), 7.0, 'bold', anchor='middle')
        c.text(xb + bar_w / 2, top + plot_h + 9.5, str(year), 7.0, anchor='middle')
    c.polyline([(left, top - 2), (left, top + plot_h), (W - right, top + plot_h)], sw=0.6)
    c.text(9.0, top + plot_h / 2, 'Publications', 7.0, anchor='middle', rotate=-90)
    lx, ly = left + 8, top + 7
    lbox_w = max(width(l, 7.0) for l in labels) + 21
    c.rect(lx - 4, ly - 7, lbox_w, len(labels) * 9.4 + 4.5, fill=WHITE, stroke=HAIR, sw=0.5)
    for k, label in enumerate(labels):
        y = ly + k * 9.4
        c.rect(lx, y - 5.4, 7.5, 6.5, fill=GRAYS[k], stroke=INK, sw=0.35)
        c.text(lx + 11, y + 0.4, label, 7.0)
    return c


FIGURES = {'fig-matrix': fig_matrix, 'fig-stack': fig_stack, 'fig-evaluation': fig_evaluation,
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
