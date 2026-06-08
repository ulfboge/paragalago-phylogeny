# SciSpace literature review — Paragalago manuscript

**Generated:** June 2026 (SciSpace Deep Review export)  
**Manuscript:** *Multilocus Species-Tree Reconstruction Reveals Deep Lineage Structure in East African Dwarf Galagos (Paragalago)*

This folder holds a structured literature search, synthesis, and simulated peer review produced in SciSpace to support manuscript revision and citation building. The canonical manuscript remains in [Google Docs](../GOOGLE_DOC.md).

---

## Start here

| Priority | File | Use for |
|----------|------|---------|
| 1 | [`synthesis/meta_review.md`](synthesis/meta_review.md) | Editorial overview — consensus reviewer concerns and revision priorities |
| 2 | [`synthesis/novelty_report.md`](synthesis/novelty_report.md) | Positioning the paper — what is novel vs prior galago work |
| 3 | [`synthesis/insights_q2_galago_systematics.md`](synthesis/insights_q2_galago_systematics.md) | Introduction & Discussion framing for *Paragalago* taxonomy |
| 4 | [`synthesis/insights_q1_coalescent_methods.md`](synthesis/insights_q1_coalescent_methods.md) | Methods justification — StarBEAST3 vs alternatives |
| 5 | [`combined/combined_galago_phylogenetics_comprehensive_review.csv`](combined/combined_galago_phylogenetics_comprehensive_review.csv) | Master bibliography with relevance scores — import to Zotero |

---

## Folder layout

```
literature_review/
├── README.md                 ← you are here
├── manuscript_export/        Snapshot of manuscript text used for the review
├── synthesis/                AI-written summaries and simulated peer review
├── combined/                 Deduplicated master bibliographies (start here for citations)
├── searches/                 Raw search results by topic and database
│   ├── coalescent_methods/
│   ├── galago_systematics/
│   ├── biogeography_phylogeography/
│   ├── conservation/
│   ├── molecular_markers/
│   └── phylogenetics_general/
└── paper_tables/             SciSpace structured paper extractions by subtopic
    ├── best_practice/
    ├── biogeographic/
    ├── multispecies_coalescent/
    ├── phylogeography/
    ├── taxonomy/
    └── ...
```

### `synthesis/` (12 files)

| File | Content |
|------|---------|
| `meta_review.md` | Combined editorial decision and cross-reviewer themes |
| `novelty_report.md` | Short novelty and impact assessment |
| `novelty_analysis_comprehensive.md` | Extended novelty analysis |
| `reviewer_1_report.md` | Simulated review — methods & theory |
| `reviewer_2_report.md` | Simulated review — experiments & practical impact |
| `reviewer_3_report.md` | Simulated review — clarity & positioning |
| `insights_q1_coalescent_methods.md` | MSC / StarBEAST3 methods literature synthesis |
| `insights_q2_galago_systematics.md` | Galago taxonomy and phylogenetics synthesis |
| `insights_q3_biogeography.md` | Eastern Arc / coastal forest biogeography synthesis |
| `insights_q4_molecular_markers.md` | Marker choice and locus panel literature |
| `insights_q5_conservation_genetics.md` | Conservation genetics and threatened primates |
| `bibliographic_info.md` | Manuscript metadata used for the review |

### `combined/` (2 files)

Deduplicated CSV bibliographies merging SciSpace, Google Scholar, PubMed, arXiv, Zotero, and library searches. Columns typically include title, authors, DOI, PDF link, relevance score, and abstract snippet. **Use these for citation picking**, not the raw `searches/` files.

### `searches/` (91 files)

Raw exports per database (`scispace_*`, `scholar_*`, `pubmed_*`, `arxiv_*`, `zotero_*`, `library_*`). Useful for tracing where a reference was found or re-running a narrower search.

### `paper_tables/` (57 files)

SciSpace agent outputs — structured tables of papers grouped by review question (e.g. `paper_table_phylogeograph_*`, `paper_table_taxonomic-sta_*`). Good for deep-diving one subtopic when writing a specific paragraph.

---

## How to use this material

### 1. Manuscript revision (highest value)

Work through `synthesis/meta_review.md` as a revision checklist. All three simulated reviewers flagged:

- **Citations** — Introduction and Discussion need much stronger literature positioning
- **Methods** — justify locus choice, StarBEAST3, and report MCMC diagnostics
- **Malawi lineage** — emphasise first molecular data from southern Malawi
- **Conservation** — add explicit conservation implications section
- **Limitations** — sample sizes (especially Malawi *n*=2), no absolute dating, no introgression tests

Cross-reference `insights_q*.md` files when rewriting each section.

### 2. Building the reference list

1. Open `combined/combined_galago_phylogenetics_comprehensive_review.csv` in Excel or import to Zotero.
2. Sort by relevance score; filter for papers not already in your library.
3. For section-specific gaps, use the matching `insights_q*.md` (cited inline as `[1]`, `[2]`, …) and pull DOIs from the linked `searches/` or `paper_tables/` files.
4. Key papers repeatedly flagged for *Paragalago* work: Pozzi et al. (2014, 2020), Masters et al. (2017), Génin (2021), Karlsson field reports.

### 3. Methods section support

`insights_q1_coalescent_methods.md` provides ready-made prose on when to use StarBEAST3 vs ASTRAL/BPP/*BEAST and best-practice bullets (locus filtering, convergence, introgression checks). `paper_tables/best_practice/` and `paper_tables/multispecies_coalescent/` hold primary sources.

### 4. Discussion / biogeography

`insights_q3_biogeography.md` synthesises Eastern Arc refugia, Pleistocene fragmentation, and coastal forest barriers — directly relevant to interpreting your four ingroup lineages. Pair with `paper_tables/phylogeography/` and `paper_tables/biogeographic/`.

### 5. Conservation framing

`insights_q5_conservation_genetics.md` plus `searches/conservation/` support a conservation genetics paragraph linking lineage diversity to forest fragment prioritisation.

### 6. Response to reviewers (if submitted)

`synthesis/reviewer_*.md` anticipate likely reviewer comments. Use them as a pre-submission checklist or draft point-by-point responses.

---

## Related material elsewhere

| Location | What |
|----------|------|
| [Google Docs manuscript](../GOOGLE_DOC.md) | Canonical editable manuscript |
| `galagos` repo → `docs/publication/ai_reviews/ai_manuscript_feedback/` | Earlier AI review pass including `REVISION_GUIDE_AND_REFERENCES.md` and `citation_recommendations_by_section.md` |
| `phylogenetic_analyses/2025_galagoides_starbeast3/` | StarBEAST3 analysis outputs |

---

## Notes

- Simulated reviews are **not real peer review** — use as a structured self-audit, not as journal feedback.
- Relevance scores in combined CSVs are SciSpace estimates; verify fit before citing.
- The `manuscript_export/` snapshot may lag behind the live Google Doc; always edit the Google Doc as source of truth.
