# Pharmacogenomics and individual variation

> **Layer:** [09 Pharmacology and Therapeutics](../README.md) › [Pharmacodynamics](README.md)
> **Builds on:** [Genomic variation and mutation](../../04-genetics-evolution-and-development/01-inheritance/genomic-variation-and-mutation.md), [Complex traits and heritability](../../04-genetics-evolution-and-development/01-inheritance/complex-traits-and-heritability.md), [Human evolution and variation](../../04-genetics-evolution-and-development/02-evolution/human-evolution-and-variation.md), [Drug metabolism and interactions](../01-pharmacokinetics/drug-metabolism-and-interactions.md), [Dose–response and therapeutic index](dose-response-and-therapeutic-index.md)
> **Enables:** [Adverse drug reactions and pharmacovigilance](adverse-drug-reactions-and-pharmacovigilance.md), [Anticancer drugs](../03-drug-classes-by-mechanism/anticancer-drugs.md), [Histopathology, cytology and molecular diagnostics](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/histopathology-cytology-and-molecular-diagnostics.md), [Systemic anticancer therapy](../../12-organ-system-specialties/07-oncology/systemic-anticancer-therapy.md), [The future of medicine](../../15-medicine-in-society/03-populations-and-the-future/the-future-of-medicine.md)

## Essence

The quantal dose–response curve is wide because people differ, and much of that difference is inherited. Variants in the genes for metabolising enzymes, transporters, receptors and the human leukocyte antigen (HLA) system change how much drug a given dose produces and how a given concentration is received. Pharmacogenomics is the study of these variants, and its practical form is a small set of gene–drug pairs for which a test before prescribing changes the dose or the drug. The single idea is that the population's dose–response curve is the sum of several narrower curves, one per genotype, and that identifying which curve a patient is on removes variation that otherwise looks like chance. Genes are only part of the picture: age, organ function, body composition, diet, other drugs and disease supply the rest.

## Core tenets

1. **Enzyme polymorphisms produce discrete metaboliser phenotypes, and the consequence depends on whether the parent drug or its metabolite is active.** Loss-of-function alleles of CYP2D6, CYP2C19, CYP2C9, dihydropyrimidine dehydrogenase (DPYD), thiopurine methyltransferase (TPMT) and N-acetyltransferase 2 (NAT2) are common. A poor metaboliser of an active drug accumulates it (CYP2C9 and warfarin bleeding; DPYD and fluorouracil toxicity; TPMT and azathioprine myelosuppression). A poor metaboliser of a prodrug gets no effect (CYP2C19 and clopidogrel, with higher stent thrombosis after coronary intervention). An ultra-rapid metaboliser of a prodrug can be poisoned by the product (CYP2D6 duplication and codeine in children). The direction of harm is set by [metabolism](../01-pharmacokinetics/drug-metabolism-and-interactions.md); the gene decides who is affected.

2. **Transporter variants change where a drug goes.** The hepatic uptake transporter encoded by SLCO1B1 carries statins into the liver; a reduced-function variant (c.521T>C) raises plasma simvastatin and the risk of myopathy several-fold at higher doses. Because transporters are expressed at the gut, liver, kidney and blood–brain barrier, such variants alter absorption and elimination as well as distribution.

3. **Target variants change the response to a given concentration.** Variants in the vitamin K epoxide reductase gene (VKORC1) alter sensitivity to warfarin independently of CYP2C9, and together the two genes explain roughly a third of the variance in dose requirement. In oncology the target variant is usually somatic, in the tumour rather than the patient: an epidermal growth factor receptor (EGFR) mutation predicts response to EGFR inhibitors, and a KRAS mutation predicts resistance to antibodies against the same receptor. This is why [molecular diagnostics](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/histopathology-cytology-and-molecular-diagnostics.md) precedes [systemic anticancer therapy](../../12-organ-system-specialties/07-oncology/systemic-anticancer-therapy.md).

4. **HLA variants predict the rare immune reactions.** Abacavir hypersensitivity occurs almost only in carriers of HLA-B*57:01; screening before prescribing has nearly eliminated it. Carbamazepine Stevens–Johnson syndrome is strongly associated with HLA-B*15:02, an allele common in Han Chinese and Southeast Asian populations and rare in Europeans; allopurinol severe cutaneous reactions with HLA-B*58:01. These are the clearest cases of a type B [adverse reaction](adverse-drug-reactions-and-pharmacovigilance.md) being made predictable, and they show that susceptibility can be population-specific.

5. **Allele frequencies differ between ancestries because of drift and selection, so the clinical value of a test depends on the population.** CYP2D6 poor metabolisers are ~5–10% of Europeans and under 2% of East Asians; CYP2C19 poor metabolisers are ~2–5% of Europeans and ~15% of East Asians; HLA-B*15:02 ranges from near zero to over 10%. Ancestry is a crude proxy for genotype, and genotype is what matters; the point is that a test's yield, and so its cost-effectiveness, varies by setting, which [health economics](../../15-medicine-in-society/01-health-systems/health-economics-and-priority-setting.md) must weigh.

6. **Most variation in drug response remains non-genetic or polygenic, and the gene is one input among many.** Age halves renal clearance between 30 and 80; renal and hepatic disease, body composition, pregnancy, smoking (CYP1A2 induction), diet, adherence and co-prescribed inhibitors and inducers all move the concentration; disease severity and receptor state move the response. Twin studies suggest heritability of 50–90% for the clearance of some drugs, but for most clinical outcomes single variants explain a few percent, and polygenic scores for drug response are still research tools. A pharmacogenomic result refines a prior; it does not replace monitoring.

7. **Implementation is a problem of information flow, not of biology.** A genotype is fixed for life, so the economic case favours testing once, pre-emptively, for a panel of variants, and storing the result where every future prescription will meet it. Clinical guidelines (the Clinical Pharmacogenetics Implementation Consortium, from 2011, and the Dutch Pharmacogenetics Working Group) translate genotype into dosing advice for a few dozen gene–drug pairs. The limiting steps are electronic records, prescriber awareness and evidence that testing improves outcomes, which randomised trials such as PREPARE (2023) have begun to supply.

## Key concepts

| Term | Meaning |
|---|---|
| Pharmacogenetics / pharmacogenomics | The effect of single gene variants, or of the whole genome, on drug response |
| Metaboliser phenotype | Poor, intermediate, normal, rapid or ultra-rapid activity of a metabolising enzyme, inferred from genotype |
| Star allele | Nomenclature for haplotypes of pharmacogenes (CYP2D6*4 is a common null allele) |
| Germline versus somatic variant | Inherited variant in every cell versus acquired variant in a tumour; both guide drug choice |
| Companion diagnostic | A test required or recommended before prescribing a drug, usually for a tumour marker or an HLA allele |
| HLA association | Strong link between a specific HLA allele and a drug hypersensitivity reaction |
| Pre-emptive panel testing | Genotyping many pharmacogenes once, in advance of any prescription |
| Heritability of drug response | Fraction of variance in response explained by genetic variation; high for clearance, lower for outcomes |

## How it fits

- **Below:** The variants are described in [genomic variation](../../04-genetics-evolution-and-development/01-inheritance/genomic-variation-and-mutation.md), their population distribution in [human variation](../../04-genetics-evolution-and-development/02-evolution/human-evolution-and-variation.md), and the limits of single-gene prediction in [complex traits](../../04-genetics-evolution-and-development/01-inheritance/complex-traits-and-heritability.md). The assumption is that a variant's functional effect is known from biochemistry.
- **Above:** Companion diagnostics are part of [drug development](../05-drug-development-and-toxicology/from-target-to-approval.md); tumour genotyping is the basis of [targeted anticancer therapy](../../12-organ-system-specialties/07-oncology/systemic-anticancer-therapy.md); pre-emptive panels are a test case for [health informatics](../../15-medicine-in-society/01-health-systems/health-informatics-and-artificial-intelligence.md) and the [future of medicine](../../15-medicine-in-society/03-populations-and-the-future/the-future-of-medicine.md).
- **Siblings:** This leaf explains why the [quantal curve](dose-response-and-therapeutic-index.md) is wide and why some [type B reactions](adverse-drug-reactions-and-pharmacovigilance.md) are predictable; it is the genetic half of what [metabolism and interactions](../01-pharmacokinetics/drug-metabolism-and-interactions.md) describes environmentally.

## Common misconceptions

- **"Pharmacogenomic testing will soon personalise every prescription."** For most drugs, non-genetic factors dominate and single variants explain little; the proven gene–drug pairs number in the dozens, not thousands.
- **"Ancestry tells you a patient's metaboliser status."** Allele frequencies differ by population, but every phenotype occurs in every population; only the genotype tells you about the individual.
- **"A tumour's mutation profile is the patient's pharmacogenome."** Somatic variants guide which drug will act on the tumour; germline variants guide how the patient will handle the drug. Both matter and they are different tests.

## Go deeper

- Mary Relling and William Evans, "Pharmacogenomics in the clinic" (*Nature*, 2015): a review of the gene–drug pairs with actionable evidence and the barriers to implementation.
- Jesse Swen and colleagues, "A 12-gene pharmacogenetic panel to prevent adverse drug reactions: an open-label, multicentre, controlled, cluster-randomised crossover implementation study" (*Lancet*, 2023): the PREPARE trial.
- Clinical Pharmacogenetics Implementation Consortium guidelines (cpicpgx.org, from 2011): the primary source for genotype-to-dose translation.
