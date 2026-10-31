# 07 Topology

> **Layer:** 07 Topology
> **Children:** [Point-Set Topology](01-point-set-topology/README.md) · [Algebraic Topology](02-algebraic-topology/README.md) · [Manifolds](03-manifolds/README.md)

## What this area is about

Topology is the study of the properties of a space that survive continuous deformation: stretching, bending and squeezing, but not tearing or gluing. A coffee cup and a doughnut are the same to a topologist, because each has one hole; a sphere and a torus are different, and topology explains why that difference can be proved and not merely seen. The subject asks three kinds of question. What is a space, and what is a continuous map, once distances are forgotten? How can two spaces be shown to be different, or a map shown not to exist? And which spaces are there: can they be listed?

The layer answers in three areas. Point-set topology takes open sets as the primitive notion and isolates the properties analysis depends on, compactness and connectedness above all. Algebraic topology attaches groups to spaces, the fundamental group and homology, so that a difference of groups proves a difference of spaces, and draws from them the Euler characteristic and the fixed-point theorems; higher homotopy groups and fibrations extend the first, and cohomology, with its cup product and Poincaré duality, refines the second. Manifolds, the spaces that look locally like ℝⁿ, are where these tools meet their main objects: surfaces are classified completely, knots are distinguished by polynomials, and three-dimensional spaces were classified geometrically when Perelman proved the Poincaré conjecture.

The basic abstraction is **the invariant**: a quantity or structure that homeomorphic spaces share, so that a difference in the invariant proves the spaces different.

## Why this layer sits here

Topology needs three things from below. [06 Real Analysis](../06-real-analysis/README.md) supplies the model: in a metric space, continuity, convergence and compactness can all be expressed through open sets, and that observation is the definition of a topological space. [05 Abstract Algebra](../05-abstract-algebra/README.md) supplies groups, presentations and quotient groups, the language of the fundamental group and homology, and the Galois correspondence that covering spaces imitate. [04 Linear Algebra](../04-linear-algebra/README.md) supplies rank and dimension, which make homology computable and the Euler characteristic invariant. Underneath, [01 Sets and Foundations](../01-sets-and-foundations/README.md) supplies quotients by equivalence relations, cardinality, and the axiom of choice, to which Tychonoff's theorem is equivalent.

Topology is in turn a foundation for what follows. Geometry in layer 08 adds curvature and metrics to manifolds. Complex and functional analysis in 09 use winding numbers, Riemann surfaces and weak topologies. Differential equations in 10 live on manifolds, and homological algebra in 13 abstracts the chain complexes of homology. So the layer sits after the algebra and analysis it combines, and before the geometry and analysis that use it.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Point-Set Topology](01-point-set-topology/README.md) | The language: open sets, continuity, products and quotients, compactness, connectedness, separation and metrisability | 06 metric spaces, 01 sets and choice |
| [Algebraic Topology](02-algebraic-topology/README.md) | The invariants: fundamental group, covering spaces, homology, Euler characteristic, fixed-point theorems, higher homotopy groups, cohomology and duality | Point-set topology, 05 groups, 04 linear algebra |
| [Manifolds](03-manifolds/README.md) | The main objects: smooth structures, surfaces, knots, three-manifolds and the Poincaré conjecture | Both of the above, 06 several-variable calculus |

Point-set topology is the grammar: without products, quotients and compactness, there is no way to define a homotopy, glue a cell complex, or lift a path. Algebraic topology is the toolkit: it turns questions about spaces into questions about groups. Manifolds are the subject matter on which the toolkit is tested, and they repay it with the theorems the layer is famous for.

```
   06 metric spaces        05 groups        04 rank, dimension
          │                    │                  │
          ▼                    │                  │
   point-set topology          │                  │
   open sets, compactness,     │                  │
   connectedness, quotients    │                  │
          │                    ▼                  ▼
          └──────────► algebraic topology ◄───────┘
          │            π₁, covers, homology, χ, fixed points,
          │            πₙ and fibrations, cohomology, duality
          │                    │
          ▼                    ▼
      manifolds: smooth structures, surfaces, knots, 3-manifolds
                               │
                               ▼
         08 geometry, 09 complex analysis, 10 dynamics, 13 homological algebra
```

## Connections to neighbouring layers

- **[01 Sets and Foundations](../01-sets-and-foundations/README.md):** quotient spaces are quotient sets with a topology; Tychonoff's theorem is equivalent to the axiom of choice (Kelley, 1950).
- **[04 Linear Algebra](../04-linear-algebra/README.md):** rank–nullity proves the Euler characteristic is an invariant; tangent spaces are vector spaces.
- **[05 Abstract Algebra](../05-abstract-algebra/README.md):** connected covers correspond to subgroups of π₁ just as intermediate fields correspond to subgroups of a Galois group.
- **[06 Real Analysis](../06-real-analysis/README.md):** metric spaces are the model; the implicit function theorem builds manifolds.
- **[08 Geometry](../08-geometry/README.md):** Gauss–Bonnet makes χ a total curvature; de Rham cohomology recovers real cohomology from differential forms; characteristic classes are cohomology classes of vector bundles; Riemannian metrics live on manifolds.
- **[09 Advanced Analysis](../09-advanced-analysis/README.md):** winding numbers in Cauchy's theorem; Riemann surfaces as branched covers; compactness in weak topologies.
- **[10 Differential Equations and Dynamics](../10-differential-equations-and-dynamics/README.md):** Ricci flow is a nonlinear partial differential equation; phase spaces are manifolds; Schauder's fixed-point theorem gives existence of solutions.
- **[13 Structure and Metamathematics](../13-structure-and-metamathematics/README.md):** general homological algebra and category theory grew from homology; homotopy type theory reads types as spaces.

## Connections across layers

The layer's applications reach well beyond pure mathematics. Kakutani's extension of Brouwer's fixed-point theorem gives the existence of Nash equilibria in [game theory](../14-applied-and-computational-mathematics/05-games-decisions-and-finance/game-theory.md). Knot invariants arise from quantum field theory, and enzymes that knot and unlink DNA (deoxyribonucleic acid) are studied with them, as the [nucleic acids](../../medicine-first-principles/02-biochemistry-and-molecular-biology/01-macromolecules/nucleic-acids.md) leaf of the medicine tree describes. Triangle meshes in [computer graphics](../../cs-first-principles/14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md) are checked with V − E + F, and homology computed at many scales is a tool for finding shape in data, alongside the methods of [unsupervised learning](../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md). The Poincaré conjecture, the only Millennium Prize problem solved as of 2026, belongs to the story told in [open problems](../15-mathematics-in-context/open-problems.md).

## Cross-cutting threads

- [Invariants](../CROSS-CUTTING.md#invariants): compactness, π₁, homology, χ and knot polynomials.
- [Equivalence and quotients](../CROSS-CUTTING.md#equivalence-and-quotients): homeomorphism and homotopy as the equivalences; gluing as the construction.
- [Completeness and compactness](../CROSS-CUTTING.md#completeness-and-compactness): finite subcovers and Tychonoff's theorem.
- [Local to global](../CROSS-CUTTING.md#local-to-global): manifolds and covering spaces are locally trivial; Seifert–van Kampen assembles π₁ from pieces.
- [Duality](../CROSS-CUTTING.md#duality): cohomology dualises homology, and Poincaré duality pairs complementary degrees on a manifold.
- [Decomposition and classification](../CROSS-CUTTING.md#decomposition-and-classification): surfaces and three-manifolds.
- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): no retraction, no combing the sphere, no algorithm for 4-manifolds.
- [Dictionaries between fields](../CROSS-CUTTING.md#dictionaries-between-fields): covering spaces and Galois theory.
- [Existence and construction](../CROSS-CUTTING.md#existence-and-construction): fixed-point theorems prove existence without construction.
