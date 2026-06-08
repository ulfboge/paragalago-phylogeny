# Data layout

Local archive of supporting materials for the Paragalago multilocus phylogeny manuscript. Large binary folders are kept on disk but excluded from git (see `.gitignore`).

```
paragalago-phylogeny/
├── manuscript/              # Google Docs links + SciSpace literature review
│   └── literature_review/   # SciSpace search exports, synthesis, simulated peer review
├── sequences/               # Alignments (12S, 16S, cytB, IRBP, vWF) [local only]
├── phylogenetic_analyses/
│   ├── 2025_galagoides_starbeast3/  # Publication StarBEAST3 run (outputs local only)
│   └── divergence_dating/           # BEAST primates divergence-dating tutorial run
├── sampling_and_metadata/   # Excel sampling sheets, cytB nexus, Malawi field data [mostly local only]
├── spatial_data/            # QGIS project, sample locations, survey KMZ maps [local only]
├── grants_and_reports/      # Grant applications and preliminary reports [in git]
├── legacy_manuscripts/      # Older Galagoides vocal-analysis manuscript [local only]
└── project_notes/           # Workflow, primer notes, EndNote library [mostly local only]
```

## Source locations (OneDrive / Google Drive migration)

| Content | Original path |
|---------|---------------|
| Sequences | `G:\My Drive\OneDrive_Migration\Phylogeny\` |
| Legacy RevBayes (2016) | `G:\My Drive\OneDrive_Migration\RevBayes\` |
| Manuscript (Google Docs) | `G:\My Drive\Multilocus Species-Tree Reconstruction... (Paragalago).gdoc` |
| Manuscript markdown exports | `C:\Users\galag\GitHub\jobb-ansökningar\research\galagos\` |

## In git vs local only

**Tracked in git:** README, documentation, grant PDFs/DOCs, workflow notes, folder structure.

**Local only (gitignored):** sequence alignments, MCMC logs/trees, Malawi media (~2 GB), spatial layers, EndNote PDF library.
