# Drug metabolism and interactions

> **Layer:** [09 Pharmacology and Therapeutics](../README.md) › [Pharmacokinetics](README.md)
> **Builds on:** [Enzymes and catalysis](../../02-biochemistry-and-molecular-biology/01-macromolecules/enzymes-and-catalysis.md), [Redox and electron transfer](../../00-physical-and-chemical-foundations/02-chemistry-of-life/redox-and-electron-transfer.md), [Kinetics, equilibrium and catalysis](../../00-physical-and-chemical-foundations/02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md), [The liver as metabolic hub](../../06-physiology/06-gastrointestinal-system/the-liver-as-metabolic-hub.md), [Gene regulation and epigenetic mechanisms](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/gene-regulation-and-epigenetic-mechanisms.md)
> **Enables:** [Elimination, half-life and dosing](elimination-half-life-and-dosing.md), [Pharmacogenomics and individual variation](../02-pharmacodynamics/pharmacogenomics-and-individual-variation.md), [Toxicology and poisoning](../05-drug-development-and-toxicology/toxicology-and-poisoning.md), [Frailty, multimorbidity and polypharmacy](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md), [Liver disease](../../12-organ-system-specialties/04-gastroenterology-and-hepatology/liver-disease.md)

## Essence

The kidney excretes water-soluble molecules; most drugs are lipid-soluble, because that is what crosses membranes to reach a target, so left alone they would be reabsorbed from the tubule and persist for weeks. Metabolism solves this by making drugs more polar in two stages: phase I reactions (chiefly oxidation by cytochrome P450 enzymes) add or expose a functional group, and phase II reactions conjugate it to a water-soluble handle such as glucuronic acid. The single idea is that this machinery evolved to handle dietary toxins, not drugs, so it is broad, inducible, inhibitable and genetically variable, and almost every clinically important drug interaction is a consequence of one drug changing how fast an enzyme handles another.

## Core tenets

1. **Metabolism exists to convert lipid-soluble molecules into excretable ones.** A drug that crosses the gut wall and the blood–brain barrier will also cross the renal tubule back into blood after filtration. Adding a hydroxyl group and then a glucuronide or sulphate makes it ionised and water-soluble, so it stays in urine or is pumped into bile. Metabolism is therefore the gatekeeper of duration: a drug cleared only by metabolism has a half-life set by enzyme capacity, not by the kidney.

2. **Cytochrome P450 (CYP) enzymes are few, promiscuous and dominate phase I.** About a dozen CYP isoforms metabolise most drugs; CYP3A4 alone handles roughly half of them, with CYP2D6, CYP2C9, CYP2C19 and CYP1A2 covering most of the rest. Each has a broad active site that accepts many structures, which is why one inhibitor affects many drugs. The reaction is a monooxygenation: molecular oxygen is split, one atom going into the substrate, the other to water, using electrons from reduced nicotinamide adenine dinucleotide phosphate (NADPH).

3. **Inhibition raises exposure quickly; induction lowers it slowly.** An inhibitor competes for or inactivates the enzyme at once, so the victim drug's concentration rises over hours to days towards a new steady state. Clarithromycin, azole antifungals and grapefruit juice inhibit CYP3A4; combining them with a CYP3A4 substrate of narrow therapeutic index such as simvastatin or ciclosporin can produce toxicity. Induction requires synthesis of new enzyme via nuclear receptors (the pregnane X receptor, the constitutive androstane receptor), so rifampicin, carbamazepine or St John's wort take one to two weeks to lower levels, and levels rebound over a similar period after the inducer stops. The time course is the signature that distinguishes the two.

4. **Metabolism can activate as well as inactivate.** Prodrugs depend on it: clopidogrel is inert until CYP2C19 makes its active thiol, and codeine's analgesia comes largely from the morphine CYP2D6 produces. Some metabolites are toxic: paracetamol is safe while glucuronidation and sulphation cope, but at high doses a minor CYP2E1 pathway produces N-acetyl-p-benzoquinone imine (NAPQI), which depletes glutathione and kills hepatocytes, the mechanism that makes [paracetamol poisoning](../05-drug-development-and-toxicology/toxicology-and-poisoning.md) and its antidote intelligible. Active metabolites with long half-lives (diazepam's desmethyldiazepam) extend a drug's effect well beyond the parent's.

5. **Enzyme kinetics decide whether clearance is constant.** Most drugs are present at concentrations far below the enzyme's Michaelis constant (Km), so the rate is proportional to concentration: first-order kinetics, constant clearance and a fixed half-life. Phenytoin, ethanol and high-dose aspirin approach saturation, so a small dose increase produces a disproportionate rise in concentration and the half-life lengthens with dose. This is the [kinetics of catalysis](../../00-physical-and-chemical-foundations/02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md) applied to a patient.

6. **Hepatic clearance depends on blood flow for some drugs and enzyme capacity for others.** For a high-extraction drug (most of what enters the liver is removed in one pass), clearance approximates hepatic blood flow, ~1.5 L/min, and falls with heart failure or shock. For a low-extraction drug, clearance tracks enzyme activity and free fraction, so it is the one sensitive to inhibitors, inducers and genetic variants. The same disease therefore changes two drugs differently depending on which limit applies.

7. **Genetic variation in these enzymes makes populations of fast and slow metabolisers.** CYP2D6 ranges from absent (poor metabolisers, ~5–10% of Europeans) to duplicated (ultra-rapid); CYP2C19 and thiopurine methyltransferase show similar polymorphism. A poor metaboliser gets no analgesia from codeine and an ultra-rapid one can be poisoned by the morphine produced. This is developed in [pharmacogenomics](../02-pharmacodynamics/pharmacogenomics-and-individual-variation.md).

8. **Interactions also occur at transporters and at the kidney, not only at CYPs.** P-glycoprotein inhibition raises digoxin levels; organic anion transporter competition is why probenecid prolongs penicillin's half-life and why some drugs precipitate gout. Interactions multiply with the number of drugs, roughly as the number of pairs, which is why [polypharmacy](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md) is dangerous even when each drug is individually appropriate.

## Key concepts

| Term | Meaning |
|---|---|
| Phase I reaction | Oxidation, reduction or hydrolysis that introduces or exposes a functional group, mostly by CYP enzymes |
| Phase II reaction | Conjugation (glucuronidation, sulphation, acetylation, glutathione) that adds a polar handle for excretion |
| Cytochrome P450 (CYP) | Haem-containing monooxygenase family in liver and gut; named for its 450 nm absorption peak when reduced and bound to carbon monoxide |
| Enzyme induction | Increased synthesis of metabolising enzyme after exposure to an inducer; onset and offset over one to two weeks |
| Enzyme inhibition | Reduced activity by competition or inactivation; onset within hours |
| Hepatic extraction ratio | Fraction of drug removed in one pass through the liver; high-extraction drugs are flow-limited |
| First-order kinetics | Rate of elimination proportional to concentration; constant half-life |
| Zero-order (saturation) kinetics | Rate fixed by enzyme capacity; half-life rises with dose |
| Prodrug | Compound requiring metabolic activation |
| Poor and ultra-rapid metaboliser | Phenotypes produced by loss-of-function or duplicated alleles of a metabolising enzyme |

## How it fits

- **Below:** CYP chemistry is [redox](../../00-physical-and-chemical-foundations/02-chemistry-of-life/redox-and-electron-transfer.md) and [enzyme kinetics](../../02-biochemistry-and-molecular-biology/01-macromolecules/enzymes-and-catalysis.md); induction is [gene regulation](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/gene-regulation-and-epigenetic-mechanisms.md) through nuclear receptors; the organ is the [liver](../../06-physiology/06-gastrointestinal-system/the-liver-as-metabolic-hub.md). The assumption is that enzyme activity, not delivery, limits clearance for the drugs where interactions matter.
- **Above:** Metabolic clearance is the main term in [half-life and dosing](elimination-half-life-and-dosing.md); it decides which drugs need adjustment in [liver disease](../../12-organ-system-specialties/04-gastroenterology-and-hepatology/liver-disease.md), and it is the mechanism behind most interaction alerts in [health informatics](../../15-medicine-in-society/01-health-systems/health-informatics-and-artificial-intelligence.md).
- **Siblings:** First-pass metabolism links this leaf to [absorption](absorption-and-bioavailability.md); free fraction from [distribution](distribution-and-protein-binding.md) feeds the clearance of low-extraction drugs; renal excretion in [elimination](elimination-half-life-and-dosing.md) is the other exit route, and the two trade off: a drug cleared by both routes is buffered against failure of either.

## Common misconceptions

- **"Metabolism inactivates drugs."** It can activate prodrugs, create toxic intermediates, or produce active metabolites that outlast the parent.
- **"An inducer and an inhibitor act on the same timescale."** Inhibition acts within hours; induction and its offset take one to two weeks because enzyme must be synthesised or decay.
- **"Liver disease reduces the clearance of all drugs equally."** Cirrhosis spares glucuronidation relative to CYP oxidation and raises the bioavailability of high-extraction drugs through shunting; the effect is drug-specific.

## Go deeper

- Laurence Brunton, Björn Knollmann (eds), *Goodman & Gilman's The Pharmacological Basis of Therapeutics* (14th ed., 2023), chapter on drug metabolism: the enzyme families and their chemistry.
- Malcolm Rowland and Thomas Tozer, *Clinical Pharmacokinetics and Pharmacodynamics* (4th ed., 2011): hepatic clearance, extraction ratio and the well-stirred model.
- Ulrich Zanger and Matthias Schwab, "Cytochrome P450 enzymes in drug metabolism" (*Pharmacology & Therapeutics*, 2013): a review of isoform contributions and polymorphism.
