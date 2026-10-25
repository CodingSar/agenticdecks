# Complex traits and heritability

> **Layer:** [04 Genetics, Evolution and Development](../README.md) › [Inheritance](README.md)
> **Builds on:** [Distributions and descriptive statistics](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/distributions-and-descriptive-statistics.md), [Regression, adjustment and survival analysis](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md), [Mendelian inheritance and pedigrees](mendelian-inheritance-and-pedigrees.md), [Genomic variation and mutation](genomic-variation-and-mutation.md)
> **Enables:** [Multifactorial disease and risk](../../08-pathology/05-disease-as-process/multifactorial-disease-and-risk.md), [Risk prediction and stratification](../../10-epidemiology-and-evidence/03-screening-and-prevention/risk-prediction-and-stratification.md), [Obesity, lipids and metabolic syndrome](../../12-organ-system-specialties/05-endocrinology/obesity-lipids-and-metabolic-syndrome.md), [Mood and anxiety disorders](../../14-life-course-mind-and-integrative-care/03-psychiatry/mood-and-anxiety-disorders.md)

## Essence

Height, blood pressure, body mass and the risk of diabetes, coronary disease, schizophrenia and most cancers all run in families, yet none follows a Mendelian pattern. They are complex traits: shaped by hundreds to thousands of variants of small effect together with environment, and distributed continuously. Fisher showed in 1918 that many Mendelian factors acting additively produce exactly this pattern. Heritability is the fraction of a population's variation in a trait attributable to genetic differences, and the one idea that prevents misunderstanding is that **heritability describes variance in a population, not causation in an individual, and depends on the environment the population lives in**.

## Core tenets

1. **Many small additive effects give a normal distribution and a familial but non-Mendelian trait.** If a trait sums contributions from many loci, the central limit theorem gives a Gaussian ([distributions](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/distributions-and-descriptive-statistics.md)) and relatives correlate in proportion to shared alleles. Disease is modelled as a liability on this scale with a threshold. It explains why sibling recurrence risk is roughly the square root of population prevalence (a disease of 1% has sibling risk of ~10%) and falls off fast for distant relatives.

2. **Heritability is a ratio of variances and a population statistic.** Phenotypic variance V_P = V_G + V_E; narrow-sense heritability h² = V_A / V_P counts only additive genetic variance, which is what parents transmit. Height has h² ≈ 0.8 in well-nourished populations; most common diseases 0.3–0.7. A heritability of 0.8 does not mean 80% of a person's height is genetic; it means 80% of the differences between people, in that population and environment, go with genetic differences.

3. **Heritability is estimated from relatives and from genomes, and the two disagreed.** Twin studies compare monozygotic with dizygotic twins; adoption studies separate shared genes from shared homes. Genome-wide association studies then found that significant variants for height explained only a few percent of variance in early studies and ~40–50% with samples in the millions, leaving a gap called the missing heritability. It is largely accounted for by many variants too small to reach significance individually, by rare variants, and by some inflation of twin estimates.

4. **Association is found by comparing allele frequencies across the genome, with a severe multiple-testing correction.** A Genome-Wide Association Study (GWAS) tests about a million variants, so significance is set at p < 5 × 10^-8 ([hypothesis testing](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md)). A hit is a region, not a gene: the associated variant tags a causal one in linkage disequilibrium, usually regulatory. Ancestry differences between cases and controls produce spurious hits and must be adjusted for ([regression](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md)).

5. **Polygenic scores sum many small effects, and their value is stratification.** A polygenic risk score weights each allele by its effect size and sums. For coronary artery disease, the top few percent of the score have about three times average risk, comparable to a monogenic familial hypercholesterolaemia variant, and the score adds to conventional risk factors ([risk prediction](../../10-epidemiology-and-evidence/03-screening-and-prevention/risk-prediction-and-stratification.md)). Its limits are real: discrimination is modest, scores built on European-ancestry cohorts transfer poorly to others, and a score is a probability, not a diagnosis.

6. **Genetic variants are natural experiments for testing causality.** Alleles are assigned at conception, independently of later lifestyle and confounders, so a variant that raises LDL cholesterol lifelong can be used as an instrument: if carriers have more coronary disease in proportion to their LDL, LDL is causal. This is Mendelian randomisation ([causal inference](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md)). It confirmed LDL as a cause of coronary disease and showed that HDL cholesterol, though associated, is not, explaining the failure of drugs that raised HDL.

7. **Rare large-effect and common small-effect variants are ends of one spectrum, and both inform drug discovery.** GWAS loci name pathways: the lipid loci include every target of a current lipid-lowering drug, and loss-of-function variants in PCSK9 that lower LDL and protect against coronary disease led directly to PCSK9 inhibitors (approved 2015).

8. **Gene and environment interact and correlate, so the partition into V_G and V_E is a model.** Phenylketonuria is fully genetic and fully environmental: the gene destroys the enzyme, the diet decides the outcome. [Multifactorial disease](../../08-pathology/05-disease-as-process/multifactorial-disease-and-risk.md) is the rule, and the practical response to a high polygenic risk is usually environmental: in the top polygenic stratum for coronary disease, a favourable lifestyle roughly halves the risk.

## Key concepts

| Term | Meaning |
|---|---|
| Complex (multifactorial) trait | Trait shaped by many genes and environment, with continuous variation |
| Heritability (h²) | Fraction of phenotypic variance due to additive genetic variance in a population |
| Genome-wide association study (GWAS) | Hypothesis-free comparison of allele frequencies between cases and controls |
| Linkage disequilibrium | Correlation between nearby alleles; an associated variant tags a region |
| Polygenic risk score | Weighted sum of a person's risk alleles |
| Mendelian randomisation | Using genetic variants as instruments to test the causality of an exposure |
| Gene–environment interaction | The effect of a genotype depending on the environment |

## How it fits

- **Below:** the model is [distributions](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/distributions-and-descriptive-statistics.md) and variance decomposition; the methods are [regression](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md) and [causal inference](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md); the alleles are [common variants](genomic-variation-and-mutation.md); the single-gene limit is [Mendelian inheritance](mendelian-inheritance-and-pedigrees.md).
- **Above:** [multifactorial disease](../../08-pathology/05-disease-as-process/multifactorial-disease-and-risk.md) is the pathological framing; [risk prediction](../../10-epidemiology-and-evidence/03-screening-and-prevention/risk-prediction-and-stratification.md) uses polygenic scores; [metabolic](../../12-organ-system-specialties/05-endocrinology/obesity-lipids-and-metabolic-syndrome.md) and [psychiatric](../../14-life-course-mind-and-integrative-care/03-psychiatry/mood-and-anxiety-disorders.md) disorders are archetypal polygenic conditions; [population genetics](../02-evolution/natural-selection-and-population-genetics.md) explains the variants' frequencies.
- **Siblings:** this leaf is the many-locus limit of [Mendelian](mendelian-inheritance-and-pedigrees.md) genetics using the [variation](genomic-variation-and-mutation.md) catalogued earlier; [epigenetic inheritance](epigenetic-inheritance-and-imprinting.md) is one route by which environment leaves a heritable mark.

## Common misconceptions

- **"A heritability of 80% means the trait is 80% genetic in each person."** Heritability partitions differences between people in one population and environment, and changes when the environment changes.

## Go deeper

- Ronald A. Fisher, "The Correlation Between Relatives on the Supposition of Mendelian Inheritance", *Transactions of the Royal Society of Edinburgh* (1918): where quantitative genetics began.
- Peter M. Visscher and colleagues, "10 Years of GWAS Discovery: Biology, Function, and Translation", *American Journal of Human Genetics* (2017): what association studies found and what they are for.
- George Davey Smith and Shah Ebrahim, "'Mendelian Randomization': Can Genetic Epidemiology Contribute to Understanding Environmental Determinants of Disease?", *International Journal of Epidemiology* (2003).
