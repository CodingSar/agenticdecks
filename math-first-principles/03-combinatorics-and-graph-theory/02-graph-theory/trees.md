# Trees

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Graph Theory](README.md)
> **Builds on:** [Graphs and connectivity](graphs-and-connectivity.md), [Combinatorial sequences](../01-enumeration/combinatorial-sequences.md), [Mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md)
> **Enables:** [Colouring and planarity](colouring-and-planarity.md), [Determinants](../../04-linear-algebra/02-determinants-and-eigenvalues/determinants.md), [Free groups and presentations](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md), [Minimum spanning trees](../../../cs-first-principles/05-algorithms-and-data-structures/05-graph-algorithms/minimum-spanning-trees.md), [Search trees](../../../cs-first-principles/05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md)

## Essence
A tree is a connected graph with no cycles: just enough edges to hold the vertices together and not one more. This balance makes trees the skeleton of every connected graph, the natural shape of hierarchies and recursive data, and the base case of most inductive arguments about graphs, because a tree always has a leaf that can be removed. Trees are counted exactly (there are nⁿ⁻² labelled trees on n vertices), found greedily (the cheapest spanning tree is built by always taking the cheapest safe edge), and characterised in half a dozen equivalent ways, each useful in a different proof.

## Core tenets
1. **Every finite tree with at least two vertices has at least two leaves.** Take a longest path; an end vertex has no neighbour off the path, since that would extend it, and no other neighbour on the path, since that would close a cycle, so it has degree 1. Removing a leaf leaves a smaller tree, which is the engine of induction on trees. The finiteness hypothesis matters: the two-way infinite path is an infinite tree with no leaves.

2. **For a graph G on n vertices, the following are equivalent.** G is a tree; G is connected with n − 1 edges; G is acyclic with n − 1 edges; G is minimally connected (deleting any edge disconnects it); G is maximally acyclic (adding any edge creates a cycle); between any two vertices there is exactly one path. The key fact behind all of them: adding an edge to a graph either joins two components or closes a cycle, never both, so a graph with n vertices, c components and no cycle has exactly n − c edges.

3. **Every connected graph has a spanning tree.** Delete edges lying on cycles one at a time; each deletion keeps the graph connected, since the rest of the cycle reroutes around the edge, and the process stops at a connected acyclic subgraph on all vertices. So a connected graph has at least n − 1 edges, and a spanning tree is a minimal certificate of connectivity. Breadth-first search builds one that also records shortest distances from a root.

4. **Cayley's formula: there are nⁿ⁻² labelled trees on vertices {1, …, n}.** Prüfer's bijection removes the leaf with the smallest label n − 2 times, recording each time the label of its neighbour; the resulting sequence in {1, …, n}ⁿ⁻² determines the tree, because a vertex's degree is one more than its number of appearances, so the leaf removed at each step can be recovered. The count is for labelled trees; unlabelled trees, counted up to isomorphism, have no closed formula.

5. **The matrix-tree theorem counts spanning trees of any graph as a determinant.** Kirchhoff's theorem says the number of spanning trees equals any cofactor of the Laplacian matrix D − A, where D is the diagonal matrix of degrees. For the complete graph this gives Cayley's nⁿ⁻² again. The proof expands the determinant over edge subsets (the Cauchy–Binet formula) and belongs to [determinants](../../04-linear-algebra/02-determinants-and-eigenvalues/determinants.md).

6. **Greedy algorithms find minimum spanning trees because of the cut property.** For any split of the vertices into two sides, a cheapest edge crossing the split lies in some minimum spanning tree: exchange it for the crossing edge on the tree path between its ends, and the cost does not rise. Kruskal's algorithm (add the cheapest edge that closes no cycle) and Prim's algorithm (grow one tree by its cheapest outgoing edge) both only ever add such edges. Matroids are exactly the structures on which this greedy rule is always optimal, so trees are the model case of a wider theory.

7. **König's lemma: an infinite, connected, locally finite graph contains an infinite path.** From a vertex, infinitely many vertices are reachable through finitely many neighbours, so by the infinite pigeonhole principle one neighbour leads to infinitely many; repeat forever. Local finiteness is essential: an infinite star has every path of length at most 2. The lemma is a combinatorial form of compactness, and turns finite statements into infinite ones and back, as in [Ramsey theory](../04-extremal-combinatorics/ramsey-theory.md).

8. **Rooted trees model recursion, and their counts are Catalan numbers.** A rooted binary tree is empty or a root with an ordered pair of subtrees, so binary trees with n nodes are counted by the Catalan number Cₙ ([combinatorial sequences](../01-enumeration/combinatorial-sequences.md)). Search trees, parse trees and recursion trees in computing are this structure; in algebra, the Cayley graph of a free group is a tree, which is how [free groups](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md) are recognised.

## Key concepts
| Term | Meaning |
|---|---|
| Tree | A connected graph with no cycles |
| Forest | A graph with no cycles; each component is a tree |
| Leaf | A vertex of degree 1 |
| Spanning tree | A subgraph that is a tree and contains every vertex |
| Prüfer sequence | A sequence of n − 2 labels encoding a labelled tree |
| Laplacian matrix | D − A, degrees on the diagonal minus adjacency |
| Cut property | A cheapest edge across any split lies in some minimum spanning tree |
| Locally finite | Every vertex has finite degree |
| Rooted tree | A tree with a distinguished vertex, giving parent–child structure |

## How it fits
- **Below:** Trees are special [graphs](graphs-and-connectivity.md); their properties are proved by [induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md) on leaves; Catalan counts come from [combinatorial sequences](../01-enumeration/combinatorial-sequences.md).
- **Above:** The matrix-tree theorem is [linear algebra](../../04-linear-algebra/02-determinants-and-eigenvalues/determinants.md); trees as Cayley graphs identify [free groups](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md); a graph is homotopy equivalent to a wedge of circles, one per non-tree edge ([the Euler characteristic](../../07-topology/02-algebraic-topology/the-euler-characteristic.md)); spanning trees are core to [network algorithms](../../../cs-first-principles/05-algorithms-and-data-structures/05-graph-algorithms/minimum-spanning-trees.md) and [routing](../../../cs-first-principles/08-networking/03-network-layer/routing-algorithms.md).
- **Siblings:** [Colouring and planarity](colouring-and-planarity.md) proves Euler's formula by induction starting from a spanning tree; [matchings](matchings-and-network-flows.md) on trees are found greedily from the leaves.

## Common misconceptions
- **"Every tree has a leaf"**: true for finite trees with at least two vertices, false for infinite ones such as the two-way infinite path.
- **"nⁿ⁻² counts trees on n vertices"**: it counts labelled trees. On 4 vertices there are 16 labelled trees but only 2 up to isomorphism, the path and the star.
- **"Greedy algorithms are always optimal on graphs"**: greedy works for spanning trees because of the cut property; for shortest tours or maximum independent sets it can fail badly.

## Go deeper
- Diestel, *Graph Theory* (5th edition, 2017): chapter 1 proves the equivalent definitions of trees and develops infinite graphs.
- Aigner and Ziegler, *Proofs from THE BOOK* (1998): four proofs of Cayley's formula, side by side.
- Schrijver, *Combinatorial Optimization* (2003): spanning trees, matroids and the greedy algorithm in full depth.
