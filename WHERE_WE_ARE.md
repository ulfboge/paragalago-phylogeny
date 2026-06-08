# Where we are — Paragalago phylogeny project

**Last updated:** 8 June 2026  
**Open this folder in Cursor:** `C:\Users\galag\GitHub\paragalago-phylogeny`  
**GitHub:** https://github.com/ulfboge/paragalago-phylogeny

This file is the handover note for resuming work. The manuscript lives in Google Docs; this repo holds supporting data, links, and documentation.

---

## Manuscript (canonical source)

**Title:** *Multilocus Species-Tree Reconstruction Reveals Deep Lineage Structure in East African Dwarf Galagos (Paragalago)*

**Authors:** Johan Karlsson, Andrew Perkin, Cristiano Vernesi, Simon K. Bearder

**Edit in Google Docs:**  
https://docs.google.com/document/d/1pMebmT2tvqQMpEa4pEL9EHxDGD09J9KGDEMyW29rgm0/edit?usp=sharing

Section `.gdoc` files on Google Drive (root of `G:\My Drive\`): Introduction, METHODS SUMMARY, Results, Discussion, Acknowledgements, Funding Statement.

SciSpace literature review: [`manuscript/literature_review/STEP_BY_STEP_GUIDE.md`](manuscript/literature_review/STEP_BY_STEP_GUIDE.md) (workflow) · [`manuscript/literature_review/`](manuscript/literature_review/) (files). Additional markdown exports live in the related **galagos** repo (see below).

---

## Analysis status

### Valid analysis to use (StarBEAST3) — COMPLETE

The publication-ready multispecies coalescent analysis is **finished** with excellent convergence (ESS > 12,000 for key parameters). It uses **verified correct sequences** (Nov 2025).

**Location (in this repo):**

```
phylogenetic_analyses\2025_galagoides_starbeast3\
```

| What | Path |
|------|------|
| **BEAST XML (load this to re-run)** | `phylogenetic_analyses\2025_galagoides_starbeast3\config\Galago_StarBeast3_full.xml` |
| Resume state | `phylogenetic_analyses\2025_galagoides_starbeast3\config\Galago_StarBeast3_full.xml.state` |
| MCMC log (Tracer) | `phylogenetic_analyses\2025_galagoides_starbeast3\logs\galago_full.log` |
| Posterior species trees | `phylogenetic_analyses\2025_galagoides_starbeast3\trees\galago_full.species.trees` |
| **MCC tree (figures)** | `phylogenetic_analyses\2025_galagoides_starbeast3\trees\galago_full_MCC.tree` |
| Input FASTAs (6 loci) | `phylogenetic_analyses\2025_galagoides_starbeast3\sequences\*_speciesclean.fasta` |
| Species mapping | `phylogenetic_analyses\2025_galagoides_starbeast3\sequences\species_mapping.txt` |
| Tree docs | `phylogenetic_analyses\2025_galagoides_starbeast3\trees\TREE_FILES_EXPLANATION.md`, `MCC_TREE_ANNOTATIONS_EXPLAINED.md` |
| Full file index | `phylogenetic_analyses\2025_galagoides_starbeast3\FILE_ORGANIZATION.md` |

**Model:** StarBEAST3 in BEAST 2.7.8 · 6 loci (12S, 16S, CYTB, IRBP, vWF es28, vWF in11) · HKY+Γ per locus · relaxed clock · Yule speciation.

**Main result:** Four ingroup lineages — *P. z. zanzibaricus*, *P. z. udzungwensis*, *P. rondoensis*, and Malawi *Paragalago cf. granti/nyasae* — all nodes ≥ 0.9998 posterior support.

### Older / invalid work — do not use for publication

- An earlier concatenated BEAST run had **incorrect sequences** (documented in galagos repo `NEXT_STEPS.md`).
- **Legacy RevBayes** work (~2016) was removed from this repo; originals remain on OneDrive (`RevBayes\` migration folder).
- **Legacy vocal manuscript** in `legacy_manuscripts\` is a separate acoustic project, not the genetic phylogeny paper.

---

## BEAST software on this machine

| Path | What it is |
|------|------------|
| `C:\Users\galag\BEAST.v2.7.7.Windows\BEAST\` | Windows BEAST 2.7.7 installer (use this for `beast`, `beauti`, etc.) |
| `C:\Users\galag\BEAST\2.7\` | BEAST packages only (2.7.8 + starbeast3 add-on) — no `.exe` launchers |

**To re-run the analysis:**

1. Open **BEAST** from the Windows install (`BEAST.v2.7.7.Windows`).
2. **File → Load** → `phylogenetic_analyses\2025_galagoides_starbeast3\config\Galago_StarBeast3_full.xml`
3. Run (or Resume if `.state` exists).
4. Check convergence: **Tracer** → `galago_full.log`
5. Summarize trees: **TreeAnnotator** on `galago_full.species.trees` → MCC tree

---

## This repository (`paragalago-phylogeny`)

Consolidated archive copied from `G:\My Drive\OneDrive_Migration\Phylogeny` (June 2026). ~2.5 GB on disk; only docs and small files are in git.

```
C:\Users\galag\GitHub\paragalago-phylogeny\
├── WHERE_WE_ARE.md          ← you are here
├── README.md
├── DATA_LAYOUT.md
├── manuscript/              Google Docs links
├── sequences/               [local] multilocus alignments
├── phylogenetic_analyses/   StarBEAST3 analysis + BEAST tutorial
├── sampling_and_metadata/   [local] Excel sheets, Malawi field data
├── spatial_data/            [local] QGIS + KMZ maps
├── grants_and_reports/      grant PDFs/DOCs (in git)
├── legacy_manuscripts/      [local] old vocal manuscript
└── project_notes/           workflow, primers, EndNote
```

---

## Related repository (active analysis + manuscript exports)

```
C:\Users\galag\GitHub\jobb-ansökningar\research\galagos\
```

- GitHub: https://github.com/ulfboge/galagos  
- Manuscript markdown: `docs\publication\manuscript\`  
- Session notes: `docs\project\SESSION_SUMMARY_2026-01-19.md`  
- StarBEAST3 analysis moved here (June 2026): `phylogenetic_analyses\2025_galagoides_starbeast3\`

---

## Original data sources (OneDrive / Google Drive)

| Content | Path |
|---------|------|
| Migration archive | `G:\My Drive\OneDrive_Migration\Phylogeny\` |
| RevBayes (2016) | `G:\My Drive\OneDrive_Migration\RevBayes\` |
| Manuscript `.gdoc` | `G:\My Drive\Multilocus Species-Tree Reconstruction Reveals Deep Lineage Structure in East African Dwarf Galagos (Paragalago).gdoc` |

---

## Likely next steps

1. **Manuscript** — continue editing in Google Docs; use `manuscript\literature_review\synthesis\meta_review.md` as a revision checklist; export figures from `galago_full_MCC.tree` / `visualizations\` when needed.
2. **Figures** — review SVG/PNG in `2025_galagoides_starbeast3\visualizations\`.
3. **Submission prep** — data availability statement, GenBank accessions, supplementary alignments.
4. **Commit docs** — `FILE_ORGANIZATION.md` and tree explanation markdown are tracked in git; MCMC logs/trees/FASTAs stay gitignored.

---

## Quick commands

```powershell
# Open this project in Cursor (from any terminal)
cursor "C:\Users\galag\GitHub\paragalago-phylogeny"

# Jump to the StarBEAST3 analysis
cd "C:\Users\galag\GitHub\paragalago-phylogeny\phylogenetic_analyses\2025_galagoides_starbeast3"
```
