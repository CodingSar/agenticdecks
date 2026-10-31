# Classification of Surfaces

> **Layer:** [07 Topology](../README.md) › [Manifolds](README.md)
> **Builds on:** [Topological and Smooth Manifolds](topological-and-smooth-manifolds.md), [The Euler Characteristic](../02-algebraic-topology/the-euler-characteristic.md), [Homotopy and the Fundamental Group](../02-algebraic-topology/homotopy-and-the-fundamental-group.md), [Subspaces, Products and Quotients](../01-point-set-topology/subspaces-products-and-quotients.md), [Free Groups and Presentations](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md)
> **Enables:** [Three-Manifolds and the Poincaré Conjecture](three-manifolds-and-the-poincare-conjecture.md), [The Gauss–Bonnet Theorem](../../08-geometry/02-differential-geometry/the-gauss-bonnet-theorem.md), [Analytic Continuation and Riemann Surfaces](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md), [Algebraic Curves and Riemann–Roch](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/algebraic-curves-and-riemann-roch.md)

## Essence

Classification is the dream of every area of mathematics: a complete list of the objects, and a way to tell which one you are holding. For closed surfaces the dream comes true. Every compact connected surface without boundary is homeomorphic to exactly one of these: the sphere; a sphere with g handles (a connected sum of g tori); or a sphere with k cross-caps (a connected sum of k projective planes). Two numbers decide which: whether the surface is orientable, and its Euler characteristic. The proof cuts the surface into triangles, unfolds it into a polygon with edges glued in pairs, and simplifies the gluing pattern by algebra on words. Nothing comparable is possible in dimension 4 and above, which makes this theorem the high-water mark of complete classification in topology.

## Core tenets

1. **The list is complete and has no repetitions.** Write Σ_g for the connected sum of g tori (Σ₀ = S²) and N_k for the connected sum of k projective planes ℝP². Every closed connected surface is homeomorphic to exactly one Σ_g (g ≥ 0) or N_k (k ≥ 1). The Klein bottle is N₂. The hypotheses matter: without compactness, the plane, the open annulus and surfaces with infinitely many handles appear, and their classification needs extra invariants describing how they run off to infinity.

2. **Orientability and χ decide.** A surface is non-orientable if and only if it contains a Möbius band, along which a small clockwise circle comes back anticlockwise. The Σ_g are orientable with χ = 2 − 2g; the N_k are non-orientable with χ = 2 − k ([Euler characteristic](../02-algebraic-topology/the-euler-characteristic.md)). So χ and orientability together pin down g or k. Neither alone suffices: the torus and the Klein bottle share χ = 0, and S² and Σ₁ are both orientable.

3. **Step one: triangulate.** Every compact surface can be cut into finitely many triangles meeting edge to edge (Radó's theorem). This is the hard analytic input; it uses the Jordan curve theorem and its relatives in the plane. Smooth surfaces can be triangulated more easily. After triangulation the problem becomes combinatorial.

4. **Step two: unfold into a polygon with a word.** Glue the triangles one at a time along shared edges, keeping the result a disc. What remains is a single polygon whose edges are identified in pairs, recorded by reading the edge labels round the boundary, with a⁻¹ for an edge traversed against its arrow. The standard forms are:

   ```
   S²        a a⁻¹
   torus     a b a⁻¹ b⁻¹
   ℝP²       a a
   Klein     a b a b⁻¹
   Σ_g       a₁ b₁ a₁⁻¹ b₁⁻¹ ⋯ a_g b_g a_g⁻¹ b_g⁻¹
   N_k       a₁ a₁ a₂ a₂ ⋯ a_k a_k
   ```

5. **Step three: normalise by cutting and regluing.** Adjacent pairs a a⁻¹ fold away. A pair appearing twice in the same direction (a … a) can be cut and reglued until it is adjacent, giving a cross-cap a a. Two interlocking pairs (a … b … a⁻¹ … b⁻¹) can be gathered into a handle a b a⁻¹ b⁻¹. One further move closes the argument: a torus plus a projective plane equals three projective planes, T # ℝP² ≅ N₃, so a mixture of handles and cross-caps reduces to cross-caps alone. Each move is a homeomorphism, so the surface never changes, only its description.

6. **The invariants prove that the list has no repeats.** The polygon is a cell structure with one face, so the [fundamental group](../02-algebraic-topology/homotopy-and-the-fundamental-group.md) has one generator per edge pair and one relation, the word: π₁(Σ_g) = ⟨a₁, b₁, …, a_g, b_g ∣ a₁b₁a₁⁻¹b₁⁻¹ ⋯ a_g b_g a_g⁻¹ b_g⁻¹⟩. Abelianising gives H₁(Σ_g) ≅ ℤ²ᵍ and H₁(N_k) ≅ ℤᵏ⁻¹ ⊕ ℤ/2. These differ for every pair of surfaces on the list, so no two are homeomorphic.

7. **Surfaces with boundary and the geometry of surfaces.** A compact surface with boundary is a closed one with b open discs removed, and χ = 2 − 2g − b in the orientable case. Each closed surface also carries a metric of constant curvature, of the sign of χ: spherical for S² and ℝP², flat for the torus and Klein bottle, hyperbolic for everything else (the uniformisation theorem). The [Gauss–Bonnet theorem](../../08-geometry/02-differential-geometry/the-gauss-bonnet-theorem.md) forces the sign. This geometric picture is the template that Thurston extended to [three-manifolds](three-manifolds-and-the-poincare-conjecture.md).

## Key concepts

| Term | Meaning |
|---|---|
| Closed surface | A compact connected 2-manifold without boundary |
| Connected sum M # N | Remove a disc from each and glue along the boundary circles |
| Genus g | The number of handles of an orientable surface |
| Cross-cap | A Möbius band glued into a hole; adding one is a connected sum with ℝP² |
| Orientable | Containing no Möbius band, so a consistent sense of rotation exists |
| Polygon word | The cyclic list of edge labels describing how a polygon's edges are glued |
| Triangulation | A decomposition into triangles meeting along whole edges or vertices |

## How it fits

- **Below:** the polygon is a [quotient space](../01-point-set-topology/subspaces-products-and-quotients.md); the words are [group presentations](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md); [χ](../02-algebraic-topology/the-euler-characteristic.md) and [π₁](../02-algebraic-topology/homotopy-and-the-fundamental-group.md) are the distinguishing invariants.
- **Above:** compact [Riemann surfaces](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md) are orientable, hence some Σ_g, and the genus g is the topological number in [Riemann–Roch](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/algebraic-curves-and-riemann-roch.md); [Gauss–Bonnet](../../08-geometry/02-differential-geometry/the-gauss-bonnet-theorem.md) links χ to curvature.
- **Siblings:** surfaces are the 2-dimensional [manifolds](topological-and-smooth-manifolds.md); Seifert surfaces bounded by [knots](knot-theory.md) define the knot genus; [three-manifolds](three-manifolds-and-the-poincare-conjecture.md) are often built by gluing along surfaces.

## Common misconceptions

- **"The Klein bottle needs four dimensions, so it is not a real surface."**: It cannot be embedded in ℝ³ without crossing itself, but it is a perfectly good closed surface, N₂. Every closed non-orientable surface fails to embed in ℝ³, yet each embeds in ℝ⁴.
- **"Higher-dimensional manifolds will eventually be classified the same way."**: In dimension 4 and above every finitely presented group is the fundamental group of a closed manifold, and deciding whether two such manifolds are homeomorphic is algorithmically impossible (Markov). Dimension 3 is the frontier, where geometrisation gives a different kind of answer.

## Go deeper

- M. A. Armstrong, *Basic Topology* (1983): a careful proof of the classification by surgery on triangulations.
- John Stillwell, *Classical Topology and Combinatorial Group Theory* (2nd edition, 1993): polygon words and fundamental groups.
- Jeffrey R. Weeks, *The Shape of Space* (1985): what it would be like to live in these surfaces and their 3-dimensional cousins.
