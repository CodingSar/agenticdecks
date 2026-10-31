# Estimation and Likelihood

> **Layer:** [11 Probability and Statistics](../README.md) › [Statistical Inference](README.md)
> **Builds on:** [Random Variables and Distributions](../01-measure-theoretic-probability/random-variables-and-distributions.md), [The Law of Large Numbers](../02-limit-theorems/the-law-of-large-numbers.md), [The Central Limit Theorem](../02-limit-theorems/the-central-limit-theorem.md), [Conditional Expectation](../01-measure-theoretic-probability/conditional-expectation.md), [Estimates and Inequalities](../../06-real-analysis/01-limits-and-convergence/estimates-and-inequalities.md)
> **Enables:** [Hypothesis Tests and Confidence Intervals](hypothesis-tests-and-confidence-intervals.md), [Bayesian Inference](bayesian-inference.md), [Linear Models and Regression](linear-models-and-regression.md), [Information Theory](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/information-theory.md), [Statistical Learning Theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md)

## Essence

Probability goes from a known distribution to data; statistics goes back. A statistical model is a family of distributions P_θ indexed by a parameter θ, and an estimator is any function of the data used to guess θ. The likelihood, the density of the observed data viewed as a function of θ, is the common currency of inference. Ronald Fisher (1922) proposed the maximum likelihood estimator (MLE): choose the θ that makes the data most probable. For large samples it is consistent and approximately normal with the smallest possible variance, a bound set by the Fisher information, the curvature of the log-likelihood. Each of these guarantees has a counterexample that shows where it stops.

## Core tenets

1. **Error splits into bias and variance, and unbiasedness is not the goal.** The mean squared error (MSE) of an estimator T of θ decomposes as E[(T − θ)²] = (E[T] − θ)² + Var(T). For normal data, the unbiased variance estimate divides ∑(Xᵢ − X̄)² by n − 1, but dividing by n + 1 gives smaller MSE. Charles Stein (1956) showed that in three or more dimensions even the sample mean of a normal vector is inadmissible, and the James–Stein estimator (1961), which shrinks it towards a point, has smaller MSE for every value of the mean.

2. **Sufficient statistics keep all the information, and conditioning on them improves estimators.** A statistic S is sufficient when the conditional law of the data given S does not depend on θ; by the factorisation theorem this holds exactly when the likelihood factors as g(S, θ)·h(data). For n coin tosses, the number of heads is sufficient. The Rao–Blackwell theorem replaces any estimator T by E[T ∣ S]: the bias is unchanged, and by the conditional variance decomposition the variance can only fall.

3. **Maximum likelihood is consistent because of the Kullback–Leibler divergence.** For independent and identically distributed (i.i.d.) observations with density f(x; θ), the MLE maximises (1/n)·∑ log f(Xᵢ; θ). By the law of large numbers this tends to E_θ₀[log f(X; θ)], where θ₀ is the true parameter, and the gap E_θ₀[log f(X; θ₀)] − E_θ₀[log f(X; θ)] is the Kullback–Leibler divergence, which is non-negative by Jensen's inequality and zero only at θ₀ for an identifiable model. For normal data the MLE of the mean is X̄; for coin tosses, the proportion of heads.

4. **Fisher information measures how sharply the data pin down θ.** The score is the derivative of the log-likelihood, U(θ) = ∂/∂θ log f(X; θ). Under smoothness conditions it has mean 0, and its variance is the Fisher information I(θ) = E[U(θ)²] = −E[∂²/∂θ² log f(X; θ)], the expected curvature of the log-likelihood. For one toss of a coin with heads probability p, I(p) = 1/(p(1 − p)): information is lowest at p = 1/2, where outcomes are least predictable.

5. **The Cramér–Rao bound limits every unbiased estimator.** Cauchy–Schwarz applied to the covariance of T and the score, which equals 1 for unbiased T, gives

   ```
   Var(T)  ≥  1 / (n·I(θ))       for every unbiased estimator T based on n i.i.d. observations
   ```

   This was proved independently by C. R. Rao (1945) and Harald Cramér (1946). The regularity conditions matter: for the uniform law on [0, θ], whose support moves with θ, the unbiased estimator ((n + 1)/n)·max Xᵢ has variance θ²/(n(n + 2)), of order 1/n², faster than any bound of order 1/n.

6. **The MLE is asymptotically normal and efficient.** Expanding the score around θ₀ to first order gives √n·(θ̂ − θ₀) ≈ (1/√n)·∑ U(Xᵢ; θ₀) divided by I(θ₀). The numerator is a sum of independent mean-zero terms with variance I(θ₀), so by the central limit theorem

   ```
   √n·(θ̂ₙ − θ₀)  →  N(0, 1/I(θ₀))   in distribution.
   ```

   The MLE attains the Cramér–Rao bound in the limit, and the observed curvature of the log-likelihood gives standard errors.

7. **The theory has limits, and they are instructive.** In the Neyman–Scott problem (1948), n pairs of normal observations each have their own mean but share a variance σ²; the number of parameters grows with n, and the MLE of σ² converges to σ²/2. When the model is wrong, the MLE converges to the member closest to the truth in Kullback–Leibler divergence, which may be far from it. In high dimensions, where parameters are as numerous as observations, regularisation and shrinkage replace pure maximum likelihood.

## Key concepts

| Term | Meaning |
|---|---|
| Statistical model | A family of distributions P_θ, θ in a parameter set Θ |
| Estimator | A function of the data used to guess θ |
| Likelihood L(θ) | The density of the observed data as a function of θ |
| Mean squared error | E[(T − θ)²] = bias² + variance |
| Sufficient statistic | A summary given which the data carry no further information about θ |
| Score | The derivative of the log-likelihood in θ |
| Fisher information I(θ) | The variance of the score, the expected curvature of the log-likelihood |
| Efficiency | Attaining the Cramér–Rao bound, exactly or asymptotically |

## How it fits

- **Below:** the [law of large numbers](../02-limit-theorems/the-law-of-large-numbers.md) gives consistency, the [central limit theorem](../02-limit-theorems/the-central-limit-theorem.md) asymptotic normality, [conditional expectation](../01-measure-theoretic-probability/conditional-expectation.md) Rao–Blackwell, and Cauchy–Schwarz and Jensen from [estimates and inequalities](../../06-real-analysis/01-limits-and-convergence/estimates-and-inequalities.md) in 06 give Cramér–Rao and consistency.
- **Above:** computing an MLE is an optimisation problem, often [convex](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md); the Kullback–Leibler divergence is central to [information theory](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/information-theory.md); training a classifier by minimising cross-entropy is maximum likelihood ([statistical learning theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md)).
- **Siblings:** likelihood ratios give the best [tests](hypothesis-tests-and-confidence-intervals.md); multiplying the likelihood by a prior gives [Bayesian inference](bayesian-inference.md); for normal errors, least squares in [linear models](linear-models-and-regression.md) is maximum likelihood.

## Common misconceptions

- **"Unbiased estimators are best"**: shrinkage trades a little bias for a large drop in variance, and James–Stein shows that this can win everywhere at once.
- **"The likelihood is the probability that θ is true"**: it is a function of θ that need not integrate to 1. Turning it into a probability for θ requires a prior.
- **"Maximum likelihood is always consistent"**: it fails when parameters grow with the sample, as in Neyman–Scott, or when the model is badly misspecified.

## Go deeper

- George Casella and Roger Berger, *Statistical Inference* (2nd edition, 2002): the standard introduction to estimation and testing.
- Erich Lehmann and George Casella, *Theory of Point Estimation* (2nd edition, 1998): sufficiency, efficiency and shrinkage in depth.
- A. W. van der Vaart, *Asymptotic Statistics* (1998): the modern asymptotic theory of maximum likelihood.
