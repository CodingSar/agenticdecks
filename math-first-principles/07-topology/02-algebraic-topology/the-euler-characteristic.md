# The Euler Characteristic

> **Layer:** [07 Topology](../README.md) › [Algebraic Topology](README.md)
> **Builds on:** [Homology](homology.md), [Colouring and Planarity](../../03-combinatorics-and-graph-theory/02-graph-theory/colouring-and-planarity.md), [Linear Systems and Rank–Nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md)
> **Enables:** [Classification of Surfaces](../03-manifolds/classification-of-surfaces.md), [The Gauss–Bonnet Theorem](../../08-geometry/02-differential-geometry/the-gauss-bonnet-theorem.md), [Polytopes](../../08-geometry/03-convex-and-discrete-geometry/polytopes.md), [Geometry and Transformations (CS)](../../../cs-first-principles/14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md)

## Essence

For any convex polyhedron, vertices minus edges plus faces equals 2: a cube has 8 − 12 + 6 = 2, a tetrahedron 4 − 6 + 4 = 2. Euler noticed this; topology explains it. The alternating count χ = V − E + F, and its higher-dimensional version with cells of every dimension, does not depend on how a space is cut into pieces, because it equals the alternating sum of the Betti numbers, which are homology invariants. It is the simplest topological invariant that is a number, and it reaches surprisingly far: it classifies closed surfaces together with orientability, it equals the total curvature of a surface divided by 2π, and it counts the zeros of vector fields and the fixed points of maps.

## Core tenets

1. **χ is the alternating count of cells.** For a space cut into finitely many cells, with cₙ cells of dimension n, define χ = c₀ − c₁ + c₂ − … . For a polyhedral surface this is V − E + F. Examples: the sphere S² has χ = 2 (a tetrahedron, or one vertex plus one 2-cell), the torus 0 (a square with sides glued gives 1 vertex, 2 edges, 1 face), the projective plane ℝP² 1, the Klein bottle 0.

2. **χ is a topological invariant, because it equals the alternating sum of Betti numbers.** Over ℚ, let Zₙ be the n-cycles and Bₙ the n-boundaries. Rank–nullity applied to each boundary map gives cₙ = dim Zₙ + dim Bₙ₋₁, and bₙ = dim Zₙ − dim Bₙ. In the alternating sum the boundary terms telescope away:

   ```
   ∑ₙ (−1)ⁿ cₙ = ∑ₙ (−1)ⁿ (dim Zₙ + dim Bₙ₋₁) = ∑ₙ (−1)ⁿ (dim Zₙ − dim Bₙ) = ∑ₙ (−1)ⁿ bₙ
   ```

   The left side depends on the cutting, the right side only on the space, so every decomposition gives the same number. Before homology, proofs of "V − E + F = 2" were notoriously leaky: polyhedra with tunnels or hollow insides break the formula, a story told by Lakatos.

3. **For surfaces, χ records the genus.** The closed orientable surface of genus g (a sphere with g handles) has b₀ = 1, b₁ = 2g, b₂ = 1, so χ = 2 − 2g. The connected sum of k projective planes has χ = 2 − k. Each handle costs 2 and each cross-cap 1, because forming a connected sum removes a disc from each piece (χ drops by 1 each) and glues along a circle (χ = 0): χ(M # N) = χ(M) + χ(N) − 2. With orientability, χ classifies closed surfaces completely ([classification of surfaces](../03-manifolds/classification-of-surfaces.md)).

4. **χ behaves like a size: it adds, multiplies and scales under covers.** For subspaces built of cells, χ(A ∪ B) = χ(A) + χ(B) − χ(A ∩ B), the inclusion–exclusion principle of counting. For products, χ(X × Y) = χ(X)·χ(Y), so the torus S¹ × S¹ has χ = 0·0. For an n-sheeted cover E → X, each cell of X lifts to n cells, so χ(E) = n·χ(X). This gives quick impossibility proofs: S² (χ = 2) cannot cover any surface except itself and ℝP², since 2 = n·χ(X) forces n ≤ 2.

5. **Euler's formula constrains every planar picture.** A connected planar graph drawn without crossings divides the plane, with the outside counted as a face, so that V − E + F = 2. Since each face has at least three edges and each edge borders two faces, E ≤ 3V − 6, so the complete graph on five vertices is not planar. The same count shows that a convex polyhedron whose faces are all p-gons meeting q at each vertex must satisfy 1/p + 1/q > 1/2, which leaves exactly five regular solids.

6. **χ is total curvature and counts zeros and fixed points.** The Gauss–Bonnet theorem says that for a closed surface with Gaussian curvature K, ∫ K dA = 2π·χ: no metric on the torus can be positively curved everywhere ([the Gauss–Bonnet theorem](../../08-geometry/02-differential-geometry/the-gauss-bonnet-theorem.md)). The Poincaré–Hopf theorem says that the indices of the zeros of a vector field with isolated zeros on a closed manifold sum to χ, which explains the hairy ball theorem (χ(S²) = 2 ≠ 0). And χ is the Lefschetz number of the identity map, linking it to [fixed-point theorems](fixed-point-theorems.md).

7. **χ is a weak invariant, and odd-dimensional closed manifolds hide it.** Every closed odd-dimensional manifold has χ = 0 (a consequence of [Poincaré duality](cohomology-and-poincare-duality.md)), so χ says nothing about 3-manifolds. Spaces with the same χ can differ: the torus and the Klein bottle both have χ = 0, and so does the circle S¹. χ is the first shadow of homology, not a replacement for it.

## Key concepts

| Term | Meaning |
|---|---|
| Euler characteristic χ | The alternating sum c₀ − c₁ + c₂ − … of cell counts, equal to ∑ (−1)ⁿ bₙ |
| Betti number bₙ | The dimension of the n-th homology group over ℚ |
| Genus g | The number of handles of a closed orientable surface |
| Connected sum M # N | Remove a disc from each surface and glue along the boundary circles |
| Index of a zero | The degree of the vector field's direction on a small circle round the zero |
| Gauss–Bonnet theorem | The integral of Gaussian curvature over a closed surface equals 2π·χ |

## How it fits

- **Below:** Euler's formula for [planar graphs](../../03-combinatorics-and-graph-theory/02-graph-theory/colouring-and-planarity.md) is the combinatorial seed; [rank–nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md) and [homology](homology.md) prove its invariance.
- **Above:** [Gauss–Bonnet](../../08-geometry/02-differential-geometry/the-gauss-bonnet-theorem.md) turns χ into curvature; [polytopes](../../08-geometry/03-convex-and-discrete-geometry/polytopes.md) generalise the face counts to higher dimensions; triangle meshes in [computer graphics](../../../cs-first-principles/14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md) use V − E + F to check that a mesh is a closed surface of the expected genus.
- **Siblings:** χ is the numerical summary of [homology](homology.md); it multiplies under [covering spaces](covering-spaces.md); as the Lefschetz number of the identity it ties to [fixed-point theorems](fixed-point-theorems.md).

## Common misconceptions

- **"V − E + F = 2 for every polyhedron."**: Only for those whose surface is a sphere. A picture frame (a polyhedral torus) has V − E + F = 0.
- **"Two surfaces with the same χ are the same."**: The torus and the Klein bottle both have χ = 0; orientability must be added to classify.

## Go deeper

- Imre Lakatos, *Proofs and Refutations* (1976): the history of Euler's formula as a study of how proofs and definitions evolve.
- David Richeson, *Euler's Gem* (2008): a gentle book-length account of the formula and its descendants.
- Allen Hatcher, *Algebraic Topology* (2002): χ through cell complexes and homology.
