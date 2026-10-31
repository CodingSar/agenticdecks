# Point-Set Topology

> **Layer:** [07 Topology](../README.md) › Point-Set Topology
> **Children:** [Topological Spaces and Continuous Maps](topological-spaces-and-continuous-maps.md) · [Subspaces, Products and Quotients](subspaces-products-and-quotients.md) · [Compactness](compactness.md) · [Connectedness](connectedness.md) · [Separation Axioms and Metrisability](separation-axioms-and-metrisability.md)

## What this area is about

Real analysis showed that continuity, convergence and compactness can be phrased entirely through open sets of a metric space, without mentioning distances. Point-set topology takes that observation as a definition. A topological space is a set together with a chosen family of "open" subsets, closed under arbitrary unions and finite intersections, and a continuous map is one that pulls open sets back to open sets. That small change of primitive buys a great deal: spaces with no natural metric, such as infinite products, quotients obtained by gluing, and the Zariski topology of algebraic geometry, become legitimate objects, and theorems proved once apply to all of them.

The area has two jobs. It builds spaces, by restricting to subsets, multiplying and gluing. And it isolates the properties that make analysis work, chiefly compactness (every open cover has a finite subcover) and connectedness (the space does not split into two open pieces), together with the separation axioms that say how well points and closed sets can be kept apart. Each property is shown to be preserved by continuous maps, so it is a topological invariant, and each is tested against counterexamples that show what breaks without it.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Topological spaces and continuous maps](topological-spaces-and-continuous-maps.md) | The open-set axioms, continuity, homeomorphism, bases | 06 metric spaces, 01 sets |
| [Subspaces, products and quotients](subspaces-products-and-quotients.md) | Building new spaces; why the product topology beats the box topology; gluing | Topological spaces, 01 quotients |
| [Compactness](compactness.md) | Open covers, Heine–Borel, Tychonoff's theorem and the axiom of choice | Spaces, products |
| [Connectedness](connectedness.md) | Connected versus path-connected; the topologist's sine curve; components | Spaces, subspaces |
| [Separation axioms and metrisability](separation-axioms-and-metrisability.md) | Hausdorff spaces, Urysohn's lemma, when a topology comes from a metric | Compactness, products |

The first leaf fixes the language; the second supplies the constructions that every later leaf uses for examples. Compactness and connectedness are the two great invariants, each the abstract form of a property of [0, 1] that analysis relies on: the extreme value theorem and the intermediate value theorem. The last leaf closes the circle by asking when the abstraction gives nothing new, that is, when a topology is induced by some metric. Urysohn's answer, for second-countable spaces, is that a regular Hausdorff space is metrisable, which is exactly why manifolds can be treated as metric spaces.

```
           topological spaces, continuity
                       │
           subspaces, products, quotients
              │                    │
         compactness          connectedness
              │                    │
   separation and metrisability    │
              └─────────┬──────────┘
                        ▼
          algebraic topology, manifolds
```

## Connections to sibling areas

- [Algebraic topology](../02-algebraic-topology/README.md): homotopy needs products (X × [0, 1]) and quotients (cell complexes); path-connectedness makes the fundamental group independent of the base point; compactness of [0, 1] powers the path-lifting argument.
- [Manifolds](../03-manifolds/README.md): the definition of a manifold uses the Hausdorff property and second countability, and surfaces are built as quotients of polygons.

## Connections across layers

- [06 Real analysis](../../06-real-analysis/README.md): metric spaces, sequences and the Heine–Borel theorem are the model this area generalises.
- [01 Sets and foundations](../../01-sets-and-foundations/README.md): quotients by equivalence relations, cardinality and the axiom of choice, which Tychonoff's theorem is equivalent to.
- [09 Advanced analysis](../../09-advanced-analysis/README.md): weak topologies on Banach spaces are not metrisable, and compactness in them comes from Tychonoff.
- [12 Number theory and algebraic geometry](../../12-number-theory-and-algebraic-geometry/README.md): the Zariski topology is compact but not Hausdorff.

## Cross-cutting threads

- [Abstraction and generalisation](../../CROSS-CUTTING.md#abstraction-and-generalisation): open sets replace distances.
- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): finite subcovers turn local bounds into global ones.
- [Equivalence and quotients](../../CROSS-CUTTING.md#equivalence-and-quotients): gluing spaces by identifying points.
- [Structure and morphism](../../CROSS-CUTTING.md#structure-and-morphism): continuous maps as the morphisms; products and quotients by universal properties.
- [Invariants](../../CROSS-CUTTING.md#invariants): compactness and connectedness are preserved by homeomorphisms.
