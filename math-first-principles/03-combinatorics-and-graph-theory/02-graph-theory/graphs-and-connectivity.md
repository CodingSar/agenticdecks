# Graphs and Connectivity

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Graph Theory](README.md)
> **Builds on:** [Relations and orders](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md), [Equivalence relations and quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md), [Counting principles and binomial coefficients](../01-enumeration/counting-principles-and-binomial-coefficients.md), [Mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md)
> **Enables:** [Trees](trees.md), [Matchings and network flows](matchings-and-network-flows.md), [Colouring and planarity](colouring-and-planarity.md), [The spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md), [Graph traversal](../../../cs-first-principles/05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md)

## Essence
A graph is a set of vertices together with a set of edges, each edge joining two vertices. It is the simplest mathematical model of anything made of pairwise connections: road maps, molecules, networks, dependencies, social ties. Graph theory asks which global properties follow from local structure: whether everything is reachable from everything, whether one can walk every edge once, how many vertices must fail before the network falls apart. Its basic tools are counting (the handshake lemma), induction on vertices or edges, and the extremal choice of a longest path or a smallest counterexample.

## Core tenets
1. **A simple graph is a symmetric, irreflexive relation on a finite vertex set.** Writing G = (V, E) with each edge an unordered pair {u, v} of distinct vertices, adjacency is a relation that is symmetric (edges have no direction) and irreflexive (no loops). Dropping symmetry gives directed graphs, which model one-way roads and dependencies; allowing repeated edges or loops gives multigraphs. Isomorphic graphs, related by an adjacency-preserving bijection, count as the same.

2. **The handshake lemma: the degrees add up to twice the number of edges.** Counting the pairs (vertex, edge at that vertex) by vertices gives ∑ deg v, and by edges gives 2∣E∣, since each edge has two ends. Hence the number of vertices of odd degree is even: at any party, the number of people who shook an odd number of hands is even.

3. **Connectivity is an equivalence relation, and components are its classes.** Say u ∼ v when some walk joins u to v. Reflexivity uses the walk of length 0, symmetry reverses the walk, and transitivity concatenates walks, so ∼ is an equivalence relation and V splits into connected components. Any walk from u to v contains a path, a walk with no repeated vertex, obtained by cutting out the loops between repeated visits.

4. **A graph is bipartite if and only if it has no cycle of odd length.** A cycle in a bipartite graph alternates sides, so it has even length. Conversely, in a connected graph with no odd cycle, fix a vertex r and colour each vertex by the parity of its distance from r; an edge between two vertices of the same parity would close, with the two shortest paths to r, a closed walk of odd length, which always contains an odd cycle. Do this in every component.

5. **An Euler circuit exists if and only if the graph is connected (apart from isolated vertices) and every degree is even.** Each pass through a vertex uses two edges, so the condition is necessary, which settled Euler's Königsberg bridge problem (1736) negatively. For sufficiency, a walk that never repeats an edge can only get stuck at its start, so it closes into a circuit; if edges remain, splice in a circuit through a vertex already visited and repeat. Euler circuits are found in linear time.

6. **Hamiltonian cycles, which visit every vertex once, have no comparable criterion.** Deciding whether one exists is NP-complete, that is, as hard as any problem in NP (nondeterministic polynomial time, the problems whose solutions can be checked quickly), so no simple characterisation is expected unless P = NP ([complexity](../../../cs-first-principles/02-theory-of-computation/04-complexity/p-np-and-np-completeness.md)). Sufficient conditions exist: Dirac proved that a graph on n ≥ 3 vertices with minimum degree at least n/2 is Hamiltonian, by taking a longest path and showing its ends can be joined into a cycle through all its vertices.

7. **Menger's theorem: the minimum number of vertices separating u from v equals the maximum number of internally disjoint u–v paths, for non-adjacent u and v.** Disjoint paths each need a separate removed vertex, so the minimum is at least the maximum; equality is the deep part, best proved by [network flows](matchings-and-network-flows.md). A graph is k-connected when it has more than k vertices and no set of fewer than k vertices disconnects it, so Menger says k-connectivity means k disjoint routes between every pair.

8. **The adjacency matrix turns walks into algebra.** With A the V × V matrix whose (u, v) entry is 1 for an edge, the (u, v) entry of Aᵏ counts walks of length k from u to v, by induction on k via the definition of matrix multiplication. Eigenvalues of A and of the Laplacian D − A then encode structure: the multiplicity of the Laplacian eigenvalue 0 equals the number of components. Spectral graph theory needs [the spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md); its limit is that non-isomorphic graphs can share a spectrum.

## Key concepts
| Term | Meaning |
|---|---|
| Graph | A vertex set with edges, each an unordered pair of distinct vertices |
| Degree | The number of edges at a vertex |
| Walk, path, cycle | A sequence of adjacent vertices; one with no repeated vertex; a closed path of length at least 3 |
| Connected component | A class of the equivalence relation "joined by a walk" |
| Bipartite graph | A graph whose vertices split into two sides with every edge crossing |
| Euler circuit | A closed walk using every edge exactly once |
| Hamiltonian cycle | A cycle through every vertex |
| k-connected | Remains connected after deleting any fewer than k vertices |
| Adjacency matrix | The 0–1 matrix of the adjacency relation |

## How it fits
- **Below:** Graphs are [relations](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md), components are [equivalence classes](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md), and the handshake lemma is [double counting](../01-enumeration/counting-principles-and-binomial-coefficients.md).
- **Above:** Spectral methods use [the spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md) and [Perron–Frobenius theory](../../04-linear-algebra/02-determinants-and-eigenvalues/non-negative-matrices-and-perron-frobenius.md); random walks on graphs are [Markov chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md); search and shortest paths are [graph algorithms](../../../cs-first-principles/05-algorithms-and-data-structures/05-graph-algorithms/README.md); graph structure underlies [network models in medicine](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/03-systems-and-models/nonlinear-dynamics-oscillations-and-networks.md).
- **Siblings:** [Trees](trees.md) are the minimal connected graphs; [matchings and flows](matchings-and-network-flows.md) prove Menger's theorem; [colouring and planarity](colouring-and-planarity.md) generalise bipartiteness.

## Common misconceptions
- **"Graphs with the same degree sequence are isomorphic"**: a 6-cycle and two disjoint triangles both have every degree equal to 2, but one is connected and the other is not.
- **"Euler circuits and Hamiltonian cycles are equally hard"**: the edge version has a parity criterion and a linear-time algorithm; the vertex version is NP-complete.
- **"The spectrum determines the graph"**: the star with four leaves and the disjoint union of a 4-cycle with an isolated vertex have the same adjacency eigenvalues.

## Go deeper
- Diestel, *Graph Theory* (5th edition, 2017): the standard rigorous graduate text, with full proofs of Menger's theorem.
- West, *Introduction to Graph Theory* (2nd edition, 2001): a careful first course with many exercises.
- Bollobás, *Modern Graph Theory* (1998): connectivity, flows and random graphs from one author.
