"""Report exact ten-word overlap between the survey and public project prose."""
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

MANUSCRIPT = Path(__file__).resolve().parents[1]
from project_paths import literature_root
REPOSITORY = literature_root(MANUSCRIPT)
TOKEN = re.compile(r"[a-z0-9]+(?:[-'][a-z0-9]+)*")
LATEX_ARG = re.compile(r"\\(?:cite|ref|eqref|label|input|includegraphics|bibliography)(?:\[[^\]]*\])?\{[^}]*\}")
LATEX_COMMAND = re.compile(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?")
MATH = re.compile(r"\${1,2}.*?\${1,2}", re.DOTALL)


def paragraphs(text: str):
    current = []
    for line in text.splitlines():
        if not line.strip():
            if current:
                yield " ".join(current)
                current = []
        else:
            current.append(line)
    if current:
        yield " ".join(current)


def tokens(text: str):
    text = re.sub(r"(?<!\\)%[^\n]*", " ", text)
    text = LATEX_ARG.sub(" ", text)
    text = MATH.sub(" ", text)
    text = LATEX_COMMAND.sub(" ", text)
    return TOKEN.findall(text.lower())


def ngrams(words, size):
    return [tuple(words[i:i + size]) for i in range(max(0, len(words) - size + 1))]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=10)
    parser.add_argument("--output", type=Path, default=MANUSCRIPT / "revision/overlap-report.json")
    args = parser.parse_args()
    if args.size < 5:
        parser.error("--size must be at least 5")

    source_index = defaultdict(list)
    for root in (REPOSITORY / "03-reviews", REPOSITORY / "04-analysis"):
        for path in sorted(root.rglob("*.md")):
            relative = path.relative_to(REPOSITORY).as_posix()
            for line_number, paragraph in enumerate(paragraphs(path.read_text(encoding="utf-8")), 1):
                for gram in set(ngrams(tokens(paragraph), args.size)):
                    source_index[gram].append({"file": relative, "paragraph": line_number})

    total_windows = 0
    matches = []
    for path in sorted((MANUSCRIPT / "sections").glob("*.tex")):
        relative = path.relative_to(MANUSCRIPT).as_posix()
        section_windows = 0
        section_matches = Counter()
        for paragraph in paragraphs(path.read_text(encoding="utf-8")):
            for gram in ngrams(tokens(paragraph), args.size):
                section_windows += 1
                if gram in source_index:
                    section_matches[gram] += 1
        total_windows += section_windows
        for gram, occurrences in sorted(section_matches.items()):
            matches.append({
                "section": relative,
                "ngram": " ".join(gram),
                "survey_occurrences": occurrences,
                "sources": source_index[gram],
            })

    overlapping_windows = sum(item["survey_occurrences"] for item in matches)
    report = {
        "ngram_size": args.size,
        "source_documents": len(list((REPOSITORY / "03-reviews").rglob("*.md")))
        + len(list((REPOSITORY / "04-analysis").rglob("*.md"))),
        "survey_windows": total_windows,
        "unique_overlapping_phrases": len(matches),
        "matching_survey_windows": overlapping_windows,
        "overlap_percent_of_survey_windows": round(100 * overlapping_windows / max(total_windows, 1), 4),
        "matches": matches,
        "interpretation": "Exact phrase matches are screening signals; technical names and standard terminology need manual review.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "matches"}, indent=2))


if __name__ == "__main__":
    main()
