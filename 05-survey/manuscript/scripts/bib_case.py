"""Brace-protect case-sensitive title words before IEEEtran.bst applies sentence case.

IEEEtran.bst lowercases article and conference titles except the first letter and
the letter after a colon. Publisher BibTeX exports rarely brace acronyms or method
names, which would print "SLAM" as "slam" and "CARE" as "Care". This module braces
only words whose case carries meaning, leaving ordinary title-case words to the
style file:

* a hyphen-separated segment with a capital after its first character
  (SLAM, LiDAR, MPC, 3D, NavGPT) or a single capital inside a hyphenated name
  (R-FAC, C-CBF);
* proper names listed in ``PROPER_NAMES`` (Gaussian, Kalman, Voronoi, ...).

A hyphenated token is braced segment by segment when its other segments are
descriptive words (``LiDAR-based`` becomes ``{LiDAR}-based``); otherwise the whole
token is braced so that method names such as GA-Nav or Co-NavGPT stay intact.
Text already inside braces, math, and LaTeX commands is left unchanged.
"""
import re

PROPER_NAMES = {
    'Ackermann', 'Bayesian', 'Bezier', 'Boolean', 'Carlo', 'Cauchy', 'Delaunay', 'Dijkstra',
    'Euclidean', 'Euler', 'Fisher', 'Fourier', 'Gauss', 'Gaussian', 'Hamiltonian', 'Hessian',
    'Hilbert', 'Huber', 'Jacobian', 'Kalman', 'Koopman', 'Kullback', 'Lagrangian', 'Leibler',
    'Lie', 'Lyapunov', 'Mahalanobis', 'Markov', 'Mars', 'Monte', 'Nash', 'Newton', 'Pareto',
    'Poisson', 'Riemannian', 'Schmidt', 'Shannon', 'Stackelberg', 'Taylor', 'Voronoi',
    'Wasserstein', 'Wiener',
}

DESCRIPTIVE = {
    'aided', 'assisted', 'augmented', 'aware', 'based', 'camera', 'centric', 'constrained',
    'driven', 'enhanced', 'free', 'guided', 'imu', 'inertial', 'informed', 'integrated',
    'learning', 'level', 'odometer', 'only', 'radar', 'visual', 'wheel',
}

TOKEN = re.compile(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*")


def _meaningful(segment: str) -> bool:
    return bool(re.search(r'[A-Z]', segment[1:])) or segment in PROPER_NAMES


def _protect_token(token: str) -> str:
    segments = token.split('-')
    flags = [_meaningful(s) for s in segments]
    if len(segments) > 1:
        # A lone capital is part of a name when it leads the token (Q-learning,
        # R-FAC) or adjoins a protected segment.
        for i, s in enumerate(segments):
            if len(s) == 1 and s.isupper() and (
                    i == 0 or any(flags[j] for j in (i - 1, i + 1) if 0 <= j < len(segments))):
                flags[i] = True
    if not any(flags):
        return token
    if len(segments) == 1:
        return '{' + token + '}'
    rest = [s for s, f in zip(segments, flags) if not f]
    if all(s.lower() in DESCRIPTIVE for s in rest):
        return '-'.join('{' + s + '}' if f else s for s, f in zip(segments, flags))
    return '{' + token + '}'


def protect_title(title: str) -> str:
    """Return the inner title text with case-sensitive words braced."""
    out, i, depth, math = [], 0, 0, False
    while i < len(title):
        c = title[i]
        if c == '\\':
            m = re.match(r'\\([A-Za-z]+|.)', title[i:])
            out.append(m.group(0))
            i += len(m.group(0))
            continue
        if c == '$':
            math = not math
        elif c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        elif depth == 0 and not math:
            m = TOKEN.match(title, i)
            if m and (i == 0 or not title[i - 1].isalnum()):
                out.append(_protect_token(m.group(0)))
                i = m.end()
                continue
        out.append(c)
        i += 1
    return ''.join(out)


def _field_span(entry: str, name: str):
    """Locate the delimited value of a BibTeX field; return (start, end) of its inner text."""
    m = re.search(r'(^|[\s,])' + name + r'\s*=\s*', entry, re.I | re.M)
    if not m:
        return None
    i = m.end()
    if entry[i] == '"':
        j = entry.index('"', i + 1)
        return i + 1, j
    if entry[i] != '{':
        return None
    depth = 0
    for j in range(i, len(entry)):
        if entry[j] == '{':
            depth += 1
        elif entry[j] == '}':
            depth -= 1
            if depth == 0:
                return i + 1, j
    raise ValueError('unbalanced title field')


def protect_entry(entry: str) -> str:
    """Apply ``protect_title`` to the title field of one BibTeX entry."""
    span = _field_span(entry, 'title')
    if span is None:
        return entry
    a, b = span
    inner = entry[a:b]
    # A title wrapped whole in braces ({{Title Case Words}}) would keep title case
    # under IEEEtran; unwrap it so that the same word-level rule applies.
    if inner.startswith('{') and inner.endswith('}') and _closing(inner, 0) == len(inner) - 1:
        inner = inner[1:-1]
    return entry[:a] + protect_title(inner) + entry[b:]


def _closing(text: str, start: int) -> int:
    depth = 0
    for j in range(start, len(text)):
        if text[j] == '{':
            depth += 1
        elif text[j] == '}':
            depth -= 1
            if depth == 0:
                return j
    return -1
