# Multilinear Algebra

> **Layer:** [04 Linear Algebra](../README.md) › Multilinear Algebra
> **Children:** [Tensor products](tensor-products.md) · [Exterior algebra](exterior-algebra.md)

## What this area is about
Linear algebra studies maps that are linear in one variable. Many of the most important constructions are linear in several variables separately: the inner product, the determinant, matrix multiplication, the curvature of a surface. Multilinear algebra turns such maps back into linear ones by building new spaces. The tensor product V ⊗ W is the universal space for bilinear maps, defined by that property and only then constructed. Quotients of the tensor algebra then pick out symmetric tensors, which are polynomials, and alternating tensors, which form the exterior algebra of oriented areas and volumes. The determinant reappears as the top exterior power, now defined without matrices, and the exterior algebra of the dual space becomes, pointwise on a manifold, the language of differential forms.

## How the children fit together
| Child | Its role in the whole | Depends on |
|---|---|---|
| [Tensor products](tensor-products.md) | Universal property, dimension mn, tensor rank, Hom(V, W) ≅ V∗ ⊗ W | Dual spaces, linear maps |
| [Exterior algebra](exterior-algebra.md) | Wedge product, Λᵏ(V), the determinant as top exterior power | Tensor products, determinants |

```
                tensor algebra
            (all V ⊗ ⋯ ⊗ V together)
              /                   \
   symmetric algebra          exterior algebra
   (quotient by v ⊗ w − w ⊗ v)  (quotient by v ⊗ v)
     = polynomials               = oriented volumes
```

Tensor products come first, because both other constructions are quotients of the tensor algebra. The tensor product answers a universal question: what is the most general way to multiply a vector of V by a vector of W bilinearly? Its answer explains linear maps as tensors, gives the trace as a contraction, and introduces the notion of rank that governs entanglement and the complexity of matrix multiplication. The exterior algebra imposes the single extra relation v ∧ v = 0. That makes products of dependent vectors vanish, so a wedge product records the subspace spanned and the volume of the parallelepiped. Its top degree is one-dimensional, which is exactly why each linear map has a determinant. The symmetric algebra, the other quotient, is the coordinate-free form of the polynomial ring and is met again in algebra and geometry.

## Connections to sibling areas
- [Vector spaces and linear maps](../01-vector-spaces-and-linear-maps/README.md): dual spaces supply the V∗ factors of tensors, and Hom(V, W) is itself a tensor product.
- [Determinants and eigenvalues](../02-determinants-and-eigenvalues/README.md): the determinant is the top exterior power, and the coefficients of the characteristic polynomial are traces on exterior powers.
- [Inner product spaces](../03-inner-product-spaces/README.md): an inner product is a symmetric tensor of type (0, 2), and with an orientation it gives the Hodge star and, in ℝ³, the cross product.

## Connections across layers
- Below, the area uses [quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md) for the construction and [binomial coefficients](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md) for dimensions.
- Above, [differential forms and de Rham cohomology](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md) apply exterior algebra at every point of a manifold; [universal properties](../../13-structure-and-metamathematics/01-category-theory/universal-properties-and-adjunctions.md) make the definition of the tensor product a model case; tensor products of [modules](../../05-abstract-algebra/04-modules-and-representations/modules.md) generalise it; composite systems in [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) and spacetime curvature in [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md) are tensors.
- In computing, multi-qubit registers are tensor products ([qubits and quantum circuits](../../../cs-first-principles/02-theory-of-computation/05-quantum-computation/qubits-and-quantum-circuits.md)).

## Cross-cutting threads
- [Abstraction and generalisation](../../CROSS-CUTTING.md#abstraction-and-generalisation): defining an object by a universal property rather than a construction.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): the universal property gives uniqueness, and a quotient construction gives existence.
- [Invariants](../../CROSS-CUTTING.md#invariants): the determinant and the trace as basis-free invariants of a map.
- [Local to global](../../CROSS-CUTTING.md#local-to-global): exterior algebra at each point integrates, through Stokes's theorem, to statements about whole manifolds.
