# Homological Algebra

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Category theory](README.md)
> **Builds on:** [Modules](../../05-abstract-algebra/04-modules-and-representations/modules.md), [Linear systems and rank–nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md), [Homology](../../07-topology/02-algebraic-topology/homology.md), [Differential forms and de Rham cohomology](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md), [Universal properties and adjunctions](universal-properties-and-adjunctions.md)
> **Enables:** [Higher categories and homotopy type theory](higher-categories-and-homotopy-type-theory.md)

## Essence

Simplicial homology of a space and de Rham cohomology of a manifold both come from a sequence of abelian groups with maps whose composite is zero, and both measure how far "boundary" falls short of "cycle". Homological algebra studies such chain complexes for their own sake, in any category where kernels and cokernels behave like those of modules. Its central tools are exact sequences, the snake lemma that turns a short exact sequence of complexes into a long exact sequence, and derived functors such as Tor and Ext that measure exactly how far tensor product and Hom fail to preserve exactness.

## Core tenets

1. **A chain complex is a sequence of maps with ∂∘∂ = 0, and homology measures its failure to be exact.** A complex is a sequence of modules Cₙ with maps ∂ₙ: Cₙ → Cₙ₋₁ satisfying ∂ₙ∘∂ₙ₊₁ = 0, so every boundary is a cycle. Its homology is Hₙ = ker ∂ₙ / im ∂ₙ₊₁. Simplicial chains, with ∂ the alternating sum of faces, give the [homology](../../07-topology/02-algebraic-topology/homology.md) of a space, and differential forms, with d∘d = 0, give de Rham cohomology.

2. **Short exact sequences need not split.** A sequence 0 → A → B → C → 0 is exact when the image of each map is the kernel of the next. The sequence 0 → ℤ → ℤ → ℤ/2 → 0, whose first map is multiplication by 2, is exact, but B = ℤ is not A ⊕ C, since ℤ has no element of order 2. Over a field every short exact sequence splits, which is why rank–nullity is enough for linear algebra and homological algebra begins with modules.

3. **The snake lemma connects kernels and cokernels.** Given a map between two short exact sequences, as below, there is an exact sequence of six terms, whose connecting map δ is found by chasing an element through the diagram. Applied to a short exact sequence of complexes, it gives the long exact sequence in homology, of which the Mayer–Vietoris sequence is a case.

   ```
        0 → A  →  B  →  C  → 0
            ↓f    ↓g    ↓h
        0 → A' →  B' →  C' → 0

   ker f → ker g → ker h ─δ→ coker f → coker g → coker h
   ```

4. **Tensor product is right exact but not exact, and Tor measures the defect.** Tensoring 0 → ℤ → ℤ → ℤ/2 → 0 with ℤ/2 gives ℤ/2 → ℤ/2 → ℤ/2 → 0, whose first map is zero, so injectivity is lost. To repair this, resolve a module A by free modules, … → F₁ → F₀ → A → 0, tensor with B, and take homology: the result is Torₙ(A, B), independent of the resolution because any two are homotopy equivalent. Here Tor₁(ℤ/n, B) is the n-torsion of B.

5. **Ext classifies extensions.** Applying Hom(−, B) to a projective resolution of A and taking cohomology gives Extⁿ(A, B); from 0 → ℤ → ℤ → ℤ/n → 0 one gets Ext¹(ℤ/n, B) ≅ B/nB. The name is literal: Ext¹(A, B) classifies short exact sequences 0 → B → E → A → 0 up to equivalence, with zero for the split one. Ext¹(ℤ/2, ℤ) ≅ ℤ/2 has two elements, the split sequence and the one in tenet 2.

6. **Universal coefficient theorems compute other coefficients from integral homology.** For a space X, Hₙ(X; G) ≅ (Hₙ(X) ⊗ G) ⊕ Tor₁(Hₙ₋₁(X), G), and dually Hⁿ(X; G) ≅ Hom(Hₙ(X), G) ⊕ Ext¹(Hₙ₋₁(X), G). For the real projective plane, with H₁ = ℤ/2 and H₂ = 0, these give H₂(ℝP²; ℤ/2) ≅ ℤ/2 and H²(ℝP²; ℤ) ≅ ℤ/2, both coming entirely from torsion. The splittings exist but are not natural.

7. **Abelian categories make the method portable.** Grothendieck's Tôhoku paper (1957) isolated the axioms on kernels and cokernels that the arguments need, and showed that sheaves of abelian groups satisfy them with enough injective objects, so sheaf cohomology is a derived functor. Group cohomology is Hⁿ(G, M) = Extⁿ over ℤ[G] of (ℤ, M). Derived categories, from Grothendieck and his student Jean-Louis Verdier in the 1960s, keep the whole complex instead of only its homology.

## Key concepts

| Term | Meaning |
|---|---|
| Chain complex | Modules Cₙ with maps ∂ satisfying ∂∘∂ = 0 |
| Homology Hₙ | Cycles modulo boundaries, ker ∂ₙ / im ∂ₙ₊₁ |
| Exact sequence | A sequence in which each image equals the next kernel |
| Split | A short exact sequence with B ≅ A ⊕ C compatibly |
| Projective, injective resolution | An exact complex of projective, injective modules ending at a given module |
| Derived functor | The homology of a functor applied to a resolution |
| Tor, Ext | The derived functors of ⊗ and Hom |
| Abelian category | A category whose kernels and cokernels behave as for modules |

## How it fits

- **Below:** It abstracts the boundary maps of [homology](../../07-topology/02-algebraic-topology/homology.md) and the exterior derivative of [de Rham cohomology](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md), and replaces the vector spaces of [rank–nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md) by [modules](../../05-abstract-algebra/04-modules-and-representations/modules.md), where sequences stop splitting.
- **Above:** Sheaf cohomology in algebraic geometry and group cohomology in number theory are its derived functors.
- **Siblings:** [Adjunctions](universal-properties-and-adjunctions.md) explain why ⊗ is right exact, and [higher categories](higher-categories-and-homotopy-type-theory.md) supply stable ∞-categories, a better home for derived categories.

## Common misconceptions

- **"Free resolutions are infinite or arbitrary, so Tor and Ext depend on choices."**: Any two resolutions are chain homotopy equivalent, so the derived functors are well defined; and by Hilbert's syzygy theorem (1890) a finitely generated module over a polynomial ring in n variables over a field has a free resolution of length at most n.
- **"Homology determines a space."**: The Poincaré homology sphere has the homology of the 3-sphere but a fundamental group of order 120, so it is not homeomorphic to it.

## Go deeper

- Charles Weibel, *An Introduction to Homological Algebra* (1994): the standard modern text.
- Henri Cartan and Samuel Eilenberg, *Homological Algebra* (1956): the book that founded the subject.
- Allen Hatcher, *Algebraic Topology* (2002): homology and the universal coefficient theorems with full topological motivation.
