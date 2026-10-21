# Probability and Statistics

> **Layer:** [01 Mathematical Foundations](../README.md) › Probability and Statistics
> **Children:** [Probability](probability.md) · [Random Variables and Distributions](random-variables-and-distributions.md) · [Statistical Inference](statistical-inference.md) · [Markov Chains](markov-chains.md)

## What this area is about

Probability and statistics are the mathematics of reasoning under uncertainty. Probability starts from a model of chance and predicts what data will look like; statistics starts from data and infers what the model must be. Computer science needs both directions. Systems must cope with uncertainty they cannot remove (when the next packet arrives, which disk fails, what the user types). Algorithms deliberately inject randomness to defeat worst-case inputs and to make large problems small by sampling. And learning systems exist precisely to infer models from data.

The unifying idea is that *uncertainty can be quantified and combined by fixed rules*. Once outcomes are described as sets with probabilities, conditioning, independence, expectation and Bayes' rule let you compute the chance of failure, the expected cost of an algorithm, the tail latency of a service, or the confidence in a measured improvement, instead of guessing.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Probability](probability.md) | Axioms, conditioning, independence, Bayes' rule, union bound; randomness as a tool | Sets, combinatorics |
| [Random Variables and Distributions](random-variables-and-distributions.md) | Numbers attached to outcomes; expectation, variance, tail bounds, standard and heavy-tailed distributions | Probability, calculus |
| [Statistical Inference](statistical-inference.md) | From data back to models: estimation, likelihood, confidence, testing, bias–variance | Both of the above, optimization |
| [Markov Chains](markov-chains.md) | Random processes that evolve step by step: transition matrices, stationary distributions, mixing, MCMC, queues | Probability, distributions, linear algebra |

Read the first three in order. Probability defines events and how their likelihoods combine. Random variables make outcomes numeric, so you can average, bound tails, and recognise the mechanisms (independent trials, memoryless waiting, sums of many effects, rich-get-richer growth) that produce standard distributions. Inference reverses the arrow. Markov chains can be read after random variables: they string single random experiments into a *process* in time, where the next state depends only on the current one. They supply the models behind queues and reinforcement learning, and, through Markov Chain Monte Carlo (MCMC), the sampling engine that makes Bayesian inference computable.

```
   model ──── probability, distributions ────► data
     ▲                                          │
     └────────── statistical inference ◄────────┘
          (estimate, quantify uncertainty, test)
```

Two results tie the area together. The law of large numbers and the Central Limit Theorem say that averages of many independent observations concentrate around the true mean, with spread shrinking like 1/√n; this is why sampling, measurement and learning from data work at all. Tail bounds (Markov, Chebyshev, Chernoff) turn that concentration into guarantees, the form algorithm designers and reliability engineers need.

## Connections to sibling areas

- **[Logic](../01-logic/README.md):** Events combine with AND, OR and NOT; probability generalises truth values to degrees of belief.
- **[Sets, Relations and Functions](../02-sets-relations-functions/README.md):** Events are subsets of a sample space and random variables are functions on it.
- **[Discrete Mathematics](../03-discrete-mathematics/README.md):** Finite probability is [counting](../03-discrete-mathematics/combinatorics.md); the birthday bound and union bound are shared tools. A Markov chain is a random walk on a [graph](../03-discrete-mathematics/graph-theory.md).
- **[Algebra](../04-algebra/README.md):** [Markov chains](markov-chains.md) are matrices whose dominant eigenvector is the long-run distribution, and their mixing speed is an eigenvalue gap; covariance matrices drive Principal Component Analysis (PCA).
- **[Continuous Mathematics](../05-continuous-mathematics/README.md):** Densities and expectations are integrals; maximum-likelihood estimation and model training are optimisation problems; the density of a sum of independent variables is a convolution, which [Fourier analysis](../05-continuous-mathematics/fourier-analysis.md) turns into a product.

## Connections across layers

The area underlies [information theory](../../02-theory-of-computation/01-information-theory/README.md) (entropy is an expected value), [randomized algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md) and [streaming sketches](../../05-algorithms-and-data-structures/07-advanced-topics/streaming-and-online-algorithms.md), [queueing and latency](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) (Markov models of queues), the definition of security in [modern cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md), [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md) and [observability](../../12-software-engineering/04-operations/observability.md), nearly all of [artificial intelligence](../../13-artificial-intelligence/README.md) (including the Markov decision processes of [reinforcement learning](../../13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md)), and the evaluation methods of [human-computer interaction](../../14-human-and-visual-computing/01-human-computer-interaction/README.md).

## Cross-cutting threads

- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): replication works only to the degree that failures are independent.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): sampling error shrinks only like 1/√n; no estimator escapes the bias–variance trade-off.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): randomized algorithms trade a tiny error probability for speed or simplicity.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): held-out data and controlled experiments are how claims about systems and models are checked.
- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): Bayesian updating revises beliefs as evidence arrives.
