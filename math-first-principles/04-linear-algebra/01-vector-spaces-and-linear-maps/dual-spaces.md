# Dual Spaces

> **Layer:** [04 Linear Algebra](../README.md) › [Vector Spaces and Linear Maps](README.md)
> **Builds on:** [Linear maps and matrices](linear-maps-and-matrices.md), [Linear systems and rank–nullity](linear-systems-and-rank-nullity.md), [Linear independence, bases and dimension](linear-independence-bases-and-dimension.md)
> **Enables:** [Tensor products](../04-multilinear-algebra/tensor-products.md), [Natural transformations and the Yoneda lemma](../../13-structure-and-metamathematics/01-category-theory/natural-transformations-and-the-yoneda-lemma.md), [Hahn–Banach and Baire category](../../09-advanced-analysis/03-functional-analysis/hahn-banach-and-baire-category.md), [Distributions](../../09-advanced-analysis/04-harmonic-analysis/distributions.md), [Convex optimisation and duality](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md)

## Essence
The dual space V∗ of a vector space V consists of the linear functionals, the linear maps V → F. A functional is a measurement: it takes a vector and returns a number, as a coordinate, a definite integral or an evaluation at a point does. In finite dimension V∗ has the same dimension as V, but there is no natural way to identify them; there is, however, a natural identification of V with its double dual V∗∗. That contrast was one of the motivating examples when Samuel Eilenberg and Saunders Mac Lane made "natural" precise in 1945, founding category theory.

## Core tenets
1. **A basis determines a dual basis.** If e₁, …, eₙ is a basis of V, the coordinate functionals e¹, …, eⁿ, defined by eⁱ(eⱼ) = 1 when i = j and 0 otherwise, form a basis of V∗. Any functional φ equals φ(e₁)e¹ + ⋯ + φ(eₙ)eⁿ, since both sides agree on the basis. Hence dim V∗ = dim V when V is finite-dimensional.

2. **A dual basis vector depends on the whole basis.** In ℝ² with basis e₁ = (1, 0), e₂ = (0, 1), the first coordinate functional is e¹(x, y) = x. Keep e₁ but change e₂ to (1, 1): now (x, y) = (x − y)e₁ + y e₂, so the new e¹ is x − y. Changing one basis vector changed a dual vector belonging to a different one. Correspondingly, if a change of basis is given by P, coordinates of vectors transform by P⁻¹ but components of functionals transform by P, which is the origin of the physicists' contravariant and covariant indices.

3. **V embeds naturally in V∗∗, and in finite dimension this is an isomorphism.** Each v gives the functional ev(v) on V∗ defined by φ ↦ φ(v). This map V → V∗∗ uses no choices, which is what natural means. It is injective, since a non-zero v is the first vector of some basis and its coordinate functional takes the value 1 on it. In finite dimension, dimensions match and ev is an isomorphism. It is an isomorphism if and only if V is finite-dimensional: the dual of ℝ[x] is the space of all real sequences (a functional is fixed by its values on 1, x, x², …), whose dimension is uncountable, while ℝ[x] has countable dimension.

4. **V ≅ V∗ needs extra structure.** Any basis gives an isomorphism eᵢ ↦ eⁱ, but by tenet 2 it changes with the basis. An inner product supplies a canonical one, v ↦ ⟨·, v⟩ (in the complex case it is conjugate-linear); this is the finite-dimensional [Riesz representation](../03-inner-product-spaces/inner-products-and-orthogonality.md). The derivative of a function is naturally a functional; turning it into the gradient vector uses the inner product.

5. **The transpose is the dual of a map.** A linear T: V → W induces Tᵀ: W∗ → V∗ by Tᵀ(φ) = φ ∘ T. In dual bases its matrix is the transpose of the matrix of T, which explains why transposes appear at all. Arrows reverse: (ST)ᵀ = TᵀSᵀ.

6. **Annihilators turn subspaces upside down.** For a subspace U of V, the annihilator U⁰ is the set of functionals vanishing on U, and dim U + dim U⁰ = dim V. Larger subspaces have smaller annihilators, and U⁰⁰ = U under V ≅ V∗∗. In ℝ³, a plane through 0 is the kernel of one functional, unique up to scale, which is its normal. This reversal is [projective duality](../../08-geometry/01-classical-geometry/projective-geometry.md) between points and lines.

7. **ker Tᵀ = (im T)⁰.** A functional φ on W kills im T exactly when φ ∘ T = 0. Two consequences follow at once: rank Tᵀ = rank T (row rank equals column rank), and b lies in im T if and only if every φ with Tᵀφ = 0 has φ(b) = 0, which is the Fredholm alternative of [linear systems](linear-systems-and-rank-nullity.md).

8. **In analysis, one uses continuous duals.** For normed spaces the useful dual consists of continuous functionals. Spaces equal to their double dual in this sense are called reflexive: Hilbert spaces and Lᵖ for 1 < p < ∞ are, ℓ¹ is not. [Hahn–Banach](../../09-advanced-analysis/03-functional-analysis/hahn-banach-and-baire-category.md) guarantees enough functionals; [distributions](../../09-advanced-analysis/04-harmonic-analysis/distributions.md) are functionals on test functions; and the dual problem in [optimisation](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md) lives in a dual space.

## Key concepts
| Term | Meaning |
|---|---|
| Linear functional | Linear map V → F |
| Dual space V∗ | Space of all linear functionals on V |
| Dual basis | Coordinate functionals of a basis |
| Double dual V∗∗ | Dual of V∗; contains V naturally |
| Evaluation map | v ↦ (φ ↦ φ(v)), natural and injective |
| Transpose Tᵀ | φ ↦ φ ∘ T from W∗ to V∗ |
| Annihilator U⁰ | Functionals vanishing on U |
| Reflexive space | Normed space whose evaluation map onto the continuous double dual is onto |

## How it fits
- **Below:** [linear maps](linear-maps-and-matrices.md), [bases](linear-independence-bases-and-dimension.md) and [rank–nullity](linear-systems-and-rank-nullity.md) give dimensions and the transpose.
- **Above:** [tensor products](../04-multilinear-algebra/tensor-products.md) identify Hom(V, W) with V∗ ⊗ W; [natural transformations](../../13-structure-and-metamathematics/01-category-theory/natural-transformations-and-the-yoneda-lemma.md) generalise V → V∗∗; covectors on manifolds become [differential forms](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md).
- **Siblings:** [linear systems](linear-systems-and-rank-nullity.md) gain a solvability certificate from the dual; the [transpose](linear-maps-and-matrices.md) gets its meaning here.

## Common misconceptions
- **"V and V∗ are the same thing."**: they have the same dimension, but they transform differently under change of basis. In graphics, surface normals are covectors and must be transformed by the inverse transpose, not by the matrix used for points ([geometry and transformations](../../../cs-first-principles/14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md)).
- **"V → V∗∗ is always onto."**: only in finite dimension. For infinite-dimensional spaces V∗ is strictly bigger in dimension than V, and V∗∗ bigger still.

## Go deeper
- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (2nd edition, 1958): duality, annihilators and reflexivity done classically.
- Sheldon Axler, *Linear Algebra Done Right* (4th edition, 2024): duals and the transpose without coordinates.
- Samuel Eilenberg and Saunders Mac Lane, "General theory of natural equivalences", *Transactions of the American Mathematical Society* (1945): where naturality was defined.
