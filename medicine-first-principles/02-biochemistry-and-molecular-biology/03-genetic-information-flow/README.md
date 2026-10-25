# Genetic information flow

> **Layer:** [02 Biochemistry and Molecular Biology](../README.md) › Genetic information flow
> **Children:** [DNA replication and repair](dna-replication-and-repair.md) · [Transcription and RNA processing](transcription-and-rna-processing.md) · [Translation and protein targeting](translation-and-protein-targeting.md) · [Gene regulation and epigenetic mechanisms](gene-regulation-and-epigenetic-mechanisms.md) · [Molecular techniques](molecular-techniques.md)

## What this area is about

This area follows information from a sequence of Deoxyribonucleic Acid (DNA) to a working protein in its right place, and back to the copy that is passed to the next cell. Crick's central dogma is the spine: DNA is replicated, transcribed into Ribonucleic Acid (RNA), and translated into protein, and information does not flow back from protein to sequence. Around that spine sit the processes that make it reliable (proofreading, mismatch repair, nonsense-mediated decay, folding checks), the processes that make it selective (promoters, enhancers, chromatin, methylation, microRNAs) and the processes that address the product (signal peptides, the endoplasmic reticulum).

The unifying idea is that one molecule's sequence specifies another's by complementary pairing, and that every pairing step is checked. Base pairing lets DNA template DNA and RNA, lets tRNA anticodons read codons, lets microRNAs find targets, and lets a laboratory probe find a gene. The checks are what make a genome stable across a lifetime, and the failures of the checks, or their deliberate overload by drugs, are where cancer, inherited disease and antimicrobial therapy enter.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [DNA replication and repair](dna-replication-and-repair.md) | Copying the archive and keeping it intact; mutation and its signatures | Nucleic acids, enzymes |
| [Transcription and RNA processing](transcription-and-rna-processing.md) | Making the working copy; capping, splicing, decay | Nucleic acids |
| [Translation and protein targeting](translation-and-protein-targeting.md) | Reading the copy into protein and sending it to its address | Transcription, proteins |
| [Gene regulation and epigenetic mechanisms](gene-regulation-and-epigenetic-mechanisms.md) | Deciding which genes are read, and remembering the decision | Transcription, 01 feedback |
| [Molecular techniques](molecular-techniques.md) | The same enzymes and pairing rules used as laboratory instruments | All of the above |

```
      replication (copy, proofread, repair)
           |
   DNA ----+----> transcription ----> pre-mRNA --splice, cap, tail--> mRNA
    ^                 ^                                                  |
    |      regulation: factors, enhancers, chromatin, methylation        |
    |      (which genes, how much, remembered through division)          v
    |                                                   translation on the ribosome
  mutation                                                               |
  (what repair missed)                                   targeting: cytosol, nucleus,
                                                         mitochondrion, ER -> secretion
  techniques: PCR, sequencing, antibodies, cloning, editing read and rewrite each step
```

Read replication, transcription and translation in that order; it is the order of the dogma and each assumes the one before. Gene regulation then explains why only a fraction of the genome is transcribed in any cell, and how that fraction is remembered. Molecular techniques comes last because it uses all four as tools, and because it is the bridge to the diagnostic layers.

## Connections to sibling areas

- **[Macromolecules](../01-macromolecules/README.md):** nucleic acids and proteins are the substrates and products; the ribosome and spliceosome are RNA enzymes; protein folding is the last step of translation and the first subject of quality control.
- **[Metabolism](../02-metabolism/README.md):** replication, transcription and translation consume nucleotides, amino acids and a large share of the cell's ATP; nutrient state feeds back on expression through transcription factors and on translation through mTOR, and antimetabolite drugs starve nucleotide synthesis.
- **[Cell signalling](../04-cell-signalling/README.md):** almost every signalling cascade ends at a transcription factor; nuclear receptors are both receptors and transcription factors; the time course of a hormone's effect is the time course of transcription and protein turnover.

## Connections across layers

From below, this area takes [base pairing and recognition](../../00-physical-and-chemical-foundations/02-chemistry-of-life/carbon-chemistry-and-molecular-recognition.md), the [probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md) of error and the [feedback](../../01-quantitative-and-scientific-foundations/03-systems-and-models/feedback-and-control.md) that gives a network memory. To the layers above it gives the [cell cycle](../../03-cell-biology/02-the-cell-life-cycle/the-cell-cycle-and-its-checkpoints.md) its S phase and checkpoints, [inheritance](../../04-genetics-evolution-and-development/01-inheritance/README.md) its mutations and epigenetic marks, [development](../../04-genetics-evolution-and-development/03-development/README.md) its patterning genes, [virology](../../07-microbiology-and-immunology/01-microbes-and-infection/viruses.md) its parasites of the machinery, [neoplasia](../../08-pathology/03-neoplasia/README.md) its genomic instability and oncogenes, [antimicrobials](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/antimicrobials.md) and [anticancer drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md) their targets, [advanced therapies](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/biologics-and-advanced-therapies.md) their products, and [molecular diagnostics](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/histopathology-cytology-and-molecular-diagnostics.md) its methods.

## Cross-cutting threads

- [Signalling and information](../../CROSS-CUTTING.md#signalling-and-information): a genome is a message with redundancy (the degenerate code) and error correction (proofreading and repair).
- [Specificity and recognition](../../CROSS-CUTTING.md#specificity-and-recognition): base pairing, codon reading and factor binding are all recognition with a tolerated error rate.
- [Injury and repair](../../CROSS-CUTTING.md#injury-and-repair): DNA is damaged continuously and repaired continuously; cancer is the ledger falling behind.
- [Feedback and homeostasis](../../CROSS-CUTTING.md#feedback-and-homeostasis): autoregulatory transcription factors give cells a stable identity.
- [Time courses](../../CROSS-CUTTING.md#time-courses): mRNA half-lives of minutes to a day and protein turnover set how fast a cell can change its mind.
- [Trade-offs and evolutionary legacy](../../CROSS-CUTTING.md#trade-offs-and-evolutionary-legacy): a mutation rate low enough for stability, high enough for evolution; mitochondrial ribosomes as the price of a bacterial ancestor.
