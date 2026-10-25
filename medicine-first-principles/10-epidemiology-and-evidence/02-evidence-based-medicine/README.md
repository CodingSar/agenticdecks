# Evidence-based medicine

> **Layer:** [10 Epidemiology and Evidence](../README.md) › Evidence-based medicine
> **Children:** [Randomized controlled trials](randomized-controlled-trials.md) · [Diagnostic accuracy studies](diagnostic-accuracy-studies.md) · [Systematic reviews and meta-analysis](systematic-reviews-and-meta-analysis.md) · [Grading evidence and guidelines](grading-evidence-and-guidelines.md) · [Research integrity and publication bias](research-integrity-and-publication-bias.md)

## What this area is about

Epidemiology asks what causes disease; evidence-based medicine asks what to do about it, and how sure we can be. Its questions are the ones a clinician faces: does this treatment work, how well does this test discriminate, what does the whole literature say, how much should a recommendation be trusted, and can the literature itself be believed? Each child answers one of them with a specific research design or appraisal method. The field exists because, for most of medicine's history, the answers came from authority and anecdote, and because the methods of layer 01 and the epidemiology parent make it possible to replace them with measurement.

The unifying idea is **controlled comparison, then honest synthesis**. A treatment effect is the difference between what happened and what would have happened otherwise, and only a randomised comparison estimates that counterfactual without assumptions about who got treated. A test's value is how much it changes a probability, measured against a reference standard. Single studies are noisy, so the unit of evidence is the systematic review. And every step is only as good as the completeness and honesty of what was reported, which is why integrity is a child of this parent and not a footnote.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Randomized controlled trials](randomized-controlled-trials.md) | The experiment that removes confounding; the design for questions of treatment | [Bias, confounding and chance](../01-epidemiology/bias-confounding-and-chance.md) |
| [Diagnostic accuracy studies](diagnostic-accuracy-studies.md) | The 2×2 table, sensitivity, specificity and likelihood ratios; the design for questions of testing | [Bayesian reasoning](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md) |
| [Systematic reviews and meta-analysis](systematic-reviews-and-meta-analysis.md) | Pooling all the evidence on a question, with heterogeneity and risk of bias made explicit | Trials; diagnostic studies |
| [Grading evidence and guidelines](grading-evidence-and-guidelines.md) | Rating certainty per outcome and turning it into recommendations of stated strength | Reviews |
| [Research integrity and publication bias](research-integrity-and-publication-bias.md) | Why the literature overstates effects, and the practices that keep it honest | All of the above |

```
   question of treatment  -->  randomised trial  --\
                                                    >--> systematic review --> grade certainty --> guideline
   question of testing    -->  accuracy study    --/              ^
                                                                  |
                              registration, full reporting, independence (integrity)
```

Read trials first; they define what a fair comparison is, and every other child either imitates them (accuracy studies with blinded reference standards), combines them (reviews), judges them (grading) or protects them (integrity). Diagnostic accuracy studies stand slightly apart: they are observational, their output is a likelihood ratio rather than an effect size, and they are the direct input to the bedside reasoning of layer 11.

## Connections to sibling areas

- **[Epidemiology](../01-epidemiology/README.md):** supplies the measures (relative risk, number needed to treat, odds ratio) in which trial results are expressed, the catalogue of biases that trial design defends against, and the observational designs that answer the questions trials cannot (rare harms, long-term effects, unassignable exposures). A trial is epidemiology with the exposure assigned by lot.
- **[Screening and prevention](../03-screening-and-prevention/README.md):** screening programmes are the hardest case for this parent: their benefit can only be shown by randomised trials of invitation to screening with mortality as the outcome, because every observational measure of screening is inflated by lead-time and length bias, and their tests are judged by the accuracy methods here at a prevalence low enough to make false positives the dominant result.

## Connections across layers

From below, this area takes [hypothesis testing and confidence intervals](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md) (power, sample size, the meaning of a pooled interval), [Bayesian reasoning](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md) (likelihood ratios, the base rate of true hypotheses), [the scientific method](../../01-quantitative-and-scientific-foundations/03-systems-and-models/the-scientific-method-and-models.md) (pre-stated hypotheses, replication), and from pharmacology the [placebo effect](../../09-pharmacology-and-therapeutics/04-non-drug-therapeutics/behaviour-change-and-the-placebo-effect.md) that blinding exists to neutralise and the [drug development pipeline](../../09-pharmacology-and-therapeutics/05-drug-development-and-toxicology/from-target-to-approval.md) whose phase III trials are the main source of treatment evidence.

To the layers above it gives the likelihood ratios used in [pre-test to post-test reasoning](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md), the effect sizes that [shared decision-making](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/prognosis-and-shared-decision-making.md) presents to patients, the named trials that underpin every disease leaf in layers 12–14 (for example [ischaemic heart disease](../../12-organ-system-specialties/01-cardiology/ischemic-heart-disease.md) and [systemic anticancer therapy](../../12-organ-system-specialties/07-oncology/systemic-anticancer-therapy.md)), the guidelines that [quality improvement](../../15-medicine-in-society/01-health-systems/patient-safety-and-quality-improvement.md) audits against, and the effect estimates that [health economics](../../15-medicine-in-society/01-health-systems/health-economics-and-priority-setting.md) prices.

## Cross-cutting threads

- [Probability and uncertainty](../../CROSS-CUTTING.md#probability-and-uncertainty): a trial result is an interval, a test result is a likelihood ratio, a guideline is a certainty rating.
- [Cause and mechanism](../../CROSS-CUTTING.md#cause-and-mechanism): randomisation is the cleanest route from association to cause; surrogate outcomes are where mechanism and outcome part company.
- [Harm and benefit](../../CROSS-CUTTING.md#harm-and-benefit): every recommendation balances a number needed to treat against a number needed to harm.
- [Dose–response](../../CROSS-CUTTING.md#dose-response): a gradient across trial doses raises the certainty of a causal effect.
- [Specificity and recognition](../../CROSS-CUTTING.md#specificity-and-recognition): sensitivity and specificity are the test's recognition performance, and imperfect recognition has a cost on both sides.
