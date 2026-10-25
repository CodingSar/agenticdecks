# Mitosis, meiosis and chromosome segregation

> **Layer:** [03 Cell Biology](../README.md) › [The cell life cycle](README.md)
> **Builds on:** [The cell cycle and its checkpoints](the-cell-cycle-and-its-checkpoints.md), [The cytoskeleton and cell motility](../01-cell-structure/the-cytoskeleton-and-cell-motility.md), [Nucleic acids](../../02-biochemistry-and-molecular-biology/01-macromolecules/nucleic-acids.md), [Probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md)
> **Enables:** [Chromosomes and cytogenetics](../../04-genetics-evolution-and-development/01-inheritance/chromosomes-and-cytogenetics.md), [Mendelian inheritance and pedigrees](../../04-genetics-evolution-and-development/01-inheritance/mendelian-inheritance-and-pedigrees.md), [Gametogenesis and the menstrual cycle](../../06-physiology/09-reproduction-and-the-life-course/gametogenesis-and-the-menstrual-cycle.md), [Single-gene and chromosomal disorders](../../08-pathology/04-genetic-metabolic-and-environmental-disease/single-gene-and-chromosomal-disorders.md)

## Essence

Two metres of Deoxyribonucleic Acid (DNA) in 46 chromosomes must be shared exactly between two daughter cells, every time, in every one of the ~10^16 divisions of a human lifetime. Mitosis does this by condensing the replicated chromosomes, attaching each sister pair to a bipolar microtubule spindle, verifying that every pair is under tension from both poles, and only then cutting the cohesion between sisters. Meiosis is mitosis modified to halve the chromosome number for sex: one round of replication, two rounds of division, with homologous chromosomes paired and recombined in the first. The one idea is **tension-sensing**: a chromosome is correctly attached when pulled from both sides, and the spindle checkpoint will not release anaphase until every chromosome reports tension. Errors give aneuploidy, the leading cause of miscarriage, of Down syndrome, and a hallmark of cancer cells; recombination in meiosis is why siblings differ and why genes can be mapped.

## Core tenets

1. **Sister chromatids are held together from replication to anaphase by cohesin, and segregation is the controlled destruction of that link.** Cohesin rings encircle the two copies as they are made in S phase. In mitosis the spindle pulls sisters in opposite directions, but cohesin resists until the Anaphase-Promoting Complex destroys securin, releasing the protease separase, which cuts cohesin. Separation is therefore simultaneous for all chromosomes and irreversible. A sister pair that loses cohesion early can segregate randomly; one that cannot lose it is torn or left behind.

2. **The spindle is self-organising, and attachment is corrected by trial and error.** Microtubules growing from the two centrosomes search by dynamic instability ([cytoskeleton](../01-cell-structure/the-cytoskeleton-and-cell-motility.md)) until they capture a kinetochore, the protein machine built on each chromatid's centromere. Correct attachment (each sister to the opposite pole) puts the kinetochore pair under tension; wrong attachments (both sisters to one pole, or one sister to both) do not. Low tension leaves the kinetochore kinase Aurora B able to phosphorylate and loosen the attachment, so wrong ones are released and tried again while right ones are stabilised. Correctness is reached by a physical test rather than by recognising sequence.

3. **The spindle assembly checkpoint makes anaphase wait for the last chromosome.** An unattached kinetochore emits an inhibitory signal (the Mitotic Checkpoint Complex) that blocks the Anaphase-Promoting Complex. A single unattached kinetochore in a cell with 92 is enough to hold the whole cell, which is a remarkable amplification ([cell cycle checkpoints](the-cell-cycle-and-its-checkpoints.md)). When the signal weakens (checkpoint gene mutations, or drugs that stall the spindle for so long that the cell "slips" through), cells exit mitosis with the wrong number of chromosomes. Antimitotic chemotherapy relies on prolonged checkpoint arrest leading to death.

4. **Meiosis produces haploid, genetically unique gametes by two reductions and one shuffle.** In meiosis I, homologous chromosomes (one from each parent) pair along their length, exchange segments by crossing over, and are pulled to opposite poles while sister chromatids stay together (cohesin at the centromere is protected by shugoshin). Meiosis II then separates sisters as in mitosis. Each pair orients independently, giving 2^23 (~8 million) possible combinations before crossing over is counted; with one to three crossovers per chromosome, every gamete is unique. This is the physical basis of Mendel's laws of segregation and independent assortment ([Mendelian inheritance](../../04-genetics-evolution-and-development/01-inheritance/mendelian-inheritance-and-pedigrees.md)) and of the fact that linked genes are inherited together in proportion to their distance.

5. **Crossing over is not optional: it holds homologues together.** The chiasmata formed by recombination are what physically link a homologous pair until anaphase I. A pair with no crossover can separate early and segregate at random. Small chromosomes with few crossovers (21, 22) and the X in oocytes are the most vulnerable, which is one reason trisomy 21 is the commonest viable autosomal trisomy.

6. **Human female meiosis is slow and error-prone by design, and the error rate rises with age.** Oocytes begin meiosis in the fetus, arrest in prophase I for 10 to 50 years, and complete meiosis I only at ovulation and meiosis II at fertilisation ([gametogenesis](../../06-physiology/09-reproduction-and-the-life-course/gametogenesis-and-the-menstrual-cycle.md)). Cohesin laid down in fetal life must survive those decades without being replaced, and it degrades. The result is that most human aneuploidy is maternal in origin and of meiosis I, and the risk of a trisomic pregnancy rises steeply after about 35 years. Male meiosis runs continuously from puberty with a much lower aneuploidy rate but accumulates point mutations with each replication.

7. **Aneuploidy is common in conception and lethal in most of its forms.** Roughly a quarter or more of human oocytes are chromosomally abnormal, and aneuploidy is found in about half of first-trimester miscarriages. Monosomy of any autosome and most trisomies are incompatible with life; trisomy 21, 18 and 13 and sex-chromosome aneuploidies (45,X; 47,XXY) survive because of small gene content or X inactivation ([chromosomes and cytogenetics](../../04-genetics-evolution-and-development/01-inheritance/chromosomes-and-cytogenetics.md); [chromosomal disorders](../../08-pathology/04-genetic-metabolic-and-environmental-disease/single-gene-and-chromosomal-disorders.md)). The phenotype of aneuploidy is dosage: a 1.5-fold change in hundreds of genes at once, which no cell is tuned for.

8. **Chromosomal instability is a hallmark of cancer and a double-edged one.** Many tumours missegregate a chromosome every few divisions because of extra centrosomes, weakened checkpoints or cohesion defects. This generates diversity on which selection acts, accelerating tumour evolution and drug resistance; but high rates are also lethal to the cancer cell, and lagging chromosomes trapped in micronuclei rupture and trigger inflammation. Mitotic errors are thus both an engine of cancer and a therapeutic vulnerability.

## Key concepts

| Term | Meaning |
|---|---|
| Chromatid | One of the two identical copies of a replicated chromosome |
| Cohesin | Ring complex holding sister chromatids together until separase cuts it |
| Kinetochore | Protein machine on the centromere that binds spindle microtubules and reports tension |
| Bi-orientation | Sisters attached to opposite poles; the only configuration under tension |
| Spindle assembly checkpoint | Signal from unattached kinetochores that blocks anaphase |
| Homologous chromosomes | The maternal and paternal copies of one chromosome, paired in meiosis I |
| Crossing over / chiasma | Physical exchange between homologues; also the link that holds them together |
| Nondisjunction | Failure of chromosomes or chromatids to separate; the cause of aneuploidy |
| Aneuploidy | Abnormal chromosome number; trisomy and monosomy |
| Independent assortment | Random orientation of each homologous pair relative to the others |

## How it fits

- **Below:** the spindle is the [cytoskeleton](../01-cell-structure/the-cytoskeleton-and-cell-motility.md) in action; the trigger and irreversibility come from the [cell cycle](the-cell-cycle-and-its-checkpoints.md); the 2^23 count and the probability of a nondisjunction event are [probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md).
- **Above:** meiosis gives the rules of [inheritance](../../04-genetics-evolution-and-development/01-inheritance/mendelian-inheritance-and-pedigrees.md), the karyotypes of [cytogenetics](../../04-genetics-evolution-and-development/01-inheritance/chromosomes-and-cytogenetics.md), the timing of [gametogenesis](../../06-physiology/09-reproduction-and-the-life-course/gametogenesis-and-the-menstrual-cycle.md), and the recombination maps used to find disease genes; mitotic error feeds [neoplasia](../../08-pathology/03-neoplasia/oncogenes-tumour-suppressors-and-genomic-instability.md).
- **Siblings:** the spindle checkpoint is one of the [checkpoints](the-cell-cycle-and-its-checkpoints.md); a cell that fails mitosis badly dies by [apoptosis](cell-death-apoptosis-necrosis-and-autophagy.md) or becomes [senescent](senescence-and-telomeres.md); [stem cells](stem-cells-differentiation-and-regeneration.md) can divide asymmetrically by orienting the spindle.

## Common misconceptions

- **"Chromosomes are pulled apart by the spindle."** They are held together by cohesin against the spindle's pull; the trigger of anaphase is cutting cohesin, not increasing force.
- **"Meiosis just halves the chromosome number."** The reduction could be done in one step; the second division and the recombination exist to shuffle alleles, which is the evolutionary point of sex.
- **"Down syndrome is inherited."** About 95% of cases are new nondisjunction events in a parent's meiosis, mostly maternal; only the rare translocation forms run in families.

## Go deeper

- Bruce Alberts and colleagues, *Molecular Biology of the Cell* (7th ed., 2022), chapters on the cell cycle and on meiosis: spindle mechanics and checkpoint logic.
- Terry Hassold and Patricia Hunt, "To Err (Meiotically) Is Human: The Genesis of Human Aneuploidy", *Nature Reviews Genetics* (2001): the maternal age effect and its mechanisms.
- Kim Nasmyth and Christian H. Haering, "Cohesin: Its Roles and Mechanisms", *Annual Review of Genetics* (2009): the ring that holds sisters together.
