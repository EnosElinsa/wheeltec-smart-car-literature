"""Minimal SVG drawing kit for the manuscript figures.

Coordinates are in points, so a figure of width 516 placed at \\textwidth in an
IEEE two-column journal keeps its font sizes. Text uses Times to match the
IEEEtran body font, lines are thin and black or gray, corners are square, and
no color is needed to read a figure. MuPDF converts the SVG files to vector PDF;
it ignores stroke-dasharray and markers, so dashes and arrowheads are drawn
explicitly.
"""
from __future__ import annotations

import math
from html import escape

import fitz

FONT = 'Times'
_METRIC = {('normal', 'normal'): 'tiro', ('bold', 'normal'): 'tibo',
           ('normal', 'italic'): 'tiit', ('bold', 'italic'): 'tibi'}

INK = '#111111'
MUTED = '#4A4A4A'
RULE = '#7A7A7A'
HAIR = '#B5B5B5'
FILL = '#E6E6E6'
FILL_LIGHT = '#F3F3F3'
WHITE = '#FFFFFF'

# Grayscale ramp for categorical data (dark to light), readable in print.
GRAYS = ['#262626', '#5C5C5C', '#8E8E8E', '#BDBDBD', '#E4E4E4']


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
    def rect(self, x, y, w, h, fill='none', stroke='none', sw=0.6, rx=0.0, dash=None):
        if dash is None:
            self.items.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" '
                              f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
            return
        if fill != 'none':
            self.items.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{fill}"/>')
        self.polyline([(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)], stroke=stroke, sw=sw, dash=dash)

    def circle(self, cx, cy, r, fill, stroke='none', sw=0.6):
        self.items.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r}" fill="{fill}" stroke="{stroke}" '
                          f'stroke-width="{sw}"/>')

    def polygon(self, points, fill, stroke='none', sw=0.6):
        pts = ' '.join(f'{x:.2f},{y:.2f}' for x, y in points)
        self.items.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
                          f'stroke-linejoin="miter"/>')

    def polyline(self, points, stroke=INK, sw=0.6, dash=None):
        if dash is None:
            pts = ' '.join(f'{x:.2f},{y:.2f}' for x, y in points)
            self.items.append(f'<polyline points="{pts}" fill="none" stroke="{stroke}" stroke-width="{sw}" '
                              f'stroke-linejoin="miter" stroke-linecap="butt"/>')
            return
        on, off = dash
        period = on + off
        phase = 0.0  # position within the dash pattern, continuous across segments
        dashes, current = [], None
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            length = math.hypot(x2 - x1, y2 - y1)
            if length == 0:
                continue
            ux, uy = (x2 - x1) / length, (y2 - y1) / length
            u = 0.0
            while u < length - 1e-9:
                if phase < on:
                    step = min(on - phase, length - u)
                    a = (x1 + ux * u, y1 + uy * u)
                    b = (x1 + ux * (u + step), y1 + uy * (u + step))
                    if current is None:
                        current = [a]
                    current.append(b)
                else:
                    step = min(period - phase, length - u)
                    if current is not None:
                        dashes.append(current)
                        current = None
                u += step
                phase = (phase + step) % period
        if current is not None:
            dashes.append(current)
        for d in dashes:
            pts = ' '.join(f'{x:.2f},{y:.2f}' for x, y in d)
            self.items.append(f'<polyline points="{pts}" fill="none" stroke="{stroke}" stroke-width="{sw}" '
                              f'stroke-linejoin="round" stroke-linecap="butt"/>')

    def arrow(self, points, stroke=INK, sw=0.6, dash=None, head=3.6, both=False, open_head=False):
        """Polyline ending in a slim arrowhead (and optionally starting with one)."""
        points = list(points)

        def tip(p_from, p_to):
            (x1, y1), (x2, y2) = p_from, p_to
            length = math.hypot(x2 - x1, y2 - y1)
            ux, uy = (x2 - x1) / length, (y2 - y1) / length
            base = (x2 - ux * head, y2 - uy * head)
            half = head * 0.36
            tri = [(x2, y2), (base[0] - uy * half, base[1] + ux * half), (base[0] + uy * half, base[1] - ux * half)]
            if open_head:
                self.polyline([tri[1], tri[0], tri[2]], stroke=stroke, sw=sw)
                return (x2, y2)
            self.polygon(tri, fill=stroke)
            return base

        body = points[:]
        body[-1] = tip(points[-2], points[-1])
        if both:
            body[0] = tip(points[1], points[0])
        self.polyline(body, stroke=stroke, sw=sw, dash=dash)

    # Text ------------------------------------------------------------------
    def text(self, x, y, s, size=7.0, weight='normal', style='normal', anchor='start', fill=INK, rotate=None):
        transform = ''
        if rotate is not None:
            transform = f' transform="rotate({rotate} {x:.2f} {y:.2f})"'
        self.items.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{FONT}" font-size="{size}" '
                          f'font-weight="{weight}" font-style="{style}" text-anchor="{anchor}" '
                          f'fill="{fill}"{transform}>{escape(s)}</text>')

    def lines(self, x, y, rows, size=7.0, leading=None, **kw):
        """Draw consecutive lines starting at baseline y; return the next baseline."""
        leading = leading or size * 1.2
        for row in rows:
            self.text(x, y, row, size=size, **kw)
            y += leading
        return y

    def marker(self, cx, cy, label, r=4.6):
        """Circled numeral that identifies an open interface (Section X)."""
        self.circle(cx, cy, r, fill=WHITE, stroke=INK, sw=0.6)
        self.text(cx, cy + 2.35, label, size=6.6, weight='bold', anchor='middle', fill=INK)

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
