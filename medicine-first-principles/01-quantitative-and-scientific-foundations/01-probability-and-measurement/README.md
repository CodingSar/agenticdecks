# Probability and Measurement

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › Probability and Measurement
> **Children:** [Measurement error and biological variation](measurement-error-and-biological-variation.md) · [Probability](probability.md) · [Distributions and descriptive statistics](distributions-and-descriptive-statistics.md) · [Bayesian reasoning](bayesian-reasoning.md)

## What this area is about

Medicine acts on numbers it cannot trust completely: a blood pressure that varies by the minute, a laboratory value with a 5% error, a test that misses one case in ten, a prevalence estimated from a sample. This area answers: *how does one describe, quantify and reason with uncertainty so that a single patient's result can be read correctly?* It supplies the vocabulary (probability, distribution, standard deviation, likelihood ratio) that every later layer uses when it says "normal", "abnormal", "risk" or "likely".

The unifying idea is **variation is the rule, and every number is a sample from it**. Biology varies between people and within one person over time; instruments add error; disease shifts a distribution rather than replacing it. A measurement is therefore evidence, not truth, and the right response to evidence is to update a probability, not to declare a fact. Probability gives the rules, distributions give the shapes, measurement theory separates signal from noise, and Bayesian reasoning closes the loop by turning a noisy observation into a revised belief about the patient.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Probability](probability.md) | The rules of uncertainty: axioms, independence, conditional probability, odds, expected value | Nothing (root) |
| [Distributions and descriptive statistics](distributions-and-descriptive-statistics.md) | The shapes probability takes over values: normal, log-normal, binomial, Poisson; mean, SD, SE, percentiles | Probability |
| [Measurement error and biological variation](measurement-error-and-biological-variation.md) | Precision, bias, within-person variation, reference ranges, agreement, regression to the mean | Probability, distributions |
| [Bayesian reasoning](bayesian-reasoning.md) | Updating belief with evidence: prior, likelihood ratio, posterior, thresholds | Probability, distributions |

```
   probability (rules) ──► distributions (shapes)
         │                       │
         │              ┌────────┴────────┐
         ▼              ▼                 ▼
   Bayesian reasoning   measurement error & biological variation
   (one patient,        (one measurement, how much to trust)
    how to update)
         │                       │
         └──────► 10 Epidemiology, 11 Clinical Method ◄──────┘
```

Read probability first; it is short and everything else uses its rules. Distributions come next, because the normal curve and the standard error are what the other two leaves assume. Measurement error and Bayesian reasoning can be read in either order: the first says how much a number should be believed, the second says what to do with a number once believed to that extent. Together they describe the two halves of reading a test result: is this value real, and what does it mean for this patient?

## Connections to sibling areas

- **[Inference and causation](../02-inference-and-causation/README.md):** that area asks what a sample says about a population and whether an association is causal. It rests on the standard error and the sampling distributions introduced here, and the Bayesian view of evidence introduced here is its alternative to significance testing.
- **[Systems and models](../03-systems-and-models/README.md):** feedback loops, compartments and signals are deterministic models; this area supplies the noise that real measurements of them carry, and the scientific method leaf there explains why probability statements are what models predict.

## Connections across layers

This area has nothing beneath it; it is half of the formal root. Above, it is used everywhere a number is interpreted. [00 Physical and Chemical Foundations](../../00-physical-and-chemical-foundations/README.md) borrows probability for entropy and the log-normal for allometry. [04 Genetics](../../04-genetics-evolution-and-development/README.md) is probability applied to alleles and the normal distribution applied to polygenic traits. [06 Physiology](../../06-physiology/README.md) supplies the within-person variation that homeostasis produces. [10 Epidemiology and Evidence](../../10-epidemiology-and-evidence/README.md) measures prevalence, sensitivity and specificity, the inputs to Bayes. [11 Clinical Method and Diagnostics](../../11-clinical-method-and-diagnostics/README.md) is this area at the bedside: reference ranges, pre-test probability, thresholds and the cognitive biases that distort them. [15 Medicine in Society](../../15-medicine-in-society/README.md) inherits the base-rate problem whenever an algorithm screens a population.

## Cross-cutting threads

- [Probability and uncertainty](../../CROSS-CUTTING.md#probability-and-uncertainty): the whole area; medicine reasons under uncertainty at every level.
- [Signalling and information](../../CROSS-CUTTING.md#signalling-and-information): a test result is a signal with noise, and its information content is its likelihood ratio.
- [Harm and benefit](../../CROSS-CUTTING.md#harm-and-benefit): test and treatment thresholds weigh the harm of missing disease against the harm of acting on a false positive.
- [Time-courses](../../CROSS-CUTTING.md#time-courses): within-person variation and regression to the mean are what repeated measurements show over time.
