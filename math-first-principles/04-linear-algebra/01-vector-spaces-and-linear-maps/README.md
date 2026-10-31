# Vector Spaces and Linear Maps

> **Layer:** [04 Linear Algebra](../README.md) › Vector Spaces and Linear Maps
> **Children:** [Fields and vector spaces](fields-and-vector-spaces.md) · [Linear independence, bases and dimension](linear-independence-bases-and-dimension.md) · [Linear maps and matrices](linear-maps-and-matrices.md) · [Linear systems and rank–nullity](linear-systems-and-rank-nullity.md) · [Dual spaces](dual-spaces.md)

## What this area is about
This area builds the language of linear algebra from axioms. A vector space is any set where vectors can be added and scaled by elements of a field; a linear map is a function respecting those operations. The unifying idea is the basis: it turns vectors into coordinate lists, linear maps into matrices, and functionals into a dual basis. Because all bases of a space have the same size, dimension classifies finite-dimensional spaces completely, and rank classifies linear maps up to separate changes of basis. Solving linear equations, the oldest problem in the subject, becomes the study of kernels and images, and duality explains why every unsolvable system has a certificate of its unsolvability.

## How the children fit together
| Child | Its role in the whole | Depends on |
|---|---|---|
| [Fields and vector spaces](fields-and-vector-spaces.md) | The axioms, the examples, subspaces and quotients | Layers 00–02 only |
| [Linear independence, bases and dimension](linear-independence-bases-and-dimension.md) | Coordinates, the exchange lemma and the invariance of dimension | Fields and vector spaces |
| [Linear maps and matrices](linear-maps-and-matrices.md) | Maps as matrices, composition as product, change of basis | Bases and dimension |
| [Linear systems and rank–nullity](linear-systems-and-rank-nullity.md) | Ax = b, elimination, and dim ker + rank = dim V | Linear maps |
| [Dual spaces](dual-spaces.md) | Functionals, the transpose, annihilators and naturality | Linear maps, linear systems |

```
   fields and vector spaces
              |
   bases and dimension
              |
   linear maps and matrices
              |
   linear systems and rank–nullity
              |
         dual spaces
```

The order is a chain, because each step uses the one before. Fields and vector spaces fix the rules and supply the examples. Bases and dimension then show that, once a basis is chosen, every finite-dimensional space looks like Fⁿ, which is what makes computation possible. Linear maps are the next object: a map is free to send a basis anywhere, so it is recorded by a matrix, and the matrix changes by conjugation when the basis changes. Linear systems ask the basic question about one map, whether Tx = b can be solved, and rank–nullity answers how much freedom the solutions have. Dual spaces close the area by turning the picture around: functionals measure vectors, every map has a transpose, and the image of a map is described by the functionals that vanish on it.

## Connections to sibling areas
- [Determinants and eigenvalues](../02-determinants-and-eigenvalues/README.md): determinants test invertibility of the square matrices introduced here, and eigenvalues classify maps from a space to itself, which rank alone cannot do.
- [Inner product spaces](../03-inner-product-spaces/README.md): adding lengths and angles turns the dual space into the space itself (Riesz) and turns unsolvable systems into least-squares problems.
- [Multilinear algebra](../04-multilinear-algebra/README.md): tensor products are built from the dual spaces and the universal property of bilinear maps, and exterior powers grow out of dimension counting.

## Connections across layers
- Below, the area uses [axioms](../../00-logic-and-proof/03-the-axiomatic-method/axioms-definitions-and-theorems.md), [quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md), [the axiom of choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md) and [modular arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md).
- Above, [modules](../../05-abstract-algebra/04-modules-and-representations/modules.md) replace the field by a ring, [field extensions](../../05-abstract-algebra/02-rings-and-fields/field-extensions.md) are measured by dimension, [the derivative](../../06-real-analysis/03-calculus-of-several-variables/the-derivative-as-a-linear-map.md) is a linear map, [Banach spaces](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md) take the theory to infinite dimension, and [numerical linear algebra](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-linear-algebra.md) makes elimination reliable.
- In computing, the same material appears as [linear algebra for computer science](../../../cs-first-principles/01-mathematical-foundations/04-algebra/linear-algebra.md).

## Cross-cutting threads
- [Structure and morphism](../../CROSS-CUTTING.md#structure-and-morphism): vector spaces and linear maps are a model case of objects studied through their structure-preserving maps.
- [Invariants](../../CROSS-CUTTING.md#invariants): dimension and rank are the complete invariants for spaces and for maps up to change of basis.
- [Duality](../../CROSS-CUTTING.md#duality): V∗, the transpose and annihilators reverse inclusions and arrows.
- [Equivalence and quotients](../../CROSS-CUTTING.md#equivalence-and-quotients): V/U and the first isomorphism theorem.
