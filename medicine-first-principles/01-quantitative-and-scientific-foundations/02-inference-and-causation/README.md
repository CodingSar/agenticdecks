# Inference and Causation

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › Inference and Causation
> **Children:** [Hypothesis testing and confidence intervals](hypothesis-testing-and-confidence-intervals.md) · [Regression, adjustment and survival analysis](regression-adjustment-and-survival-analysis.md) · [Causal inference](causal-inference.md)

## What this area is about

A study observes a few hundred patients; medicine wants a rule for millions. A drug appears to help; medicine wants to know whether it *caused* the help. This area answers: *how does one reason from a sample to a population, from many variables to the effect of one, and from association to cause?* It is the logic behind every claim that a treatment works, a risk factor matters or an exposure is safe, and the reason those claims are argued in terms of intervals, adjusted ratios and trial design.

The unifying idea is **a finding has four explanations, and the job is to eliminate three**. Any association can be due to chance, to bias in how the data were collected, to confounding by a third factor, or to cause. Hypothesis testing and confidence intervals deal with chance. Regression and adjustment deal with measured confounders and produce the estimates themselves. Causal inference deals with bias and confounding as a whole, states the assumptions under which cause can be claimed, and explains why randomisation is the one design that needs the fewest.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Hypothesis testing and confidence intervals](hypothesis-testing-and-confidence-intervals.md) | From sample to population: sampling distributions, intervals, p-values, power, multiplicity | [Distributions](../01-probability-and-measurement/distributions-and-descriptive-statistics.md) |
| [Regression, adjustment and survival analysis](regression-adjustment-and-survival-analysis.md) | Many variables at once: coefficients, odds and hazard ratios, adjustment, censoring, prediction | Hypothesis testing, [exponential processes](../03-systems-and-models/compartment-models-and-exponential-processes.md) |
| [Causal inference](causal-inference.md) | From association to cause: counterfactuals, exchangeability, confounders and colliders, randomisation, component causes | Regression, [probability](../01-probability-and-measurement/probability.md) |

```
   observed association
          │
          ├── chance?        → hypothesis testing & confidence intervals
          ├── confounding?   → regression & adjustment (measured factors)
          ├── bias / design? → causal inference (diagrams, randomisation, instruments)
          │
          └── cause          → mechanism (00, 02–08) + intervention (09–14)
```

Read them in order. Hypothesis testing gives the uncertainty attached to any estimate. Regression produces the estimates that matter in practice (an adjusted hazard ratio, a risk score) and introduces survival data. Causal inference then stands back and asks what those estimates can mean: which variables should have been in the model, which must not have been, and when a trial is the only answer. The first two leaves are statistics; the third is epistemology with statistics as its tool.

## Connections to sibling areas

- **[Probability and measurement](../01-probability-and-measurement/README.md):** supplies the sampling distributions, the standard error and the Bayesian alternative to significance testing. Measurement error there becomes regression dilution and misclassification bias here; regression to the mean there is why a control group is needed here.
- **[Systems and models](../03-systems-and-models/README.md):** the scientific method leaf states what it means for a hypothesis to be falsifiable, which is what a null hypothesis is; compartment models supply the constant hazard that makes survival exponential; feedback and nonlinear dynamics warn that a regression coefficient from a system with loops may not describe what happens when one intervenes.

## Connections across layers

This area has nothing beneath it. Above, it is the method of [10 Epidemiology and Evidence](../../10-epidemiology-and-evidence/README.md) almost in its entirety: study designs are strategies for exchangeability, randomised trials are tenet 3 of causal inference institutionalised, meta-analysis pools confidence intervals, and bias and confounding are its named enemies. [08 Pathology](../../08-pathology/README.md) uses component causes to describe aetiology and multifactorial disease. [09 Pharmacology](../../09-pharmacology-and-therapeutics/README.md) establishes that drugs work through the trials these methods design. [11 Clinical Method](../../11-clinical-method-and-diagnostics/README.md) uses regression-based prognostic scores and reads trial results into one patient's decision. [15 Medicine in Society](../../15-medicine-in-society/README.md) judges health policy, inequality and safety interventions by the same logic, usually without the luxury of randomisation.

## Cross-cutting threads

- [Cause and mechanism](../../CROSS-CUTTING.md#cause-and-mechanism): the area's central theme; from association through confounding to component causes.
- [Probability and uncertainty](../../CROSS-CUTTING.md#probability-and-uncertainty): every estimate carries an interval; every claim is provisional.
- [Harm and benefit](../../CROSS-CUTTING.md#harm-and-benefit): trials measure both, and the balance is an effect size with an interval, not a p-value.
- [Dose–response](../../CROSS-CUTTING.md#dose-response): a biological gradient is one of Hill's considerations and a regression slope.
- [Time-courses](../../CROSS-CUTTING.md#time-courses): survival curves and hazards describe how outcomes unfold over time.
