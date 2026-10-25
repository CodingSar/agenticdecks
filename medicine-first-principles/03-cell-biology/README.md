# 03 Cell Biology

> **Layer:** 03 Cell Biology
> **Children:** [Cell structure](01-cell-structure/README.md) · [The cell life cycle](02-the-cell-life-cycle/README.md) · [Cells in community](03-cells-in-community/README.md)

## What this area is about

The cell is the smallest thing that is alive, and this layer is where the two roots of the tree meet in a living unit. From layer 00 come gradients, diffusion limits, mechanics and the chemistry of bonds and redox; from layer 01 come feedback, oscillators and exponential growth; from layer 02 come enzymes, membranes, pumps, genes and signalling cascades. None of these is alive on its own. A cell is what you get when they are combined in one bounded, self-maintaining, self-copying structure: **thermodynamics** (a membrane holding gradients that cost energy to maintain), **chemistry** (enzymes sorted into compartments where incompatible reactions can run side by side), and **information** (a genome read into proteins that each carry an address, and signals that tell the cell when to divide, differentiate or die). Every organ, every disease and every drug in the layers above is ultimately an account of what cells are doing.

The layer has three parts. *Cell structure* is the cell as a built object: compartments, skeleton, traffic and maintenance. *The cell life cycle* is the cell as a decision-maker: divide, share chromosomes, die, stop or stay a stem cell. *Cells in community* is the cell as a citizen: holding on, communicating, coping with stress and raising the alarm.

## Why this layer sits here

This layer needs [00 Physical and Chemical Foundations](../00-physical-and-chemical-foundations/README.md) for the fact that a bilayer blocks ions and that [diffusion](../00-physical-and-chemical-foundations/01-physics-of-the-body/diffusion-osmosis-and-transport.md) is fast over micrometres and useless over millimetres, which sets the size of cells and organelles ([scale](../00-physical-and-chemical-foundations/01-physics-of-the-body/scale-and-allometry.md)); for the [mechanics](../00-physical-and-chemical-foundations/01-physics-of-the-body/mechanics-and-materials.md) of filaments and collagen; and for [redox chemistry](../00-physical-and-chemical-foundations/02-chemistry-of-life/redox-and-electron-transfer.md), which is both the energy source and the main hazard. It needs [01 Quantitative and Scientific Foundations](../01-quantitative-and-scientific-foundations/README.md) for [feedback and oscillators](../01-quantitative-and-scientific-foundations/03-systems-and-models/feedback-and-control.md), which the cell cycle and every stress sensor instantiate, and for [probability](../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md), which governs meiotic assortment and mutation. It needs all of [02 Biochemistry and Molecular Biology](../02-biochemistry-and-molecular-biology/README.md): the macromolecules it is built from, the metabolism that pays for its gradients, the information flow from gene to targeted protein, and the receptors and cascades through which it is told what to do.

What the layers above need from it is **the cell as a unit with a repertoire**: a bounded, polarised object with a defined set of compartments, a cytoskeleton, a cycle with checkpoints, two ways of dying, a permanent arrest, a stem cell hierarchy, adhesion, junctions and a stress response. [04 Genetics, Evolution and Development](../04-genetics-evolution-and-development/README.md) needs meiosis for inheritance and differentiation for development. [05 Tissues and Anatomy](../05-tissues-and-anatomy/README.md) classifies tissues by their cells, junctions and matrix. [06 Physiology](../06-physiology/README.md) needs regulated exocytosis for every synapse and gland, gap junctions for the heartbeat and tight junctions for every barrier. [07 Microbiology and Immunology](../07-microbiology-and-immunology/README.md) needs apoptosis as a weapon, trafficking for antigen presentation and alarmins to start inflammation. [08 Pathology](../08-pathology/README.md) begins with cell injury, adaptation and death, and its whole account of neoplasia is this layer's controls failing. The abstraction this layer contributes is **regulated fate**: a cell's structure, division, death and identity are decisions made by circuits with sensors, thresholds and irreversible steps, and disease is those circuits misreading, miscounting or breaking.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [01 Cell structure](01-cell-structure/README.md) | The built cell: organelles as maintained compartments, the cytoskeleton as mechanics and transport, trafficking as flow, quality control as maintenance | 00 physics; 02 membranes, folding, targeting, ATP |
| [02 The cell life cycle](02-the-cell-life-cycle/README.md) | The deciding cell: the cycle and its checkpoints, mitosis and meiosis, apoptosis and necrosis, senescence, stem cells | 01 feedback; 02 replication and kinase cascades; cell structure |
| [03 Cells in community](03-cells-in-community/README.md) | The social cell: adhesion and matrix, communication and junctions, the stress response | Cell structure, cell life cycle; 02 receptors; 00 mechanics and diffusion |

```
   00 gradients, diffusion, mechanics, redox       01 feedback, oscillators, probability
                      \                                   /
                       02 enzymes, membranes, genes, signals
                                      |
             +------------------------+------------------------+
             |                        |                        |
       01 structure             02 life cycle            03 community
   compartments, skeleton,    divide, segregate,       adhere, communicate,
   traffic, maintenance       die, stop, renew         withstand stress
             \                        |                        /
              +--------- the cell: bounded, self-maintaining, fated ---------+
                                      |
        04 inheritance & development   05 tissues   06 physiology   07 immunity   08 pathology
```

Read structure first, because the life cycle and the community both assume a cell with compartments, a skeleton and a maintenance system. Within structure, organelles come before trafficking and quality control. The life cycle is best read in order: the cycle and its checkpoints define the vocabulary; mitosis and meiosis, death, senescence and stem cells are the branches of its decision tree. Cells in community can be read last; the stress response is its natural end, because it is the point where cell biology hands over to pathology.

## Connections to neighbouring layers

- **[02 Biochemistry and Molecular Biology](../02-biochemistry-and-molecular-biology/README.md):** supplies every component. The boundary is organisation: 02 describes the sodium pump, 03 describes the cell that would swell and burst without it; 02 describes a kinase cascade, 03 describes the decision to divide that it drives.
- **[04 Genetics, Evolution and Development](../04-genetics-evolution-and-development/README.md):** takes meiosis as the mechanism of inheritance and its errors, differentiation and signalling as the mechanism of development, and senescence and apoptosis as trade-offs that evolution has set.
- **[05 Tissues and Anatomy](../05-tissues-and-anatomy/README.md):** is this layer at the next scale. Epithelium is cells with tight junctions on a basement membrane; connective tissue is matrix with cells in it; blood is a stem cell hierarchy in flow.
- **[06 Physiology](../06-physiology/README.md):** every physiological mechanism is a cell biological one aggregated: secretion is exocytosis, conduction is gap junctions and ion channels, muscle is the cytoskeleton, hormone action is receptor and trafficking biology.
- **[07 Microbiology and Immunology](../07-microbiology-and-immunology/README.md):** pathogens enter by endocytosis, cleave SNAREs, block apoptosis and exploit the cytoskeleton; the immune system kills by apoptosis, reads trafficking through antigen presentation and is summoned by alarmins.
- **[08 Pathology](../08-pathology/README.md):** is the closest consumer. Cell injury, adaptation and death ([08.01](../08-pathology/01-cell-and-tissue-injury/README.md)) is the stress response and the death pathways read in tissue; [neoplasia](../08-pathology/03-neoplasia/README.md) is the cell cycle, apoptosis, senescence, adhesion and stem cell biology each subverted; storage diseases and amyloidosis are organelles and quality control failing.
- **[09 Pharmacology and Therapeutics](../09-pharmacology-and-therapeutics/README.md):** antimitotics, antimetabolites, proteasome inhibitors, BH3 mimetics, CDK inhibitors, senolytics and cell therapies are each aimed at a leaf of this layer; chemotherapy toxicity is the cost of hitting every cycling tissue.
- **[12 Organ-system Specialties](../12-organ-system-specialties/README.md)** and **[14 Life Course, Mind and Integrative Care](../14-life-course-mind-and-integrative-care/README.md):** [neurodegeneration](../12-organ-system-specialties/10-neurology/neurodegenerative-disease.md) is protein quality control failing in cells that cannot divide; [haematological malignancies](../12-organ-system-specialties/06-haematology/haematological-malignancies.md) are stem cell hierarchies gone wrong; [frailty](../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/frailty-multimorbidity-and-polypharmacy.md) is senescence and stem cell exhaustion seen in a person.

## Connections across layers

This layer converts molecules into a living unit and hands the layers above a cell with a fixed repertoire. From below it takes gradients, mechanics, feedback and the full molecular toolkit; to the layers above it gives the tissue, the organism's development, the mechanism of every physiological function and the first vocabulary of disease. Three ideas introduced here reappear at every higher scale: that a barrier is only useful with regulated transport across it, that fate is decided by circuits with irreversible steps, and that a unit's survival depends on the signals it receives from the community it belongs to.

## Cross-cutting threads

- [Barriers and compartments](../CROSS-CUTTING.md#barriers-and-compartments): the membrane, the organelle, the tight junction and the basement membrane are the first instances of the body's compartment logic.
- [Gradients and flow](../CROSS-CUTTING.md#gradients-and-flow): every organelle is a gradient paid for with ATP; vesicle traffic and motor transport are directed flow.
- [Feedback and homeostasis](../CROSS-CUTTING.md#feedback-and-homeostasis): the cyclin oscillator, the checkpoints and every stress sensor are feedback loops.
- [Signalling and information](../CROSS-CUTTING.md#signalling-and-information): signal sequences, degrons, lateral inhibition and alarmins are the cell's addresses and messages.
- [Structure determines function](../CROSS-CUTTING.md#structure-determines-function): cristae, filaments, collagen, claudins and connexins.
- [Scale and surface-to-volume](../CROSS-CUTTING.md#scale-and-surface-to-volume): diffusion sets cell and organelle size; long cells need motors; tissues need vessels.
- [Trade-offs and evolutionary legacy](../CROSS-CUTTING.md#trade-offs-and-evolutionary-legacy): apoptosis and senescence suppress cancer at the cost of degeneration and ageing; the captured mitochondrion powers and kills the cell.
- [Injury and repair](../CROSS-CUTTING.md#injury-and-repair): adaptation, reversible injury, regeneration from stem cells and fibrosis from matrix begin here.
- [Time courses](../CROSS-CUTTING.md#time-courses): filament turnover in seconds, a cell cycle in hours, a telomere clock in decades.
