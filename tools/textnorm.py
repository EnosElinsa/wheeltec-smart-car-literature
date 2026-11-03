"""Text normalization and fuzzy containment for excerpt verification.

Excerpts in reviews are copied from PDF text or from MinerU Markdown. The two
sources differ in hyphenation, quote characters, ligatures, line breaks, and
light Markdown or LaTeX markup. ``normalize`` removes those differences so that
an excerpt can be found in either source by plain substring search.
"""

from __future__ import annotations

import re
import unicodedata

_DASHES = "\u2010\u2011\u2012\u2013\u2014\u2015\u2212-"
_QUOTES = "'\"\u2018\u2019\u201a\u201b\u201c\u201d\u201e\u201f\u00b4\u0060"
_DASH_RE = re.compile("[" + re.escape(_DASHES) + "]")
_QUOTE_RE = re.compile("[" + re.escape(_QUOTES) + "]")
_MARKUP_RE = re.compile(r"[*#$\\{}~^]")
_TAG_RE = re.compile(r"</?[a-zA-Z][^>]{0,40}>")
_SPACE_RE = re.compile(r"\s+")


def normalize(text: str) -> str:
    """Return a lower-case, markup-free, single-spaced version of ``text``."""
    t = unicodedata.normalize("NFKC", text)
    t = t.replace("\u00ad", "")
    t = _TAG_RE.sub(" ", t)
    t = _DASH_RE.sub("-", t)
    t = re.sub(r"-\s+", "", t)  # hyphenation across line breaks
    t = t.replace("-", "")
    t = _QUOTE_RE.sub("", t)
    t = _MARKUP_RE.sub("", t)
    t = t.lower()
    t = _SPACE_RE.sub(" ", t)
    t = re.sub(r"\s+([,.;:!?)\]%])", r"\1", t)
    t = re.sub(r"([(\[])\s+", r"\1", t)
    return t.strip()


def ngrams(words: list[str], n: int) -> set[tuple[str, ...]]:
    return {tuple(words[i : i + n]) for i in range(len(words) - n + 1)}


def coverage(needle_norm: str, hay_ngrams: set[tuple[str, ...]], n: int) -> float:
    """Fraction of the needle's word n-grams that occur in the haystack."""
    words = needle_norm.split()
    grams = ngrams(words, n)
    if not grams:
        return 0.0
    return sum(1 for g in grams if g in hay_ngrams) / len(grams)


class NormalizedText:
    """A normalized document with a cached n-gram index."""

    def __init__(self, raw: str, n: int = 5):
        self.text = normalize(raw)
        self.n = n
        self._grams: set[tuple[str, ...]] | None = None

    @property
    def grams(self) -> set[tuple[str, ...]]:
        if self._grams is None:
            self._grams = ngrams(self.text.split(), self.n)
        return self._grams

    def match(self, needle: str, threshold: float = 0.8) -> str:
        """Return ``"exact"``, ``"fuzzy"``, or ``"missing"`` for ``needle``."""
        norm = normalize(needle)
        if not norm:
            return "missing"
        if norm in self.text:
            return "exact"
        if len(norm.split()) >= self.n + 2 and coverage(norm, self.grams, self.n) >= threshold:
            return "fuzzy"
        return "missing"
