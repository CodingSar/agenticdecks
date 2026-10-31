# Colouring and Planarity

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Graph Theory](README.md)
> **Builds on:** [Graphs and connectivity](graphs-and-connectivity.md), [Trees](trees.md), [Mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md)
> **Enables:** [Extremal graph theory](../04-extremal-combinatorics/extremal-graph-theory.md), [The Euler characteristic](../../07-topology/02-algebraic-topology/the-euler-characteristic.md), [Classification of surfaces](../../07-topology/03-manifolds/classification-of-surfaces.md), [Computers and proof](../../15-mathematics-in-context/computers-and-proof.md), [Register allocation](../../../cs-first-principles/06-programming-languages/03-compilers/code-generation-and-register-allocation.md)

## Essence
A proper colouring gives adjacent vertices different colours, and the chromatic number χ(G) is the fewest colours that suffice. Colouring models conflict avoidance: timetables, frequencies, registers. A planar graph is one that can be drawn in the plane without crossing edges. The two topics meet in the most famous problem of graph theory, whether every map can be coloured with four colours. The bridge is Euler's formula V − E + F = 2, which forces planar graphs to be sparse, hence to have a vertex of small degree, hence to be colourable with few colours by induction.

## Core tenets
1. **Euler's formula: a connected graph drawn without crossings, with V vertices, E edges and F faces, has V − E + F = 2.** Induct on the number of edges outside a spanning tree. A tree has E = V − 1 and one face, so the sum is 2. Adding an edge that closes a cycle increases E by one and splits one face into two, by the Jordan curve theorem, so the sum is unchanged. On a torus it becomes V − E + F = 0, the [Euler characteristic](../../07-topology/02-algebraic-topology/the-euler-characteristic.md) of the surface.

2. **Planar graphs are sparse: a simple planar graph with V ≥ 3 vertices has at most 3V − 6 edges.** Every face is bounded by at least three edges and every edge borders at most two faces, so 3F ≤ 2E; substituting into Euler's formula gives E ≤ 3V − 6. Hence K₅, with 10 > 9 edges, is not planar. In a bipartite graph faces have at least four sides, so E ≤ 2V − 4, and K₃,₃, with 9 > 8 edges, is not planar. The bound also means the average degree is below 6, so every planar graph has a vertex of degree at most 5.

3. **Kuratowski's theorem: a graph is planar if and only if it contains no subdivision of K₅ or K₃,₃.** Necessity holds because subdividing edges does not affect planarity. Sufficiency, proved by Kuratowski in 1930, is the hard direction. Wagner's equivalent version uses minors (contract edges as well as delete them), and the Robertson–Seymour graph minor theorem generalises it: every minor-closed family of graphs is characterised by finitely many forbidden minors.

4. **Greedy colouring uses at most Δ + 1 colours, and the bound is nearly sharp.** Colour vertices in any order with the first colour unused by coloured neighbours; a vertex has at most Δ (the maximum degree) neighbours, so Δ + 1 colours suffice. Brooks' theorem says Δ colours suffice for a connected graph unless it is complete or an odd cycle. Colouring is hard in general: deciding whether χ(G) ≤ 3 is NP-complete, and χ is not determined locally, since there are triangle-free graphs of any chromatic number (Mycielski's construction).

5. **The five colour theorem: every planar graph can be properly coloured with five colours.** Induct on V: remove a vertex v of degree at most 5 and colour the rest. If v's neighbours use at most four colours, v gets the fifth. Otherwise v has five neighbours v₁, …, v₅ in cyclic order with five colours. Consider the subgraph coloured with the colours of v₁ and v₃: if v₁ and v₃ lie in different components (Kempe chains), swap the two colours in v₁'s component, freeing a colour for v. If they are joined, that chain with v forms a cycle separating v₂ from v₄, so the chain of colours of v₂ and v₄ cannot join them, and swapping there frees a colour instead.

6. **The four colour theorem is true, and its proof needs a computer.** Guthrie posed the problem in 1852; Kempe's 1879 proof failed at a double swap, and Heawood repaired it to five colours in 1890. Appel and Haken proved four colours suffice in 1976 with an unavoidable set of reducible configurations: every planar triangulation contains one (a discharging argument), and none can occur in a minimal counterexample (a computer check). Robertson, Sanders, Seymour and Thomas gave a simpler computer proof in 1997, and Gonthier formally verified the theorem in the Coq proof assistant in 2005 ([computers and proof](../../15-mathematics-in-context/computers-and-proof.md)).

7. **Colouring depends on the surface.** On the torus, of Euler characteristic 0, Euler's formula permits denser graphs: the complete graph K₇ embeds there, and seven colours are needed and suffice. Ringel and Youngs completed Heawood's formula for the number of colours needed on every other closed surface, with one exception, the Klein bottle, which needs 6. The plane, the simplest surface, was the hardest case.

8. **Edge colouring is almost determined by the maximum degree.** A proper edge colouring gives edges at a common vertex different colours, so it needs at least Δ colours; Vizing's theorem says Δ + 1 always suffice for simple graphs. Bipartite graphs need exactly Δ, by splitting into matchings ([matchings](matchings-and-network-flows.md)).

## Key concepts
| Term | Meaning |
|---|---|
| Proper colouring | Adjacent vertices receive different colours |
| Chromatic number χ(G) | The fewest colours in a proper colouring |
| Euler's formula | V − E + F = 2 for connected plane graphs |
| Subdivision | A graph obtained by inserting vertices into edges |
| Minor | A graph obtained by deleting and contracting edges |
| Kempe chain | A component of the subgraph using two chosen colours |
| Reducible configuration | A subgraph that cannot occur in a minimal counterexample |

## How it fits
- **Below:** Built on [graphs](graphs-and-connectivity.md), spanning [trees](trees.md) and [induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md); the face-splitting step borrows the Jordan curve theorem from topology.
- **Above:** Euler's formula is the [Euler characteristic](../../07-topology/02-algebraic-topology/the-euler-characteristic.md) of the sphere, generalised by the [classification of surfaces](../../07-topology/03-manifolds/classification-of-surfaces.md) and the faces of [polytopes](../../08-geometry/03-convex-and-discrete-geometry/polytopes.md); the four colour proof is the classic case in [computers and proof](../../15-mathematics-in-context/computers-and-proof.md); colouring is [register allocation](../../../cs-first-principles/06-programming-languages/03-compilers/code-generation-and-register-allocation.md).
- **Siblings:** Two-colourability is bipartiteness in [graphs and connectivity](graphs-and-connectivity.md); chromatic number governs Turán density in [extremal graph theory](../04-extremal-combinatorics/extremal-graph-theory.md).

## Common misconceptions
- **"A graph that needs many colours must contain a large complete subgraph"**: Mycielski's triangle-free graphs have arbitrarily large chromatic number; the odd wheel with five spokes has no K₄ yet needs four colours.
- **"A non-planar graph contains K₅ or K₃,₃ as a subgraph"**: only a subdivision or a minor is guaranteed; the Petersen graph is non-planar but contains neither as a subgraph.
- **"The four colour proof is unverified computer output"**: it has been independently re-proved and formally verified in a proof assistant.

## Go deeper
- Wilson, *Four Colors Suffice* (2002): the history of the problem from Guthrie to the computer proofs.
- Diestel, *Graph Theory* (5th edition, 2017): planarity, colouring and the graph minor theorem with full proofs.
- Aigner and Ziegler, *Proofs from THE BOOK* (1998): the five colour theorem and the art of Euler's formula.
