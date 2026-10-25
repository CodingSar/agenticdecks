# DNA replication and repair

> **Layer:** [02 Biochemistry and Molecular Biology](../README.md) › [Genetic information flow](README.md)
> **Builds on:** [Nucleic acids](../01-macromolecules/nucleic-acids.md), [Enzymes and catalysis](../01-macromolecules/enzymes-and-catalysis.md), [Probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md), [Redox and electron transfer](../../00-physical-and-chemical-foundations/02-chemistry-of-life/redox-and-electron-transfer.md)
> **Enables:** [The cell cycle and its checkpoints](../../03-cell-biology/02-the-cell-life-cycle/the-cell-cycle-and-its-checkpoints.md), [Senescence and telomeres](../../03-cell-biology/02-the-cell-life-cycle/senescence-and-telomeres.md), [Genomic variation and mutation](../../04-genetics-evolution-and-development/01-inheritance/genomic-variation-and-mutation.md), [Oncogenes, tumour suppressors and genomic instability](../../08-pathology/03-neoplasia/oncogenes-tumour-suppressors-and-genomic-instability.md), [Anticancer drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md)

## Essence

Before a cell divides it must copy about 3 billion base pairs, and between divisions it must undo the tens of thousands of chemical lesions its Deoxyribonucleic Acid (DNA) suffers every day. Replication uses each strand as a template; fidelity comes not from one perfect enzyme but from three layers of checking, each removing about 99% of the errors the one before let through. Repair is a set of pathways each matched to a class of damage. When either system fails, mutations accumulate and the result is cancer, and because tumours depend on repair to survive the damage that chemotherapy and radiotherapy inflict, the same enzymes are among medicine's most important drug targets.

## Core tenets

1. **Replication is semiconservative, templated, and runs in one direction.** Meselson and Stahl (1958) showed that each daughter helix keeps one old strand. Polymerases add nucleotides only to a free 3'-hydroxyl and only in the 5'→3' direction, so one strand (leading) is copied continuously and the other (lagging) in short Okazaki fragments primed by RNA, later joined by ligase. A helicase opens the fork and a sliding clamp keeps the polymerase on; human cells copy about 50 bases a second per fork from tens of thousands of origins in parallel.

2. **Fidelity is layered, and the layers multiply.** Base pairing alone would give about one error in 10^4–10^5. The polymerase's own 3'→5' exonuclease removes a mispaired base before continuing (proofreading), improving fidelity about a hundredfold. Mismatch repair then scans the new strand for distortions and excises them, another hundredfold. The product is about one error in 10^9–10^10 bases, a handful per division; each of us carries roughly 60–70 new mutations absent from both parents, most from the father's germline and rising with his age. The rate is tuned, not minimised: evolution needs variation.

3. **Linear chromosomes cannot be copied to the end, so they shorten.** The lagging strand's last primer leaves a gap, so each division loses 50–100 base pairs from the chromosome end. Telomeres, repetitive capped sequences, absorb the loss; telomerase, a reverse transcriptase carrying its own RNA template, rebuilds them in germ cells, stem cells and most cancers. Somatic cells without telomerase count their divisions and stop, which is a brake on tumours and a contributor to ageing ([senescence](../../03-cell-biology/02-the-cell-life-cycle/senescence-and-telomeres.md)).

4. **Damage is continuous and chemically diverse, so repair is specialised.** Base excision repair removes small chemical changes (deaminated or oxidised bases, uracil) by glycosylases. Nucleotide excision repair cuts out bulky, helix-distorting lesions such as ultraviolet pyrimidine dimers; its absence (xeroderma pigmentosum) raises skin cancer risk about a thousandfold. Mismatch repair fixes replication errors; inherited loss (Lynch syndrome) causes colorectal and endometrial cancer and leaves a signature, microsatellite instability. Double-strand breaks, the most dangerous lesion, are repaired accurately by homologous recombination when a sister chromatid is available (needing BRCA1 and BRCA2) or quickly and inaccurately by non-homologous end joining.

5. **Damage is sensed before it is copied.** Kinases (ATM for double-strand breaks, ATR for stalled forks) phosphorylate hundreds of targets, halting the [cell cycle](../../03-cell-biology/02-the-cell-life-cycle/the-cell-cycle-and-its-checkpoints.md) and stabilising p53, which drives repair, arrest or apoptosis. p53 is mutated in about half of all cancers because losing it lets damaged cells keep dividing.

6. **Repair defects cause cancer, and cancer's reliance on repair is its weakness.** A cell with a broken repair pathway accumulates mutations faster (a mutator phenotype), which is how inherited repair defects produce cancer syndromes. But a tumour that has lost one pathway depends on the others: BRCA-deficient cells die when PARP, an enzyme of single-strand break repair, is inhibited, because the breaks become unrepairable double-strand breaks. This synthetic lethality (olaparib and related drugs) is the model for targeting repair. Chemotherapy and radiotherapy work by inflicting damage faster than the tumour can mend it, and methylation of the repair gene MGMT predicts a glioma's response to temozolomide.

7. **The copying machinery is a drug target, and differences between organisms make it selective.** Bacterial gyrase and topoisomerase IV are hit by fluoroquinolones; viral polymerases accept chain-terminating nucleosides that human polymerases largely reject (aciclovir, activated only by the viral thymidine kinase; reverse transcriptase inhibitors for HIV); human topoisomerases are trapped by etoposide and irinotecan; nucleoside analogues such as cytarabine and gemcitabine poison replicating tumour cells.

8. **Mutations record their causes.** Each damaging process leaves a characteristic pattern: ultraviolet light gives C→T changes at adjacent pyrimidines, tobacco smoke gives G→T, defective mismatch repair gives indels at repeats, and a clock-like signature accumulates with age. Reading these mutational signatures from a tumour genome (Alexandrov et al., 2013) infers aetiology from sequence, and sequencing normal tissues shows that clones carrying driver mutations expand in healthy ageing skin, oesophagus and blood.

## Key concepts

| Term | Meaning |
|---|---|
| Semiconservative | Each daughter duplex has one parental and one new strand |
| Proofreading | Polymerase 3'→5' exonuclease that removes a just-inserted mispair |
| Mismatch repair | Post-replication correction of mispaired bases on the new strand |
| Telomere, telomerase | Protective chromosome end; the enzyme that extends it |
| Excision repair | Base excision (small lesions) and nucleotide excision (bulky lesions) |
| Homologous recombination | Accurate double-strand break repair using a sister template; needs BRCA1/2 |
| Non-homologous end joining | Fast, error-prone ligation of broken ends |
| Synthetic lethality | Death from losing two genes that are individually dispensable |
| Mutational signature | Sequence pattern of mutations characteristic of a cause |

## How it fits

- **Below:** the template rule and the chemistry of lesions are in [nucleic acids](../01-macromolecules/nucleic-acids.md); polymerase fidelity is [enzyme](../01-macromolecules/enzymes-and-catalysis.md) kinetics; error rates compound as [probabilities](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md); oxidative lesions are [redox](../../00-physical-and-chemical-foundations/02-chemistry-of-life/redox-and-electron-transfer.md) damage.
- **Above:** replication is one phase of the [cell cycle](../../03-cell-biology/02-the-cell-life-cycle/the-cell-cycle-and-its-checkpoints.md); surviving errors become [heritable variation](../../04-genetics-evolution-and-development/01-inheritance/genomic-variation-and-mutation.md); failed repair is [genomic instability](../../08-pathology/03-neoplasia/oncogenes-tumour-suppressors-and-genomic-instability.md); the machinery is the target of [anticancer drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md) and antimicrobials.
- **Siblings:** [transcription](transcription-and-rna-processing.md) reads what replication copies; [gene regulation](gene-regulation-and-epigenetic-mechanisms.md) explains how methylation is copied with the DNA; [molecular techniques](molecular-techniques.md) borrow polymerases to amplify and sequence.

## Common misconceptions

- **"Mutations are rare accidents of copying."** Most lesions are chemical damage between divisions; genomes persist because repair is continuous, not because DNA is inert.
- **"Cancer mutations are mostly inherited."** Fewer than one in ten cancers involves a strongly predisposing inherited variant; most driver mutations are somatic.
- **"Repair is always protective."** End joining of the wrong ends creates the translocations of leukaemias and lymphomas; repair pathways also rescue tumour cells from treatment.

## Go deeper

- Alberts et al., *Molecular Biology of the Cell* (7th ed., 2022), chapter 5: replication, repair and recombination.
- Tomas Lindahl, "Instability and decay of the primary structure of DNA" (*Nature*, 1993): the daily lesion load.
- Ludmil B. Alexandrov et al., "Signatures of mutational processes in human cancer" (*Nature*, 2013): reading causes from sequence.
