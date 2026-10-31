# The Law of Large Numbers

> **Layer:** [11 Probability and Statistics](../README.md) › [Limit Theorems](README.md)
> **Builds on:** [Modes of Convergence](modes-of-convergence.md), [Independence and Zero–One Laws](../01-measure-theoretic-probability/independence-and-zero-one-laws.md), [Random Variables and Distributions](../01-measure-theoretic-probability/random-variables-and-distributions.md), [Expectation and Variance](../../03-combinatorics-and-graph-theory/03-discrete-probability/expectation-and-variance.md)
> **Enables:** [The Central Limit Theorem](the-central-limit-theorem.md), [Concentration Inequalities](concentration-inequalities.md), [Markov Chains](../03-stochastic-processes/markov-chains.md), [Estimation and Likelihood](../04-statistical-inference/estimation-and-likelihood.md), [Monte Carlo Methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md)

## Essence

Let X₁, X₂, … be independent and identically distributed (i.i.d.) random variables with mean μ = E[X₁], and let X̄ₙ = (X₁ + … + Xₙ)/n be the average of the first n. The law of large numbers says that X̄ₙ → μ: in probability (the weak law) and almost surely (the strong law). It is why probabilities can be measured as frequencies, why sampling works and why Monte Carlo simulation is possible. The idea is that averaging cancels independent errors: the variance of X̄ₙ is σ²/n, where σ² is the variance of X₁. A finite mean is exactly the right hypothesis, and the Cauchy distribution, which has none, shows what happens without it.

## Core tenets

1. **With finite variance, the weak law is one line of Chebyshev.** Independence makes variances add, so Var(X̄ₙ) = σ²/n, and Chebyshev's inequality gives P(∣X̄ₙ − μ∣ > ε) ≤ σ²/(nε²) → 0. Only uncorrelatedness was used, not full independence. Jacob Bernoulli proved the case of coin tossing, by direct estimates of binomial sums, in *Ars Conjectandi* (1713).

2. **A finite mean suffices for the weak law.** Aleksandr Khinchin (1929) removed the variance assumption by truncation: split each Xₖ into Xₖ·1{∣Xₖ∣ ≤ n} and Xₖ·1{∣Xₖ∣ > n}. The truncated parts have variance at most E[X₁²·1{∣X₁∣ ≤ n}], which grows more slowly than n when E∣X₁∣ < ∞, so Chebyshev still controls their average. The remainders all vanish except on an event of probability at most n·P(∣X₁∣ > n), which tends to 0. Truncation, keeping the bulk and discarding rare large values, is the basic technique of the subject.

3. **The strong law: X̄ₙ → μ almost surely if and only if E∣X₁∣ < ∞.** With a finite fourth moment there is a short proof. Write Sₙ = X₁ + … + Xₙ; expanding E[(Sₙ − nμ)⁴], only terms whose indices pair up survive, so it is at most C·n² for a constant C. Markov's inequality gives P(∣X̄ₙ − μ∣ > ε) ≤ C/(n²ε⁴), which is summable, and the first Borel–Cantelli lemma finishes. Kolmogorov proved the full theorem with truncation and his maximal inequality; Nasrollah Etemadi (1981) gave an elementary proof needing only pairwise independence, proving convergence along the subsequence ⌊αᵏ⌋ for α > 1 and filling the gaps by monotonicity.

4. **Without a finite mean the average does not settle.** If E∣X₁∣ = ∞, then ∑ₙ P(∣X₁∣ > n) = ∞, because E∣X₁∣ ≤ 1 + ∑ₙ P(∣X₁∣ > n); by the second Borel–Cantelli lemma, ∣Xₙ∣ > n infinitely often. But Xₙ/n = X̄ₙ − ((n − 1)/n)·X̄ₙ₋₁ would tend to 0 if X̄ₙ converged, so X̄ₙ has no finite limit. For the Cauchy law the failure is total: its characteristic function is e^(−∣t∣), so X̄ₙ has characteristic function (e^(−∣t∣/n))ⁿ = e^(−∣t∣) and is again standard Cauchy. Averaging a million measurements is no better than taking one.

5. **The weak law can hold where the strong law fails.** There are constants mₙ with X̄ₙ − mₙ → 0 in probability if and only if x·P(∣X₁∣ > x) → 0 as x → ∞, and then mₙ = E[X₁·1{∣X₁∣ ≤ n}] works. A symmetric law with P(∣X₁∣ > x) of order 1/(x log x) meets this condition, so its averages tend to 0 in probability. Yet E∣X₁∣ = ∞, so by tenet 4, ∣Xₙ∣/n > 1 infinitely often, and the averages do not converge almost surely.

6. **Independence can be traded for stationarity, at the price of ergodicity.** Birkhoff's ergodic theorem (1931) says that for a stationary sequence with E∣X₁∣ < ∞, X̄ₙ converges almost surely: to μ when the sequence is ergodic, and otherwise to a random limit, the conditional expectation given the invariant events ([ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md)). Andrey Markov introduced his chains in 1906 partly to show that the law of large numbers does not need independence. The ergodic theorem for Markov chains is what makes Markov chain Monte Carlo work.

7. **Uniform laws of large numbers underlie statistics and learning.** The empirical distribution function Fₙ(x), the fraction of the first n observations that are at most x, converges to F(x) for each x by the strong law; the Glivenko–Cantelli theorem (1933) says that the convergence is almost surely uniform in x, the starting point of [nonparametric statistics](../04-statistical-inference/nonparametric-statistics-and-the-bootstrap.md). Asking for uniformity over a whole class of events leads to the Vapnik–Chervonenkis dimension and [statistical learning theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md): learning from examples is a uniform law of large numbers over a class of hypotheses.

## Key concepts

| Term | Meaning |
|---|---|
| i.i.d. | Independent, with a common law |
| Sample mean X̄ₙ | (X₁ + … + Xₙ)/n |
| Weak law | X̄ₙ → μ in probability |
| Strong law | X̄ₙ → μ almost surely |
| Chebyshev's inequality | P(∣Y − E[Y]∣ ≥ a) ≤ Var(Y)/a² for every a > 0 |
| Truncation | Splitting a variable into a bounded part and a rare large part, handled separately |
| Stationary sequence | A sequence whose joint laws are unchanged by a shift of time |
| Empirical distribution function | Fₙ(x) = (number of i ≤ n with Xᵢ ≤ x)/n |

## How it fits

- **Below:** Chebyshev's inequality and the variance of a sum come from [expectation and variance](../../03-combinatorics-and-graph-theory/03-discrete-probability/expectation-and-variance.md) in 03; the proofs run on the [Borel–Cantelli lemmas](../01-measure-theoretic-probability/independence-and-zero-one-laws.md) and the [modes of convergence](modes-of-convergence.md).
- **Above:** [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md) in 14 estimate an integral as an average of random samples, with error of order σ/√n; consistency of an [estimator](../04-statistical-inference/estimation-and-likelihood.md) is usually a law of large numbers.
- **Siblings:** the [central limit theorem](the-central-limit-theorem.md) describes the fluctuations of X̄ₙ around μ, of size σ/√n, that this law says vanish; [concentration inequalities](concentration-inequalities.md) bound the probability of a deviation of size ε at a fixed n, exponentially small in n.

## Common misconceptions

- **"After many heads, tails is due"**: this is the gambler's fallacy. The tosses are independent and the law says nothing about the next one. The number of heads minus n/2 typically grows like √n; only the proportion converges, because the difference is divided by n.
- **"Averages always converge"**: they need a finite mean. Cauchy averages are as spread out as one observation, and heavy-tailed data such as insurance losses can come close to this.
- **"The strong law is the weak law with a better proof"**: they are different statements. The weak law allows the average to stray from μ infinitely often, provided each straying becomes rarer; the strong law forbids it for almost every sequence of outcomes.

## Go deeper

- William Feller, *An Introduction to Probability Theory and Its Applications*, Volume 1 (3rd edition, 1968): the law for coin tossing, with its fallacies discussed head on.
- Rick Durrett, *Probability: Theory and Examples* (5th edition, 2019): every proof mentioned here, including Etemadi's.
- Persi Diaconis and Brian Skyrms, *Ten Great Ideas about Chance*: the law of large numbers in its historical and philosophical setting.
