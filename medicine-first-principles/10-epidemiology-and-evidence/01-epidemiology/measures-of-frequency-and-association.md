# Measures of frequency and association

> **Layer:** [10 Epidemiology and Evidence](../README.md) › [Epidemiology](README.md)
> **Builds on:** [Probability](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md), [Distributions and descriptive statistics](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/distributions-and-descriptive-statistics.md), [Multifactorial disease and risk](../../08-pathology/05-disease-as-process/multifactorial-disease-and-risk.md)
> **Enables:** [Randomized controlled trials](../02-evidence-based-medicine/randomized-controlled-trials.md), [Risk prediction and stratification](../03-screening-and-prevention/risk-prediction-and-stratification.md), [Using tests, pre-test probability and thresholds](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md), [Health economics and priority setting](../../15-medicine-in-society/01-health-systems/health-economics-and-priority-setting.md)

## Essence

Epidemiology counts. Before anyone can ask whether smoking causes lung cancer or whether a drug prevents stroke, someone must say how often the disease occurs, in whom, and how that frequency differs between people with and without an exposure. Two kinds of number do this: **measures of frequency** (how much disease there is: prevalence, incidence, mortality) and **measures of association** (how one group's frequency compares with another's: ratios and differences). Every number in a trial, a guideline or a screening programme is one of these. The idea that organises them is that a frequency is a probability estimated from a count divided by the population and time that could have produced it.

## Core tenets

1. **Every frequency needs a numerator, a denominator and a time.** A count of cases means nothing without the population it came from and the period over which it was collected. Prevalence is the proportion of a population with the condition at a point in time (cases / people). Incidence is the rate at which new cases arise (new cases / person-time at risk). Quoting a numerator alone ("300 deaths") is the commonest error in public discussion of disease.

2. **Prevalence is incidence multiplied by duration.** In a steady state with uncommon disease, prevalence ≈ incidence rate × mean duration. A disease can be prevalent because it is common or because it lasts long. Insulin made type 1 diabetes prevalent by making it chronic rather than fatal; a rapidly fatal cancer has high incidence and low prevalence. So a therapy that prolongs life without curing raises prevalence, and prevalence is a poor measure of risk.

3. **Risk and rate are different denominators for the same event.** *Cumulative incidence* (risk) is new cases divided by people at risk at the start, a probability over a stated period. An *incidence rate* divides by person-time (per 1,000 person-years), so people who leave, die or join part-way contribute what they contributed. Rates handle variable follow-up; risks are what a patient understands. For a short period and a rare outcome the two are numerically close.

4. **Association is a comparison, and there are two ways to compare: divide or subtract.** Take 1,000 exposed people with 50 cases and 1,000 unexposed with 20:

   | | Disease | No disease | Total | Risk |
   |---|---|---|---|---|
   | Exposed | 50 | 950 | 1,000 | 0.050 |
   | Unexposed | 20 | 980 | 1,000 | 0.020 |

   The **relative risk** is 0.050 / 0.020 = 2.5. The **risk difference** is 0.050 − 0.020 = 0.030, or 3 extra cases per 100 exposed. The ratio says how strongly exposure is linked to disease and is what causal research reports; the difference says how much disease the exposure actually adds and is what decisions need.

5. **Odds ratios approximate relative risks only when the outcome is rare.** Odds are cases / non-cases. In the table the odds ratio is (50/950) / (20/980) = 2.58, close to 2.5 because 5% is rare. With a 50% outcome the two diverge badly. Odds ratios are used because case-control studies and logistic regression can estimate nothing else; reporting an odds ratio of 4 as "four times the risk" overstates a common outcome.

6. **The inverse of the risk difference is the number needed to treat.** If a treatment lowers five-year mortality from 10% to 8%, the absolute risk reduction is 2 percentage points and the **number needed to treat** (NNT) is 1 / 0.02 = 50. The relative risk reduction is 20% both here and when mortality falls from 1% to 0.8%, where the NNT is 500. The ratio is roughly portable between populations of different baseline risk; the difference and the NNT are not, and they are what the patient experiences.

7. **Attributable fractions say how much disease an exposure explains.** Among the exposed the fraction is (RR − 1) / RR; with RR 2.5, 60% of cases in exposed people are attributable. The *population* attributable fraction also depends on how common the exposure is: a weak but universal exposure (air pollution) can account for more cases than a strong but rare one, which is why population and individual [prevention](../03-screening-and-prevention/levels-of-prevention.md) point to different targets.


## Key concepts

| Term | Meaning |
|---|---|
| Prevalence | Proportion of a defined population with the condition at a point in time |
| Incidence rate | New cases per unit of person-time at risk |
| Cumulative incidence (risk) | Probability that a person free of disease at baseline develops it over a stated period |
| Relative risk | Risk in the exposed divided by risk in the unexposed |
| Odds ratio | Odds of disease in one group divided by the odds in the other |
| Risk difference | Risk in the exposed minus risk in the unexposed; the absolute risk reduction of a treatment |
| Number needed to treat (NNT) | 1 / absolute risk reduction; its mirror for harms is the number needed to harm |
| Attributable fraction | Share of cases that would not have occurred without the exposure |
| Standardisation | Removing the effect of a differing age structure from a comparison of rates |

## How it fits

- **Below:** these are the [probabilities](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md) of layer 01 estimated from counts, with the sampling variation of any count; the picture of disease as many component causes each raising risk comes from [multifactorial disease and risk](../../08-pathology/05-disease-as-process/multifactorial-disease-and-risk.md).
- **Above:** a [trial](../02-evidence-based-medicine/randomized-controlled-trials.md) reports a relative risk and an NNT; prevalence is the [pre-test probability](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md) a clinician starts from; cost per outcome averted in [health economics](../../15-medicine-in-society/01-health-systems/health-economics-and-priority-setting.md) is a price multiplied by an NNT.
- **Siblings:** [observational study designs](observational-study-designs.md) decide which measures a study can estimate (a case-control study yields only odds ratios); [bias, confounding and chance](bias-confounding-and-chance.md) explains why an association may not be causal; [infectious disease dynamics](infectious-disease-dynamics.md) adds the measures peculiar to transmissible disease.

## Common misconceptions

- **"A relative risk of 2 means a big risk."**: it means twice a baseline that may be tiny. The risk difference, not the ratio, measures what is at stake for one person.
- **"Prevalence tells you how dangerous a disease is."**: it reflects duration as much as occurrence; better treatment that keeps people alive raises prevalence while lowering mortality.
- **"An odds ratio is a relative risk."**: only when the outcome is uncommon in both groups; for common outcomes it exaggerates the association.

## Go deeper

- Kenneth J. Rothman, *Epidemiology: An Introduction* (2nd ed., 2012): the clearest short account of measures and their logic.
- Leon Gordis, *Epidemiology* (6th ed., 2018): the standard textbook, with many worked tables.
- Geoffrey Rose, "Sick individuals and sick populations", *International Journal of Epidemiology* (1985): why population attributable fractions and individual relative risks lead to different strategies.
