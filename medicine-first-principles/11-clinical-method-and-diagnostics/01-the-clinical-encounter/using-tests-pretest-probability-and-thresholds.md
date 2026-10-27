# Using tests, pre-test probability and thresholds

> **Layer:** [11 Clinical Method and Diagnostics](../README.md) › [The clinical encounter](README.md)
> **Builds on:** [Bayesian reasoning](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md), [Diagnostic accuracy studies](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md), [Measures of frequency and association](../../10-epidemiology-and-evidence/01-epidemiology/measures-of-frequency-and-association.md), [Clinical reasoning and cognitive bias](clinical-reasoning-and-cognitive-bias.md)
> **Enables:** [Clinical chemistry and reference ranges](../02-laboratory-medicine/clinical-chemistry-and-reference-ranges.md), [Ischemic heart disease](../../12-organ-system-specialties/01-cardiology/ischemic-heart-disease.md), [The acute abdomen](../../13-acute-perioperative-and-procedural-care/01-surgery/the-acute-abdomen.md), [Health economics and priority setting](../../15-medicine-in-society/01-health-systems/health-economics-and-priority-setting.md)

## Essence

A test is worth ordering only if its result could change what you do. That single sentence contains the whole theory of testing. Before the test there is a probability of disease, set by prevalence and the history and examination. The test result multiplies the odds by its likelihood ratio to give a post-test probability. And action depends on where that probability falls relative to two thresholds: below the *test threshold* the disease is unlikely enough to dismiss without testing; above the *treatment threshold* it is likely enough to treat without further testing; only between them is a test useful. The thresholds are set by the costs of the two errors (missing the disease, treating someone who does not have it), so testing is as much a decision analysis as a measurement.

## Core tenets

1. **Pre-test probability comes from epidemiology and the encounter, and no test result can be read without it.** Prevalence in the relevant population is the starting prior; the features of the history and examination move it. A positive result means something different in a patient whose pre-test probability was 5% and one whose probability was 60%, because the same likelihood ratio acts on different odds. Clinicians who skip this step read tests as if they were verdicts and are misled by every false positive in a low-risk patient.

2. **Updating works in odds, and likelihood ratios are the multipliers.** Convert probability to odds (p / (1 − p)), multiply by the likelihood ratio, convert back. Worked example: a 55-year-old with exertional chest pain has, say, a 30% pre-test probability of coronary disease. Pre-test odds 0.3/0.7 = 0.43. An exercise test with positive likelihood ratio about 3 is positive: post-test odds 1.29, post-test probability 1.29/2.29 = 56%. Had the pre-test probability been 5% (odds 0.053), the same result gives odds 0.16 and probability 14%: still probably not disease. Two tests in sequence multiply their likelihood ratios only if they are conditionally independent, which tests of the same mechanism are not.

3. **Likelihood ratios near 1 are useless however good the test sounds.** A positive likelihood ratio of 2 barely moves a probability; 10 moves 30% to about 80%; a negative ratio of 0.1 moves 30% to about 4%. Sensitivity and specificity are properties of the test reported in [accuracy studies](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md); likelihood ratios are what the clinician needs because they combine the two and act directly on odds. The rule "sensitive tests rule out, specific tests rule in" is the same statement: a high-sensitivity test has a small negative ratio, a high-specificity test a large positive one.

4. **Two thresholds define when a test is worth doing.** Pauker and Kassirer (1980) showed that if treatment's benefit when the disease is present and its harm when absent are known, there is a probability above which treating is right without more information (the treatment threshold) and one below which neither testing nor treating is right (the test threshold). A test is useful only if the pre-test probability lies between them and the result could cross one. The thresholds move: a dangerous, easily treated disease (bacterial meningitis) has a low treatment threshold; a treatment that is toxic and a disease that is benign push it high.

   ```
   0% -------- test threshold -------- treatment threshold -------- 100%
       no test, no treat    |   test: result may cross a line   |   treat without testing
   ```

5. **A test that cannot cross a threshold should not be ordered.** If the pre-test probability is 2% and the best available test has a positive likelihood ratio of 4, the post-test probability is about 8%, still below any treatment threshold; the test cannot change the decision and its false positives will lead to more tests. Conversely, when probability is already above the treatment threshold a confirmatory test delays treatment and a false negative may wrongly withhold it. This is the logic behind "do not order the test if you would not act on the result."

6. **Harms of testing are real and compound.** Every test has false positives, each of which generates further tests, anxiety, procedures and sometimes treatment; imaging exposes to radiation and finds incidental lesions in a large fraction of adults; a reference range defines 5% of healthy people as abnormal by construction ([reference ranges](../02-laboratory-medicine/clinical-chemistry-and-reference-ranges.md)). A panel of twenty independent tests in a healthy person has roughly a 64% chance of at least one "abnormal" result. Testing in low-probability patients manufactures disease, which is the [overdiagnosis](../../10-epidemiology-and-evidence/03-screening-and-prevention/screening-principles-and-biases.md) of the clinic.


## Key concepts

| Term | Meaning |
|---|---|
| Pre-test probability | Probability of disease before the test, from prevalence and clinical features |
| Post-test probability | Probability after the result; pre-test odds × likelihood ratio, converted back |
| Odds | p / (1 − p); the form in which Bayesian updating is a multiplication |
| Likelihood ratio | Probability of the result in disease divided by its probability in health |
| Test threshold | Probability below which the disease is dismissed without testing |
| Treatment threshold | Probability above which treatment is given without further testing |
| Conditional independence | Two tests give independent evidence only if their errors are uncorrelated given the disease |
| Clinical decision rule | A validated score that estimates probability and directs testing |
| Incidentaloma | An unexpected finding on a test ordered for another reason |

## How it fits

- **Below:** the arithmetic is [Bayes' theorem](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md) in odds form; the likelihood ratios come from [diagnostic accuracy studies](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md); the prior is a [prevalence](../../10-epidemiology-and-evidence/01-epidemiology/measures-of-frequency-and-association.md); the hypothesis being tested comes from [clinical reasoning](clinical-reasoning-and-cognitive-bias.md).
- **Above:** every test in the [laboratory](../02-laboratory-medicine/README.md) and [imaging](../03-imaging-and-physiological-measurement/README.md) parents is used this way; [ischaemic heart disease](../../12-organ-system-specialties/01-cardiology/ischemic-heart-disease.md) and the [acute abdomen](../../13-acute-perioperative-and-procedural-care/01-surgery/the-acute-abdomen.md) are the classic threshold problems; pricing a testing strategy is [health economics](../../15-medicine-in-society/01-health-systems/health-economics-and-priority-setting.md).
- **Siblings:** [history](history-taking-and-communication.md) and [examination](physical-examination-and-signs.md) set the pre-test probability; [prognosis and shared decision-making](prognosis-and-shared-decision-making.md) supplies the values that fix where the treatment threshold sits.

## Common misconceptions

- **"A positive test means the patient has the disease."**: it means the probability has risen by the likelihood ratio; from a low prior, most positives are false.
- **"More tests give a clearer picture."**: tests of the same mechanism are not independent, and each adds false positives; a test that cannot cross a threshold adds only noise.
- **"The thresholds are medical facts."**: they are set by the consequences of the two errors, which depend on the treatment, the disease and the patient's values.

## Go deeper

- Stephen G. Pauker and Jerome P. Kassirer, "The threshold approach to clinical decision making", *New England Journal of Medicine* (1980): the two-threshold model.
- David L. Sackett, R. Brian Haynes, Gordon H. Guyatt and Peter Tugwell, *Clinical Epidemiology: A Basic Science for Clinical Medicine* (2nd ed., 1991): likelihood ratios and the nomogram, for clinicians.
- Harold C. Sox, Michael C. Higgins and Douglas K. Owens, *Medical Decision Making* (2nd ed., 2013): the full decision-analytic treatment.
