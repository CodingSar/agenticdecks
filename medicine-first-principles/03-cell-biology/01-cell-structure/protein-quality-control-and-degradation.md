# Protein quality control and degradation

> **Layer:** [03 Cell Biology](../README.md) › [Cell structure](README.md)
> **Builds on:** [Proteins: structure and folding](../../02-biochemistry-and-molecular-biology/01-macromolecules/proteins-structure-and-folding.md), [Translation and protein targeting](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/translation-and-protein-targeting.md), [Organelles and compartmentalization](organelles-and-compartmentalization.md), [Kinetics, equilibrium and catalysis](../../00-physical-and-chemical-foundations/02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md)
> **Enables:** [Neurodegenerative disease](../../12-organ-system-specialties/10-neurology/neurodegenerative-disease.md), [Diseases of aging and degeneration](../../08-pathology/04-genetic-metabolic-and-environmental-disease/diseases-of-aging-and-degeneration.md), [Anticancer drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md), [The cellular stress response](../03-cells-in-community/the-cellular-stress-response.md)

## Essence

A cell makes millions of protein molecules an hour, and a substantial fraction misfold, are damaged by heat or oxidation, or are simply no longer needed. Protein quality control is the machinery that recognises these, tries to refold them, and otherwise destroys them: chaperones, the ubiquitin–proteasome system and autophagy to the lysosome. Its logic is that **a protein's concentration is set by synthesis minus degradation**, so controlled destruction is as much a regulatory tool as controlled transcription, and a half-life can be minutes (cyclins, transcription factors) or years (lens crystallins). When the system is overwhelmed, misfolded proteins aggregate, and aggregates are the common pathology of Alzheimer's, Parkinson's, Huntington's and prion diseases, of amyloidosis, and of much of ageing.

## Core tenets

1. **Folding is marginal, so misfolding is common and must be managed.** The folded state of a typical protein is only ~20–60 kJ/mol more stable than the unfolded ensemble ([protein structure](../../02-biochemistry-and-molecular-biology/01-macromolecules/proteins-structure-and-folding.md)), and a crowded cytosol favours aggregation of exposed hydrophobic surfaces. Roughly a tenth to a third of newly made polypeptides are estimated to be degraded shortly after synthesis as failures. Quality control is therefore not an emergency system; it runs continuously.

2. **Chaperones buy time and prevent aggregation by binding exposed hydrophobic patches.** Heat Shock Protein 70 (Hsp70) binds unfolded segments in an Adenosine Triphosphate (ATP)-dependent cycle and releases them to try again; the chaperonin cage (Hsp60, TRiC) encloses a single chain so it can fold without neighbours; Hsp90 matures signalling proteins such as kinases and steroid receptors. Chaperone expression rises within minutes of heat, oxidative or ischaemic stress because the stress itself (unfolded protein) is the signal, which is a textbook negative feedback loop ([stress response](../03-cells-in-community/the-cellular-stress-response.md)).

3. **The ubiquitin–proteasome system destroys selected proteins fast and specifically.** An enzyme cascade (E1 activating, E2 conjugating, E3 ligase) attaches a chain of ubiquitin to a lysine on the target; the 26S proteasome recognises the chain, unfolds the protein and cuts it into peptides. Specificity lives in the ~600 human E3 ligases, each recognising a motif (a phosphorylated degron, an exposed N-terminus, a misfolded surface). This is how the [cell cycle](../02-the-cell-life-cycle/the-cell-cycle-and-its-checkpoints.md) advances irreversibly (cyclins are destroyed, not inhibited), how p53 is kept low in healthy cells, and how a hypoxic cell stabilises its hypoxia-inducible factor when oxygen-dependent hydroxylation stops marking it for destruction.

4. **The endoplasmic reticulum has its own inspection and a route back out.** Secretory proteins fold in the Endoplasmic Reticulum (ER) under the eye of lectin chaperones that read glycan trimming as a timer; a chain that fails repeatedly is retrotranslocated to the cytosol and degraded by the proteasome (ER-Associated Degradation, ERAD). When misfolded protein accumulates faster than this, the Unfolded Protein Response (UPR) slows translation, expands the ER and increases chaperones, and if that fails, triggers apoptosis. The common cystic fibrosis mutation (F508del) is a trafficking-competent channel destroyed by ERAD; alpha-1 antitrypsin Z variant polymerises in hepatocyte ER, causing liver disease by accumulation and lung disease by absence.

5. **Autophagy clears what the proteasome cannot: aggregates, organelles and bulk cytoplasm.** A double membrane engulfs a region of cytoplasm, a damaged mitochondrion (mitophagy) or a tagged aggregate, and fuses with the lysosome. Starvation induces it to recycle amino acids; it is the only route for turning over whole organelles. Mutations in mitophagy genes (PINK1, Parkin) cause early-onset Parkinson's disease, and the accumulation of lipofuscin in ageing cells is undigested autophagic residue. The lysosomal storage diseases ([organelles](organelles-and-compartmentalization.md)) are the terminal step of this pathway failing.

6. **Aggregation is a nucleated polymerisation, which explains its tempo and its spread.** Misfolded proteins with exposed beta strands can stack into cross-beta amyloid fibrils. Nucleation is slow and rare; growth on an existing fibril is fast. So aggregation diseases have a long silent phase, then accelerate; and a seed can template the misfolding of normal protein, which is how prions propagate without nucleic acid and how tau and alpha-synuclein pathology appear to spread from cell to cell along anatomical pathways in Alzheimer's and Parkinson's disease ([neurodegeneration](../../12-organ-system-specialties/10-neurology/neurodegenerative-disease.md)). Systemic amyloidosis is the same chemistry with light chains, transthyretin or serum amyloid A deposited in kidney, heart and nerve.

7. **Proteostasis declines with age, and this is a leading theory of why ageing has a shared phenotype.** Chaperone induction weakens, proteasome activity falls, lysosomes fill with indigestible material and oxidised proteins accumulate. Long-lived post-mitotic cells (neurons, cardiomyocytes) cannot dilute damage by dividing, which is why neurodegeneration and cardiac amyloid are diseases of late life ([diseases of aging](../../08-pathology/04-genetic-metabolic-and-environmental-disease/diseases-of-aging-and-degeneration.md)). In model organisms, interventions that enhance proteostasis (reduced insulin-like signalling, dietary restriction, boosted autophagy) extend lifespan.

8. **Degradation is a drug target in both directions.** Proteasome inhibitors (bortezomib) kill plasma cells in myeloma because a cell secreting its own weight in antibody every few days depends on ERAD and the proteasome more than any other. Targeted protein degraders (thalidomide analogues and designed bifunctional molecules) recruit an E3 ligase to a protein of choice and remove it rather than merely blocking it. Heat shock protein inhibitors and autophagy modulators are under study for cancer and neurodegeneration ([anticancer drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md)).

## Key concepts

| Term | Meaning |
|---|---|
| Proteostasis | The network that keeps every protein at the right concentration and conformation |
| Chaperone | Protein that binds unfolded chains to prevent aggregation and assist folding; Hsp70, Hsp90, chaperonins |
| Ubiquitin | 76-residue tag whose chains mark a protein for the proteasome; attached by E1–E2–E3 cascades |
| E3 ligase | The enzyme that chooses the substrate; the source of specificity in degradation |
| Proteasome | Barrel-shaped protease that unfolds and digests ubiquitinated proteins |
| ERAD | Retrotranslocation of misfolded ER proteins to the cytosol for proteasomal destruction |
| Unfolded protein response | ER stress programme: less translation, more chaperones, apoptosis if unresolved |
| Autophagy | Lysosomal degradation of engulfed cytoplasm, aggregates or organelles |
| Amyloid | Cross-beta fibrils formed by nucleated polymerisation of misfolded protein |
| Degron | Short motif that marks a protein for degradation, often after phosphorylation |

## How it fits

- **Below:** rests on the marginal stability and hydrophobic collapse described in [protein folding](../../02-biochemistry-and-molecular-biology/01-macromolecules/proteins-structure-and-folding.md), the nucleation kinetics of [chemical kinetics](../../00-physical-and-chemical-foundations/02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md), and the compartments of the [organelle](organelles-and-compartmentalization.md) leaf.
- **Above:** explains why [neurodegenerative diseases](../../12-organ-system-specialties/10-neurology/neurodegenerative-disease.md) are proteinopathies, why [ageing tissues](../../08-pathology/04-genetic-metabolic-and-environmental-disease/diseases-of-aging-and-degeneration.md) accumulate aggregates, how hypoxia signalling works in [pathology](../../08-pathology/01-cell-and-tissue-injury/cell-injury-adaptation-and-death.md), and a class of [anticancer drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md).
- **Siblings:** the proteasome drives the irreversibility of the [cell cycle](../02-the-cell-life-cycle/the-cell-cycle-and-its-checkpoints.md); failed quality control ends in [apoptosis](../02-the-cell-life-cycle/cell-death-apoptosis-necrosis-and-autophagy.md); the [stress response](../03-cells-in-community/the-cellular-stress-response.md) is its regulatory layer.

## Common misconceptions

- **"Proteins are stable once folded."** Folding is reversible and marginal; a protein samples unfolded states continuously, and the cell relies on constant surveillance.
- **"Degradation is waste disposal."** It is a regulatory mechanism with the same precision as transcription, and the only way to make a process irreversible on a timescale of minutes.
- **"Aggregates kill because they are big."** Small soluble oligomers are often the most toxic species, and large inclusions may be partly protective sequestration; the fibril is the end point, not necessarily the culprit.

## Go deeper

- F. Ulrich Hartl, Andreas Bracher and Manajit Hayer-Hartl, "Molecular Chaperones in Protein Folding and Proteostasis", *Nature* (2011): the chaperone network as a system.
- Aaron Ciechanover, "Intracellular Protein Degradation: From a Vague Idea Through the Lysosome and the Ubiquitin–Proteasome System and onto Human Diseases and Drug Targeting" (Nobel lecture, 2004).
- Christopher M. Dobson, "Protein Folding and Misfolding", *Nature* (2003): why aggregation is a generic property of polypeptides.
- Bruce Alberts and colleagues, *Molecular Biology of the Cell* (7th ed., 2022), sections on protein folding, the proteasome and autophagy.
