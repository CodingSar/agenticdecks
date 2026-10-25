# Bayesian Reasoning

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › [Probability and Measurement](README.md)
> **Builds on:** [Probability](probability.md), [Distributions and descriptive statistics](distributions-and-descriptive-statistics.md)
> **Enables:** [Using tests, pre-test probability and thresholds](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md), [Clinical reasoning and cognitive bias](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/clinical-reasoning-and-cognitive-bias.md), [Diagnostic accuracy studies](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md), [Screening principles and biases](../../10-epidemiology-and-evidence/03-screening-and-prevention/screening-principles-and-biases.md)

## Essence

Diagnosis is the revision of belief by evidence, and Bayes' theorem is the arithmetic of that revision. Before any test, a clinician holds a probability that the patient has a disease (the prior, or pre-test probability), drawn from prevalence, the history and the examination. A test result does not reveal the truth; it moves the probability, by an amount that depends on how much more often the result occurs in the diseased than in the healthy (the likelihood ratio). The same positive result therefore means different things in different patients: a positive troponin in a 60-year-old with crushing chest pain nearly confirms infarction, while the same value in a 25-year-old with a sore chest wall is probably a false positive. Every test, sign and symptom is a likelihood ratio, and every clinical decision is a comparison of a post-test probability with a threshold for action.

## Core tenets

1. **Bayes' theorem reverses a conditional probability.** `P(D | T) = P(T | D) · P(D) / P(T)`: the probability of disease given a test result equals the probability of that result in disease, times the prior probability of disease, divided by the overall probability of the result. The denominator is the sum over diseased and healthy: `P(T|D)P(D) + P(T|not D)P(not D)`. It is the only correct way to get from "how tests behave in patients with known status" (what studies measure) to "what this result means for this patient" (what the clinician needs).

2. **In odds form the update is a single multiplication.** Post-test odds = pre-test odds × likelihood ratio. The likelihood ratio for a positive result is `sensitivity / (1 − specificity)`; for a negative result it is `(1 − sensitivity) / specificity`. A test with sensitivity 90% and specificity 90% has a positive likelihood ratio of 9 and a negative one of 0.11. From a pre-test probability of 10% (odds 1:9), a positive result gives odds of 1:1, a probability of 50%; from 50% (odds 1:1) it gives 9:1, a probability of 90%. The same test, two very different answers.

3. **The prior is not optional; ignoring it is the base-rate fallacy.** Screening 10,000 women aged 40 for breast cancer (prevalence ~0.4%) with a mammogram of sensitivity ~85% and specificity ~90% yields ~34 true positives and ~996 false positives: a positive result means cancer about 3% of the time. The same test in a woman with a palpable lump (prior perhaps 30%) gives a positive predictive value near 80%. Prevalence in the population being tested, not the test's accuracy, dominates what a positive result means when disease is rare.

4. **Likelihood ratios are properties of the test; predictive values are properties of the test in a population.** Sensitivity and specificity, and hence likelihood ratios, are roughly stable across settings (though they drift with disease spectrum and severity). Positive and negative predictive values change with prevalence, so a predictive value quoted from a hospital study cannot be carried into primary care. A likelihood ratio above 10 or below 0.1 changes belief substantially; between 0.5 and 2 the test is nearly useless.

5. **Evidence accumulates by multiplying likelihood ratios, if the pieces are independent.** A history, an examination finding and a laboratory value each update the odds in turn. Clinical decision rules (for pulmonary embolism, streptococcal throat, ankle fracture) are formalised versions of this chain. But findings that share a cause are not independent (two signs of the same dehydrated state), and multiplying their likelihood ratios overstates the evidence; the rules are derived empirically for that reason.

6. **Decisions are made against thresholds, not at certainty.** A test is worth doing only if its result could cross a threshold: below the *test threshold* the disease is too unlikely to pursue; above the *treatment threshold* one treats without testing. The thresholds depend on the harm of a missed diagnosis, the harm of unnecessary treatment and the cost of the test. A test that cannot move the probability across a threshold changes nothing and should not be ordered; this is the formal reason "routine" investigations waste money and generate false positives.

7. **The prior itself comes from evidence and can be formalised.** Bayesian statistics treats parameters (a treatment effect, a prevalence) as having probability distributions that data update: posterior ∝ likelihood × prior. A small trial showing a dramatic effect is tempered by a sceptical prior that large effects are rare; a biologically implausible association needs more data than a plausible one. This is how an experienced clinician reads a surprising result.

## Key concepts

| Term | Meaning |
|---|---|
| Prior (pre-test) probability | Probability of disease before the test, from prevalence and clinical findings |
| Posterior (post-test) probability | Probability of disease after incorporating the result |
| Sensitivity | `P(positive | disease)`; the fraction of diseased correctly detected |
| Specificity | `P(negative | no disease)`; the fraction of healthy correctly cleared |
| Likelihood ratio | How many times more likely a result is in the diseased than in the healthy |
| Positive / negative predictive value | `P(disease | positive)` / `P(no disease | negative)`; depend on prevalence |
| Base-rate fallacy | Judging a result's meaning without regard to prevalence |
| Test threshold / treatment threshold | Probabilities below which one does not test and above which one treats without testing |

## How it fits

- **Below:** the theorem is a rearrangement of [conditional probability](probability.md); sensitivity and specificity are tail areas of two [distributions](distributions-and-descriptive-statistics.md) (test values in diseased and healthy) split at a cut-off.
- **Above:** [using tests at the bedside](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/using-tests-pretest-probability-and-thresholds.md) and [clinical reasoning](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/clinical-reasoning-and-cognitive-bias.md) are this leaf in practice; [diagnostic accuracy studies](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md) measure the likelihood ratios; [screening](../../10-epidemiology-and-evidence/03-screening-and-prevention/screening-principles-and-biases.md) is tenet 3 at population scale.
- **Siblings:** [probability](probability.md) supplies the rules; [measurement error](measurement-error-and-biological-variation.md) explains why a test result is uncertain evidence in the first place; [distributions](distributions-and-descriptive-statistics.md) show that a cut-off trades sensitivity against specificity.

## Common misconceptions

- **"A sensitive test rules in; a specific test rules out."** The reverse: a highly sensitive test that is negative rules out (few diseased are missed); a highly specific test that is positive rules in (few healthy are flagged).
- **"A positive result from a 95%-accurate test means 95% chance of disease."** Only if the prior was 50%; at 1% prevalence most positives are false.

## Go deeper

- David L. Sackett, R. Brian Haynes, Gordon H. Guyatt and Peter Tugwell, *Clinical Epidemiology: A Basic Science for Clinical Medicine* (2nd ed., 1991): likelihood ratios and thresholds for the bedside.
- Stephen G. Pauker and Jerome P. Kassirer, "The threshold approach to clinical decision making" (*New England Journal of Medicine*, 1980): the test and treatment thresholds.
- Gerd Gigerenzer, *Reckoning with Risk* (2002): natural frequencies as the way to make Bayes intuitive.
