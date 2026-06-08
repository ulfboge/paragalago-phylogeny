# StarBeast3 Analysis File Organization

**Last Updated**: 2026-06-08  
**Analysis**: Galagoides multispecies coalescent phylogenetic analysis using StarBeast3  
**Location**: `paragalago-phylogeny/phylogenetic_analyses/2025_galagoides_starbeast3/`

## Directory Structure

```
2025_galagoides_starbeast3/
├── config/                          # Configuration and state files
│   ├── Galago_StarBeast3_full.xml  # Main StarBeast3 XML configuration
│   └── Galago_StarBeast3_full.xml.state  # BEAST state file (resume point)
│
├── trees/                           # All tree files
│   ├── galago_full_MCC.tree        # Maximum Clade Credibility species tree
│   ├── galago_full.species.trees   # Posterior distribution of species trees
│   ├── 12S_speciesclean.trees      # Posterior gene trees for 12S
│   ├── 16S_speciesclean.trees      # Posterior gene trees for 16S
│   ├── CYTB_speciesclean.trees     # Posterior gene trees for CYTB
│   ├── IRBP_speciesclean.trees     # Posterior gene trees for IRBP
│   ├── vWFes28_speciesclean.trees  # Posterior gene trees for vWFes28
│   └── vWFin11_speciesclean.trees  # Posterior gene trees for vWFin11
│
├── logs/                            # Analysis logs and summaries
│   ├── galago_full.log             # MCMC chain log (main analysis)
│   ├── galago_full.txt             # Tracer summary statistics
│   └── galago_starbest3.txt        # Additional summary statistics
│
├── sequences/                       # Input sequence files
│   ├── 12S_speciesclean.fasta      # 12S aligned sequences
│   ├── 16S_speciesclean.fasta      # 16S aligned sequences
│   ├── CYTB_speciesclean.fasta     # CYTB aligned sequences
│   ├── IRBP_speciesclean.fasta     # IRBP aligned sequences
│   ├── vWFes28_speciesclean.fasta   # vWFes28 aligned sequences
│   ├── vWFin11_speciesclean.fasta  # vWFin11 aligned sequences
│   └── species_mapping.txt          # Sample to species mapping
│
├── visualizations/                  # Tree visualizations
│   ├── galago_full_MCC.tree.svg    # MCC tree visualization (SVG)
│   ├── galago_species_tree_cleaner.svg  # Species tree (SVG)
│   ├── galago_species_tree_cleaner.png   # Species tree (PNG)
│   └── galago_tree_FigTree_clean_subspecies.svg  # FigTree export
│
└── archive/                         # Test files and backups
    ├── Galago_StarBeast3_test.xml  # Test XML (early version)
    ├── Galago_StarBeast3_test_2.xml  # Test XML (second version)
    ├── Galago_StarBeast3_test.xml.state  # Test state file
    ├── starbeast3.log               # Test run log
    └── galago_full.zip              # Backup archive
```

## Active Files (Main Analysis)

### Configuration
- **XML**: `config/Galago_StarBeast3_full.xml`
  - StarBeast3 multispecies coalescent analysis
  - 6 loci: 12S, 16S, CYTB, IRBP, vWFes28, vWFin11
  - Includes LOOPY_GN_MalB and ZIT_GN_MalB (verified correct sequences)
  - Date: November 24, 2025

### Analysis Output
- **Log file**: `logs/galago_full.log`
  - MCMC chain log with parameter estimates
  - Contains: posterior, prior, likelihood, tree parameters, model parameters
  - Excellent convergence (ESS > 12,000 for key parameters)

- **Summary**: `logs/galago_full.txt`
  - Tracer summary statistics
  - ESS values, means, HPD intervals

### Tree Files
- **MCC Species Tree**: `trees/galago_full_MCC.tree`
  - Maximum Clade Credibility species tree
  - Generated from posterior species trees
  - Ready for visualization and interpretation

- **Posterior Species Trees**: `trees/galago_full.species.trees`
  - Full posterior distribution of species trees
  - Can be used for DensiTree visualization
  - Can generate additional summary trees

- **Gene Trees**: `trees/*_speciesclean.trees`
  - Posterior distributions for each locus
  - 6 separate gene tree files

### Input Sequences
- **FASTA Files**: `sequences/*_speciesclean.fasta`
  - Aligned sequences for each locus
  - Used as input for StarBeast3 analysis
  - All sequences verified correct

- **Species Mapping**: `sequences/species_mapping.txt`
  - Maps individual samples to species assignments
  - Used for species tree inference

## Analysis Details

### Model Configuration
- **Species Tree Model**: Multispecies Coalescent (StarBeast3)
- **Substitution Model**: HKY + Gamma (per locus)
- **Clock Model**: Relaxed clock (per locus)
- **Tree Prior**: Yule speciation model

### Convergence Status
✅ **Excellent Convergence**
- Posterior: ESS = 15,292
- Likelihood: ESS = 13,924
- Tree parameters: ESS > 16,000
- Most parameters: ESS > 12,000

### Sequence Verification
✅ **All sequences verified correct**
- ZIT_GN_MalB: Correct (starts with `TATGCTTAACC...`)
- LOOPY_GN_MalB: Correct (starts with `TATGCTTAACC...`)
- All other sequences match original source files

## File Locations Summary

| File Type | Location | Description |
|-----------|----------|-------------|
| **StarBeast3 XML** | `config/Galago_StarBeast3_full.xml` | Input configuration |
| **MCMC Log** | `logs/galago_full.log` | Parameter estimates |
| **Posterior Species Trees** | `trees/galago_full.species.trees` | All sampled species trees |
| **MCC Species Tree** | `trees/galago_full_MCC.tree` | Maximum clade credibility tree |
| **Gene Trees** | `trees/*_speciesclean.trees` | Per-locus posterior trees |
| **Input Sequences** | `sequences/*_speciesclean.fasta` | Aligned input sequences |
| **Species Mapping** | `sequences/species_mapping.txt` | Sample to species assignments |
| **Visualizations** | `visualizations/*.svg`, `visualizations/*.png` | Tree visualizations |

## Comparison with Invalid BEAST Analysis

This StarBeast3 analysis **replaces** the invalid BEAST analysis that had incorrect sequences:

| Aspect | Invalid BEAST | Valid StarBeast3 |
|--------|---------------|------------------|
| **Sequences** | ❌ 100% incorrect | ✅ Verified correct |
| **Convergence** | ✅ Good (but meaningless) | ✅ Excellent |
| **Model** | Single concatenated tree | Multispecies coalescent |
| **Loci** | 4 loci | 6 loci |
| **Status** | 🔴 INVALID | ✅ VALID |

## Next Steps

1. ✅ **Analysis Complete** - StarBeast3 run finished with excellent convergence
2. ✅ **MCC Tree Generated** - Ready for visualization
3. ✅ **Files Organized** - All files in proper structure
4. ⏳ **Visualization** - Create publication-quality figures
5. ⏳ **Interpretation** - Analyze species relationships and divergence times

## Notes

- All test files have been moved to `archive/`
- PDF references moved to `data/phylogenetic/references/`
- This analysis uses **correct sequences** (verified November 24, 2025)
- Convergence is excellent (ESS > 12,000 for key parameters)
- This is the **valid** analysis to use for publication

---

**Status**: ✅ **Analysis Complete - Files Organized**
