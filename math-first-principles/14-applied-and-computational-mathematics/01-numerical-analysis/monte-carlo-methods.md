# Monte Carlo Methods

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Numerical Analysis](README.md)
> **Builds on:** [The Law of Large Numbers](../../11-probability-and-statistics/02-limit-theorems/the-law-of-large-numbers.md), [The Central Limit Theorem](../../11-probability-and-statistics/02-limit-theorems/the-central-limit-theorem.md), [Concentration Inequalities](../../11-probability-and-statistics/02-limit-theorems/concentration-inequalities.md), [Markov Chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md)
> **Enables:** [Gradient Methods](../02-optimisation/gradient-methods.md), [Mathematical Finance](../05-games-decisions-and-finance/mathematical-finance.md), [Statistical Learning Theory](../06-data-and-learning/statistical-learning-theory.md)

## Essence

Monte Carlo methods compute a number by writing it as an expectation and averaging random samples. The law of large numbers makes the average converge and the central limit theorem says how fast: the error falls like N^(−1/2) for N samples, whatever the dimension of the space sampled. That rate is slow, but grids need a number of points exponential in the dimension, so in high dimension randomness wins. When the distribution cannot be sampled directly, Markov chain Monte Carlo (MCMC) builds a random walk that has it as its long-run distribution.

## Core tenets

1. **The error is σ/√N in every dimension.** To estimate I = E[f(X)], average f(X₁), …, f(X_N) over independent samples. The estimate is unbiased with variance σ²/N, where σ² = Var f(X), so by the central limit theorem the error is approximately normal with standard deviation σ/√N, and the samples themselves estimate σ, giving a confidence interval for free. A tensor-product rule with n points per axis in d dimensions needs nᵈ points, so for an integral over [0, 1]¹⁰⁰ only sampling is feasible. The price is that each extra correct digit costs 100 times more samples, and if σ is infinite, as for x^(−0.7) on [0, 1], the rate fails.

2. **Variance reduction attacks σ, not N.** Importance sampling draws X from a density q and averages f(X)p(X)/q(X), which is unbiased for every q positive where fp is nonzero, and has small variance when q is nearly proportional to ∣f∣p. A rare event needs it: P(Z > 10) ≈ 7.6 × 10⁻²⁴ for a standard normal Z, so naive sampling would almost never see it, while samples from a normal centred at 10, reweighted, estimate it to a few per cent with thousands of draws. A control variate g with known mean, correlated with f with correlation ρ, cuts the variance by the factor 1 − ρ²; antithetic pairs and stratification work similarly.

3. **Quasi-random points beat N^(−1/2) for smooth integrands in moderate dimension.** Low-discrepancy sequences fill the cube more evenly than random points. The Koksma–Hlawka inequality bounds the error by the variation of f times the discrepancy of the points, which can be of order (log N)ᵈ/N. The dimension now appears, but many high-dimensional integrands in finance depend mainly on a few directions, where quasi-Monte Carlo works well.

4. **Markov chain Monte Carlo samples what cannot be sampled directly.** Often π is known only up to a constant, as in a Boltzmann distribution e^(−E(x)/T) or a Bayesian posterior. The Metropolis algorithm (Nicholas Metropolis, Arianna and Marshall Rosenbluth, Augusta and Edward Teller, 1953) proposes a symmetric random move from x to y and accepts it with probability min(1, π(y)/π(x)). Then π(x)P(x, y) = π(y)P(y, x), detailed balance, so π is stationary, and only ratios of π, in which the unknown constant cancels, are needed. If the chain is irreducible and aperiodic, the ergodic theorem for Markov chains makes time averages converge to expectations under π. W. Keith Hastings (1970) allowed asymmetric proposals; the Gibbs sampler updates one coordinate at a time from its conditional distribution.

5. **The cost of Markov chain Monte Carlo is the mixing time.** Successive states are correlated, so N steps are worth only an effective sample size N/τ, where τ is the integrated autocorrelation time, and the chain must first forget its start. A chain on a multimodal π can stay in one mode for longer than any run. Bounding mixing times rigorously, through the spectral gap, coupling or conductance, is hard and done only for special chains; in practice convergence is diagnosed, never proved. Hamiltonian Monte Carlo uses gradients of log π to make long, distant proposals that are still accepted often.

6. **Randomness can be provably more powerful than determinism.** Martin Dyer, Alan Frieze and Ravi Kannan (1991) estimated the volume of a convex body in ℝᵈ, given by a membership oracle, to any fixed relative accuracy in time polynomial in d, by random walks inside it. No deterministic polynomial-time algorithm can do this: Imre Bárány and Zoltán Füredi showed that any such algorithm can be wrong by a factor exponential in d.

## Key concepts

| Term | Meaning |
|---|---|
| Monte Carlo estimator | The average of f over N independent samples, an unbiased estimate of E[f] |
| Variance reduction | Changing the estimator so that σ shrinks while the mean stays the same |
| Importance sampling | Sampling from a different density and reweighting by the likelihood ratio |
| Detailed balance | π(x)P(x, y) = π(y)P(y, x), which makes π stationary for P |
| Mixing time | Steps needed for the chain's distribution to come close to π |
| Effective sample size | The number of independent samples worth as much as a correlated run |

## How it fits

- **Below:** the [law of large numbers](../../11-probability-and-statistics/02-limit-theorems/the-law-of-large-numbers.md) gives convergence, the [central limit theorem](../../11-probability-and-statistics/02-limit-theorems/the-central-limit-theorem.md) the rate and [concentration inequalities](../../11-probability-and-statistics/02-limit-theorems/concentration-inequalities.md) nonasymptotic error bounds; MCMC rests on the theory of [Markov chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md) and, for general state spaces, on [ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md).
- **Above:** stochastic gradient descent in [gradient methods](../02-optimisation/gradient-methods.md) is a Monte Carlo estimate of a gradient; option prices in [mathematical finance](../05-games-decisions-and-finance/mathematical-finance.md) are expectations computed by simulation; [Bayesian inference](../../11-probability-and-statistics/04-statistical-inference/bayesian-inference.md) relies on MCMC; [epidemic models](../04-mathematical-modelling/mathematical-biology-and-epidemics.md) are simulated stochastically; randomised algorithms in computer science use the same ideas ([CS](../../../cs-first-principles/05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md)).
- **Siblings:** Hamiltonian Monte Carlo integrates its trajectories with symplectic [time-stepping](numerical-methods-for-differential-equations.md); Monte Carlo replaces grid-based [quadrature](interpolation-and-approximation.md) in high dimension; its statistical error is far larger than the rounding error studied in [floating point](floating-point-conditioning-and-stability.md).

## Common misconceptions

- **"Monte Carlo beats the curse of dimensionality for free"**: the rate N^(−1/2) is dimension-free, but σ, and the mixing time of a sampler, can grow quickly with the dimension.
- **"A long run guarantees a converged chain"**: a chain trapped in one mode looks perfectly stable; diagnostics can show failure, never prove success.

## Go deeper

- Christian P. Robert and George Casella, *Monte Carlo Statistical Methods* (2nd edition, 2004): the statistical reference, including MCMC.
- Paul Glasserman, *Monte Carlo Methods in Financial Engineering* (2003): variance reduction and quasi-Monte Carlo in practice.
- David A. Levin, Yuval Peres and Elizabeth L. Wilmer, *Markov Chains and Mixing Times* (2009): the mathematics of mixing.
