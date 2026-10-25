# Absorption and bioavailability

> **Layer:** [09 Pharmacology and Therapeutics](../README.md) › [Pharmacokinetics](README.md)
> **Builds on:** [Diffusion, osmosis and transport](../../00-physical-and-chemical-foundations/01-physics-of-the-body/diffusion-osmosis-and-transport.md), [Acids, bases and buffers](../../00-physical-and-chemical-foundations/02-chemistry-of-life/acids-bases-and-buffers.md), [Membrane transport and ion gradients](../../02-biochemistry-and-molecular-biology/04-cell-signalling/membrane-transport-and-ion-gradients.md), [Secretion, digestion and absorption](../../06-physiology/06-gastrointestinal-system/secretion-digestion-and-absorption.md), [The liver as metabolic hub](../../06-physiology/06-gastrointestinal-system/the-liver-as-metabolic-hub.md)
> **Enables:** [Elimination, half-life and dosing](elimination-half-life-and-dosing.md), [Drug metabolism and interactions](drug-metabolism-and-interactions.md), [Toxicology and poisoning](../05-drug-development-and-toxicology/toxicology-and-poisoning.md), [Poisoning and overdose](../../13-acute-perioperative-and-procedural-care/04-emergency-medicine/poisoning-and-overdose.md), [Frailty, multimorbidity and polypharmacy](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md)

## Essence

A drug acts only where it is, and most drugs are given somewhere other than their target. Absorption is the movement of a drug from its site of administration into the bloodstream; bioavailability (F) is the fraction of the given dose that arrives there unchanged. Both are governed by a small set of physical facts: a molecule crosses a lipid membrane in proportion to its concentration gradient, its lipid solubility and the area available, and it survives the journey only if the gut wall and the liver let it pass. The single idea is that the route of administration chooses which barriers a drug must cross, and every barrier takes a toll that is predictable from the drug's chemistry.

## Core tenets

1. **Crossing a membrane is passive diffusion unless a transporter intervenes.** Fick's law says flux is proportional to surface area times the concentration gradient divided by membrane thickness, scaled by a permeability that rises with lipid solubility. The small intestine has ~30 m² of villous surface and a thin epithelium, so it absorbs most oral drugs; the stomach, despite being first, absorbs little. Carrier-mediated uptake (for example of levodopa by the large neutral amino acid transporter) and efflux pumps such as P-glycoprotein, which throws absorbed drug back into the lumen, modify the passive picture for specific molecules.

2. **Only the un-ionised fraction crosses easily, and pH sets that fraction.** Most drugs are weak acids or bases. The Henderson–Hasselbalch relation fixes the ratio of ionised to un-ionised forms from the pKa and the local pH; the un-ionised form is lipid soluble and crosses, the ionised form is trapped in water. A weak acid such as aspirin (pKa ~3.5) is largely un-ionised in gastric acid, yet the vast surface of the intestine still dominates its absorption. The same rule explains ion trapping: a weak base concentrates in acidic compartments (stomach, urine made acidic), which [toxicology](../05-drug-development-and-toxicology/toxicology-and-poisoning.md) exploits to hasten elimination.

3. **Oral drugs face first-pass metabolism before they reach the systemic circulation.** Blood from the gut drains through the portal vein into the liver, and the gut wall itself carries metabolising enzymes. A drug with high hepatic extraction may lose most of each oral dose before it reaches the heart. Glyceryl trinitrate is nearly fully destroyed on first pass, which is why it is given sublingually or transdermally, routes that drain into systemic veins. Bioavailability is therefore F = (fraction absorbed) × (fraction escaping gut-wall metabolism) × (fraction escaping hepatic metabolism).

4. **Bioavailability is measured as area under the curve, not peak concentration.** F is the ratio of the area under the plasma concentration–time curve (AUC) after the test route to the AUC after intravenous injection of the same dose, because AUC integrates everything that reached the plasma regardless of timing. Two formulations with the same F but different absorption rates give different peaks and troughs; regulators call them bioequivalent only when both AUC and peak fall within set limits (conventionally 80–125% of the reference).

5. **Rate of absorption shapes the concentration profile as much as extent.** Intravenous injection puts all the drug in plasma at time zero; intramuscular and subcutaneous routes release it from a depot at a rate fixed by local blood flow and formulation; modified-release oral forms deliberately slow dissolution so that absorption, not elimination, limits the plasma level. When absorption is slower than elimination, the terminal slope of the curve reflects absorption ("flip-flop" kinetics), and the drug appears to have a longer half-life than it has.

6. **Physiology varies the barriers, so bioavailability is a property of the drug in a patient, not of the drug alone.** Gastric emptying sets when an oral drug reaches the intestine; food, opioids and diabetic gastroparesis delay it. Gut blood flow falls in shock, so oral and intramuscular absorption become unreliable in the critically ill, which is one reason [critical care](../../13-acute-perioperative-and-procedural-care/03-critical-care/shock-and-haemodynamic-support.md) uses intravenous routes. Portosystemic shunting in [cirrhosis](../../12-organ-system-specialties/04-gastroenterology-and-hepatology/liver-disease.md) bypasses first-pass metabolism and can raise the bioavailability of high-extraction drugs several-fold.

7. **Formulation is part of the drug.** Dissolution precedes absorption, and particle size, salt form, coating and excipients determine its speed. Enteric coatings resist acid and dissolve at intestinal pH; prodrugs (an ester that an esterase hydrolyses to the active acid) are designed to cross a barrier that the active molecule cannot. Changing manufacturer can change exposure for drugs with narrow therapeutic windows, which is why bioequivalence testing exists.

## Key concepts

| Term | Meaning |
|---|---|
| Bioavailability (F) | Fraction of an administered dose reaching the systemic circulation unchanged; 1 by definition for intravenous dosing |
| First-pass metabolism | Loss of drug in gut wall and liver between absorption and systemic circulation |
| Area under the curve (AUC) | Integral of plasma concentration over time; proportional to the amount that reached plasma divided by clearance |
| pKa | pH at which a weak acid or base is half ionised |
| Ion trapping | Accumulation of a weak acid or base in a compartment whose pH favours its ionised form |
| P-glycoprotein | An ATP-binding cassette efflux pump in gut, liver, kidney and blood–brain barrier that exports many drugs |
| Bioequivalence | Two formulations whose AUC and peak concentration fall within accepted limits of each other |
| Flip-flop kinetics | Profile in which absorption is slower than elimination, so the terminal decline reflects absorption |
| Prodrug | Inactive compound converted in the body to the active drug, often to improve absorption |

## How it fits

- **Below:** Fick's law and partition coefficients come from [diffusion and transport](../../00-physical-and-chemical-foundations/01-physics-of-the-body/diffusion-osmosis-and-transport.md); the ionisation rule from [acids and bases](../../00-physical-and-chemical-foundations/02-chemistry-of-life/acids-bases-and-buffers.md); the gut's surface, motility and portal drainage from [gastrointestinal physiology](../../06-physiology/06-gastrointestinal-system/secretion-digestion-and-absorption.md). The assumption throughout is that the epithelium behaves as a lipid barrier with a few specific transporters.
- **Above:** F enters every dosing calculation in [elimination and dosing](elimination-half-life-and-dosing.md); route selection is a recurring decision in [anaesthesia](../../13-acute-perioperative-and-procedural-care/02-anaesthesia-and-perioperative-medicine/general-and-regional-anaesthesia.md), [palliative care](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/palliative-care-and-symptom-control.md) and poisoning.
- **Siblings:** Absorption gets the drug into plasma; [distribution](distribution-and-protein-binding.md) decides where it goes next; [metabolism](drug-metabolism-and-interactions.md) and [elimination](elimination-half-life-and-dosing.md) remove it. First-pass metabolism is the point where absorption and metabolism overlap.

## Common misconceptions

- **"Acidic drugs are absorbed in the stomach because they are un-ionised there."** The stomach's small surface area and thick mucus mean that even favourably ionised drugs are mostly absorbed in the intestine once gastric emptying delivers them.
- **"A faster-acting formulation has higher bioavailability."** Speed and extent are independent; an immediate-release and a modified-release tablet can have identical F with very different peaks.
- **"Intramuscular injection is reliable in every patient."** Absorption from muscle depends on local perfusion, which collapses in shock and is poor in the cold or oedematous limb.

## Go deeper

- Laurence Brunton, Björn Knollmann (eds), *Goodman & Gilman's The Pharmacological Basis of Therapeutics* (14th ed., 2023), chapter on pharmacokinetics: the standard account of absorption and bioavailability.
- Malcolm Rowland and Thomas Tozer, *Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications* (4th ed., 2011): the quantitative treatment, with worked examples of first-pass loss.
- Leslie Benet and colleagues, "BDDCS applied to over 900 drugs" (*AAPS Journal*, 2011): how solubility and metabolism together predict a drug's absorption behaviour.
