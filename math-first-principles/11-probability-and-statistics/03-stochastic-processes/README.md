# Stochastic Processes

> **Layer:** [11 Probability and Statistics](../README.md) › Stochastic Processes
> **Children:** [Markov Chains](markov-chains.md) · [Martingales](martingales.md) · [Brownian Motion](brownian-motion.md) · [Stochastic Calculus](stochastic-calculus.md)

## What this area is about

A stochastic process is a family of random variables indexed by time: a random walk, a queue, a stock price, a diffusing particle. The limit theorems study sums of independent terms; processes allow dependence, but of controlled kinds. Two structural properties, both stated with conditional expectation, organise almost everything. The Markov property says that the future depends on the past only through the present. The martingale property says that the expected future equals the present. A Markov chain is described locally by its one-step transition matrix P, and the global questions (equilibrium, return, hitting probabilities) become linear equations: πP = π for an equilibrium, Ph = h for a harmonic function, and in continuous time the heat equation and its relatives. Brownian motion is the process with both properties in continuous time, and stochastic calculus is the analysis built on it.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Markov chains](markov-chains.md) | Memoryless evolution; stationary distributions, convergence, mixing, recurrence | No earlier child; uses conditional expectation and the law of large numbers |
| [Martingales](martingales.md) | Fair games; optional stopping and almost sure convergence | Markov chains |
| [Brownian motion](brownian-motion.md) | The continuous scaling limit of random walks; Gaussian, Markov and a martingale | Markov chains, martingales |
| [Stochastic calculus](stochastic-calculus.md) | Integration against Brownian motion, Itô's formula, stochastic differential equations | Martingales, Brownian motion |

Read them in order. Markov chains come first because they need the least: a matrix and a starting distribution. Martingales add the betting point of view, and the two meet when a harmonic function h, with Ph = h, turns a chain X into a martingale h(Xₙ). Brownian motion arrives as the limit of random walks, and both earlier ideas apply to it at once. Stochastic calculus then makes the martingale transform continuous and turns Brownian motion into a tool for building new processes.

```
   Markov chains ──── simple random walk ──(Donsker scaling)──► Brownian motion
        │                                                          │
        │  Ph = h gives martingales h(Xₙ)                          │
        ▼                                                          ▼
   martingales ───── martingale transform ∑ Hₖ·ΔMₖ ──────► stochastic calculus
                                                   (Itô integral, Itô's formula, SDEs)
```

## Connections to sibling areas

- **[Measure-theoretic probability](../01-measure-theoretic-probability/README.md):** Kolmogorov's extension theorem builds processes as measures on path space, conditional expectation defines both the Markov and martingale properties, and filtrations model the flow of information.
- **[Limit theorems](../02-limit-theorems/README.md):** the ergodic theorem for chains and martingale convergence extend the law of large numbers to dependent sequences; Donsker's theorem extends the central limit theorem to whole paths; martingale differences give McDiarmid's concentration inequality.
- **[Statistical inference](../04-statistical-inference/README.md):** Markov chain Monte Carlo computes Bayesian posteriors, posterior means form a martingale, and likelihood ratios are martingales under the null hypothesis, the basis of sequential testing.

## Connections across layers

From below, the [Perron–Frobenius theorem](../../04-linear-algebra/02-determinants-and-eigenvalues/non-negative-matrices-and-perron-frobenius.md) of 04 gives stationary distributions, [graph connectivity](../../03-combinatorics-and-graph-theory/02-graph-theory/graphs-and-connectivity.md) in 03 gives irreducibility, [ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md) and the [heat equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md) of 10 are the deterministic counterparts of chains and diffusions, and the [Lᵖ spaces](../../09-advanced-analysis/01-measure-and-integration/lp-spaces.md) of 09 carry the Itô integral.

Upward, layer 14 uses all four children: [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md), [mathematical finance](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/mathematical-finance.md), [epidemic models](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md) and the numerical solution of stochastic differential equations. In the computer-science tree, [Markov chains](../../../cs-first-principles/01-mathematical-foundations/06-probability-and-statistics/markov-chains.md) model queues and algorithms, and [reinforcement learning](../../../cs-first-principles/13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md) is built on Markov decision processes.

## Cross-cutting threads

- [Local to global](../../CROSS-CUTTING.md#local-to-global): a one-step transition rule or an infinitesimal generator determines long-run behaviour through πP = π, Ph = h and the heat equation.
- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): ergodic averages along a single chain replace averages over independent samples.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): Wiener's measure and Lévy's midpoint construction build a random continuous function.
- [Duality](../../CROSS-CUTTING.md#duality): distributions evolve forward by πP and functions backward by Pf, the forward and backward Kolmogorov equations.
- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): random walks converge to Brownian motion and Euler schemes to diffusions.
- [Invariants](../../CROSS-CUTTING.md#invariants): a martingale's expectation is conserved, and the stationary distribution is the invariant of a chain.
