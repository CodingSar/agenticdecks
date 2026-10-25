# Enzymes and catalysis

> **Layer:** [02 Biochemistry and Molecular Biology](../README.md) › [Macromolecules](README.md)
> **Builds on:** [Kinetics, equilibrium and catalysis](../../00-physical-and-chemical-foundations/02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md), [Proteins: structure and folding](proteins-structure-and-folding.md), [Acids, bases and buffers](../../00-physical-and-chemical-foundations/02-chemistry-of-life/acids-bases-and-buffers.md), [Energy and thermodynamics](../../00-physical-and-chemical-foundations/01-physics-of-the-body/energy-and-thermodynamics.md)
> **Enables:** [Metabolism](../02-metabolism/README.md), [Drug metabolism and interactions](../../09-pharmacology-and-therapeutics/01-pharmacokinetics/drug-metabolism-and-interactions.md), [Inborn errors of metabolism](../../08-pathology/04-genetic-metabolic-and-environmental-disease/inborn-errors-of-metabolism.md), [Clinical chemistry and reference ranges](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/clinical-chemistry-and-reference-ranges.md), [Receptor theory, agonists and antagonists](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/receptor-theory-agonists-and-antagonists.md)

## Essence

An enzyme is a protein (occasionally an Ribonucleic Acid (RNA)) that speeds up one reaction by binding its transition state more tightly than its substrate, lowering the activation barrier without touching the equilibrium. Rate enhancements of 10^6 to 10^17 mean that reactions that would take years occur in milliseconds, and only reactions that have an enzyme occur at all. That selectivity channels a shared pool of molecules into pathways and makes metabolism controllable: regulate the enzyme and you regulate the flux. Most drugs are either receptor ligands or enzyme inhibitors, and most inherited metabolic diseases are a missing or crippled enzyme.

## Core tenets

1. **Enzymes change rates, never equilibria.** A catalyst lowers the free energy of the transition state (ΔG‡) and leaves the free-energy difference between substrate and product (ΔG) untouched, so it accelerates the forward and reverse reactions by the same factor. [Thermodynamics](../../00-physical-and-chemical-foundations/01-physics-of-the-body/energy-and-thermodynamics.md) decides whether and how far; the enzyme decides how fast and which.

2. **The active site is complementary to the transition state, not the substrate.** Pauling's insight (1946): a site that bound the substrate perfectly would stabilise it and raise the barrier, so the enzyme instead binds the strained, partly bonded transition state and uses the binding energy to pay for the distortion. Molecules that mimic a transition state are therefore potent inhibitors: statins resemble the intermediate of 3-Hydroxy-3-Methylglutaryl-Coenzyme A (HMG-CoA) reductase, and Human Immunodeficiency Virus (HIV) protease inhibitors mimic the tetrahedral intermediate of peptide hydrolysis.

3. **A handful of chemical tricks does most of the work.** Acid–base catalysis uses side chains whose pKa sits near 7, especially histidine, to donate or accept protons at the right moment. Covalent catalysis forms a transient enzyme–substrate bond (the serine of chymotrypsin, thrombin and acetylcholinesterase). Metal ions polarise water or substrate: zinc in carbonic anhydrase lowers the pKa of a bound water so it attacks carbon dioxide 10^7 times a second. Proximity and orientation hold two reactants in the right geometry. Cofactors (Nicotinamide Adenine Dinucleotide (NAD), Flavin Adenine Dinucleotide (FAD), pyridoxal phosphate, thiamine) supply chemistry that amino-acid side chains cannot.

4. **Michaelis–Menten kinetics describes a saturable catalyst.** With one substrate, rate v = Vmax [S] / (Km + [S]): first-order at low substrate, zero-order at high. Km is the substrate concentration giving half-maximal rate. kcat/Km measures efficiency, with an upper bound of about 10^8–10^9 per molar per second, the rate at which molecules collide by diffusion. Physiological substrate concentrations often lie near Km, so flux responds to supply: glucokinase in liver and pancreatic beta cells has a Km near 8 mmol/L, above fasting glucose, and so acts as a glucose sensor, while hexokinase in other tissues (Km ~0.1 mmol/L) is always saturated.

5. **Inhibition is pharmacology.** Competitive inhibitors occupy the active site and raise the apparent Km but can be outcompeted by substrate (methotrexate on dihydrofolate reductase); non-competitive inhibitors bind elsewhere and lower Vmax. Irreversible inhibitors modify the enzyme covalently: aspirin acetylates cyclo-oxygenase, organophosphates phosphorylate acetylcholinesterase, and beta-lactam antibiotics acylate the bacterial transpeptidase, so recovery requires new enzyme synthesis. Many drug interactions are one drug inhibiting or inducing the enzyme that clears another.

6. **Pathways are controlled at committed, irreversible steps.** The first step unique to a pathway, held far from equilibrium, is where regulation acts: feedback inhibition by the end product, allosteric activation by a signal of demand (Adenosine Monophosphate (AMP) on phosphofructokinase-1), covalent modification by phosphorylation, and slower changes in enzyme amount by transcription. Allosteric enzymes show sigmoidal rather than hyperbolic kinetics, which turns a graded input into a switch.

7. **Enzymes are stereospecific and compartmentalised.** The active site is chiral, so enzymes distinguish mirror-image molecules (only L-amino acids and D-sugars are metabolised; drug enantiomers differ in activity). Isoenzymes catalyse the same reaction in different tissues with different kinetics; placing an enzyme in a mitochondrion, peroxisome or lysosome segregates incompatible chemistry.

8. **Enzymes leaking into blood report tissue injury.** Cytoplasmic enzymes do not belong in plasma; their appearance (transaminases from liver, creatine kinase from muscle, lipase from pancreas) signals damaged membranes, their isoenzyme pattern locates the source, and their half-life sets how long the signal lasts. A missing enzyme, by contrast, shows up as an accumulated substrate: the logic of [inborn errors of metabolism](../../08-pathology/04-genetic-metabolic-and-environmental-disease/inborn-errors-of-metabolism.md) and newborn screening.

## Key concepts

| Term | Meaning |
|---|---|
| Activation energy (ΔG‡) | Free-energy difference between ground state and transition state; sets the rate |
| Transition state | The highest-energy, partly bonded configuration along the reaction path |
| Active site | The pocket where substrate binds and chemistry happens; a few residues do the catalysis |
| Km | Substrate concentration at half-maximal rate; a measure of how easily the enzyme is saturated |
| Vmax, kcat | Maximal rate; turnover number per enzyme molecule per second |
| Cofactor, coenzyme | Metal ion or organic molecule (often a vitamin derivative) required for catalysis |
| Allosteric regulation | Control of activity by a molecule binding away from the active site |
| Isoenzyme | Different proteins catalysing the same reaction, with distinct tissue distribution |

## How it fits

- **Below:** the thermodynamic and kinetic framework comes from [kinetics, equilibrium and catalysis](../../00-physical-and-chemical-foundations/02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md); proton transfer at the active site is [acid–base chemistry](../../00-physical-and-chemical-foundations/02-chemistry-of-life/acids-bases-and-buffers.md); the site itself is a [protein fold](proteins-structure-and-folding.md).
- **Above:** every pathway in [metabolism](../02-metabolism/README.md) is a chain of enzymes; the cytochrome P450 family explains [drug metabolism and interactions](../../09-pharmacology-and-therapeutics/01-pharmacokinetics/drug-metabolism-and-interactions.md); plasma enzyme assays are a pillar of [clinical chemistry](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/clinical-chemistry-and-reference-ranges.md); the mass-action treatment of binding reappears in [receptor theory](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/receptor-theory-agonists-and-antagonists.md).
- **Siblings:** the ribosome and the spliceosome show that [RNA](nucleic-acids.md) can catalyse; [lipid](lipids-and-membranes.md) membranes anchor enzymes in compartments; [glycosyltransferases](carbohydrates-and-glycobiology.md) build sugars without a template.

## Common misconceptions

- **"Enzymes make reactions happen that otherwise could not."** They only accelerate reactions that are already favourable; an unfavourable reaction needs coupling to Adenosine Triphosphate (ATP) hydrolysis, not a better catalyst.
- **"Km is the affinity of the enzyme for its substrate."** Only when the chemical step is much slower than substrate dissociation; in general Km is a kinetic constant, not a binding constant.
- **"A raised plasma enzyme measures how badly an organ is working."** It measures leakage from injured cells, which is a different thing from function: a cirrhotic liver with little tissue left can have near-normal transaminases.

## Go deeper

- Alan Fersht, *Structure and Mechanism in Protein Science* (1999): mechanism and kinetics from the physical chemist's side.
- Athel Cornish-Bowden, *Fundamentals of Enzyme Kinetics* (4th ed., 2012): why Km is not affinity.
- Nelson and Cox, *Lehninger Principles of Biochemistry* (8th ed., 2021), chapter 6: the standard treatment with the chymotrypsin and lysozyme examples.
