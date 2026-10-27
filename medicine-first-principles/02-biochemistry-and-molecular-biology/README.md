# 02 Biochemistry and Molecular Biology

> **Layer:** 02 Biochemistry and Molecular Biology
> **Children:** [Macromolecules](01-macromolecules/README.md) · [Metabolism](02-metabolism/README.md) · [Genetic information flow](03-genetic-information-flow/README.md) · [Cell signalling](04-cell-signalling/README.md)

## What this area is about

Biochemistry is chemistry organised into a living system: the same bonds, gradients, redox reactions and acid–base equilibria as in a flask, but arranged in polymers, pathways, codes and circuits that maintain themselves far from equilibrium. This layer describes that organisation at the level of molecules, before there is a cell. It has four parts. Macromolecules are the parts list: proteins that fold and catalyse, nucleic acids that store and copy a sequence, lipids that assemble into barriers, carbohydrates that fuel, hydrate and label. Metabolism is the energy economy: how electrons from food fall to oxygen and are captured as Adenosine Triphosphate (ATP), how fuels are interconverted within thermodynamic limits, and how a few hormones switch the flows. Genetic information flow is the information economy: how Deoxyribonucleic Acid (DNA) is copied, repaired, transcribed, translated and regulated, and how the same enzymes become laboratory tools. Cell signalling is the control system: how matter crosses a membrane through pumps, carriers and channels, and how a message crosses it through receptors, second messengers and kinase cascades.

The one idea the layer contributes is **a molecule's function is its shape and its free-energy state, and both are set by the chemistry below**. A protein's fold, a base pair, a bilayer, a gradient and a phosphorylated enzyme are each a configuration that weak forces and spent ATP hold in place. Everything medicine later calls a receptor, a drug target, a mutation, a metabolic disease or a signal is one of these configurations behaving as its chemistry dictates.

## Why this layer sits here

From [00 Physical and Chemical Foundations](../00-physical-and-chemical-foundations/README.md) this layer takes [free energy](../00-physical-and-chemical-foundations/01-physics-of-the-body/energy-and-thermodynamics.md) (why ATP works, why folding happens), [redox potential](../00-physical-and-chemical-foundations/02-chemistry-of-life/redox-and-electron-transfer.md) (why oxygen is the terminal acceptor), [acid–base chemistry](../00-physical-and-chemical-foundations/02-chemistry-of-life/acids-bases-and-buffers.md) (how enzymes catalyse, how nitrogen is excreted), [diffusion and osmosis](../00-physical-and-chemical-foundations/01-physics-of-the-body/diffusion-osmosis-and-transport.md) and [membrane electrostatics](../00-physical-and-chemical-foundations/01-physics-of-the-body/electricity-and-excitable-membranes.md) (why gradients exist and what they are worth), and [molecular recognition](../00-physical-and-chemical-foundations/02-chemistry-of-life/carbon-chemistry-and-molecular-recognition.md) (why an enzyme, a receptor, an antibody and a base pair are the same phenomenon). From [01 Quantitative and Scientific Foundations](../01-quantitative-and-scientific-foundations/README.md) it takes [feedback and control](../01-quantitative-and-scientific-foundations/03-systems-and-models/feedback-and-control.md), which makes gene networks stable and signalling adaptive, [probability](../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md), which governs mutation and error rates, and the vocabulary of [information and noise](../01-quantitative-and-scientific-foundations/03-systems-and-models/information-signals-and-noise.md).

What the layers above need from it is a set of mechanisms they can cite instead of restate. [03 Cell Biology](../03-cell-biology/README.md) assembles these molecules into organelles and a cell cycle and inherits the problem of misfolded proteins; [04 Genetics, Evolution and Development](../04-genetics-evolution-and-development/README.md) treats the mutation and the epigenetic mark as units of inheritance; [06 Physiology](../06-physiology/README.md) is this layer at organ scale; [08 Pathology](../08-pathology/README.md) begins injury with ATP depletion and cancer with DNA repair and kinase signalling; [09 Pharmacology](../09-pharmacology-and-therapeutics/README.md) is largely applied biochemistry; [11 Clinical Method and Diagnostics](../11-clinical-method-and-diagnostics/README.md) measures the molecules described here.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [01 Macromolecules](01-macromolecules/README.md) | The parts: proteins and enzymes, nucleic acids, lipids and membranes, carbohydrates | 00 chemistry and thermodynamics |
| [02 Metabolism](02-metabolism/README.md) | The energy economy: ATP and redox carriers, central pathways, fat, nitrogen, integration, cofactors | 01, 00 redox, 01 feedback |
| [03 Genetic information flow](03-genetic-information-flow/README.md) | The information economy: replication and repair, transcription, translation, regulation, techniques | 01 (nucleic acids, proteins), 02 (energy) |
| [04 Cell signalling](04-cell-signalling/README.md) | The control system: transport and gradients, receptors, messengers and kinases, computation | 01 (membranes, proteins), 02 (ATP), 01-layer feedback |

```
   00 chemistry & physics ---------------------------------- 01 feedback, probability, information
            |                                                           |
            v                                                           v
   [01 macromolecules]  proteins/enzymes  nucleic acids  lipids  carbohydrates
            |                  |                  |                 |
            v                  v                  v                 v
   [02 metabolism]  electrons -> ATP ; fuels interconverted ; insulin/glucagon switch
            |
   [03 information]  DNA --copy/repair--> DNA --transcribe--> RNA --translate--> protein --> address
            |
   [04 signalling]   gradients built by pumps ; ligand -> receptor -> messenger -> kinase -> response, off
            |
            v
   03 cell biology, 06 physiology, 08 pathology, 09 pharmacology, 11 diagnostics
```

Read the macromolecules first; every other parent assumes them. Metabolism and genetic information flow can be read in either order. Cell signalling is last because it uses the membrane (01), the ATP (02) and the transcription factors (03) as components.

## Connections to neighbouring layers

- **[00 Physical and Chemical Foundations](../00-physical-and-chemical-foundations/README.md):** the material root. Every tenet in this layer is a consequence of free energy, redox potential, acid–base equilibria, diffusion, electrostatics or non-covalent recognition acting on a particular molecule.
- **[01 Quantitative and Scientific Foundations](../01-quantitative-and-scientific-foundations/README.md):** feedback gives gene networks their memory and signalling its adaptation; probability gives mutation and polymerase error their rates; the fed–fasted cycle and hormone pulsatility are control problems.
- **[03 Cell Biology](../03-cell-biology/README.md):** the next scale. Organelles are bilayer compartments populated by targeted proteins; the cell cycle is replication with checkpoints; apoptosis is a kinase and protease cascade; quality control disposes of what folding and translation get wrong.
- **[06 Physiology](../06-physiology/README.md):** gradients become the action potential and renal transport; metabolism becomes glucose homeostasis, the liver and energy balance; receptors and cascades become the endocrine and autonomic systems.
- **[08 Pathology](../08-pathology/README.md):** cell injury begins with ATP and pump failure; neoplasia is DNA repair, oncogenic signalling and epigenetic silencing; atherosclerosis is lipoprotein retention; the inborn errors are missing enzymes.
- **[09 Pharmacology and Therapeutics](../09-pharmacology-and-therapeutics/README.md):** enzymes, receptors, channels and transporters are the targets; ribosome and polymerase differences give antimicrobial selectivity; kinase inhibitors, antisense oligonucleotides, monoclonal antibodies and gene editing are this layer turned into treatments.
- **[11 Clinical Method and Diagnostics](../11-clinical-method-and-diagnostics/README.md):** clinical chemistry measures the metabolites and leaked enzymes of parent 02, glycated haemoglobin of parent 01, and molecular diagnostics uses the hybridisation, amplification, sequencing and antibody methods of parent 03.

## Connections across layers

This layer is where the two roots first meet: chemistry and physics supply the forces, feedback and probability the logic, and the result is a system that stores energy in gradients, information in sequence, and control in reversible modifications. Physiology takes the gradients as given, genetics the sequence, pharmacology the modifications.

## Cross-cutting threads

- [Structure determines function](../CROSS-CUTTING.md#structure-determines-function): the fold is the enzyme, the pocket is the receptor, the alpha or beta bond is the digestibility.
- [Gradients and flow](../CROSS-CUTTING.md#gradients-and-flow): electrons down redox potential, protons down the mitochondrial gradient, sodium down the pump's gradient.
- [Feedback and homeostasis](../CROSS-CUTTING.md#feedback-and-homeostasis): end-product inhibition, insulin against glucagon, autoregulatory transcription factors, receptor desensitisation.
- [Supply and demand](../CROSS-CUTTING.md#supply-and-demand): respiratory control matches oxygen use to ATP demand; hypoxia is the mismatch, read as lactate.
- [Barriers and compartments](../CROSS-CUTTING.md#barriers-and-compartments): the bilayer, the mitochondrial inner membrane, the oxidising reticulum versus the reducing cytosol.
- [Signalling and information](../CROSS-CUTTING.md#signalling-and-information): the genetic code's redundancy and error correction; amplification, encoding and noise in cascades.
- [Specificity and recognition](../CROSS-CUTTING.md#specificity-and-recognition): active sites, base pairs, receptor pockets and the imperfect selectivity of every drug.
- [Time courses](../CROSS-CUTTING.md#time-courses): milliseconds for channels, seconds for G proteins, hours for nuclear receptors, days for glycation, months for glycated haemoglobin.
- [Dose–response](../CROSS-CUTTING.md#dose-response): saturation kinetics of enzymes and carriers; occupancy curves; the U-shaped curve of every nutrient.
- [Trade-offs and evolutionary legacy](../CROSS-CUTTING.md#trade-offs-and-evolutionary-legacy): a tuned rather than minimal mutation rate; vitamins as lost pathways; the mitochondrion's bacterial ribosome and the drugs that hit it.
