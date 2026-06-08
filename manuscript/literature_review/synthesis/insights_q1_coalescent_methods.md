## TL;DR

StarBeast3 is currently the fastest practical Bayesian full‑MSC co‑estimator for moderate genome-scale datasets (tens–low hundreds of loci), trading heavy computation for joint inference of gene trees, species trees, and time parameters. Summary methods (ASTRAL and variants) and targeted Bayesian tools (BPP, *BEAST family) remain preferable for very large taxon or gene counts or when quick topology inference is required.

----

## When to use Bayesian coalescent

StarBeast3 and related full‑likelihood MSC approaches are recommended when joint estimation of gene trees, species tree topology, divergence times, and population parameters is required and when the dataset size is within computationally feasible bounds. These methods directly use sequence data (reducing gene tree estimation error biases) and can incorporate relaxed clocks and tip dates for aDNA or calibrated analyses.

- **StarBeast3 strengths** include adaptive operators, parallelised gene‑tree inference, and major speedups over StarBeast2 and *BEAST, making full MSC Bayesian inference feasible for datasets of ~100+ genes in many cases [1].  
- **BPP strengths** include flexible MSC parameter estimation and recent extensions for relaxed clocks and tip dates (useful for ancient DNA and time calibration) with precise divergence and population‑size estimates under many scenarios [2] [3].  
- **Use case**: choose full‑MSC Bayesian inference when divergence times and credible intervals are essential, substitution‑model uncertainty must be integrated, or gene‑tree branch lengths carry information you want to exploit [3] [1].

----

## Practical best practices

These recommendations synthesize empirical and methodological studies to reduce bias and improve accuracy when implementing MSC analyses for primates and mammals.

- **Prioritise many loci** for precision and robustness; sampling many independent loci often improves parameter estimates more than sampling few long loci [2].  
- **Filter low‑information loci** by length, parsimony‑informative sites, and missing data because short/poor alignments inflate gene‑tree estimation error and can drive discordance mistaken for biological ILS [4].  
- **Address gene tree estimation error** by using site‑based or co‑estimation approaches (StarBeast3, QuCo) or by weighting quartets and contracting very low‑support gene‑tree branches before running summary methods [5] [6] [7].  
- **Check for introgression or migration** before assuming a pure MSC: ignoring even modest gene flow can bias divergence times and topology inference; consider MSci or migration‑aware approximations (e.g., MSci models, DENIM) when gene flow is suspected [8] [9].  
- **Control for paralogy and multi‑copy families** using decomposition or paralogy‑aware methods (e.g., DISCO, ASTRAL‑Pro, SpeciesRax) rather than naively treating duplicated genes as single‑copy orthologs [10] [11].  
- **Be mindful of linkage and recombination**: closely linked loci produce dependent gene trees and reduce effective gene sample size, degrading performance of summary methods that assume independence [12].  
- **Convergence diagnostics and operator tuning** are essential for Bayesian runs; use StarBeast3’s adaptive operators and parallelisation but still assess mixing and ESS for key parameters [1] [3].  
- **Large mammal phylogenies** often combine strategies (backbone Bayesian dating plus patch-level analyses) to scale time‑calibrated species trees to thousands of species while controlling uncertainty [13].

----

## Method comparisons

The table contrasts StarBeast3, ASTRAL (summary), BPP (Bayesian MSC), and *BEAST/*BEAST2 (older full‑MSC implementations) to guide method choice.

| Feature | StarBeast3 | ASTRAL (summary) | BPP | *BEAST / *BEAST2 |
|---|---:|---|---:|---|
| Inference type | Full Bayesian co‑estimation of gene trees and species tree [1] | Summary quartets from input gene trees, optimization of quartet support [7] | Bayesian MSC for parameter and topology estimation, recent relaxed‑clock and tip‑date support [3] [2] | Full Bayesian MSC (earlier implementations) with higher computational cost [1] |
| Scales to | Tens–low hundreds of loci (parallelised), moderate taxa counts [1] | Very large numbers of genes and taxa (thousands) and fast runtimes [7] | Moderate locus counts; focuses on closely related species and parameter estimation [3] | Smaller datasets or fewer loci due to slower algorithms [1] |
| Co‑estimates gene trees | Yes (joint) [1] | No (uses pre‑estimated gene trees) [7] | Can use sequence data; coalescent likelihoods used for parameter inference [3] | Yes (older *BEAST implementations) but much slower [1] |
| Time and population estimates | Yes, Bayesian dated trees and population sizes [1] | Typically not used for full Bayesian dating from sequence alignments (summary) [7] | Yes, divergence times and Ne, including tip dating for aDNA [2] [3] | Yes, but computationally demanding and less efficient than StarBeast3 [1] |
| Robustness to gene‑tree error | Higher because sequence data are integrated, but computationally expensive [1] [5] | Sensitive to gene‑tree estimation error and gene‑tree dependence; improvements via quartet weighting and branch contraction mitigate this [7] [12] [6] | Good for parameter estimation; MCMC mixing under relaxed clocks can be problematic for species‑tree search [3] | Accurate but often prohibitively slow for many loci; earlier versions motivated StarBeast improvements [1] |
| Handles introgression/migration | Not by default; needs explicit MSci/network extensions or separate tests [8] | Does not model introgression (can be misled), though discordant signals may be explored downstream [7] | Extensions and MSci modeling available for introgression and tip dates [8] [3] | Not by default without specialized models; computational burden increases with complexity [1] |

(Cells summarize supported claims from the cited literature.)  

Additional approaches such as QuCo (quartet co‑estimation) offer a middle ground: scalable co‑estimation via quartet likelihoods and can outperform summary ASTRAL in some settings with gene‑tree error [5].

----

## Limitations and pitfalls

Implementers should explicitly test assumptions and diagnose sources of discordance because method choice strongly interacts with data characteristics and biological processes.

- **Computation versus realism tradeoff**: full MSC Bayesian co‑estimation (StarBeast3, BPP, *BEAST family) yields richer inference but is computationally costly and may not scale to thousands of loci or taxa [1] [14].  
- **Gene flow and model misspecification**: ignoring introgression or continuous migration can bias divergence times and topology unless MSci or migration‑aware models are used [8] [9].  
- **Gene tree dependence and linkage** reduce effective information for summary methods; closely spaced loci should be thinned or analyzed with methods robust to dependence [12].  
- **Gene tree estimation error and paralogy** can mislead summary methods; filter poor alignments, contract extremely low‑support branches, or use paralogy‑aware pipelines to reduce artefacts [4] [7] [10].  
- **MCMC mixing and convergence** problems can occur under complex relaxed‑clock MSC models; monitor ESS, run replicates, and use StarBeast3’s adaptive operators and parallelisation but verify convergence empirically [3] [1].  
- **No single best solution**: for large mammal or primate datasets, a hybrid workflow (filtering, summary methods for topology, targeted full‑MSC for focal clades or dating) often balances accuracy and feasibility [13] [7] [1].