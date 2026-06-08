## TL;DR

This manuscript applies StarBEAST3 multispecies coalescent to a six-locus Paragalago dataset, increasing resolution over prior mtDNA-dominated and concatenated studies and directly informs taxonomy, biogeography, and conservation needs for understudied Malawi populations.

----

## Novelty and methods

This section explains why a six‑locus StarBEAST3 species‑tree is a methodological and interpretive advance for Paragalago systematics and how this compares to prior approaches. The manuscript’s novelty lies in applying the recent StarBEAST3 multispecies coalescent implementation to a focused Paragalago dataset that combines three mitochondrial and three nuclear loci, enabling joint estimation of species tree topology and divergence times while explicitly modeling incomplete lineage sorting.

- **Why this is novel** The StarBEAST3 framework used here provides cutting‑edge MCMC proposals and relaxed‑clock integration for rapid, coherent multispecies coalescent inference, a capability emphasized by Douglas and Bouckaert 2022 [1].  
- **How this compares to earlier galago work** Earlier Paragalago and galagid studies often relied heavily on mitochondrial markers, acoustic data, concatenated multilocus analyses, or separate gene trees rather than an explicit MSC species‑tree: Pozzi et al. 2020 combined mitochondrial and nuclear loci for the zanzibaricus complex but did not report an explicit StarBEAST3 species‑tree framework [2]; Pozzi et al. 2014 assembled a broad 27‑locus dataset across Galagidae and used concatenated and coalescent methods at family scale but did not focus on fine‑scale multispecies coalescent inference within Paragalago with the same targeted locus set [3].  
- **Advantages for closely related taxa** MSC methods directly address gene tree heterogeneity and incomplete lineage sorting, improving accuracy for recent divergences typical of cryptic radiations; this benefit has been demonstrated in primate studies using MSC frameworks and extensive genomic segments [4] and in cryptic nocturnal primate delimitations where MSC aided delimitation and divergence estimation [5].

----

## Taxonomy and key related work

This section summarizes prior molecular and integrative studies that have addressed Paragalago taxonomy (including P. zanzibaricus, P. rondoensis, P. granti, P. nyasae) and lists the most relevant papers the manuscript should cite and contrast. Several targeted studies and syntheses have shaped current Paragalago taxonomy, but geographic and molecular gaps remain, especially for Malawi populations.

- Table of directly relevant studies

| Study and year | Focus and main result |
|---|---|
| Masters et al. 2017 [6] | Proposed the new genus Paragalago based on morphological, craniodental, and molecular evidence [6]. |
| Pozzi et al. 2020 [2] | Multilocus (mitochondrial + nuclear) analyses support three lineages in the P. zanzibaricus complex and test species limits [2]. |
| Pozzi et al. 2019 [7] | Combined mitochondrial cytochrome b and acoustic data to validate P. cocos and P. zanzibaricus as distinct taxa at the mtDNA level [7]. |
| Génin 2021 [8] | Demonstrated species‑specific loud‑call differences and sensory‑drive hypotheses; provided behavioral evidence validating multiple species in the complex [8]. |
| Pozzi 2014 [3] | Broad multilocus galagid phylogeny (27 loci) showing deep lineages and non‑monophyly of some dwarf galago groups, informing generic rearrangements [3]. |
| Delpero et al. 2000 [9] | Early mitochondrial sequencing across bushbaby taxa showing mtDNA signal useful for generic classification, including G. zanzibaricus sampling [9]. |
| Karlsson 2006/2009/2011 [10] [11] [12] | Field survey proposals and reports highlighting severe sampling gaps and taxonomic uncertainty for Malawian galagos (e.g., G. nyasae) and calling for molecular/vocal inventories [10] [11] [12]. |
| Penna & Pozzi 2024 review [13] | Recent synthesis of galagid systematics, highlighting integration of acoustics and genetics and remaining geographic sampling gaps [13]. |

- **What prior molecular work found** Pozzi et al. 2020 and Pozzi et al. 2019 provide the most direct molecular support for multiple lineages within the zanzibaricus complex and corroborate acoustic evidence for species boundaries in Paragalago [2] [7]. Masters et al. 2017 formalized the generic reclassification that recognized Paragalago as distinct from Galagoides [6]. Delpero et al. 2000 and Pozzi 2014 provided broader mitochondrial and multilocus contexts for placement of the Zanzibar complex within Galagidae [9] [3].  
- **Gaps for Malawi populations** Field‑based proposals and reports by Karlsson (2006, 2009, 2011) emphasize that Malawian populations (including taxa referred to as Galagoides nyasae and several putative undescribed Galagoides) remain poorly sampled molecularly and taxonomically, representing a clear geographic gap in published molecular datasets [10] [11] [12]. Pozzi et al. 2020 also noted that molecular data remain sparse for some Paragalago lineages at the population level [2].

----

## Biogeographic drivers

This section places Paragalago diversification into the broader regional biogeographic framework (Eastern Arc, Afromontane refugia, island–mainland divergence, fragmentation) using prior empirical syntheses. Multiple studies implicate climatic cycles, montane refugia, and island isolation in shaping galagid and related forest taxa diversification in eastern Africa.

- **Forest dynamics and refugia** Pozzi 2016 synthesized galagid diversification in the context of forest expansion and contraction over the Cenozoic and Plio‑Pleistocene, arguing that climatic cycles and Miocene uplift events contributed substantially to galagid lineage divergences and distributions [14]. Comparable phylogeographic studies in Afrotropical forest taxa show Pleistocene refugia in montane and lowland forests driving lineage divergence, supporting the refugial model applied to small mammals and primates [15].  
- **Island versus mainland divergence** The Zanzibar/Mafia island populations of P. zanzibaricus and related taxa have long been recognized as genetically and acoustically distinct, consistent with island‑mainland divergence and local acoustic adaptation documented for Paragalago loud calls in Génin 2021 and earlier mitochondrial work by Delpero et al. 2000 [8] [9].  
- **Forest fragmentation at fine scales** Acoustic‑based taxonomic studies and surveys in Tanzania emphasize how forest 'islands' (Eastern Arc and coastal forest fragments) promote microendemism and recent speciation in galagos, with vocal divergence often mapping onto isolated forest patches and supporting scenarios of isolation during forest contraction [16] [8]. Pozzi 2014 and Pozzi 2016 place these processes in a temporal framework of Miocene to Pleistocene events affecting galagid diversification [3] [14].

----

## Conservation relevance and remaining questions

This section summarizes conservation‑focused genetic and phylogeographic work on endangered nocturnal primates in East African fragmented forests and explains how the current manuscript aids conservation prioritization, then lists unresolved questions the literature still leaves open. Conservation urgency for cryptic galagos has been repeatedly emphasized because taxonomic splitting and restricted ranges change threat assessments.

- **Existing conservation‑relevant studies** Karlsson’s Malawi surveys and project proposals highlight severe sampling and status data gaps for Malawian galagos and the urgent need for baseline genetic, acoustic, and distributional data in deforestation‑threatened forests [10] [11] [12]. Honess 1996 and related field work link discovery of new, range‑restricted galago taxa in Eastern Arc and coastal forests to immediate conservation concern and IUCN assessments [16]. Recent reviews synthesize how improved taxonomic resolution affects conservation planning for galagids [13].  
- **How multilocus MSC helps conservation** Multilocus MSC analyses can clarify species limits, divergence times, and effective population processes that are critical for red‑listing and management; examples where MSC informed cryptic primate conservation include MSC delimitation in mouse lemurs and broader primate multispecies coalescent studies that improved divergence inference [5] [4]. By providing a species tree and divergence estimates for Paragalago lineages (including under‑sampled Malawi populations), the present manuscript supplies the taxonomic and temporal evidence needed to reassess conservation units and prioritize forest fragments for protection.  
- **Unanswered conservation questions** Key unresolved items include: the taxonomic status and range limits of Malawian populations (Karlsson 2006/2009/2011) [10] [11] [12], the extent of mito‑nuclear discordance or historic gene flow among adjacent Paragalago lineages (observed as an issue in other mammal studies [17] [18]), and integration of acoustic, genomic, and demographic data to translate phylogenetic splits into practical management units [8] [13].

----