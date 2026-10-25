# Membrane trafficking and secretion

> **Layer:** [03 Cell Biology](../README.md) › [Cell structure](README.md)
> **Builds on:** [Translation and protein targeting](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/translation-and-protein-targeting.md), [Lipids and membranes](../../02-biochemistry-and-molecular-biology/01-macromolecules/lipids-and-membranes.md), [Organelles and compartmentalization](organelles-and-compartmentalization.md), [The cytoskeleton and cell motility](the-cytoskeleton-and-cell-motility.md)
> **Enables:** [Synaptic transmission and neurotransmitters](../../06-physiology/02-nervous-system/synaptic-transmission-and-neurotransmitters.md), [Hormone classes, axes and feedback](../../06-physiology/07-endocrine-system/hormone-classes-axes-and-feedback.md), [Antigen presentation and MHC](../../07-microbiology-and-immunology/03-adaptive-immunity/antigen-presentation-and-mhc.md), [Pathogenesis, virulence and toxins](../../07-microbiology-and-immunology/01-microbes-and-infection/pathogenesis-virulence-and-toxins.md)

## Essence

Cells move proteins and lipids between compartments and across the plasma membrane without ever letting them cross a bilayer: they pinch off a vesicle from one membrane and fuse it with another. Membrane trafficking is this continuous budding and fusion, routed by coat proteins, sorting tags and fusion machinery so each cargo reaches its destination; exocytosis and endocytosis are its outward and inward faces. The idea that makes it work is **topological conservation**: a vesicle's lumen is continuous with the lumen it came from, so the inside of the endoplasmic reticulum, the Golgi, the lysosome and the outside of the cell are one space, and a protein's orientation never has to be reversed. Insulin release, neurotransmission, cholesterol uptake, antigen presentation and the entry of viruses and toxins all run on it.

## Core tenets

1. **Secretory proteins enter the endoplasmic reticulum once and never cross a membrane again.** A signal sequence threads the nascent chain through the Sec61 translocon into the Endoplasmic Reticulum (ER) lumen or inserts it into the membrane ([protein targeting](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/translation-and-protein-targeting.md)). From there to the surface it travels inside vesicles, so a domain facing the ER lumen will face the outside of the cell. This is why receptor ligand-binding sites, glycans and disulfide bonds are extracellular.

2. **Budding is driven by coats that select cargo and bend the membrane.** Clathrin (plasma membrane and Golgi to endosome), COPII (ER to Golgi) and COPI (Golgi to ER) polymerise into lattices that capture adaptor proteins bound to cargo and deform the patch into a bud; dynamin pinches it off. Cargo is chosen by short sorting signals read by adaptors, so trafficking is an information system: the coat only packages tagged proteins.

3. **Fusion is specific because of matching Soluble N-ethylmaleimide-sensitive factor Attachment protein Receptors (SNAREs) and Rab GTPases.** Each compartment displays its own Rab proteins, which recruit tethers, and its own SNAREs; a vesicle SNARE zips up with a target SNARE to pull two bilayers close enough to merge, paying the cost of removing water from between charged surfaces. Botulinum and tetanus toxins are proteases that cleave neuronal SNAREs, which is why one causes flaccid and the other spastic paralysis: no SNARE, no transmitter release ([toxins](../../07-microbiology-and-immunology/01-microbes-and-infection/pathogenesis-virulence-and-toxins.md)).

4. **Constitutive secretion is the default; regulated secretion waits for calcium.** Neurons, beta cells, mast cells and exocrine glands also store cargo in granules and release it when cytosolic calcium rises: synaptotagmin on synaptic vesicles triggers fusion within ~1 ms of calcium entry. Insulin follows the same logic on a slower clock: glucose metabolism raises Adenosine Triphosphate (ATP), closes a potassium channel, depolarises the cell, opens calcium channels and granules fuse. Sulfonylureas act on that potassium channel.

5. **Endocytosis recovers membrane, takes up nutrients and terminates signals.** The Low-Density Lipoprotein (LDL) receptor binds LDL at the surface, is internalised in a clathrin pit, releases cholesterol in the acidic endosome and recycles every ~10 minutes. Familial hypercholesterolaemia is a defect in this one cycle; a heterozygote with half the receptors has roughly double the plasma LDL. Activated receptors are also internalised and recycled or destroyed, which sets how long a hormone acts.

6. **The endosome sorts by pH.** As it matures its lumen acidifies from ~6.5 to ~5, many ligands release from their receptors, and receptor and cargo can be sent to different fates. Viruses exploit this: influenza haemagglutinin changes shape at endosomal pH and fuses the viral envelope with the endosomal membrane, delivering the genome to the cytosol.

7. **Antigen presentation is trafficking read by the immune system.** Proteins degraded in the cytosol are loaded onto Major Histocompatibility Complex (MHC) class I in the ER for cytotoxic T cells; proteins taken up by endocytosis are degraded in endosomes and loaded onto MHC class II for helper T cells. Two routes report two compartments, so the immune system can tell an infected cell from one that has eaten a pathogen ([antigen presentation](../../07-microbiology-and-immunology/03-adaptive-immunity/antigen-presentation-and-mhc.md)).

8. **Polarised cells route cargo to the right surface, and mis-sorting is disease.** An epithelial cell sends some transporters apically and others basolaterally, and tight junctions keep the two membranes apart. In the common cystic fibrosis mutation the chloride channel folds poorly and never leaves the ER; the channel would work, but it is never delivered.

## Key concepts

| Term | Meaning |
|---|---|
| Exocytosis / endocytosis | Vesicle fusion with the plasma membrane to release contents / inward budding to take material up |
| Coat protein (clathrin, COPI, COPII) | Lattice that selects cargo and shapes a bud at a given membrane |
| SNARE | Paired proteins on vesicle and target whose zipping drives fusion |
| Regulated secretion | Storage in granules until a calcium signal triggers release |
| Receptor-mediated endocytosis | Uptake of a ligand concentrated by its receptor in coated pits |
| Endosome | Sorting compartment whose falling pH separates cargo from receptor |
| Apical / basolateral | The two surfaces of a polarised epithelial cell, with distinct protein sets |

## How it fits

- **Below:** inherits the translocon from [translation and targeting](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/translation-and-protein-targeting.md), fusion energetics from [lipids and membranes](../../02-biochemistry-and-molecular-biology/01-macromolecules/lipids-and-membranes.md), and compartment identity from [organelles](organelles-and-compartmentalization.md).
- **Above:** [synaptic transmission](../../06-physiology/02-nervous-system/synaptic-transmission-and-neurotransmitters.md) and [hormone release](../../06-physiology/07-endocrine-system/hormone-classes-axes-and-feedback.md) are regulated exocytosis; [antigen presentation](../../07-microbiology-and-immunology/03-adaptive-immunity/antigen-presentation-and-mhc.md) reads the two degradation routes; [viruses and toxins](../../07-microbiology-and-immunology/01-microbes-and-infection/pathogenesis-virulence-and-toxins.md) hijack endocytosis and SNAREs; LDL receptor cycling underlies [lipid disorders](../../12-organ-system-specialties/05-endocrinology/obesity-lipids-and-metabolic-syndrome.md).
- **Siblings:** vesicles ride the [cytoskeleton](the-cytoskeleton-and-cell-motility.md); misfolded cargo is caught by [quality control](protein-quality-control-and-degradation.md) before leaving the ER; [junctions](../03-cells-in-community/cell-to-cell-communication-and-junctions.md) keep apical and basolateral pools apart.

## Common misconceptions

- **"Secreted proteins are pushed through the plasma membrane."** They never cross a bilayer after entering the ER; a vesicle carrying them merges with the surface.
- **"A disease mutation must destroy a protein's function."** Many only change where it goes; a working channel stuck in the ER is as absent as a deleted one.
- **"Endocytosis is for eating."** Its larger role is regulatory: recovering membrane after exocytosis and switching receptors off by removing them from the surface.

## Go deeper

- Bruce Alberts and colleagues, *Molecular Biology of the Cell* (7th ed., 2022), chapter on intracellular membrane traffic: coats, SNAREs and Rabs with mechanisms.
- James E. Rothman, "The Principle of Membrane Fusion in the Cell" (Nobel lecture, 2013): the SNARE hypothesis from its discoverer.
- Michael S. Brown and Joseph L. Goldstein, "A Receptor-Mediated Pathway for Cholesterol Homeostasis", *Science* (1986): the LDL receptor cycle and familial hypercholesterolaemia.
