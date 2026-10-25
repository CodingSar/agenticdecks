# T cells

> **Layer:** [07 Microbiology and Immunology](../README.md) › [Adaptive immunity](README.md)
> **Builds on:** [Antigen presentation and MHC](antigen-presentation-and-mhc.md), [Cytokines, interferons and NK cells](../02-innate-immunity/cytokines-interferons-and-nk-cells.md), [Second messengers and kinase cascades](../../02-biochemistry-and-molecular-biology/04-cell-signalling/second-messengers-and-kinase-cascades.md), [Cell death: apoptosis, necrosis and autophagy](../../03-cell-biology/02-the-cell-life-cycle/cell-death-apoptosis-necrosis-and-autophagy.md), [Nonlinear dynamics, oscillations and networks](../../01-quantitative-and-scientific-foundations/03-systems-and-models/nonlinear-dynamics-oscillations-and-networks.md)
> **Enables:** [B cells and antibodies](b-cells-and-antibodies.md), [Immunodeficiency](../04-immunity-in-disease/immunodeficiency.md), [Chronic inflammation and granulomas](../../08-pathology/01-cell-and-tissue-injury/chronic-inflammation-and-granulomas.md), [HIV and chronic viral infections](../../12-organ-system-specialties/08-infectious-diseases/hiv-and-chronic-viral-infections.md), [Anti-inflammatory and immunomodulatory drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anti-inflammatory-and-immunomodulatory-drugs.md)

## Essence

T cells are the adaptive immune system's decision-makers and its assassins. Each carries a single receptor, assembled by random gene rearrangement, that recognises one peptide-Major Histocompatibility Complex (MHC) combination; antigen selects the few clones that fit and drives them to divide thousands-fold. Helper (CD4) T cells read the cytokine context of their activation and commit to one of several programmes that direct macrophages, B cells, neutrophils or eosinophils; cytotoxic (CD8) T cells kill infected cells by inducing apoptosis. Two costs are inherent in the design: random receptors must be purged of those that bind self, which the thymus does imperfectly, and an exponential response must be shut down, so most effector cells die and a few remain as memory.

## Core tenets

1. **Diversity comes from random assembly, and specificity from clonal selection.** Each developing T cell cuts and joins variable, diversity and joining gene segments (V(D)J recombination, by the RAG enzymes) with imprecise junctions, producing a repertoire of roughly 10^7 to 10^8 distinct receptors in an adult from a theoretical 10^15 or more. Each cell keeps one receptor. Burnet's clonal selection theory (1957) follows: antigen does not instruct a cell what to make, it selects the pre-existing clones that fit and expands them 10^3- to 10^4-fold within a week.

2. **The thymus selects for usefulness and against self.** Thymocytes that cannot bind self MHC at all die by neglect (positive selection fails); those that bind self peptide-MHC strongly are deleted (negative selection); about 2 to 5% survive. Negative selection is extended to tissue antigens by the transcription factor AIRE, which makes medullary thymic cells express insulin, thyroglobulin and thousands of other peripheral proteins. Loss of AIRE causes multi-organ autoimmunity. The thymus shrinks after puberty, so the repertoire is built early; a child born without a thymus has almost no T cells.

3. **Activation needs three signals, and the drugs of transplantation each block one.** Signal 1 is the receptor engaging peptide-MHC, transmitted through Lck and ZAP-70 kinases to calcineurin, which activates the transcription factor NFAT and interleukin-2 production ([kinase cascades](../../02-biochemistry-and-molecular-biology/04-cell-signalling/second-messengers-and-kinase-cascades.md)). Signal 2 is co-stimulation, CD28 binding CD80 or CD86 on a licensed dendritic cell; signal 1 without it produces anergy. Signal 3 is the cytokine milieu that decides the programme. Calcineurin inhibitors (ciclosporin, tacrolimus) block signal 1, CTLA-4-immunoglobulin blocks signal 2, mTOR inhibitors and antimetabolites block the proliferation that follows. Inhibitory receptors on the T cell, CTLA-4 and PD-1, raise the threshold and end responses; antibodies that block them unleash T cells against tumours, and against self ([transplant and tumour immunology](../04-immunity-in-disease/transplant-and-tumour-immunology.md)).

4. **CD4 helper cells commit to a programme set by the first cytokines they meet.** Interleukin-12 induces T-bet and the Th1 programme (interferon-gamma, which activates macrophages to kill what they have swallowed: tuberculosis, *Leishmania*, granulomas). Interleukin-4 induces GATA3 and Th2 (interleukin-4, -5, -13: helminths, allergy). Interleukin-6 with transforming growth factor beta and interleukin-23 induces RORgamma-t and Th17 (interleukin-17: extracellular bacteria and fungi at mucosa; psoriasis, spondyloarthritis). Bcl-6 marks follicular helper cells that drive germinal centres; FOXP3 marks regulatory T cells that suppress. Each master regulator represses the others, a [bistable switch](../../01-quantitative-and-scientific-foundations/03-systems-and-models/nonlinear-dynamics-oscillations-and-networks.md), so a committed response is hard to redirect. The wrong programme can be fatal: a Th2 response to leprosy (lepromatous) fails where Th1 (tuberculoid) contains it.

5. **CD8 cytotoxic cells kill by instructing apoptosis.** On recognising peptide on class I, a cytotoxic cell releases perforin, which forms pores, and granzymes, which enter and activate caspases; Fas ligand on the T cell triggers the Fas death receptor on the target ([apoptosis](../../03-cell-biology/02-the-cell-life-cycle/cell-death-apoptosis-necrosis-and-autophagy.md)). Apoptosis packages viral contents rather than spilling them, and the killer detaches to kill again. The cost: hepatitis B virus injures the liver mainly through the cytotoxic cells that attack infected hepatocytes, so immune strength, not viral load, sets the severity of acute hepatitis.

6. **Contraction and memory are built into the programme.** After antigen is cleared, more than 90% of effector cells die by apoptosis within weeks; survivors persist as central memory cells in lymphoid organs, effector memory cells in circulation and tissue-resident memory cells at the site of infection, each primed to respond in hours ([immunological memory](immunological-memory-and-vaccination.md)). When antigen is not cleared, as in chronic viral infection and cancer, continued stimulation drives exhaustion: progressive loss of function with high PD-1 expression, which checkpoint blockade partly reverses.

7. **T-cell loss defines the pattern of immunodeficiency.** Without T cells there is no antibody help and no cytotoxic defence, so severe combined immunodeficiency is fatal in infancy without transplantation. Human Immunodeficiency Virus (HIV) destroys CD4 cells; below about 200 cells per microlitre the diseases of lost helper function appear (*Pneumocystis* pneumonia, cryptococcal meningitis, cytomegalovirus retinitis, reactivated tuberculosis), and the count rises again with antiretroviral therapy ([immunodeficiency](../04-immunity-in-disease/immunodeficiency.md)).

## Key concepts

| Term | Meaning |
|---|---|
| T-cell receptor | Alpha-beta heterodimer recognising peptide-MHC; one specificity per cell |
| V(D)J recombination | RAG-mediated random joining of gene segments that generates receptor diversity |
| Clonal selection | Antigen expands the pre-existing clones that fit it |
| AIRE | Transcription factor that expresses tissue antigens in the thymus for negative selection |
| Three signals | Antigen, co-stimulation and cytokine: all needed for full activation |
| Anergy | Unresponsiveness induced by antigen without co-stimulation |
| Th1, Th2, Th17, Tfh, Treg | Helper programmes defined by master regulator and signature cytokines |
| Perforin and granzymes | Cytotoxic granule proteins that induce apoptosis in targets |
| Exhaustion | Loss of T-cell function under chronic antigen stimulation, marked by PD-1 |

## How it fits

- **Below:** receptor signalling is a [kinase cascade](../../02-biochemistry-and-molecular-biology/04-cell-signalling/second-messengers-and-kinase-cascades.md); killing uses the host's own [apoptosis](../../03-cell-biology/02-the-cell-life-cycle/cell-death-apoptosis-necrosis-and-autophagy.md) machinery; subset commitment is a [bistable switch](../../01-quantitative-and-scientific-foundations/03-systems-and-models/nonlinear-dynamics-oscillations-and-networks.md); the cytokine programmes are those of [innate immunity](../02-innate-immunity/cytokines-interferons-and-nk-cells.md).
- **Above:** Th1-driven macrophage activation builds the [granuloma](../../08-pathology/01-cell-and-tissue-injury/chronic-inflammation-and-granulomas.md); calcineurin inhibitors and checkpoint antibodies are in [immunomodulatory drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anti-inflammatory-and-immunomodulatory-drugs.md); CD4 depletion is the story of [HIV](../../12-organ-system-specialties/08-infectious-diseases/hiv-and-chronic-viral-infections.md).
- **Siblings:** T cells need [antigen presentation](antigen-presentation-and-mhc.md) to see anything, give [B cells](b-cells-and-antibodies.md) the help that makes good antibody, leave behind the [memory](immunological-memory-and-vaccination.md) that vaccines aim for, and are the main object of [tolerance](tolerance-and-self-recognition.md).

## Common misconceptions

- **"The immune system learns what to make."** Receptors are made at random before any antigen is seen; antigen only selects. This is why the repertoire can recognise molecules that do not yet exist.
- **"More immune response is always better."** Cytotoxic T cells cause the liver damage of hepatitis B and much of the lung damage of tuberculosis; the right amount, in the right programme, is the goal.

## Go deeper

- F. Macfarlane Burnet, *The Clonal Selection Theory of Acquired Immunity* (1959): the founding idea.
- Kenneth Murphy and Casey Weaver, *Janeway's Immunobiology* (10th ed., 2022), chapters 7 to 9: T-cell development, activation and effector function.
- Abul K. Abbas, Andrew H. Lichtman and Shiv Pillai, *Cellular and Molecular Immunology* (10th ed., 2021): a clearer, shorter alternative treatment of the same ground.
