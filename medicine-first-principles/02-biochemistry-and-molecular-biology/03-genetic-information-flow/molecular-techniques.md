# Molecular techniques

> **Layer:** [02 Biochemistry and Molecular Biology](../README.md) › [Genetic information flow](README.md)
> **Builds on:** [Nucleic acids](../01-macromolecules/nucleic-acids.md), [DNA replication and repair](dna-replication-and-repair.md), [Proteins: structure and folding](../01-macromolecules/proteins-structure-and-folding.md), [Measurement error and biological variation](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/measurement-error-and-biological-variation.md)
> **Enables:** [Histopathology, cytology and molecular diagnostics](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/histopathology-cytology-and-molecular-diagnostics.md), [Microbiological and serological diagnosis](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/microbiological-and-serological-diagnosis.md), [Genomic variation and mutation](../../04-genetics-evolution-and-development/01-inheritance/genomic-variation-and-mutation.md), [Pharmacogenomics and individual variation](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/pharmacogenomics-and-individual-variation.md), [Biologics and advanced therapies](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/biologics-and-advanced-therapies.md)

## Essence

The techniques of molecular biology are the cell's own enzymes and recognition rules taken out of the cell and used as tools. Base pairing finds a sequence; a polymerase copies it a billionfold; a sequencer reads it; an antibody picks one protein out of thousands; a bacterium is made to manufacture human insulin; a bacterial defence system cuts a chosen site in a human chromosome. Medicine can therefore read a patient's genome, count the viral copies in their blood, type a tumour by its mutations and, in a few diseases, rewrite the defect. Each technique has a sensitivity, a specificity and a failure mode, so every result is a measurement to be interpreted.

## Core tenets

1. **Hybridisation is the master principle: a probe finds its complement.** Under the right stringency a labelled oligonucleotide binds only its exact partner, so one can detect a gene on a chromosome spread (fluorescence in situ hybridisation shows HER2 amplification or the BCR-ABL fusion), measure thousands of transcripts on a microarray, or prime a polymerase at one site. Stringency trades missed targets against false binding: the sensitivity–specificity trade-off of every diagnostic test.

2. **The polymerase chain reaction amplifies a chosen sequence exponentially.** Mullis (1983–85) saw that cycling temperature with two primers and a heat-stable polymerase doubles the target each cycle; thirty cycles yield about a billion copies. Quantitative PCR counts the cycles needed to cross a threshold, which is inversely proportional to the logarithm of the starting number, giving viral loads for HIV, hepatitis B and C and SARS-CoV-2. Because contamination is amplified as faithfully as the sample, and the method detects nucleic acid rather than live organisms, a positive result means the sequence was present, not that the patient is infectious.

3. **Sequencing has fallen a million-fold in cost and moved from gene to genome.** Sanger's chain-termination method (1977) reads ~800 bases and remains the reference for confirming a variant. Massively parallel sequencing reads hundreds of millions of short fragments at once, so a genome costs a few hundred dollars (2020s) against about three billion for the first (2003); long-read platforms resolve repeats and structural variants, and portable sequencers type outbreak strains in hours. The bottleneck is no longer reading but interpretation: a genome holds millions of variants, most harmless, and classifying a variant as pathogenic depends on population databases that are still skewed towards people of European ancestry.

4. **Antibodies are the equivalent tool for proteins.** Monoclonal antibodies (Köhler and Milstein, 1975) give an unlimited supply of one specificity. Immunoassays quantify hormones, troponin and drugs; immunohistochemistry stains a tumour for the receptors that decide treatment (oestrogen receptor, HER2, PD-L1); flow cytometry types leukaemias and counts CD4 cells; lateral-flow strips detect pregnancy or viral antigen. An antibody test detects the host's response, which lags infection by days and persists for years, so it reports exposure, not current infection.

5. **Mass spectrometry weighs molecules and has replaced many assays.** Tandem mass spectrometry on a newborn's dried blood spot screens for dozens of [inborn errors](../../08-pathology/04-genetic-metabolic-and-environmental-disease/inborn-errors-of-metabolism.md) at once by their accumulated metabolites; matrix-assisted laser desorption identifies a bacterial colony from its protein fingerprint in minutes; and it measures drugs, steroids and vitamin D more specifically than immunoassays.

6. **Recombinant DNA turned cells into factories and ended a class of transfusion-borne disease.** Restriction enzymes and ligase (1970s) let a human gene be inserted into a plasmid and expressed in bacteria, yeast or mammalian cells. Human insulin (1982) was the first product; growth hormone, erythropoietin, clotting factors (ending the HIV and hepatitis C transmission that plasma-derived factor had caused in haemophilia), hepatitis B and papillomavirus vaccines and every therapeutic antibody followed.

7. **Genome editing makes the repair machinery do the work.** CRISPR–Cas9 (Doudna and Charpentier, 2012) uses a guide RNA to direct a nuclease to one site; the cell's own end-joining then disrupts the gene, or a supplied template is copied in by homologous recombination. The first approved therapy (exagamglogene autotemcel, 2023, UK and US) edits a patient's own stem cells to disable the BCL11A enhancer, reactivating fetal haemoglobin to treat sickle cell disease and beta-thalassaemia. Viral vectors deliver genes without editing (onasemnogene for spinal muscular atrophy, 2019). Off-target cuts, immune responses and the ethics of germline editing are the open problems.

8. **Every technique has pre-analytical, analytical and interpretive limits.** Formalin fragments DNA; low tumour fraction hides a mutation; repeats and pseudogenes defeat short reads; mosaicism means blood may not represent the brain. A variant of uncertain significance is not a diagnosis, and a test's positive predictive value depends on who is tested. The [laboratory](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/histopathology-cytology-and-molecular-diagnostics.md) reports a measurement; the clinician supplies the prior.

## Key concepts

| Term | Meaning |
|---|---|
| Probe, primer | Short nucleic acid that binds its complement; to detect, or to start a polymerase |
| Stringency | Temperature and salt conditions that set how exact a match must be |
| Polymerase chain reaction | Exponential amplification of a sequence between two primers |
| Next-generation sequencing | Massively parallel reading of short fragments, assembled against a reference |
| Variant of uncertain significance | A sequence change that cannot yet be called benign or pathogenic |
| Monoclonal antibody | Identical antibodies of one specificity from a single B-cell clone |
| Recombinant protein | Protein made by expressing a cloned gene in a host cell |
| CRISPR–Cas9 | Programmable nuclease guided to a sequence by an RNA |

## How it fits

- **Below:** every nucleic-acid method is [base pairing](../01-macromolecules/nucleic-acids.md) under controlled stringency; PCR and sequencing borrow the [polymerases](dna-replication-and-repair.md); antibodies are [proteins](../01-macromolecules/proteins-structure-and-folding.md) with a binding site; every result carries [measurement error](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/measurement-error-and-biological-variation.md).
- **Above:** these are the methods of [molecular diagnostics](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/histopathology-cytology-and-molecular-diagnostics.md) and [microbiological diagnosis](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/microbiological-and-serological-diagnosis.md); they discovered the [variation](../../04-genetics-evolution-and-development/01-inheritance/genomic-variation-and-mutation.md) that [pharmacogenomics](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/pharmacogenomics-and-individual-variation.md) uses; recombinant proteins, antibodies and edited cells are the [biologics and advanced therapies](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/biologics-and-advanced-therapies.md).
- **Siblings:** this leaf is the other four made into instruments: [replication](dna-replication-and-repair.md) becomes PCR, [transcription](transcription-and-rna-processing.md) becomes RNA sequencing, [translation](translation-and-protein-targeting.md) becomes recombinant expression, and [regulation](gene-regulation-and-epigenetic-mechanisms.md) is read by methylation and chromatin assays.

## Common misconceptions

- **"A positive PCR means the patient is infectious."** It means target sequence was present; fragments persist after live virus is gone.
- **"Sequencing the genome gives the diagnosis."** It gives millions of variants; the diagnosis depends on interpreting them against phenotype and population data, and the yield in suspected rare disease is roughly a quarter to a half.
- **"CRISPR edits DNA precisely."** It cuts precisely; the repair is done by the cell and is heterogeneous unless a template or a base editor is used.

## Go deeper

- Kary B. Mullis, "The Unusual Origin of the Polymerase Chain Reaction" (*Scientific American*, 1990): the idea and the night drive.
- Tom Strachan and Andrew Read, *Human Molecular Genetics* (5th ed., 2018): techniques and their interpretation in human genetics.
- Jennifer A. Doudna and Emmanuelle Charpentier, "The new frontier of genome engineering with CRISPR-Cas9" (*Science*, 2014): the mechanism and its reach.
