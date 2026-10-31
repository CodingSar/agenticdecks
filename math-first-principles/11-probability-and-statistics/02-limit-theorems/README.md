# Limit Theorems

> **Layer:** [11 Probability and Statistics](../README.md) › Limit Theorems
> **Children:** [Modes of Convergence](modes-of-convergence.md) · [The Law of Large Numbers](the-law-of-large-numbers.md) · [The Central Limit Theorem](the-central-limit-theorem.md) · [Concentration Inequalities](concentration-inequalities.md)

## What this area is about

A single random outcome is unpredictable; the sum of many independent ones is not. This area makes that precise for Sₙ = X₁ + … + Xₙ, a sum of n independent and identically distributed (i.i.d.) terms with mean μ and variance σ², by describing it at successive scales:

```
scale n:          Sₙ/n → μ                                law of large numbers
scale √n:         (Sₙ − nμ)/(σ√n) → N(0, 1)               central limit theorem (CLT)
just above √n:    lim sup (Sₙ − nμ)/(σ√(2n log log n)) = 1  law of the iterated logarithm
deviations ~ n:   P(Sₙ ≥ na) ≈ e^(−n·I(a)) for a > μ       large deviations, concentration
```

Here I is a rate function that is 0 at μ and positive elsewhere. Each line is a different kind of statement, and the first child of the area says what kinds there are: almost sure convergence, convergence in probability, in mean and in distribution. Together these theorems are the reason that probability can be measured, that sampling works and that statistics is possible at all.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Modes of convergence](modes-of-convergence.md) | The four senses in which random variables converge, their implications and counterexamples | Nothing in this layer |
| [The law of large numbers](the-law-of-large-numbers.md) | Averages converge to the mean, weakly and strongly, exactly when the mean is finite | Modes of convergence |
| [The central limit theorem](the-central-limit-theorem.md) | Fluctuations of size σ/√n are asymptotically normal; Lindeberg, Berry–Esseen, stable laws | Modes of convergence, the law of large numbers |
| [Concentration inequalities](concentration-inequalities.md) | Exponential bounds on deviations at every n, from Markov to Hoeffding and McDiarmid | The law of large numbers, the central limit theorem |

Read them in order. The first supplies the language and its pitfalls. The second is the first-order statement, and its proofs introduce the shared tools: truncation, the Borel–Cantelli lemmas and Chebyshev's inequality. The third zooms in to the √n scale using characteristic functions. The fourth trades exact limits for honest bounds at finite n, which is what applications need. Asymptotic and non-asymptotic results answer different questions: the CLT gives the right shape of the fluctuations but no guarantee at a given n, while concentration gives a guarantee with a slightly wrong constant.

```
              modes of convergence
         (almost surely, in probability, Lᵖ, in distribution)
                        │
                        ▼
            law of large numbers  (scale n)
               │                       │
               ▼                       ▼
   central limit theorem (scale √n)   concentration (exponential tails, every n)
               │                       │
               └───────────┬───────────┘
                           ▼
            statistical inference and learning
```

## Connections to sibling areas

- **[Measure-theoretic probability](../01-measure-theoretic-probability/README.md):** supplies independence, the Borel–Cantelli lemmas, the zero–one laws that make limits deterministic, and characteristic functions.
- **[Stochastic processes](../03-stochastic-processes/README.md):** the ergodic theorem for Markov chains is a law of large numbers without independence; martingale convergence generalises the strong law; Donsker's theorem turns the CLT into Brownian motion; quadratic variation of Brownian motion is itself a law of large numbers.
- **[Statistical inference](../04-statistical-inference/README.md):** consistency of an estimator is a law of large numbers, asymptotic normality of maximum likelihood is a CLT, and confidence intervals come from either the CLT or concentration bounds.

## Connections across layers

From below, the area rests on the [discrete probability](../../03-combinatorics-and-graph-theory/03-discrete-probability/README.md) of 03 (expectation, variance, Chebyshev), on the [Lᵖ spaces](../../09-advanced-analysis/01-measure-and-integration/lp-spaces.md) and the [Fourier transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md) of 09, on [Taylor expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md) in 06, and on [ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md) in 10, which extends the strong law to stationary sequences.

Upward, [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md), [statistical learning theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md) and [random matrices](../../14-applied-and-computational-mathematics/06-data-and-learning/high-dimensional-geometry-and-random-matrices.md) in 14 are applications of these theorems. In number theory, the Erdős–Kac theorem (1940) shows that the number of prime factors of a typical integer obeys a central limit theorem, as if divisibility by different primes were independent ([sieves](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/sieves-and-additive-problems.md)). The computer-science view is in the sibling tree's [probability and statistics](../../../cs-first-principles/01-mathematical-foundations/06-probability-and-statistics/README.md).

## Cross-cutting threads

- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): the whole area is the statement that averaging independent randomness produces near-certainty.
- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): the normal approximation and its Berry–Esseen error bound are a model of an approximation with a quantified rate.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): characteristic functions translate sums of independent variables into products, and limit theorems into Fourier analysis.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): the Cauchy law, whose averages never settle, marks exactly where the hypotheses cannot be weakened.
