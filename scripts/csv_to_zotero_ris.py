#!/usr/bin/env python3
"""Convert SciSpace combined CSV bibliography to RIS for Zotero import."""

import csv
import re
import sys
from pathlib import Path


def split_authors(raw: str) -> list[str]:
    if not raw or not raw.strip():
        return []
    parts = re.split(r"[\n,;]+", raw)
    return [p.strip() for p in parts if p.strip()]


def item_type(pub_type: str) -> str:
    t = (pub_type or "").lower()
    if "book" in t:
        return "BOOK"
    if "thesis" in t or "dissertation" in t:
        return "THES"
    if "conference" in t or "proceedings" in t:
        return "CONF"
    if "report" in t or "preprint" in t or "posted" in t:
        return "JOUR"
    return "JOUR"


def row_to_ris(row: dict) -> str:
    lines = [f"TY  - {item_type(row.get('Publication Type', ''))}"]
    title = (row.get("Paper Title") or "").strip()
    if title:
        lines.append(f"TI  - {title}")
    for author in split_authors(row.get("Author Names") or ""):
        lines.append(f"AU  - {author}")
    year = (row.get("Publication Year") or "").strip()
    if year:
        lines.append(f"PY  - {year}")
    journal = (row.get("Publication Title") or "").strip()
    if journal:
        lines.append(f"JO  - {journal}")
    doi = (row.get("DOI") or "").strip()
    if doi:
        lines.append(f"DO  - {doi}")
    url = (row.get("Paper Link") or row.get("PDF Link") or "").strip()
    if url:
        lines.append(f"UR  - {url}")
    abstract = (row.get("Abstract") or "").strip()
    if abstract:
        abstract = re.sub(r"\s+", " ", abstract)[:5000]
        lines.append(f"AB  - {abstract}")
    relevance = (row.get("Relevance") or "").strip()
    if relevance:
        note = re.sub(r"\s+", " ", relevance)[:2000]
        lines.append(f"N1  - {note}")
    lines.append("ER  - ")
    return "\n".join(lines)


def main() -> int:
    src = Path(
        sys.argv[1]
        if len(sys.argv) > 1
        else "manuscript/literature_review/combined/combined_galago_phylogenetics_comprehensive_review.csv"
    )
    if not src.is_file():
        print(f"Not found: {src}", file=sys.stderr)
        return 1

    rows = list(csv.DictReader(src.open(encoding="utf-8")))
    ris_path = src.with_suffix(".ris")
    doi_path = src.parent / "dois_for_zotero.txt"

    ris_blocks = [row_to_ris(r) for r in rows]
    ris_path.write_text("\n\n".join(ris_blocks) + "\n", encoding="utf-8")

    dois = sorted({(r.get("DOI") or "").strip() for r in rows if (r.get("DOI") or "").strip()})
    doi_path.write_text("\n".join(dois) + "\n", encoding="utf-8")

    print(f"Rows: {len(rows)}")
    print(f"Unique DOIs: {len(dois)}")
    print(f"Wrote: {ris_path}")
    print(f"Wrote: {doi_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
