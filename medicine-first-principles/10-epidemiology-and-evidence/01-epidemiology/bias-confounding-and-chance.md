# Bias, confounding and chance

> **Layer:** [10 Epidemiology and Evidence](../README.md) › [Epidemiology](README.md)
> **Builds on:** [Observational study designs](observational-study-designs.md), [Causal inference](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md), [Hypothesis testing and confidence intervals](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md), [Measurement error and biological variation](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/measurement-error-and-biological-variation.md)
> **Enables:** [Randomized controlled trials](../02-evidence-based-medicine/randomized-controlled-trials.md), [Screening principles and biases](../03-screening-and-prevention/screening-principles-and-biases.md), [Grading evidence and guidelines](../02-evidence-based-medicine/grading-evidence-and-guidelines.md), [Clinical reasoning and cognitive bias](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/clinical-reasoning-and-cognitive-bias.md)

## Essence

An observed association between an exposure and a disease has four possible explanations: the exposure causes the disease; the study selected or measured its subjects in a way that manufactured the association (bias); a third factor causes both (confounding); or random variation produced it (chance). Epidemiology is largely the discipline of ruling out the last three before accepting the first. Chance shrinks with sample size. Bias and confounding are systematic, do not shrink with sample size, and can only be addressed by design, measurement and reasoning about mechanism. A study of ten million records with a biased design is precisely wrong rather than approximately right.

## Core tenets

1. **Chance is the only error that larger numbers fix.** Random error arises because a study is a sample of the outcomes that could have occurred. [Confidence intervals](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md) measure it: a relative risk of 2.0 with an interval of 0.9 to 4.4 is compatible with no effect; with 1.8 to 2.2 it is not. Halving the interval needs roughly four times the sample. Systematic errors shift the estimate rather than widen the interval, so a narrow interval around a biased number is false confidence.

2. **Selection bias arises when entry to or exit from the study depends on both exposure and outcome.** If sick smokers are referred to the hospital where cases are collected more often than sick non-smokers, smoking looks harmful whatever the truth. Healthy-worker bias, loss to follow-up that differs by arm, and volunteer bias belong here. The test: could the probability of being in my dataset depend jointly on exposure and outcome?

3. **Information bias arises when exposure or outcome is measured wrongly, and matters most when the error differs between groups.** *Recall bias*: mothers of malformed children search their memories harder. *Observer bias*: an assessor who knows the allocation reads an ambiguous X-ray more favourably. Misclassification that is the same in both groups usually drags an association toward the null; misclassification that differs between groups can create or reverse one. Blinding and objective endpoints exist to make error non-differential.

4. **Confounding is a mixing of effects: a third variable associated with the exposure and independently causing the outcome.** Coffee drinkers once appeared to have more pancreatic cancer; coffee drinkers also smoked more. A confounder must be associated with the exposure, cause the outcome, and not lie on the causal path between them (adjusting for an intermediate removes the very effect sought). Restriction, matching, stratification and regression remove confounders that were anticipated and measured; randomisation alone removes those that were not.

5. **Confounding by indication haunts every observational study of a treatment.** Doctors give drugs to people who need them, so patients prescribed a new antihypertensive are sicker than those left untreated and the drug appears to cause the heart attacks it was meant to prevent. This is why observational estimates of benefit are distrusted far more than observational estimates of harm (nobody prescribes a drug expecting liver failure), and why the [randomised trial](../02-evidence-based-medicine/randomized-controlled-trials.md) exists.

6. **Causal judgement weighs the whole pattern of evidence.** Bradford Hill's considerations (1965) remain the working checklist: strength, consistency, specificity, temporality (the only strictly necessary one), biological gradient, plausibility, coherence, experiment and analogy. None is proof; together they ask whether every alternative has been made implausible. The judgement that smoking causes lung cancer rested on this reasoning, not on a trial.

7. **Multiplicity turns chance into apparent discovery.** Test twenty subgroups at the 5% level and one will be "significant" by chance; let analysis choices depend on the data and the nominal error rate means nothing. Pre-registration and pre-specified primary outcomes exist because an investigator free to choose after seeing the data will find something. It is the clinician's confirmation bias ([clinical reasoning](../../11-clinical-method-and-diagnostics/01-the-clinical-encounter/clinical-reasoning-and-cognitive-bias.md)) met at the level of populations.

## Key concepts

| Term | Meaning |
|---|---|
| Random error | Variation from sampling, quantified by confidence intervals; falls with sample size |
| Systematic error (bias) | A flaw in design or measurement that shifts the estimate regardless of sample size |
| Selection bias | Entry to or exit from the study depends jointly on exposure and outcome |
| Information bias | Error in measuring exposure or outcome, differential or non-differential |
| Confounding | Distortion by a variable associated with exposure and independently causing outcome |
| Confounding by indication | The reason for treatment also predicts the outcome |
| Immortal-time bias | Follow-up during which the outcome could not occur is misassigned to one group |
| Bradford Hill considerations | Nine aspects of evidence weighed when judging whether an association is causal |
| Effect modification | The association genuinely differs across levels of a third variable; a finding, not an error |

## How it fits

- **Below:** confounding drawn as a directed graph of causes is in [causal inference](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md); chance is the sampling variability of [hypothesis testing](../../01-quantitative-and-scientific-foundations/02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md); error in a single measurement is [measurement error and biological variation](../../01-quantitative-and-scientific-foundations/01-probability-and-measurement/measurement-error-and-biological-variation.md).
- **Above:** every element of the randomised trial (randomisation, concealment, blinding, intention-to-treat) defends against one error named here; screening suffers the selection and time biases of [screening principles and biases](../03-screening-and-prevention/screening-principles-and-biases.md); the risk-of-bias assessment in [evidence grading](../02-evidence-based-medicine/grading-evidence-and-guidelines.md) is this file as a checklist.
- **Siblings:** [observational study designs](observational-study-designs.md) decide which errors a study is exposed to; [measures of association](measures-of-frequency-and-association.md) are what the errors distort.

## Common misconceptions

- **"A big study cannot be wrong."**: size shrinks only random error. The largest datasets (electronic records, claims) are the most exposed to confounding by indication and selection.
- **"Adjusting for more variables makes the result more trustworthy."**: adjusting for a mediator removes real effect; adjusting for a common consequence of exposure and outcome (a collider) creates spurious association. What to adjust for is a causal question answered by a diagram.
- **"Statistical significance means the association is real."**: p < 0.05 says only that chance alone is an unlikely explanation; it says nothing about bias or confounding.

## Go deeper

- Austin Bradford Hill, "The environment and disease: association or causation?", *Proceedings of the Royal Society of Medicine* (1965): the original nine considerations, with the caveats their author attached.
- Kenneth J. Rothman, Sander Greenland and Timothy L. Lash, *Modern Epidemiology* (3rd ed., 2008), chapters on validity: the systematic taxonomy of bias.
- Miguel A. Hernán and James M. Robins, *Causal Inference: What If* (2020): confounding and selection bias expressed as causal diagrams.
