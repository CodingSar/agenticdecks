# Probabilistic Reasoning

> **Layer:** [13 Artificial Intelligence](../README.md) › [Classical AI](README.md)
> **Builds on:** [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Random variables and distributions](../../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md), [Graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md), [Dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md)
> **Enables:** [Unsupervised learning](../02-machine-learning-foundations/unsupervised-learning.md), [Generative models](../04-advanced-paradigms/generative-models.md), [Reinforcement learning](../04-advanced-paradigms/reinforcement-learning.md)

## Essence

Real agents never know the world exactly: sensors are noisy, rules have exceptions, and the future is uncertain. Probabilistic reasoning represents belief as a probability distribution and updates it with Bayes' rule as evidence arrives. The obstacle is size: a joint distribution over n binary variables needs 2^n − 1 numbers. The key idea is **conditional independence**: most variables directly influence only a few others, so the joint distribution factors into small local pieces. Graphical models (Bayesian networks and Markov networks) make that factorisation explicit as a graph, which both reduces storage and lets inference algorithms exploit the structure.

## Core tenets

1. **Bayes' rule turns causal knowledge into diagnostic inference.** P(cause | effect) = P(effect | cause) · P(cause) / P(effect). We usually know how causes produce effects (a disease produces a symptom with some probability) and need the reverse. The prior P(cause) matters: a 99%-accurate test for a 1-in-10,000 disease still yields mostly false positives.

2. **Conditional independence is what makes probability tractable.** If X is independent of Y given Z, then P(X | Y, Z) = P(X | Z), and the term for X does not need a row for every value of Y. Without such assumptions, nothing beyond toy problems could be stored or learned.

3. **A Bayesian network is a factorisation drawn as a Directed Acyclic Graph (DAG).** Each node stores P(X_i | Parents(X_i)), and the joint is the product:

   P(X_1, ..., X_n) = ∏_i P(X_i | Parents(X_i))

   With at most k parents per binary node, storage is O(n · 2^k) instead of O(2^n). The graph also encodes which independences hold, readable by the d-separation criterion.

4. **Exact inference is NP-hard in general but cheap on sparse structure.** Variable elimination sums out variables one at a time, caching intermediate factors, which is dynamic programming over the graph. On trees and polytrees it is linear (belief propagation); in general it is exponential in the treewidth. This is the same structural boundary as in [constraint satisfaction](constraint-satisfaction.md).

5. **Approximate inference trades exactness for scale.** Monte Carlo methods estimate probabilities by sampling: Markov Chain Monte Carlo (MCMC), such as Gibbs sampling, builds a random walk whose long-run (stationary) distribution is the posterior; see [Markov chains](../../01-mathematical-foundations/06-probability-and-statistics/markov-chains.md). Variational inference instead picks the closest member of a simple family of distributions by optimisation. Variational methods reappear inside modern deep generative models.

6. **Time is handled by repeating a structure.** Hidden Markov Models (HMMs) and Kalman filters assume the hidden state at time t depends only on t−1 (the Markov assumption) and each observation only on the current state. Filtering then updates belief in constant time per step, regardless of history length. This powered speech recognition for decades and still powers robot localisation and Global Positioning System (GPS) tracking; learned [recurrent networks and state-space models](../03-deep-learning/recurrent-networks-and-sequence-models.md) keep the same state-update shape with learned transitions.

7. **Decisions combine beliefs with utilities.** A rational agent chooses the action maximising expected utility, Σ P(outcome | action) · U(outcome). Sequential decisions under uncertainty become Markov Decision Processes, the formal basis of [reinforcement learning](../04-advanced-paradigms/reinforcement-learning.md).

## Key concepts

| Term | Meaning |
|---|---|
| Prior / posterior | Belief before / after conditioning on evidence |
| Likelihood | P(evidence given hypothesis), viewed as a function of the hypothesis |
| Conditional independence | Knowing Z makes Y irrelevant to X |
| Bayesian network | DAG whose nodes store conditional distributions given their parents |
| Markov network | Undirected graph whose joint is a normalised product of clique potentials |
| Variable elimination | Exact inference by summing out variables in an order, caching factors |
| MCMC | Sampling from a distribution via a Markov chain that converges to it |
| HMM | Hidden discrete state chain with noisy observations at each step |
| Expected utility | Probability-weighted average of outcome values; the criterion for rational choice |

## How it fits

- **Below:** All of it rests on [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) and [distributions](../../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md); inference algorithms are [dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md) on [graphs](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md); learning parameters is [statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md).
- **Above:** Mixture models and latent-variable models in [unsupervised learning](../02-machine-learning-foundations/unsupervised-learning.md), the likelihood-based view of [generative models](../04-advanced-paradigms/generative-models.md), and the Markov Decision Process in [reinforcement learning](../04-advanced-paradigms/reinforcement-learning.md) all come from here. Every probabilistic classifier, including a language model's next-token softmax, is a conditional distribution in this sense.
- **Siblings:** It is the uncertain counterpart of [logical reasoning](knowledge-representation-and-reasoning.md): logic asks "is it true in every model?", probability asks "in what fraction of weighted models?". Counting solutions in [constraint satisfaction](constraint-satisfaction.md) is a close cousin of computing probabilities.

## Common misconceptions

- **"The arrows in a Bayesian network must be causal."** They only encode a factorisation. Causal readings need extra assumptions, studied in causal inference.
- **"Independence and conditional independence are the same."** Two independent causes become dependent once you observe their common effect ("explaining away"), and dependent variables can become independent given a common cause.
- **"Deep learning replaced probabilistic reasoning."** Deep networks are usually trained as probabilistic models (maximising likelihood) and diffusion and variational models are graphical models with neural components.

## Go deeper

- Judea Pearl, *Probabilistic Reasoning in Intelligent Systems* (1988): the founding text of Bayesian networks and belief propagation.
- Daphne Koller and Nir Friedman, *Probabilistic Graphical Models: Principles and Techniques* (2009): the comprehensive reference on representation, inference and learning.
- Sebastian Thrun, Wolfram Burgard and Dieter Fox, *Probabilistic Robotics* (2005): filtering and decision making applied to real machines.
