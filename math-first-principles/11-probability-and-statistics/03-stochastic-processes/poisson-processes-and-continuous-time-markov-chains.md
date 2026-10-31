# Poisson Processes and Continuous-Time Markov Chains

> **Layer:** [11 Probability and Statistics](../README.md) › [Stochastic Processes](README.md)
> **Builds on:** [Markov Chains](markov-chains.md), [Independence and Zero–One Laws](../01-measure-theoretic-probability/independence-and-zero-one-laws.md), [Random Variables and Distributions](../01-measure-theoretic-probability/random-variables-and-distributions.md), [The Law of Large Numbers](../02-limit-theorems/the-law-of-large-numbers.md), [Linear Systems and the Matrix Exponential](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/linear-systems-and-the-matrix-exponential.md)
> **Enables:** [Mathematical Biology and Epidemics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md), [Monte Carlo Methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md), [Latency, Bandwidth and Queueing (CS)](../../../cs-first-principles/08-networking/01-principles/latency-bandwidth-and-queueing.md)

## Essence

Many random systems change at random instants rather than on the ticks of a clock: calls reach an exchange, atoms decay, customers join a queue, molecules react. The Poisson process is the model of events that occur "completely at random" in time, and it is pinned down by one property, that the waiting time to the next event has no memory. Letting the rate of jumping depend on the current state gives a continuous-time Markov chain (CTMC). Its law is governed by a single matrix of rates, the generator Q, and its transition probabilities are the matrix exponential e^(tQ), so the theory of discrete chains carries over with a linear differential equation in place of matrix powers.

## Core tenets

1. **The Poisson process has three equivalent definitions.** A counting process N(t) with rate λ is Poisson if (a) its increments over disjoint intervals are independent and N(t + s) − N(s) has the Poisson distribution with mean λt; or (b) the gaps between events are independent and identically distributed (i.i.d.) exponential with mean 1/λ; or (c) in a short interval of length h there is one event with probability λh + o(h) and more than one with probability o(h), independently of the past. Each implies the others: (c) gives a differential equation for P(N(t) = k) whose solution is e^(−λt)(λt)ᵏ/k!, and P(first gap > t) = P(N(t) = 0) = e^(−λt) gives (b).

2. **The exponential law is the only memoryless one.** If T is exponential, P(T > s + t ∣ T > s) = P(T > t): a component that has survived is as good as new. Conversely, if G(t) = P(T > t) satisfies G(s + t) = G(s)G(t) and is monotone, then G(t) = e^(−λt), since log G is additive and monotone, hence linear. Memorylessness is exactly the Markov property in continuous time, which is why exponential holding times appear in every CTMC.

3. **Poisson counts are the law of rare events.** If n independent trials each succeed with probability λ/n, the number of successes converges in distribution to Poisson(λ) as n → ∞, because (n choose k)(λ/n)ᵏ(1 − λ/n)^(n−k) → e^(−λ)λᵏ/k!. Many small independent chances of an event give a Poisson count, whatever their source; Bortkiewicz's 1898 data on deaths from horse kicks in Prussian army corps are the classic fit.

4. **Poisson processes split and merge cleanly.** The sum of independent Poisson processes with rates λ and μ is Poisson with rate λ + μ, and the first event comes from the first process with probability λ/(λ + μ). Keeping each event independently with probability p (thinning) gives a Poisson process of rate pλ, independent of the discarded one. Given N(t) = n, the n event times are distributed as n independent uniform points on [0, t], sorted, which is the precise sense of "completely at random".

5. **A continuous-time chain is a jump chain with exponential clocks.** On a countable state space, the generator Q has off-diagonal entries q_ij ≥ 0, the rates of jumping from i to j, and diagonal entries chosen so every row sums to 0, so q_i = −q_ii is the total rate of leaving i. The chain waits in i for an exponential time with mean 1/q_i, then jumps to j with probability q_ij/q_i, independently of everything before. The sequence of states visited is an ordinary [discrete-time Markov chain](markov-chains.md), the jump chain.

6. **Transition probabilities are a matrix exponential.** Write P(t) for the matrix of P(X_t = j ∣ X₀ = i). The Markov property gives P(s + t) = P(s)P(t), and differentiating at 0 gives Kolmogorov's backward and forward equations (1931), P′(t) = QP(t) and P′(t) = P(t)Q. On a finite space the unique solution with P(0) = I is P(t) = e^(tQ), a [matrix exponential](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/linear-systems-and-the-matrix-exponential.md). For two states with rates a from 0 to 1 and b back, P₀₀(t) = b/(a + b) + (a/(a + b))·e^(−(a+b)t): the chain forgets its start at the rate a + b.

7. **Equilibrium solves πQ = 0, and periodicity disappears.** A distribution π is stationary when πQ = 0, which says that the probability flow into each state balances the flow out. An irreducible chain on a finite space has P(t) with all entries positive for every t > 0, so there is no periodicity, and P(t) converges to the unique π from any start. Time averages converge to π-averages, as the [law of large numbers](../02-limit-theorems/the-law-of-large-numbers.md) for regenerative cycles shows.

8. **Queues are birth–death chains.** In the M/M/1 queue, Kendall's notation for Markovian (Poisson) arrivals at rate λ, Markovian (exponential) service at rate μ and one server, the queue length is a CTMC that rises at rate λ and falls at rate μ. Balancing flow across each cut, λπₙ = μπₙ₊₁, gives πₙ = (1 − ρ)ρⁿ with ρ = λ/μ, provided ρ < 1. The mean number in the system is ρ/(1 − ρ), and by Little's law, mean number = λ × mean time, the mean time in the system is 1/(μ − λ). At 90% utilisation, ρ = 0.9, nine customers are present on average, which is why [network queues](../../../cs-first-principles/08-networking/01-principles/latency-bandwidth-and-queueing.md) blow up near capacity.

9. **Infinite chains can explode, and simulation is exact.** A pure birth chain with rates qₙ = n² makes infinitely many jumps in finite time, since the expected total holding time ∑ 1/n² is finite. A chain is non-explosive if, for example, its rates are bounded. Because the description in tenet 5 is constructive, a CTMC can be simulated exactly by drawing exponential holding times and jumps; in chemistry this is Gillespie's stochastic simulation algorithm, and stochastic epidemic models such as the susceptible–infected–recovered (SIR) model are run this way.

## Key concepts

| Term | Meaning |
|---|---|
| Poisson process | Counting process with independent increments and Poisson(λt) counts |
| Exponential distribution | P(T > t) = e^(−λt); the memoryless waiting time |
| Thinning and superposition | Splitting or merging Poisson processes gives Poisson processes |
| Generator Q | Matrix of jump rates; off-diagonal entries ≥ 0, rows sum to 0 |
| Jump chain | The discrete chain of states visited, with probabilities q_ij/q_i |
| Kolmogorov equations | P′ = QP (backward) and P′ = PQ (forward) |
| Stationary distribution | π with πQ = 0 |
| Explosion | Infinitely many jumps in finite time |
| Little's law | Mean number in system = arrival rate × mean time in system |

## How it fits

- **Below:** [Markov chains](markov-chains.md) supply the jump chain and the ergodic theory; [independence](../01-measure-theoretic-probability/independence-and-zero-one-laws.md) underlies independent increments; [the matrix exponential](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/linear-systems-and-the-matrix-exponential.md) in 10 solves the Kolmogorov equations.
- **Above:** stochastic epidemic and population models in [mathematical biology](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md) are CTMCs, and as the population grows they converge to the deterministic differential equations; exact event-driven simulation is a [Monte Carlo method](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md); queueing in [computer networks](../../../cs-first-principles/08-networking/01-principles/latency-bandwidth-and-queueing.md) starts from M/M/1.
- **Siblings:** the compensated process N(t) − λt is a [martingale](martingales.md), the jump counterpart of [Brownian motion](brownian-motion.md); a diffusion's generator in [stochastic calculus](stochastic-calculus.md) plays the role of Q.

## Common misconceptions

- **"Random arrivals should be evenly spaced"**: Poisson arrivals cluster; with rate 1 per minute, a gap under 15 seconds has probability 1 − e^(−1/4) ≈ 22%.
- **"The interval you land in has the average length"**: a fixed time falls in a gap of mean length about 2/λ, twice the average, because long gaps are more likely to be hit (the inspection paradox).
- **"A continuous-time chain is just a discrete chain sampled at times 1, 2, 3, …"**: sampling gives the chain with matrix e^Q, but most stochastic matrices are not of that form, and holding times carry information the jump chain loses.

## Go deeper

- J. R. Norris, *Markov Chains* (1997): chapters 2 and 3 build Poisson processes and continuous-time chains rigorously.
- J. F. C. Kingman, *Poisson Processes* (1993): the Poisson process on general spaces, short and elegant.
- Geoffrey Grimmett and David Stirzaker, *Probability and Random Processes* (3rd edition, 2001): queues, birth–death chains and many worked examples.
