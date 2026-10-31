# Polytopes

> **Layer:** [08 Geometry](../README.md) › [Convex and Discrete Geometry](README.md)
> **Builds on:** [Convex sets and separation](convex-sets-and-separation.md), [Symmetry groups and tilings](../01-classical-geometry/symmetry-groups-and-tilings.md), [The Euler characteristic](../../07-topology/02-algebraic-topology/the-euler-characteristic.md), [Colouring and planarity](../../03-combinatorics-and-graph-theory/02-graph-theory/colouring-and-planarity.md), [Group actions](../../05-abstract-algebra/01-groups/group-actions.md)
> **Enables:** [Lattices and sphere packing](lattices-and-sphere-packing.md), [Linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md), [The classification of simple Lie algebras](../04-lie-theory/the-classification-of-simple-lie-algebras.md), [Computational geometry](../../../cs-first-principles/05-algorithms-and-data-structures/07-advanced-topics/computational-geometry.md)

## Essence

A convex polytope is the convex hull of finitely many points, or equivalently a bounded intersection of finitely many half-spaces. Polytopes are where geometry, combinatorics and optimisation meet: Euler's formula V − E + F = 2 counts their faces, the regular ones are classified completely in every dimension, and linear programming is the search for the best vertex of a polytope. The classification of regular polytopes, 5 in three dimensions, 6 in four and 3 in each higher dimension, is one of the oldest complete classifications in mathematics.

## Core tenets

1. **A polytope has two descriptions, by vertices and by inequalities.** The Minkowski–Weyl theorem says the convex hull of finitely many points is a bounded intersection of finitely many half-spaces, and conversely. One direction follows from [separation](convex-sets-and-separation.md) and a finiteness argument on the faces; the other from projecting away variables. The two descriptions can differ enormously in size: the n-cube has 2ⁿ vertices but 2n facets, and converting between them is a central task in [computational geometry](../../../cs-first-principles/05-algorithms-and-data-structures/07-advanced-topics/computational-geometry.md).

2. **Euler's formula: V − E + F = 2 for every convex polyhedron.** Project the polyhedron's edges from a point just outside one face onto that face, giving a connected [planar graph](../../03-combinatorics-and-graph-theory/02-graph-theory/colouring-and-planarity.md) with the outer region as the extra face. Removing an edge on a cycle merges two faces, and removing a leaf edge deletes a vertex; both keep V − E + F unchanged, until a single vertex remains with V − E + F = 1 + 0 + 1. Convexity matters only through topology: a polyhedral picture frame, a torus, has V − E + F = 0, its [Euler characteristic](../../07-topology/02-algebraic-topology/the-euler-characteristic.md). Lakatos's *Proofs and Refutations* tells this story of counterexamples and repaired definitions.

3. **The higher-dimensional form is the Euler–Poincaré relation.** If fᵢ is the number of i-dimensional faces of a d-dimensional polytope, then the alternating sum of f₀, …, f_(d−1) equals 1 − (−1)ᵈ: 2 when d is 3, 0 when d is 4. The boundary is a topological sphere, and the formula is its Euler characteristic.

4. **There are exactly five Platonic solids.** A regular polyhedron with p-gon faces, q meeting at each vertex, has q · (1 − 2/p)π < 2π at a vertex, which simplifies to (p − 2)(q − 2) < 4. The solutions are {3, 3}, {4, 3}, {3, 4}, {5, 3} and {3, 5}: tetrahedron, cube, octahedron, dodecahedron and icosahedron, each realised. Duality swaps {p, q} and {q, p}. Their rotation groups are A₄, S₄ and A₅, of orders 12, 24 and 60. Equality (p − 2)(q − 2) = 4 gives the three regular [tilings](../01-classical-geometry/symmetry-groups-and-tilings.md) of the plane.

5. **Four dimensions have six regular polytopes, and higher dimensions three.** Schläfli found the regular convex 4-polytopes: the simplex {3, 3, 3}, the tesseract {4, 3, 3}, the 16-cell {3, 3, 4}, the self-dual 24-cell {3, 4, 3}, the 120-cell {5, 3, 3} and the 600-cell {3, 3, 5}. The same vertex-angle test, applied to the possible cells and vertex figures, leaves in each dimension d ≥ 5 only the simplex, the cube and the cross-polytope. The 24-cell, with no analogue elsewhere, is linked to the exceptional root system F₄ in [Lie theory](../04-lie-theory/the-classification-of-simple-lie-algebras.md).

6. **Face counts are bounded, and the simplex method walks along edges.** McMullen's upper bound theorem (1970) says that among d-dimensional polytopes with n vertices, the cyclic polytope has the most faces of every dimension, about n to the power ⌊d/2⌋ facets. [Linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md) maximises a linear function over a polytope, and the optimum is attained at a vertex; the simplex method moves from vertex to vertex along improving edges. Hirsch conjectured that the edge-distance between vertices is at most the number of facets minus d; Santos disproved it in 2010. Whether some polynomial bound holds, the polynomial Hirsch conjecture, is open as of 2026.

7. **Equal volume does not imply cut-and-reassemble equivalence in three dimensions.** In the plane, the Wallace–Bolyai–Gerwien theorem says polygons of equal area can be cut into finitely many pieces and reassembled into each other. In space Dehn (1900) answered Hilbert's third problem negatively: the Dehn invariant, the sum over edges of length ⊗ dihedral angle taken modulo rational multiples of π, is preserved by cutting and gluing, and it is 0 for a cube but not for a regular tetrahedron, whose dihedral angle arccos(1/3) is an irrational multiple of π.

## Key concepts

| Term | Meaning |
|---|---|
| Convex polytope | The convex hull of finitely many points; a bounded intersection of half-spaces |
| Face | The intersection of the polytope with a supporting hyperplane; vertices, edges, …, facets |
| Facet | A face of dimension one less than the polytope |
| f-vector | (f₀, f₁, …): the numbers of faces of each dimension |
| Schläfli symbol | {p, q, …}: faces are p-gons, q around each vertex, and so on |
| Dual polytope | Vertices and facets exchanged; reverses the Schläfli symbol |
| Cross-polytope | The convex hull of ±eᵢ; the octahedron in three dimensions |
| Dehn invariant | Σ length ⊗ dihedral angle; an obstruction to scissors congruence |

## How it fits

- **Below:** [Convex sets](convex-sets-and-separation.md) supply hulls and supporting hyperplanes; planar graphs and the Euler characteristic give the counting; [group actions](../../05-abstract-algebra/01-groups/group-actions.md) organise the symmetries.
- **Above:** Linear programming optimises over polytopes, and computational geometry builds convex hulls.
- **Siblings:** [Lattices and sphere packing](lattices-and-sphere-packing.md) uses Voronoi cells, which are polytopes; [Gauss–Bonnet](../02-differential-geometry/the-gauss-bonnet-theorem.md) is the smooth version of Descartes's angle-defect count.

## Common misconceptions

- **"Euler's formula holds for every polyhedron"**: Only for those with sphere-like surfaces; a polyhedral torus has V − E + F = 0.
- **"Each dimension has more regular polytopes than the last"**: The count goes 5, 6, then 3 forever.
- **"Equal volumes can always be dissected into each other"**: True for polygons, false for polyhedra, by the Dehn invariant.

## Go deeper

- Coxeter, *Regular Polytopes* (1948): the classic on regular figures in every dimension.
- Ziegler, *Lectures on Polytopes* (1995): the modern combinatorial theory.
- Lakatos, *Proofs and Refutations* (1976): Euler's formula as a case study in how mathematics develops.
