# Manuscript (Google Docs)

The manuscript is authored and maintained in **Google Docs**. This repository holds supporting data and analysis files only.

## Primary manuscript

**[Multilocus Species-Tree Reconstruction Reveals Deep Lineage Structure in East African Dwarf Galagos (Paragalago)](https://drive.google.com/drive/search?q=Multilocus%20Species-Tree%20Reconstruction%20Paragalago)**

Open the search result titled *Multilocus Species-Tree Reconstruction Reveals Deep Lineage Structure in East African Dwarf Galagos (Paragalago)* in Google Drive, then use **Share → Copy link** to obtain a direct edit URL.

> **Tip:** Once you have the direct link (`https://docs.google.com/document/d/.../edit`), paste it into this file and commit so collaborators can open the doc in one click from GitHub.

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

## Related repository

Active StarBEAST3 analyses, QGIS layers, and manuscript markdown exports:

- [ulfboge/galagos](https://github.com/ulfboge/galagos) — `docs/publication/manuscript/`

## Update the direct link automatically

When the `.gdoc` placeholder is available locally (not cloud-only), run:

```powershell
.\scripts\update-manuscript-link.ps1
```

This reads the document ID from the Google Drive placeholder and updates the link in this file.
