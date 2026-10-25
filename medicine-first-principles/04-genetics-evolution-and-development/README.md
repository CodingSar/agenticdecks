# 04 Genetics, Evolution and Development

> **Layer:** 04 Genetics, Evolution and Development
> **Children:** [Inheritance](01-inheritance/README.md) · [Evolution](02-evolution/README.md) · [Development](03-development/README.md)

## What this area is about

Layer 03 described a cell with a repertoire. This layer explains how an organism made of such cells comes to be the way it is, from three directions. *Inheritance* asks what is passed from parent to child and from cell to cell: single genes with Mendel's arithmetic, chromosomes with their dosage, the genome's millions of small variants, and the epigenetic marks that annotate them. *Evolution* asks why the genome is what it is: because selection, drift and mutation acted on populations over generations, favouring reproduction in past environments and leaving the body with mismatches, trade-offs, constraints and enemies that evolve faster than it does. *Development* asks how the genome becomes a body: how position becomes fate in gradients of a few reused signals, how three layers fold into every organ during an eight-week window, and how the body then grows, matures and declines on a schedule selection set.

The unifying idea is that **the organism is a historical object**. Its genes were shaped by what reproduced before; its form was built by a programme that could only modify what already existed; its vulnerabilities are the record of both. Much of pathology looks like bad design until it is read as the shadow of adaptation: ageing as the price of early vigour and cancer suppression, obesity and diabetes as a thrifty metabolism meeting abundance, septic shock as a defence calibrated for a world without antibiotics, antibiotic resistance as the inevitable arithmetic of selection on a population of 10^12. This layer supplies the *why* the mechanism-based layers above lack, and the tools of genetic counselling, prenatal diagnosis, cancer genomics, pharmacogenomics and stewardship.

## Why this layer sits here

This layer needs [03 Cell Biology](../03-cell-biology/README.md) for [meiosis](../03-cell-biology/02-the-cell-life-cycle/mitosis-meiosis-and-chromosome-segregation.md), which is the mechanism of Mendel's laws and of aneuploidy; for [differentiation and stem cells](../03-cell-biology/02-the-cell-life-cycle/stem-cells-differentiation-and-regeneration.md), which development is made of; and for [senescence](../03-cell-biology/02-the-cell-life-cycle/senescence-and-telomeres.md) and [apoptosis](../03-cell-biology/02-the-cell-life-cycle/cell-death-apoptosis-necrosis-and-autophagy.md), the model trade-off and the sculptor of form. It needs [02 Biochemistry and Molecular Biology](../02-biochemistry-and-molecular-biology/README.md) for the mutation rate set by [replication and repair](../02-biochemistry-and-molecular-biology/03-genetic-information-flow/dna-replication-and-repair.md), for [gene regulation and chromatin](../02-biochemistry-and-molecular-biology/03-genetic-information-flow/gene-regulation-and-epigenetic-mechanisms.md) and for the [receptors](../02-biochemistry-and-molecular-biology/04-cell-signalling/receptors-and-ligands.md) that read morphogens. It needs [01 Quantitative and Scientific Foundations](../01-quantitative-and-scientific-foundations/README.md) more than any layer so far: [probability](../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md) for segregation and drift, [Bayes](../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md) for counselling, [variance and regression](../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md) for heritability, [causal inference](../01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md) for Mendelian randomisation and teratology, and [exponential growth](../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md) for microbial and tumour populations.

What the layers above need from it is **the organism as a product of history, with the risk arithmetic that follows**. [05 Tissues and Anatomy](../05-tissues-and-anatomy/README.md) takes its tissue classification and body plan from the germ layers. [07 Microbiology and Immunology](../07-microbiology-and-immunology/README.md) takes the arms race as the frame for both pathogens and the immune system. [08 Pathology](../08-pathology/README.md) takes single-gene, chromosomal and multifactorial disease, cancer as somatic evolution, malformation as development disturbed, and ageing as trade-off. [09 Pharmacology](../09-pharmacology-and-therapeutics/README.md) takes pharmacogenomics, teratogenic risk and the evolutionary logic of combination antimicrobial and anticancer therapy. The abstraction this layer contributes is **variation, selection and position**: the organism varies because inheritance is particulate and imperfect, it is shaped because variants reproduce unequally, and its form arises because cells read their position and their moment.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [01 Inheritance](01-inheritance/README.md) | What is transmitted: Mendelian genes, chromosomes, genomic variation, complex traits, epigenetic marks | 03 meiosis and differentiation; 02 replication, chromatin, sequencing; 01 probability and regression |
| [02 Evolution](02-evolution/README.md) | Why the genome is as it is: selection and drift, evolutionary medicine, host–pathogen arms races, human history and variation | Inheritance; 01 probability and exponential growth; 03 senescence; 02 metabolism |
| [03 Development](03-development/README.md) | How the genome becomes a body and a life: embryogenesis, organogenesis, patterning, malformation, growth and ageing | Inheritance (imprinting, chromosomes); evolution (constraints, trade-offs); 03 stem cells, adhesion, death; 02 receptors; 00 diffusion |

```
          03 cell biology: meiosis, differentiation, signalling, death, senescence
                                        |
        +-------------------------------+--------------------------------+
        |                               |                                |
   01 inheritance                 02 evolution                     03 development
   what is passed on       -->    why it is so            -->      how it is read
   genes, chromosomes,            selection, drift,                gradients, layers,
   variants, marks                mismatch, trade-offs,            windows, growth,
        |                         arms races, our history          ageing
        |                               |                                |
   counselling, cancer            stewardship, "why" of          malformation, tumour
   genomics, pharmacogenomics     ageing and chronic disease     lineage, life course
```

Read inheritance first: it supplies the alleles and modes of transmission the other two assume. Evolution explains the frequencies and introduces the trade-offs that development's final leaf relies on. Development is last and ends where [05 tissues and anatomy](../05-tissues-and-anatomy/README.md) begins.

## Connections to neighbouring layers

- **[03 Cell Biology](../03-cell-biology/README.md):** supplies the mechanisms: meiosis for inheritance, differentiation and apoptosis for development, senescence for ageing.
- **[05 Tissues and Anatomy](../05-tissues-and-anatomy/README.md):** is the output of development. Tissues are germ-layer derivatives; cavities, dermatomes and the great vessels are embryology made solid.
- **[07 Microbiology and Immunology](../07-microbiology-and-immunology/README.md):** is the arms race described from both sides.
- **[08 Pathology](../08-pathology/README.md):** [genetic, metabolic and environmental disease](../08-pathology/04-genetic-metabolic-and-environmental-disease/README.md) catalogues inheritance's failures; [neoplasia](../08-pathology/03-neoplasia/README.md) is somatic mutation and clonal evolution reusing developmental pathways; [multifactorial disease](../08-pathology/05-disease-as-process/multifactorial-disease-and-risk.md) and the [diseases of ageing](../08-pathology/04-genetic-metabolic-and-environmental-disease/diseases-of-aging-and-degeneration.md) are mismatch and trade-off.
- **[09 Pharmacology and Therapeutics](../09-pharmacology-and-therapeutics/README.md):** [pharmacogenomics](../09-pharmacology-and-therapeutics/02-pharmacodynamics/pharmacogenomics-and-individual-variation.md), teratogenic [adverse reactions](../09-pharmacology-and-therapeutics/02-pharmacodynamics/adverse-drug-reactions-and-pharmacovigilance.md), the combination logic of [antimicrobials](../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/antimicrobials.md) and [anticancer drugs](../09-pharmacology-and-therapeutics/03-drug-classes-by-mechanism/anticancer-drugs.md) all rest here.
- **[10 Epidemiology and Evidence](../10-epidemiology-and-evidence/README.md):** polygenic [risk prediction](../10-epidemiology-and-evidence/03-screening-and-prevention/risk-prediction-and-stratification.md) and Mendelian randomisation as causal evidence.
- **[14 Life Course, Mind and Integrative Care](../14-life-course-mind-and-integrative-care/README.md):** [paediatrics](../14-life-course-mind-and-integrative-care/01-paediatrics/README.md) and [obstetrics](../14-life-course-mind-and-integrative-care/02-obstetrics-and-gynaecology/README.md) practise genetic counselling and prenatal diagnosis; [geriatrics](../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/README.md) manages the end of the life history.
- **[15 Medicine in Society](../15-medicine-in-society/README.md):** inherits the questions of ancestry, race, genetic privacy and antimicrobial resistance as a global commons problem.

## Connections across layers

This layer turns the cell's repertoire into an organism with a history and a risk profile. From below it takes meiosis, differentiation, mutation and the mathematics of populations; above it gives the body plan, the rules of inheritance, the "why" behind chronic disease and ageing, and the tools of genomic medicine. Three ideas recur higher up: a risk is a probability computed from inheritance and exposure, a population under pressure will evolve, and a structure's vulnerabilities are explained by how and when it was built.

## Cross-cutting threads

- [Trade-offs and evolutionary legacy](../CROSS-CUTTING.md#trade-offs-and-evolutionary-legacy): the home of this thread; antagonistic pleiotropy, mismatch, historical constraint and the life-history schedule.
- [Probability and uncertainty](../CROSS-CUTTING.md#probability-and-uncertainty): segregation, counselling, variant classification, polygenic scores, drift and mutation supply.
- [The host and its environment](../CROSS-CUTTING.md#the-host-and-its-environment): heritability depends on environment; local adaptation; developmental origins of adult disease; teratogens.
- [Signalling and information](../CROSS-CUTTING.md#signalling-and-information): the genome as a copied message; epigenetic marks; morphogen gradients and Hox codes as positional information.
- [Time courses](../CROSS-CUTTING.md#time-courses): critical periods in the embryo, generation times in the arms race, the growth curve and the Gompertz law of mortality.
- [Cause and mechanism](../CROSS-CUTTING.md#cause-and-mechanism): Mendelian disease as clean causation; Mendelian randomisation; proving a teratogen; ultimate alongside proximate explanation.
- [Dose–response](../CROSS-CUTTING.md#dose-response): gene dosage in aneuploidy and imprinting; morphogen thresholds; teratogen thresholds.
- [Redundancy and reserve](../CROSS-CUTTING.md#redundancy-and-reserve): MHC and immune diversity against unpredictable pathogens; the physiological reserve that ageing consumes.
