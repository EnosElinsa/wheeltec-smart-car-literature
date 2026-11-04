"""Minimal SVG drawing kit for the manuscript figures.

Coordinates are in points, so a figure of width 516 placed at \\textwidth in an
IEEE two-column journal keeps its font sizes. MuPDF converts the SVG files to
vector PDF; it ignores stroke-dasharray and markers, so dashes and arrowheads
are drawn explicitly.
"""
from __future__ import annotations

import math
from html import escape

import fitz

FONT = 'Helvetica'
_METRIC = {('normal', 'normal'): 'helv', ('bold', 'normal'): 'hebo',
           ('normal', 'italic'): 'heit', ('bold', 'italic'): 'hebi'}

INK = '#222222'
MUTED = '#5B6570'
RULE = '#9AA3AD'
PANEL = '#F3F5F7'
ALERT = '#C0392B'

# One hue per survey function; the same hue is used in every figure.
FUNCTION = {
    'IV': ('#2E6DB4', '#E7EFF9'),
    'V': ('#1B8A7A', '#E2F3F0'),
    'VI': ('#7A4FA0', '#F0E8F6'),
    'VII': ('#B9770E', '#FBF1DF'),
    'VIII': ('#B23A48', '#F8E6E8'),
    'N': ('#4A5560', '#EEF0F2'),
}


def width(text: str, size: float, weight: str = 'normal', style: str = 'normal') -> float:
    return fitz.get_text_length(text, fontname=_METRIC[(weight, style)], fontsize=size)


def wrap(text: str, max_width: float, size: float, weight: str = 'normal', style: str = 'normal') -> list[str]:
    lines, current = [], ''
    for word in text.split():
        trial = f'{current} {word}'.strip()
        if current and width(trial, size, weight, style) > max_width:
            lines.append(current)
            current = word
        else:
            current = trial
    if current:
        lines.append(current)
    return lines


class Canvas:
    def __init__(self, w: float, h: float):
        self.w, self.h = w, h
        self.items: list[str] = []

    # Shapes ----------------------------------------------------------------
    def rect(self, x, y, w, h, fill='none', stroke='none', sw=0.6, rx=2.0, opacity=None):
        op = f' fill-opacity="{opacity}"' if opacity is not None else ''
        self.items.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" '
                          f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{op}/>')

    def circle(self, cx, cy, r, fill, stroke='none', sw=0.6):
        self.items.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def polygon(self, points, fill, stroke='none', sw=0.6, opacity=None):
        pts = ' '.join(f'{x:.2f},{y:.2f}' for x, y in points)
        op = f' fill-opacity="{opacity}"' if opacity is not None else ''
        self.items.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{op}/>')

    def polyline(self, points, stroke=INK, sw=0.7, dash=None):
        if dash is None:
            pts = ' '.join(f'{x:.2f},{y:.2f}' for x, y in points)
            self.items.append(f'<polyline points="{pts}" fill="none" stroke="{stroke}" stroke-width="{sw}" '
                              f'stroke-linejoin="round" stroke-linecap="round"/>')
            return
        on, off = dash
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            length = math.hypot(x2 - x1, y2 - y1)
            if length == 0:
                continue
            ux, uy = (x2 - x1) / length, (y2 - y1) / length
            s = 0.0
            while s < length:
                e = min(s + on, length)
                self.items.append(f'<line x1="{x1 + ux * s:.2f}" y1="{y1 + uy * s:.2f}" x2="{x1 + ux * e:.2f}" '
                                  f'y2="{y1 + uy * e:.2f}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="butt"/>')
                s = e + off

    def arrow(self, points, stroke=INK, sw=0.7, dash=None, head=4.2, both=False):
        """Polyline ending in a filled arrowhead (and optionally starting with one)."""
        points = list(points)

        def tip(p_from, p_to):
            (x1, y1), (x2, y2) = p_from, p_to
            length = math.hypot(x2 - x1, y2 - y1)
            ux, uy = (x2 - x1) / length, (y2 - y1) / length
            base = (x2 - ux * head, y2 - uy * head)
            half = head * 0.42
            self.polygon([(x2, y2), (base[0] - uy * half, base[1] + ux * half),
                          (base[0] + uy * half, base[1] - ux * half)], fill=stroke)
            return base

        body = points[:]
        body[-1] = tip(points[-2], points[-1])
        if both:
            body[0] = tip(points[1], points[0])
        self.polyline(body, stroke=stroke, sw=sw, dash=dash)

    # Text ------------------------------------------------------------------
    def text(self, x, y, s, size=7.0, weight='normal', style='normal', anchor='start', fill=INK):
        self.items.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{FONT}" font-size="{size}" '
                          f'font-weight="{weight}" font-style="{style}" text-anchor="{anchor}" '
                          f'fill="{fill}">{escape(s)}</text>')

    def lines(self, x, y, rows, size=7.0, leading=None, **kw):
        """Draw consecutive lines starting at baseline y; return the next baseline."""
        leading = leading or size * 1.22
        for row in rows:
            self.text(x, y, row, size=size, **kw)
            y += leading
        return y

    def marker(self, cx, cy, label, r=5.2, fill=ALERT):
        self.circle(cx, cy, r, fill=fill, stroke='#FFFFFF', sw=0.8)
        self.text(cx, cy + 2.4, label, size=6.6, weight='bold', anchor='middle', fill='#FFFFFF')

    def hazard(self, cx, cy, s=6.0, fill=INK):
        """Small warning triangle used to mark a degradation source."""
        self.polygon([(cx, cy - s * 0.55), (cx - s * 0.55, cy + s * 0.45), (cx + s * 0.55, cy + s * 0.45)],
                     fill=fill)
        self.text(cx, cy + s * 0.36, '!', size=s * 0.72, weight='bold', anchor='middle', fill='#FFFFFF')

    # Output ----------------------------------------------------------------
    def svg(self) -> str:
        body = '\n'.join(self.items)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}pt" height="{self.h}pt" '
                f'viewBox="0 0 {self.w} {self.h}">\n{body}\n</svg>\n')


def svg_to_pdf(svg_text: str, pdf_path) -> None:
    """Convert SVG source to a vector PDF page with embedded fonts."""
    doc = fitz.open(stream=svg_text.encode('utf-8'), filetype='svg')
    pdf = fitz.open('pdf', doc.convert_to_pdf())
    pdf.set_metadata({'producer': 'svgkit/PyMuPDF', 'creator': 'scripts/build_figures.py'})
    pdf.save(str(pdf_path), garbage=4, deflate=True, no_new_id=True)
