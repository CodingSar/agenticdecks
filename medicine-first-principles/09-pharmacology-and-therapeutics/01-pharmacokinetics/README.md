# Pharmacokinetics

> **Layer:** [09 Pharmacology and Therapeutics](../README.md) › Pharmacokinetics
> **Children:** [Absorption and bioavailability](absorption-and-bioavailability.md) · [Distribution and protein binding](distribution-and-protein-binding.md) · [Drug metabolism and interactions](drug-metabolism-and-interactions.md) · [Elimination, half-life and dosing](elimination-half-life-and-dosing.md)

## What this area is about

Pharmacokinetics asks what the body does to a drug: how much of a dose reaches the blood, where it goes, how it is changed and how it leaves, and therefore what concentration the target will see at any moment after any regimen. It is the quantitative half of pharmacology, and almost all of it is the physics of membranes and the physiology of two organs. The gut and the capillary wall are barriers governed by Fick's law and by ionisation; the liver is a bank of broad-specificity enzymes; the kidney is a filter with pumps. Put a drug's chemistry (size, lipid solubility, pKa, protein binding) in front of those four structures and its behaviour follows.

The unifying idea is the **compartment model**: the body treated as one or two well-stirred volumes with first-order exchange and loss. Three parameters, bioavailability (F), volume of distribution (Vd) and clearance (CL), summarise a drug's kinetics, and from them half-life, loading dose, maintenance dose, time to steady state and the effect of organ failure can all be calculated. Everything in this area either measures one of those parameters or explains why it changes between drugs, patients and days.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Absorption and bioavailability](absorption-and-bioavailability.md) | How much of the dose enters plasma, and how fast; the route and the first pass through the liver | Diffusion, acid–base chemistry, gut physiology |
| [Distribution and protein binding](distribution-and-protein-binding.md) | Where the drug goes once in plasma; Vd, free fraction, barriers and reservoirs | Fluid compartments, capillary exchange, compartment models |
| [Drug metabolism and interactions](drug-metabolism-and-interactions.md) | How the liver converts lipid-soluble drugs to excretable ones, and how drugs alter each other's fate | Enzyme kinetics, redox chemistry, the liver |
| [Elimination, half-life and dosing](elimination-half-life-and-dosing.md) | How clearance and Vd set half-life, and how all three parameters set a regimen | The three leaves above, renal physiology |

```
   dose --F--> plasma <--Vd--> tissues
                 |
            CL = hepatic (metabolism) + renal (filtration + secretion - reabsorption)
                 |
      t1/2 = 0.693 x Vd / CL      Css = F x dose rate / CL
```

Read them in order. Absorption delivers the drug and introduces first-pass loss, which already needs the idea of hepatic extraction. Distribution introduces the volume term and the free-drug principle. Metabolism is the larger half of clearance and the source of most interactions. The final leaf assembles F, Vd and CL into the exponential decay and the dosing equations, and adds the renal half of clearance. The last leaf is the one a clinician uses; the first three explain why its numbers are what they are.

## Connections to sibling areas

- **[Pharmacodynamics](../02-pharmacodynamics/README.md):** kinetics delivers a concentration–time profile; dynamics converts it into effect. The therapeutic index is only meaningful once one knows how much the concentration swings between doses, and tolerance can be kinetic (faster metabolism) or dynamic (receptor change). Pharmacogenomics sits across the boundary: variant enzymes alter kinetics, variant receptors alter dynamics.
- **[Drug classes by mechanism](../03-drug-classes-by-mechanism/README.md):** each class carries kinetic signatures that follow from its chemistry. Aminoglycosides are polar, so they do not cross the gut or the blood–brain barrier and are cleared by filtration; lipid-soluble anaesthetics redistribute; monoclonal antibodies are too large to filter and persist for weeks.
- **[Non-drug therapeutics](../04-non-drug-therapeutics/README.md):** fluids, nutrients and blood products are distributed by the same compartments; the volume of distribution of sodium is extracellular water, of glucose total body water, of albumin the plasma.
- **[Drug development and toxicology](../05-drug-development-and-toxicology/README.md):** phase I trials exist to measure F, Vd and CL in humans; toxicology is kinetics at doses where elimination saturates, and antidotes and extracorporeal removal are chosen from the same parameters.

## Connections across layers

From below, this area takes [diffusion and partition](../../00-physical-and-chemical-foundations/01-physics-of-the-body/diffusion-osmosis-and-transport.md) and [ionisation](../../00-physical-and-chemical-foundations/02-chemistry-of-life/acids-bases-and-buffers.md) from the physical foundations, [compartment models and exponential decay](../../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md) from the quantitative foundations, [enzyme kinetics](../../02-biochemistry-and-molecular-biology/01-macromolecules/enzymes-and-catalysis.md) from biochemistry, and the [liver](../../06-physiology/06-gastrointestinal-system/the-liver-as-metabolic-hub.md), [kidney](../../06-physiology/05-renal-system/glomerular-filtration-and-clearance.md) and [fluid compartments](../../06-physiology/01-integrative-principles/body-fluid-compartments-and-electrolytes.md) from physiology.

Upward, it supplies the dose adjustment that [nephrology](../../12-organ-system-specialties/03-nephrology/README.md) and [hepatology](../../12-organ-system-specialties/04-gastroenterology-and-hepatology/README.md) need, the time-course reasoning in [antimicrobial stewardship](../../12-organ-system-specialties/08-infectious-diseases/antimicrobial-stewardship.md), the route and offset reasoning of [anaesthesia](../../13-acute-perioperative-and-procedural-care/02-anaesthesia-and-perioperative-medicine/README.md) and [critical care](../../13-acute-perioperative-and-procedural-care/03-critical-care/README.md), the age-dependent kinetics that govern [paediatric](../../14-life-course-mind-and-integrative-care/01-paediatrics/README.md) and [geriatric](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/README.md) prescribing, and the drug-level interpretation in [laboratory medicine](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/clinical-chemistry-and-reference-ranges.md).

## Cross-cutting threads

- [Barriers and compartments](../../CROSS-CUTTING.md#barriers-and-compartments): the gut wall, the capillary, the blood–brain barrier and the placenta each select which drugs pass.
- [Gradients and flow](../../CROSS-CUTTING.md#gradients-and-flow): absorption and distribution are diffusion down concentration gradients; hepatic clearance of high-extraction drugs is limited by blood flow.
- [Time courses](../../CROSS-CUTTING.md#time-courses): half-life, time to steady state and the slow onset of enzyme induction are all exponential approaches to a new equilibrium.
- [Scale and surface to volume](../../CROSS-CUTTING.md#scale-and-surface-to-volume): clearance scales with body size roughly as mass to the power 0.75, which is why children are not small adults in dosing.
- [Dose–response](../../CROSS-CUTTING.md#dose-response): kinetics sets the concentration; the next area sets the response.
