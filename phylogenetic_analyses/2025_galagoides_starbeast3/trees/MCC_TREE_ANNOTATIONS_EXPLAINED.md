# MCC Tree Annotations Explained

**Date**: January 19, 2026  
**Tree File**: `galago_full_MCC.tree`

## What the Numbers Mean

### ✅ **Yes, the numbers (1, 0.9998, etc.) are posterior probabilities**

In your MCC tree file, you'll see annotations like:
- `posterior=1.0` - 100% posterior support
- `posterior=0.9997777901227709` - ~99.98% posterior support

These values represent the **posterior probability** that the clade (group of species) is correct, based on the posterior distribution of trees from your StarBeast3 analysis.

**Interpretation**:
- **1.0** = The clade appears in 100% of trees in the posterior distribution
- **0.9998** = The clade appears in 99.98% of trees in the posterior distribution
- Values close to 1.0 indicate very strong support

### Scale Bar (0.006)

The scale bar showing **0.006** represents **branch length units** (substitutions per site or time units, depending on your model).

Looking at your tree file, branch lengths range from:
- Smallest: ~0.003 (terminal branches)
- Largest: ~0.055 (root to outgroup)

So a scale bar of **0.006** is appropriate for visualizing the tree - it represents a small but visible portion of the total tree height.

**What it means**: The scale bar shows the distance in your tree's units (likely substitutions per site or coalescent time units).

---

## Your Figure Caption

Your figure caption is **100% correct** for this tree:

> "Maximum clade credibility species tree inferred under the multispecies coalescent. Tip labels represent species or provisional lineages; node bars show 95% highest posterior density (HPD) intervals; numbers indicate posterior support values. The Malawi lineage is labelled Paragalago cf. granti/nyasae to reflect current taxonomic uncertainty."

### Verification:

✅ **"Maximum clade credibility species tree"** - Correct! This is exactly what `galago_full_MCC.tree` is.

✅ **"inferred under the multispecies coalescent"** - Correct! StarBeast3 uses the multispecies coalescent model.

✅ **"Tip labels represent species or provisional lineages"** - Correct! Your tree has 5 tips: Otolemur_garnettii (outgroup), Paragalago_nyasae, Paragalago_rondoensis, Paragalago_zanzibaricus, and Paragalago_zanzibaricus_udzungwensis.

✅ **"node bars show 95% highest posterior density (HPD) intervals"** - Correct! Your tree file contains `height_95%_HPD={...}` annotations that FigTree can display as node bars.

✅ **"numbers indicate posterior support values"** - Correct! The numbers you see (1, 0.9998, etc.) are the `posterior=` values from the tree annotations.

✅ **"The Malawi lineage is labelled Paragalago cf. granti/nyasae"** - This is your taxonomic designation, which is appropriate given the uncertainty mentioned in your manuscript.

---

## What's in Your Tree File

Your MCC tree contains these annotations for each node:

1. **`posterior=X`** - Posterior probability (the numbers you see: 1.0, 0.9998, etc.)
2. **`height_95%_HPD={min, max}`** - 95% highest posterior density interval for node height (shown as bars in FigTree)
3. **`length=X`** - Branch length
4. **`length_95%_HPD={min, max}`** - 95% HPD for branch length
5. **`pop=X`** - Population size estimate
6. **`height_median=X`** - Median node height

---

## Summary

- ✅ **Numbers on nodes** = Posterior probabilities (1.0, 0.9998, etc.)
- ✅ **Scale bar (0.006)** = Branch length units
- ✅ **Your figure caption** = Perfectly matches this tree!

Your caption accurately describes what's in the MCC tree file. The numbers are indeed posterior support values, and the scale bar shows branch length units.
