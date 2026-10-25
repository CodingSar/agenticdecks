# Measurement Error and Biological Variation

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › [Probability and Measurement](README.md)
> **Builds on:** [Distributions and descriptive statistics](distributions-and-descriptive-statistics.md), [Probability](probability.md)
> **Enables:** [Clinical chemistry and reference ranges](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/clinical-chemistry-and-reference-ranges.md), [Physical examination and signs](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/physical-examination-and-signs.md), [Diagnostic accuracy studies](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md), [Homeostasis and set points](../../06-physiology/01-integrative-principles/homeostasis-and-set-points.md)

## Essence

Every number in medicine is a measurement of a quantity that was already varying before the instrument touched it. A blood pressure of 142/88 mmHg carries three kinds of spread: the instrument's error, the moment-to-moment variation of the patient's true pressure, and the difference between this patient's usual value and other people's. A clinician who cannot separate these will treat noise as disease and miss disease as noise. The core ideas are that random error averages out while systematic error does not, that a "normal range" is a statement about a population and not about health, and that a change in a repeated measurement means something only when it exceeds what measurement and biology would produce on their own.

## Core tenets

1. **Random error averages out; systematic error does not.** A measurement scatters around its true value (imprecision) and may also be offset from it (bias). Repeating and averaging shrinks the random scatter by `1/√n` (four readings halve the spread) but leaves bias untouched: a cuff that is too small overestimates blood pressure on every reading. Precision is checked by repetition; accuracy needs an external standard. Laboratories run both, as internal quality control and external calibration against reference materials.

2. **The patient varies even when the measurement does not.** Within-person biological variation is often larger than analytical error. Blood pressure swings 20–30 mmHg across a day and rises in a clinic; serum potassium varies ~5% day to day; cortisol follows a circadian cycle with morning values two to three times evening ones; many hormones pulse. A single reading is a sample of a process, and a diagnosis of hypertension or diabetes rests on repeated or averaged values for this reason.

3. **Pre-analytical events are the largest source of error.** Haemolysis in the tube releases potassium and gives a falsely high value; a tourniquet left on concentrates proteins and calcium; a sample left standing lets cells consume glucose; posture shifts fluid and changes concentrations by ~10%; a fist clenched during venepuncture raises potassium. More laboratory errors arise before the analyser than inside it, which is why an unexpected result is first repeated.

4. **The reference range is a population statistic, usually the central 95%.** It is built by measuring a reference population of apparently healthy people and taking the 2.5th to 97.5th percentiles. By construction, 5% of healthy people fall outside it for every test, so a healthy person given a 20-test panel has about a 64% chance (1 − 0.95²⁰) of at least one "abnormal" result. The range also depends on age, sex, pregnancy, ethnicity and the laboratory's method, so a value is only interpretable against the range of the laboratory that produced it.

5. **"Normal" is not "healthy" and "abnormal" is not "diseased".** A reference range describes what is common, not what is optimal: the central 95% of cholesterol in a population with a high rate of heart disease is not a healthy range, and decision thresholds for cholesterol, glucose and blood pressure are therefore set by outcome studies, not percentiles. Conversely a value inside the range can be abnormal for this patient: a haemoglobin at the 10th percentile is a 30% fall for someone who lived at the 90th.

6. **A change between two measurements is real only when it exceeds the combined noise.** If analytical and within-person coefficients of variation are `CVa` and `CVi`, the difference between two results must exceed roughly `2.8 × √(CVa² + CVi²)` to be significant at the usual 95% level (the reference change value). For creatinine (CVa ~3%, CVi ~5%) that is about 16%; a rise from 80 to 88 µmol/L is noise, a rise to 100 is signal. Trends over several points beat any single pair.

7. **Regression to the mean is a consequence of measuring with noise, and it mimics treatment effect.** Patients are enrolled or treated when a value is high; their next value is, on average, lower whether or not anything was done, because part of the high reading was noise that does not recur. This explains much of the apparent benefit of untested remedies and the fall in blood pressure seen after any intervention, and it is the reason trials need a control group measured the same way.

## Key concepts

| Term | Meaning |
|---|---|
| Precision (imprecision) | Closeness of repeated measurements to each other; random error |
| Accuracy (bias) | Closeness of the mean measurement to the true value; systematic error |
| Coefficient of variation (CV) | Standard deviation divided by the mean, as a percentage |
| Within-person (intra-individual) variation | How much one person's true value fluctuates over time |
| Between-person variation | Spread of usual values across individuals |
| Pre-analytical error | Error introduced before the sample reaches the analyser |
| Reference range (interval) | Central 95% of values in a reference population |
| Reference change value | The minimum difference between two results that exceeds expected noise |
| Regression to the mean | Extreme values tend to be followed by less extreme ones |

## How it fits

- **Below:** random error is a random variable with a [distribution](distributions-and-descriptive-statistics.md), and the `1/√n` rule and the 95% interval come from [probability](probability.md). This leaf has no layer beneath it.
- **Above:** [clinical chemistry and reference ranges](../../11-clinical-method-and-diagnostics/02-laboratory-medicine/clinical-chemistry-and-reference-ranges.md) is tenets 3–6 as a discipline; [physical examination](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/physical-examination-and-signs.md) is a measurement with observer error; [diagnostic accuracy studies](../../10-epidemiology-and-evidence/02-evidence-based-medicine/diagnostic-accuracy-studies.md) quantify how well a noisy measurement separates disease; [homeostasis](../../06-physiology/01-integrative-principles/homeostasis-and-set-points.md) is the source of within-person variation.
- **Siblings:** [probability](probability.md) supplies the rules; [distributions](distributions-and-descriptive-statistics.md) describe the spread; [Bayesian reasoning](bayesian-reasoning.md) turns an imperfect measurement into a revised belief about the patient.

## Common misconceptions

- **"A result outside the reference range is abnormal."** One in twenty healthy results falls outside it by definition; the more tests ordered, the more false alarms.
- **"The patient improved after treatment, so the treatment worked."** Values selected for being extreme regress toward the mean on their own; only a comparison group shows the treatment's share.

## Go deeper

- Callum G. Fraser, *Biological Variation: From Principles to Practice* (2001): the quantitative basis of reference change values.
- Douglas G. Altman, *Practical Statistics for Medical Research* (1991): measurement, agreement and reference ranges, written for clinicians.
