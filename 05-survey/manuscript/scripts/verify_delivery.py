"""Static delivery audit after a successful manuscript build."""
import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

MANUSCRIPT = Path(__file__).resolve().parents[1]
from project_paths import literature_root
from citation_scope import load_background, load_corpus
REPOSITORY = literature_root(MANUSCRIPT)


def text_digest(path):
    """SHA-256 of a text file with CRLF normalized to LF, independent of the checkout line endings."""
    return hashlib.sha256(path.read_bytes().replace(b'\r\n', b'\n')).hexdigest()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", action="store_true", help="Also verify local publisher PDFs and full-text transcriptions")
    args = parser.parse_args()
    all_rows, rows, inclusion, citation_policy = load_corpus(REPOSITORY, MANUSCRIPT)
    stats = json.loads((MANUSCRIPT / 'generated/stats.json').read_text(encoding='utf-8'))
    assert len(rows) == len(inclusion['selected_ids']) == len(set(inclusion['selected_ids']))
    assert {row['code'] for row in rows} == set(inclusion['selected_ids'])
    assert stats['source_index_sha256'] == digest(REPOSITORY / '06-data/paper-index.csv')
    assert stats['comparison_sha256'] == digest(REPOSITORY / '06-data/corpus-comparison.csv')
    assert stats['citation_scope_sha256'] == text_digest(MANUSCRIPT / 'data/citation-scope.json')
    assert stats['inclusion_sha256'] == text_digest(REPOSITORY / '06-data/survey-inclusion.json')
    sections = sorted((MANUSCRIPT / "sections").glob("*.tex"))
    text = "\n".join(path.read_text(encoding="utf-8") for path in sections)
    # Only included artifacts define labels in the delivered manuscript.
    included = {match for match in re.findall(r"\\input\{([^}]+)\}", text)}
    all_tex = text + "\n" + "\n".join((MANUSCRIPT / (name + ".tex")).read_text(encoding="utf-8") for name in sorted(included))
    bibliography = (MANUSCRIPT / "refs.bib").read_text(encoding="utf-8")
    bibkeys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bibliography)
    cited_keys = {key.strip() for group in re.findall(r"\\cite\{([^}]+)\}", text) for key in group.split(",")}
    corpus_keys = {"P_" + row["code"] for row in rows}
    labels = re.findall(r"\\label\{([^}]+)\}", all_tex)
    ref_uses = set(re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", all_tex))
    bbl = (MANUSCRIPT / "survey.bbl").read_text(encoding="utf-8")
    resolved_keys = set(re.findall(r"\\bibitem\{([^}]+)\}", bbl))
    log = (MANUSCRIPT / "survey.log").read_text(encoding="utf-8", errors="replace")

    background = load_background(MANUSCRIPT, citation_policy)
    assert len(bibkeys) == len(set(bibkeys)) == len(rows) + len(background)
    assert corpus_keys <= cited_keys <= set(bibkeys)
    assert len(labels) == len(set(labels)) == 27
    assert resolved_keys == set(bibkeys)
    assert not ({'P_' + code for code in citation_policy['internal_reference_ids']} |
                set(citation_policy['excluded_background_keys'])) & (cited_keys | resolved_keys)
    assert not re.search(r"undefined|Overfull|LaTeX Warning", log, re.IGNORECASE)
    equation_pattern = r'\\begin\{equation\}.*?\\end\{equation\}'
    current_equations = re.findall(equation_pattern, text, re.DOTALL)
    baseline = json.loads((MANUSCRIPT / 'data/equation-baseline.json').read_text(encoding='utf-8'))
    assert len(current_equations) == 6
    assert [hashlib.sha256(e.encode('utf-8')).hexdigest() for e in current_equations] == baseline['sha256']
    source_artifacts_checked = 0
    for row in all_rows:
        for field, hash_field in (("pdf", "pdf_sha256"), ("bibtex", "bibtex_sha256"), ("markdown", "markdown_sha256")):
            if args.sources or field == 'bibtex':
                assert digest(REPOSITORY / row[field]) == row[hash_field], (row["code"], field)
                source_artifacts_checked += 1

    info = subprocess.check_output(["pdfinfo", str(MANUSCRIPT / "survey.pdf")], text=True, encoding="utf-8", errors="replace")
    pages = int(re.search(r"^Pages:\s+(\d+)", info, re.MULTILINE)[1])
    # T-IV allows at most 24 pages; the lower bound is a truncation check.
    assert 20 <= pages <= 24

    supplement = (MANUSCRIPT / "supplement.tex").read_text(encoding="utf-8")
    supplement_inputs = set(re.findall(r"\\input\{([^}]+)\}", supplement))
    supplement_tex = supplement + "\n" + "\n".join(
        (MANUSCRIPT / (name + ".tex")).read_text(encoding="utf-8")
        for name in sorted(supplement_inputs)
    )
    supplement_labels = re.findall(r"\\label\{([^}]+)\}", supplement_tex)
    supplement_refs = set(re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", supplement_tex))
    supplement_tables = {"tab:" + m for m in ("localization", "planning", "semantic", "multi-robot", "reliability")}
    assert len(supplement_labels) == len(set(supplement_labels)) == 13
    assert {"tab:selection", "fig:corpus"} | supplement_tables <= set(supplement_labels)
    assert set(supplement_labels).isdisjoint(labels)
    assert supplement_refs <= set(supplement_labels)
    # The main text cites the supplement tables through xr (\externaldocument[S-]{supplement}).
    external_refs = {ref[2:] for ref in ref_uses if ref.startswith("S-")}
    assert ref_uses - {"S-" + ref for ref in external_refs} <= set(labels)
    assert external_refs == supplement_tables
    supplement_citations = {
        key.strip() for group in re.findall(r"\\cite\{([^}]+)\}", supplement_tex)
        for key in group.split(",")
    }
    supplement_bbl = (MANUSCRIPT / "supplement.bbl").read_text(encoding="utf-8")
    supplement_resolved = set(re.findall(r"\\bibitem\{([^}]+)\}", supplement_bbl))
    assert supplement_citations == supplement_resolved <= set(bibkeys)
    assert supplement_resolved.isdisjoint({'P_' + code for code in citation_policy['internal_reference_ids']})
    technical_rows = [row for row in rows if row['survey_included'] == 'yes']
    assert len(technical_rows) == stats['evaluation_denominator']
    assert len(rows) - len(technical_rows) == stats['survey_included'].get('context', 0)
    assert all(row['evidence_type'] != 'survey' for row in technical_rows)
    evaluation_counts = {}
    for row in technical_rows:
        for attribute in row['evaluation_all'].split(','):
            attribute = attribute.strip()
            evaluation_counts[attribute] = evaluation_counts.get(attribute, 0) + 1
    assert evaluation_counts == stats['evaluation_technical']
    # Evidence map (Table IV): recompute the function x attribute counts and check the generated rows.
    evaluation_table = (MANUSCRIPT / 'generated/table-evaluation.tex').read_text(encoding='utf-8')
    evidence_map = stats['evidence_map']
    for module, values in evidence_map.items():
        group = [row for row in technical_rows if row['survey_module'] == module]
        attrs = [{x.strip() for x in row['evaluation_all'].split(',')} for row in group]
        assert values == {
            'publications': len(group),
            'residual': sum('residual' in a for a in attrs),
            'closed-loop-task': sum('closed-loop-task' in a for a in attrs),
            'designed-degradation': sum('designed-degradation' in a for a in attrs),
            'degradation-with-task': sum({'designed-degradation', 'closed-loop-task'} <= a for a in attrs),
            'integrity-reliability': sum('integrity-reliability' in a for a in attrs),
            'placement-reported': sum(row['compute_location'] != 'not-reported' for row in group),
            'wheeled-target': sum(row['boundary_platform'] == 'no' for row in group),
        }, module
    assert sum(v['publications'] for v in evidence_map.values()) == len(technical_rows)
    for key in ('publications', 'residual', 'closed-loop-task', 'designed-degradation',
                'degradation-with-task', 'integrity-reliability', 'placement-reported', 'wheeled-target'):
        cells = [str(v[key]) for v in evidence_map.values()] + [str(sum(v[key] for v in evidence_map.values()))]
        assert ' & ' + ' & '.join(cells) + r' \\' in evaluation_table, key
    inventory = list(csv.DictReader((MANUSCRIPT / 'generated/corpus-inventory.csv').open(encoding='utf-8')))
    assert {row['code'] for row in inventory} == set(inclusion['selected_ids'])
    for row in inventory:
        source = next(r for r in rows if r['code'] == row['code'])
        assert row['verification'] == source['verification_level']
        for field in ('pdf', 'bib', 'md'):
            original = {'pdf': 'pdf_sha256', 'bib': 'bibtex_sha256', 'md': 'markdown_sha256'}[field]
            assert row['source_'+field+'_sha256'] == source[original]
    cases = json.loads((MANUSCRIPT / 'data/within-study-comparisons.json').read_text(encoding='utf-8'))
    assert len(cases) == 7 and len({case['code'] for case in cases}) == 7
    by_code = {row['code']: row for row in rows}
    for case in cases:
        assert by_code[case['code']]['pdf_sha256'] == case['pdf_sha256']
        if args.sources:
            assert digest(REPOSITORY / by_code[case['code']]['pdf']) == case['pdf_sha256']
    supplement_log = (MANUSCRIPT / "supplement.log").read_text(encoding="utf-8", errors="replace")
    assert not re.search(r"undefined|Overfull|LaTeX Warning|Package .* Warning", supplement_log, re.IGNORECASE)
    supplement_info = subprocess.check_output(
        ["pdfinfo", str(MANUSCRIPT / "supplement.pdf")], text=True, encoding="utf-8", errors="replace"
    )
    supplement_pages = int(re.search(r"^Pages:\s+(\d+)", supplement_info, re.MULTILINE)[1])
    # Manuscript and evidence library share one repository; record the commit the
    # verified working tree is based on (the commit that adds this report follows it).
    base_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPOSITORY, text=True).strip()
    report = {
        "pages": pages,
        "corpus_prose_citations": len(corpus_keys),
        "indexed_library_count": len(all_rows),
        "internal_reference_ids": citation_policy['internal_reference_ids'],
        "foundational_exception_count": len(citation_policy['foundational_exceptions']),
        "citation_scope_sha256": text_digest(MANUSCRIPT / 'data/citation-scope.json'),
        "bibliography_entries": len(bibkeys),
        "resolved_bibliography_entries": len(resolved_keys),
        "unique_labels": len(labels),
        "figures": len(re.findall(r"\\begin\{figure\*?\}", all_tex)),
        "tables": len(re.findall(r"\\begin\{table\*?\}", all_tex)),
        "unresolved_references": sorted(ref_uses - set(labels) - {"S-" + ref for ref in external_refs}),
        "supplement_references": sorted("S-" + ref for ref in external_refs),
        "source_artifacts_checked": source_artifacts_checked,
        "local_fulltext_verification": "passed" if args.sources else "not-run; use --sources with local PDFs/transcriptions",
        "source_hash_mismatches": 0,
        "evaluation_denominator": len(technical_rows),
        "evaluation_attribute_counts": evaluation_counts,
        "evidence_map": evidence_map,
        "source_checked_numerical_cases": len(cases),
        "displayed_equations_unchanged": len(current_equations),
        "overfull_boxes": 0,
        "underfull_horizontal_boxes": log.count("Underfull \\hbox"),
        "underfull_vertical_boxes": log.count("Underfull \\vbox"),
        "pdf_sha256": digest(MANUSCRIPT / "survey.pdf"),
        "supplement": {
            "pages": supplement_pages,
            "unique_labels": len(supplement_labels),
            "figures": len(re.findall(r"\\begin\{figure\*?\}", supplement_tex)),
            "tables": len(re.findall(r"\\begin\{table\*?\}", supplement_tex)),
            "resolved_bibliography_entries": len(supplement_resolved),
            "unresolved_references": sorted(supplement_refs - set(supplement_labels)),
            "overfull_boxes": 0,
            "underfull_horizontal_boxes": supplement_log.count("Underfull \\hbox"),
            "underfull_vertical_boxes": supplement_log.count("Underfull \\vbox"),
            "pdf_sha256": digest(MANUSCRIPT / "supplement.pdf"),
        },
        "base_commit": base_commit,
    }
    (MANUSCRIPT / "revision/delivery-verification.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
