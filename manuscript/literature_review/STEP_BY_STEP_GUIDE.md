# Step-by-step guide — using the SciSpace literature review

**Manuscript:** *Multilocus Species-Tree Reconstruction Reveals Deep Lineage Structure in East African Dwarf Galagos (Paragalago)*  
**Canonical manuscript:** [Google Docs](https://docs.google.com/document/d/1pMebmT2tvqQMpEa4pEL9EHxDGD09J9KGDEMyW29rgm0/edit?usp=sharing)  
**This folder:** `manuscript/literature_review/`

Work through the phases below in order. Each phase has checkboxes you can tick off as you go.

---

## Phase 0 — Know what you have (5 minutes)

The SciSpace export contains **163 files** organised as follows:

| Folder | Files | What it is |
|--------|------:|------------|
| `synthesis/` | 12 | Readable summaries and simulated peer review — **start here for writing** |
| `combined/` | 2 | Master bibliographies — **start here for citations** |
| `searches/` | 91 | Raw search hits (SciSpace, Scholar, PubMed, etc.) |
| `paper_tables/` | 57 | Structured paper lists by subtopic |
| `manuscript_export/` | 1 | Snapshot of manuscript text used for the review |

Your analysis results (no re-run needed) live separately at:

`phylogenetic_analyses/2025_galagoides_starbeast3/`

---

## Phase 1 — Read the revision checklist (30–45 minutes)

**Goal:** Understand what the manuscript still needs before submission.

- [ ] Open [`synthesis/meta_review.md`](synthesis/meta_review.md)
- [ ] Read the Executive Summary and **Areas of Consensus Among Reviewers**
- [ ] Note the top issues all three simulated reviewers flagged:
  - [ ] Introduction and Discussion lack citations / literature positioning
  - [ ] Methods need stronger justification (loci, StarBEAST3, MCMC diagnostics)
  - [ ] Malawi populations (*first molecular data*) should be emphasised more
  - [ ] Add a conservation implications section
  - [ ] Add an explicit Limitations section (sample sizes, no absolute dating, etc.)
- [ ] Skim [`synthesis/novelty_report.md`](synthesis/novelty_report.md) — use this later for your cover letter and Discussion opening

**Optional deeper read:**

- [ ] [`synthesis/reviewer_1_report.md`](synthesis/reviewer_1_report.md) — methods & theory
- [ ] [`synthesis/reviewer_2_report.md`](synthesis/reviewer_2_report.md) — sample sizes & practical impact
- [ ] [`synthesis/reviewer_3_report.md`](synthesis/reviewer_3_report.md) — clarity & positioning

---

## Phase 2 — Import references into Zotero (45–90 minutes)

**Goal:** Build a working reference library from the combined bibliography.

**CSV is not a native Zotero import format.** Zotero accepts formats such as **RIS**, **BibTeX**, **BibLaTeX**, **CSL JSON**, **Zotero RDF**, and others — but not plain CSV. Use one of the options below instead.

The SciSpace CSV (`combined/combined_galago_phylogenetics_comprehensive_review.csv`) has **327 papers**, of which **242 have DOIs**.

Pre-generated import files (from the CSV):

| File | Format | Use |
|------|--------|-----|
| `combined/combined_galago_phylogenetics_comprehensive_review.ris` | **RIS** | **Recommended** — File → Import in Zotero |
| `combined/dois_for_zotero.txt` | DOI list | Bulk lookup via Add item by identifier |
| `combined/combined_galago_phylogenetics_comprehensive_review.csv` | CSV | Open in Excel to sort/filter; not for direct Zotero import |

To regenerate RIS/DOI files after editing the CSV:

```powershell
python scripts/csv_to_zotero_ris.py
```

### Step 2.1 — Choose your import method

**Option A — Import RIS file (recommended)**

- [ ] In Zotero: **File → Import…**
- [ ] Select:

  `combined/combined_galago_phylogenetics_comprehensive_review.ris`

- [ ] Import into a **new collection** named e.g. `Paragalago SciSpace 2026`
- [ ] Zotero creates items from the RIS metadata (title, authors, year, DOI, abstract, SciSpace relevance in notes)

**Option B — Bulk DOI lookup (best metadata quality)**

RIS import gives you basic fields. For **full publisher metadata** (volume, pages, journal abbreviations), let Zotero look up each DOI:

- [ ] Open `combined/dois_for_zotero.txt` (242 DOIs, one per line)
- [ ] In Zotero: click **Add item by identifier** (magic wand icon)
- [ ] Paste DOIs (you can paste many at once, separated by new lines)
- [ ] Zotero fetches complete records from Crossref/PubMed
- [ ] Repeat in batches if the dialog limits how many you can paste at once

**Option C — Shortlist only (20–30 key papers)**

- [ ] Open the CSV in Excel, sort by relevance
- [ ] Copy DOIs for your top picks into Zotero's **Add item by identifier**
- [ ] Add remaining papers manually as you cite them

**Option D — BibTeX from SciSpace / Google Scholar**

If you prefer BibTeX (also a native Zotero format):

- [ ] Export individual papers or collections from SciSpace or Google Scholar as **BibTeX**
- [ ] In Zotero: **File → Import…** → select the `.bib` file

### Step 2.2 — After import

- [ ] Select imported items → right-click → **Find Available PDF** (if Unpaywall or similar is configured)
- [ ] Create sub-collections:
  - `Introduction — systematics`
  - `Methods — coalescent`
  - `Discussion — biogeography`
  - `Discussion — conservation`
- [ ] Tag high-priority papers: `must-cite`, `Pozzi`, `Malawi`
- [ ] For the **85 papers without DOI** in the CSV: add manually when you cite them, or search by title in Zotero

### Zotero formats reference

Native import formats include: Zotero RDF, CSL JSON, BibTeX, BibLaTeX, **RIS**, Endnote XML, PubMed XML, MEDLINE/nbib, and others. **CSV is not listed** — always convert to RIS/BibTeX first, or use DOI lookup.

### If import gives incomplete records

- [ ] Select items with DOIs → right-click → **Update metadata** (or re-import via Option B)
- [ ] Fix author names manually for key papers (SciSpace sometimes exports authors on one line)

---

## Phase 3 — Revise the Introduction (1–2 hours)

**Goal:** Position the study in existing *Paragalago* and galago systematics literature.

- [ ] Open the Google Doc manuscript
- [ ] Open [`synthesis/insights_q2_galago_systematics.md`](synthesis/insights_q2_galago_systematics.md) side by side
- [ ] For each paragraph in the Introduction, add citations for:
  - [ ] Polyphyly of *Galagoides* / establishment of *Paragalago* (Masters et al. 2017; Pozzi et al. 2014)
  - [ ] *P. zanzibaricus* complex cryptic diversity (Pozzi et al. 2020; Génin 2021)
  - [ ] Malawi sampling gap (Karlsson 2006, 2009, 2011 — your own prior work)
  - [ ] Acoustic vs molecular discordance where relevant
- [ ] Pull specific papers from Zotero or `searches/galago_systematics/` and `paper_tables/taxonomy/`
- [ ] Add one clear sentence: this study provides the **first molecular data from Malawi dwarf galagos**

**Cross-check:**

- [ ] [`synthesis/meta_review.md`](synthesis/meta_review.md) — Introduction / positioning items

---

## Phase 4 — Strengthen the Methods (1–2 hours)

**Goal:** Justify StarBEAST3, locus choice, and report diagnostics.

- [ ] Open [`synthesis/insights_q1_coalescent_methods.md`](synthesis/insights_q1_coalescent_methods.md)
- [ ] Add or expand text on:
  - [ ] Why multispecies coalescent (vs concatenation) for recently diverged lineages
  - [ ] Why StarBEAST3 specifically (joint gene-tree / species-tree co-estimation)
  - [ ] Why this six-locus panel (3 mtDNA + 3 nuclear)
- [ ] Cite from `paper_tables/best_practice/` and `paper_tables/multispecies_coalescent/`
- [ ] Report MCMC diagnostics from your completed run:
  - [ ] Log file: `phylogenetic_analyses/2025_galagoides_starbeast3/logs/galago_full.log`
  - [ ] Summary: `phylogenetic_analyses/2025_galagoides_starbeast3/logs/galago_full.txt`
  - [ ] State ESS values (e.g. posterior ESS > 12,000), burn-in (10%), chain length (200M)
- [ ] Open [`synthesis/insights_q4_molecular_markers.md`](synthesis/insights_q4_molecular_markers.md) for marker-choice citations

**Optional methods addition (reviewers asked for):**

- [ ] Mention why concatenated analysis was not used, or add brief comparison
- [ ] Note absence of introgression testing as a limitation (see Phase 6)

---

## Phase 5 — Expand Discussion (2–3 hours)

**Goal:** Connect your four lineages to biogeography and conservation.

### 5A — Biogeography

- [ ] Open [`synthesis/insights_q3_biogeography.md`](synthesis/insights_q3_biogeography.md)
- [ ] Link your lineages to:
  - [ ] Eastern Arc montane refugia
  - [ ] Coastal forest fragmentation
  - [ ] Island–mainland (Zanzibar vs Udzungwa) divergence
  - [ ] Southern Malawi / miombo–montane context for the Malawi lineage
- [ ] Use `paper_tables/phylogeography/` and `paper_tables/biogeographic/` for citations

### 5B — Conservation

- [ ] Open [`synthesis/insights_q5_conservation_genetics.md`](synthesis/insights_q5_conservation_genetics.md)
- [ ] Add a short **Conservation implications** subsection:
  - [ ] Four distinct lineages = four conservation units
  - [ ] Malawi lineage taxonomic uncertainty → precautionary protection
  - [ ] Fragmented coastal and Eastern Arc forests
- [ ] Use `searches/conservation/` and `paper_tables/conservation/`

### 5C — Taxonomy

- [ ] Keep Malawi label as *Paragalago* cf. *granti*/*nyasae* (reviewers supported this)
- [ ] Cite why formal naming is premature (no *P. granti* sequences, type locality issues)
- [ ] Use `paper_tables/taxonomy/`

---

## Phase 6 — Add Limitations and novelty statement (30–60 minutes)

- [ ] Open [`synthesis/meta_review.md`](synthesis/meta_review.md) — Limitations section
- [ ] Add a dedicated **Limitations** paragraph covering:
  - [ ] Small Malawi sample size (*n* = 2)
  - [ ] No fossil or secondary calibration → relative branch lengths only (no absolute dates)
  - [ ] No formal introgression or gene-flow testing
  - [ ] Incomplete taxon sampling (e.g. *P. cocos*, *P. granti*, *P. orinus* not included)
- [ ] Open [`synthesis/novelty_report.md`](synthesis/novelty_report.md)
- [ ] Ensure Abstract and Discussion opening state three contributions:
  1. First molecular characterisation of Malawi populations
  2. StarBEAST3 MSC analysis with verified six-locus dataset
  3. Biogeographic and conservation synthesis for fragmented East African forests

---

## Phase 7 — Figures and results cross-check (30 minutes)

Your analysis is **complete** — do not re-run BEAST unless you change data or model.

- [ ] MCC tree for figures: `phylogenetic_analyses/2025_galagoides_starbeast3/trees/galago_full_MCC.tree`
- [ ] Existing SVGs: `phylogenetic_analyses/2025_galagoides_starbeast3/visualizations/`
- [ ] Confirm figure caption matches [`phylogenetic_analyses/2025_galagoides_starbeast3/trees/MCC_TREE_ANNOTATIONS_EXPLAINED.md`](../../phylogenetic_analyses/2025_galagoides_starbeast3/trees/MCC_TREE_ANNOTATIONS_EXPLAINED.md)
- [ ] Ensure Results reports sample sizes per lineage and locus

---

## Phase 8 — Final citation sweep (1 hour)

- [ ] Open Google Doc + Zotero side by side (Zotero connector or drag-and-drop citations)
- [ ] Go section by section: every factual claim in Introduction and Discussion should have a citation
- [ ] Check you have cited at minimum:
  - [ ] Pozzi et al. 2014, 2020
  - [ ] Masters et al. 2017
  - [ ] Douglas & Bouckaert 2022 (StarBEAST3) or equivalent MSC methods paper
  - [ ] Your Karlsson Malawi field reports
  - [ ] Key Eastern Arc biogeography papers from `insights_q3_biogeography.md`
- [ ] Generate bibliography from Zotero in your target journal format

**Extra resource (older AI review, galagos repo):**

If you need section-specific citation suggestions not in this export:

`galagos/docs/publication/ai_reviews/ai_manuscript_feedback/REVISION_GUIDE_AND_REFERENCES.md`

---

## Phase 9 — Pre-submission checklist

- [ ] All simulated reviewer critical items from `meta_review.md` addressed or explicitly discussed in Limitations
- [ ] Ethics / sampling statement (pet animals, permits) included if applicable
- [ ] Data availability statement (GenBank accessions, alignment availability)
- [ ] Supplementary: alignments, species mapping, BEAST XML optional
- [ ] Cover letter draws on `novelty_report.md` (Malawi first, MSC methods, conservation relevance)
- [ ] Co-authors have reviewed final Google Doc

---

## Quick reference — which file for which task

| Task | File |
|------|------|
| What to fix first | `synthesis/meta_review.md` |
| Cover letter / novelty | `synthesis/novelty_report.md` |
| Introduction citations | `synthesis/insights_q2_galago_systematics.md` |
| Methods (StarBEAST3) | `synthesis/insights_q1_coalescent_methods.md` |
| Methods (markers) | `synthesis/insights_q4_molecular_markers.md` |
| Discussion (biogeography) | `synthesis/insights_q3_biogeography.md` |
| Discussion (conservation) | `synthesis/insights_q5_conservation_genetics.md` |
| Import to Zotero | `combined/combined_galago_phylogenetics_comprehensive_review.ris` (or `dois_for_zotero.txt`) |
| Deep dive one topic | `paper_tables/<subtopic>/` |
| Trace a search hit | `searches/<topic>/` |
| Phylogeny figures | `phylogenetic_analyses/2025_galagoides_starbeast3/` |

---

## Estimated total time

| Phase | Time |
|-------|------|
| 0 — Orientation | 5 min |
| 1 — Read checklist | 30–45 min |
| 2 — Zotero import | 45–90 min |
| 3 — Introduction | 1–2 h |
| 4 — Methods | 1–2 h |
| 5 — Discussion | 2–3 h |
| 6 — Limitations | 30–60 min |
| 7 — Figures check | 30 min |
| 8 — Citation sweep | 1 h |
| 9 — Pre-submission | 1–2 h |
| **Total** | **~8–12 hours** (can split across several sessions) |

---

*Simulated SciSpace reviews are a self-audit tool, not real journal peer review. Always verify citations and relevance before including papers.*
