# Graph Theory

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › Graph Theory
> **Children:** [Graphs and connectivity](graphs-and-connectivity.md) · [Trees](trees.md) · [Matchings and network flows](matchings-and-network-flows.md) · [Colouring and planarity](colouring-and-planarity.md)

## What this area is about
A graph records which pairs among a set of objects are connected, and nothing else. That austerity is its strength: the same theorems apply to road networks, molecules, schedules, electrical circuits and the internet. Graph theory asks how global properties (connectedness, the existence of a perfect pairing, the number of colours needed, whether a crossing-free drawing exists) follow from local data. Its answers come in two characteristic forms. Some are exact characterisations, such as "bipartite if and only if no odd cycle" or "planar if and only if no subdivision of K₅ or K₃,₃". Others are min–max theorems in which an obvious obstruction turns out to be the only one, such as Hall's, König's, Menger's and max-flow min-cut. The proofs lean on induction over vertices or edges, double counting, and extremal choices such as a longest path.

## How the children fit together
| Child | Its role in the whole | Depends on |
|---|---|---|
| [Graphs and connectivity](graphs-and-connectivity.md) | Vocabulary, degrees, components, bipartiteness, Euler circuits, Menger's theorem | Enumeration, layers 00–01 |
| [Trees](trees.md) | Minimal connected graphs: characterisations, spanning trees, Cayley's formula, greedy optimisation | Graphs and connectivity |
| [Matchings and network flows](matchings-and-network-flows.md) | Min–max theorems: Hall, König, max-flow min-cut, augmenting paths | Graphs and connectivity, trees |
| [Colouring and planarity](colouring-and-planarity.md) | Euler's formula, Kuratowski's theorem, chromatic number, the four colour theorem | Graphs and connectivity, trees |

```
              graphs and connectivity
                       |
                     trees
                   /       \
     matchings and flows   colouring and planarity
```

Graphs and connectivity sets up the language and the first structural results, including the parity arguments behind Euler circuits and bipartiteness. Trees come next because they are the skeleton of every connected graph: a spanning tree certifies connectivity, and removing a leaf is the standard inductive step. The tree then feeds both later leaves. Matchings and flows grow optimal structures by augmenting paths and certify optimality by cuts, and they supply the proof of Menger's theorem, announced in the first leaf. Colouring and planarity starts Euler's formula from a spanning tree, uses it to show planar graphs are sparse, and turns sparsity into colourings by induction, ending with the four colour theorem and its computer proof. The two branches meet again in edge colouring, which splits a bipartite graph into matchings.

## Connections to sibling areas
- [Enumeration](../01-enumeration/README.md): graphs are counted with its tools; the handshake lemma is double counting, and Cayley's formula and the Catalan count of binary trees come from bijections and generating functions.
- [Discrete probability](../03-discrete-probability/README.md): random graphs G(n, p) are the main laboratory of the probabilistic method, and random walks on graphs are the simplest Markov chains.
- [Extremal combinatorics](../04-extremal-combinatorics/README.md): Ramsey and Turán theory ask how many edges or how much order force a given subgraph, and the chromatic number of the forbidden graph decides the answer.

## Connections across layers
- Below: graphs are symmetric [relations](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md), and components are [equivalence classes](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md).
- Above: adjacency and Laplacian matrices bring in [the spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md) and [determinants](../../04-linear-algebra/02-determinants-and-eigenvalues/determinants.md); Cayley graphs of groups link to [free groups](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md); Euler's formula is the [Euler characteristic](../../07-topology/02-algebraic-topology/the-euler-characteristic.md); min–max theorems are [linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md) duality; the four colour theorem is a landmark in [computers and proof](../../15-mathematics-in-context/computers-and-proof.md).
- In computing, these theorems underlie [graph algorithms](../../../cs-first-principles/05-algorithms-and-data-structures/05-graph-algorithms/README.md).

## Cross-cutting threads
- [Duality](../../CROSS-CUTTING.md#duality): matchings against covers, flows against cuts.
- [Invariants](../../CROSS-CUTTING.md#invariants): degree parity, Euler's V − E + F, the chromatic number.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): odd cycles, Hall violators, K₅ and K₃,₃ as certificates of what cannot be done.
- [Local to global](../../CROSS-CUTTING.md#local-to-global): bounded degrees and local sparsity control global colourings.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): augmenting-path proofs are algorithms that construct what they prove exists.
