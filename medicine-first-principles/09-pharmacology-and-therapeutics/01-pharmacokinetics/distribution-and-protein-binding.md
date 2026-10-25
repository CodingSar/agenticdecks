# Distribution and protein binding

> **Layer:** [09 Pharmacology and Therapeutics](../README.md) › [Pharmacokinetics](README.md)
> **Builds on:** [Compartment models and exponential processes](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md), [Body fluid compartments and electrolytes](../../06-physiology/01-integrative-principles/body-fluid-compartments-and-electrolytes.md), [Microcirculation and capillary exchange](../../06-physiology/03-cardiovascular-system/microcirculation-and-capillary-exchange.md), [Lipids and membranes](../../02-biochemistry-and-molecular-biology/01-macromolecules/lipids-and-membranes.md), [Absorption and bioavailability](absorption-and-bioavailability.md)
> **Enables:** [Elimination, half-life and dosing](elimination-half-life-and-dosing.md), [Central nervous system drugs](../03-drug-classes-by-mechanism/central-nervous-system-drugs.md), [General and regional anaesthesia](../../13-acute-perioperative-and-procedural-care/02-anaesthesia-and-perioperative-medicine/general-and-regional-anaesthesia.md), [Pregnancy and its complications](../../14-life-course-mind-and-integrative-care/02-obstetrics-and-gynaecology/pregnancy-and-its-complications.md)

## Essence

Once in plasma, a drug spreads into whatever tissues its chemistry allows and sits wherever it binds. Distribution answers the question "for a given amount in the body, what concentration will I measure in plasma?", and the answer is a single number, the apparent volume of distribution (Vd), which is not an anatomical space but the ratio of amount to concentration. A drug confined to plasma has a Vd near 3 L; one that hides in fat or binds avidly to tissue may have a Vd of hundreds of litres, far exceeding body volume. The single idea is that plasma is a window on a much larger and unevenly loaded system, and the size of that system decides loading doses, the speed of onset and how long a drug lingers after it stops being given.

## Core tenets

1. **Volume of distribution is a proportionality constant, not a space.** Vd = amount of drug in the body ÷ plasma concentration. Heparin (large, polar) stays in plasma, Vd ~ 3–5 L; gentamicin spreads into extracellular water, ~15 L; digoxin binds to skeletal and cardiac muscle, ~500 L; chloroquine sequesters in tissue, over 10,000 L. Because a loading dose = target concentration × Vd, the number is the direct route to how much drug to give to fill the body at once.

2. **Distribution follows perfusion first and partition second.** In the minutes after an intravenous dose, drug reaches organs in proportion to their blood flow: brain, heart, liver and kidney take most of the cardiac output and equilibrate fast, while muscle and fat fill slowly. A lipid-soluble anaesthetic such as propofol therefore acts within a minute and wears off as it redistributes from brain to muscle and fat, long before it is metabolised. The resulting multiphasic curve is what [compartment models](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md) describe with a distribution phase and an elimination phase.

3. **Only free drug crosses membranes and acts.** Albumin binds acidic drugs (warfarin, phenytoin) and alpha-1 acid glycoprotein binds basic drugs; binding is reversible and fast. The bound fraction is a reservoir, not an active pool. Total plasma concentration, which is what most laboratory assays report, therefore overstates activity when albumin is low or when another drug competes for the same sites, as in [cirrhosis](../../12-organ-system-specialties/04-gastroenterology-and-hepatology/liver-disease.md) or [nephrotic syndrome](../../12-organ-system-specialties/03-nephrology/glomerular-and-tubular-diseases.md).

4. **Displacement from protein matters less than it seems, because free drug is cleared faster too.** When one drug displaces another, the free concentration rises transiently, but the extra free drug distributes into tissue and is cleared, and a new steady state with nearly the same free concentration follows. Clinically important displacement interactions are rare and mostly involve drugs with both high protein binding and a narrow therapeutic range, where the transient alone is dangerous.

5. **Barriers with tight junctions and efflux pumps make some compartments hard to enter.** Most capillaries are leaky to small molecules, so interstitial fluid tracks plasma. The brain's capillaries have tight junctions and express P-glycoprotein, so only lipid-soluble, un-ionised, non-substrate molecules enter freely; this is why loperamide, an opioid, acts on the gut and not the brain, and why quaternary ammonium anticholinergics do not cause confusion. The placenta is permeable to most drugs and protective to few, which governs [teratogenesis](../../04-genetics-evolution-and-development/03-development/congenital-malformations-and-teratogens.md). Inflamed meninges become leakier, which antibiotics for meningitis rely on.

6. **Body composition changes Vd and therefore dosing.** Neonates are ~75–80% water with little fat, so water-soluble drugs need larger weight-based doses; the elderly have more fat and less water and muscle, so lipid-soluble benzodiazepines accumulate and act longer. Pregnancy expands plasma volume and total body water by roughly 40–50%, which dilutes many drugs. Oedema and ascites expand the extracellular space into which polar drugs distribute. These are the mechanisms behind age-related dosing in [paediatrics](../../14-life-course-mind-and-integrative-care/01-paediatrics/growth-development-and-the-child-as-patient.md) and [geriatrics](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md).

7. **Tissue binding creates reservoirs that outlast plasma.** Drugs that dissolve in fat (amiodarone), bind to melanin (chloroquine in the retina) or incorporate into bone (tetracyclines, bisphosphonates) leave plasma quickly but leave the body slowly; the apparent half-life lengthens as these reservoirs refill plasma. A large Vd combined with slow release is why some drug effects and toxicities persist for weeks or months after the last dose.

## Key concepts

| Term | Meaning |
|---|---|
| Volume of distribution (Vd) | Amount of drug in body divided by plasma concentration; the volume plasma would have to be to hold all the drug at that concentration |
| Loading dose | Dose needed to reach a target concentration at once: target × Vd ÷ bioavailability |
| Redistribution | Movement of drug from highly perfused tissue to slowly perfused tissue, ending an effect without eliminating the drug |
| Free fraction | Proportion of plasma drug not bound to protein; the pharmacologically active share |
| Albumin and alpha-1 acid glycoprotein | Main plasma binding proteins for acidic and basic drugs respectively |
| Blood–brain barrier | Capillary endothelium with tight junctions and efflux pumps that limits entry of polar and transported molecules into the central nervous system |
| Partition coefficient | Ratio of a drug's solubility in lipid to its solubility in water; predicts membrane crossing and fat storage |
| Two-compartment model | Plasma plus a peripheral compartment that fills and empties at a finite rate, producing a biphasic concentration curve |

## How it fits

- **Below:** The maths is a [compartment model](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md); the anatomy of the compartments is in [body fluid compartments](../../06-physiology/01-integrative-principles/body-fluid-compartments-and-electrolytes.md); the capillary leak rules are those of [capillary exchange](../../06-physiology/03-cardiovascular-system/microcirculation-and-capillary-exchange.md). The assumption is that free drug equilibrates rapidly between plasma and the tissues it can enter.
- **Above:** Vd fixes the loading dose and, with clearance, the half-life in [elimination and dosing](elimination-half-life-and-dosing.md). Redistribution underlies the offset of intravenous [anaesthetics](../../13-acute-perioperative-and-procedural-care/02-anaesthesia-and-perioperative-medicine/general-and-regional-anaesthesia.md); barrier penetration decides which [antimicrobials](../03-drug-classes-by-mechanism/antimicrobials.md) treat meningitis and which [central nervous system drugs](../03-drug-classes-by-mechanism/central-nervous-system-drugs.md) work at all.
- **Siblings:** [Absorption](absorption-and-bioavailability.md) fixes how much enters; distribution fixes where it is; [metabolism](drug-metabolism-and-interactions.md) and [elimination](elimination-half-life-and-dosing.md) fix how fast it leaves. Vd and clearance together, not either alone, set half-life.

## Common misconceptions

- **"A volume of distribution larger than the body is a measurement error."** It is the expected result for a drug concentrated in tissue; the number reports where the drug is relative to plasma, not a real volume.
- **"High protein binding makes a drug dangerous to combine with others."** Displacement raises free concentration only briefly; the body re-equilibrates by clearing the extra free drug. Danger arises mainly when metabolism is inhibited at the same time.
- **"The drug stops working because it has been eliminated."** For a single intravenous dose of a lipid-soluble agent, offset is usually redistribution; the drug is still in the body and repeated doses accumulate.

## Go deeper

- Malcolm Rowland and Thomas Tozer, *Clinical Pharmacokinetics and Pharmacodynamics* (4th ed., 2011): distribution, volumes and the free-drug hypothesis in full.
- Leslie Benet and Betty-ann Hoener, "Changes in plasma protein binding have little clinical relevance" (*Clinical Pharmacology & Therapeutics*, 2002): the argument of tenet 4.
- Laurence Brunton, Björn Knollmann (eds), *Goodman & Gilman's The Pharmacological Basis of Therapeutics* (14th ed., 2023): the blood–brain and placental barriers in context.
