# Paragalago genetic phylogeny

Supporting data archive for:

**Multilocus Species-Tree Reconstruction Reveals Deep Lineage Structure in East African Dwarf Galagos (Paragalago)**

Authors: Johan Karlsson, Andrew Perkin, Cristiano Vernesi, Simon K. Bearder

---

## Manuscript (Google Docs)

The manuscript is maintained in **Google Docs** — not as a file in this repository.

**[Open manuscript in Google Docs →](https://docs.google.com/document/d/1pMebmT2tvqQMpEa4pEL9EHxDGD09J9KGDEMyW29rgm0/edit?usp=sharing)**

Section documents and notes: [`manuscript/GOOGLE_DOC.md`](manuscript/GOOGLE_DOC.md)

Related active work (StarBEAST3, QGIS, markdown exports): [github.com/ulfboge/galagos](https://github.com/ulfboge/galagos)

---

## Repository contents

| Folder | Description |
|--------|-------------|
| [`manuscript/`](manuscript/) | Google Docs links and manuscript metadata |
| [`sequences/`](sequences/) | Multilocus alignments (local; gitignored) |
| [`phylogenetic_analyses/`](phylogenetic_analyses/) | RevBayes and BEAST analyses (mostly local) |
| [`sampling_and_metadata/`](sampling_and_metadata/) | Field sampling spreadsheets and metadata |
| [`spatial_data/`](spatial_data/) | QGIS projects and survey maps (local) |
| [`grants_and_reports/`](grants_and_reports/) | Grant applications and preliminary reports |
| [`legacy_manuscripts/`](legacy_manuscripts/) | Earlier Galagoides vocal-analysis draft (local) |
| [`project_notes/`](project_notes/) | Workflow and primer documentation |

Full layout: [`DATA_LAYOUT.md`](DATA_LAYOUT.md)

---

## Clone and use locally

```powershell
git clone https://github.com/ulfboge/paragalago-phylogeny.git
cd paragalago-phylogeny
```

Large data folders are gitignored. If you need the full local archive (~2.5 GB), copy from the organized folder on disk or restore from Google Drive / OneDrive migration sources listed in `DATA_LAYOUT.md`.

To resolve a direct Google Docs edit link when the `.gdoc` file is synced locally:

```powershell
.\scripts\update-manuscript-link.ps1
```

---

## Loci

Mitochondrial: 12S, 16S, CYTB  
Nuclear: IRBP, vWF intron 11, vWF exon 28  
Framework: multispecies coalescent (StarBEAST3)
