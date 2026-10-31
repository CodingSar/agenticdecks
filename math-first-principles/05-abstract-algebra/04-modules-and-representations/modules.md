# Modules

> **Layer:** [05 Abstract Algebra](../README.md) › [Modules and Representations](README.md)
> **Builds on:** [Rings and Ideals](../02-rings-and-fields/rings-and-ideals.md), [Factorisation in Integral Domains](../02-rings-and-fields/factorisation-in-integral-domains.md), [Jordan Normal Form](../../04-linear-algebra/02-determinants-and-eigenvalues/jordan-normal-form.md), [Linear Systems and Rank–Nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md)
> **Enables:** [Representations of Finite Groups](representations-of-finite-groups.md), [Homological Algebra](../../13-structure-and-metamathematics/01-category-theory/homological-algebra.md), [Homology](../../07-topology/02-algebraic-topology/homology.md), [Lattices and Sphere Packing](../../08-geometry/03-convex-and-discrete-geometry/lattices-and-sphere-packing.md)

## Essence

A module is a vector space whose scalars come from a ring instead of a field. The definition is the same, but the consequences differ: without division, modules need not have bases, and elements can be killed by non-zero scalars. The concept unifies three familiar objects. Abelian groups are exactly the modules over ℤ, ideals are modules over their ring, and a vector space with a chosen linear map T is a module over the polynomial ring F[t], with t acting as T. Over a principal ideal domain (PID) there is one structure theorem for finitely generated modules, and it yields both the classification of finitely generated abelian groups and the Jordan normal form of a matrix.

## Core tenets

1. **A module over R is an abelian group M with a scalar multiplication R × M → M satisfying the vector space axioms.** If R is a field, a module is a vector space. Every abelian group is a ℤ-module in exactly one way, with n·m = m + ⋯ + m. A vector space V with a linear map T becomes an F[t]-module by setting p(t)·v = p(T)v, so studying one linear map is studying one module.

2. **Modules need not be free.** A free module has a basis, like Rⁿ. In ℤ/6 as a ℤ-module, 6·m = 0 for every m, so no non-empty set is linearly independent and there is no basis. Being torsion-free is not enough either: ℚ is torsion-free over ℤ but not free, and not finitely generated. Over ℤ[x], the ideal (2, x) is torsion-free and finitely generated but not free, since any two of its elements a and b satisfy the relation b·a − a·b = 0, and it is not principal.

3. **Over a PID, submodules of free modules are free.** A submodule of Rⁿ is free of rank at most n, by induction on n using that every ideal is principal. This is the hypothesis that makes the classification work, and it fails in the example above: (2, x) is a submodule of the free module ℤ[x] but is not free.

4. **The structure theorem: every finitely generated module over a PID R is a direct sum of cyclic modules.**
   ```
   M ≅ Rʳ ⊕ R/(d₁) ⊕ R/(d₂) ⊕ ⋯ ⊕ R/(dₖ),     d₁ ∣ d₂ ∣ ⋯ ∣ dₖ,  each dᵢ a non-unit
   ```
   The rank r and the invariant factors dᵢ, up to units, are determined by M. Splitting each R/(dᵢ) by the Chinese remainder theorem into pieces R/(pᵉ) gives the equivalent elementary divisor form.

5. **The proof is Smith normal form.** Write M as Rⁿ modulo the submodule spanned by the relations, the rows of a matrix A. Invertible row and column operations, essentially the Euclidean algorithm, reduce A to a diagonal matrix with entries d₁ ∣ d₂ ∣ ⋯. For the abelian group with generators a, b and relations 2a + 4b = 0 and 6a + 6b = 0:
   ```
   [2 4]   subtract 3 × row 1   [2  4]   subtract 2 × column 1   [2  0]
   [6 6]   ───────────────────> [0 −6]   ─────────────────────>  [0 −6]
   ```
   so the group is ℤ/2 ⊕ ℤ/6.

6. **With R = ℤ: every finitely generated abelian group is ℤʳ ⊕ ℤ/d₁ ⊕ ⋯ ⊕ ℤ/dₖ.** The abelian groups of order 72 = 2³ · 3² correspond to a partition of 3 for the 2-part and of 2 for the 3-part, so there are 3 × 2 = 6:
   ```
   ℤ/72          ℤ/2 ⊕ ℤ/36       ℤ/2 ⊕ ℤ/2 ⊕ ℤ/18
   ℤ/3 ⊕ ℤ/24    ℤ/6 ⊕ ℤ/12       ℤ/2 ⊕ ℤ/6 ⊕ ℤ/6
   ```
   Finiteness is essential: ℚ and the infinite product ℤ × ℤ × ⋯ are not of this form.

7. **With R = F[t]: canonical forms for matrices.** A linear map T on a finite-dimensional space makes V a finitely generated torsion F[t]-module, so V ≅ ⊕ F[t]/(dᵢ). Each summand F[t]/(d) is spanned by v, Tv, T²v, …, on which T acts by the companion matrix of d: this is the rational canonical form, valid over any field. The largest invariant factor dₖ is the minimal polynomial, and the product of all of them is the characteristic polynomial, which gives the Cayley–Hamilton theorem. When the characteristic polynomial splits, the elementary divisors (t − λ)ᵉ give the Jordan blocks. Two matrices are similar if and only if their modules are isomorphic.

8. **Beyond PIDs, modules measure how far rings are from fields.** Over general rings, finitely generated modules have no simple classification. Projective modules, the direct summands of free ones, generalise free modules; homological algebra measures how far a module is from projective by resolving it with free modules. Over a PID every submodule of a free module is free, so such resolutions stop after one step.

## Key concepts

| Term | Meaning |
|---|---|
| R-module | An abelian group with an action of the ring R by scalars |
| Free module | A module with a basis, isomorphic to a direct sum of copies of R |
| Torsion element | An m with r·m = 0 for some non-zero r |
| Cyclic module | One generated by a single element, isomorphic to R/I |
| Invariant factors | The d₁ ∣ d₂ ∣ ⋯ ∣ dₖ in the structure theorem |
| Elementary divisors | The prime powers pᵉ obtained by splitting the invariant factors |
| Smith normal form | The diagonal form of a matrix over a PID under invertible row and column operations |
| Rational canonical form | The block matrix of companion matrices given by the invariant factors |

## How it fits

- **Below:** [rings and ideals](../02-rings-and-fields/rings-and-ideals.md) supply the scalars and cyclic modules R/I; the PID property comes from [factorisation in integral domains](../02-rings-and-fields/factorisation-in-integral-domains.md); [rank–nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md) is the field case of Smith normal form; [the Jordan normal form](../../04-linear-algebra/02-determinants-and-eigenvalues/jordan-normal-form.md) is recovered here as a corollary.
- **Above:** [homology](../../07-topology/02-algebraic-topology/homology.md) groups are finitely generated abelian groups, whose rank and torsion are read off by the structure theorem; [homological algebra](../../13-structure-and-metamathematics/01-category-theory/homological-algebra.md) studies modules through resolutions; [lattices](../../08-geometry/03-convex-and-discrete-geometry/lattices-and-sphere-packing.md) are free ℤ-modules inside ℝⁿ.
- **Siblings:** [representations of finite groups](representations-of-finite-groups.md) are modules over the group algebra.

## Common misconceptions

- **"Every module has a basis, as every vector space does."** ℤ/n and ℚ are counterexamples over ℤ.
- **"A linearly independent set of size n in Rⁿ is a basis."** In ℤ, the single element 2 is independent but does not span ℤ; over a field this cannot happen.
- **"Torsion-free means free."** True for finitely generated modules over a PID only: ℚ over ℤ and (2, x) over ℤ[x] are torsion-free but not free.

## Go deeper

- David Dummit and Richard Foote, *Abstract Algebra* (3rd edition, 2004): modules over PIDs with both applications worked in detail.
- Michael Artin, *Algebra* (2nd edition, 2011): Smith normal form and its uses, approached through matrices.
