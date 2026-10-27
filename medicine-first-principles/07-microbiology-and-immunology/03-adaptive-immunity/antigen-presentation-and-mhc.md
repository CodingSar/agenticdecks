# Antigen presentation and MHC

> **Layer:** [07 Microbiology and Immunology](../README.md) › [Adaptive immunity](README.md)
> **Builds on:** [Barriers and pattern recognition](../02-innate-immunity/barriers-and-pattern-recognition.md), [Protein quality control and degradation](../../03-cell-biology/01-cell-structure/protein-quality-control-and-degradation.md), [Membrane trafficking and secretion](../../03-cell-biology/01-cell-structure/membrane-trafficking-and-secretion.md), [Vascular and lymphatic architecture](../../05-tissues-and-anatomy/02-body-organization/vascular-and-lymphatic-architecture.md), [Natural selection and population genetics](../../04-genetics-evolution-and-development/02-evolution/natural-selection-and-population-genetics.md)
> **Enables:** [T cells](t-cells.md), [Tolerance and self-recognition](tolerance-and-self-recognition.md), [Transplant and tumour immunology](../04-immunity-in-disease/transplant-and-tumour-immunology.md), [Pharmacogenomics and individual variation](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/pharmacogenomics-and-individual-variation.md)

## Essence

T cells cannot see a microbe. They see short peptides held in the groove of a Major Histocompatibility Complex (MHC) molecule on the surface of another cell, and the MHC class tells them where the peptide came from: class I displays fragments of proteins made inside the cell, class II displays fragments of material the cell has eaten. Antigen presentation is a continuous surface report of what every cell contains. The genes encoding MHC are the most variable in the human genome, so each person presents a different slice of any pathogen; populations are hard to defeat, individuals differ in susceptibility and transplanted organs are rejected. And a T cell acts on a report only when a dendritic cell, licensed by innate recognition, carries it to a lymph node.

## Core tenets

1. **T cells recognise peptide plus MHC, not antigen alone.** Zinkernagel and Doherty (1974) showed that cytotoxic T cells kill virus-infected cells only when the target shares the T cell's own MHC: the receptor binds a composite of peptide and the MHC molecule holding it (MHC restriction). Each MHC variant binds a large but specific set of peptides by a few anchor residues. In humans the MHC is called the Human Leukocyte Antigen (HLA) system.

2. **Class I reports the cytosol; class II reports what was eaten.** Every nucleated cell continuously degrades a sample of its proteins in the proteasome, pumps the 8 to 10 residue fragments into the endoplasmic reticulum through the TAP transporter, loads them onto MHC class I (HLA-A, -B, -C) and displays them to CD8 T cells. A virus-infected or mutated cell thus betrays itself by its own peptides ([protein degradation](../../03-cell-biology/01-cell-structure/protein-quality-control-and-degradation.md)). Professional antigen-presenting cells (dendritic cells, macrophages, B cells) also load 13 to 25 residue peptides from endocytosed material onto MHC class II (HLA-DR, -DQ, -DP) in endosomes and display them to CD4 T cells. Dendritic cells can also cross-present eaten material on class I, priming CD8 responses against viruses that do not infect them.

3. **Dendritic cells decide whether a report leads to immunity.** An immature dendritic cell samples tissue continuously but presents poorly. When its pattern recognition receptors fire it matures: it raises MHC and the co-stimulatory molecules CD80 and CD86, and migrates through the lymphatics to the T-cell zone of the draining node. A T cell that meets its peptide on a mature dendritic cell is activated; one that meets it on a resting cell without co-stimulation is switched off (anergy). Innate recognition thus licenses adaptive immunity, which is why adjuvants work and why self, which carries no microbial patterns, is usually tolerated ([tolerance and self-recognition](tolerance-and-self-recognition.md)).

4. **Lymph nodes exist to make rare meetings likely.** A naive T cell specific for any given peptide-MHC is roughly one in 10^5 to 10^6. Antigen arrives in the draining node within hours via lymph; naive T cells enter from blood through high endothelial venules, scan dendritic cells for about a day, and leave to try the next node until they find their antigen. The node concentrates antigen, presenting cells and lymphocytes in one small volume ([lymphatic architecture](../../05-tissues-and-anatomy/02-body-organization/vascular-and-lymphatic-architecture.md)). Swollen nodes are the visible sign that this is happening.

5. **MHC is the most polymorphic human gene system, by selection.** The IMGT/HLA database lists tens of thousands of alleles (2020s), and each person carries up to six different class I and six to eight class II molecules. Because each variant binds different peptides, a pathogen that escapes one person's presentation faces a different set in the next, and heterozygotes present more than homozygotes. This is balancing selection driven by pathogens ([natural selection](../../04-genetics-evolution-and-development/02-evolution/natural-selection-and-population-genetics.md)), and it is the reason no two unrelated people are tissue-compatible.

6. **HLA type is the strongest genetic determinant of immune disease and of some drug reactions.** HLA-B27 raises the risk of ankylosing spondylitis roughly 50- to 100-fold; HLA-DQ2 and DQ8 are near-necessary for coeliac disease because they bind deamidated gluten peptides; HLA-DR3 and DR4 predispose to type 1 diabetes, DR4 to rheumatoid arthritis. HLA-B*57:01 predicts hypersensitivity to abacavir and HLA-B*15:02 severe skin reactions to carbamazepine, so testing precedes prescribing ([pharmacogenomics](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/pharmacogenomics-and-individual-variation.md)). The mechanism in each case is the same: a particular groove presents a particular self or drug-modified peptide.

7. **Presentation is where pathogens and tumours hide, and where other cells watch for hiding.** Herpes simplex blocks TAP, cytomegalovirus degrades class I, many tumours lose class I by mutation. A cell without class I is invisible to CD8 T cells but, lacking the inhibitory signal, is killed by Natural Killer (NK) cells ([cytokines, interferons and NK cells](../02-innate-immunity/cytokines-interferons-and-nk-cells.md)).

## Key concepts

| Term | Meaning |
|---|---|
| Major Histocompatibility Complex (MHC) | Gene cluster encoding the peptide-presenting molecules; HLA in humans |
| MHC class I | HLA-A, -B, -C on all nucleated cells; presents cytosolic peptides to CD8 T cells |
| MHC class II | HLA-DR, -DQ, -DP on professional presenting cells; presents endocytosed peptides to CD4 T cells |
| MHC restriction | A T cell recognises peptide only on its own MHC type |
| Cross-presentation | Dendritic cell loading of eaten antigen onto class I |
| Dendritic cell | The professional antigen-presenting cell that initiates T-cell responses |
| Co-stimulation | Second signal (CD80/CD86 to CD28) without which antigen induces anergy |
| Polymorphism | Many alleles at a locus in the population; extreme in HLA |
| HLA association | Statistical link between an HLA allele and a disease or drug reaction |

## How it fits

- **Below:** class I loading depends on the [proteasome and quality control](../../03-cell-biology/01-cell-structure/protein-quality-control-and-degradation.md); class II loading on [endosomal trafficking](../../03-cell-biology/01-cell-structure/membrane-trafficking-and-secretion.md); dendritic cell migration on the [lymphatics](../../05-tissues-and-anatomy/02-body-organization/vascular-and-lymphatic-architecture.md); the [innate](../02-innate-immunity/barriers-and-pattern-recognition.md) signal is the licence.
- **Above:** HLA matching and allorecognition are the core of [transplant immunology](../04-immunity-in-disease/transplant-and-tumour-immunology.md); HLA-typed prescribing is [pharmacogenomics](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/pharmacogenomics-and-individual-variation.md); HLA associations run through [autoimmunity](../04-immunity-in-disease/autoimmunity.md) and the rheumatological diseases of layer 12.
- **Siblings:** presentation is the input to [T cells](t-cells.md); B cells present antigen to get T-cell help ([B cells and antibodies](b-cells-and-antibodies.md)); the decision between activation and anergy at presentation is the first step of [tolerance](tolerance-and-self-recognition.md).

## Common misconceptions

- **"T cells recognise proteins."** They recognise short peptides in an MHC groove; the shape of the native protein is invisible to them, which is why they are unaffected by the conformational tricks that defeat antibodies.
- **"MHC exists to reject transplants."** Transplant rejection is a by-product of a system selected to present pathogen peptides; the polymorphism that frustrates surgeons is what protects populations.
- **"Carrying a risk allele means getting the disease."** Most people with HLA-B27 never develop ankylosing spondylitis and most DQ2 carriers never develop coeliac disease; HLA sets a necessary groove, not a sufficient cause.

## Go deeper

- Rolf M. Zinkernagel and Peter C. Doherty, "Restriction of in vitro T cell-mediated cytotoxicity in lymphocytic choriomeningitis within a syngeneic or semiallogeneic system", *Nature* (1974): the discovery of MHC restriction.
- Kenneth Murphy and Casey Weaver, *Janeway's Immunobiology* (10th ed., 2022), chapter 6: antigen processing and presentation.
- Ralph M. Steinman, "Decisions about dendritic cells: past, present, and future", *Annual Review of Immunology* (2012): the dendritic cell as the initiator of immunity, by its discoverer.
