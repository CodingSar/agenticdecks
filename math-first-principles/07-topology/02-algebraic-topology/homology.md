# Homology

> **Layer:** [07 Topology](../README.md) › [Algebraic Topology](README.md)
> **Builds on:** [Homotopy and the Fundamental Group](homotopy-and-the-fundamental-group.md), [Subspaces, Products and Quotients](../01-point-set-topology/subspaces-products-and-quotients.md), [Homomorphisms and Quotient Groups](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md), [Linear Systems and Rank–Nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md)
> **Enables:** [The Euler Characteristic](the-euler-characteristic.md), [Fixed-Point Theorems](fixed-point-theorems.md), [Homological Algebra](../../13-structure-and-metamathematics/01-category-theory/homological-algebra.md), [Differential Forms and de Rham Cohomology](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md)

## Essence

Homology counts holes of each dimension by linear algebra. A space is broken into simplices (points, edges, triangles, tetrahedra and their higher analogues); formal sums of n-simplices are n-chains, and the boundary map ∂ sends each simplex to the signed sum of its faces. The boundary of a boundary is zero, ∂∂ = 0, so every boundary is a cycle, and the homology group Hₙ, cycles modulo boundaries, measures the n-dimensional cycles that bound nothing. Homology forgets the non-commutativity that π₁ keeps, but it is computable in every dimension, and because continuous maps induce homomorphisms it proves impossibility theorems, starting from the homology of spheres.

## Core tenets

1. **Boundaries have no boundary: ∂∂ = 0.** For an oriented simplex [v₀, …, vₙ], where v̂ᵢ marks an omitted vertex,

   ```
   ∂[v₀, …, vₙ] = ∑ᵢ (−1)ⁱ · [v₀, …, v̂ᵢ, …, vₙ]
   ```

   Applying ∂ twice, the face missing vᵢ and vⱼ (i < j) appears twice: removing vⱼ then vᵢ gives sign (−1)ʲ(−1)ⁱ, and removing vᵢ then vⱼ, which has moved to position j − 1, gives (−1)ⁱ(−1)ʲ⁻¹. The two cancel. For a triangle, ∂[a, b, c] = [b, c] − [a, c] + [a, b] is a closed loop, and its boundary is (c − b) − (c − a) + (b − a) = 0.

2. **Homology is cycles modulo boundaries.** An n-cycle is a chain with ∂c = 0 and an n-boundary is a chain ∂d; since ∂∂ = 0, boundaries are cycles, and Hₙ(X) = ker ∂ₙ / im ∂ₙ₊₁. A loop round a hole survives in the quotient, while a loop bounding a filled region dies. H₀ is free abelian on the path components. For path-connected X, H₁ is the abelianisation of π₁ (the Hurewicz theorem), so the figure-eight has H₁ ≅ ℤ² although its π₁ is free on two generators. Singular homology, built from all continuous maps of simplices into X, needs no triangulation and agrees with every triangulation.

3. **Homology is a functor and a homotopy invariant.** A continuous f: X → Y induces f_*: Hₙ(X) → Hₙ(Y), with (g∘f)_* = g_*∘f_* and id_* = id, and homotopic maps induce the same homomorphism. So homotopy-equivalent spaces have isomorphic homology. This is what turns a computation into an impossibility proof: a hypothetical construction would produce a homomorphism of groups that cannot exist.

4. **The Mayer–Vietoris sequence computes homology by cutting.** If X is the union of the interiors of A and B, there is a long exact sequence, in which the image of each map is the kernel of the next:

   ```
   … → Hₙ(A ∩ B) → Hₙ(A) ⊕ Hₙ(B) → Hₙ(X) → Hₙ₋₁(A ∩ B) → …
   ```

   The proof subdivides every cycle into small pieces lying in A or in B, as van Kampen's theorem does for loops; the map Hₙ(X) → Hₙ₋₁(A ∩ B) takes the boundary of a cycle's part in A. Exactness lets known groups force unknown ones.

5. **Spheres: for n ≥ 1, Hₖ(Sⁿ) ≅ ℤ when k = 0 or k = n, and Hₖ(Sⁿ) = 0 otherwise.** Cover Sⁿ by two open caps, each contractible, overlapping in a band homotopy equivalent to Sⁿ⁻¹. Mayer–Vietoris gives Hₖ(Sⁿ) ≅ Hₖ₋₁(Sⁿ⁻¹) for k ≥ 2, with a small correction in degrees 0 and 1, and induction from S⁰, two points, finishes. For n ≥ 2 no retraction of the disc Dⁿ onto Sⁿ⁻¹ exists, since the identity of Hₙ₋₁(Sⁿ⁻¹) ≅ ℤ would factor through Hₙ₋₁(Dⁿ) = 0. And ℝⁿ is not homeomorphic to ℝᵐ for n ≠ m, since removing a point leaves spaces homotopy equivalent to Sⁿ⁻¹ and Sᵐ⁻¹.

6. **Degree measures how a map wraps a sphere round itself.** A map f: Sⁿ → Sⁿ acts on Hₙ(Sⁿ) ≅ ℤ as multiplication by an integer, its degree. A reflection has degree −1, so the antipodal map x ↦ −x, a composite of n + 1 reflections, has degree (−1)ⁿ⁺¹. If Sⁿ carried a nowhere-zero tangent vector field v, turning each x through a half-turn in the direction of v(x) would be a homotopy from the identity to the antipodal map. For even n their degrees are 1 and −1, so every continuous tangent vector field on S² vanishes somewhere: the hairy ball theorem.

7. **Over a field homology is linear algebra, and torsion is what a field can hide.** With coefficients in a field, chains form vector spaces, ∂ is a matrix, and dim Hₙ = dim ker ∂ₙ − rank ∂ₙ₊₁ by rank–nullity; the dimensions over ℚ are the Betti numbers bₙ. Integer homology can also have torsion: H₁(ℝP²) ≅ ℤ/2, because the loop once round ℝP² is not a boundary but twice it is. Rational coefficients erase this torsion, and coefficients in ℤ/2 detect it.

## Key concepts

| Term | Meaning |
|---|---|
| n-simplex | The convex hull of n + 1 points in general position: point, edge, triangle, tetrahedron |
| Chain | A formal integer combination of oriented simplices |
| Cycle, boundary | A chain c with ∂c = 0; a chain of the form ∂d |
| Hₙ(X) | The n-th homology group, ker ∂ₙ / im ∂ₙ₊₁ |
| Betti number bₙ | The dimension of Hₙ with rational coefficients: the number of independent n-dimensional holes |
| Torsion | Elements of finite order in integer homology, invisible over ℚ |
| Exact sequence | A sequence of homomorphisms in which the image of each is the kernel of the next |
| Degree | The integer by which f: Sⁿ → Sⁿ multiplies Hₙ(Sⁿ) ≅ ℤ |

## How it fits

- **Below:** Homology is [quotient groups](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md) applied to chains and, over a field, [rank–nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md); spaces are built by [gluing](../01-point-set-topology/subspaces-products-and-quotients.md); H₁ is the abelian shadow of [π₁](homotopy-and-the-fundamental-group.md).
- **Above:** Chain complexes, exact sequences and derived functors in general are [homological algebra](../../13-structure-and-metamathematics/01-category-theory/homological-algebra.md) in 13. De Rham's theorem in 08 says that the cohomology of a smooth manifold built from [differential forms](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md) equals its singular [cohomology](cohomology-and-poincare-duality.md) with real coefficients, the dual of homology: ∂∂ = 0 matches dd = 0, and Stokes's theorem pairs them.
- **Siblings:** [The Euler characteristic](the-euler-characteristic.md) is the alternating sum of the Betti numbers; [fixed-point theorems](fixed-point-theorems.md) use the no-retraction theorem and traces on homology; [covering spaces](covering-spaces.md) keep the non-abelian information that homology loses; the Hurewicz theorem matches homology with the first non-zero [higher homotopy group](higher-homotopy-groups-and-fibrations.md).

## Common misconceptions

- **"Homology depends on the triangulation."**: Singular homology is defined from all continuous maps of simplices and is a homotopy invariant; every triangulation computes the same groups.
- **"Homology and homotopy groups see the same holes."**: The Poincaré homology sphere has the homology of S³ but a non-trivial π₁, and πₙ(S²) is non-zero for infinitely many n, while Hₙ(S²) = 0 for all n > 2.

## Go deeper

- Allen Hatcher, *Algebraic Topology* (2002): chapter 2 develops singular homology, Mayer–Vietoris and degree with many examples.
- James Munkres, *Elements of Algebraic Topology* (1984): simplicial homology built carefully, with the algebra in full.
