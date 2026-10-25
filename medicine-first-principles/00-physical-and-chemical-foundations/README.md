# 00 Physical and Chemical Foundations

> **Layer:** 00 Physical and Chemical Foundations (material root of the tree)
> **Children:** [Physics of the Body](01-physics-of-the-body/README.md) · [Chemistry of Life](02-chemistry-of-life/README.md)

## What this area is about

A patient is a physical object. Blood is a fluid obeying Poiseuille's law; a nerve is a leaky cable; the lung is a diffusion membrane with 70 m² of surface; plasma is a buffered salt solution at pH 7.4; every calorie eaten ends as heat or fat; every drug is a shape that fits, or nearly fits, a protein's surface. This layer answers the question: *what does the physical and chemical world impose on a living body that no amount of biology can escape, and what does it therefore predict about how the body is built, how it fails and how it can be examined?*

The layer has two children. [Physics of the body](01-physics-of-the-body/README.md) covers energy, pressure and flow, diffusion and osmosis, bioelectricity, mechanics, waves and radiation, and the consequences of size. [Chemistry of life](02-chemistry-of-life/README.md) covers bonds and shape, water and concentration, acids and buffers, redox, kinetics and catalysis, and molecular recognition. They are not two separate roots: physics supplies the forces and chemistry the molecules they act on, and most medical ideas use both at once (osmosis is diffusion of a chemical solvent; the mitochondrion is a redox chain driving an electrical gradient).

The one idea this layer contributes to the whole stack is **the gradient and its cost**: everything in the body moves down a gradient of pressure, concentration, voltage, temperature or chemical potential, that flow does the body's work, and the body must spend free energy from food to rebuild every gradient it spends. Every later layer restates this in its own terms, as oxygen delivery, as membrane potential, as the sodium pump, as blood pressure, as shock.

## Why this layer sits here

This is the **bottom layer**: the material root of the knowledge base. It depends on no other layer's results. Thermodynamics, fluid mechanics and chemical bonding would be true if no physician had ever lived.

It sits beside, not above, [01 Quantitative and Scientific Foundations](../01-quantitative-and-scientific-foundations/README.md), the **formal root**. Physics is written in mathematics, so leaves here cite 01 for their language: entropy is [probability](../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md) over molecular arrangements; radioactive decay, drug elimination and the decay of a signal along a nerve are [exponential processes](../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md); allometric scaling is a [regression](../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md) on a log–log plot; a laboratory concentration is a [measurement with error](../01-quantitative-and-scientific-foundations/01-probability-and-measurement/measurement-error-and-biological-variation.md); molecular recognition is a [signal read against noise](../01-quantitative-and-scientific-foundations/03-systems-and-models/information-signals-and-noise.md). This is the single upward link the tree permits, and it runs one way: 01 never cites 00.

The two roots grow separately for one layer and meet at the cell. [02 Biochemistry](../02-biochemistry-and-molecular-biology/README.md) is this layer's chemistry organised into the body's own molecules, and [03 Cell Biology](../03-cell-biology/README.md) is where gradients (physics), enzymes (chemistry) and genes and signals (information, from 01) first combine into a living unit. From [04](../04-genetics-evolution-and-development/README.md) upward every layer stands on both roots.

```
   01 Quantitative and Scientific Foundations ─────┐   (formal root)
                                                   ├──► 02 Biochemistry ──► 03 Cell Biology ──► ...
   00 Physical and Chemical Foundations ───────────┘   (material root: this layer)
          ▲ cites 01 for its language
```

What the layers above need from this one: an energy budget and the rule of coupling ([energy and thermodynamics](01-physics-of-the-body/energy-and-thermodynamics.md)); the flow laws of tubes and walls ([fluids](01-physics-of-the-body/fluids-pressure-and-flow.md), [diffusion and osmosis](01-physics-of-the-body/diffusion-osmosis-and-transport.md)); ionic gradients as batteries ([electricity and excitable membranes](01-physics-of-the-body/electricity-and-excitable-membranes.md)); the physics of every imaging method and sense organ ([waves, sound, light and radiation](01-physics-of-the-body/waves-sound-light-and-radiation.md)); the materials of the skeleton and vessel wall ([mechanics and materials](01-physics-of-the-body/mechanics-and-materials.md)); the reason children and adults differ ([scale and allometry](01-physics-of-the-body/scale-and-allometry.md)); the arithmetic of blood pH ([acids, bases and buffers](02-chemistry-of-life/acids-bases-and-buffers.md)); the source of metabolic energy and of oxidative injury ([redox](02-chemistry-of-life/redox-and-electron-transfer.md)); the constants K, Kd, Km and half-life ([kinetics, equilibrium and catalysis](02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md)); and the principle that shape is read by shape ([molecular recognition](02-chemistry-of-life/carbon-chemistry-and-molecular-recognition.md)).

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Physics of the Body](01-physics-of-the-body/README.md) | Forces and flows: energy, pressure, diffusion, electricity, mechanics, waves, scale | Mathematics (01) only |
| [Chemistry of Life](02-chemistry-of-life/README.md) | Molecules in water: bonds, solutions, protons, electrons, rates, recognition | Physics (thermodynamics, electricity), mathematics (01) |

Read physics first, beginning with thermodynamics, because the chemistry of equilibrium, redox and buffering is thermodynamics applied to molecules. The two areas cross-reference constantly: diffusion needs solutions, redox needs membrane voltage, mechanics needs the molecular shape of collagen.

## Connections to neighbouring layers

- **[01 Quantitative and Scientific Foundations](../01-quantitative-and-scientific-foundations/README.md):** the parallel root. It supplies the language (probability, exponential processes, regression, signal and noise) and in return takes from this layer nothing, by design.
- **[02 Biochemistry and Molecular Biology](../02-biochemistry-and-molecular-biology/README.md):** the direct heir. Bonds become proteins and membranes, redox becomes the respiratory chain, kinetics becomes enzymology, gradients become membrane transport.
- **[05 Tissues and Anatomy](../05-tissues-and-anatomy/README.md):** connective tissue, bone and vessel walls are the materials of mechanics; the branching architecture of vessels and airways is what scaling demands.
- **[06 Physiology](../06-physiology/README.md):** nearly every physiological equation is stated here first: Fick, Poiseuille, Laplace, Starling, Nernst, Henderson–Hasselbalch, Michaelis–Menten. Physiology adds the control loops.
- **[08 Pathology](../08-pathology/README.md):** oedema, aneurysm, infarction, oxidative injury and radiation damage are these laws with one term pushed out of range.
- **[09 Pharmacology and Therapeutics](../09-pharmacology-and-therapeutics/README.md):** absorption is polarity and pKa, distribution is solubility and binding, elimination is first-order and saturable kinetics, receptor theory is Kd, dosing by size is allometry, radiotherapy is ionising radiation.
- **[11 Clinical Method and Diagnostics](../11-clinical-method-and-diagnostics/README.md):** every imaging modality is wave physics; every electrical recording is volume conduction; every laboratory value is a concentration in water read against a reference range.

## Connections across layers

This layer gives the stack its hard limits and its recurring equations. The surface-to-volume constraint ([scale](01-physics-of-the-body/scale-and-allometry.md)) explains why a circulation exists, why a tumour must recruit vessels to grow beyond a millimetre, and why a neonate needs a different dose. Laplace's law links the [aneurysm](../12-organ-system-specialties/01-cardiology/hypertension-and-vascular-disease.md), the dilated ventricle in [heart failure](../12-organ-system-specialties/01-cardiology/heart-failure.md) and the surfactant-deficient lung of the [newborn](../14-life-course-mind-and-integrative-care/01-paediatrics/the-newborn-and-neonatology.md). The Nernst equation is why potassium disturbances cause [arrhythmias](../12-organ-system-specialties/01-cardiology/arrhythmias.md). The bicarbonate buffer is why the lung and kidney are partners in [acid–base disorders](../12-organ-system-specialties/03-nephrology/electrolyte-and-acid-base-disorders.md). Imperfect molecular recognition is the reason for [adverse drug reactions](../09-pharmacology-and-therapeutics/02-pharmacodynamics/adverse-drug-reactions-and-pharmacovigilance.md) and [autoimmunity](../07-microbiology-and-immunology/04-immunity-in-disease/autoimmunity.md). The hazard of ionising radiation sets the rules of [radiography](../11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/radiography-and-computed-tomography.md) and the power of [radiotherapy](../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md).

## Cross-cutting threads

- [Gradients and flow](../CROSS-CUTTING.md#gradients-and-flow): the layer's organising idea; every leaf is one gradient, its flow law and its cost.
- [Scale and surface-to-volume](../CROSS-CUTTING.md#scale-and-surface-to-volume): why size dictates design, from the cell to the newborn.
- [Structure determines function](../CROSS-CUTTING.md#structure-determines-function): radius to the fourth power, hollow bones, molecular shape and chirality.
- [Barriers and compartments](../CROSS-CUTTING.md#barriers-and-compartments): membranes as capacitors and semipermeable walls; the compartments that solutes define.
- [Specificity and recognition](../CROSS-CUTTING.md#specificity-and-recognition): complementary surfaces, affinity and the cost of cross-reactivity.
- [Supply and demand](../CROSS-CUTTING.md#supply-and-demand): oxygen delivery by Fick's law against metabolic consumption by redox.
- [Dose–response](../CROSS-CUTTING.md#dose-response): the Kd and Km hyperbolas; radiation dose; mechanical load.
- [Time-courses](../CROSS-CUTTING.md#time-courses): first-order decay and half-life, from radionuclides to drugs.
- [Feedback and homeostasis](../CROSS-CUTTING.md#feedback-and-homeostasis): buffers as chemical resistance to change, the raw material of physiological control.
