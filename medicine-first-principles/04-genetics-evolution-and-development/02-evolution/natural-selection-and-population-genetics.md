# Natural selection and population genetics

> **Layer:** [04 Genetics, Evolution and Development](../README.md) › [Evolution](README.md)
> **Builds on:** [Probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md), [Genomic variation and mutation](../01-inheritance/genomic-variation-and-mutation.md), [Mendelian inheritance and pedigrees](../01-inheritance/mendelian-inheritance-and-pedigrees.md), [Compartment models and exponential processes](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md)
> **Enables:** [Evolutionary medicine](evolutionary-medicine.md), [Host–pathogen coevolution and resistance](host-pathogen-coevolution-and-resistance.md), [Causes of cancer](../../08-pathology/03-neoplasia/causes-of-cancer.md), [Infectious disease dynamics](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md)

## Essence

Evolution is a change in the frequency of alleles in a population over generations. It needs only three things, all established in the previous area: variation (mutation), inheritance (meiosis and Mendel) and differential reproduction. When an allele raises the expected number of surviving offspring of its carriers, even slightly, its frequency rises: that is natural selection. When frequencies change by sampling chance alone, that is drift, and in small populations drift beats selection. Population genetics is the arithmetic of these forces, and the single idea is **the fate of an allele is decided by its effect on reproduction, not on health, and by the size of the population it lives in**. This arithmetic explains why genetic diseases persist, why some are common in particular populations, how bacteria defeat antibiotics in weeks and how tumours defeat chemotherapy in months: a tumour and an infection are populations evolving inside a patient.

## Core tenets

1. **Without evolutionary forces, allele frequencies do not change: that is the null model.** In a large, randomly mating population with no mutation, selection or migration, an allele of frequency p stays at p, and genotype frequencies settle at p², 2pq and q² in one generation (Hardy–Weinberg, 1908) ([probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md)). The model is useful because of its failures: deviation reveals a force at work. It also gives the carrier frequency of a recessive disease directly. Cystic fibrosis affects ~1 in 2,500 births of Northern European ancestry, so q² = 1/2,500, q = 1/50, and the carrier frequency 2pq ≈ 1 in 25. A recessive allele is mostly hidden in carriers, which is why selection against the disease removes it very slowly.

2. **Selection changes frequency at a rate set by the selection coefficient and the dominance of the allele.** If carriers of an allele leave (1 + s) offspring for every one left by non-carriers, the allele's frequency changes by roughly s × p × q per generation when it is co-dominant. A 1% advantage takes ~1,000 generations to move an allele from 1% to 99%; in human terms ~25,000 years, in bacterial terms a few weeks. A dominant harmful allele is exposed to selection in every carrier and is eliminated fast, so dominant lethal diseases exist mainly through new mutation (achondroplasia). A recessive harmful allele at low frequency is almost invisible to selection, since nearly all copies are in healthy heterozygotes, so it lingers for thousands of generations.

3. **Mutation and selection reach a balance, which sets the frequency of most Mendelian diseases.** New copies of a harmful allele arise each generation at rate μ; selection removes a fraction s of the copies present. At equilibrium the frequency is about μ/s for a dominant allele and √(μ/s) for a recessive one. For a dominant lethal, frequency equals the mutation rate (~10^-5 to 10^-6), which is the observed incidence of such disorders. The formula explains why rare diseases are rare but never absent, and why a disease that selection has stopped punishing (haemophilia now treated, phenylketonuria now managed) will rise in frequency only over many generations and very slowly.

4. **Drift dominates in small populations, producing founder effects and the clustering of diseases in isolated groups.** Each generation samples alleles from the last; in a population of effective size N an allele's frequency wanders by about √(pq/2N) per generation. Selection cannot act on an allele whose selection coefficient is smaller than ~1/N. When a population is founded by a few hundred people and grows, whatever those founders carried becomes common: Tay–Sachs disease and several others in Ashkenazi Jews, hereditary tyrosinaemia in Quebec, variegate porphyria in South African Afrikaners, Ellis–van Creveld syndrome in the Amish. The human population passed through bottlenecks of ~10,000 effective breeding individuals, which is why humans are genetically less diverse than most great apes despite being far more numerous.

5. **Balancing selection keeps harmful alleles common when the heterozygote has an advantage.** The sickle cell allele is lethal in homozygotes without treatment yet reaches 10–20% in parts of West Africa, because heterozygotes are ~90% protected against death from *Plasmodium falciparum* malaria. The equilibrium frequency is set by the ratio of the two disadvantages, and the allele's geographic distribution maps historical malaria exactly. Thalassaemias, glucose-6-phosphate dehydrogenase deficiency and Duffy-negative blood group have the same explanation ([human variation](human-evolution-and-variation.md)). Balancing selection by frequency dependence maintains the extreme diversity of the Major Histocompatibility Complex: a rare allele presents pathogens the common ones have been adapted to by the pathogen.

6. **Selection acts on reproduction, so it is weak after reproductive age and blind to late-life disease.** An allele that kills at 70 has already been passed on; one that kills at 7 has not. The force of selection declines with age (Medawar, 1952; Hamilton, 1966), so mutations harmful only in late life accumulate in the genome unopposed, and alleles that help early reproduction at the cost of later disease are positively favoured. This single fact is the foundation of the evolutionary theory of ageing and of much of [evolutionary medicine](evolutionary-medicine.md): Huntington disease (onset ~40) persists at a frequency far above the mutation–selection balance for a lethal allele because carriers have usually reproduced before symptoms.

7. **Populations evolving inside a patient follow the same rules at microbial speed.** A bacterial infection contains ~10^9–10^12 cells with a mutation rate of ~10^-9 per base per division, so every single-base resistance mutation already exists somewhere in the population before an antibiotic is given; the drug does not create resistance, it selects it ([host–pathogen coevolution](host-pathogen-coevolution-and-resistance.md)). A tumour at diagnosis holds ~10^9 cells with thousands of mutations each, spatially separated into subclones; chemotherapy kills the sensitive majority and the resistant minority regrows, which is clonal evolution and the reason cure requires combination therapy or eradication of every cell ([causes of cancer](../../08-pathology/03-neoplasia/causes-of-cancer.md)). Fisher's geometric reasoning applies: large populations with high mutation rates adapt fast, which is the argument for treating early, hard and with several drugs at once.

8. **Selection is detectable in the genome, and the signatures point to the pressures that shaped us.** A beneficial allele sweeps through a population carrying neighbouring variants with it, leaving a stretch of reduced diversity and long shared haplotypes; comparing the ratio of protein-changing to silent changes between species finds genes under positive or purifying selection. In humans the strongest recent signals are in genes for diet (lactase persistence in dairying populations, ~10,000 years), pathogen defence (the malaria genes above, the CCR5 and HLA loci), skin pigmentation and altitude (EPAS1 in Tibetans). Infection has been the dominant selective force on the human genome in the Holocene, which is why so much human variation is immunological ([infectious disease dynamics](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md)).

## Key concepts

| Term | Meaning |
|---|---|
| Fitness | Expected number of offspring of a genotype relative to others; the currency of selection |
| Selection coefficient (s) | Proportional fitness difference between genotypes |
| Hardy–Weinberg equilibrium | Genotype frequencies p², 2pq, q² when no evolutionary force acts |
| Genetic drift | Random change in allele frequency from sampling; strong when the population is small |
| Effective population size | The size of an idealised population with the same drift as the real one |
| Founder effect / bottleneck | High frequency of an allele because the founders happened to carry it |
| Mutation–selection balance | Equilibrium frequency at which new mutations equal those removed by selection |
| Balancing selection | Maintenance of both alleles, by heterozygote advantage or frequency dependence |
| Selective sweep | Rapid rise of a beneficial allele that reduces diversity around it |
| Clonal evolution | Selection among somatic or microbial clones within one host |

## How it fits

- **Below:** the arithmetic is [probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md) and [exponential growth](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md); the raw material is [mutation](../01-inheritance/genomic-variation-and-mutation.md); the transmission rules are [Mendel's](../01-inheritance/mendelian-inheritance-and-pedigrees.md).
- **Above:** [evolutionary medicine](evolutionary-medicine.md) and [host–pathogen coevolution](host-pathogen-coevolution-and-resistance.md) apply it to the body and its microbes; [antimicrobials](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/antimicrobials.md) and [anticancer therapy](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md) fight populations that evolve; [infectious disease epidemiology](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md) tracks selection in pathogen populations.
- **Siblings:** this leaf supplies the mechanism that [evolutionary medicine](evolutionary-medicine.md) interprets, that [host–pathogen coevolution](host-pathogen-coevolution-and-resistance.md) runs at speed, and that produced the [human variation](human-evolution-and-variation.md) of the last leaf.

## Common misconceptions

- **"Selection favours health or survival."** It favours reproduction. A trait that shortens life after reproduction is invisible to it; one that raises offspring count at the cost of health is favoured.
- **"Harmful alleles should have been eliminated by now."** Recessive alleles hide in carriers, mutation replenishes them, drift fixes them in small populations and heterozygote advantage can actively maintain them.
- **"Antibiotics cause bacteria to mutate."** Resistance mutations arise at the background rate whether or not the drug is present; the drug selects the pre-existing mutants.

## Go deeper

- Daniel L. Hartl and Andrew G. Clark, *Principles of Population Genetics* (4th ed., 2007): the standard quantitative text.
- John H. Gillespie, *Population Genetics: A Concise Guide* (2nd ed., 2004): the essential models in a short book.
- Charles Darwin, *On the Origin of Species* (1859): the argument from variation, inheritance and struggle, still the clearest statement of the logic.
- Mel Greaves and Carlo C. Maley, "Clonal Evolution in Cancer", *Nature* (2012): the tumour as an evolving population.
