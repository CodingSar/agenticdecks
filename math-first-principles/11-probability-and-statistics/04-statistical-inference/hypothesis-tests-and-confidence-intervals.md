# Hypothesis Tests and Confidence Intervals

> **Layer:** [11 Probability and Statistics](../README.md) › [Statistical Inference](README.md)
> **Builds on:** [Estimation and Likelihood](estimation-and-likelihood.md), [The Central Limit Theorem](../02-limit-theorems/the-central-limit-theorem.md), [Concentration Inequalities](../02-limit-theorems/concentration-inequalities.md), [Random Variables and Distributions](../01-measure-theoretic-probability/random-variables-and-distributions.md)
> **Enables:** [Linear Models and Regression](linear-models-and-regression.md), [Mathematics and Society](../../15-mathematics-in-context/mathematics-and-society.md), [Hypothesis Testing and Confidence Intervals in medicine](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/02-inference-and-causation/hypothesis-testing-and-confidence-intervals.md), [Randomized Controlled Trials](../../../medicine-first-principles/10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md), [Evaluation and Experimentation](../../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/evaluation-and-experimentation.md)

## Essence

A hypothesis test is a rule for deciding, from data, whether to reject a null hypothesis H₀ in favour of an alternative H₁, designed so that the probability of wrongly rejecting a true H₀ is at most a chosen level α. Jerzy Neyman and Egon Pearson (1933) framed testing as an optimisation: among tests with that error rate, find the one most likely to detect H₁ when it is true, and they showed that the likelihood ratio is optimal. A confidence interval is the set of parameter values that a test would not reject. Both are guarantees about a procedure over repeated sampling, not probabilities about the particular hypothesis or parameter at hand; most misuse forgets this.

## Core tenets

1. **A test trades two errors.** A test is a rejection region R in the space of outcomes, or more generally a function φ(x) ∈ [0, 1] giving the probability of rejecting. Its size is the probability of rejecting when H₀ holds (a type I error); its power is the probability of rejecting when H₁ holds, one minus the probability of a type II error. Shrinking one error enlarges the other at a fixed sample size; only more data reduces both.

2. **The Neyman–Pearson lemma: for simple hypotheses the likelihood ratio test is most powerful.** Let f₀ and f₁ be the densities under H₀ and H₁, and let φ* reject when f₁(x)/f₀(x) > k, with k chosen to give size α. For any other test φ of size at most α,

   ```
   (φ*(x) − φ(x))·(f₁(x) − k·f₀(x))  ≥  0   for every x,
   ```

   since φ* = 1 where f₁ > k·f₀ and φ* = 0 where f₁ < k·f₀. Integrating gives power(φ*) − power(φ) ≥ k·(size(φ*) − size(φ)) ≥ 0.

3. **Optimality extends partly to composite hypotheses.** If the likelihood ratio between any two parameter values is monotone in a statistic T, as for exponential families, one test rejecting for large T is most powerful against every alternative at once: a uniformly most powerful (UMP) test. Usually none exists, and the generalised likelihood ratio test is used instead. Samuel Wilks (1938) showed that, under H₀, twice the log of the maximised likelihood ratio is approximately chi-squared, with degrees of freedom equal to the number of constrained parameters.

4. **A p-value is a statistic that is uniform under the null hypothesis.** If a test rejects for large values of T, the p-value of observed t is p = P_H₀(T ≥ t), the probability under H₀ of a result at least as extreme. When T has a continuous distribution under H₀, p is uniformly distributed on [0, 1], so rejecting when p ≤ α gives size exactly α. A p-value is not the probability that H₀ is true, and a large one is not evidence for H₀.

5. **The base rate decides what a rejection means.** Suppose 10% of tested hypotheses are true effects, the power is 0.8 and α = 0.05. Of 1,000 tests, 100 are real and 80 of them are detected; of the 900 null cases, 45 are rejected by chance. So 45 of the 125 discoveries, 36%, are false. Testing many hypotheses compounds this: the Bonferroni correction tests each at α/m for m hypotheses, and Yoav Benjamini and Yosef Hochberg (1995) introduced the less conservative control of the false discovery rate. The American Statistical Association issued a statement in 2016 warning against equating p < 0.05 with truth or importance.

6. **Confidence intervals are inverted tests.** If for each value θ₀ there is a test of θ = θ₀ at level α, the set of θ₀ not rejected is a confidence set with coverage 1 − α: whatever the true θ, the random set contains it with probability at least 1 − α. The guarantee is about the procedure. Once the data are in, a computed interval such as [2.1, 3.4] either contains θ or does not.

7. **Intervals come from exact laws, the central limit theorem or concentration.** For normal data with unknown variance, William Sealy Gosset, writing as "Student" (1908), found the exact law of (X̄ − μ)/(S/√n), where S² is the sample variance: the t distribution with n − 1 degrees of freedom. For large n the central limit theorem gives the approximate interval X̄ ± 1.96·S/√n at 95%. For observations in [0, 1], Hoeffding's inequality gives X̄ ± √(log(2/α)/(2n)), valid at every n but wider.

## Key concepts

| Term | Meaning |
|---|---|
| Null hypothesis H₀ | The default claim a test is designed to reject only on strong evidence |
| Size, or level α | Probability of rejecting H₀ when it is true |
| Power | Probability of rejecting H₀ when the alternative is true |
| Likelihood ratio | f₁(x)/f₀(x), the factor by which the data favour H₁ over H₀ |
| UMP test | A test most powerful against every alternative simultaneously |
| p-value | Probability under H₀ of a result at least as extreme as the one observed |
| False discovery rate | The expected proportion of false rejections among all rejections |
| Confidence interval | A random interval covering the true parameter with probability 1 − α |

## How it fits

- **Below:** [likelihood](estimation-and-likelihood.md) supplies the test statistics; the [central limit theorem](../02-limit-theorems/the-central-limit-theorem.md) and [concentration inequalities](../02-limit-theorems/concentration-inequalities.md) supply approximate and exact-at-every-n intervals.
- **Above:** [clinical trials](../../../medicine-first-principles/10-epidemiology-and-evidence/02-evidence-based-medicine/randomized-controlled-trials.md) are designed around size and power; the replication crisis and [publication bias](../../../medicine-first-principles/10-epidemiology-and-evidence/02-evidence-based-medicine/research-integrity-and-publication-bias.md) are partly tenet 5 at scale, a theme of [mathematics and society](../../15-mathematics-in-context/mathematics-and-society.md).
- **Siblings:** t and F tests for coefficients are the workhorses of [linear models](linear-models-and-regression.md); [Bayesian inference](bayesian-inference.md) answers the question a p-value is often mistaken for, the probability of the hypothesis given the data.

## Common misconceptions

- **"p = 0.03 means a 3% chance that H₀ is true"**: it is a probability of data given H₀, not of H₀ given data. Converting one into the other needs a prior, as tenet 5 shows.
- **"A 95% interval contains θ with probability 95%"**: before the data are seen, the random interval does; afterwards, a fixed interval either contains θ or not. A Bayesian credible interval makes the other statement.
- **"Not significant means no effect"**: a small study can have low power, so a large p-value may reflect too little data rather than a null effect.

## Go deeper

- Erich Lehmann and Joseph Romano, *Testing Statistical Hypotheses* (3rd edition, 2005): the Neyman–Pearson theory in full.
- Larry Wasserman, *All of Statistics* (2004): tests, intervals and multiple testing in one concise course.
- Jerzy Neyman and Egon Pearson, "On the problem of the most efficient tests of statistical hypotheses" (1933): the paper that introduced the lemma.
