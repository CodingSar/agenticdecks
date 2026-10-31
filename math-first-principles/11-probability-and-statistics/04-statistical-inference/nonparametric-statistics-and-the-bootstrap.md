# Nonparametric Statistics and the Bootstrap

> **Layer:** [11 Probability and Statistics](../README.md) › [Statistical Inference](README.md)
> **Builds on:** [Estimation and Likelihood](estimation-and-likelihood.md), [Hypothesis Tests and Confidence Intervals](hypothesis-tests-and-confidence-intervals.md), [The Law of Large Numbers](../02-limit-theorems/the-law-of-large-numbers.md), [The Central Limit Theorem](../02-limit-theorems/the-central-limit-theorem.md), [Concentration Inequalities](../02-limit-theorems/concentration-inequalities.md)
> **Enables:** [Statistical Learning Theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md), [Monte Carlo Methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md), [Statistical Inference (CS)](../../../cs-first-principles/01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md)

## Essence

Parametric inference assumes a family indexed by a few numbers, such as the normal distributions, and is only as good as that assumption. Nonparametric statistics drops it and lets the data speak about the whole distribution. Three ideas carry the field. The sample's empirical distribution converges to the truth uniformly, at a known rate. Ranks and permutations give tests whose null distribution is exact whatever the underlying law. And the bootstrap estimates the variability of almost any statistic by recomputing it on samples drawn from the data themselves, trading mathematics for computation.

## Core tenets

1. **The empirical distribution estimates everything at once.** For a sample X₁, …, Xₙ that is independent and identically distributed (i.i.d.) from F, the empirical distribution function F̂ₙ(x) is the fraction of observations ≤ x. For each x it is an average of indicators, so it is unbiased with variance F(x)(1 − F(x))/n. The Glivenko–Cantelli theorem (1933) strengthens pointwise convergence to sup_x ∣F̂ₙ(x) − F(x)∣ → 0 almost surely, and the Dvoretzky–Kiefer–Wolfowitz inequality, with Massart's sharp constant, gives P(sup ∣F̂ₙ − F∣ > ε) ≤ 2e^(−2nε²). With n = 1,000, a band of ±0.043 around F̂ₙ contains the whole of F with probability at least 95%.

2. **Kolmogorov–Smirnov compares distributions without parameters.** For continuous F, the statistic Dₙ = sup ∣F̂ₙ − F∣ has the same distribution whatever F is, because applying F to the data turns them into uniform variables without changing Dₙ. Kolmogorov found the limit law of √n·Dₙ in 1933; its 95% point is about 1.36, so reject when Dₙ > 1.36/√n. Smirnov's two-sample version compares two empirical distribution functions.

3. **Ranks give exact, distribution-free tests.** If two samples come from the same continuous distribution, all assignments of the ranks 1, …, m + n to the two groups are equally likely, so the null distribution of any rank statistic can be computed by counting. The Wilcoxon rank-sum test (1945), equivalent to the Mann–Whitney test (1947), uses the sum of one group's ranks; the sign and signed-rank tests do the same for a median. The cost is small: against normal data the Wilcoxon test has asymptotic efficiency 3/π ≈ 0.955 relative to the t-test, and Hodges and Lehmann showed in 1956 that it never falls below 0.864.

4. **Permutation tests are exact under exchangeability.** If the null hypothesis says that group labels are irrelevant, so the data are exchangeable, then every relabelling of the data is equally likely. Recomputing any statistic over all relabellings, or a large random sample of them, gives its exact null distribution; with B random relabellings the p-value (1 + #{relabelled statistics ≥ observed})/(1 + B) is valid at every B. Fisher introduced the idea in 1935. Randomisation in an experiment guarantees the exchangeability by design.

5. **Density estimation trades bias against variance.** The kernel estimate f̂(x) = (1/(nh))·∑ K((x − Xᵢ)/h) spreads each observation into a bump of width h. Its bias is of order h², from the curvature of f, and its variance is of order 1/(nh), from the few points in each window. Balancing them gives h ∝ n^(−1/5) and mean squared error of order n^(−4/5), slower than the 1/n of a correct parametric model. In d dimensions the rate falls to n^(−4/(4+d)), a form of the curse of dimensionality.

6. **The bootstrap is the plug-in principle applied to the sampling distribution.** To learn how a statistic θ̂ = T(X₁, …, Xₙ) varies, we would draw fresh samples from F. Efron's bootstrap (1979) draws them from F̂ₙ instead: resample n points with replacement, recompute T, repeat B times, and use the spread of the results as an estimate of the spread of θ̂. Each resample omits a given point with probability (1 − 1/n)ⁿ ≈ e^(−1) ≈ 0.37. No standard-error formula is needed, so medians, correlations and complex algorithms are handled alike.

7. **Bootstrap intervals can beat the normal approximation.** The percentile interval takes quantiles of the resampled θ̂. For smooth statistics, studentised bootstrap intervals, which resample (θ̂ − θ)/(standard error), capture the skewness that the [central limit theorem](../02-limit-theorems/the-central-limit-theorem.md) ignores: Peter Hall's Edgeworth-expansion analysis showed their one-sided coverage error is of order 1/n rather than 1/√n.

8. **The bootstrap fails when the statistic is not smooth in F.** For the maximum of a uniform sample on [0, θ], a resample reproduces the sample maximum with probability 1 − (1 − 1/n)ⁿ → 1 − e^(−1) ≈ 0.63, while the true sampling distribution has no atom, so the bootstrap distribution is wrong at every n. It also fails for the mean of heavy-tailed data with infinite variance, and for dependent data unless whole blocks are resampled. Consistency needs the statistic to depend smoothly on F.

## Key concepts

| Term | Meaning |
|---|---|
| Empirical distribution function F̂ₙ | Fraction of the sample at or below each point |
| Glivenko–Cantelli theorem | F̂ₙ → F uniformly, almost surely |
| Kolmogorov–Smirnov statistic | sup ∣F̂ₙ − F∣, with a distribution free of F |
| Rank test | A test using only the ordering of the data |
| Permutation test | Exact test from recomputing a statistic over relabellings |
| Kernel density estimate | Average of bumps of width h placed at the data |
| Bootstrap | Resampling the data with replacement to estimate sampling variability |
| Plug-in principle | Estimate a feature of F by the same feature of F̂ₙ |

## How it fits

- **Below:** the [law of large numbers](../02-limit-theorems/the-law-of-large-numbers.md) gives Glivenko–Cantelli, [concentration inequalities](../02-limit-theorems/concentration-inequalities.md) give the Dvoretzky–Kiefer–Wolfowitz bound, and [estimation](estimation-and-likelihood.md) supplies the bias–variance language.
- **Above:** cross-validation, the resampling cousin of the bootstrap, chooses models in [statistical learning theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md); the bootstrap is a [Monte Carlo method](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md) applied to F̂ₙ; A/B testing in the computer science tree's [statistical inference](../../../cs-first-principles/01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md) often uses permutation tests and bootstrap intervals.
- **Siblings:** [hypothesis tests](hypothesis-tests-and-confidence-intervals.md) get exact or assumption-light versions here; [linear models](linear-models-and-regression.md) can be bootstrapped by resampling cases or residuals; the Bayesian bootstrap reweights the data with random Dirichlet weights, a link to [Bayesian inference](bayesian-inference.md).

## Common misconceptions

- **"Nonparametric means assumption-free"**: rank and permutation tests still assume independence or exchangeability, and the bootstrap assumes the sample represents the population.
- **"The bootstrap creates new data"**: it reuses the same n points, so it cannot reduce variability or repair a biased sample.
- **"Rank tests waste information"**: they lose about 5% efficiency under normality and gain heavily with heavy tails.

## Go deeper

- Bradley Efron and Robert J. Tibshirani, *An Introduction to the Bootstrap* (1993): the method from its inventor.
- Larry Wasserman, *All of Nonparametric Statistics* (2006): empirical processes, density estimation and the bootstrap in one concise book.
- A. C. Davison and D. V. Hinkley, *Bootstrap Methods and Their Application* (1997): practical resampling for real data, including dependent data.
