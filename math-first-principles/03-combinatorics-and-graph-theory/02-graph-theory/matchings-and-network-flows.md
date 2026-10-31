# Matchings and Network Flows

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Graph Theory](README.md)
> **Builds on:** [Graphs and connectivity](graphs-and-connectivity.md), [Trees](trees.md), [Mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md)
> **Enables:** [Posets and extremal set theory](../04-extremal-combinatorics/posets-and-extremal-set-theory.md), [Linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md), [Convex optimisation and duality](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md), [Network flow algorithms](../../../cs-first-principles/05-algorithms-and-data-structures/05-graph-algorithms/network-flow.md)

## Essence
A matching pairs vertices along edges with no vertex used twice: workers with jobs, students with schools, rows with columns. A flow sends material from a source to a sink through a network of capacitated pipes. Both problems have the same shape: an obvious obstruction (too few neighbours, a narrow cut) bounds the best possible value, and the theorems of Hall, König, Menger and Ford–Fulkerson say that the obvious obstruction is the only one. These min–max theorems are the combinatorial face of linear programming duality, and their proofs are algorithms: improve along an augmenting path until a certificate of optimality appears.

## Core tenets
1. **Hall's theorem (1935): a bipartite graph with sides X and Y has a matching covering X if and only if ∣N(S)∣ ≥ ∣S∣ for every S ⊆ X**, where N(S) is the set of neighbours of S. Necessity is clear. For sufficiency, induct on ∣X∣. If every non-empty proper S has ∣N(S)∣ > ∣S∣, match any x to any neighbour and delete both; the condition survives. Otherwise some proper S is tight, ∣N(S)∣ = ∣S∣: match S into N(S) by induction, and X ∖ S into Y ∖ N(S), where Hall's condition holds because a violating T would make S ∪ T violate it in G.

2. **Hall's theorem needs X to be finite.** Let X = {x₀, x₁, …} and Y = {y₁, y₂, …}, with x₀ adjacent to every yᵢ and each other xᵢ adjacent only to yᵢ. Every finite S satisfies Hall's condition, yet x₁, x₂, … use up all of Y and leave x₀ unmatched. The theorem does extend to infinite X when every vertex of X has finite degree, by a compactness argument.

3. **Regular bipartite graphs have perfect matchings.** If every vertex has degree k ≥ 1, the k∣S∣ edges leaving S ⊆ X all land in N(S), which receives at most k∣N(S)∣ edges, so ∣N(S)∣ ≥ ∣S∣. Removing the matching leaves a (k − 1)-regular graph, so the edges split into k perfect matchings; this is why every Latin rectangle extends to a Latin square.

4. **König's theorem (1931): in a bipartite graph, the maximum size of a matching equals the minimum size of a vertex cover.** A cover must contain an end of each matching edge, so a matching is never larger than a cover. Equality is the content and fails without bipartiteness: a triangle has maximum matching 1 and minimum cover 2.

5. **Augmenting paths certify optimality (Berge, 1957).** A path whose edges alternate between non-matching and matching edges, with both ends unmatched, can be flipped to enlarge the matching. Conversely, if M′ is larger than M, the symmetric difference M △ M′ splits into alternating paths and cycles, and one path has more edges of M′, an augmenting path for M. In general graphs Tutte's theorem gives the obstruction to a perfect matching (a set S whose removal leaves more than ∣S∣ components of odd size), and Edmonds' blossom algorithm finds maximum matchings in polynomial time.

6. **Max-flow min-cut (Ford and Fulkerson, 1956): the maximum value of an s–t flow equals the minimum capacity of a cut separating s from t.** For any set S containing s but not t, the net flow out of S equals the flow value, so no flow exceeds any cut. If the residual network, which records the spare capacity forwards and the cancellable flow backwards, has no path from s to t, let S be the vertices it reaches from s: every edge leaving S is saturated and every edge entering S is empty, so the flow value equals the capacity of S.

7. **Integral capacities give integral optimal flows, which yields the other theorems.** Starting from zero and augmenting by whole units keeps every flow value an integer and terminates. With unit capacities, a flow becomes a set of disjoint paths, so Hall, König and Menger all follow by building the right network. The integrality hypothesis matters: with irrational capacities a poorly chosen augmentation sequence can fail to terminate, whereas always augmenting along a shortest path (Edmonds and Karp) runs in polynomial time on any capacities.

8. **These theorems are linear programming duality with integral optima.** Maximum flow and minimum cut are a pair of dual linear programs, and the constraint matrix of a bipartite or network problem is totally unimodular (every square submatrix has determinant 0 or ±1), so the programs have integral optimal solutions. Min–max equality is then strong duality from [linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md), and the certificates are the dual solutions.

## Key concepts
| Term | Meaning |
|---|---|
| Matching | A set of edges with no shared vertex |
| Perfect matching | A matching covering every vertex |
| Hall's condition | ∣N(S)∣ ≥ ∣S∣ for every subset S of one side |
| Vertex cover | A set of vertices meeting every edge |
| Augmenting path | An alternating path joining two unmatched vertices |
| Flow | An assignment of amounts to edges, within capacities and conserved at inner vertices |
| Cut | A vertex set S containing s but not t; its capacity is the total capacity of edges leaving it |
| Residual network | Spare capacity forwards plus cancellable flow backwards |
| Total unimodularity | Every square submatrix has determinant 0, 1 or −1 |

## How it fits
- **Below:** Matchings live in [graphs](graphs-and-connectivity.md) and are proved by [induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md); greedy matching from the leaves of a [tree](trees.md) is the simplest case.
- **Above:** Min–max theorems are [linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md) and [convex duality](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md); the algorithms are [network flow](../../../cs-first-principles/05-algorithms-and-data-structures/05-graph-algorithms/network-flow.md); stable matchings and assignment problems lead to [game theory](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/game-theory.md).
- **Siblings:** Menger's theorem in [graphs and connectivity](graphs-and-connectivity.md) is a flow corollary; König's theorem proves Dilworth's theorem in [posets](../04-extremal-combinatorics/posets-and-extremal-set-theory.md); edge colourings of bipartite graphs in [colouring](colouring-and-planarity.md) come from repeated matchings.

## Common misconceptions
- **"A maximal matching is maximum"**: a matching that cannot be extended may still be half the maximum size; on a path with three edges the middle edge alone is maximal but not maximum.
- **"Max-flow min-cut needs integer capacities"**: the equality holds for any non-negative real capacities; integrality is needed only for the optimal flow to be integral and for naive augmentation to terminate.
- **"König's theorem holds in all graphs"**: an odd cycle already breaks it; in general graphs the obstruction is Tutte's.

## Go deeper
- Lovász and Plummer, *Matching Theory* (1986): the definitive account of matchings in bipartite and general graphs.
- Ford and Fulkerson, *Flows in Networks* (1962): the founders' own development of flows and their combinatorial corollaries.
- Schrijver, *Combinatorial Optimization* (2003): matchings, flows and total unimodularity unified by polyhedral methods.
