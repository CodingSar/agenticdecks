# Natural selection and population genetics

> **Layer:** [04 Genetics, Evolution and Development](../README.md) › [Evolution](README.md)
> **Builds on:** [Probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md), [Genomic variation and mutation](../01-inheritance/genomic-variation-and-mutation.md), [Mendelian inheritance and pedigrees](../01-inheritance/mendelian-inheritance-and-pedigrees.md), [Compartment models and exponential processes](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md)
> **Enables:** [Evolutionary medicine](evolutionary-medicine.md), [Host–pathogen coevolution and resistance](host-pathogen-coevolution-and-resistance.md), [Causes of cancer](../../08-pathology/03-neoplasia/causes-of-cancer.md), [Infectious disease dynamics](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md)

## Essence

Evolution is a change in the frequency of alleles in a population over generations. It needs only variation (mutation), inheritance (meiosis and Mendel) and differential reproduction. When an allele raises the expected number of surviving offspring of its carriers, its frequency rises: that is natural selection. When frequencies change by sampling chance alone, that is drift. The single idea is **the fate of an allele is decided by its effect on reproduction, not on health, and by the size of the population it lives in**. This arithmetic explains why genetic diseases persist, how bacteria defeat antibiotics in weeks and how tumours defeat chemotherapy in months: an infection and a tumour are populations evolving inside a patient.

## Core tenets

1. **Without evolutionary forces, allele frequencies do not change: that is the null model.** In a large, randomly mating population with no mutation, selection or migration, an allele of frequency p stays at p and genotypes settle at p², 2pq and q² (Hardy–Weinberg, 1908; [probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md)). Deviation reveals a force at work, and the model gives carrier frequencies directly: cystic fibrosis affects ~1 in 2,500 births of Northern European ancestry, so q = 1/50 and the carrier frequency 2pq ≈ 1 in 25.

2. **Selection changes frequency at a rate set by the selection coefficient and by dominance.** If carriers leave (1 + s) offspring for every one left by non-carriers, frequency changes by roughly s × p × q per generation. A 1% advantage takes ~1,000 generations to carry an allele from 1% to 99%: ~25,000 years for humans, a few weeks for bacteria. A dominant harmful allele is exposed in every carrier and eliminated fast; a rare recessive one hides in carriers and lingers for thousands of generations.

3. **Mutation and selection balance, and that sets the frequency of most Mendelian diseases.** New copies arise at rate μ per generation; selection removes a fraction s of those present. At equilibrium the frequency is about μ/s for a dominant allele and √(μ/s) for a recessive one. For a dominant lethal the frequency equals the mutation rate (~10^-5 to 10^-6), the observed incidence of such disorders. A disease that treatment has stopped punishing rises in frequency only over many generations.

4. **Drift dominates in small populations, producing founder effects.** In a population of effective size N a frequency wanders by about √(pq/2N) per generation, and selection cannot act on an allele whose coefficient is below ~1/N. When a population is founded by a few hundred people, whatever they carried becomes common: Tay–Sachs disease in Ashkenazi Jews, hereditary tyrosinaemia in Quebec, variegate porphyria in Afrikaners.

5. **Balancing selection keeps harmful alleles common when the heterozygote has an advantage.** The sickle cell allele is lethal in untreated homozygotes yet reaches 10–20% in parts of West Africa, because heterozygotes are strongly protected against death from *Plasmodium falciparum* malaria; its distribution maps historical malaria ([human variation](human-evolution-and-variation.md)). Frequency-dependent selection maintains the extreme diversity of the Major Histocompatibility Complex: a rare allele presents pathogens the common ones have been adapted to.

6. **Selection acts on reproduction, so it is blind to late-life disease.** An allele that kills at 70 has already been passed on; one that kills at 7 has not. The force of selection declines with age (Medawar, 1952; Hamilton, 1966), so mutations harmful only late in life accumulate unopposed, and alleles that help early reproduction at the cost of later disease are favoured. This founds the evolutionary theory of ageing ([evolutionary medicine](evolutionary-medicine.md)); Huntington disease (onset ~40) persists because carriers have usually reproduced first.

7. **Populations evolving inside a patient follow the same rules at microbial speed.** A bacterial infection holds ~10^9–10^12 cells with a mutation rate of ~10^-9 per base per division, so every single-base resistance mutation already exists before an antibiotic is given; the drug selects it rather than creating it ([host–pathogen coevolution](host-pathogen-coevolution-and-resistance.md)). A tumour at diagnosis holds ~10^9 cells in subclones; chemotherapy kills the sensitive majority and the resistant minority regrows, which is why cure needs combination therapy ([causes of cancer](../../08-pathology/03-neoplasia/causes-of-cancer.md)).

8. **Selection is detectable in the genome, and the signatures name the pressures.** A beneficial allele sweeps through a population carrying neighbouring variants, leaving long shared haplotypes. In humans the strongest recent signals are in genes for diet (lactase persistence), pathogen defence (malaria genes, Human Leukocyte Antigen (HLA) loci), pigmentation and altitude. Infection has been the dominant selective force on the human genome in the Holocene ([infectious disease dynamics](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md)).

## Key concepts

| Term | Meaning |
|---|---|
| Fitness | Expected number of offspring of a genotype relative to others |
| Selection coefficient (s) | Proportional fitness difference between genotypes |
| Hardy–Weinberg equilibrium | Genotype frequencies p², 2pq, q² when no evolutionary force acts |
| Genetic drift | Random change in allele frequency from sampling; strong in small populations |
| Founder effect / bottleneck | High frequency of an allele because the founders happened to carry it |
| Mutation–selection balance | Equilibrium at which new mutations equal those removed by selection |
| Balancing selection | Maintenance of both alleles by heterozygote advantage or frequency dependence |
| Clonal evolution | Selection among somatic or microbial clones within one host |

## How it fits

- **Below:** the arithmetic is [probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md) and [exponential growth](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md); the raw material is [mutation](../01-inheritance/genomic-variation-and-mutation.md); the transmission rules are [Mendel's](../01-inheritance/mendelian-inheritance-and-pedigrees.md).
- **Above:** [evolutionary medicine](evolutionary-medicine.md) and [host–pathogen coevolution](host-pathogen-coevolution-and-resistance.md) apply it; [antimicrobials](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/antimicrobials.md) and [anticancer drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md) fight populations that evolve; [infectious disease epidemiology](../../10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md) tracks selection in pathogens.
- **Siblings:** this leaf supplies the mechanism that [evolutionary medicine](evolutionary-medicine.md) interprets, that [host–pathogen coevolution](host-pathogen-coevolution-and-resistance.md) runs at speed, and that produced [human variation](human-evolution-and-variation.md).

## Common misconceptions

- **"Selection favours health or survival."** It favours reproduction; a trait that shortens life after reproduction is invisible to it.
- **"Harmful alleles should have been eliminated by now."** Recessive alleles hide in carriers, mutation replenishes them, drift fixes them in small populations and heterozygote advantage can maintain them.

## Go deeper

- Daniel L. Hartl and Andrew G. Clark, *Principles of Population Genetics* (4th ed., 2007): the standard quantitative text.
- Charles Darwin, *On the Origin of Species* (1859): the argument from variation, inheritance and struggle, still the clearest statement of the logic.
- Mel Greaves and Carlo C. Maley, "Clonal Evolution in Cancer", *Nature* (2012): the tumour as an evolving population.
