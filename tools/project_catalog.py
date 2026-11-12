"""Validate the project directory and resolve exact publication identities."""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlsplit

CATALOG_PATH = "06-data/open-source-projects.json"


def url_identity(url: str) -> str:
    parsed = urlsplit(url)
    return (parsed.hostname or "").lower().removeprefix("www.") + parsed.path.rstrip("/").lower()


def _https(url: str) -> bool:
    parsed = urlsplit(url)
    return parsed.scheme == "https" and bool(parsed.hostname) and not parsed.username and not parsed.password


def validate(data: dict, entries=None) -> dict:
    """Reject broken facets, duplicate projects and unrelated paper links."""
    if data.get("schema_version") != 1:
        raise ValueError("Unsupported open-source project schema")
    for key in ("categories", "methods"):
        values = data[key]
        ids = [value["id"] for value in values]
        if len(ids) != len(set(ids)) or any(not v.get("name") or not v.get("name_en") for v in values):
            raise ValueError(f"Invalid project {key}")
    categories = {value["id"] for value in data["categories"]}
    methods = {value["id"] for value in data["methods"]}
    environments = set(data["environments"])
    seen = set()
    records = {entry.code: entry.row for entry in entries} if entries is not None else None
    for project in data["projects"]:
        code = project["id"]
        if not re.fullmatch(r"[a-z0-9_-]+", code) or code in seen:
            raise ValueError(f"Duplicate or invalid project id: {code}")
        seen.add(code)
        for key in ("name", "summary", "description", "algorithm_summary", "inputs", "outputs", "adaptation"):
            if not isinstance(project[key], str) or not project[key].strip():
                raise ValueError(f"Missing project field: {code}.{key}")
        if project["category"] not in categories:
            raise ValueError(f"Unknown project category: {code}")
        for key, allowed in (("methods", methods), ("environments", environments)):
            values = project[key]
            if not values or len(values) != len(set(values)) or not set(values) <= allowed:
                raise ValueError(f"Unknown or duplicate project {key}: {code}")
        if not project["algorithms"] or any(not isinstance(value, str) or not value for value in project["algorithms"]):
            raise ValueError(f"Missing project algorithms: {code}")
        if not _https(project["repository"]) or urlsplit(project["repository"]).hostname != "github.com":
            raise ValueError(f"Invalid project repository: {code}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", project["github"]["verified_on"]):
            raise ValueError(f"Missing repository verification date: {code}")
        for resource in project.get("resources", []):
            if not _https(resource["url"]):
                raise ValueError(f"Invalid project resource URL: {code}")
        for paper in project["papers"]:
            if not paper["title"] or not _https(paper["url"]):
                raise ValueError(f"Invalid project publication: {code}")
            if paper["year"] and not re.fullmatch(r"(?:19|20)\d{2}", paper["year"]):
                raise ValueError(f"Invalid publication year: {code}")
            for paper_code in paper["paper_codes"]:
                if records is None:
                    continue
                record = records.get(paper_code)
                if not record or record.get("view_group", "main") not in {"main", "surveys"}:
                    raise ValueError(f"Unknown active paper: {code}/{paper_code}")
                identities = {url_identity(record.get("official_url", ""))}
                if record.get("doi"):
                    identities.add(url_identity("https://doi.org/" + record["doi"]))
                if url_identity(paper["url"]) not in identities:
                    raise ValueError(f"Publication identity mismatch: {code}/{paper_code}")
    return data


def load(root: Path, entries=None) -> dict:
    path = root / CATALOG_PATH
    if not path.is_file():
        return {"schema_version": 1, "categories": [], "methods": [], "environments": [], "projects": []}
    return validate(json.loads(path.read_text(encoding="utf-8")), entries)


def markdown(data: dict, entries) -> str:
    """A portable English directory with no sibling-checkout dependency."""
    records = {entry.code: entry.row for entry in entries}
    methods = {value["id"]: value["name_en"] for value in data["methods"]}
    count = len(data["projects"])
    drl = sum("drl" in project["methods"] for project in data["projects"])
    linked = {code for project in data["projects"] for paper in project["papers"] for code in paper["paper_codes"]}
    lines = ["# Open-source robotics projects\n\n",
             f"{count} projects across six application areas, including {drl} projects with deep reinforcement learning methods. "
             f"{len(linked)} distinct publications link to reading files in the paper catalog. "
             "Project and publication counts are separate; multiple projects can cite the same paper.\n\n",
             "[Browse and compare projects](INDEX.html#view=projects) · [Paper catalog](INDEX.html) · "
             "[Library guide](README.md) · [Data and interface guide](06-data/index-interface.md)\n\n",
             "Search by project, algorithm or publication; filter by task, method, implementation environment and publication year. "
             "Compare up to four projects by algorithm, observations, outputs and R680 adaptation. "
             "The standalone HTML includes all project data and works without the textbook checkout or a server.\n\n",
             "Algorithms, runtime notes and platform limits are maintained in "
             "[open-source-projects.json](06-data/open-source-projects.json). "
             "The directory was adapted from [textbook chapter 54](" + data["source"]["url"] + "). "
             "Repository metadata is a dated GitHub snapshot; missing license metadata is left blank. "
             "A ROS 2 tag identifies an available implementation or linked integration; the detailed notes distinguish Humble, Foxy, Jazzy and Kilted. "
             "It does not establish R680 compatibility. Third-party code retains its own license.\n"]
    for category in data["categories"]:
        projects = [project for project in data["projects"] if project["category"] == category["id"]]
        if not projects:
            continue
        lines.append(f"\n## {category['name_en']} ({len(projects)})\n\n")
        lines.append("| Project | Algorithms | Implementation | Publications |\n|---|---|---|---|\n")
        for project in projects:
            references = []
            for paper in project["papers"]:
                links = [f"[{paper['title']}]({paper['url']})"]
                for code in paper["paper_codes"]:
                    record = records[code]
                    for key, label in (("pdf", "PDF"), ("markdown", "Full text")):
                        if record.get(key):
                            links.append(f"[{label}]({record[key]})")
                references.append(" · ".join(links))
            values = [f"[{project['name']}]({project['repository']})",
                      ", ".join(project["algorithms"]), ", ".join(project["environments"]), "<br>".join(references)]
            lines.append("| " + " | ".join(value.replace("|", "\\|") for value in values) + " |\n")
    lines.append("\nRegenerate this directory and the HTML with `python -m tools.build_indexes --strict`. "
                 "No paper source bytes, review decisions or survey selections are changed by project indexing.\n")
    return "".join(lines)
