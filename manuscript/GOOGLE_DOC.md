# Manuscript (Google Docs)

The manuscript is authored and maintained in **Google Docs**. This repository holds supporting data and analysis files only.

## Primary manuscript

**[Multilocus Species-Tree Reconstruction Reveals Deep Lineage Structure in East African Dwarf Galagos (Paragalago)](https://docs.google.com/document/d/1pMebmT2tvqQMpEa4pEL9EHxDGD09J9KGDEMyW29rgm0/edit?usp=sharing)**

Direct edit link: `https://docs.google.com/document/d/1pMebmT2tvqQMpEa4pEL9EHxDGD09J9KGDEMyW29rgm0/edit`

## Section documents (Google Drive)

These section files also live on Google Drive and can be edited separately:

| Section | Local shortcut (Google Drive for Desktop) |
|---------|-------------------------------------------|
| Introduction | `G:\My Drive\Introduction.gdoc` |
| Methods summary | `G:\My Drive\METHODS SUMMARY.gdoc` |
| Results | `G:\My Drive\Results.gdoc` |
| Discussion | `G:\My Drive\Discussion.gdoc` |
| Acknowledgements | `G:\My Drive\Acknowledgements.gdoc` |
| Funding statement | `G:\My Drive\Funding Statement.gdoc` |

## Literature review (SciSpace)

Structured bibliography, topic syntheses, and simulated peer review for manuscript revision:

- [`literature_review/README.md`](literature_review/README.md) — start here
- [`literature_review/synthesis/meta_review.md`](literature_review/synthesis/meta_review.md) — revision checklist
- [`literature_review/combined/`](literature_review/combined/) — master bibliographies for Zotero import

## Related repository

StarBEAST3 analysis (now in this repo), QGIS layers, and additional manuscript markdown exports:

- [ulfboge/galagos](https://github.com/ulfboge/galagos) — `docs/publication/manuscript/`

## Update the direct link automatically

When the `.gdoc` placeholder is available locally (not cloud-only), run:

```powershell
.\scripts\update-manuscript-link.ps1
```

This reads the document ID from the Google Drive placeholder and updates the link in this file.
