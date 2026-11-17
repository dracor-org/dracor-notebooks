"""Generate the status badges and the status table of the DraCor Notebooks.

Reads status/notebooks.csv (the notebooks) and status/results.csv (the test
results per notebook and server) and writes

- status/badges/<folder>.<server>.json: one shields.io endpoint badge per
  notebook and server (https://shields.io/badges/endpoint-badge),
- status/table.md: the status table, included in the start page of the book,
- the same table into README.md, between the markers
  <!-- status-table-start --> and <!-- status-table-end -->.

Run from the root of the repository after updating status/results.csv:

    python status/make_badges.py

Only the standard library is needed.
"""
import csv
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
STATUS = ROOT / "status"
RAW = "https://raw.githubusercontent.com/dracor-org/dracor-notebooks/main/status/badges"
DETAILS = "https://dracor-org.github.io/dracor-notebooks/appendix/tested-environments.html"
REPO = "https://github.com/dracor-org/dracor-notebooks/tree/main"
SERVERS = {"production": "dracor.org", "staging": "staging"}

# result: (text, colour)
RESULTS = {
    "runs": ("runs", "brightgreen"),
    "partial": ("partly runs", "yellow"),
    "fails": ("fails", "red"),
    "legacy": ("runs on API v0 (deprecated)", "orange"),
    "untested": ("not tested", "lightgrey"),
}


def badge(row):
    text, colour = RESULTS[row["result"]]
    if row["result"] == "partial" and row["detail"]:
        text = row["detail"]
    if row["date"]:
        text = f"{text} · {row['date']}"
    version = "v0 " + row["api_version"] if row["result"] == "legacy" else row["api_version"]
    return {"schemaVersion": 1,
            "label": f"{SERVERS[row['server']]} API {version}",
            "message": text,
            "color": colour}


def badge_markdown(folder, server):
    url = f"{RAW}/{folder}.{server}.json"
    alt = f"Status on {SERVERS[server]}"
    return f"[![{alt}](https://img.shields.io/endpoint?url={quote(url, safe='')})]({DETAILS})"


def main():
    notebooks = list(csv.DictReader(open(STATUS / "notebooks.csv", encoding="utf-8")))
    results = list(csv.DictReader(open(STATUS / "results.csv", encoding="utf-8")))

    (STATUS / "badges").mkdir(exist_ok=True)
    for row in results:
        path = STATUS / "badges" / f"{row['folder']}.{row['server']}.json"
        path.write_text(json.dumps(badge(row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = ["| Notebook | Authors | dracor.org | staging (next release) |",
             "|---|---|---|---|"]
    for nb in notebooks:
        lines.append(f"| [{nb['title']}]({REPO}/{nb['folder']}) | {nb['authors']} | "
                     f"{badge_markdown(nb['folder'], 'production')} | {badge_markdown(nb['folder'], 'staging')} |")
    table = "\n".join(lines) + "\n"
    (STATUS / "table.md").write_text(table, encoding="utf-8")

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    start, end = "<!-- status-table-start -->", "<!-- status-table-end -->"
    if start in text and end in text:
        before, rest = text.split(start, 1)
        _, after = rest.split(end, 1)
        readme.write_text(f"{before}{start}\n{table}{end}{after}", encoding="utf-8")
    print(f"{len(results)} badges, table with {len(notebooks)} notebooks")


if __name__ == "__main__":
    main()
