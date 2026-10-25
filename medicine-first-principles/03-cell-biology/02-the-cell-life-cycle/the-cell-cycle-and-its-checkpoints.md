# The cell cycle and its checkpoints

> **Layer:** [03 Cell Biology](../README.md) › [The cell life cycle](README.md)
> **Builds on:** [DNA replication and repair](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/dna-replication-and-repair.md), [Second messengers and kinase cascades](../../02-biochemistry-and-molecular-biology/04-cell-signalling/second-messengers-and-kinase-cascades.md), [Feedback and control](../../01-quantitative-and-scientific-foundations/03-systems-and-models/feedback-and-control.md), [Protein quality control and degradation](../01-cell-structure/protein-quality-control-and-degradation.md)
> **Enables:** [Hallmarks of cancer](../../08-pathology/03-neoplasia/hallmarks-of-cancer.md), [Oncogenes, tumour suppressors and genomic instability](../../08-pathology/03-neoplasia/oncogenes-tumour-suppressors-and-genomic-instability.md), [Anticancer drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md), [Radiotherapy and radiation biology](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md)

## Essence

The cell cycle is the ordered sequence by which one cell becomes two: grow (G1), copy the genome exactly once (S), check and prepare (G2), then divide (M). The problem it solves is fidelity under uncertainty: the genome must be replicated completely and only once, and no cell should divide with damaged or unreplicated Deoxyribonucleic Acid (DNA). The solution is a **biochemical oscillator built from cyclin-dependent kinases, made irreversible by protein destruction and gated by checkpoints** that halt progress until a condition is met. Cancer is, at its root, this control system failing: every tumour has lost a brake, gained an accelerator, or both. Chemotherapy and radiotherapy work because dividing cells are the most vulnerable to interference with it.

## Core tenets

1. **A kinase oscillator drives the cycle, and its phases are set by which cyclin is present.** Cyclin-Dependent Kinases (CDKs) are inactive alone; a cyclin subunit activates them and chooses their substrates. Cyclin D–CDK4/6 responds to growth signals in G1; cyclin E–CDK2 commits to S phase; cyclin A–CDK2 runs replication; cyclin B–CDK1 drives mitosis. Each cyclin is synthesised during one phase and destroyed at its end, so the cell is pushed from one state to the next rather than drifting. The control circuit is a relaxation oscillator of the kind described in [feedback and control](../../01-quantitative-and-scientific-foundations/03-systems-and-models/feedback-and-control.md): positive feedback makes each transition switch-like, and negative feedback (the kinase activating its own destroyer) resets it.

2. **Irreversibility comes from destruction, not from switching off.** Two ubiquitin ligases, SCF (in G1/S) and the Anaphase-Promoting Complex (APC/C, in mitosis), target cyclins and inhibitors for the proteasome ([protein degradation](../01-cell-structure/protein-quality-control-and-degradation.md)). Because a degraded protein cannot be reactivated, each phase can only be left in one direction. Separase, the enzyme that cuts sister chromatids apart, is released by APC/C destroying its inhibitor securin, so anaphase is both triggered and made final by the same proteolytic event.

3. **The restriction point in late G1 is the decision to divide, and it is the point most often corrupted in cancer.** Before it, the cell needs continuous mitogenic signalling (growth factor receptor to Ras to MAP kinase to cyclin D; [kinase cascades](../../02-biochemistry-and-molecular-biology/04-cell-signalling/second-messengers-and-kinase-cascades.md)). The retinoblastoma protein (Rb) holds the E2F transcription factors silent; cyclin D–CDK4/6 and then cyclin E–CDK2 phosphorylate Rb, releasing E2F, which transcribes S-phase genes including cyclin E itself. That positive loop makes the decision all-or-none and independent of further signals. Almost every human cancer has disabled this gate: by Rb loss, cyclin D amplification, CDK4 activation, or deletion of the CDK inhibitor p16. CDK4/6 inhibitors (palbociclib) re-close it in some breast cancers.

4. **Checkpoints are surveillance pathways that stop the oscillator until a condition is satisfied.** The DNA damage checkpoint (sensor kinases ATM and ATR, effector kinases Chk1 and Chk2, and p53) arrests at G1/S or G2/M while repair proceeds; the replication checkpoint prevents mitosis until S phase is complete; the spindle assembly checkpoint holds anaphase until every kinetochore is attached. Each works by inhibiting a CDK (through the inhibitors p21 or p27, or by keeping CDK1 phosphorylated and inactive). A checkpoint is a negative feedback loop with a delay built in deliberately.

5. **p53 is the integrator of stress, which is why it is the most frequently mutated gene in cancer.** Normally kept at low concentration by continuous degradation (via the E3 ligase MDM2), p53 is stabilised by DNA damage, oncogene activation, hypoxia and ribosomal stress. Stabilised p53 transcribes p21 (arrest), repair genes, and if damage persists, pro-apoptotic genes ([cell death](cell-death-apoptosis-necrosis-and-autophagy.md)). About half of all cancers carry a p53 mutation, and most of the rest disable the pathway another way (MDM2 amplification, viral proteins that bind p53). A cell without p53 keeps dividing with damaged DNA and accumulates further mutations, which is the mechanism behind [genomic instability](../../08-pathology/03-neoplasia/oncogenes-tumour-suppressors-and-genomic-instability.md).

6. **Replication is licensed once per cycle by a mechanism that is impossible to run twice.** Origins of replication are loaded with the MCM helicase only in late M and G1, when CDK activity is low; rising CDK activity in S phase both fires the origins and prevents new loading until the next mitosis. So no origin can fire twice in one cycle, and unreplicated DNA is impossible unless the checkpoint is also broken. The temporal separation of licensing and firing is the elegant core of exactly-once replication ([DNA replication](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/dna-replication-and-repair.md)).

7. **Cells leave the cycle more often than they stay in it.** Most adult cells are in G0, a stable non-dividing state: some reversibly (hepatocytes, lymphocytes, which re-enter on demand), some permanently (neurons, cardiomyocytes). Terminal differentiation and [senescence](senescence-and-telomeres.md) are exits. The regenerative capacity of a tissue (liver regrows, heart scars) is the fraction of its cells able to re-enter, and this is what [tissue repair](../../08-pathology/01-cell-and-tissue-injury/tissue-repair-regeneration-and-fibrosis.md) depends on.

8. **Therapies exploit cycle dependence.** Antimetabolites and topoisomerase inhibitors damage S-phase cells; antimitotics arrest M phase; ionising radiation is most lethal in M and G2, when chromatin is condensed and repair is restricted, and least in late S. Rapidly cycling normal tissues (marrow, gut epithelium, hair follicle) take the collateral damage, which explains the common toxicity profile of cytotoxic chemotherapy ([anticancer drugs](../../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md); [radiotherapy](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/radiotherapy-and-radiation-biology.md)). Fractionated radiotherapy works partly by catching cells as they move through sensitive phases.

## Key concepts

| Term | Meaning |
|---|---|
| G1, S, G2, M, G0 | Growth, DNA synthesis, second gap, mitosis, and the quiescent state outside the cycle |
| Cyclin-dependent kinase (CDK) | Kinase active only with a cyclin partner; the engine of the cycle |
| Cyclin | Phase-specific activator of a CDK, synthesised then destroyed each cycle |
| Restriction point | Late G1 commitment after which division no longer needs growth factors |
| Rb–E2F | Brake and accelerator at the restriction point; Rb phosphorylation releases E2F |
| Checkpoint | Signalling pathway that halts the cycle until DNA is intact, replicated or attached |
| p53 | Stress-activated transcription factor that arrests or kills damaged cells |
| APC/C, SCF | Ubiquitin ligases that make phase transitions irreversible |
| Licensing | Loading of replication helicases on origins only when CDK activity is low |
| CDK inhibitor (p16, p21, p27) | Proteins that bind and silence CDK–cyclin complexes |

## How it fits

- **Below:** uses [kinase cascades](../../02-biochemistry-and-molecular-biology/04-cell-signalling/second-messengers-and-kinase-cascades.md) as the input, [DNA replication](../../02-biochemistry-and-molecular-biology/03-genetic-information-flow/dna-replication-and-repair.md) as the task, [proteolysis](../01-cell-structure/protein-quality-control-and-degradation.md) for irreversibility, and the oscillator and feedback ideas of [layer 01](../../01-quantitative-and-scientific-foundations/03-systems-and-models/feedback-and-control.md).
- **Above:** [the hallmarks of cancer](../../08-pathology/03-neoplasia/hallmarks-of-cancer.md) begin with sustained proliferation and evaded growth suppression, which are this leaf's gates broken; [oncogenes and tumour suppressors](../../08-pathology/03-neoplasia/oncogenes-tumour-suppressors-and-genomic-instability.md) are its components named; chemotherapy and radiotherapy target it.
- **Siblings:** M phase is described in [mitosis and meiosis](mitosis-meiosis-and-chromosome-segregation.md); the exits are [cell death](cell-death-apoptosis-necrosis-and-autophagy.md) and [senescence](senescence-and-telomeres.md); [stem cells](stem-cells-differentiation-and-regeneration.md) are cells that balance cycling with exit.

## Common misconceptions

- **"Cancer cells divide faster than normal cells."** Many divide no faster than gut epithelium; the defect is that they do not stop, not that they are quick. Tumour growth reflects the balance of division against death and exit.
- **"Checkpoints are the normal timer of the cycle."** The timer is the cyclin–CDK oscillator; checkpoints only intervene when something is wrong, and cells lacking them cycle at normal speed until damage accumulates.
- **"p53 is a tumour suppressor because it stops division."** Its larger role is deciding between repair, permanent arrest and death; loss removes the cell's ability to eliminate itself when damaged.

## Go deeper

- David O. Morgan, *The Cell Cycle: Principles of Control* (2007): the clearest account of the oscillator and its logic.
- Leland H. Hartwell and Ted A. Weinert, "Checkpoints: Controls That Ensure the Order of Cell Cycle Events", *Science* (1989): the paper that named the idea.
- Robert A. Weinberg, *The Biology of Cancer* (2nd ed., 2014), chapters on Rb and p53: the cycle as cancer sees it.
