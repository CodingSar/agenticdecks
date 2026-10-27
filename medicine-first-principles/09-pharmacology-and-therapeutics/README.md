# 09 Pharmacology and Therapeutics

> **Layer:** 09 Pharmacology and Therapeutics
> **Children:** [Pharmacokinetics](01-pharmacokinetics/README.md) · [Pharmacodynamics](02-pharmacodynamics/README.md) · [Drug classes by mechanism](03-drug-classes-by-mechanism/README.md) · [Non-drug therapeutics](04-non-drug-therapeutics/README.md) · [Drug development and toxicology](05-drug-development-and-toxicology/README.md)

## What this area is about

This layer is about intervention: what medicine can do to a body once it knows how the body works (layers 02–07) and how it fails (layer 08). Most interventions are drugs, and a drug is a molecule that borrows a signal the body already uses, so pharmacology is physiology and pathology with the sign reversed. The layer asks two questions of every drug, where it goes (pharmacokinetics) and what it does there (pharmacodynamics), then organises the drugs themselves by the mechanism they share rather than the disease they treat, adds the therapies that are not drugs (surgery, radiation, devices, fluids, behaviour) because they are mechanisms too, and closes with how a drug is proven and what any substance does in excess.

The unifying idea is **dose–response**: a concentration at a target produces an effect that rises, saturates and, past a point, harms. Kinetics converts a dose into a concentration over time; receptor theory converts the concentration into an effect; the therapeutic index measures the distance between the effect wanted and the harm risked; and trials, pharmacovigilance and toxicology map the curve's two ends in populations. Nothing in the layer is a treatment recommendation. Drugs are named only as examples, by their International Nonproprietary Names, with no doses and no lists of what to give first; which treatment a patient should receive is decided by evidence ([10](../10-epidemiology-and-evidence/README.md)) and by the clinical encounter ([11](../11-clinical-method-and-diagnostics/README.md)), and described in the specialties ([12](../12-organ-system-specialties/README.md)–[14](../14-life-course-mind-and-integrative-care/README.md)).

## Why this layer sits here

From below, pharmacology needs almost everything. It takes diffusion, ionisation and radiation from the [physical and chemical foundations](../00-physical-and-chemical-foundations/README.md); compartment models, exponential decay and feedback from the [quantitative foundations](../01-quantitative-and-scientific-foundations/README.md); receptors, enzymes and metabolism from [biochemistry](../02-biochemistry-and-molecular-biology/README.md); the cell cycle and cell death from [cell biology](../03-cell-biology/README.md); variation and the evolution of resistance from [genetics and evolution](../04-genetics-evolution-and-development/README.md); the liver, kidney, autonomic nervous system, synapses, heart and endocrine axes from [physiology](../06-physiology/README.md); microbes and immunity from [microbiology and immunology](../07-microbiology-and-immunology/README.md); and inflammation, neoplasia, repair and toxic injury from [pathology](../08-pathology/README.md). It sits directly above pathology because a drug's rationale is a mechanism of disease to reverse, and its target is a protein that physiology has already described.

From above, every clinical layer uses it. [Epidemiology and evidence](../10-epidemiology-and-evidence/README.md) tests whether a mechanism translates into benefit; [clinical method](../11-clinical-method-and-diagnostics/README.md) interprets drug levels and chooses between treatments for one patient; the [specialties](../12-organ-system-specialties/README.md) cite a drug class by mechanism instead of restating it; [acute care](../13-acute-perioperative-and-procedural-care/README.md) runs kinetics and receptor theory at speed; the [life-course specialties](../14-life-course-mind-and-integrative-care/README.md) apply them to bodies whose kinetics differ; and [medicine in society](../15-medicine-in-society/README.md) pays for the drugs, regulates them and litigates their harms. The abstraction this layer contributes is the **therapeutic window**: a band of exposure between no effect and harm, defined by kinetics and dynamics together, within which every intervention must be kept.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Pharmacokinetics](01-pharmacokinetics/README.md) | What the body does to the drug: absorption, distribution, metabolism, elimination; the three parameters F, Vd and CL and the dosing equations they give | Diffusion, compartment models, the liver and kidney |
| [Pharmacodynamics](02-pharmacodynamics/README.md) | What the drug does to the body: receptor theory, dose–response, the therapeutic index, tolerance, adverse reactions, inherited variation | Receptors and ligands, distributions, feedback, immunity, genetics |
| [Drug classes by mechanism](03-drug-classes-by-mechanism/README.md) | The drugs themselves, grouped by the physiological system or pathological process they act on | Kinetics, dynamics, and the physiology, microbiology and pathology of each system |
| [Non-drug therapeutics](04-non-drug-therapeutics/README.md) | Surgery, radiotherapy, devices, fluids and blood, behaviour and placebo, written as mechanisms | Repair, radiation physics, materials, fluid compartments, reward circuits |
| [Drug development and toxicology](05-drug-development-and-toxicology/README.md) | How a target becomes a drug and what excess of any agent does | The four parents above, hypothesis testing, toxic injury |

```
           dose
             |  pharmacokinetics (01): F, Vd, CL  ->  concentration over time
             v
      concentration at target
             |  pharmacodynamics (02): occupancy, efficacy, therapeutic index
             v
          effect  <----  drug classes (03): which target, which system
             |
             |  non-drug therapeutics (04): the same questions asked of a scalpel, a beam, a litre
             v
   proof and excess: development and toxicology (05) map the curve's two ends
```

Read the two principles parents first, kinetics then dynamics; each leaf elsewhere assumes their vocabulary (half-life, steady state, agonist, antagonist, therapeutic index). Drug classes can then be read in any order, since each stands on its own physiology; biologics last, because it cuts across the others. Non-drug therapeutics applies the same questions to interventions that are not molecules, and development and toxicology close the layer by describing the pipeline every drug passed through and the far end of the curve that every agent has.

## Connections to neighbouring layers

- **[00 Physical and chemical foundations](../00-physical-and-chemical-foundations/README.md):** Fick's law and partition coefficients govern absorption and distribution; the Henderson–Hasselbalch relation decides ionisation and ion trapping; chemical equilibrium is receptor theory; ionising radiation is the physics of radiotherapy; materials science is the physics of implants.
- **[01 Quantitative and scientific foundations](../01-quantitative-and-scientific-foundations/README.md):** kinetics is a compartment model with exponential decay; the quantal dose–response curve is a cumulative distribution; tolerance and endocrine drugs are feedback with the drug inside the loop; development is sequential hypothesis testing; the placebo arm is regression to the mean made visible.
- **[02 Biochemistry and molecular biology](../02-biochemistry-and-molecular-biology/README.md):** receptors, second messengers and signal termination are the targets and the mechanisms of tolerance; cytochrome P450 is enzyme kinetics; DNA repair is what cytotoxics and radiation overwhelm; recombinant proteins and antibodies are molecular techniques made therapeutic.
- **[06 Physiology](../06-physiology/README.md):** the liver and kidney clear drugs; the autonomic, cardiovascular, nervous, endocrine, renal and haemostatic systems supply the targets of the drug classes; fluid compartments distribute fluids and blood.
- **[07 Microbiology and immunology](../07-microbiology-and-immunology/README.md):** the structures of microbes are the targets of antimicrobials; hypersensitivity is the mechanism of type B adverse reactions; cytokines and T-cells are what immunomodulators block and checkpoint inhibitors release; antibodies are the template for biologics.
- **[08 Pathology](../08-pathology/README.md):** inflammation, neoplasia, thrombosis and repair are the processes the drug classes reverse and surgery relies on; toxic injury is toxicology's cellular end; oedema is the toxicity of fluid.
- **[10 Epidemiology and evidence](../10-epidemiology-and-evidence/README.md):** randomised trials decide whether a mechanism becomes a benefit; the number needed to treat and to harm quantifies the therapeutic index in populations; observational studies confirm pharmacovigilance signals.
- **[12](../12-organ-system-specialties/README.md), [13](../13-acute-perioperative-and-procedural-care/README.md) and [14](../14-life-course-mind-and-integrative-care/README.md), the specialties:** every disease leaf cites a drug class here for what its treatment reverses; critical care, anaesthesia and emergency medicine run kinetics and antidotes in real time; paediatrics and geriatrics apply the same equations to bodies with different volumes and clearances, and polypharmacy in the elderly is where interactions and adverse reactions concentrate.

## Cross-cutting threads

- [Dose–response](../CROSS-CUTTING.md#dose-response): the layer's organising principle, from receptor occupancy to the median lethal dose.
- [Barriers and compartments](../CROSS-CUTTING.md#barriers-and-compartments): the gut wall, blood–brain barrier and placenta select what a drug reaches; fluids fill the compartment they match.
- [Feedback and homeostasis](../CROSS-CUTTING.md#feedback-and-homeostasis): the body replies to every drug, as reflex tachycardia, rising TSH, tolerance, rebound and withdrawal.
- [Specificity and recognition](../CROSS-CUTTING.md#specificity-and-recognition): affinity, selectivity between receptor subtypes and between pathogen and host, and the perfect specificity of an antibody.
- [Time courses](../CROSS-CUTTING.md#time-courses): half-life, steady state, the weeks of enzyme induction and antidepressant onset, the years of late radiation effects.
- [Trade-offs and evolutionary legacy](../CROSS-CUTTING.md#trade-offs-and-evolutionary-legacy): resistance in microbes and tumours is evolution driven by treatment.
- [Harm and benefit](../CROSS-CUTTING.md#harm-and-benefit): the therapeutic index, adverse reactions, the restrictive thresholds for transfusion and the benefit–harm judgement of approval.
- [Probability and uncertainty](../CROSS-CUTTING.md#probability-and-uncertainty): the quantal curve is a distribution; the rule of three bounds what trials can see; a genotype refines a prior.
