# Cohomology and Poincaré Duality

> **Layer:** [07 Topology](../README.md) › [Algebraic Topology](README.md)
> **Builds on:** [Homology](homology.md), [The Euler Characteristic](the-euler-characteristic.md), [Dual Spaces](../../04-linear-algebra/01-vector-spaces-and-linear-maps/dual-spaces.md), [Topological and Smooth Manifolds](../03-manifolds/topological-and-smooth-manifolds.md)
> **Enables:** [Differential Forms and de Rham Cohomology](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md), [Vector Bundles, Connections and Characteristic Classes](../../08-geometry/02-differential-geometry/vector-bundles-connections-and-characteristic-classes.md), [Homological Algebra](../../13-structure-and-metamathematics/01-category-theory/homological-algebra.md), [Algebraic Curves and Riemann–Roch](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/algebraic-curves-and-riemann-roch.md)

## Essence

Cohomology is homology seen through its [dual](../../04-linear-algebra/01-vector-spaces-and-linear-maps/dual-spaces.md): instead of chains, one studies functions on chains, and every arrow reverses. The groups carry the same information as homology, but they gain a product, the cup product, which makes cohomology a ring and distinguishes spaces that homology cannot. On a closed orientable manifold, Poincaré duality identifies cohomology in degree k with homology in the complementary degree n − k, so the Betti numbers read the same forwards and backwards. The cup product then becomes intersection of submanifolds, and in dimension 4 this intersection form nearly classifies the manifold.

## Core tenets

1. **Cochains are functions on chains, and the coboundary is the dual of ∂.** For an abelian group G, an n-cochain assigns an element of G to each singular n-simplex, and the coboundary δ is defined by (δφ)(c) = φ(∂c). Since ∂∂ = 0, also δδ = 0, and the cohomology Hⁿ(X; G) is the kernel of δ modulo its image. A map f: X → Y pulls cochains back, giving f*: Hⁿ(Y) → Hⁿ(X), in the opposite direction to [homology](homology.md), just as a linear map induces a transpose on dual spaces.

2. **The universal coefficient theorem: cohomology is determined by homology, with torsion shifted up.** Hⁿ(X; ℤ) ≅ Hom(Hₙ(X), ℤ) ⊕ Ext(Hₙ₋₁(X), ℤ), where, for finitely generated groups, the Ext term is the torsion of Hₙ₋₁. Over a field, Hⁿ is simply the dual vector space of Hₙ. For the projective plane ℝP², H₁ = ℤ/2 and H₂ = 0, while H¹(ℝP²; ℤ) = 0 and H²(ℝP²; ℤ) = ℤ/2: the torsion has moved up one degree. So the groups alone add nothing new; the product does.

3. **The cup product makes cohomology a ring, and the ring sees more than the groups.** For cochains α of degree p and β of degree q, α ⌣ β evaluates α on the front p-face of a simplex and β on its back q-face, then multiplies. This descends to cohomology, is natural under pullback and is graded commutative: α ⌣ β = (−1)^(pq) β ⌣ α. The torus and the wedge S² ∨ S¹ ∨ S¹, a sphere and two circles joined at a point, have the same homology, ℤ, ℤ² and ℤ. In the torus the product of the two degree-1 generators generates H²; in the wedge every such product is 0, because each generator lives on a separate piece. So they are not homotopy equivalent.

4. **Ring structure proves theorems that groups cannot.** The cohomology of complex projective space ℂPⁿ is ℤ[x]/(xⁿ⁺¹) with x in degree 2, which separates ℂP² from S² ∨ S⁴ although their groups agree. With ℤ/2 coefficients, ℝPⁿ has ring (ℤ/2)[x]/(xⁿ⁺¹) with x in degree 1, and comparing rings under a would-be map gives a proof of the Borsuk–Ulam theorem of [fixed-point theorems](fixed-point-theorems.md). Cup products also define the Hopf invariant of a map S³ → S², detecting the generator of π₃(S²) in [higher homotopy groups](higher-homotopy-groups-and-fibrations.md).

5. **Poincaré duality: on a closed orientable n-manifold, Hᵏ(M) ≅ Hₙ₋ₖ(M).** Let M be a compact [manifold](../03-manifolds/topological-and-smooth-manifolds.md) without boundary, orientable, so that it has a fundamental class [M] generating Hₙ(M; ℤ). Capping with [M] is an isomorphism from Hᵏ(M) to Hₙ₋ₖ(M). Poincaré stated it in 1895, and the idea behind his proofs is the dual cell decomposition: each k-cell of a triangulation crosses exactly one dual (n − k)-cell. The modern proof checks the statement on coordinate charts and glues by induction with the Mayer–Vietoris sequence. Both hypotheses matter: ℝⁿ is not compact and has H⁰ = ℤ but Hₙ = 0, and ℝP² is not orientable and has H⁰ = ℤ but H₂ = 0. With ℤ/2 coefficients orientation is not needed.

6. **Duality gives symmetric Betti numbers and kills χ in odd dimensions.** Combined with the universal coefficient theorem over a field, duality gives bₖ = bₙ₋ₖ. When n is odd, the terms (−1)ᵏbₖ and (−1)ⁿ⁻ᵏbₙ₋ₖ cancel in pairs, so a closed odd-dimensional manifold has [Euler characteristic](the-euler-characteristic.md) 0. (For non-orientable ones, use ℤ/2 coefficients.)

7. **Cup product is intersection, and in dimension 4 the intersection form is a classifying invariant.** If classes α and β are dual to oriented submanifolds A and B meeting transversally, α ⌣ β is dual to A ∩ B, so on a closed oriented 4-manifold the pairing of two degree-2 classes counts the signed intersection points of two surfaces. Duality makes this symmetric integer form unimodular, with determinant ±1. Freedman (1982) showed it classifies simply connected closed topological 4-manifolds, up to one extra ℤ/2 invariant, while Donaldson (1983), using gauge theory, showed that a smooth one with definite form must have a diagonalisable form. The unimodular E₈ form is therefore realised by a topological 4-manifold with no smooth structure.

## Key concepts

| Term | Meaning |
|---|---|
| Cochain | A function from n-chains to a coefficient group G |
| Coboundary δ | The dual of ∂, with δδ = 0 |
| Contravariance | Maps X → Y induce maps Hⁿ(Y) → Hⁿ(X) |
| Universal coefficient theorem | Cohomology from homology: the dual of Hₙ plus the torsion of Hₙ₋₁ |
| Cup product | The product Hᵖ × H^q → H^(p+q) that makes cohomology a graded ring |
| Fundamental class | The generator [M] of Hₙ(M; ℤ) for a closed oriented n-manifold |
| Cap product | The pairing of a cohomology class with a homology class, used in duality |
| Intersection form | The cup-product pairing on the middle cohomology of a closed oriented 4k-manifold |

## How it fits

- **Below:** [Homology](homology.md) supplies chains and ∂; [dual spaces](../../04-linear-algebra/01-vector-spaces-and-linear-maps/dual-spaces.md) model the reversal of arrows; [manifolds](../03-manifolds/topological-and-smooth-manifolds.md) are where duality holds.
- **Above:** [De Rham's theorem](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md) identifies real cohomology with forms, cup with wedge product; [characteristic classes](../../08-geometry/02-differential-geometry/vector-bundles-connections-and-characteristic-classes.md) are cohomology classes of bundles; Ext and derived functors belong to [homological algebra](../../13-structure-and-metamathematics/01-category-theory/homological-algebra.md); Serre duality behind [Riemann–Roch](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/algebraic-curves-and-riemann-roch.md) is its algebraic cousin.
- **Siblings:** [Higher homotopy groups](higher-homotopy-groups-and-fibrations.md) represent cohomology by Eilenberg–MacLane spaces; [the Euler characteristic](the-euler-characteristic.md) is an alternating sum of the same ranks.

## Common misconceptions

- **"Cohomology is homology with the arrows reversed."**: The groups follow from homology, but the cup product is new structure; it separates the torus from S² ∨ S¹ ∨ S¹.
- **"Hⁿ is always the dual of Hₙ."**: Only over a field; over ℤ torsion moves up one degree, as for ℝP².
- **"Poincaré duality holds on every manifold."**: It needs compactness without boundary and, over ℤ, orientability; ℝⁿ and ℝP² fail it.

## Go deeper

- Allen Hatcher, *Algebraic Topology* (2002): chapter 3 develops cup products and proves Poincaré duality.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (1982): duality and the intersection pairing through forms.
- Glen E. Bredon, *Topology and Geometry* (1993): a thorough account linking singular, de Rham and Čech cohomology.
