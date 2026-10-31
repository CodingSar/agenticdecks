# The Central Limit Theorem

> **Layer:** [11 Probability and Statistics](../README.md) › [Limit Theorems](README.md)
> **Builds on:** [Modes of Convergence](modes-of-convergence.md), [The Law of Large Numbers](the-law-of-large-numbers.md), [Random Variables and Distributions](../01-measure-theoretic-probability/random-variables-and-distributions.md), [The Fourier Transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md), [Taylor Expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md)
> **Enables:** [Concentration Inequalities](concentration-inequalities.md), [Brownian Motion](../03-stochastic-processes/brownian-motion.md), [Hypothesis Tests and Confidence Intervals](../04-statistical-inference/hypothesis-tests-and-confidence-intervals.md), [Estimation and Likelihood](../04-statistical-inference/estimation-and-likelihood.md), [High-Dimensional Geometry and Random Matrices](../../14-applied-and-computational-mathematics/06-data-and-learning/high-dimensional-geometry-and-random-matrices.md)

## Essence

The law of large numbers says that the average of n independent and identically distributed (i.i.d.) observations tends to their mean μ; the Central Limit Theorem (CLT) says how it fluctuates on the way. The error is of size σ/√n, where σ² is the variance, and rescaled by that factor it is approximately standard normal, whatever the distribution of the observations, provided only that the variance is finite. This is why the bell curve appears wherever many small independent effects add up. The proof is Fourier analysis: characteristic functions turn sums into products, and every one with mean 0 and variance σ² looks like 1 − σ²t²/2 near t = 0.

## Core tenets

1. **The theorem (Lindeberg–Lévy form).** With Φ the standard normal distribution function:

   ```
   X₁, X₂, … i.i.d.,  E[X₁] = μ,  Var(X₁) = σ² with 0 < σ² < ∞,  Sₙ = X₁ + … + Xₙ.
   Then for every real x:
       P( (Sₙ − nμ)/(σ√n) ≤ x )  →  Φ(x) = (1/√(2π)) ∫_(−∞)^x e^(−u²/2) du.
   ```

   Abraham de Moivre found the coin-tossing case in 1733, Pierre-Simon Laplace extended it in 1812, and George Pólya named it in 1920. The scaling √n is forced: Sₙ − nμ has standard deviation σ√n.

2. **The proof is a Taylor expansion of the characteristic function.** Standardise so that μ = 0 and σ = 1. A finite second moment allows two differentiations under the integral, so φ(t) = E[e^(itX₁)] = 1 − t²/2 + r(t) with r(t)/t² → 0 as t → 0. Independence turns the sum into a product, so Sₙ/√n has characteristic function

   ```
   φ(t/√n)ⁿ  =  (1 − t²/(2n) + r(t/√n))ⁿ  →  e^(−t²/2),
   ```

   the characteristic function of the standard normal, and Lévy's continuity theorem converts this into convergence in distribution. Only the first two moments enter, which is why the limit is universal.

3. **The normal law is the fixed point of adding and rescaling.** If X and X′ are independent standard normals, (X + X′)/√2 is again standard normal. Heuristically, the cumulants κₖ (the coefficients of log φ) add over independent terms, so the k-th cumulant of Sₙ/√n is n·κₖ/n^(k/2) → 0 for every k ≥ 3: only mean and variance survive, and a law with no higher cumulants is normal.

4. **Non-identical terms need the Lindeberg condition.** For independent Xₖ with mean 0 and variance σₖ², put sₙ² = σ₁² + … + σₙ². Jarl Waldemar Lindeberg (1922) proved Sₙ/sₙ → N(0, 1) in distribution under the condition

   ```
   for every ε > 0:   (1/sₙ²) ∑_(k ≤ n) E[ Xₖ² · 1{∣Xₖ∣ > ε·sₙ} ]  →  0,
   ```

   which says that no single term carries a noticeable share of the variance. William Feller (1935) showed that it is also necessary when maxₖ σₖ²/sₙ² → 0. It fails when one term dominates: for Xₖ = ±2^(k/2) with independent fair signs, each new term carries about half the total variance, and Sₙ/sₙ converges to a law confined to ∣x∣ ≤ 1/(√2 − 1) ≈ 2.414, which is not normal. Lindeberg's proof, swapping terms one at a time for normal ones, now drives universality theorems for random matrices.

5. **The Berry–Esseen theorem gives the rate, and the rate is sharp.** If ρ = E∣X₁ − μ∣³ < ∞, then for all x and n,

   ```
   ∣ P( (Sₙ − nμ)/(σ√n) ≤ x ) − Φ(x) ∣  ≤  C·ρ/(σ³·√n),
   ```

   with a universal constant C, by Andrew Berry (1941) and Carl-Gustav Esseen (1942); C < 0.5 is now known. The rate 1/√n cannot be improved: for fair coins, P(Sₙ ≤ x) jumps by P(Sₙ = n/2) ≈ √(2/(πn)) at the centre, about 0.08 at n = 100, and the continuous Φ cannot follow a jump. It controls the bulk, not the far tails.

6. **Without a finite variance the limit need not be normal.** For the standard Cauchy law, Sₙ/n is again standard Cauchy, so the right scaling is n, not √n, and the limit is Cauchy rather than normal. More generally, if both tails behave like c·x^(−α) with 0 < α < 2, the sum, centred when α > 1, must be divided by n^(1/α), and the limit is one of Paul Lévy's α-stable laws, whose tails are just as heavy.

7. **The theorem extends in every direction.** For random vectors with covariance matrix Σ, (Sₙ − nμ)/√n → N(0, Σ), by applying the one-dimensional theorem to every linear combination ⟨a, Sₙ⟩. Martingales and Markov chains have central limit theorems too. Donsker's theorem (1951) is the functional version: the rescaled path of a random walk converges to [Brownian motion](../03-stochastic-processes/brownian-motion.md).

## Key concepts

| Term | Meaning |
|---|---|
| Standard normal law N(0, 1) | The law with density (1/√(2π))·e^(−x²/2) and distribution function Φ |
| Characteristic function | φ(t) = E[e^(itX)], the Fourier transform of the law |
| Cumulants | The coefficients κₖ in log φ(t) = ∑ₖ κₖ·(it)ᵏ/k!; they add over independent terms |
| Lindeberg condition | No single term carries a noticeable share of the total variance |
| Berry–Esseen bound | A uniform error bound of order ρ/(σ³√n) for the normal approximation |
| Stable law | A law that independent copies of itself reproduce when summed and rescaled |

## How it fits

- **Below:** characteristic functions are the [Fourier transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md) of 09; [Taylor expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md) in 06 gives the expansion of φ; Lévy's continuity theorem comes from [modes of convergence](modes-of-convergence.md).
- **Above:** most [confidence intervals and tests](../04-statistical-inference/hypothesis-tests-and-confidence-intervals.md) rest on it, and asymptotic normality of [maximum likelihood](../04-statistical-inference/estimation-and-likelihood.md) is a central limit theorem for the score; in 12, the Erdős–Kac theorem says that the number of distinct prime factors of an integer is approximately normal ([sieves](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/sieves-and-additive-problems.md)).
- **Siblings:** the [law of large numbers](the-law-of-large-numbers.md) is the first-order statement and the CLT its √n correction; [concentration inequalities](concentration-inequalities.md) give bounds valid at every n, including the tails.

## Common misconceptions

- **"The CLT says data are normal"**: it is about averages, not single observations. Incomes stay skewed however many are observed.
- **"n = 30 is always enough"**: the error depends on the skewness through ρ/σ³. For thirty tosses of a coin with success probability 0.01, the sum is 0 about three times in four, nothing like a bell curve.
- **"Any sum of many small effects is normal"**: the effects must be independent, or nearly so, with finite variance and no dominant term. Correlated shocks and heavy tails break it, as market crashes show.

## Go deeper

- William Feller, *An Introduction to Probability Theory and Its Applications*, Volume 2 (2nd edition, 1971): Lindeberg, Berry–Esseen and stable laws in one classic.
- Rick Durrett, *Probability: Theory and Examples* (5th edition, 2019): a modern proof of every form above.
- Hans Fischer, *A History of the Central Limit Theorem: From Classical to Modern Probability Theory* (2011): how the theorem grew from Laplace to Lévy and Feller.
