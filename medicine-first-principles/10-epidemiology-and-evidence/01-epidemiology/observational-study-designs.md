# Observational study designs

> **Layer:** [10 Epidemiology and Evidence](../README.md) › [Epidemiology](README.md)
> **Builds on:** [Measures of frequency and association](measures-of-frequency-and-association.md), [Causal inference](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md), [Regression, adjustment and survival analysis](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md)
> **Enables:** [Bias, confounding and chance](bias-confounding-and-chance.md), [Adverse drug reactions and pharmacovigilance](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/adverse-drug-reactions-and-pharmacovigilance.md), [Social determinants and health inequity](../../15-medicine-in-society/03-populations-and-the-future/social-determinants-and-health-inequity.md)

## Essence

Most questions in medicine cannot be answered by experiment. Nobody can randomise people to smoke, to be poor or to carry a gene, and rare harms of a drug appear only after a million people have taken it. Observational designs answer such questions by choosing *whom to observe and in what order*: start with exposure and watch for disease (cohort), start with disease and look back for exposure (case-control), or measure both at once (cross-sectional). Each is a different trade-off between cost, speed, what it can measure and which errors it invites. The unifying idea is that a design is a sampling scheme, and what you sample on determines which measure of association you can estimate and which biases you must defend against.

## Core tenets

1. **The cohort study follows exposure forward, so it estimates incidence directly.** Assemble people free of the outcome, record exposure, follow them, count outcomes. Because denominators are known it yields rates, risks, relative risks and risk differences, and it can study many outcomes of one exposure. Its cost is time: the British Doctors Study (Doll and Hill, from 1951) needed decades to show that smokers died of lung cancer at many times the rate of non-smokers. Loss to follow-up that differs by exposure or outcome distorts the result.

2. **The case-control study samples on outcome, so it can estimate only an odds ratio.** Take people with the disease, choose comparable people without it, compare past exposure. Because the investigator fixes the ratio of cases to controls, disease frequency is unknown and risks cannot be computed; but the odds ratio for exposure equals the odds ratio for disease, and for a rare disease approximates the relative risk. It is fast and efficient for rare diseases and long latencies, which is why it linked thalidomide to limb defects (1961).

3. **Controls must represent the population that produced the cases.** The study asks "what was the exposure frequency in the population from which these cases came?" Controls estimate that frequency, so they must come from the same source population and be chosen independently of exposure. Hospital controls, friend controls and population controls each fail in characteristic ways; a control group chosen for convenience is the design's commonest fatal flaw.

4. **Cross-sectional studies measure prevalence and cannot order cause and effect.** Measuring exposure and disease at one moment yields prevalence, which is what health surveys need. But the association may run either way (does low income cause illness, or illness low income?), and it over-represents long-lasting cases because prevalence is incidence times duration. It is the right design for burden and the wrong one for cause.

5. **Ecological studies compare groups, not people.** Correlating national fat intake with national breast-cancer rates is cheap and suggestive, but an association between group averages need not hold within individuals; the people eating the fat may not be the people getting the cancer (the ecological fallacy). Group-level data are right for exposures that act on groups (policies, air quality) and dangerous as evidence of individual causation.

6. **Hybrid designs trade some features for others.** A *nested case-control* study draws controls from inside an existing cohort, gaining its unbiased exposure measurement at case-control cost. A *case-crossover* design uses each person as their own control at a different time, removing stable confounders, and suits transient exposures with acute effects. *Target-trial emulation* analyses observational records as though they were the randomised trial one would have run, forcing explicit choices about eligibility, time zero and comparator.

7. **Design chooses the biases you will face; analysis can only partly repair them.** Cohorts suffer from loss to follow-up and confounding; case-control studies from recall and control selection; cross-sectional studies from reverse causation. [Regression](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/regression-adjustment-and-survival-analysis.md) adjusts for confounders that were measured, never for those that were not. This is why [evidence grading](../02-evidence-based-medicine/grading-evidence-and-guidelines.md) ranks designs before results.

## Key concepts

| Term | Meaning |
|---|---|
| Cohort study | Follows exposed and unexposed people forward from exposure to outcome |
| Case-control study | Compares past exposure in people with and without the outcome |
| Cross-sectional study | Measures exposure and outcome in a population at one time |
| Ecological study | Compares exposure and outcome across groups using group-level data |
| Nested case-control | Case-control sampling within a defined cohort |
| Case-crossover | Each case serves as their own control at a different time |
| Prospective versus retrospective | Whether data are collected as events unfold or reconstructed from records |
| Target-trial emulation | Designing an observational analysis to mimic the trial that would answer the question |
| Source population | The population that generated the cases and from which controls must be drawn |

## How it fits

- **Below:** which design identifies a causal effect, and under what untestable assumptions, is the subject of [causal inference](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md); the measures each design yields are those of [measures of frequency and association](measures-of-frequency-and-association.md).
- **Above:** [pharmacovigilance](../../09-pharmacology-and-therapeutics/02-pharmacodynamics/adverse-drug-reactions-and-pharmacovigilance.md) depends on cohort and case-control designs because trials are too small for rare harms; the evidence for [social determinants of health](../../15-medicine-in-society/03-populations-and-the-future/social-determinants-and-health-inequity.md) is almost entirely observational; [health informatics](../../15-medicine-in-society/01-health-systems/health-informatics-and-artificial-intelligence.md) supplies the record-based cohorts.
- **Siblings:** [bias, confounding and chance](bias-confounding-and-chance.md) catalogues the errors each design invites; the [randomised trial](../02-evidence-based-medicine/randomized-controlled-trials.md) in the neighbouring parent removes confounding by construction and is used whenever ethics and feasibility allow.

## Common misconceptions

- **"Retrospective means case-control and prospective means cohort."**: the terms describe when data were collected, not the sampling scheme; a cohort assembled from old records still follows exposure forward in logical time.
- **"Observational studies are always inferior to trials."**: for rare harms, long latencies and exposures that cannot be assigned they are the only evidence there will be. The question is whether the design fits the question and whether confounding is plausible.
- **"A case-control study can tell you how common the disease is."**: the investigator chose how many cases and controls to include, so disease frequency is a property of the design, not the population.

## Go deeper

- Kenneth J. Rothman, Sander Greenland and Timothy L. Lash, *Modern Epidemiology* (3rd ed., 2008): the definitive treatment of design and its logic.
- Richard Doll and A. Bradford Hill, "The mortality of doctors in relation to their smoking habits", *British Medical Journal* (1954): the cohort study that made the method.
- Miguel A. Hernán and James M. Robins, "Using big data to emulate a target trial when a randomized trial is not available", *American Journal of Epidemiology* (2016): the modern framework for observational causal questions.
