# 11 Probability and Statistics

> **Layer:** 11 Probability and Statistics
> **Children:** [Measure-Theoretic Probability](01-measure-theoretic-probability/README.md) · [Limit Theorems](02-limit-theorems/README.md) · [Stochastic Processes](03-stochastic-processes/README.md) · [Statistical Inference](04-statistical-inference/README.md)

## What this area is about

This layer makes chance rigorous and then turns it around to learn from data. Probability began with games: Blaise Pascal and Pierre de Fermat solved the problem of dividing the stakes of an interrupted game in their correspondence of 1654. For nearly three centuries it had no agreed foundation beyond finite cases, until Andrey Kolmogorov (1933) defined a probability as a measure of total mass 1. That single move imports the whole of measure theory and lets one speak precisely about infinitely many coin tosses, a point chosen from an interval or the path of a diffusing particle.

The layer's first area sets up that framework. The second proves the great limit theorems: averages converge to means (the law of large numbers), fluctuations around them are normal (the Central Limit Theorem, CLT), and large deviations are exponentially rare (concentration). The third studies random evolution in time: Markov chains in discrete and continuous time, Poisson processes, martingales, Brownian motion and the stochastic calculus built on it. The fourth inverts the direction, from data back to the distribution that produced them, with or without a parametric model.

The contribution to the stack is **randomness as structure**: independence, conditioning and averaging, which turn uncertainty about single outcomes into near-certainty about aggregates.

## Why this layer sits here

Probability needs analysis that only arrives late in the stack. From [advanced analysis](../09-advanced-analysis/README.md) in 09 it takes measure, the Lebesgue integral, Lᵖ spaces, the Radon–Nikodym theorem and the Fourier transform. From [discrete probability](../03-combinatorics-and-graph-theory/03-discrete-probability/README.md) in 03 it takes the finite case, which it generalises rather than repeats. From [linear algebra](../04-linear-algebra/README.md) in 04 it takes Perron–Frobenius for Markov chains, and projections and the singular value decomposition (SVD) for regression. From [real analysis](../06-real-analysis/README.md) in 06 it takes Taylor expansion and the basic inequalities. From [differential equations and dynamics](../10-differential-equations-and-dynamics/README.md) in 10 it takes the heat equation, which Brownian motion solves, and ergodic theory, which generalises the strong law. From [sets and foundations](../01-sets-and-foundations/README.md) it takes the axiom of choice, which produces sets that cannot be assigned a probability.

Above it, number theory borrows probabilistic models, metamathematics asks what a random sequence is, applied mathematics computes with randomness, and the philosophy of mathematics asks what probability means.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Measure-theoretic probability](01-measure-theoretic-probability/README.md) | The framework: probability spaces, random variables, independence, conditional expectation | Nothing in this layer |
| [Limit theorems](02-limit-theorems/README.md) | What happens to sums of many independent terms: laws of large numbers, CLT, concentration | Measure-theoretic probability |
| [Stochastic processes](03-stochastic-processes/README.md) | Random evolution with dependence: Markov chains, Poisson processes, martingales, Brownian motion, Itô calculus | Measure-theoretic probability, limit theorems |
| [Statistical inference](04-statistical-inference/README.md) | Learning about the distribution from data: estimation, testing, Bayesian methods, regression, the bootstrap | Measure-theoretic probability, limit theorems, stochastic processes |

The four areas form a stack with a fork at the top. The framework comes first, because every later statement is about measures and measurable functions. The limit theorems come next, because they are the reason probability says anything definite. Stochastic processes and statistical inference both build on the limit theorems, and each borrows from the other: Markov chain Monte Carlo powers Bayesian computation, and martingales prove that posteriors are consistent.

```
            measure-theoretic probability
      (Ω, ℱ, P), random variables, independence, E[X ∣ 𝒢]
                           │
                           ▼
                    limit theorems
           law of large numbers, CLT, concentration
                ┌──────────┴──────────┐
                ▼                     ▼
      stochastic processes ───► statistical inference
   chains, martingales,      estimation, tests, Bayes,
   Brownian motion, Itô      regression
```

## Connections to neighbouring layers

- **[03 Combinatorics and graph theory](../03-combinatorics-and-graph-theory/README.md):** finite probability and the probabilistic method are the discrete case; random walks live on graphs.
- **[04 Linear algebra](../04-linear-algebra/README.md):** stochastic matrices, Perron–Frobenius, orthogonal projection for conditional expectation and least squares, covariance matrices as positive semi-definite forms.
- **[09 Advanced analysis](../09-advanced-analysis/README.md):** the foundations, from σ-algebras to the Fourier transform that proves the CLT.
- **[10 Differential equations and dynamics](../10-differential-equations-and-dynamics/README.md):** the heat equation is Brownian motion averaged, and ergodic theory is the law of large numbers for stationary systems.
- **[12 Number theory and algebraic geometry](../12-number-theory-and-algebraic-geometry/README.md):** Harald Cramér's random model of the primes (1936) and the Erdős–Kac theorem treat divisibility as if it were chance.
- **[13 Structure and metamathematics](../13-structure-and-metamathematics/README.md):** Solovay's model shows the role of choice in non-measurable sets, and Per Martin-Löf (1966) defined a random sequence by computability.
- **[14 Applied and computational mathematics](../14-applied-and-computational-mathematics/README.md):** Monte Carlo methods, mathematical finance, statistical learning theory and random matrices are built directly on this layer.
- **[15 Mathematics in context](../15-mathematics-in-context/README.md):** the interpretation of probability, and the use and misuse of statistical evidence in science and society.

## Connections across layers

The computer-science tree treats the same material as a tool for algorithms and machine learning in its [probability and statistics](../../cs-first-principles/01-mathematical-foundations/06-probability-and-statistics/README.md) area; the medicine tree applies it to diagnosis, trials and causal questions in its [quantitative and scientific foundations](../../medicine-first-principles/01-quantitative-and-scientific-foundations/README.md). This layer supplies the proofs that both take as given.

## Cross-cutting threads

- [Randomness and averaging](../CROSS-CUTTING.md#randomness-and-averaging): the layer's central theme, from the law of large numbers to ergodic averages along Markov chains.
- [Abstraction and generalisation](../CROSS-CUTTING.md#abstraction-and-generalisation): Kolmogorov's axioms make probability a special case of measure theory.
- [Approximation and limits](../CROSS-CUTTING.md#approximation-and-limits): the normal approximation, Donsker's theorem and asymptotic statistics.
- [Existence and construction](../CROSS-CUTTING.md#existence-and-construction): infinite product measures, Wiener measure and conditional expectations exist by abstract theorems.
- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): non-measurable sets, the Cauchy law that breaks the limit theorems, the Cramér–Rao bound.
- [Extremal principles and optimisation](../CROSS-CUTTING.md#extremal-principles-and-optimisation): maximum likelihood, least squares and most powerful tests.
- [Dictionaries between fields](../CROSS-CUTTING.md#dictionaries-between-fields): conditioning as projection, sums as products of characteristic functions, diffusions as partial differential equations.
- [Symmetry](../CROSS-CUTTING.md#symmetry): exchangeability, and the reflection principle for Brownian motion.
