# Diagnostic accuracy studies

> **Layer:** [10 Epidemiology and Evidence](../README.md) › [Evidence-based medicine](README.md)
> **Builds on:** [Bayesian reasoning](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md), [Measurement error and biological variation](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/measurement-error-and-biological-variation.md), [Measures of frequency and association](../01-epidemiology/measures-of-frequency-and-association.md), [Bias, confounding and chance](../01-epidemiology/bias-confounding-and-chance.md)
> **Enables:** [Using tests, pre-test probability and thresholds](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md), [Screening principles and biases](../03-screening-and-prevention/screening-principles-and-biases.md), [Clinical chemistry and reference ranges](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/clinical-chemistry-and-reference-ranges.md), [Health informatics and artificial intelligence](../../15-medicine-in-society/01-health-systems/health-informatics-and-artificial-intelligence.md)

## Essence

A diagnostic test is a measurement whose result is used to change the probability that a patient has a condition. A diagnostic accuracy study measures how well it does that by applying the test and a reference standard (the best available definition of truth) to the same patients and cross-tabulating the results. From that 2×2 table come sensitivity and specificity, which are properties of the test, and likelihood ratios, which say how much the result should move a probability. The single idea is that a test's value is not "accuracy" but *how much it changes what you believe*, and that this depends on the result obtained, on the spectrum of patients tested and on what the reference standard really measures.

## Core tenets

1. **The 2×2 table defines everything, and its two columns are conditioned on truth.** Test 1,000 people of whom 100 have the disease. The test is positive in 90 of them and in 90 of the 900 without it:

   | | Disease | No disease |
   |---|---|---|
   | Test positive | 90 (true positive) | 90 (false positive) |
   | Test negative | 10 (false negative) | 810 (true negative) |

   Sensitivity = 90/100 = 0.90 (positive in disease). Specificity = 810/900 = 0.90 (negative in health). Both are column proportions: they describe the test given the truth, and that is why they do not depend on prevalence.

2. **Predictive values are row proportions, and they depend entirely on prevalence.** In the table, the positive predictive value is 90/180 = 0.50: half the positives are false. Drop prevalence to 1% (10 cases in 1,000): true positives 9, false positives 99, and the positive predictive value is 9/108 = 0.08. The same test that is useful in a specialist clinic generates mostly false alarms when applied to the healthy. A clinician wants the row (given this result, what is the probability of disease?) but the study can only hand over the column.

3. **Likelihood ratios carry the column information in a form Bayes can use.** The positive likelihood ratio is sensitivity / (1 − specificity) = 0.90/0.10 = 9: a positive result is nine times as likely in disease as in health. The negative likelihood ratio is (1 − sensitivity) / specificity = 0.10/0.90 = 0.11. Multiply the pre-test *odds* by the likelihood ratio to get post-test odds, as [Bayesian reasoning](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md) prescribes. A ratio near 1 is uninformative whatever the sensitivity and specificity sound like; ratios above 10 or below 0.1 change decisions.

4. **A threshold trades sensitivity for specificity, and the receiver operating characteristic curve shows the whole trade.** Most tests are continuous (a troponin concentration, a lesion score) and "positive" means above a cut-off. Lower the cut-off and sensitivity rises while specificity falls. The Receiver Operating Characteristic (ROC) curve plots sensitivity against 1 − specificity for every cut-off; the area under it (0.5 useless, 1.0 perfect) summarises discrimination independently of threshold. Choosing the threshold is a value judgement about which error costs more, not a statistical one.

5. **Spectrum decides accuracy: a test looks better when the diseased are obviously ill and the healthy are obviously well.** Sensitivity measured in advanced cancer does not apply to early cancer; specificity measured in healthy volunteers does not apply to patients with symptoms that mimic the disease. Case-control designs that compare clear cases with clear non-cases inflate both. A valid study enrols a consecutive series of the patients in whom the test would actually be used, with the diagnostic uncertainty they actually have.

6. **The reference standard is the ceiling, and verification bias is the commonest leak.** No test can be shown more accurate than the standard it is compared with. When the reference standard is applied only to test-positive patients (because it is invasive), the false negatives go unverified and sensitivity is overestimated (partial verification bias). When the test result influences the reference (the pathologist knows the scan), incorporation bias follows. Blinded, complete verification is to a diagnostic study what concealment and blinding are to a trial.


## Key concepts

| Term | Meaning |
|---|---|
| Reference standard | The best available method for establishing whether the condition is present |
| Sensitivity | Proportion of people with the condition in whom the test is positive |
| Specificity | Proportion of people without the condition in whom the test is negative |
| Positive and negative predictive value | Proportion of positive (negative) results that are correct; depend on prevalence |
| Likelihood ratio | How many times more likely a result is in people with the condition than without |
| ROC curve | Sensitivity against 1 − specificity across all thresholds; its area measures discrimination |
| Spectrum bias | Accuracy differs because the study's patients are more or less obviously diseased than those in practice |
| Verification bias | Reference standard applied selectively, usually to test-positives, distorting sensitivity |
| Incorporation bias | The index test forms part of the reference standard |

## How it fits

- **Below:** the arithmetic is [Bayes' theorem](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md) in odds form; the test's own imprecision and the overlap of distributions between sick and well are [measurement error and biological variation](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/measurement-error-and-biological-variation.md); spectrum and verification bias are special cases of [selection and information bias](../01-epidemiology/bias-confounding-and-chance.md).
- **Above:** these numbers feed [pre-test to post-test reasoning](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md) at the bedside; [reference ranges](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/clinical-chemistry-and-reference-ranges.md) are thresholds on continuous tests; every [screening test](../03-screening-and-prevention/screening-principles-and-biases.md) and every machine-learning classifier in [health informatics](../../15-medicine-in-society/01-health-systems/health-informatics-and-artificial-intelligence.md) is judged by the same ROC curves and suffers the same spectrum bias.
- **Siblings:** the [randomised trial](randomized-controlled-trials.md) is the design that could show a test improves outcomes; [meta-analysis](systematic-reviews-and-meta-analysis.md) of accuracy studies must handle the threshold trade-off that single trials do not face.

## Common misconceptions

- **"A 90% sensitive test rules disease out when negative."**: only if the pre-test probability was modest; at 50% pre-test probability a negative result with likelihood ratio 0.11 still leaves a 10% probability of disease.
- **"Sensitivity and specificity are fixed properties of a test."**: they are fixed given the threshold and the spectrum of patients; both move when either changes.
- **"An accurate test is a useful test."**: a test helps only if its result crosses a decision threshold and the decision changes the course of disease; many accurate tests detect conditions that would never have mattered, which is the overdiagnosis problem of [screening](../03-screening-and-prevention/screening-principles-and-biases.md).

## Go deeper

- David L. Sackett and R. Brian Haynes, "The architecture of diagnostic research", *British Medical Journal* (2002): the phases a diagnostic test should pass through before use.
- Patrick M. Bossuyt et al., "STARD 2015 (Standards for Reporting Diagnostic Accuracy): an updated list of essential items for reporting diagnostic accuracy studies", *British Medical Journal* (2015): the reporting standard, which doubles as a checklist of biases.
- Steven McGee, *Evidence-Based Physical Diagnosis* (4th ed., 2018): likelihood ratios for hundreds of symptoms and signs, with the studies behind them.
