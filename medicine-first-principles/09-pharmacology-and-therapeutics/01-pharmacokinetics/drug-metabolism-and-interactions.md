# Drug metabolism and interactions

> **Layer:** [09 Pharmacology and Therapeutics](../README.md) › [Pharmacokinetics](README.md)
> **Builds on:** [Enzymes and catalysis](../../02-biochemistry-and-molecular-biology/01-macromolecules/enzymes-and-catalysis.md), [Redox and electron transfer](../../00-physical-and-chemical-foundations/02-chemistry-of-life/redox-and-electron-transfer.md), [Kinetics, equilibrium and catalysis](../../00-physical-and-chemical-foundations/02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md), [The liver as metabolic hub](../../06-physiology/06-gastrointestinal-system/the-liver-as-metabolic-hub.md), [Gene regulation and epigenetic mechanisms](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/gene-regulation-and-epigenetic-mechanisms.md)
> **Enables:** [Elimination, half-life and dosing](elimination-half-life-and-dosing.md), [Pharmacogenomics and individual variation](../02-pharmacodynamics/pharmacogenomics-and-individual-variation.md), [Toxicology and poisoning](../05-drug-development-and-toxicology/toxicology-and-poisoning.md), [Frailty, multimorbidity and polypharmacy](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md), [Liver disease](../../12-organ-system-specialties/04-gastroenterology-and-hepatology/liver-disease.md)

## Essence

The kidney excretes water-soluble molecules; most drugs are lipid-soluble, because that is what crosses membranes, so left alone they would be reabsorbed from the tubule and persist for weeks. Metabolism makes drugs more polar in two stages: phase I reactions (chiefly oxidation by cytochrome P450 enzymes) add or expose a functional group, and phase II reactions conjugate it to a water-soluble handle such as glucuronic acid. The single idea is that this machinery evolved for dietary toxins, not drugs, so it is broad, inducible, inhibitable and genetically variable, and almost every important drug interaction is one drug changing how fast an enzyme handles another.

## Core tenets

1. **Metabolism exists to convert lipid-soluble molecules into excretable ones.** A drug that crosses the gut wall will also cross the renal tubule back into blood after filtration. Adding a hydroxyl group and then a glucuronide or sulphate makes it ionised and water-soluble, so it stays in urine or is pumped into bile. A drug cleared only by metabolism therefore has a half-life set by enzyme capacity, not by the kidney.

2. **Cytochrome P450 (CYP) enzymes are few, promiscuous and dominate phase I.** About a dozen CYP isoforms metabolise most drugs; CYP3A4 alone handles roughly half, with CYP2D6, CYP2C9, CYP2C19 and CYP1A2 covering most of the rest. Each has a broad active site, which is why one inhibitor affects many drugs. The reaction is a monooxygenation: oxygen is split, one atom going into the substrate and the other to water, using electrons from reduced nicotinamide adenine dinucleotide phosphate (NADPH).

3. **Inhibition raises exposure quickly; induction lowers it slowly.** An inhibitor competes for or inactivates the enzyme at once, so the victim drug's concentration rises over hours to days towards a new steady state: clarithromycin, azole antifungals and grapefruit juice inhibit CYP3A4, and a narrow-index substrate such as simvastatin or ciclosporin can reach toxicity. Induction requires synthesis of new enzyme via nuclear receptors (the pregnane X receptor, the constitutive androstane receptor), so rifampicin, carbamazepine or St John's wort take one to two weeks to lower levels, which rebound over a similar period after the inducer stops.

4. **Metabolism can activate as well as inactivate.** Prodrugs depend on it: clopidogrel is inert until CYP2C19 makes its active thiol, and codeine's analgesia comes largely from the morphine CYP2D6 produces. Some metabolites are toxic: paracetamol is safe while glucuronidation and sulphation cope, but at high doses a minor CYP2E1 pathway produces N-acetyl-p-benzoquinone imine (NAPQI), which depletes glutathione and kills hepatocytes, the mechanism behind [paracetamol poisoning](../05-drug-development-and-toxicology/toxicology-and-poisoning.md) and its antidote. Long-lived active metabolites (diazepam's desmethyldiazepam) extend a drug's effect beyond the parent's.

5. **Enzyme kinetics decide whether clearance is constant.** Most drugs are present far below the enzyme's Michaelis constant (Km), so the rate is proportional to concentration: first-order kinetics, constant clearance, fixed half-life. Phenytoin, ethanol and high-dose aspirin approach saturation, so a small dose increase produces a disproportionate rise in concentration and the half-life lengthens with dose: the [kinetics of catalysis](../../00-physical-and-chemical-foundations/02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md) applied to a patient.

6. **Hepatic clearance depends on blood flow for some drugs and enzyme capacity for others.** For a high-extraction drug (most of what enters the liver is removed in one pass), clearance approximates hepatic blood flow, ~1.5 L/min, and falls with heart failure or shock. For a low-extraction drug, clearance tracks enzyme activity and free fraction, so it is the one sensitive to inhibitors, inducers and genetic variants.

7. **Genetic variation in these enzymes makes populations of fast and slow metabolisers.** CYP2D6 ranges from absent (poor metabolisers, ~5–10% of Europeans) to duplicated (ultra-rapid); CYP2C19 and thiopurine methyltransferase show similar polymorphism. A poor metaboliser gets no analgesia from codeine and an ultra-rapid one can be poisoned by the morphine produced ([pharmacogenomics](../02-pharmacodynamics/pharmacogenomics-and-individual-variation.md)).

8. **Interactions also occur at transporters and at the kidney, not only at CYPs.** P-glycoprotein inhibition raises digoxin levels; organic anion transporter competition is why probenecid prolongs penicillin's half-life. Interactions multiply roughly as the number of drug pairs, which is why [polypharmacy](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md) is dangerous even when each drug is individually appropriate; enzyme maturation and decline across life are in [pharmacokinetics across the life course](pharmacokinetics-across-the-life-course.md).

## Key concepts

| Term | Meaning |
|---|---|
| Phase I reaction | Oxidation, reduction or hydrolysis that introduces or exposes a functional group, mostly by CYP enzymes |
| Phase II reaction | Conjugation (glucuronidation, sulphation, acetylation, glutathione) that adds a polar handle for excretion |
| Cytochrome P450 (CYP) | Haem-containing monooxygenase family in liver and gut, named for its 450 nm absorption peak |
| Induction and inhibition | Increased enzyme synthesis (onset and offset over one to two weeks) versus reduced activity by competition or inactivation (onset within hours) |
| Hepatic extraction ratio | Fraction of drug removed in one pass through the liver; high-extraction drugs are flow-limited |
| First-order versus zero-order kinetics | Elimination proportional to concentration (constant half-life) versus fixed by enzyme capacity (half-life rises with dose) |
| Poor and ultra-rapid metaboliser | Phenotypes produced by loss-of-function or duplicated alleles of a metabolising enzyme |

## How it fits

- **Below:** CYP chemistry is [redox](../../00-physical-and-chemical-foundations/02-chemistry-of-life/redox-and-electron-transfer.md) and [enzyme kinetics](../../02-biochemistry-and-molecular-biology/01-macromolecules/enzymes-and-catalysis.md); induction is [gene regulation](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/gene-regulation-and-epigenetic-mechanisms.md) through nuclear receptors; the organ is the [liver](../../06-physiology/06-gastrointestinal-system/the-liver-as-metabolic-hub.md). The assumption is that enzyme activity, not delivery, limits clearance for the drugs where interactions matter.
- **Above:** Metabolic clearance is the main term in [half-life and dosing](elimination-half-life-and-dosing.md); it decides which drugs need adjustment in [liver disease](../../12-organ-system-specialties/04-gastroenterology-and-hepatology/liver-disease.md) and is the mechanism behind most interaction alerts.
- **Siblings:** First-pass metabolism links this leaf to [absorption](absorption-and-bioavailability.md); free fraction from [distribution](distribution-and-protein-binding.md) feeds the clearance of low-extraction drugs; renal excretion in [elimination](elimination-half-life-and-dosing.md) is the other exit route, and the two trade off: a drug cleared by both routes is buffered against failure of either.

## Common misconceptions

- **"Metabolism inactivates drugs."** It can activate prodrugs, create toxic intermediates, or produce active metabolites that outlast the parent.
- **"An inducer and an inhibitor act on the same timescale."** Inhibition acts within hours; induction and its offset take one to two weeks.
- **"Liver disease reduces the clearance of all drugs equally."** Cirrhosis spares glucuronidation relative to CYP oxidation and raises the bioavailability of high-extraction drugs through shunting.

## Go deeper

- Laurence Brunton, Björn Knollmann (eds), *Goodman & Gilman's The Pharmacological Basis of Therapeutics* (14th ed., 2023): the enzyme families and their chemistry.
- Malcolm Rowland and Thomas Tozer, *Clinical Pharmacokinetics and Pharmacodynamics* (4th ed., 2011): hepatic clearance, extraction ratio and the well-stirred model.
- Ulrich Zanger and Matthias Schwab, "Cytochrome P450 enzymes in drug metabolism" (*Pharmacology & Therapeutics*, 2013): a review of isoform contributions and polymorphism.
