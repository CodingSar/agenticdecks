# Brownian Motion

> **Layer:** [11 Probability and Statistics](../README.md) › [Stochastic Processes](README.md)
> **Builds on:** [The Central Limit Theorem](../02-limit-theorems/the-central-limit-theorem.md), [Martingales](martingales.md), [Markov Chains](markov-chains.md), [The Heat Equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md), [Independence and Zero–One Laws](../01-measure-theoretic-probability/independence-and-zero-one-laws.md)
> **Enables:** [Stochastic Calculus](stochastic-calculus.md), [Mathematical Finance](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/mathematical-finance.md), [The Mathematics of Quantum Mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md)

## Essence

Brownian motion is the random continuous path that a random walk becomes when its steps are made small and fast in the right proportion. Robert Brown observed the jittering of pollen particles in water in 1827; Louis Bachelier used it to model stock prices in 1900; Albert Einstein explained it in 1905 as the effect of molecular collisions and linked it to diffusion; Norbert Wiener constructed it rigorously in 1923 as a probability measure on the space of continuous functions. It sits at a crossroads: it is a Gaussian process, a martingale, a Markov process and the probabilistic solution of the heat equation, and its paths are continuous everywhere yet differentiable nowhere.

## Core tenets

1. **The definition is forced by the central limit theorem.** A standard Brownian motion is a process (Bₜ) for t ≥ 0 with B₀ = 0, independent increments, Bₜ − Bₛ normal with mean 0 and variance t − s for s < t, and continuous paths. Any limit of rescaled random walks must have independent stationary increments, and the central limit theorem makes them normal. Monroe Donsker's invariance principle (1951) makes this a theorem: for a walk with mean-zero steps of variance 1, the path t ↦ S_⌊nt⌋/√n converges in distribution to B.

2. **It exists: Lévy's midpoint construction.** Define B at time 1 as a standard normal. Given B at the dyadic points k/2ⁿ, set each new midpoint to the average of its neighbours plus an independent normal correction of variance 2^(−n−2). The corrections at level n have maximum of order √(n·2⁻ⁿ), which is summable, so by the first Borel–Cantelli lemma the piecewise linear interpolations converge uniformly almost surely, and a uniform limit of continuous functions is continuous.

3. **It is self-similar.** For every c > 0, the process (c^(−1/2)·B_(ct)) is again a standard Brownian motion: zooming in by c in time and √c in space shows the same picture at every scale. Time inversion, t·B_(1/t), is also a Brownian motion. The graph {(t, Bₜ)} of a path has Hausdorff dimension 3/2 almost surely, a natural random fractal ([Hausdorff dimension](../../09-advanced-analysis/01-measure-and-integration/hausdorff-dimension-and-fractals.md)).

4. **Its paths are continuous but nowhere differentiable.** Raymond Paley, Norbert Wiener and Antoni Zygmund proved in 1933 that, almost surely, the path has a derivative at no point. Scaling explains it: over a time step h the path moves about √h, so the difference quotient has size h^(−1/2) → ∞. The paths are Hölder continuous of every order below 1/2 and of no order 1/2 or above. Their quadratic variation over [0, t] is exactly t:

   ```
   ∑ₖ (B_(tₖ₊₁) − B_(tₖ))²  →  t   in L², as the mesh of the partition 0 = t₀ < … < tₘ = t tends to 0.
   ```

   This is a law of large numbers for the squared increments, and it is the source of the rule (dB)² = dt of stochastic calculus.

5. **It is a martingale and a strong Markov process.** Bₜ, Bₜ² − t and exp(θBₜ − θ²t/2) are martingales. Brownian motion restarts afresh at stopping times, and combined with symmetry this gives the reflection principle: P(max over s ≤ t of Bₛ ≥ a) = 2·P(Bₜ ≥ a) for a > 0. Paul Lévy's characterisation turns this around: a continuous martingale M with M₀ = 0 and Mₜ² − t a martingale is a Brownian motion.

6. **It solves the heat equation.** The density of x + Bₜ is the heat kernel p(t, x, y) = (2πt)^(−1/2)·e^(−(y − x)²/(2t)), and for bounded continuous f the function u(t, x) = E[f(x + Bₜ)] solves ∂u/∂t = ½·∂²u/∂x² with u(0, x) = f(x). Einstein's relation between diffusion and molecular motion allowed Jean Perrin to estimate Avogadro's number from observed particles, evidence that persuaded sceptics that atoms exist. In higher dimensions, Shizuo Kakutani showed in 1944 that the solution of the Dirichlet problem for Laplace's equation at x is E[f(B at its exit point)], for Brownian motion started at x ([harmonic functions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md)).

7. **Dimension decides recurrence, as for random walks.** Brownian motion in the plane comes arbitrarily close to every point infinitely often but hits a given point with probability 0; in three or more dimensions it escapes to infinity. This mirrors Pólya's theorem for the random walk on ℤᵈ in [Markov chains](markov-chains.md).

## Key concepts

| Term | Meaning |
|---|---|
| Standard Brownian motion | Continuous paths, B₀ = 0, independent increments Bₜ − Bₛ normal with variance t − s |
| Wiener measure | The law of Brownian motion on the space of continuous functions |
| Donsker's invariance principle | Rescaled random walks converge in distribution to Brownian motion |
| Brownian scaling | c^(−1/2)·B_(ct) is again a Brownian motion |
| Quadratic variation | The limit of sums of squared increments; equal to t for Brownian motion |
| Reflection principle | P(max over s ≤ t of Bₛ ≥ a) = 2·P(Bₜ ≥ a) |
| Heat kernel | The normal density p(t, x, y) of x + Bₜ, the fundamental solution of the heat equation |

## How it fits

- **Below:** the [central limit theorem](../02-limit-theorems/the-central-limit-theorem.md) fixes the normal increments; the [heat equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md) in 10 is its analytic shadow; [martingales](martingales.md) and [Markov chains](markov-chains.md) supply the discrete versions of its two key properties.
- **Above:** geometric Brownian motion is the Black–Scholes model of [mathematical finance](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/mathematical-finance.md); the Feynman–Kac formula connects it to the Schrödinger equation of [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) in imaginary time.
- **Siblings:** [stochastic calculus](stochastic-calculus.md) integrates against Brownian paths, which ordinary calculus cannot do because they have infinite length on every interval.

## Common misconceptions

- **"A Brownian path is a wiggly smooth curve"**: it has no tangent anywhere and infinite length on every interval; no amount of zooming reveals a straight piece.
- **"Brownian motion drifts away like t"**: its typical size at time t is √t, and by the law of the iterated logarithm, lim sup Bₜ/√(2t log log t) = 1 almost surely.
- **"It is an exact physical model"**: a real particle has inertia and a velocity. The Ornstein–Uhlenbeck model of velocity is more realistic at short times, and Brownian motion is its idealisation at long times.

## Go deeper

- Peter Mörters and Yuval Peres, *Brownian Motion* (2010): the path properties in depth, including dimension and recurrence.
- Jean-François Le Gall, *Brownian Motion, Martingales, and Stochastic Calculus* (2016): a concise rigorous route to stochastic calculus.
- Albert Einstein, *Investigations on the Theory of the Brownian Movement* (English edition, 1926): the 1905 papers that tied the motion to molecules.
