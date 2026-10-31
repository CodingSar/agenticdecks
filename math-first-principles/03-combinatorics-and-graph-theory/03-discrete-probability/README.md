# Discrete Probability

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › Discrete Probability
> **Children:** [Finite probability spaces](finite-probability-spaces.md) · [Expectation and variance](expectation-and-variance.md) · [The probabilistic method](the-probabilistic-method.md) · [Random graphs](random-graphs.md)

## What this area is about
Probability on a finite or countable set is weighted counting. Every outcome gets a non-negative weight, the weights add up to 1, and the probability of an event is the total weight of its outcomes. That one definition already supports conditioning, independence, Bayes' rule, random variables, expectation, variance and the first inequalities that link averages to certainty. Every statement reduces to a sum, so no limits, integrals or measure theory are needed. This area has two jobs. It is the honest first course in probability: everything in it survives unchanged when [measure-theoretic probability](../../11-probability-and-statistics/README.md) takes over. It is also a proof technique for combinatorics: to show that an object with some property exists, choose an object at random and show that it has the property with positive probability. Erdős turned that idea into a method that still gives the best known bounds for many extremal problems.

## How the children fit together
| Child | Its role in the whole | Depends on |
|---|---|---|
| [Finite probability spaces](finite-probability-spaces.md) | Sample spaces, events, conditioning, independence, Bayes' rule, the union bound | Enumeration, sets, countable sets |
| [Expectation and variance](expectation-and-variance.md) | Random variables, linearity of expectation, indicators, variance, Markov and Chebyshev | Finite probability spaces |
| [The probabilistic method](the-probabilistic-method.md) | Existence proofs by random choice: union bound, averaging, alteration, second moments, the Local Lemma | Both of the above, graphs |
| [Random graphs](random-graphs.md) | G(n, p), thresholds, the giant component, connectivity, cliques and colourings of typical graphs | The probabilistic method, expectation and variance, graphs |

```
finite probability spaces  ──>  expectation and variance
           \                          /
            ──>  the probabilistic method  <──  graph theory
                          |
                    random graphs
```

The first leaf turns counting into probability and adds the one new idea, conditioning. The second adds numbers to outcomes. Its key fact is that expectation is linear whether or not the parts are independent, so expected counts become sums of probabilities. The third leaf uses both as tools for existence proofs. The union bound shows that bad events cannot cover the whole space. The averaging principle shows that some outcome is at least the mean. Chebyshev's inequality, used as the second moment method, shows that a count is positive with high probability. Each step adds one tool, and the probabilistic method uses all of them. The fourth leaf turns the method from existence to description: instead of asking whether some graph has a property, it asks what a typical random graph looks like, and finds sudden thresholds at which triangles, a giant component and connectivity appear.

## Connections to sibling areas
- [Enumeration](../01-enumeration/README.md): uniform probability is counting divided by counting, the union bound is truncated inclusion–exclusion, and probability generating functions are ordinary generating functions of distributions.
- [Graph theory](../02-graph-theory/README.md): [random graphs](random-graphs.md) G(n, p) are the main objects of the probabilistic method, random regular graphs are [expanders](../02-graph-theory/spectral-graph-theory-and-expanders.md), and random walks on graphs are the simplest Markov chains.
- [Extremal combinatorics](../04-extremal-combinatorics/README.md): random constructions give the lower bounds in Ramsey theory and the matching constructions in extremal graph theory.

## Connections across layers
- Below: events are [sets](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md), and countable spaces rest on [countable sets](../../01-sets-and-foundations/02-infinity-and-cardinality/countable-sets.md).
- Above: uncountable spaces need [measure and σ-algebras](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md) and [Kolmogorov's axioms](../../11-probability-and-statistics/01-measure-theoretic-probability/probability-spaces-and-kolmogorovs-axioms.md); averages of many trials lead to the [law of large numbers](../../11-probability-and-statistics/02-limit-theorems/the-law-of-large-numbers.md) and [concentration inequalities](../../11-probability-and-statistics/02-limit-theorems/concentration-inequalities.md); random sampling is the basis of [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md) and random codes of [information theory](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/information-theory.md).
- In other fields: the same material appears as [probability and statistics for computing](../../../cs-first-principles/01-mathematical-foundations/06-probability-and-statistics/README.md) and as [probability and measurement in medicine](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/01-probability-and-measurement/README.md).

## Cross-cutting threads
- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): linearity of expectation and the averaging principle.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): random objects prove existence without constructing anything, and derandomisation turns some of these proofs into algorithms.
- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): thresholds in random graphs and the weak law of large numbers.
- [Infinity and size](../../CROSS-CUTTING.md#infinity-and-size): there is no uniform distribution on a countably infinite set.
