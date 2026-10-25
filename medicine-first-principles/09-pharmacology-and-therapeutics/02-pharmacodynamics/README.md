# Pharmacodynamics

> **Layer:** [09 Pharmacology and Therapeutics](../README.md) › Pharmacodynamics
> **Children:** [Receptor theory, agonists and antagonists](receptor-theory-agonists-and-antagonists.md) · [Dose–response and therapeutic index](dose-response-and-therapeutic-index.md) · [Tolerance, dependence and withdrawal](tolerance-dependence-and-withdrawal.md) · [Adverse drug reactions and pharmacovigilance](adverse-drug-reactions-and-pharmacovigilance.md) · [Pharmacogenomics and individual variation](pharmacogenomics-and-individual-variation.md)

## What this area is about

Pharmacodynamics asks what a drug does to the body once it is there: how a concentration at a target becomes an effect, how the size of that effect depends on concentration, how it changes with time and repeated exposure, how it differs between people, and when it becomes harm. Where pharmacokinetics is the physics of membranes and the physiology of two organs, pharmacodynamics is the chemistry of binding and the biology of the signalling systems that drugs borrow. Almost every drug is an impostor: it occupies a site built for an endogenous ligand, substrate or ion, and the body's response is whatever that site normally does, run up or down.

The unifying idea is the **dose–response relationship**, derived from the law of mass action and read in two forms: the graded curve of one system and the quantal curve of a population. Everything else in the area is a modification of that curve: antagonists shift it, tolerance moves it over time, genes and disease spread it across people, and the toxicity curve lying close beside it is what makes a drug dangerous.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Receptor theory, agonists and antagonists](receptor-theory-agonists-and-antagonists.md) | The equilibrium chemistry of binding: affinity, efficacy, the kinds of ligand and antagonism | Receptors and ligands, chemical equilibrium |
| [Dose–response and therapeutic index](dose-response-and-therapeutic-index.md) | The curve for one system and for a population; the margin between benefit and harm | Receptor theory, distributions, elimination kinetics |
| [Tolerance, dependence and withdrawal](tolerance-dependence-and-withdrawal.md) | The curve drifting over days under feedback; what happens when the drug is removed | Receptor theory, feedback, signal termination |
| [Adverse drug reactions and pharmacovigilance](adverse-drug-reactions-and-pharmacovigilance.md) | The toxicity curve, the immune reactions outside it, and how rare harms are found after approval | Dose–response, hypersensitivity, causal inference |
| [Pharmacogenomics and individual variation](pharmacogenomics-and-individual-variation.md) | Why the population curve is wide; the inherited and acquired sources of variation | Genomic variation, metabolism, dose–response |

```
   concentration at target  --(receptor theory)-->  graded effect
            |                                           |
   (kinetics sets this)                   population of thresholds
                                                        |
                                        quantal curves: efficacy | toxicity
                                                 /            |           \
                                   shifts in time        rare immune      spread by
                                 (tolerance, rebound)    harms (ADR)    genes, age, disease
```

Read receptor theory first; it supplies the vocabulary (agonist, antagonist, affinity, efficacy, potency) and the equation that every later leaf assumes. Dose–response turns it into population terms and defines the therapeutic index. The last three leaves are three ways the simple curve fails to describe a real patient: the curve moves with time, the harm curve is sometimes not a curve at all but a rare immune event, and the curve is a different curve for each genotype.

## Connections to sibling areas

- **[Pharmacokinetics](../01-pharmacokinetics/README.md):** supplies the concentration that dynamics responds to. The two meet in the therapeutic window: kinetics decides how far concentration swings, dynamics how wide the safe band is. Kinetic tolerance (enzyme induction) and pharmacogenomic variation in metabolism belong to both.
- **[Drug classes by mechanism](../03-drug-classes-by-mechanism/README.md):** every class is an application of receptor theory to one physiological system; the drug-class leaves assume the reader knows what a partial agonist or a competitive antagonist is and spend their words on the system instead.
- **[Non-drug therapeutics](../04-non-drug-therapeutics/README.md):** radiotherapy has its own dose–response curves (tumour control and normal-tissue complication) with the same logic of a therapeutic ratio; the placebo effect is a response with no pharmacological dose and so the cleanest test of what "effect" means.
- **[Drug development and toxicology](../05-drug-development-and-toxicology/README.md):** target validation is receptor theory applied to a new protein; phase II trials find the dose on the curve; toxicology is the far right end of the quantal curve; pharmacovigilance is the last, open-ended phase of development.

## Connections across layers

From below, the area takes the [receptors](../../02-biochemistry-and-molecular-biology/04-cell-signalling/receptors-and-ligands.md) and [signal termination](../../02-biochemistry-and-molecular-biology/04-cell-signalling/signal-amplification-integration-and-termination.md) of cell signalling, [equilibrium chemistry](../../00-physical-and-chemical-foundations/02-chemistry-of-life/kinetics-equilibrium-and-catalysis.md), the [distributions](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/distributions-and-descriptive-statistics.md) and [feedback](../../01-quantitative-and-scientific-foundations/03-systems-and-models/feedback-and-control.md) of the quantitative layer, [hypersensitivity](../../07-microbiology-and-immunology/04-immunity-in-disease/hypersensitivity-and-allergy.md) from immunology and [genomic variation](../../04-genetics-evolution-and-development/01-inheritance/genomic-variation-and-mutation.md) from genetics.

Upward, it gives [randomised trials](../../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md) their dose and their harm outcomes, [laboratory medicine](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/clinical-chemistry-and-reference-ranges.md) its therapeutic ranges, [oncology](../../12-organ-system-specialties/07-oncology/README.md) its companion diagnostics, [psychiatry](../../14-life-course-mind-and-integrative-care/03-psychiatry/README.md) the distinction between dependence and addiction, [geriatrics](../../14-life-course-mind-and-integrative-care/04-geriatrics-and-palliative-care/README.md) the arithmetic of polypharmacy, and [patient safety](../../15-medicine-in-society/01-health-systems/patient-safety-and-quality-improvement.md) its largest single category of preventable harm.

## Cross-cutting threads

- [Dose–response](../../CROSS-CUTTING.md#dose-response): the area's organising principle, in graded and quantal form.
- [Specificity and recognition](../../CROSS-CUTTING.md#specificity-and-recognition): affinity is molecular recognition; the cost of imperfect recognition is the side effect at the second receptor.
- [Feedback and homeostasis](../../CROSS-CUTTING.md#feedback-and-homeostasis): tolerance and withdrawal are feedback loops that have absorbed the drug into the set point.
- [Harm and benefit](../../CROSS-CUTTING.md#harm-and-benefit): the therapeutic index and the whole of pharmacovigilance.
- [Probability and uncertainty](../../CROSS-CUTTING.md#probability-and-uncertainty): the quantal curve is a distribution, the rule of three bounds what trials can see, and a genotype refines a prior.
