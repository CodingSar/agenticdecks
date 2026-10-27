# 10 Epidemiology and Evidence

> **Layer:** 10 Epidemiology and Evidence
> **Children:** [Epidemiology](01-epidemiology/README.md) · [Evidence-based medicine](02-evidence-based-medicine/README.md) · [Screening and prevention](03-screening-and-prevention/README.md)

## What this area is about

Everything below this layer describes a body: how it is built, how it works, how it fails, and what a drug does to it. None of that tells you how often a disease occurs, whether a risk factor causes it, whether a treatment works, how well a test discriminates, or whether finding disease early helps. Those are questions about populations, answered by counting people and comparing groups, and this layer is the method for answering them. Epidemiology supplies the measures and designs for frequency and cause; evidence-based medicine supplies the experiment (the randomised trial), the appraisal of tests, and the synthesis and grading of the literature; screening and prevention apply both to the hardest case, intervening on the well.

The one abstraction this layer contributes is **the population measure**: incidence, prevalence, relative risk, risk difference, number needed to treat, sensitivity, specificity, likelihood ratio, the reproduction number. Every one is a probability or a ratio of probabilities estimated from a count and a denominator, every one carries sampling error, and every one can be distorted by bias and confounding in ways that more data do not cure. The layer's recurring lesson is that the difference between an association and a cause, or between a test that looks accurate and a test that helps, is a matter of design, not of sample size.

## Why this layer sits here

From below it needs [01 Quantitative and Scientific Foundations](../01-quantitative-and-scientific-foundations/README.md) almost entire: [probability](../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md) and [Bayes](../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md) for frequencies and likelihood ratios, [hypothesis testing and confidence intervals](../01-quantitative-and-scientific-foundations/02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md) for chance, [regression and survival analysis](../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md) for adjustment and prediction, [causal inference](../01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md) for confounding, and [compartment models](../01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md) for epidemics. It needs [07 Microbiology and Immunology](../07-microbiology-and-immunology/README.md) for the [chain of infection](../07-microbiology-and-immunology/01-microbes-and-infection/transmission-and-the-chain-of-infection.md) and [vaccination](../07-microbiology-and-immunology/03-adaptive-immunity/immunological-memory-and-vaccination.md) that infectious disease dynamics rest on, [08 Pathology](../08-pathology/README.md) for [natural history](../08-pathology/05-disease-as-process/etiology-pathogenesis-and-natural-history.md) and [multifactorial risk](../08-pathology/05-disease-as-process/multifactorial-disease-and-risk.md), and [09 Pharmacology](../09-pharmacology-and-therapeutics/README.md) for the [placebo effect](../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/behaviour-change-and-the-placebo-effect.md) that trials must blind against and the [development pipeline](../09-pharmacology-and-therapeutics/05-drug-development-and-toxicology/from-target-to-approval.md) whose trials are the main evidence of treatment effect.

What the layers above need from it is the bridge from population to patient. [11 Clinical Method](../11-clinical-method-and-diagnostics/README.md) is this layer applied to one person: prevalence becomes pre-test probability, a likelihood ratio from an accuracy study moves it, a trial's number needed to treat sets the treatment threshold, a risk score gives the prognosis. Every disease leaf in [12](../12-organ-system-specialties/README.md), [13](../13-acute-perioperative-and-procedural-care/README.md) and [14](../14-life-course-mind-and-integrative-care/README.md) cites risk factors from cohorts, treatments from trials, and screening programmes judged here. [15 Medicine in Society](../15-medicine-in-society/README.md) prices the effect sizes, builds surveillance into health systems, and takes the evidence on social determinants, almost all of it observational, as its starting point.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [01 Epidemiology](01-epidemiology/README.md) | Measures of frequency and association, observational designs, bias and confounding, infectious disease dynamics, surveillance | 01 (probability, inference, models), 07, 08 |
| [02 Evidence-based medicine](02-evidence-based-medicine/README.md) | The randomised trial, diagnostic accuracy, systematic review, grading, research integrity | 01 Epidemiology; 01 Bayes; 09 placebo |
| [03 Screening and prevention](03-screening-and-prevention/README.md) | Levels of prevention, screening biases, risk prediction | Both of the above; 08 natural history |

```
   layer 01: probability, inference, causal diagrams, compartment models
                     |
   01 Epidemiology:  count --> compare --> rule out bias, confounding, chance
                     |                                   \
   02 Evidence:      randomise (trials)    characterise tests (2x2)
                     synthesise (reviews)  grade (guidelines)  protect (integrity)
                     |
   03 Prevention:    act earlier on the natural history; screen; stratify by risk
                     |
   layer 11: one patient (pre-test probability, likelihood ratio, threshold)
   layers 12-15: specialties, systems, society
```

Read epidemiology first: nothing in the other two parents is intelligible without incidence, relative risk, confounding and the distinction between association and cause. Evidence-based medicine then adds the one design that settles cause by experiment and the machinery for appraising and combining studies. Screening and prevention is placed last because it needs all of it: the natural history from pathology, the test characteristics from accuracy studies, the trial as the only valid judge, and the regression models of layer 01 turned into risk scores.

## Connections to neighbouring layers

- **[01 Quantitative and Scientific Foundations](../01-quantitative-and-scientific-foundations/README.md):** the mathematics this layer is written in. Where 01 defines a confidence interval or a confounder abstractly, this layer shows what each does to a study of real people.
- **[07 Microbiology and Immunology](../07-microbiology-and-immunology/README.md):** infectious disease dynamics is transmission biology and immunity expressed as a population model; herd immunity is immunological memory counted across a population.
- **[08 Pathology](../08-pathology/README.md):** the natural history of disease is the timeline on which prevention levels, lead time and sojourn time are marked; multifactorial causation is why risk is continuous and thresholds are value judgements.
- **[09 Pharmacology and Therapeutics](../09-pharmacology-and-therapeutics/README.md):** pharmacology says what a drug does; this layer says whether it works, through trials, and whether it is safe, through pharmacovigilance built on observational designs.
- **[11 Clinical Method and Diagnostics](../11-clinical-method-and-diagnostics/README.md):** the direct customer. Bedside reasoning is Bayesian updating with the prevalences, likelihood ratios and effect sizes produced here.
- **[12 Organ-system Specialties](../12-organ-system-specialties/README.md):** each specialty's evidence base is a set of cohorts and named trials appraised by the standards of this layer; each specialty's screening programme is judged by its biases.
- **[15 Medicine in Society](../15-medicine-in-society/README.md):** surveillance becomes public health infrastructure, effect sizes become cost-effectiveness ratios, and the observational evidence on inequality becomes policy.

## Connections across layers

This layer is the hinge between the biological half of the tree and the clinical and social half. Below it, medicine is mechanism; above it, medicine is decision. It supplies the quantities in which decisions are stated and the standards by which the evidence for them is judged, and it carries one warning upward: that every number it produces is an estimate from a sample, exposed to bias, and valid for the population it came from.

## Cross-cutting threads

- [Probability and uncertainty](../CROSS-CUTTING.md#probability-and-uncertainty): the layer's native language; every measure is an estimated probability with an interval.
- [Cause and mechanism](../CROSS-CUTTING.md#cause-and-mechanism): from association to cause via design, Bradford Hill and randomisation.
- [Harm and benefit](../CROSS-CUTTING.md#harm-and-benefit): number needed to treat and to harm, overdiagnosis, the asymmetry of preventing disease in the well.
- [Feedback and homeostasis](../CROSS-CUTTING.md#feedback-and-homeostasis): epidemic dynamics as a feedback loop between prevalence and incidence.
- [Time courses](../CROSS-CUTTING.md#time-courses): incubation, latency, natural history, lead time, follow-up.
- [Dose–response](../CROSS-CUTTING.md#dose-response): biological gradient as evidence of cause; thresholds on continuous risk.
- [The host and its environment](../CROSS-CUTTING.md#the-host-and-its-environment): exposures, behaviour and social position as the independent variables of population health.
