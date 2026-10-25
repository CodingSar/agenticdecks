# Membrane trafficking and secretion

> **Layer:** [03 Cell Biology](../README.md) › [Cell structure](README.md)
> **Builds on:** [Translation and protein targeting](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/translation-and-protein-targeting.md), [Lipids and membranes](../../02-biochemistry-and-molecular-biology/01-macromolecules/lipids-and-membranes.md), [Organelles and compartmentalization](organelles-and-compartmentalization.md), [The cytoskeleton and cell motility](the-cytoskeleton-and-cell-motility.md)
> **Enables:** [Synaptic transmission and neurotransmitters](../../06-physiology/02-nervous-system/synaptic-transmission-and-neurotransmitters.md), [Hormone classes, axes and feedback](../../06-physiology/07-endocrine-system/hormone-classes-axes-and-feedback.md), [Antigen presentation and MHC](../../07-microbiology-and-immunology/03-adaptive-immunity/antigen-presentation-and-mhc.md), [Pathogenesis, virulence and toxins](../../07-microbiology-and-immunology/01-microbes-and-infection/pathogenesis-virulence-and-toxins.md)

## Essence

Cells move proteins and lipids between compartments and across the plasma membrane without ever letting them cross a bilayer: they pinch off a vesicle from one membrane and fuse it with another. Membrane trafficking is this continuous budding and fusion, routed by coat proteins, molecular tags and fusion machinery so that each cargo reaches its destination. Secretion (exocytosis) and uptake (endocytosis) are its two outward and inward faces. The idea that makes it work is **topological conservation**: because a vesicle's lumen is continuous with the lumen it came from, the inside of the endoplasmic reticulum, the Golgi, the lysosome and the outside of the cell are one space, and a protein's orientation never has to be reversed. Insulin release, neurotransmission, antibody secretion, cholesterol uptake, antigen presentation and the entry of viruses and toxins all run on this system.

## Core tenets

1. **Secretory proteins enter the endoplasmic reticulum once and never cross a membrane again.** A signal sequence threads the nascent chain through the Sec61 translocon into the Endoplasmic Reticulum (ER) lumen or inserts it as a membrane protein ([protein targeting](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/translation-and-protein-targeting.md)). From there to the cell surface the protein travels inside vesicles. A domain facing the ER lumen will face the outside of the cell; a cytosolic domain stays cytosolic. This is why receptor ligand-binding sites, glycosylation and disulfide bonds are all extracellular, and why the cytosol is reducing while the outside is oxidising.

2. **Budding is driven by coat proteins that select cargo and bend the membrane.** Clathrin (plasma membrane and Golgi to endosome), COPII (ER to Golgi) and COPI (Golgi to ER and within the Golgi) polymerise into a lattice that captures adaptor proteins bound to cargo and deforms the patch into a bud; dynamin or related Guanosine Triphosphatases (GTPases) pinch it off. Cargo selection is by short sorting signals recognised by adaptors, so trafficking, like compartmentalisation, is an information system: the vesicle knows what it carries because the coat only packaged proteins with the right tag.

3. **Fusion is specific because of matching Soluble N-ethylmaleimide-sensitive factor Attachment protein Receptors (SNAREs) and Rab GTPases.** Each compartment displays its own Rab proteins, which recruit tethering factors, and its own SNAREs; a vesicle SNARE (v-SNARE) zips up with a target SNARE (t-SNARE) to pull two bilayers close enough to merge. The cost of membrane fusion (removing water from between two charged surfaces) is paid by the SNARE zipper. Botulinum and tetanus toxins are proteases that cleave neuronal SNAREs, which is why one causes flaccid and the other spastic paralysis: no SNARE, no neurotransmitter release ([toxins](../../07-microbiology-and-immunology/01-microbes-and-infection/pathogenesis-virulence-and-toxins.md)).

4. **Constitutive secretion is the default; regulated secretion waits for calcium.** Every cell continuously delivers membrane and matrix proteins to its surface. Specialised cells (neurons, beta cells, mast cells, exocrine glands) also store cargo in dense granules and release it in milliseconds to minutes when cytosolic calcium rises. Synaptotagmin is the calcium sensor on synaptic vesicles; a rise from ~100 nM to tens of micromolar at the active zone triggers fusion within ~1 ms. Insulin secretion follows the same logic on a slower clock: glucose metabolism raises Adenosine Triphosphate (ATP), closes a potassium channel, depolarises the cell, opens calcium channels, and granules fuse. The sulfonylurea drugs act on that potassium channel.

5. **Endocytosis recovers membrane, takes up nutrients and terminates signals.** Receptor-mediated endocytosis concentrates ligand-bound receptors into clathrin-coated pits: the Low-Density Lipoprotein (LDL) receptor binds LDL at the surface, is internalised, releases cholesterol in the acidic endosome and recycles to the surface every ~10 minutes. Familial hypercholesterolaemia is a defect in this one cycle, and a heterozygote with half the receptors has roughly double the plasma LDL cholesterol. Activated signalling receptors are also internalised and either recycled (resensitisation) or sent to the lysosome (down-regulation), which sets the duration of a hormonal signal.

6. **The endosome sorts by pH.** As an endosome matures its lumen acidifies (from ~6.5 to ~5), and many ligands release from their receptors at low pH, so receptor and cargo can be sent to different fates. Viruses exploit this: influenza haemagglutinin changes shape at endosomal pH and fuses the viral envelope with the endosomal membrane, delivering the genome to the cytosol. Drugs that raise endosomal pH (chloroquine) block that step, which is why they were tried, and mostly failed, as antivirals.

7. **Antigen presentation is trafficking read by the immune system.** Proteins degraded in the cytosol are loaded onto Major Histocompatibility Complex (MHC) class I in the ER and shown to cytotoxic T cells; proteins taken up by endocytosis are degraded in endosomes and loaded onto MHC class II for helper T cells. The two pathways report two compartments, so the immune system can distinguish an infected cell (intracellular antigen) from one that has eaten a pathogen ([antigen presentation](../../07-microbiology-and-immunology/03-adaptive-immunity/antigen-presentation-and-mhc.md)).

8. **Polarised cells route cargo to the right surface.** An epithelial cell sends transporters to its apical membrane and others to its basolateral membrane, using distinct sorting signals and separate vesicle populations; tight junctions prevent the two populations from mixing. Mis-sorting is disease: in some forms of cystic fibrosis the chloride channel folds poorly and never leaves the ER, so the apical membrane simply lacks it. The trafficked channel is normal in function; the problem is delivery.

## Key concepts

| Term | Meaning |
|---|---|
| Exocytosis / endocytosis | Fusion of a vesicle with the plasma membrane to release contents / budding inward to take material up |
| Coat protein (clathrin, COPI, COPII) | Lattice that selects cargo and shapes a bud at a given membrane |
| Adaptor protein | Links a cargo sorting signal to the coat |
| SNARE | Paired proteins on vesicle and target whose zipping drives fusion |
| Rab GTPase | Compartment-specific switch that recruits tethers and gives a membrane its identity |
| Regulated secretion | Storage of cargo in granules until a calcium signal triggers release |
| Receptor-mediated endocytosis | Uptake of a ligand concentrated by its receptor in coated pits |
| Endosome | Sorting compartment whose falling pH separates cargo from receptor |
| Apical / basolateral | The two surfaces of a polarised epithelial cell, with distinct protein sets |

## How it fits

- **Below:** inherits the translocon and signal sequences from [translation and targeting](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/translation-and-protein-targeting.md), the bilayer's fusion energetics from [lipids and membranes](../../02-biochemistry-and-molecular-biology/01-macromolecules/lipids-and-membranes.md), and compartment identity from [organelles](organelles-and-compartmentalization.md).
- **Above:** [synaptic transmission](../../06-physiology/02-nervous-system/synaptic-transmission-and-neurotransmitters.md) and [hormone release](../../06-physiology/07-endocrine-system/hormone-classes-axes-and-feedback.md) are regulated exocytosis; [antigen presentation](../../07-microbiology-and-immunology/03-adaptive-immunity/antigen-presentation-and-mhc.md) reads the two degradation routes; [viral entry and toxins](../../07-microbiology-and-immunology/01-microbes-and-infection/pathogenesis-virulence-and-toxins.md) hijack endocytosis and SNAREs; LDL receptor cycling underlies lipid disorders in [endocrinology](../../12-organ-system-specialties/05-endocrinology/obesity-lipids-and-metabolic-syndrome.md).
- **Siblings:** vesicles ride the [cytoskeleton](the-cytoskeleton-and-cell-motility.md); misfolded cargo is caught by [quality control](protein-quality-control-and-degradation.md) before it can leave the ER; [junctions](../03-cells-in-community/cell-to-cell-communication-and-junctions.md) keep apical and basolateral pools apart.

## Common misconceptions

- **"Secreted proteins are pushed through the plasma membrane."** They never cross a bilayer after entering the ER; they are delivered inside a vesicle that merges with the surface.
- **"A disease-causing mutation must destroy a protein's function."** Many only change where it goes; a functional channel stuck in the ER is as absent as a deleted one.
- **"Endocytosis is for eating."** Its larger role is regulatory: recovering membrane after exocytosis and switching off receptors by removing them from the surface.

## Go deeper

- Bruce Alberts and colleagues, *Molecular Biology of the Cell* (7th ed., 2022), chapter on intracellular membrane traffic: coats, SNAREs and Rabs with mechanisms.
- James E. Rothman, "The Principle of Membrane Fusion in the Cell" (Nobel lecture, 2013): the SNARE hypothesis from its discoverer.
- Michael S. Brown and Joseph L. Goldstein, "A Receptor-Mediated Pathway for Cholesterol Homeostasis", *Science* (1986): the LDL receptor cycle and familial hypercholesterolaemia.
