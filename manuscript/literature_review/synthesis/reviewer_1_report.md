# Reviewer 1 Report: Methods & Theory Specialist

## Summary

This manuscript presents a multilocus species-tree reconstruction of East African dwarf galagos (*Paragalago*) using six loci (three mitochondrial: 12S, 16S, CYTB; three nuclear: IRBP, vWF intron 11, vWF exon 28) analyzed under the multispecies coalescent framework implemented in StarBEAST3. The authors recover four well-supported regional lineages: *P. zanzibaricus zanzibaricus* (Zanzibar Island), *P. z. udzungwensis* (mainland Tanzania), *P. rondoensis* (southern coastal forests), and a previously uncharacterized Malawi lineage tentatively identified as *Paragalago* cf. *granti*/*nyasae*. All internal nodes show very high posterior support (≥0.9998). The temporal pattern indicates that *P. rondoensis* forms the deepest ingroup split, the Malawi lineage diverges next, and the shallowest divergence (~3% of total tree height) separates the Zanzibar and Udzungwa subspecies. The authors interpret these patterns in the context of long-term isolation in coastal and montane refugia, island-mainland divergence, and forest fragmentation dynamics. This represents the first molecular phylogenetic placement of Malawi dwarf galago populations and provides an important foundation for taxonomic revision and conservation planning.

---

## Soundness: 4/5

**Justification**: The methodological approach is generally sound and represents a clear advance over previous concatenated or mitochondrial-only analyses of *Paragalago*. The use of StarBEAST3 for multispecies coalescent inference is appropriate for this taxonomic scale and explicitly addresses incomplete lineage sorting, which is critical for recently diverged taxa. The six-locus dataset provides a reasonable balance between mitochondrial and nuclear markers, and the statistical support for all major nodes is exceptionally high (≥0.9998 posterior probability).

However, several methodological details require clarification or raise concerns:

1. **Locus selection justification**: The manuscript does not provide explicit rationale for selecting these specific six loci beyond general statements about mitochondrial vs. nuclear markers. Were these loci chosen based on prior success in galagid phylogenetics, availability of primers, sequencing success rates, or phylogenetic informativeness? A brief justification would strengthen the methods.

2. **Taxon sampling within lineages**: While the inclusion of Malawi specimens is a major advance, the manuscript provides limited detail on within-lineage sampling. How many individuals per lineage were included? Are they from single localities or multiple populations? This affects the generalizability of the species-tree inference.

3. **Molecular clock model**: The manuscript mentions "relative time" and reports divergences as proportions of total tree height but does not clearly specify whether a strict or relaxed clock was implemented, what prior distributions were used for clock rates, or whether clock-like behavior was assessed. Given that StarBEAST3 supports relaxed clocks, this should be clarified.

4. **Model selection and partitioning**: The methods section should specify:
   - How substitution models were selected for each locus (e.g., jModelTest, PartitionFinder)
   - Whether partitioning by gene or by codon position was applied
   - Whether linked or unlinked substitution models were used across loci

5. **MCMC diagnostics**: While high posterior support is reported, the manuscript should provide:
   - Chain length and sampling frequency
   - Burnin proportion
   - ESS values for key parameters (tree topology, divergence times, population sizes)
   - Evidence of convergence across independent runs

6. **Gene tree vs. species tree concordance**: The manuscript does not present individual gene trees or discuss the degree of gene tree heterogeneity. Given that the primary justification for MSC methods is to accommodate such heterogeneity, showing the extent of discordance would strengthen the argument for the coalescent approach.

7. **Population size parameters**: StarBEAST models population sizes (theta parameters) for each branch. Are these estimates biologically reasonable? Do they correlate with known ecological or demographic factors (e.g., island vs. mainland populations)?

Despite these concerns, the core analytical approach is appropriate and the results appear robust. The exceptionally high posterior support (≥0.9998) for all nodes is reassuring but also somewhat unusual—typically some nodes show intermediate support. This could reflect genuine strong signal or potentially inadequate model complexity (e.g., overly simple substitution models or priors). Sensitivity analyses would help assess robustness.

---

## Presentation: 4/5

**Overall assessment**: The manuscript is generally well-written and logically structured, with clear presentation of the main findings. However, several aspects of presentation could be improved:

**Strengths**:
- Abstract is concise and effectively summarizes key findings
- Introduction provides good context on *Paragalago* taxonomy and biogeography
- Results are clearly stated with appropriate statistical support
- Discussion integrates findings with biogeographic hypotheses

**Areas for improvement**:

1. **Methods section**: Requires substantial expansion to meet journal standards for phylogenetic studies. Specifically:
   - Detailed specimen information (voucher numbers, collection localities, GPS coordinates)
   - DNA extraction and amplification protocols
   - Primer sequences or citations
   - Sequencing platform and quality control
   - Sequence alignment and trimming procedures
   - Complete StarBEAST3 settings (priors, operators, chain parameters)
   - Justification for outgroup selection (*Otolemur garnettii*)

2. **Results section**: Should include:
   - Summary statistics for each locus (alignment length, variable sites, parsimony-informative sites)
   - MCMC diagnostics (ESS values, convergence assessment)
   - Quantitative measures of gene tree discordance
   - Population size (theta) estimates for each lineage

3. **Figure quality**: 
   - The manuscript mentions a "maximum clade credibility tree" but the figure is not described in detail in the review materials
   - Figure should include scale bar (in substitutions per site or time units)
   - Branch support values should be clearly labeled
   - Consider adding gene tree concordance visualization (e.g., DensiTree plot)

4. **Table of specimens**: A supplementary table listing all specimens, voucher numbers, collection localities, and GenBank accession numbers is essential for reproducibility

5. **Terminology consistency**: 
   - The manuscript uses "relative time" and "proportion of tree height" interchangeably—standardize terminology
   - Clarify whether "dwarf galagos" refers to *Paragalago* specifically or includes other genera

6. **Statistical notation**: 
   - Posterior probabilities are reported as "≥0.9998" which is unusual notation. Report exact values or use standard thresholds (e.g., PP=1.00)
   - If values are truly ≥0.9998, explain why they did not reach 1.00

7. **Citation format**: Ensure all methodological citations are complete and current (e.g., BEAST3 software, alignment programs, model selection tools)

**Minor issues**:
- Some sentences are overly long and could be split for clarity
- Avoid repetition between Abstract, Introduction, and Discussion
- Define all abbreviations at first use (e.g., MSC, ESU, MCMC)

---

## Contribution: 4/5

**Assessment**: This manuscript makes significant contributions to *Paragalago* systematics, biogeography, and conservation biology:

**Major contributions**:

1. **First molecular data from Malawi**: This is the most important empirical contribution. Multiple prior studies (Karlsson 2006, 2009, 2011) identified Malawi populations as a critical sampling gap. By including these specimens and demonstrating a distinct lineage, the authors fill a major geographic and taxonomic void.

2. **Methodological advance for *Paragalago***: The application of StarBEAST3 represents the most rigorous phylogenetic treatment of the genus to date. While previous studies used concatenation (Pozzi et al. 2014) or focused on mtDNA (Delpero et al. 2000), this is apparently the first explicit MSC species-tree analysis focused on *Paragalago* with balanced mitochondrial and nuclear sampling.

3. **Four-lineage framework**: The clear resolution of four well-supported lineages provides a robust framework for future taxonomic, ecological, and conservation work. The exceptionally high posterior support (≥0.9998) for all nodes is notable.

4. **Temporal and biogeographic context**: By providing relative divergence times, the manuscript allows testing of biogeographic hypotheses about refugia, island-mainland divergence, and forest fragmentation.

**Comparison to state-of-the-art**:

The manuscript builds directly on and extends:
- **Masters et al. (2017)**: Proposed *Paragalago* as a distinct genus but lacked Malawi sampling
- **Pozzi et al. (2020)**: Supported three lineages in the *zanzibaricus* complex using multilocus data but did not include Malawi and did not explicitly report MSC species-tree analysis
- **Pozzi et al. (2014)**: Broad 27-locus galagid phylogeny but with limited within-*Paragalago* sampling

The current manuscript provides more focused, denser sampling within *Paragalago* and applies more sophisticated coalescent methods than previous work.

**Limitations on contribution**:

1. **Incremental vs. transformative**: While the inclusion of Malawi specimens is novel, the four-lineage structure largely confirms previous findings (Pozzi et al. 2020 identified three lineages; this adds a fourth). The methodological advance (StarBEAST3) is important but represents refinement rather than fundamental revision.

2. **Taxonomic resolution incomplete**: The Malawi lineage cannot be definitively assigned to *P. granti* or *P. nyasae* without sampling from type localities. This limits immediate taxonomic impact.

3. **Relative vs. absolute times**: The use of relative rather than absolute divergence times limits direct comparison to biogeographic events and fossil records. While this is understandable given the absence of reliable calibrations, it reduces the biogeographic contribution.

4. **Limited locus number**: Six loci is a substantial improvement over previous studies but modest compared to phylogenomic approaches (RADseq, UCEs, whole genomes) now common in primate systematics. This limits resolution of potential gene flow, introgression, or population structure.

5. **No species delimitation tests**: While the manuscript presents a species tree, it does not formally test species boundaries using methods like BPP, STACEY, or BFD*. Given the taxonomic uncertainty (especially for the Malawi lineage), such tests would strengthen the contribution.

**Overall**: Despite these limitations, the contribution is significant and will be of broad interest to primatologists, systematists, and conservation biologists. The manuscript establishes an essential foundation for future work.

---

## Strengths

1. **Critical geographic sampling**: The inclusion of Malawi specimens fills a major gap repeatedly identified in the literature (Karlsson 2006, 2009, 2011). This is the manuscript's single most important contribution.

2. **Appropriate methodological framework**: StarBEAST3 is the state-of-the-art for multispecies coalescent inference at this taxonomic scale. The explicit modeling of incomplete lineage sorting is essential for recently diverged taxa and represents a clear advance over concatenated approaches.

3. **Exceptionally high statistical support**: Posterior probabilities ≥0.9998 for all internal nodes indicate strong phylogenetic signal and robust inference. This provides confidence in the four-lineage structure.

4. **Balanced locus selection**: The combination of three mitochondrial and three nuclear loci provides complementary evolutionary rates and inheritance patterns, which is appropriate for MSC inference.

5. **Clear biogeographic hypotheses**: The manuscript effectively integrates phylogenetic findings with biogeographic processes (refugia, island-mainland divergence, forest fragmentation), providing testable predictions.

6. **Conservation relevance**: By identifying four distinct lineages and providing molecular evidence for their evolutionary independence, the manuscript directly informs conservation prioritization and IUCN assessments.

7. **Temporal framework**: The relative divergence time estimates (deepest: *P. rondoensis*; intermediate: Malawi; shallowest: Zanzibar-Udzungwa) provide insights into the sequence of diversification events.

8. **Transparent acknowledgment of uncertainty**: The authors appropriately note that the Malawi lineage cannot be definitively assigned to *P. granti* or *P. nyasae* without additional sampling, demonstrating scientific caution.

9. **Foundation for future work**: The molecular data and phylogenetic framework establish a baseline for population genetics, phylogenomics, and integrative taxonomy.

10. **Outgroup selection**: *Otolemur garnettii* is an appropriate outgroup for rooting the *Paragalago* tree, being a well-characterized galagid outside the focal clade.

---

## Weaknesses

### Major concerns:

1. **Insufficient methodological detail**: The methods section lacks critical information required for reproducibility and evaluation:
   - No specimen voucher numbers or collection details
   - No primer sequences or citations
   - No sequencing platform or quality control procedures
   - Incomplete StarBEAST3 settings (priors, operators, chain length)
   - No model selection procedure described
   - No MCMC diagnostics reported (ESS values, convergence)
   
   **This is a critical deficiency that must be addressed before publication.**

2. **No gene tree presentation or discordance analysis**: The primary justification for MSC methods is to accommodate gene tree heterogeneity from incomplete lineage sorting. However:
   - Individual gene trees are not shown
   - Degree of gene tree discordance is not quantified
   - No discussion of which loci show concordance vs. conflict
   
   **Recommendation**: Add supplementary figures showing individual gene trees and quantify discordance using metrics like Robinson-Foulds distance or quartet concordance. Discuss biological implications (e.g., incomplete lineage sorting vs. introgression).

3. **Relative vs. absolute divergence times**: The manuscript reports divergences as proportions of total tree height rather than absolute ages. While understandable given limited fossil calibrations for galagids, this limits:
   - Direct comparison to biogeographic events (e.g., Pleistocene glacial cycles, sea-level changes)
   - Assessment of diversification rates
   - Comparison to other African primate radiations
   
   **Recommendation**: Explore secondary calibrations from broader primate phylogenies (e.g., Pozzi et al. 2014) or biogeographic priors (e.g., Zanzibar island formation) to obtain absolute age estimates, even if approximate.

4. **No formal species delimitation**: While the manuscript presents a species tree, it does not formally test species boundaries using dedicated delimitation methods (e.g., BPP, STACEY, BFD*). Given the taxonomic uncertainty for the Malawi lineage and the conservation implications of species-level taxonomy, such tests would strengthen the manuscript.
   
   **Recommendation**: Implement BPP or similar methods to test alternative delimitation scenarios (e.g., four species vs. three species with Malawi as a subspecies).

5. **Limited within-lineage sampling**: The manuscript states 24 individuals total but does not clearly specify:
   - How many individuals per lineage
   - Whether sampling represents single localities or multiple populations
   - Geographic coverage within each lineage's range
   
   **Concern**: If each lineage is represented by only a few individuals from a single locality, the species tree may not capture within-lineage diversity or population structure. This could lead to overconfidence in species boundaries.
   
   **Recommendation**: Provide a table of specimens with collection localities and discuss sampling limitations.

6. **Lack of sensitivity analyses**: The manuscript does not report sensitivity to:
   - Prior distributions (e.g., population size priors, clock rate priors)
   - Substitution model choice
   - Partitioning schemes
   - Outgroup selection
   
   **Recommendation**: Conduct sensitivity analyses varying key priors and models to assess robustness of the four-lineage topology.

### Moderate concerns:

7. **Unusually high posterior support**: All nodes show PP ≥0.9998, which is exceptionally high. While this could reflect genuine strong signal, it could also indicate:
   - Overly simple models that underestimate uncertainty
   - Inadequate chain mixing leading to premature convergence
   - Prior distributions dominating the posterior
   
   **Recommendation**: Check MCMC diagnostics carefully (ESS, trace plots) and consider more complex models or alternative priors.

8. **No assessment of mito-nuclear discordance**: Other African mammal studies have found substantial mito-nuclear discordance due to introgression or sex-biased dispersal (Demos et al. 2019; Petzold & Hassanin 2020). The manuscript does not:
   - Compare mitochondrial vs. nuclear gene trees
   - Test for cyto-nuclear discordance
   - Discuss implications for species boundaries
   
   **Recommendation**: Conduct separate analyses of mitochondrial vs. nuclear loci and test for significant discordance.

9. **Population size estimates not discussed**: StarBEAST models effective population sizes (theta parameters) for each branch. These estimates could provide insights into:
   - Demographic history (bottlenecks, expansions)
   - Island vs. mainland population sizes
   - Vulnerability to genetic drift
   
   **Recommendation**: Report theta estimates and discuss biological implications.

10. **Locus selection not justified**: The choice of these specific six loci is not explained. Were they:
    - Selected based on phylogenetic informativeness?
    - Chosen for comparability with previous studies?
    - The only loci that amplified successfully?
    
    **Recommendation**: Provide brief justification for locus selection.

11. **No integration with acoustic data**: Previous studies (Génin 2021; Pozzi et al. 2019) have demonstrated species-specific loud-call differences in *Paragalago*. The manuscript does not:
    - Report acoustic data for the Malawi lineage
    - Compare acoustic vs. genetic boundaries
    - Discuss concordance/discordance between data types
    
    **Recommendation**: If acoustic data are available for Malawi specimens, include them. If not, acknowledge this as a limitation and priority for future work.

12. **Incomplete comparison to previous phylogenetic hypotheses**: The manuscript should more explicitly compare the four-lineage topology to previous hypotheses, particularly:
    - Pozzi et al. (2020): three lineages in *zanzibaricus* complex
    - Masters et al. (2017): generic boundaries
    - Honess (1996): subspecies designations
    
    **Recommendation**: Add a table or figure comparing alternative topologies and discuss support for each.

### Minor concerns:

13. **Figure presentation**: The manuscript mentions a maximum clade credibility tree but does not provide detailed figure description or legends in the review materials. Ensure:
    - Scale bar is included (substitutions per site or time units)
    - Branch support values are clearly labeled
    - Node ages (relative or absolute) are indicated
    - Lineage names match taxonomy used in text

14. **GenBank accession numbers**: Not mentioned in the manuscript. All sequences must be deposited in GenBank with accession numbers provided.

15. **Supplementary materials**: The manuscript would benefit from:
    - Supplementary Table S1: Specimen information (voucher numbers, localities, GPS coordinates, GenBank accessions)
    - Supplementary Table S2: Locus characteristics (length, variable sites, model selected)
    - Supplementary Table S3: MCMC diagnostics (ESS values for key parameters)
    - Supplementary Figure S1: Individual gene trees
    - Supplementary Figure S2: MCMC trace plots
    - Supplementary File S1: Aligned sequence data
    - Supplementary File S2: StarBEAST3 XML file

16. **Statistical notation**: The notation "≥0.9998" is unconventional. Standard practice is to report:
    - Exact posterior probabilities (e.g., PP=0.9998)
    - Or use threshold notation (e.g., PP>0.95, PP=1.00)
    
    If values are truly ≥0.9998 but not 1.00, explain why.

17. **Terminology**: "Relative time" and "proportion of tree height" are used interchangeably. Standardize on one term and define clearly.

18. **Citation completeness**: Ensure all software, methods, and prior studies are properly cited:
    - BEAST3/StarBEAST3 (Douglas & Bouckaert 2022)
    - Sequence alignment software
    - Model selection tools
    - Tree visualization software
    - All relevant *Paragalago* studies (Masters et al. 2017; Pozzi et al. 2020, 2019, 2014; Génin 2021; Karlsson 2006, 2009, 2011)

---

## Suggestions

1. **Expand methods section substantially**: Include all details necessary for reproducibility (specimen information, lab protocols, bioinformatic pipelines, complete StarBEAST3 settings, model selection, MCMC diagnostics).

2. **Present and analyze gene tree heterogeneity**: Show individual gene trees, quantify discordance, and discuss biological implications (incomplete lineage sorting vs. introgression).

3. **Attempt absolute divergence time estimation**: Use secondary calibrations or biogeographic priors to obtain approximate absolute ages, enabling comparison to biogeographic events.

4. **Conduct formal species delimitation tests**: Use BPP or similar methods to test alternative delimitation scenarios and provide statistical support for species boundaries.

5. **Provide detailed specimen information**: Create supplementary table with voucher numbers, collection localities, GPS coordinates, and GenBank accession numbers.

6. **Report population size estimates**: Discuss theta parameters from StarBEAST3 and their biological implications (demography, island vs. mainland differences).

7. **Assess mito-nuclear concordance**: Separately analyze mitochondrial vs. nuclear loci and test for significant discordance that could indicate introgression or sex-biased processes.

8. **Conduct sensitivity analyses**: Test robustness to prior distributions, substitution models, and partitioning schemes.

9. **Integrate acoustic data if available**: If loud-call recordings exist for Malawi specimens, include acoustic analysis to test concordance with genetic boundaries.

10. **Expand discussion of conservation implications**: Provide specific recommendations for:
    - IUCN red-list assessments for each lineage
    - Priority forest fragments for protection
    - Connectivity corridors to maintain gene flow
    - Monitoring protocols for genetic diversity

11. **Compare explicitly to previous phylogenetic hypotheses**: Create table or figure comparing the four-lineage topology to previous studies and discuss areas of agreement/disagreement.

12. **Discuss future directions**: Outline specific next steps:
    - Phylogenomic approaches (RADseq, UCEs) for higher resolution
    - Population genomic sampling within lineages
    - Sampling from *P. granti* type locality
    - Integration of morphological and acoustic data
    - Ancient DNA from museum specimens

13. **Improve figure quality**: Ensure maximum clade credibility tree includes:
    - Clear scale bar
    - Branch support values
    - Node ages (relative or absolute)
    - High-resolution graphics suitable for publication

14. **Add supplementary materials**: Include tables, figures, and files listed in "Weaknesses" section above.

15. **Standardize terminology and notation**: Use consistent terms for time estimates and standard notation for posterior probabilities.

---

## Questions

1. **Specimen sampling**: How many individuals represent each of the four lineages? Are they from single localities or multiple populations within each lineage's range? Please provide a detailed specimen table.

2. **MCMC diagnostics**: What were the ESS values for tree topology, divergence times, and population sizes? How many independent runs were conducted? Did they converge on the same topology and parameter estimates?

3. **Gene tree discordance**: What is the degree of discordance among the six gene trees? Do all loci support the same four-lineage topology, or is there conflict? If there is conflict, which nodes show discordance?

4. **Molecular clock model**: Was a strict or relaxed clock implemented? What prior distributions were used for clock rates? Was clock-like behavior assessed for each locus?

5. **Substitution models**: How were substitution models selected for each locus (e.g., jModelTest, PartitionFinder, BEAST's built-in model selection)? What models were selected? Were models linked or unlinked across loci?

6. **Partitioning strategy**: Were mitochondrial loci partitioned by codon position? Were nuclear loci partitioned? What was the rationale for the partitioning scheme?

7. **Prior sensitivity**: How sensitive are the results to prior distributions, particularly population size priors and clock rate priors? Were alternative priors tested?

8. **Population size estimates**: What are the effective population size (theta) estimates for each lineage? Do they differ significantly (e.g., island vs. mainland)? Are they biologically plausible given known ecology?

9. **Mito-nuclear concordance**: Do the mitochondrial and nuclear loci support the same topology? Is there evidence of cyto-nuclear discordance that could indicate introgression or sex-biased dispersal?

10. **Locus selection rationale**: Why were these specific six loci chosen? Were they selected based on phylogenetic informativeness, prior use in galagid studies, or sequencing success rates?

11. **Absolute vs. relative time**: Why was absolute divergence time estimation not attempted? Could secondary calibrations from broader primate phylogenies (e.g., Pozzi et al. 2014) be applied?

12. **Species delimitation**: Were formal species delimitation methods (BPP, STACEY, BFD*) considered? If not, why not? If so, what were the results?

13. **Acoustic data**: Are loud-call recordings available for the Malawi specimens? If so, do they show diagnostic differences from other lineages? If not, is this a priority for future fieldwork?

14. **Taxonomic assignment of Malawi lineage**: What evidence would be needed to definitively assign the Malawi lineage to *P. granti* vs. *P. nyasae*? Are there plans to sample from type localities?

15. **Within-lineage diversity**: Does within-lineage genetic diversity vary among the four lineages? Are island populations (Zanzibar) less diverse than mainland populations, as expected from island biogeography theory?

16. **Outgroup choice**: Why was *Otolemur garnettii* chosen as the outgroup? Were other galagids considered? How might outgroup choice affect the ingroup topology?

17. **Fossil calibrations**: Are there any fossil galagids that could be used for absolute dating? If not, what is the oldest reliable calibration point in the broader primate tree that could be used?

18. **Conservation genetics**: Are there plans for follow-up population genetic studies to assess genetic diversity, inbreeding, and connectivity within each lineage?

19. **Biogeographic priors**: Could biogeographic events (e.g., Zanzibar island formation, Eastern Arc uplift) be used as priors for divergence time estimation?

20. **Comparison to concatenated analysis**: How does the StarBEAST3 species tree compare to a concatenated supermatrix analysis? Are the topologies identical, or does the coalescent approach resolve conflict?

---

## Rating: 7/10

**Recommendation: Accept with major revisions**

**Justification**: This manuscript makes important empirical (first molecular data from Malawi) and methodological (StarBEAST3 MSC analysis) contributions to *Paragalago* systematics. The four-lineage structure is well-supported and provides a robust framework for future taxonomic, biogeographic, and conservation work. However, the manuscript requires substantial revision to meet publication standards:

**Major revisions required**:
1. Expand methods section with complete reproducibility details
2. Present and analyze gene tree heterogeneity
3. Report MCMC diagnostics and convergence assessment
4. Provide specimen table with voucher numbers and localities
5. Discuss population size estimates and biological implications
6. Assess mito-nuclear concordance
7. Conduct sensitivity analyses

**Recommended revisions**:
1. Attempt absolute divergence time estimation
2. Conduct formal species delimitation tests
3. Integrate acoustic data if available
4. Expand conservation discussion with specific recommendations

With these revisions, the manuscript will be a strong contribution suitable for publication in a leading systematic biology or conservation genetics journal (e.g., *Molecular Phylogenetics and Evolution*, *Systematic Biology*, *BMC Evolutionary Biology*, *Conservation Genetics*).

---

## Confidence: 4/5 (High)

**Justification**: I am highly confident in this assessment based on:

1. **Expertise in multispecies coalescent methods**: I have extensive experience evaluating MSC analyses and am familiar with StarBEAST3 implementation and best practices.

2. **Knowledge of primate phylogenetics**: I am well-versed in the methodological and empirical standards for primate systematic studies.

3. **Familiarity with *Paragalago* literature**: I have reviewed the key prior studies (Masters et al. 2017; Pozzi et al. 2020, 2014; Génin 2021) and understand the taxonomic and biogeographic context.

4. **Experience with similar manuscripts**: I have reviewed numerous multilocus phylogenetic studies and am familiar with common strengths and weaknesses.

**Minor uncertainty**: My confidence is not absolute (5/5) because:
- I have not seen the actual sequence alignments or StarBEAST3 output files, only the manuscript text
- Some methodological details may be present in supplementary materials not provided for this review
- I am not a field expert on East African biogeography, so some biogeographic interpretations may require additional specialist review

Overall, I am confident that the major methodological concerns identified are valid and that addressing them will substantially strengthen the manuscript.
