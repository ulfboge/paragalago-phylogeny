# Reviewer 2 Report: Experiments & Practical Impact Specialist

## Summary

This manuscript presents a multilocus phylogenetic analysis of East African dwarf galagos (*Paragalago*) using six genetic markers (mitochondrial 12S, 16S, CYTB; nuclear IRBP, vWF intron 11, vWF exon 28) and multispecies coalescent methods (StarBEAST3). The study includes 24 individuals from Zanzibar, mainland Tanzania, and—critically—Malawi, representing the first molecular sampling of Malawian dwarf galago populations. The authors recover four well-supported lineages: *P. zanzibaricus zanzibaricus* (Zanzibar), *P. z. udzungwensis* (mainland Tanzania), *P. rondoensis* (southern coastal Tanzania), and a distinct Malawi lineage (*Paragalago* cf. *granti*/*nyasae*). All nodes show posterior probabilities ≥0.9998. The temporal pattern suggests that *P. rondoensis* diverged first, followed by the Malawi lineage, with the most recent split separating Zanzibar and mainland Tanzania populations (~3% of total tree height). The authors interpret these findings in the context of forest refugia, island-mainland isolation, and habitat fragmentation, with direct implications for conservation prioritization in threatened East African forests.

---

## Soundness: 4/5

**Justification**: The experimental design is generally sound, with appropriate molecular markers, suitable analytical methods, and clear results. The inclusion of Malawi specimens addresses a critical sampling gap, and the high statistical support for all major clades provides confidence in the phylogenetic inference. However, several aspects of the experimental design and data presentation require clarification or raise concerns:

**Strengths of experimental design**:
1. **Appropriate marker selection**: Six loci combining mitochondrial (maternal, fast-evolving) and nuclear (biparental, slower-evolving) markers provide complementary phylogenetic signal
2. **Suitable analytical framework**: StarBEAST3 multispecies coalescent is appropriate for recent divergences with potential incomplete lineage sorting
3. **Critical geographic sampling**: First inclusion of Malawi populations fills major gap
4. **Adequate outgroup**: *Otolemur garnettii* provides phylogenetic context

**Concerns about experimental design and reporting**:

1. **Sample size and geographic coverage**: The manuscript states "24 individuals" but does not provide:
   - Breakdown by lineage (how many per lineage?)
   - Geographic distribution within lineages (single locality or multiple populations?)
   - Sampling map showing collection sites
   
   **Concern**: If some lineages are represented by only 1-2 individuals from a single locality, the phylogenetic inference may not capture within-lineage diversity or population structure. This could lead to overconfident species boundaries.
   
   **Recommendation**: Provide Table 1 with specimen details (ID, lineage, locality, GPS coordinates, voucher numbers, GenBank accessions) and Figure 1 showing sampling localities on a map.

2. **No molecular data summary**: The manuscript does not provide basic descriptive statistics for the molecular data:
   - Alignment length for each locus
   - Number of variable sites per locus
   - Number of parsimony-informative sites per locus
   - Percentage of missing data
   - GC content
   
   **Recommendation**: Add Table 2 summarizing locus characteristics. This allows readers to assess data quality and phylogenetic informativeness.

3. **Sequencing success rates not reported**: The manuscript does not indicate:
   - Whether all 24 individuals were successfully sequenced for all 6 loci (144 sequences total)
   - If not, what percentage of sequences were obtained
   - Whether missing data is randomly distributed or concentrated in certain individuals/loci
   
   **Concern**: Substantial missing data could bias phylogenetic inference, especially in coalescent analyses that model population processes.
   
   **Recommendation**: Report sequencing success matrix and discuss any systematic patterns of missing data.

4. **No baseline comparisons or validation**: The manuscript does not:
   - Compare StarBEAST3 results to concatenated analysis (e.g., RAxML, IQ-TREE)
   - Show individual gene trees to demonstrate concordance/discordance
   - Validate results with alternative coalescent methods (e.g., ASTRAL, SVDquartets)
   
   **Recommendation**: Add supplementary analyses showing: (a) concatenated ML tree, (b) individual gene trees, (c) ASTRAL species tree. Discuss areas of agreement/disagreement.

5. **Temporal calibration absent**: The manuscript reports "relative time" (proportions of tree height) rather than absolute ages. While this is understandable given limited fossil calibrations, it severely limits:
   - Comparison to biogeographic events (Pleistocene glaciations, sea-level changes, island formation)
   - Assessment of diversification rates
   - Evaluation of time-dependent processes (e.g., speciation rates, extinction rates)
   
   **Recommendation**: Explore secondary calibrations from broader primate phylogenies (Pozzi et al. 2014) or biogeographic priors (Zanzibar island age ~5-6 Ma based on geological evidence) to obtain approximate absolute ages.

6. **No robustness checks**: The manuscript does not report sensitivity analyses for:
   - Prior distributions (population size priors, clock rate priors)
   - Substitution model choice
   - Partitioning schemes (by gene vs. by codon position)
   - Outgroup selection
   
   **Recommendation**: Conduct sensitivity analyses varying key assumptions and report whether the four-lineage topology is robust.

7. **Statistical support interpretation**: All nodes show PP ≥0.9998, which is exceptionally high. While this could reflect strong signal, it raises questions:
   - Are MCMC chains adequately mixing?
   - Are models sufficiently complex to capture uncertainty?
   - Are priors dominating the posterior?
   
   **Recommendation**: Provide MCMC diagnostics (ESS values, trace plots, convergence across independent runs) to demonstrate that high support reflects genuine signal rather than inadequate sampling or model misspecification.

---

## Presentation: 3/5

**Assessment**: The manuscript is generally well-written with clear presentation of main findings, but several critical aspects of experimental design, data quality, and results presentation are missing or inadequately described. This significantly hampers reproducibility and evaluation of the work.

**Strengths**:
- Abstract effectively summarizes key findings
- Introduction provides good context on *Paragalago* taxonomy and biogeography
- Results section clearly states main findings with statistical support
- Discussion integrates findings with biogeographic hypotheses

**Major deficiencies**:

1. **Methods section lacks essential experimental details**:
   - No specimen collection details (localities, dates, collectors, voucher numbers)
   - No DNA extraction protocol (kit, tissue type, quality control)
   - No PCR amplification details (primers, cycling conditions, product size)
   - No sequencing platform specified (Sanger, Illumina, etc.)
   - No sequence quality control described (base calling, trimming, error rates)
   - No alignment procedure specified (algorithm, manual editing, gap treatment)
   - Incomplete StarBEAST3 settings (priors, operators, chain length, burnin, sampling frequency)
   - No model selection procedure described
   
   **Impact**: These omissions make the study **non-reproducible**, which is unacceptable for publication.

2. **Results section missing key data summaries**:
   - No table of specimen information
   - No table of locus characteristics (length, variability, model selected)
   - No MCMC diagnostics (ESS values, convergence assessment)
   - No summary of population size estimates from StarBEAST3
   - No quantification of gene tree discordance
   
   **Impact**: Readers cannot assess data quality, analytical rigor, or robustness of results.

3. **Figure presentation inadequate**:
   - Maximum clade credibility tree is mentioned but not fully described
   - No sampling locality map provided
   - No visualization of gene tree heterogeneity (e.g., DensiTree plot)
   - No MCMC trace plots to demonstrate convergence
   
   **Recommendation**: Add:
   - **Figure 1**: Map of East Africa showing sampling localities color-coded by lineage
   - **Figure 2**: Maximum clade credibility tree with scale bar, node support, and divergence times
   - **Supplementary Figure S1**: Individual gene trees
   - **Supplementary Figure S2**: DensiTree plot showing gene tree heterogeneity
   - **Supplementary Figure S3**: MCMC trace plots for key parameters

4. **No supplementary materials mentioned**: Modern phylogenetic studies require extensive supplementary materials:
   - **Supplementary Table S1**: Specimen information
   - **Supplementary Table S2**: Locus characteristics
   - **Supplementary Table S3**: MCMC diagnostics
   - **Supplementary Data S1**: Aligned sequences (FASTA or NEXUS format)
   - **Supplementary Data S2**: StarBEAST3 XML file
   - **Supplementary Data S3**: Tree file (NEXUS format)
   
   **Impact**: Without these materials, the study cannot be reproduced or validated by other researchers.

5. **Inconsistent terminology**: The manuscript uses "relative time," "proportion of tree height," and "~3% of total tree height" interchangeably without clear definition. Standardize terminology.

6. **Statistical notation unconventional**: Posterior probabilities reported as "≥0.9998" is unusual. Standard practice is to report exact values (e.g., PP=0.9998) or use threshold notation (e.g., PP=1.00).

7. **GenBank accessions not provided**: All sequences must be deposited in GenBank with accession numbers listed in the manuscript or supplementary materials.

---

## Contribution: 4/5

**Assessment**: The manuscript makes significant empirical contributions to *Paragalago* systematics and conservation, but the practical impact is somewhat limited by incomplete taxonomic resolution and lack of absolute temporal framework.

**Major empirical contributions**:

1. **First molecular data from Malawi** (★★★★★): This is the single most important contribution. Multiple prior studies (Karlsson 2006, 2009, 2011) identified Malawi galago populations as critically understudied. By obtaining molecular data and demonstrating a distinct lineage, the authors:
   - Fill a major geographic sampling gap
   - Provide baseline data for taxonomic revision
   - Inform conservation status assessments
   - Enable future population genetic studies

2. **Four-lineage phylogenetic framework** (★★★★☆): The clear resolution of four well-supported lineages provides:
   - Robust framework for future taxonomic work
   - Evolutionary context for biogeographic hypotheses
   - Basis for defining conservation units (ESUs)
   
   **Comparison to previous work**: Pozzi et al. (2020) identified three lineages in the *zanzibaricus* complex; this study adds a fourth (Malawi) and provides higher statistical support using MSC methods.

3. **Temporal pattern of diversification** (★★★☆☆): The relative divergence times (deepest: *P. rondoensis*; intermediate: Malawi; shallowest: Zanzibar-Udzungwa) provide insights into:
   - Sequence of lineage splitting events
   - Relative ages of biogeographic processes
   
   **Limitation**: Without absolute ages, direct comparison to biogeographic events (Pleistocene glaciations, sea-level changes, island formation) is not possible.

4. **Conservation prioritization** (★★★★☆): By identifying four distinct lineages and documenting their geographic distributions, the manuscript:
   - Informs IUCN red-list assessments
   - Prioritizes forest fragments for protection (Rondo Plateau, Malawi montane forests, Udzungwa Mountains, Zanzibar)
   - Provides molecular evidence for conservation planning in Tanzania and Malawi

**Limitations on practical impact**:

1. **Taxonomic resolution incomplete**: The Malawi lineage cannot be definitively assigned to *P. granti* or *P. nyasae* without:
   - Sampling from type localities (Mount Kilimanjaro for *P. granti*)
   - Morphological comparisons
   - Acoustic data
   
   **Impact**: Formal taxonomic revision and species descriptions cannot proceed without this additional work.

2. **No population-level insights**: The species-tree approach focuses on lineage divergence but does not address:
   - Within-lineage genetic diversity
   - Population structure and connectivity
   - Gene flow among adjacent populations
   - Effective population sizes and demographic history
   
   **Impact**: Conservation planning requires population-level data (e.g., for defining management units, assessing inbreeding risk, designing connectivity corridors).

3. **Limited locus number**: Six loci is an improvement over previous studies but modest compared to phylogenomic approaches (RADseq, UCEs, whole genomes) now common in conservation genetics. Higher resolution data could:
   - Detect recent or ongoing gene flow
   - Identify adaptive genetic variation
   - Assess inbreeding and genetic load

4. **No integration with ecological or behavioral data**: The manuscript does not incorporate:
   - Acoustic data (loud-call recordings)
   - Morphological measurements
   - Ecological niche models
   - Habitat association data
   
   **Impact**: Integrative species delimitation combining multiple data types would provide stronger evidence for species boundaries.

5. **No direct conservation recommendations**: While the manuscript discusses conservation implications, it does not provide specific, actionable recommendations such as:
   - Proposed IUCN threat categories for each lineage
   - Priority forest fragments for immediate protection
   - Connectivity corridors to maintain gene flow
   - Monitoring protocols for genetic diversity
   - Translocation or captive breeding considerations

**Overall contribution assessment**: Despite these limitations, the manuscript makes important contributions that will be valuable to primatologists, systematists, and conservation biologists. The Malawi molecular data alone justifies publication, and the MSC framework provides a solid foundation for future work.

---

## Strengths

1. **Critical geographic sampling achievement**: Obtaining molecular data from Malawi populations fills the most significant gap in *Paragalago* sampling. This required substantial field effort in logistically challenging, remote forest sites and represents years of work (Karlsson's proposals date to 2006).

2. **High statistical support**: Posterior probabilities ≥0.9998 for all nodes provide strong confidence in the four-lineage structure. This level of support is rare in phylogenetic studies and suggests robust phylogenetic signal.

3. **Appropriate analytical framework**: StarBEAST3 multispecies coalescent is the state-of-the-art method for this taxonomic scale and explicitly addresses incomplete lineage sorting, which is critical for recently diverged taxa.

4. **Balanced molecular marker selection**: Three mitochondrial + three nuclear loci provide complementary evolutionary rates and inheritance patterns, which is appropriate for MSC inference.

5. **Clear conservation relevance**: The manuscript directly addresses conservation priorities by:
   - Identifying distinct lineages requiring separate management
   - Highlighting threatened forest fragments harboring unique diversity
   - Providing molecular evidence for IUCN assessments

6. **Biogeographic integration**: The temporal pattern of divergences (deepest: *P. rondoensis*; intermediate: Malawi; shallowest: Zanzibar-Udzungwa) aligns well with biogeographic hypotheses about:
   - Long-term isolation of coastal refugia (Rondo Plateau)
   - Southern miombo-montane refugia (Malawi)
   - Recent island-mainland divergence (Zanzibar)

7. **Foundation for future work**: The molecular data and phylogenetic framework establish essential baseline for:
   - Population genetic studies within lineages
   - Phylogenomic analyses with higher resolution
   - Integrative taxonomy combining genetic, acoustic, and morphological data
   - Conservation genetics assessments

8. **Transparent acknowledgment of uncertainty**: The authors appropriately note that the Malawi lineage cannot be definitively assigned without additional sampling, demonstrating scientific caution.

9. **Builds on strong prior foundation**: The manuscript effectively extends previous work by Masters et al. (2017), Pozzi et al. (2020, 2014), and Génin (2021), providing continuity with established literature.

10. **Practical conservation impact**: By documenting a distinct Malawi lineage, the manuscript:
    - Elevates conservation priority for Malawi montane forests
    - Provides evidence for national protected area planning
    - Supports international conservation funding proposals

---

## Weaknesses

### Critical deficiencies (must be addressed):

1. **No specimen information table**: The manuscript lacks a basic table listing:
   - Specimen ID
   - Lineage assignment
   - Collection locality (with GPS coordinates)
   - Collection date
   - Collector
   - Voucher number (museum catalog number)
   - GenBank accession numbers for each locus
   
   **Impact**: Without this information, the study is **not reproducible**. Readers cannot assess geographic coverage, sampling bias, or verify identifications. This is a **fundamental requirement** for publication in any journal.
   
   **Recommendation**: Add Table 1 with complete specimen information.

2. **No molecular data summary**: The manuscript does not provide basic descriptive statistics:
   
   | Locus | Alignment length | Variable sites | Parsimony-informative sites | Missing data (%) | Model selected |
   |-------|------------------|----------------|------------------------------|------------------|----------------|
   | 12S | ? | ? | ? | ? | ? |
   | 16S | ? | ? | ? | ? | ? |
   | CYTB | ? | ? | ? | ? | ? |
   | IRBP | ? | ? | ? | ? | ? |
   | vWF intron 11 | ? | ? | ? | ? | ? |
   | vWF exon 28 | ? | ? | ? | ? | ? |
   
   **Impact**: Readers cannot assess data quality or phylogenetic informativeness. This information is **essential** for evaluating the soundness of the phylogenetic inference.
   
   **Recommendation**: Add Table 2 with locus characteristics.

3. **No MCMC diagnostics reported**: The manuscript does not provide:
   - Chain length
   - Burnin proportion
   - Sampling frequency
   - Number of independent runs
   - ESS (Effective Sample Size) values for key parameters:
     - Tree topology
     - Divergence times
     - Population sizes (theta)
     - Substitution rates
   - Convergence assessment across runs
   
   **Impact**: Without MCMC diagnostics, readers cannot determine whether the high posterior support (≥0.9998) reflects genuine signal or inadequate chain mixing, premature convergence, or model misspecification. This is **critical** for validating Bayesian phylogenetic analyses.
   
   **Recommendation**: Add Table 3 with MCMC diagnostics and Supplementary Figure with trace plots.

4. **No sampling locality map**: The manuscript does not include a map showing:
   - Collection localities for all 24 individuals
   - Color-coding by lineage assignment
   - Forest cover and protected areas
   - Geographic barriers (mountains, rivers, sea)
   
   **Impact**: Readers cannot visualize the geographic distribution of lineages or assess whether sampling captures the full range of each lineage. A map is **essential** for biogeographic studies.
   
   **Recommendation**: Add Figure 1 showing sampling localities.

5. **Methods section severely incomplete**: Critical experimental details are missing:
   
   **Specimen collection**:
   - Collection methods (live capture, museum specimens, tissue type)
   - Permits and ethical approvals
   - Specimen preservation (frozen, ethanol, etc.)
   
   **DNA extraction**:
   - Extraction kit or protocol
   - Tissue type (muscle, liver, blood, etc.)
   - DNA quality control (gel electrophoresis, spectrophotometry)
   
   **PCR amplification**:
   - Primer sequences or citations
   - PCR cycling conditions (denaturation, annealing, extension temperatures and times)
   - Expected product sizes
   - PCR product purification
   
   **Sequencing**:
   - Sequencing platform (Sanger, Illumina, etc.)
   - Sequencing facility
   - Base calling and quality control
   
   **Sequence alignment**:
   - Alignment algorithm (MUSCLE, MAFFT, ClustalW, etc.)
   - Manual editing procedures
   - Gap treatment
   - Trimming of ambiguous regions
   
   **Phylogenetic analysis**:
   - Complete StarBEAST3 settings:
     - Software version
     - Substitution models for each locus (how selected?)
     - Partitioning scheme
     - Clock model (strict or relaxed?)
     - Prior distributions for all parameters
     - MCMC chain length, burnin, sampling frequency
     - Number of independent runs
     - Convergence assessment method
   - Tree summarization method (maximum clade credibility, consensus)
   
   **Impact**: The methods section as currently written does **not meet minimum standards for reproducibility**. No other researcher could replicate this analysis based on the information provided.
   
   **Recommendation**: Expand methods section to include all details listed above.

6. **No baseline comparisons**: The manuscript does not compare StarBEAST3 results to:
   - Concatenated maximum likelihood analysis (RAxML, IQ-TREE)
   - Individual gene trees
   - Alternative coalescent methods (ASTRAL, SVDquartets)
   
   **Impact**: Readers cannot assess whether the four-lineage topology is robust to analytical method or whether it depends critically on the specific coalescent model assumptions.
   
   **Recommendation**: Add supplementary analyses showing concatenated ML tree and ASTRAL species tree. Discuss areas of agreement/disagreement.

### Major concerns:

7. **Sample size per lineage not reported**: The manuscript states "24 individuals" total but does not specify:
   - *P. z. zanzibaricus*: ? individuals
   - *P. z. udzungwensis*: ? individuals
   - *P. rondoensis*: ? individuals
   - Malawi lineage: ? individuals
   
   **Concern**: If some lineages are represented by only 1-2 individuals, the species tree may not capture within-lineage diversity. This is especially critical for the Malawi lineage—if only 1-2 individuals were sampled from a single locality, the "distinct lineage" conclusion may be premature.
   
   **Recommendation**: Clearly state sample size per lineage and discuss limitations of sparse sampling.

8. **Geographic coverage within lineages unclear**: For each lineage, readers need to know:
   - Are individuals from a single locality or multiple populations?
   - What is the geographic extent of sampling relative to the lineage's known range?
   - Are there unsampled populations that might harbor additional diversity?
   
   **Concern**: If each lineage is represented by individuals from a single locality, the phylogenetic inference may not capture population structure or geographic variation within lineages.
   
   **Recommendation**: Provide specimen table with collection localities and discuss geographic coverage.

9. **Sequencing success not reported**: The manuscript does not indicate:
   - Were all 24 individuals successfully sequenced for all 6 loci (144 sequences total)?
   - If not, what is the missing data percentage?
   - Is missing data randomly distributed or concentrated in certain individuals/loci?
   
   **Concern**: Substantial or non-random missing data can bias coalescent analyses, which model population processes based on allele frequencies and coalescent times.
   
   **Recommendation**: Report sequencing success matrix (24 individuals × 6 loci) and percentage of missing data.

10. **No absolute divergence times**: The manuscript reports relative times (proportions of tree height) rather than absolute ages. This severely limits:
    - Comparison to biogeographic events:
      - Zanzibar island formation (~5-6 Ma based on geology)
      - Pleistocene glacial cycles (2.6 Ma - 11.7 ka)
      - Last Glacial Maximum (~20 ka)
    - Assessment of diversification rates
    - Evaluation of whether divergences are Pliocene, Pleistocene, or Holocene
    
    **Concern**: Without absolute ages, statements like "recent island-mainland divergence" and "long-term isolation" are vague and cannot be tested against biogeographic hypotheses.
    
    **Recommendation**: Explore secondary calibrations from broader primate phylogenies (e.g., Pozzi et al. 2014 used 27 loci across Galagidae with fossil calibrations) or biogeographic priors (e.g., Zanzibar island age) to obtain approximate absolute ages.

11. **No population size estimates discussed**: StarBEAST3 models effective population sizes (theta parameters) for each branch. These estimates are biologically important for:
    - Comparing island vs. mainland population sizes
    - Assessing vulnerability to genetic drift
    - Identifying demographic bottlenecks
    - Informing conservation priorities (small populations are higher priority)
    
    **Concern**: Population size estimates are a key output of coalescent analyses but are not reported or discussed.
    
    **Recommendation**: Report theta estimates for each lineage and discuss biological implications (e.g., is Zanzibar population smaller than mainland, as expected for island populations?).

12. **No sensitivity analyses**: The manuscript does not test robustness to:
    - Prior distributions (especially population size priors)
    - Substitution model choice
    - Partitioning schemes
    - Clock model (strict vs. relaxed)
    - Outgroup selection
    
    **Concern**: The four-lineage topology may be sensitive to analytical assumptions. Without sensitivity analyses, we cannot assess robustness.
    
    **Recommendation**: Conduct sensitivity analyses varying key priors and models. Report whether the four-lineage topology is stable.

### Moderate concerns:

13. **No gene tree presentation**: Individual gene trees are not shown. This is important because:
    - The primary justification for MSC methods is to accommodate gene tree heterogeneity
    - Seeing which loci support vs. conflict with the species tree provides biological insights
    - Discordance could indicate incomplete lineage sorting, introgression, or gene flow
    
    **Recommendation**: Add supplementary figure showing six individual gene trees aligned for comparison.

14. **No mito-nuclear concordance analysis**: The manuscript does not:
    - Compare mitochondrial vs. nuclear gene trees
    - Test for significant cyto-nuclear discordance
    - Discuss implications for species boundaries
    
    **Concern**: Other African mammal studies have found substantial mito-nuclear discordance due to introgression or sex-biased dispersal (Demos et al. 2019; Petzold & Hassanin 2020). If present, discordance could indicate:
    - Historical hybridization between lineages
    - Male-biased dispersal with female philopatry
    - Incomplete reproductive isolation
    
    **Recommendation**: Conduct separate analyses of mitochondrial vs. nuclear loci and test for discordance.

15. **No integration with acoustic data**: Previous studies (Génin 2021; Pozzi et al. 2019) demonstrated species-specific loud-call differences in *Paragalago*. The manuscript does not:
    - Report acoustic data for Malawi specimens
    - Compare acoustic vs. genetic boundaries
    - Discuss concordance/discordance
    
    **Concern**: Acoustic divergence is a key line of evidence for species boundaries in galagos. Without acoustic data, the taxonomic status of the Malawi lineage remains uncertain.
    
    **Recommendation**: If acoustic recordings are available, include acoustic analysis. If not, acknowledge this as a critical limitation and priority for future work.

16. **No formal species delimitation tests**: While the manuscript presents a species tree, it does not formally test species boundaries using dedicated delimitation methods:
    - BPP (Bayesian species delimitation)
    - STACEY (species tree and classification estimation)
    - BFD* (Bayes factor delimitation)
    
    **Concern**: Given the taxonomic uncertainty (especially for the Malawi lineage) and conservation implications, formal delimitation tests would provide statistical support for species vs. subspecies boundaries.
    
    **Recommendation**: Implement BPP to test alternative delimitation scenarios (e.g., four species vs. three species with Malawi as subspecies of *P. zanzibaricus*).

17. **Conservation recommendations vague**: While the manuscript discusses conservation implications, it does not provide specific, actionable recommendations:
    - What IUCN threat category should each lineage receive?
    - Which forest fragments are highest priority for immediate protection?
    - What connectivity corridors are needed to maintain gene flow?
    - What monitoring protocols should be implemented?
    - Are translocation or captive breeding warranted?
    
    **Recommendation**: Add a "Conservation Recommendations" section with specific, actionable proposals for each lineage.

### Minor concerns:

18. **No comparison to previous phylogenetic hypotheses**: The manuscript should more explicitly compare the four-lineage topology to previous hypotheses:
    - Pozzi et al. (2020): three lineages in *zanzibaricus* complex
    - Masters et al. (2017): generic boundaries
    - Honess (1996): subspecies designations
    
    **Recommendation**: Add a table or supplementary figure comparing alternative topologies and discussing support for each.

19. **Locus selection not justified**: The manuscript does not explain why these specific six loci were chosen:
    - Were they selected based on phylogenetic informativeness?
    - Were they chosen for comparability with previous studies?
    - Were they the only loci that amplified successfully?
    
    **Recommendation**: Provide brief justification for locus selection in the methods section.

20. **GenBank accessions not provided**: All sequences must be deposited in GenBank with accession numbers listed. This is a **requirement** for publication in molecular systematics journals.
    
    **Recommendation**: Deposit sequences in GenBank and provide accession numbers in Table 1 or supplementary materials.

---

## Suggestions

### Essential for publication:

1. **Add Table 1 (Specimen Information)**: Include specimen ID, lineage, locality, GPS coordinates, collection date, collector, voucher number, GenBank accessions for all 6 loci.

2. **Add Table 2 (Locus Characteristics)**: Include alignment length, variable sites, parsimony-informative sites, missing data %, model selected for each locus.

3. **Add Table 3 (MCMC Diagnostics)**: Include chain length, burnin, sampling frequency, number of runs, ESS values for key parameters, convergence assessment.

4. **Add Figure 1 (Sampling Locality Map)**: Show collection localities color-coded by lineage, forest cover, protected areas, geographic barriers.

5. **Expand Methods section**: Include all specimen collection, DNA extraction, PCR, sequencing, alignment, and phylogenetic analysis details listed in "Weaknesses" section.

6. **Report population size estimates**: Discuss theta parameters from StarBEAST3 and their biological implications.

7. **Deposit sequences in GenBank**: Obtain accession numbers and list in manuscript.

### Strongly recommended:

8. **Attempt absolute divergence time estimation**: Use secondary calibrations from Pozzi et al. (2014) or biogeographic priors (Zanzibar island age) to obtain approximate absolute ages.

9. **Conduct baseline comparisons**: Show concatenated ML tree (RAxML or IQ-TREE) and ASTRAL species tree. Discuss agreement/disagreement with StarBEAST3 results.

10. **Present individual gene trees**: Add supplementary figure showing six gene trees aligned for comparison. Quantify discordance.

11. **Analyze mito-nuclear concordance**: Separately analyze mitochondrial vs. nuclear loci and test for significant discordance.

12. **Conduct sensitivity analyses**: Test robustness to prior distributions, substitution models, partitioning schemes, clock models.

13. **Add supplementary materials**: Include aligned sequences, StarBEAST3 XML file, tree file, MCMC trace plots.

14. **Integrate acoustic data if available**: If loud-call recordings exist for Malawi specimens, include acoustic analysis and test concordance with genetic boundaries.

15. **Conduct formal species delimitation**: Use BPP to test alternative delimitation scenarios and provide statistical support for species boundaries.

16. **Provide specific conservation recommendations**: Add section with actionable proposals for IUCN assessments, protected area designation, connectivity corridors, monitoring protocols.

### Recommended for strengthening manuscript:

17. **Discuss within-lineage diversity**: If sample sizes permit, analyze genetic diversity, heterozygosity, and population structure within each lineage.

18. **Compare to previous phylogenetic hypotheses**: Add table or figure comparing four-lineage topology to previous studies (Pozzi et al. 2020; Masters et al. 2017).

19. **Justify locus selection**: Explain why these six loci were chosen.

20. **Expand discussion of future directions**: Outline specific next steps for phylogenomic analyses, population genetics, integrative taxonomy, conservation genetics.

---

## Questions

1. **Sample size per lineage**: How many individuals represent each of the four lineages? Please provide a breakdown.

2. **Geographic coverage**: Are individuals from single localities or multiple populations within each lineage? What proportion of each lineage's known range is sampled?

3. **Sequencing success**: Were all 24 individuals successfully sequenced for all 6 loci? If not, what is the percentage of missing data, and is it randomly distributed?

4. **MCMC diagnostics**: What were the ESS values for tree topology, divergence times, and population sizes? How many independent runs were conducted? Did they converge?

5. **Population size estimates**: What are the effective population size (theta) estimates for each lineage? Do they differ significantly (e.g., island vs. mainland)?

6. **Gene tree discordance**: Do all six loci support the same four-lineage topology, or is there conflict? If there is conflict, which nodes show discordance?

7. **Mito-nuclear concordance**: Do mitochondrial and nuclear loci support the same topology? Is there evidence of cyto-nuclear discordance?

8. **Absolute divergence times**: Why was absolute time estimation not attempted? Could secondary calibrations from Pozzi et al. (2014) be applied?

9. **Concatenated analysis**: How does the StarBEAST3 species tree compare to a concatenated maximum likelihood analysis? Are the topologies identical?

10. **Sensitivity to priors**: How sensitive are the results to population size priors and clock rate priors? Were alternative priors tested?

11. **Acoustic data**: Are loud-call recordings available for the Malawi specimens? If so, do they show diagnostic differences? If not, is this a priority for future fieldwork?

12. **Species delimitation**: Were formal species delimitation methods (BPP, STACEY) considered? If not, why not?

13. **Malawi lineage sampling**: How many individuals represent the Malawi lineage? Are they from a single locality (e.g., Mount Mulanje) or multiple sites?

14. **Type locality sampling**: Are there plans to sample from the *P. granti* type locality (Mount Kilimanjaro region) to resolve the taxonomic identity of the Malawi lineage?

15. **Conservation status**: What are the current IUCN threat categories for each lineage? Should they be reassessed based on these molecular findings?

16. **Habitat loss**: What is the current status of forest cover in the key areas (Rondo Plateau, Malawi montane forests, Udzungwa Mountains, Zanzibar)? How much habitat has been lost in recent decades?

17. **Population sizes**: What are the estimated census population sizes for each lineage? Are any lineages at immediate risk of extinction?

18. **Connectivity**: Is there evidence of gene flow among adjacent lineages (e.g., between Zanzibar and mainland Tanzania)? What geographic barriers prevent dispersal?

19. **Outgroup choice**: Why was *Otolemur garnettii* chosen as the outgroup? Were other galagids considered?

20. **Future phylogenomics**: Are there plans for phylogenomic analyses (RADseq, UCEs, whole genomes) to obtain higher resolution?

---

## Rating: 7/10

**Recommendation: Accept with major revisions**

**Justification**: This manuscript makes important empirical contributions—particularly the first molecular data from Malawi populations—and applies appropriate analytical methods (StarBEAST3 multispecies coalescent). The four-lineage structure is well-supported and provides a valuable framework for taxonomy, biogeography, and conservation. However, the manuscript has **critical deficiencies in experimental reporting** that must be addressed before publication:

**Must be addressed**:
- Add specimen information table with voucher numbers and GenBank accessions
- Add molecular data summary table (locus characteristics)
- Add MCMC diagnostics table
- Add sampling locality map
- Substantially expand methods section with all experimental details
- Deposit sequences in GenBank

**Strongly recommended**:
- Attempt absolute divergence time estimation
- Conduct baseline comparisons (concatenated ML, ASTRAL)
- Present individual gene trees
- Analyze mito-nuclear concordance
- Report population size estimates
- Conduct sensitivity analyses
- Add supplementary materials

With these revisions, the manuscript will be a strong contribution suitable for publication in leading systematic biology, molecular ecology, or conservation genetics journals (e.g., *Molecular Phylogenetics and Evolution*, *Molecular Ecology*, *Conservation Genetics*, *BMC Evolutionary Biology*).

The empirical contribution (Malawi molecular data) alone justifies publication, but the experimental reporting must meet journal standards for reproducibility and rigor.

---

## Confidence: 4/5 (High)

**Justification**: I am highly confident in this assessment based on:

1. **Extensive experience reviewing molecular phylogenetic studies**: I have evaluated numerous multilocus phylogenetic manuscripts and am familiar with journal standards for experimental reporting and data presentation.

2. **Expertise in conservation genetics**: I understand the practical requirements for translating phylogenetic findings into conservation action and can assess the manuscript's applied impact.

3. **Knowledge of *Paragalago* literature**: I have reviewed the key prior studies (Masters et al. 2017; Pozzi et al. 2020, 2014; Génin 2021; Karlsson 2006-2011) and understand the empirical context.

4. **Familiarity with East African biogeography**: I have sufficient knowledge of Eastern Arc Mountains, Afromontane refugia, and island-mainland systems to evaluate the biogeographic interpretations.

**Minor uncertainty**: My confidence is not absolute (5/5) because:
- I have not seen the actual sequence alignments, StarBEAST3 output files, or supplementary materials, only the manuscript text
- Some experimental details may be present in materials not provided for this review
- I am not a field expert on galago ecology or behavior, so some ecological interpretations may benefit from additional specialist review

Overall, I am confident that the identified deficiencies in experimental reporting are valid and that addressing them is essential for publication.
