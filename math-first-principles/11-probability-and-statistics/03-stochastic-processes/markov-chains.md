# Markov Chains

> **Layer:** [11 Probability and Statistics](../README.md) › [Stochastic Processes](README.md)
> **Builds on:** [Non-Negative Matrices and Perron–Frobenius](../../04-linear-algebra/02-determinants-and-eigenvalues/non-negative-matrices-and-perron-frobenius.md), [Graphs and Connectivity](../../03-combinatorics-and-graph-theory/02-graph-theory/graphs-and-connectivity.md), [Conditional Expectation](../01-measure-theoretic-probability/conditional-expectation.md), [The Law of Large Numbers](../02-limit-theorems/the-law-of-large-numbers.md), [Ergodic Theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md)
> **Enables:** [Brownian Motion](brownian-motion.md), [Bayesian Inference](../04-statistical-inference/bayesian-inference.md), [Monte Carlo Methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md), [Mathematical Biology and Epidemics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md), [Markov Chains in computer science](../../../cs-first-principles/01-mathematical-foundations/06-probability-and-statistics/markov-chains.md)

## Essence

A Markov chain is a random process whose future depends on the past only through the present: the next state is drawn from a distribution that depends only on the current one. On a finite or countable state space S the whole chain is a stochastic matrix P, with P(x, y) the probability of moving from x to y, and the distribution after n steps is the starting distribution times Pⁿ. The central questions are whether there is an equilibrium, a distribution π with πP = π, whether the chain approaches it, and how fast. The answers combine linear algebra, graph theory and coupling, and underlie Markov chain Monte Carlo (MCMC), the main tool for sampling from complicated distributions.

## Core tenets

1. **The Markov property makes the transition matrix the whole story.** A sequence X₀, X₁, … is a Markov chain with transition matrix P when P(Xₙ₊₁ = y ∣ X₀, …, Xₙ) = P(Xₙ, y). Every row of P is a probability distribution, and the Chapman–Kolmogorov equations say that n-step transitions compose by matrix multiplication:

   ```
   P(Xₙ = y ∣ X₀ = x) = Pⁿ(x, y),        Pᵐ⁺ⁿ = Pᵐ·Pⁿ.
   ```

   Andrey Markov introduced such chains in 1906, partly to show that the law of large numbers holds without independence.

2. **A finite chain always has a stationary distribution; an infinite one need not.** A row vector π ≥ 0 with entries summing to 1 is stationary when πP = π, so that a chain started from π stays in π forever. For finite S, the constant column vector is a right eigenvector of P with eigenvalue 1, so a left one exists, and Perron–Frobenius makes it non-negative; alternatively, any limit point of the averages (1/n)·(μ + μP + … + μPⁿ⁻¹) is stationary. The simple random walk on ℤ has none: a stationary π would have to be constant, and no constant sums to 1.

3. **Irreducibility gives uniqueness, with a probabilistic formula.** A chain is irreducible when every state can reach every other, so that its transition graph is strongly connected. A finite irreducible chain has exactly one stationary distribution, and π(x) = 1/E_x[T_x], where T_x is the time of the first return to x when started at x: the long-run fraction of time spent at x is the reciprocal of the mean gap between visits.

4. **Aperiodicity gives convergence, and coupling proves it.** The period of x is the greatest common divisor (gcd) of the lengths of the cycles through x. The chain that flips between two states each step has stationary distribution (1/2, 1/2) but alternates forever, because its period is 2. For a finite irreducible aperiodic chain, Pⁿ(x, ·) → π for every x. Wolfgang Doeblin's coupling proof (1938) runs two copies, one from x and one from π, independently until they meet, and then together; the distance between their laws is at most the probability that they have not yet met, which tends to 0.

5. **The spectral gap and the mixing time measure the speed.** For a reversible chain on N states, the eigenvalues of P are real, 1 = λ₁ > λ₂ ≥ … ≥ λ_N ≥ −1, and the distance to π decays like λⁿ with λ = max(λ₂, ∣λ_N∣); 1 − λ is the spectral gap. The mixing time is the number of steps needed to bring the total variation distance to π below 1/4. Some chains show a cutoff, staying far from π and then dropping abruptly: Dave Bayer and Persi Diaconis (1992) showed that riffle-shuffling a 52-card deck mixes sharply at about seven shuffles.

6. **On infinite state spaces, recurrence divides the behaviour.** A state x is recurrent when the chain returns to it with probability 1, which happens if and only if ∑ₙ Pⁿ(x, x) = ∞. For the simple random walk on ℤᵈ, Pⁿ(0, 0) at even n is of order n^(−d/2), so the walk is recurrent in dimensions 1 and 2 and transient in 3 and above, as George Pólya proved in 1921. On ℤ the walk is null recurrent: it returns surely, but E[T₀] = ∞, which by tenet 3 is why no stationary distribution exists.

7. **Ergodic averages and detailed balance make chains computational tools.** For an irreducible chain with stationary π, (1/n)·∑ f(Xₖ) → ∑ f(x)·π(x) almost surely, a law of large numbers for dependent samples. To sample from a target π known only up to a constant, design a chain with π stationary. Detailed balance, π(x)·P(x, y) = π(y)·P(y, x), is sufficient, and the Metropolis rule (1953) achieves it: propose y from a symmetric proposal and accept with probability min(1, π(y)/π(x)). PageRank is the stationary distribution of a random surfer on the web.

## Key concepts

| Term | Meaning |
|---|---|
| Transition matrix P | P(x, y) = probability of moving from x to y in one step; rows sum to 1 |
| Stationary distribution π | A distribution with πP = π |
| Irreducible | Every state can reach every other |
| Period | The gcd of the lengths of the cycles through a state |
| Recurrent, transient | Returns with probability 1, or with probability less than 1 |
| Reversible | Satisfies detailed balance π(x)·P(x, y) = π(y)·P(y, x) |
| Total variation distance | max over events A of ∣μ(A) − ν(A)∣ |
| Mixing time | Steps needed to come within total variation 1/4 of π |

## How it fits

- **Below:** [Perron–Frobenius](../../04-linear-algebra/02-determinants-and-eigenvalues/non-negative-matrices-and-perron-frobenius.md) in 04 gives the eigenvector, [connectivity](../../03-combinatorics-and-graph-theory/02-graph-theory/graphs-and-connectivity.md) in 03 gives irreducibility, [conditional expectation](../01-measure-theoretic-probability/conditional-expectation.md) states the Markov property, and [ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md) in 10 is the general setting of tenet 7.
- **Above:** [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md) and [Bayesian inference](../04-statistical-inference/bayesian-inference.md) use MCMC; epidemic and population models in [mathematical biology](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md) are chains; queues in [networking](../../../cs-first-principles/08-networking/01-principles/latency-bandwidth-and-queueing.md) are continuous-time chains.
- **Siblings:** a function h with Ph = h makes h(Xₙ) a [martingale](martingales.md), and the scaled simple random walk converges to [Brownian motion](brownian-motion.md).

## Common misconceptions

- **"Every chain settles down to equilibrium"**: it needs irreducibility for uniqueness, aperiodicity for convergence, and, on infinite spaces, positive recurrence for a stationary distribution to exist at all.
- **"Markov chains cannot model memory"**: enlarge the state to include the last k states and any finite memory becomes Markov.
- **"A sampler has mixed when its output looks stable"**: a chain can stay in one mode of a distribution for longer than any feasible run. Diagnostics detect some failures to mix, never prove mixing.

## Go deeper

- J. R. Norris, *Markov Chains* (1997): a clear and rigorous first course, discrete and continuous time.
- David Levin and Yuval Peres, *Markov Chains and Mixing Times* (2nd edition, 2017): coupling, spectral methods and cutoff.
- Persi Diaconis, "The Markov chain Monte Carlo revolution" (2009): a survey of why sampling by chains changed science.
