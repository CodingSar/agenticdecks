# Random Graphs

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Discrete Probability](README.md)
> **Builds on:** [The probabilistic method](the-probabilistic-method.md), [Expectation and variance](expectation-and-variance.md), [Graphs and connectivity](../02-graph-theory/graphs-and-connectivity.md)
> **Enables:** [Concentration inequalities](../../11-probability-and-statistics/02-limit-theorems/concentration-inequalities.md), [Martingales](../../11-probability-and-statistics/03-stochastic-processes/martingales.md), [Independence and zero–one laws](../../11-probability-and-statistics/01-measure-theoretic-probability/independence-and-zero-one-laws.md), [Mathematical biology and epidemics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md), [Ramsey theory](../04-extremal-combinatorics/ramsey-theory.md)

## Essence
A random graph is built by deciding each possible edge by a coin toss. The theory asks what a typical such graph looks like when the number of vertices n is large, and its central discovery is the phase transition: as the edge probability p increases, properties such as containing a triangle, being connected or having a giant component appear suddenly, within a narrow window of p. Paul Erdős and Alfréd Rényi founded the subject around 1960, and it became the main laboratory of the probabilistic method. Its tools, first and second moments, branching processes and concentration, are the standard way to analyse large random structures, from networks to the spread of disease.

## Core tenets
1. **There are two standard models, and statements are asymptotic.** In G(n, p), introduced by Edgar Gilbert in 1959, each of the C(n, 2) possible edges is present independently with probability p. In G(n, m), studied by Erdős and Rényi from 1959, a graph with exactly m edges is chosen uniformly. With m close to p · C(n, 2) the two behave alike. An event holds with high probability when its probability tends to 1 as n → ∞, and p is usually a function of n.

2. **First and second moments locate thresholds.** The expected number of triangles in G(n, p) is C(n, 3)p³, about (np)³/6. If np → 0, Markov's inequality shows that there is no triangle with high probability; if np → ∞, the second moment method shows that there is one. So 1/n is the threshold. At p = c/n the triangle count is approximately Poisson with mean c³/6. In general a fixed graph H appears at about n^(−1/m), where m is the largest ratio of edges to vertices among subgraphs of H: the densest part of H is the bottleneck.

3. **Every monotone property has a threshold.** A property is monotone if adding edges preserves it, like connectivity or containing a triangle. Béla Bollobás and Andrew Thomason (1987) proved that every such property has a threshold function p*(n): it holds with probability tending to 0 when p is much smaller than p* and tending to 1 when p is much larger. Some thresholds are coarse, such as the triangle's, where the probability varies smoothly with c at p = c/n; others are sharp, such as connectivity.

4. **Connectivity arrives when the last isolated vertex disappears.** At p = (ln n + c)/n the expected number of isolated vertices is about n · e^(−np) = e^(−c), and their number is approximately Poisson. Erdős and Rényi showed that the probability of being connected tends to e^(−e^(−c)). Isolated vertices are the last obstacle: with high probability the graph becomes connected at the moment its last isolated vertex acquires an edge.

5. **The giant component appears at average degree 1.** Take p = c/n, so that the average degree is about c. If c < 1, every component has O(log n) vertices. If c > 1, there is a unique giant component with about βn vertices, where β solves β = 1 − e^(−cβ), and every other component has O(log n) vertices; for c = 2, β ≈ 0.80. At c = 1 the largest component has order n^(2/3). The proof explores a component vertex by vertex: each vertex reveals about c new neighbours on average, approximately a branching process with Poisson offspring, which dies out for sure when c ≤ 1 and survives with probability β when c > 1.

6. **Cliques and colourings of G(n, 1/2) are known to leading order.** The largest clique and the largest independent set have about 2 log₂ n vertices, concentrated on two consecutive values. This is Erdős's 1947 Ramsey lower bound seen from the other side ([Ramsey theory](../04-extremal-combinatorics/ramsey-theory.md)). Bollobás (1988) showed that the chromatic number is about n/(2 log₂ n), using concentration of a martingale. Greedy search finds a clique of about log₂ n vertices, and whether an efficient algorithm can find one of size (1 + ε) log₂ n, a question raised by Richard Karp in 1976, is open as of 2026.

7. **Thresholds are close to the obvious counting bound.** The expectation threshold is the smallest p at which no simple first-moment count rules a property out. Jeff Kahn and Gil Kalai conjectured in 2006 that the true threshold exceeds it by at most a factor of order log n. Jinyoung Park and Huy Tuan Pham proved this in 2022, recovering at once the thresholds for perfect matchings, Hamiltonian cycles and spanning trees of bounded degree up to constant factors. Random regular graphs, a related model, are the standard source of [expanders](../02-graph-theory/spectral-graph-theory-and-expanders.md).

## Key concepts
| Term | Meaning |
|---|---|
| G(n, p) | n vertices, each edge present independently with probability p |
| G(n, m) | Uniformly random graph with n vertices and m edges |
| With high probability | With probability tending to 1 as n → ∞ |
| Monotone property | A property preserved by adding edges |
| Threshold function | p* such that the property is unlikely for p ≪ p* and likely for p ≫ p* |
| Giant component | A component containing a constant fraction of the vertices |
| Branching process | Each individual has a random number of children, independently |
| Expectation threshold | Smallest p at which first-moment counts no longer exclude a property |

## How it fits
- **Below:** [the probabilistic method](the-probabilistic-method.md) supplies the first and second moment methods; [expectation and variance](expectation-and-variance.md) supply indicators and Chebyshev's inequality; [graphs and connectivity](../02-graph-theory/graphs-and-connectivity.md) supply components.
- **Above:** [concentration inequalities](../../11-probability-and-statistics/02-limit-theorems/concentration-inequalities.md) and [martingales](../../11-probability-and-statistics/03-stochastic-processes/martingales.md) sharpen the estimates; for constant p every first-order property has probability tending to 0 or 1, a [zero–one law](../../11-probability-and-statistics/01-measure-theoretic-probability/independence-and-zero-one-laws.md); an epidemic spreads widely in the same way that a giant component forms ([epidemics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md)).
- **Siblings:** [the probabilistic method](the-probabilistic-method.md) asks whether some graph has a property, this leaf asks what a typical graph is like; [finite probability spaces](finite-probability-spaces.md) make G(n, p) a product of n(n − 1)/2 independent coin tosses.

## Common misconceptions
- **"Once the average degree passes 1, the graph is connected."**: the giant component appears at average degree 1, but connectivity needs average degree about ln n. In between, the giant coexists with many small components and isolated vertices.
- **"Every threshold is sudden."**: at p = c/n a triangle appears with probability tending to 1 − e^(−c³/6), which rises gradually with c. Connectivity, by contrast, switches on in a window of width about 1/n around ln n/n.
- **"G(n, p) is a good model of real networks."**: its degrees are nearly Poisson and it has few triangles, while many real networks have heavy-tailed degrees and much clustering, which the small-world (1998) and preferential attachment (1999) models were designed to capture.

## Go deeper
- Bollobás, *Random Graphs* (2nd edition, 2001): the classic monograph, from thresholds to the giant component.
- Janson, Łuczak and Ruciński, *Random Graphs* (2000): subgraph counts, Poisson approximation and the phase transition.
- Frieze and Karoński, *Introduction to Random Graphs* (2016): a modern graduate text with complete proofs.
