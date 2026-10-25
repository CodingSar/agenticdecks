# The cell cycle and its checkpoints

> **Layer:** [03 Cell Biology](../README.md) › [The cell life cycle](README.md)
> **Builds on:** [DNA replication and repair](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/dna-replication-and-repair.md), [Second messengers and kinase cascades](../../02-biochemistry-and-molecular-biology/04-cell-signalling/second-messengers-and-kinase-cascades.md), [Feedback and control](../../01-quantitative-and-scientific-foundations/03-systems-and-models/feedback-and-control.md), [Protein quality control and degradation](../01-cell-structure/protein-quality-control-and-degradation.md)
> **Enables:** [Hallmarks of cancer](../../08-pathology/03-neoplasia/hallmarks-of-cancer.md), [Oncogenes, tumour suppressors and genomic instability](../../08-pathology/03-neoplasia/oncogenes-tumour-suppressors-and-genomic-instability.md), [Anticancer drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md), [Radiotherapy and radiation biology](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md)

## Essence

The cell cycle is the ordered sequence by which one cell becomes two: grow (G1), copy the genome exactly once (S), check and prepare (G2), divide (M). The problem it solves is fidelity: the Deoxyribonucleic Acid (DNA) must be replicated completely and only once, and no cell should divide with damaged or unreplicated DNA. The solution is **a kinase oscillator made irreversible by protein destruction and gated by checkpoints** that halt progress until a condition is met. Cancer is this control system failing: every tumour has lost a brake, gained an accelerator, or both.

## Core tenets

1. **A kinase oscillator drives the cycle, and the cyclin present sets the phase.** Cyclin-Dependent Kinases (CDKs) are inactive alone; a cyclin activates them and chooses their substrates. Cyclin D–CDK4/6 responds to growth signals in G1; cyclin E–CDK2 commits to S; cyclin A–CDK2 runs replication; cyclin B–CDK1 drives mitosis. Each cyclin is made in one phase and destroyed at its end, so the cell is pushed from state to state. The circuit is a relaxation oscillator ([feedback and control](../../01-quantitative-and-scientific-foundations/03-systems-and-models/feedback-and-control.md)): positive feedback makes each transition switch-like, negative feedback (the kinase activating its own destroyer) resets it.

2. **Irreversibility comes from destruction, not from switching off.** Two ubiquitin ligases, SCF (G1/S) and the Anaphase-Promoting Complex (APC/C, mitosis), send cyclins and inhibitors to the proteasome ([protein degradation](../01-cell-structure/protein-quality-control-and-degradation.md)). A degraded protein cannot be reactivated, so each phase can only be left in one direction. Anaphase itself is triggered by APC/C destroying securin, the inhibitor of the enzyme that cuts sister chromatids apart.

3. **The restriction point in late G1 is the decision to divide, and the gate most often corrupted in cancer.** Before it the cell needs continuous mitogenic signalling (growth factor receptor to Ras to MAP kinase to cyclin D; [kinase cascades](../../02-biochemistry-and-molecular-biology/04-cell-signalling/second-messengers-and-kinase-cascades.md)). The retinoblastoma protein (Rb) holds the E2F transcription factors silent; cyclin D–CDK4/6 then cyclin E–CDK2 phosphorylate Rb, releasing E2F, which transcribes S-phase genes including cyclin E itself. That positive loop makes the decision all-or-none. Nearly every cancer has disabled this gate (Rb loss, cyclin D amplification, p16 deletion); CDK4/6 inhibitors re-close it in some breast cancers.

4. **Checkpoints stop the oscillator until a condition is satisfied.** The DNA damage checkpoint (sensor kinases ATM and ATR, effectors Chk1, Chk2 and p53) arrests at G1/S or G2/M while repair proceeds; the replication checkpoint prevents mitosis until S is complete; the spindle assembly checkpoint holds anaphase until every kinetochore is attached. Each works by inhibiting a CDK.

5. **p53 integrates stress, which is why it is the most frequently mutated gene in cancer.** Kept low by continuous degradation via the E3 ligase MDM2, p53 is stabilised by DNA damage, oncogene activation and hypoxia. It then transcribes p21 (arrest), repair genes and, if damage persists, pro-apoptotic genes ([cell death](cell-death-apoptosis-necrosis-and-autophagy.md)). About half of cancers carry a p53 mutation and most of the rest disable the pathway otherwise (MDM2 amplification, viral proteins). A cell without p53 keeps dividing with damaged DNA, the mechanism behind [genomic instability](../../08-pathology/03-neoplasia/oncogenes-tumour-suppressors-and-genomic-instability.md).

6. **Replication is licensed once per cycle by a mechanism that cannot run twice.** Origins are loaded with the MCM helicase only in late M and G1, when CDK activity is low; rising CDK activity fires the origins and blocks new loading until the next mitosis. Separating licensing from firing in time is the core of exactly-once [replication](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/dna-replication-and-repair.md).

7. **Most adult cells are outside the cycle.** G0 is a stable non-dividing state: reversible in hepatocytes and lymphocytes, permanent in neurons and cardiomyocytes. Terminal differentiation and [senescence](senescence-and-telomeres.md) are exits. A tissue's regenerative capacity (liver regrows, heart scars) is the fraction of its cells able to re-enter, which is what [tissue repair](../../08-pathology/01-cell-and-tissue-injury/tissue-repair-regeneration-and-fibrosis.md) depends on.

8. **Therapies exploit cycle dependence.** Antimetabolites and topoisomerase inhibitors damage S-phase cells; antimitotics arrest M; ionising radiation is most lethal in M and G2 and least in late S. Rapidly cycling normal tissues (marrow, gut epithelium, hair follicle) take the collateral damage, which explains the shared toxicity profile of cytotoxic chemotherapy ([anticancer drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md); [radiotherapy](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md)).

## Key concepts

| Term | Meaning |
|---|---|
| G1, S, G2, M, G0 | Growth, DNA synthesis, second gap, mitosis, and quiescence outside the cycle |
| Cyclin-dependent kinase (CDK) | Kinase active only with a cyclin partner; the engine of the cycle |
| Cyclin | Phase-specific CDK activator, synthesised then destroyed each cycle |
| Restriction point | Late G1 commitment after which division no longer needs growth factors |
| Rb–E2F | Brake and accelerator at the restriction point |
| Checkpoint | Pathway that halts the cycle until DNA is intact, replicated or attached |
| p53 | Stress-activated transcription factor that arrests or kills damaged cells |
| APC/C, SCF | Ubiquitin ligases that make phase transitions irreversible |

## How it fits

- **Below:** input from [kinase cascades](../../02-biochemistry-and-molecular-biology/04-cell-signalling/second-messengers-and-kinase-cascades.md), the task from [DNA replication](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/dna-replication-and-repair.md), irreversibility from [proteolysis](../01-cell-structure/protein-quality-control-and-degradation.md), oscillator logic from [layer 01](../../01-quantitative-and-scientific-foundations/03-systems-and-models/feedback-and-control.md).
- **Above:** [the hallmarks of cancer](../../08-pathology/03-neoplasia/hallmarks-of-cancer.md) begin with sustained proliferation and evaded growth suppression, this leaf's gates broken; [oncogenes and tumour suppressors](../../08-pathology/03-neoplasia/oncogenes-tumour-suppressors-and-genomic-instability.md) are its components named; chemotherapy and radiotherapy target it.
- **Siblings:** M phase is [mitosis and meiosis](mitosis-meiosis-and-chromosome-segregation.md); the exits are [cell death](cell-death-apoptosis-necrosis-and-autophagy.md) and [senescence](senescence-and-telomeres.md); [stem cells](stem-cells-differentiation-and-regeneration.md) balance cycling against exit.

## Common misconceptions

- **"Cancer cells divide faster than normal cells."** Many divide no faster than gut epithelium; the defect is that they do not stop. Tumour growth is division minus death and exit.
- **"Checkpoints are the cycle's timer."** The timer is the cyclin–CDK oscillator; checkpoints intervene only when something is wrong.
- **"p53 suppresses tumours by stopping division."** Its larger role is choosing between repair, permanent arrest and death; its loss removes the cell's ability to eliminate itself.

## Go deeper

- David O. Morgan, *The Cell Cycle: Principles of Control* (2007): the clearest account of the oscillator and its logic.
- Leland H. Hartwell and Ted A. Weinert, "Checkpoints: Controls That Ensure the Order of Cell Cycle Events", *Science* (1989): the paper that named the idea.
- Robert A. Weinberg, *The Biology of Cancer* (2nd ed., 2014), chapters on Rb and p53: the cycle as cancer sees it.
