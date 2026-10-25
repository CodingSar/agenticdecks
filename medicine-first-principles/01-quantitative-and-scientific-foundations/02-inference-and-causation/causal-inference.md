# Causal Inference

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › [Inference and Causation](README.md)
> **Builds on:** [Probability](../01-probability-and-measurement/probability.md), [Regression, adjustment and survival analysis](regression-adjustment-and-survival-analysis.md), [The scientific method and models](../03-systems-and-models/the-scientific-method-and-models.md)
> **Enables:** [Bias, confounding and chance](../../10-epidemiology-and-evidence/01-epidemiology/bias-confounding-and-chance.md), [Randomised controlled trials](../../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md), [Multifactorial disease and risk](../../08-pathology/05-disease-as-process/multifactorial-disease-and-risk.md), [Aetiology, pathogenesis and natural history](../../08-pathology/05-disease-as-process/etiology-pathogenesis-and-natural-history.md)

## Essence

Medicine's useful knowledge is causal: smoking causes lung cancer, this drug lowers mortality, that exposure is safe. Yet almost all data show only association, and association has three explanations besides cause: chance, bias in how the data were gathered, and confounding by a third factor that produces both exposure and outcome. Causal inference is the discipline of saying when, and how confidently, an association can be read as a cause. Its central idea is the counterfactual: the effect of a treatment on a patient is the difference between what happened and what *would have* happened without it, a quantity that can never be observed for one person but can be estimated for a group if the treated and untreated are exchangeable. Randomisation makes them exchangeable by design; every other method tries to make them exchangeable by assumption, and the assumptions are where the arguments live.

## Core tenets

1. **A cause is defined by a counterfactual contrast.** Exposure X causes outcome Y in a population if the frequency of Y would differ had X been different, everything else held fixed. For an individual the untreated outcome is unobservable once they are treated (the fundamental problem of causal inference), so causal effects are average effects over groups: the difference, or ratio, between what happened to the exposed and what would have happened to them unexposed. All methods are ways of estimating that missing second quantity.

2. **Association equals causation only when the compared groups are exchangeable.** If the treated and untreated would have had the same outcomes in the absence of treatment, the observed difference is the causal effect. Confounding is the failure of exchangeability: a factor (age, severity, wealth) that influences both who gets the exposure and who gets the outcome. Patients given a new drug are usually healthier or sicker than those not given it, and no sample size corrects this.

3. **Randomisation produces exchangeability without knowing the confounders.** Assigning exposure by chance makes the groups alike, on average, in every measured and unmeasured factor; the only systematic difference is the treatment. This is why the randomised trial is the reference standard for causal claims about interventions, and why its results overturn observational findings (hormone replacement and heart disease, antioxidant vitamins and cancer, antiarrhythmic drugs after infarction, which increased deaths). It cannot be used for harmful or unmodifiable exposures, and its participants may not resemble the patients to be treated.

4. **Causal diagrams make the assumptions explicit and tell you what to adjust for.** A directed acyclic graph draws each variable as a node and each presumed causal influence as an arrow. A confounder is a common cause of exposure and outcome and must be adjusted for; a mediator lies on the path from exposure to outcome and must not be if the total effect is wanted; a collider is a common *effect* of two variables, and adjusting for it (or selecting on it) manufactures a false association. Studying only hospitalised patients, who are there because of either the exposure or the outcome, is collider bias.

5. **Observational methods estimate causal effects by assumption, and the assumption must be stated.** Adjustment and matching assume all confounders are measured. Instrumental variables use a factor (a gene, a policy, a distance to hospital) that affects exposure but not outcome except through it; Mendelian randomisation uses inherited variants this way and has tested whether low cholesterol or high alcohol intake are causes rather than markers. Each design replaces "we measured everything" with a different, checkable assumption.

6. **Causes are usually components, neither necessary nor sufficient alone.** Most disease is produced by combinations: the tubercle bacillus is necessary for tuberculosis but infects far more people than it sickens; smoking causes lung cancer in about one smoker in six over a lifetime, so it is neither necessary nor sufficient. Rothman's causal pie model pictures a sufficient cause as a set of component causes that together complete the disease; removing any component prevents the cases that needed it. This is why a disease can have a strong genetic cause and still be prevented by changing an exposure.

7. **Judging causation from evidence uses criteria, none decisive.** Hill's considerations (1965) remain the checklist: strength of association, consistency across studies and populations, specificity, temporality (cause precedes effect, the only requirement that is absolute), a biological gradient (dose–response), plausibility, coherence with other knowledge, experimental evidence and analogy. They organise an argument rather than score it. The case for smoking and lung cancer was made this way, against the objection that no trial had been done.

## Key concepts

| Term | Meaning |
|---|---|
| Counterfactual | What would have happened to the same unit under a different exposure |
| Average causal effect | The difference in outcomes had everyone been exposed versus had no one been |
| Exchangeability | Compared groups would have the same outcome distribution if treated alike |
| Confounder | A common cause of exposure and outcome |
| Mediator | A variable on the causal path from exposure to outcome |
| Collider | A common effect of two variables; adjusting for it induces bias |
| Directed acyclic graph | A causal diagram of variables and arrows used to choose adjustment |
| Component, necessary and sufficient cause | Parts that complete a causal pie; one required for all cases; one that alone produces the outcome |
| Hill's considerations | Nine viewpoints for judging whether an association is causal |

## How it fits

- **Below:** counterfactuals are stated as [conditional probabilities](../01-probability-and-measurement/probability.md); adjustment is [regression](regression-adjustment-and-survival-analysis.md) guided by a causal diagram; a causal claim is a [falsifiable model](../03-systems-and-models/the-scientific-method-and-models.md) of the world.
- **Above:** [bias, confounding and chance](../../10-epidemiology-and-evidence/01-epidemiology/bias-confounding-and-chance.md) and [observational designs](../../10-epidemiology-and-evidence/01-epidemiology/observational-study-designs.md) are tenets 2, 4 and 5 as a field; [randomised trials](../../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md) are tenet 3; [aetiology and natural history](../../08-pathology/05-disease-as-process/etiology-pathogenesis-and-natural-history.md) and [multifactorial disease](../../08-pathology/05-disease-as-process/multifactorial-disease-and-risk.md) are tenets 6 and 8 in pathology.
- **Siblings:** [hypothesis testing](hypothesis-testing-and-confidence-intervals.md) rules out chance, the first of the three alternatives to cause; [regression](regression-adjustment-and-survival-analysis.md) is the tool, and this leaf is the rule for using it.

## Common misconceptions

- **"A large, consistent association proves causation."** Confounding can be large and consistent too; hormone replacement therapy's apparent cardiac benefit was both.
- **"Adjusting for more variables is always safer."** Adjusting for a mediator removes the effect being sought; adjusting for a collider creates a false one.

## Go deeper

- Austin Bradford Hill, "The environment and disease: association or causation?" (*Proceedings of the Royal Society of Medicine*, 1965): the considerations, in the author's words.
- Kenneth J. Rothman, *Epidemiology: An Introduction* (2nd ed., 2012): causal pies, confounding and the counterfactual, concisely.
- Miguel A. Hernán and James M. Robins, *Causal Inference: What If* (2020): the rigorous modern treatment, freely available.
