# Inheritance

> **Layer:** [04 Genetics, Evolution and Development](../README.md) › Inheritance
> **Children:** [Mendelian inheritance and pedigrees](mendelian-inheritance-and-pedigrees.md) · [Chromosomes and cytogenetics](chromosomes-and-cytogenetics.md) · [Genomic variation and mutation](genomic-variation-and-mutation.md) · [Complex traits and heritability](complex-traits-and-heritability.md) · [Epigenetic inheritance and imprinting](epigenetic-inheritance-and-imprinting.md)

## What this area is about

This area answers the question a patient asks when a relative falls ill: will it happen to me, and to my children? Inheritance is the transmission of information from parent to child and from cell to daughter cell, and medicine needs it at three scales: the single gene whose variant produces a disease with a predictable pattern in a family; the chromosome, whose dosage must be exact; and the whole genome, whose millions of small differences together shape risk for the common diseases. A fourth layer, epigenetic marks, sits on top of the sequence and decides what is read. The unifying idea is **particulate information copied with errors and shuffled by sex**: meiosis separates and recombines alleles, replication introduces new variants, and the arithmetic of segregation and the statistics of many small effects follow from those two facts. Genetic counselling, prenatal diagnosis, cancer genomics and pharmacogenomics all apply this area to one person.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Mendelian inheritance and pedigrees](mendelian-inheritance-and-pedigrees.md) | One gene, two alleles, random segregation: the patterns in families and the risk arithmetic | 03 meiosis; 01 probability and Bayes |
| [Chromosomes and cytogenetics](chromosomes-and-cytogenetics.md) | The packaging: dosage, aneuploidy, rearrangements, X inactivation, the tests that see them | 03 mitosis and meiosis; 02 chromatin; Mendelian |
| [Genomic variation and mutation](genomic-variation-and-mutation.md) | The alleles themselves: where variants come from, how they are classified and interpreted | 02 replication and repair; 02 sequencing |
| [Complex traits and heritability](complex-traits-and-heritability.md) | Many loci of small effect plus environment: heritability, GWAS, polygenic scores, Mendelian randomisation | Mendelian; variation; 01 distributions and regression |
| [Epigenetic inheritance and imprinting](epigenetic-inheritance-and-imprinting.md) | Marks on the sequence that are copied through mitosis, and the few that cross generations | 02 epigenetic mechanisms; 03 differentiation; cytogenetics |

```
   scale of the variant:   single base ------- gene ------- segment ------- chromosome
                            genomic variation   Mendelian    cytogenetics    cytogenetics
   number of loci:          one (Mendelian) ------------------------> thousands (complex traits)
   what is inherited:       sequence  +  marks on the sequence (epigenetic inheritance, imprinting)
```

Read Mendelian inheritance first; it supplies the vocabulary (allele, dominant, penetrance) and the arithmetic that everything else modifies. Chromosomes extends the unit of inheritance from the gene to the segment and the whole chromosome, and introduces dosage. Genomic variation goes the other way, down to the single base, and explains where alleles come from and how a laboratory decides whether one matters. Complex traits is the many-locus limit: when hundreds of variants each nudge a trait, Mendel's ratios disappear into a bell curve and the tools become statistical. Epigenetic inheritance is the exception clause for all four, and the bridge to development, where the same marks make a liver cell stay a liver cell.

## Connections to sibling areas

- **[Evolution](../02-evolution/README.md):** population genetics is inheritance iterated over generations; the allele frequencies that make a variant common or rare, and that let the laboratory call a variant benign, were set by mutation, drift and selection. Imprinting's parental conflict and the persistence of deleterious alleles are evolutionary questions.
- **[Development](../03-development/README.md):** the embryo is where the inherited genome is read. Epigenetic reprogramming after fertilisation is the first developmental event; chromosomal and single-gene disorders present as congenital malformations; imprinted genes control fetal growth.

## Connections across layers

From below: [meiosis](../../03-cell-biology/02-the-cell-life-cycle/mitosis-meiosis-and-chromosome-segregation.md) is the mechanism of Mendel's laws and of aneuploidy; [DNA replication and repair](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/dna-replication-and-repair.md) sets the mutation rate; [gene regulation](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/gene-regulation-and-epigenetic-mechanisms.md) supplies the marks; [molecular techniques](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/molecular-techniques.md) supply the tests; and [probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/README.md), [regression](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md) and [causal inference](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md) are the mathematics of pedigrees, heritability and Mendelian randomisation.

Upward: [08 pathology](../../08-pathology/04-genetic-metabolic-and-environmental-disease/README.md) catalogues the single-gene, chromosomal and multifactorial diseases and treats cancer as somatic mutation ([neoplasia](../../08-pathology/03-neoplasia/README.md)); [09 pharmacology](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/pharmacogenomics-and-individual-variation.md) uses common variation to predict drug response; [10 epidemiology](../../10-epidemiology-and-evidence/03-screening-and-prevention/risk-prediction-and-stratification.md) incorporates polygenic scores into risk prediction; [11 laboratory medicine](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/histopathology-cytology-and-molecular-diagnostics.md) delivers karyotypes and sequence interpretation; [12 haematology](../../12-organ-system-specialties/06-haematology/haematological-malignancies.md) classifies leukaemia by its chromosomes; [14 paediatrics](../../14-life-course-mind-and-integrative-care/01-paediatrics/congenital-and-genetic-disease-in-childhood.md) and [obstetrics](../../14-life-course-mind-and-integrative-care/02-obstetrics-and-gynaecology/pregnancy-and-its-complications.md) carry out genetic counselling and prenatal diagnosis.

## Cross-cutting threads

- [Probability and uncertainty](../../CROSS-CUTTING.md#probability-and-uncertainty): segregation is a coin toss, counselling is Bayes, a variant's classification is a weight of evidence, a polygenic score is a probability.
- [Signalling and information](../../CROSS-CUTTING.md#signalling-and-information): the genome as a message copied with errors; epigenetic marks as annotations on the message.
- [Dose–response](../../CROSS-CUTTING.md#dose-response): gene dosage explains aneuploidy, haploinsufficiency and imprinting disorders.
- [Cause and mechanism](../../CROSS-CUTTING.md#cause-and-mechanism): Mendelian disease as the cleanest cause–effect in medicine; Mendelian randomisation as the route from association to cause.
- [The host and its environment](../../CROSS-CUTTING.md#the-host-and-its-environment): heritability depends on environment; gene–environment interaction is the rule in complex disease.
- [Trade-offs and evolutionary legacy](../../CROSS-CUTTING.md#trade-offs-and-evolutionary-legacy): imprinting as parental conflict; common deleterious alleles persisting through balancing selection.
