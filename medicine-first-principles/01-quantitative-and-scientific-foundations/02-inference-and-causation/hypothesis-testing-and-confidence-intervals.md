# Hypothesis Testing and Confidence Intervals

> **Layer:** [01 Quantitative and Scientific Foundations](../README.md) › [Inference and Causation](README.md)
> **Builds on:** [Distributions and descriptive statistics](../01-probability-and-measurement/distributions-and-descriptive-statistics.md), [Probability](../01-probability-and-measurement/probability.md), [The scientific method and models](../03-systems-and-models/the-scientific-method-and-models.md)
> **Enables:** [Randomised controlled trials](../../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md), [Bias, confounding and chance](../../10-epidemiology-and-evidence/01-epidemiology/bias-confounding-and-chance.md), [Systematic reviews and meta-analysis](../../10-epidemiology-and-evidence/02-evidence-based-medicine/systematic-reviews-and-meta-analysis.md), [Research integrity and publication bias](../../10-epidemiology-and-evidence/02-evidence-based-medicine/research-integrity-and-publication-bias.md)

## Essence

A study measures a sample, but medicine wants to know about everyone like the sample. Statistical inference is the set of rules for making that jump honestly: a confidence interval says how far the true population value could plausibly lie from the estimate, and a hypothesis test asks whether the data are surprising enough to doubt a specific claim, usually the claim of no effect. Both rest on one idea, that a statistic computed from a random sample has a known sampling distribution whose width shrinks with sample size. The interval is the more informative of the two, because it shows the size of the effect and the uncertainty around it, while a p-value compresses both into one number that is routinely misread. Most of what goes wrong in medical research goes wrong at this step.

## Core tenets

1. **A sample statistic is one draw from a sampling distribution.** Repeat a study many times and the estimated mean, proportion or risk ratio would scatter around the true value with a spread equal to the standard error, which falls as `1/√n`. One never sees that scatter, but its width can be calculated from the one sample's own variability. Every confidence interval and p-value is a statement about this imagined repetition, which is why they describe the procedure's long-run behaviour rather than the probability that this particular result is true.

2. **A 95% confidence interval is the range of population values compatible with the data.** Constructed as roughly estimate ± 2 standard errors, it is built by a procedure that captures the true value in 95% of repetitions. Its width is the study's precision: a trial reporting a relative risk of 0.80 with interval 0.75–0.85 has found a modest, firmly established benefit; one reporting 0.80 with interval 0.40–1.60 has found almost nothing. Reading the ends of the interval, and asking whether both would lead to the same decision, is the essential skill.

3. **A hypothesis test asks how surprising the data would be if a null hypothesis were true.** The p-value is the probability of a result at least as extreme as the one observed, *given* no true effect. A p of 0.03 means that, if the treatment did nothing, a difference this large or larger would arise by chance 3% of the time. It is not the probability that the null is true, nor that the result will replicate, nor a measure of effect size: a trivial effect in a huge study and a large effect in a small one can share the same p.

4. **The 0.05 threshold is a convention, and dichotomising on it is the root of most abuse.** Fisher proposed 5% as a rough guide; it became a gate for publication. Results at p = 0.049 and p = 0.051 differ negligibly in evidence but are treated as success and failure, which invites selective reporting, re-analysis until significance appears (p-hacking) and the burying of null results (publication bias). The remedy is to report estimates with intervals, pre-register analyses, and treat p as a continuous measure of surprise.

5. **Two errors trade against each other, and power is the price of avoiding the second.** A type I error rejects a true null (false alarm, rate α, usually 5%); a type II error misses a real effect (rate β). Power, `1 − β`, is the probability of detecting an effect of a given size, and depends on that size, the variability and the sample. Underpowered studies are the norm in many fields: a trial with 50% power has a coin-flip chance of finding a real effect, and when it does find one it tends to overestimate it, because only the lucky large results cross the threshold.

6. **Multiple comparisons multiply false positives.** Testing twenty independent hypotheses at α = 0.05 gives a 64% chance of at least one spurious "significant" result. Subgroup analyses, many endpoints and repeated interim looks are all forms of this. Corrections (Bonferroni, false discovery rate) restore the error rate at the cost of power; pre-specifying one primary outcome is the cleaner solution. A subgroup finding not predicted in advance is a hypothesis, not a result.

7. **Statistical significance is not clinical importance, and absence of evidence is not evidence of absence.** A blood pressure reduction of 1 mmHg can be highly significant in 100,000 patients and worthless to any of them; a 30% mortality reduction can be "non-significant" in 60 patients and the most important finding in the field. A non-significant result means the data are compatible with no effect; it is also compatible with every value in its interval, including large benefits and harms. Equivalence and non-inferiority require their own designs with pre-specified margins.

8. **Frequentist and Bayesian inference answer different questions, and both are used.** The confidence interval and p-value describe how the procedure would behave over repetitions; the Bayesian posterior describes how plausible each effect size is given the data and a prior. For a single well-designed trial they usually agree; they diverge when the prior is strong, as with implausible mechanisms or tiny studies, which is exactly when the frequentist result most misleads. Meta-analysis is the frequentist route to the same end: pooling makes the sampling distribution narrow.

## Key concepts

| Term | Meaning |
|---|---|
| Sampling distribution | The spread of a statistic over hypothetical repeated samples |
| Standard error | The standard deviation of that spread; falls as `1/√n` |
| Confidence interval | Range of population values compatible with the data at a stated level, usually 95% |
| Null hypothesis | The claim being tested, usually "no difference" |
| p-value | Probability of data at least this extreme if the null were true |
| Type I error (α) | Rejecting a true null; a false positive |
| Type II error (β) | Failing to reject a false null; a missed effect |
| Power | `1 − β`; probability of detecting a real effect of a given size |
| Effect size | The magnitude of a difference or association, with units |
| Multiple comparisons | Many tests inflate the chance of at least one false positive |
| Non-inferiority margin | Pre-specified largest loss of effect judged acceptable |

## How it fits

- **Below:** the sampling distribution is the [central limit theorem](../01-probability-and-measurement/distributions-and-descriptive-statistics.md) applied to a statistic; the p-value is a [conditional probability](../01-probability-and-measurement/probability.md); the null hypothesis is a [falsifiable model](../03-systems-and-models/the-scientific-method-and-models.md).
- **Above:** [randomised trials](../../10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md) are designed around power and a primary outcome; [bias, confounding and chance](../../10-epidemiology-and-evidence/01-epidemiology/bias-confounding-and-chance.md) names chance as one of three explanations for any finding; [meta-analysis](../../10-epidemiology-and-evidence/02-evidence-based-medicine/systematic-reviews-and-meta-analysis.md) pools estimates and intervals; [publication bias](../../10-epidemiology-and-evidence/02-evidence-based-medicine/research-integrity-and-publication-bias.md) and [grading evidence](../../10-epidemiology-and-evidence/02-evidence-based-medicine/grading-evidence-and-guidelines.md) are responses to tenets 4–7.
- **Siblings:** [regression](regression-adjustment-and-survival-analysis.md) produces the estimates that intervals are built around; [causal inference](causal-inference.md) asks the question a significant association cannot answer: whether it is cause.

## Common misconceptions

- **"p = 0.05 means a 5% chance the result is due to chance."** It means a 5% chance of data this extreme if there were no effect; the probability that the finding is false depends also on how plausible the effect was beforehand.
- **"A non-significant result shows the treatment does not work."** It shows the study could not distinguish the effect from zero; the interval says what effects remain possible.
- **"A significant result in a large trial is important."** Size of effect and p-value are different things; read the estimate and its interval, then ask whether it matters to a patient.

## Go deeper

- Douglas G. Altman and colleagues (eds), *Statistics with Confidence* (2nd ed., 2000): the case for intervals over p-values, with methods.
- Steven N. Goodman, "Toward evidence-based medical statistics. 1: The P value fallacy" (*Annals of Internal Medicine*, 1999): what p-values do and do not mean.
- John P. A. Ioannidis, "Why most published research findings are false" (*PLoS Medicine*, 2005): power, bias and multiplicity combined into one argument.
