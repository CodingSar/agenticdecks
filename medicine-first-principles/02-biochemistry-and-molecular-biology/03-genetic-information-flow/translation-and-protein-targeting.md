# Translation and protein targeting

> **Layer:** [02 Biochemistry and Molecular Biology](../README.md) › [Genetic information flow](README.md)
> **Builds on:** [Transcription and RNA processing](transcription-and-rna-processing.md), [Nucleic acids](../01-macromolecules/nucleic-acids.md), [Proteins: structure and folding](../01-macromolecules/proteins-structure-and-folding.md), [Bioenergetics: ATP and redox carriers](../02-metabolism/bioenergetics-atp-and-redox-carriers.md)
> **Enables:** [Antimicrobials](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/antimicrobials.md), [Membrane trafficking and secretion](../../03-cell-biology/01-cell-structure/membrane-trafficking-and-secretion.md), [Protein quality control and degradation](../../03-cell-biology/01-cell-structure/protein-quality-control-and-degradation.md), [Organelles and compartmentalization](../../03-cell-biology/01-cell-structure/organelles-and-compartmentalization.md), [Bacteria](../../07-microbiology-and-immunology/01-microbes-and-infection/bacteria.md)

## Essence

Translation converts a sequence of nucleotides into a sequence of amino acids using a code of three-letter words, read by transfer RNAs (tRNAs) that are charged by enzymes which are the true decoders, on a ribosome whose catalytic heart is RNA. The product is then delivered: a signal built into the protein's own sequence sends it to the cytosol, the nucleus, the mitochondrion, or into the endoplasmic reticulum for secretion or the membrane. Two facts carry most of the medicine. Bacterial and human ribosomes differ enough that half of all antibiotic classes work by jamming the bacterial one, and the mitochondrion's bacterial ancestry explains those antibiotics' side effects. And the reading frame, the targeting signal and the folding checkpoints are each a place where a mutation turns a correct sequence into no protein, a misplaced protein, or a protein the cell destroys.

## Core tenets

1. **The code is triplet, degenerate, nearly universal, and built to fail gently.** Sixty-one codons specify twenty amino acids and three say stop; most amino acids have several codons differing in the third position, and tRNAs read that position loosely (wobble). Similar codons encode chemically similar amino acids, so many point mutations are harmless or mild. Insertions or deletions not a multiple of three shift the frame and garble everything downstream: in Duchenne muscular dystrophy an out-of-frame deletion leaves no dystrophin, while an in-frame deletion of the same region gives the milder Becker form.

2. **Aminoacyl-tRNA synthetases are the decoders, and translation is the cell's biggest energy bill.** Each of the twenty synthetases recognises its amino acid and its tRNAs and joins them, with an editing site that hydrolyses wrong pairings (error about 1 in 10^4). Charging costs two phosphoanhydride bonds and each elongation step two more, so a protein costs at least four ATP equivalents per residue and protein synthesis consumes around a third of a growing cell's energy. Starved or stressed cells therefore shut translation down first, by phosphorylating the initiation factor eIF2 and inhibiting the nutrient-sensing kinase mTOR.

3. **The ribosome is a ribozyme with three sites.** Two subunits assemble on the mRNA; the small subunit checks codon–anticodon pairing, the large one forms the peptide bond using its ribosomal RNA, not a protein, as catalyst. tRNAs pass through the A (aminoacyl), P (peptidyl) and E (exit) sites, driven by GTP-hydrolysing elongation factors that also provide a kinetic check on the pairing. Bacteria start at a Shine–Dalgarno sequence with formyl-methionine; eukaryotes scan from the 5' cap to the first AUG. The human ribosome adds five or six residues a second; a bacterial one three times as many.

4. **Differences between ribosomes are the basis of half of antibiotic therapy.** Aminoglycosides bind the bacterial small subunit and cause misreading; tetracyclines block its A site; macrolides plug the exit tunnel of the large subunit; chloramphenicol, clindamycin and linezolid block peptide-bond formation or assembly. Human cytosolic ribosomes are spared, but mitochondrial ribosomes are bacterial in origin, which is why aminoglycosides damage the inner ear and kidney, chloramphenicol suppresses marrow, and a mitochondrial ribosomal RNA variant (m.1555A>G) makes carriers deaf after a single aminoglycoside dose. Diphtheria toxin and ricin kill by inactivating the human elongation factor and ribosomal RNA respectively.

5. **Termination has its own quality control.** Release factors read the stop codon and hydrolyse the finished chain off. A premature stop triggers nonsense-mediated decay of the mRNA; a stalled ribosome triggers degradation of both the mRNA and the partial chain. Roughly a fifth of new polypeptides misfold despite chaperones waiting at the ribosome exit, and the cell's [degradation machinery](../../03-cell-biology/01-cell-structure/protein-quality-control-and-degradation.md) disposes of them, so protein synthesis is a leaky process constantly cleaned up.

6. **A protein's address is written in its sequence.** Blobel's signal hypothesis (1975): an N-terminal stretch of hydrophobic residues is recognised while the chain is still emerging, the ribosome is docked on the endoplasmic reticulum and the chain threads through a channel into the lumen. No signal means the protein stays in the cytosol; other internal sequences send proteins to the nucleus, into mitochondria or peroxisomes, and hydrophobic stop-transfer segments anchor them in membranes. Diseases follow from wrong addresses: peroxisomal import failure (Zellweger syndrome), a missing lysosomal tag so that enzymes are secreted instead (I-cell disease), signal-peptide mutations in preproinsulin causing neonatal diabetes.

7. **The endoplasmic reticulum folds, modifies and inspects secretory proteins.** Inside it the signal peptide is cut off, sugars are attached to asparagines, disulfides form in the oxidising lumen, and chaperones check the fold; only correctly folded proteins move on to the Golgi, and failures are sent back to the cytosol for destruction (the fate of most mutant CFTR in cystic fibrosis). When misfolded proteins exceed capacity, the unfolded protein response slows translation and expands the reticulum, and if that fails it triggers apoptosis, a mechanism in beta-cell loss in diabetes and in neurodegeneration.

8. **Modification after translation multiplies the proteome.** Proteolytic cleavage activates zymogens (trypsin, clotting factors) and hormones (insulin is cut from proinsulin, releasing C-peptide, which is why C-peptide measures a patient's own insulin). Phosphorylation, acetylation, ubiquitination, lipid anchors (farnesylation of Ras), glycosylation and vitamin K-dependent carboxylation each change where a protein is, whom it binds and how long it lasts. The ~20,000 genes give rise to many hundreds of thousands of distinct protein forms, and the amount of a protein correlates only loosely with the amount of its mRNA.

## Key concepts

| Term | Meaning |
|---|---|
| Codon, anticodon | Three-nucleotide word on mRNA; its complement on tRNA |
| Reading frame | The grouping of nucleotides into triplets, set by the start codon |
| Wobble | Loose pairing at the third codon position; one tRNA reads several codons |
| Aminoacyl-tRNA synthetase | Enzyme that attaches the right amino acid to its tRNA; the real decoder |
| Peptidyl transferase | The ribosomal RNA site that forms the peptide bond |
| Signal peptide | N-terminal hydrophobic sequence directing a chain into the endoplasmic reticulum |
| Translocon | The channel through which a nascent chain crosses the reticulum membrane |
| Unfolded protein response | Stress programme triggered by excess misfolded protein in the reticulum |
| Zymogen | Inactive precursor activated by cleavage |

## How it fits

- **Below:** the mRNA, tRNA and ribosomal RNA are [nucleic acids](../01-macromolecules/nucleic-acids.md) reading each other by base pairing; the product's fate is governed by [folding](../01-macromolecules/proteins-structure-and-folding.md); the cost is paid in the [ATP and GTP](../02-metabolism/bioenergetics-atp-and-redox-carriers.md) of bioenergetics.
- **Above:** ribosome selectivity organises the [antimicrobials](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/antimicrobials.md); targeting feeds [trafficking and secretion](../../03-cell-biology/01-cell-structure/membrane-trafficking-and-secretion.md) and populates the [organelles](../../03-cell-biology/01-cell-structure/organelles-and-compartmentalization.md); misfolded products go to [quality control](../../03-cell-biology/01-cell-structure/protein-quality-control-and-degradation.md); the bacterial ribosome and its resistance mutations belong to [bacteria](../../07-microbiology-and-immunology/01-microbes-and-infection/bacteria.md).
- **Siblings:** [transcription](transcription-and-rna-processing.md) supplies the message; [gene regulation](gene-regulation-and-epigenetic-mechanisms.md) also acts at translation through microRNAs and initiation factors; [molecular techniques](molecular-techniques.md) express recombinant proteins by borrowing this machinery.

## Common misconceptions

- **"The ribosome is a protein machine."** Its catalytic core is RNA; the proteins are scaffolding, which is why the ribosome is evidence for an RNA-first origin of life.
- **"Protein levels follow mRNA levels."** Translation rates and protein half-lives vary over orders of magnitude; the correlation across genes is modest.
- **"Synonymous mutations are silent."** They can create or destroy splice sites, alter mRNA structure or stability, or slow translation through rare codons.

## Go deeper

- Alberts et al., *Molecular Biology of the Cell* (7th ed., 2022), chapters 6 and 12: translation, and intracellular compartments and protein sorting.
- Günter Blobel, "Protein Targeting" (Nobel lecture, 1999): the signal hypothesis and its proof.
- Venki Ramakrishnan, *Gene Machine: The Race to Decipher the Secrets of the Ribosome* (2018): how the structure was solved and what it showed about antibiotics.
