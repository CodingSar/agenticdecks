# Markov Chains

> **Layer:** [01 Mathematical Foundations](../README.md) › [Probability and Statistics](README.md)
> **Builds on:** [Probability](probability.md), [Random Variables and Distributions](random-variables-and-distributions.md), [Linear Algebra](../04-algebra/linear-algebra.md), [Graph Theory](../03-discrete-mathematics/graph-theory.md)
> **Enables:** [Reinforcement Learning](../../13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md), [Latency, Bandwidth and Queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md), [Randomized Algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md), [Probabilistic Reasoning](../../13-artificial-intelligence/01-classical-ai/probabilistic-reasoning.md)

## Essence

A Markov chain is a random process whose next state depends only on its current state, not on how it got there. That one assumption, memorylessness, turns a process that could depend on its entire history into a matrix of transition probabilities, so questions about the future become questions of [linear algebra](../04-algebra/linear-algebra.md): repeated matrix multiplication, eigenvectors and linear equations. They model queues, web surfers, card shuffles, text and the random walks inside randomized algorithms. The central result: a well-behaved chain forgets its start and settles into a unique stationary distribution, which can be computed, sampled or deliberately designed.

## Core tenets

1. **The Markov property is a modelling choice about what counts as state.** P(X_(t+1) | X_t, X_(t−1), …) = P(X_(t+1) | X_t). Almost any process becomes Markov if the state holds enough history: a text model that predicts from the last two words is a chain on word pairs. The art is choosing a state small enough to compute with yet rich enough for the property to hold.

2. **A transition matrix moves distributions forward.** For finitely many states, P_ij is the probability of going from i to j, and each row sums to 1. If the row vector π_t is the distribution at time t, then π_(t+1) = π_t P and π_t = π_0 Pᵗ. Equivalently, the chain is a random walk on a weighted directed [graph](../03-discrete-mathematics/graph-theory.md).

3. **A stationary distribution is a left eigenvector with eigenvalue 1.** A distribution with πP = π is unchanged by a step. Every finite chain has one. If the chain is *irreducible* (every state reachable from every other), it is unique and gives every state positive probability. A shortcut for many chains is *detailed balance*: if π_i P_ij = π_j P_ji for all pairs, π is stationary.

4. **Ergodic chains forget where they started.** If a finite chain is irreducible and *aperiodic* (it does not cycle with a fixed period), then π_t converges to π from any start, and the fraction of time spent in each state converges to π too. So averages along one long simulated trajectory estimate averages under π.

5. **The spectral gap sets how fast mixing happens.** The distance to stationarity shrinks roughly like |λ₂|ᵗ, where λ₂ is the second-largest eigenvalue in magnitude, so the mixing time scales with 1/(1 − |λ₂|). Bottlenecks between well-connected regions shrink the gap. A classic result: about seven riffle shuffles mix a 52-card deck (Bayer and Diaconis, 1992). Walks on expander graphs mix in O(log n) steps, which [randomized algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md) exploit.

6. **Hitting times and absorption reduce to linear equations.** The expected time h_i to reach a target from state i satisfies h_i = 1 + Σ_j P_ij h_j, one equation per state. This analyses gambler's ruin, retry loops and randomized algorithms: a random walk on truth assignments solves 2-SAT (satisfiability with two literals per clause) in O(n²) expected steps, because the number of correctly set variables behaves like a walk on a line.

7. **PageRank is the stationary distribution of a random surfer.** Follow a random outgoing link with probability d (typically 0.85), otherwise jump to a random page. The jump makes the chain irreducible and aperiodic, so a unique stationary distribution exists, and power iteration (repeatedly computing πP) converges at a rate set by d. Rank is long-run time share (Brin and Page, 1998).

8. **Markov Chain Monte Carlo (MCMC) builds a chain to sample a distribution you cannot sample directly.** To draw from a distribution known only up to a normalising constant, such as a Bayesian posterior, design transitions whose stationary distribution is that target. The Metropolis–Hastings rule proposes a move and accepts it with a probability chosen to satisfy detailed balance; Gibbs sampling resamples one variable at a time. Samples are correlated and valid only after mixing, so diagnosing convergence is the practical difficulty.

9. **Continuous time gives queues; adding actions gives decision processes.** In continuous time each state is held for an exponentially distributed, memoryless time. A single-server queue with Poisson arrivals (rate λ) and exponential service (rate μ) is such a chain; balance equations give P(n jobs) = (1 − ρ)ρⁿ with ρ = λ/μ, and mean time in system 1/(μ − λ) ([queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md)). Letting an agent choose actions that change transitions and earn rewards gives a Markov Decision Process (MDP), the formal model of [reinforcement learning](../../13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md). Hiding the state behind noisy observations gives a Hidden Markov Model (HMM), used in speech recognition and [probabilistic reasoning](../../13-artificial-intelligence/01-classical-ai/probabilistic-reasoning.md).

## Key concepts

| Term | Meaning |
|---|---|
| Markov property | The future depends on the past only through the present state |
| Transition matrix | P_ij = probability of moving from state i to state j; rows sum to 1 |
| Stationary distribution | π with πP = π |
| Detailed balance | π_i P_ij = π_j P_ji; implies stationarity |
| Mixing time | Steps needed to get close to stationarity from any start |
| Spectral gap | 1 − \|λ₂\|; a larger gap means faster mixing |
| MCMC | Sampling by running a chain whose stationary distribution is the target |
| MDP / HMM | Chain plus actions and rewards / chain observed only through noisy outputs |

## How it fits

- **Below:** Events from [probability](probability.md), holding times from [distributions](random-variables-and-distributions.md), the matrix view from [linear algebra](../04-algebra/linear-algebra.md), reachability and periodicity from [graph theory](../03-discrete-mathematics/graph-theory.md).
- **Above:** [Queueing models](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) of networks and servers are continuous-time chains. [Reinforcement learning](../../13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md) is built on MDPs. [Probabilistic reasoning](../../13-artificial-intelligence/01-classical-ai/probabilistic-reasoning.md) uses HMMs and MCMC. [Randomized algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md) analyse random walks. Shannon modelled English as a Markov source, whose [entropy](../../02-theory-of-computation/01-information-theory/entropy-and-information.md) rate follows from its transition matrix.
- **Siblings:** [Probability](probability.md) and [random variables](random-variables-and-distributions.md) describe single experiments; this leaf strings them into processes. [Statistical inference](statistical-inference.md) uses MCMC to compute Bayesian posteriors.

## Common misconceptions

- **"Memoryless means the process has no memory of anything."** It remembers exactly its current state, and the state can be made to hold whatever history matters.
- **"Every chain converges to its stationary distribution."** A periodic chain (a walk that alternates between two sides of a bipartite graph) oscillates forever, and a reducible chain's limit depends on where it starts.
- **"Running MCMC for a while guarantees correct samples."** A chain with a small spectral gap can sit in one region for a very long time while looking converged.

## Go deeper

- David Levin, Yuval Peres and Elizabeth Wilmer, *Markov Chains and Mixing Times* (2nd ed., 2017): stationary distributions and mixing, free online.
- Sergey Brin and Lawrence Page, "The Anatomy of a Large-Scale Hypertextual Web Search Engine" (1998): PageRank as a random walk.
