# Mendelian inheritance and pedigrees

> **Layer:** [04 Genetics, Evolution and Development](../README.md) › [Inheritance](README.md)
> **Builds on:** [Mitosis, meiosis and chromosome segregation](../../03-cell-biology/02-the-cell-life-cycle/mitosis-meiosis-and-chromosome-segregation.md), [Probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md), [Bayesian reasoning](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md), [Proteins: structure and folding](../../02-biochemistry-and-molecular-biology/01-macromolecules/proteins-structure-and-folding.md)
> **Enables:** [Single-gene and chromosomal disorders](../../08-pathology/04-genetic-metabolic-and-environmental-disease/single-gene-and-chromosomal-disorders.md), [Congenital and genetic disease in childhood](../../14-life-course-mind-and-integrative-care/01-paediatrics/congenital-and-genetic-disease-in-childhood.md), [Pregnancy and its complications](../../14-life-course-mind-and-integrative-care/02-obstetrics-and-gynaecology/pregnancy-and-its-complications.md), [Natural selection and population genetics](../02-evolution/natural-selection-and-population-genetics.md)

## Essence

Mendel's insight (1866) was that heredity is particulate: each parent passes one of two copies of each factor, the copies do not blend, and which copy is passed is a matter of chance. Meiosis is the mechanism: the two alleles of a gene sit on homologous chromosomes that segregate to different gametes. A pedigree is a diagram of who is related to whom and who is affected, and reading one is applied probability: from the pattern of affected relatives one infers the mode of inheritance, and from the mode one computes the risk to the next child. The idea that makes the whole subject work is **one gene, two alleles, random segregation**, from which dominant, recessive and X-linked patterns follow as arithmetic. Around 7,000 single-gene disorders are known; individually rare, together they affect ~1% of births and fill a large share of paediatric wards. Genetic counselling is this leaf applied to one family.

## Core tenets

1. **Segregation and independent assortment are facts about meiosis.** A diploid cell has two alleles of every autosomal gene; meiosis I separates the homologues, so a gamete carries one allele chosen with probability 1/2 ([meiosis](../../03-cell-biology/02-the-cell-life-cycle/mitosis-meiosis-and-chromosome-segregation.md)). Genes on different chromosomes assort independently; genes on the same chromosome travel together unless a crossover separates them, with probability that rises with distance (1% recombination defines a centimorgan, ~1 million base pairs on average). Linkage is how disease genes were mapped before sequencing, and it is why a marker near a gene can track it through a family.

2. **Dominance is a statement about the heterozygote's phenotype, and it has molecular reasons.** An allele is dominant if one copy is enough to produce the trait. This happens when half the normal protein is insufficient (haploinsufficiency: most transcription factor and structural protein disorders, such as Marfan syndrome), when the mutant protein poisons the normal one in a multimer (dominant negative: glycine substitutions in collagen), or when the mutation activates the protein (gain of function: achondroplasia's constitutively active fibroblast growth factor receptor 3). Recessive disorders are mostly loss of enzymes: one working copy supplies enough catalysis because enzymes are not rate-limiting at half dose ([enzymes](../../02-biochemistry-and-molecular-biology/01-macromolecules/enzymes-and-catalysis.md)). Dominance is therefore not a property of the allele alone but of the biochemistry it sits in.

3. **Each mode of inheritance has a signature in the pedigree.** Autosomal dominant: every generation affected, both sexes, an affected parent transmits to half of children, male-to-male transmission possible. Autosomal recessive: affected children of unaffected carrier parents, 1 in 4 recurrence, consanguinity raises the odds, often a single generation. X-linked recessive: affected males, carrier mothers, no male-to-male transmission, half of a carrier's sons affected and half of her daughters carriers (haemophilia, Duchenne muscular dystrophy). X-linked dominant and mitochondrial (maternal transmission to all children, variable severity) complete the set. The table below gives the arithmetic.

   | Mode | Risk to child of affected parent | Risk to child of two carriers | Sex pattern |
   |---|---|---|---|
   | Autosomal dominant | 1/2 | (both affected: 3/4) | Equal |
   | Autosomal recessive | Low unless partner is a carrier | 1/4 affected, 1/2 carrier | Equal |
   | X-linked recessive | Affected father: all daughters carriers, no sons affected | Carrier mother: 1/2 sons affected, 1/2 daughters carriers | Males affected |
   | Mitochondrial | Affected mother: all children (variable); affected father: none | | Maternal line |

4. **Penetrance and expressivity are why the arithmetic does not always match the family.** Penetrance is the fraction of genotype carriers who show the phenotype at all; expressivity is how severely. Hereditary breast and ovarian cancer from a BRCA1 mutation has ~60–80% lifetime penetrance for breast cancer, so an unaffected carrier mother is common. Neurofibromatosis type 1 is fully penetrant but varies from a few skin spots to disfiguring tumours within one family. Reduced penetrance comes from modifier genes, environment and chance (a second somatic hit for tumour suppressors), and it is the usual reason a dominant disease "skips" a generation.

5. **New mutations, mosaicism and anticipation break naive expectations.** Many dominant disorders arise as new mutations (most achondroplasia; ~1/3 of Duchenne cases), so no family history does not exclude a genetic disease and the recurrence risk to the parents is low, but not zero, because a mutation present in a fraction of a parent's germ cells (germline mosaicism) can recur. Trinucleotide repeat disorders (Huntington disease, myotonic dystrophy, fragile X) show anticipation: the repeat expands at each transmission, so onset is earlier and severity greater in each generation. Anticipation was once dismissed as an observation bias; the molecular mechanism vindicated it.

6. **Bayesian calculation is the core of genetic counselling.** A woman whose brother has Duchenne muscular dystrophy has a prior carrier probability of 1/2 (if her mother is an obligate carrier). If she has had three unaffected sons, the probability of that outcome is 1/8 if she is a carrier and 1 if she is not; the posterior carrier probability is (1/2 × 1/8) / (1/2 × 1/8 + 1/2 × 1) = 1/9 ([Bayesian reasoning](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md)). Biochemical tests and sequencing add further likelihood ratios. Counselling communicates these numbers, the options (prenatal or preimplantation diagnosis, testing relatives) and their implications without directing the choice.

7. **Genotype–phenotype relations are rarely one-to-one.** The same gene can cause several diseases depending on the mutation (different mutations in the cystic fibrosis gene cause classic cystic fibrosis, isolated male infertility or pancreatitis), and the same disease can result from mutations in many genes (locus heterogeneity: retinitis pigmentosa has >80 causative genes). Compound heterozygotes carry two different recessive alleles of one gene. These complications do not refute Mendel; they show that "one gene, one disease" was always an approximation of "one gene, one protein, many contexts".

8. **Mendelian disease is the proving ground for mechanism and for therapy.** Because a single defect produces the phenotype, Mendelian disorders have revealed the function of genes that complex disease only hints at: familial hypercholesterolaemia gave the LDL receptor pathway and the statins; cystic fibrosis gave the chloride channel and, in the 2010s, small-molecule correctors and potentiators; spinal muscular atrophy gave antisense and gene therapies in the 2010s–2020s. The pathway from a rare Mendelian disease to a common treatment is a recurring pattern in [drug development](../../09-pharmacology-and-therapeutics/05-drug-development-and-toxicology/from-target-to-approval.md).

## Key concepts

| Term | Meaning |
|---|---|
| Allele | One of the alternative versions of a gene at a locus |
| Genotype / phenotype | The alleles present / the observable trait they produce |
| Homozygous / heterozygous / hemizygous | Two identical alleles / two different / one copy only (X-linked genes in males) |
| Dominant / recessive | Phenotype shown by heterozygote / only by homozygote |
| Haploinsufficiency, dominant negative, gain of function | Three molecular reasons for dominance |
| Penetrance / expressivity | Proportion of carriers affected / degree of severity among those affected |
| Linkage / recombination fraction | Co-inheritance of nearby loci / probability a crossover separates them |
| Consanguinity | Mating between relatives; raises the chance both carry the same recessive allele |
| Germline mosaicism | A mutation in a fraction of a parent's gametes, allowing recurrence without the parent being affected |
| Anticipation | Earlier onset and greater severity in successive generations; repeat expansion |

## How it fits

- **Below:** the laws are [meiosis](../../03-cell-biology/02-the-cell-life-cycle/mitosis-meiosis-and-chromosome-segregation.md) described as arithmetic; the arithmetic is [probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md) and [Bayes](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md); dominance is explained by [protein](../../02-biochemistry-and-molecular-biology/01-macromolecules/proteins-structure-and-folding.md) and enzyme biochemistry.
- **Above:** [single-gene disorders](../../08-pathology/04-genetic-metabolic-and-environmental-disease/single-gene-and-chromosomal-disorders.md) and [inborn errors](../../08-pathology/04-genetic-metabolic-and-environmental-disease/inborn-errors-of-metabolism.md) are its catalogue; [paediatrics](../../14-life-course-mind-and-integrative-care/01-paediatrics/congenital-and-genetic-disease-in-childhood.md) and [obstetrics](../../14-life-course-mind-and-integrative-care/02-obstetrics-and-gynaecology/pregnancy-and-its-complications.md) apply it in counselling and prenatal diagnosis; allele frequencies feed [population genetics](../02-evolution/natural-selection-and-population-genetics.md).
- **Siblings:** [chromosomes](chromosomes-and-cytogenetics.md) are where the alleles sit and what happens when whole segments are lost; [genomic variation](genomic-variation-and-mutation.md) describes the alleles themselves; [complex traits](complex-traits-and-heritability.md) is what happens when hundreds of loci each contribute a little; [imprinting](epigenetic-inheritance-and-imprinting.md) is the exception in which the parent of origin matters.

## Common misconceptions

- **"Dominant means common or strong."** It means the heterozygote is affected; many dominant alleles are rare and mild, and the commonest alleles are often recessive.
- **"A recessive disease needs an affected relative."** Carriers are healthy and usually unaware; most children with a recessive disorder have no family history, which is why population carrier screening exists.
- **"If a parent is affected, the risk to each child depends on how many are already affected."** Each conception is an independent trial; three affected children do not make the fourth less likely.

## Go deeper

- Robert L. Nussbaum, Roderick R. McInnes and Huntington F. Willard, *Thompson & Thompson Genetics in Medicine* (8th ed., 2016): the standard medical genetics text, with worked risk calculations.
- Gregor Mendel, "Versuche über Pflanzen-Hybriden" (1866): short, quantitative and still readable in translation.
- Peter S. Harper, *Practical Genetic Counselling* (8th ed., 2010): how the arithmetic becomes a conversation with a family.
