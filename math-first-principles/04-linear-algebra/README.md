# 04 Linear Algebra

> **Layer:** 04 Linear Algebra
> **Children:** [Vector spaces and linear maps](01-vector-spaces-and-linear-maps/README.md) · [Determinants and eigenvalues](02-determinants-and-eigenvalues/README.md) · [Inner product spaces](03-inner-product-spaces/README.md) · [Multilinear algebra](04-multilinear-algebra/README.md)

## What this area is about
Linear algebra is the study of vector spaces and the linear maps between them. It is the one part of mathematics that is almost completely understood, and for that reason almost every other part tries to reduce its problems to it: calculus approximates functions by linear maps, geometry studies tangent spaces, algebra represents groups by matrices, and computation solves linear systems by the billion. The layer is organised by a series of classification questions, each with a complete answer. Up to isomorphism, a vector space is classified by its dimension. A linear map between two spaces is classified by its rank. A map from a space to itself is classified by its eigenvalues and, in full, by its Jordan normal form. A symmetric matrix is diagonalised by an orthonormal basis (the spectral theorem), every matrix has a singular value decomposition, and a real quadratic form is classified by its signature. Multilinear maps are made linear by tensor products, and the determinant appears as the top exterior power.

## Why this layer sits here
Linear algebra needs only what the first four layers supply. From [logic and proof](../00-logic-and-proof/README.md) it takes the axiomatic method and induction, which run the exchange lemma and most proofs about dimension. From [sets and foundations](../01-sets-and-foundations/README.md) it takes functions, quotients and, for infinite-dimensional spaces, the axiom of choice. From [number systems](../02-number-systems/README.md) it takes its fields, ℚ, ℝ, ℂ and ℤ/p; the fundamental theorem of algebra, which guarantees eigenvalues over ℂ, is the only analytic fact it uses. From [combinatorics and graph theory](../03-combinatorics-and-graph-theory/README.md) it takes permutations for the determinant, binomial coefficients for exterior powers, and graphs for Perron–Frobenius theory. In return it gives every later layer the same lesson: a linear map is determined by what it does to a basis, and the questions worth asking are those whose answers no change of basis can alter. It comes before abstract algebra so that groups, rings and modules can be met with matrix examples already in hand.

## How the children fit together
| Child | Its role in the whole | Depends on |
|---|---|---|
| [Vector spaces and linear maps](01-vector-spaces-and-linear-maps/README.md) | Axioms, bases, dimension, matrices, linear systems, duality | Layers 00–03 |
| [Determinants and eigenvalues](02-determinants-and-eigenvalues/README.md) | Invariants of a map from a space to itself; Jordan form; Perron–Frobenius | Vector spaces and linear maps |
| [Inner product spaces](03-inner-product-spaces/README.md) | Orthogonality, the spectral theorem, singular values, quadratic forms | Both of the above |
| [Multilinear algebra](04-multilinear-algebra/README.md) | Tensor products and exterior algebra | Vector spaces and linear maps, determinants |

```
          vector spaces and linear maps
             /            |            \
  determinants and        |        multilinear algebra
  eigenvalues ────────────┼──────────▶ (det = top exterior power)
             \            |
              inner product spaces
```

The first area builds the language and solves the first two classification problems: dimension for spaces and rank for maps. The second turns to maps from a space to itself, where one basis must serve on both sides; determinants and eigenvalues provide the invariants, and the Jordan form completes the classification over ℂ. The third adds an inner product, and with it the strongest theorems of the subject, the spectral theorem and the singular value decomposition, which never fail and are stable to compute. The fourth leaves linearity in one variable for linearity in several, and in doing so explains the determinant from first principles.

## Connections to neighbouring layers
- [02 Number systems](../02-number-systems/README.md): ℂ supplies eigenvalues, and modular arithmetic supplies finite fields for coding theory.
- [03 Combinatorics and graph theory](../03-combinatorics-and-graph-theory/README.md): adjacency matrices and graph Laplacians turn graphs into linear algebra, and Kirchhoff's matrix-tree theorem counts spanning trees by a determinant.
- [05 Abstract algebra](../05-abstract-algebra/README.md): modules generalise vector spaces, the Jordan form becomes the structure theorem for modules over a polynomial ring, and field extensions are measured by dimension.
- [06 Real analysis](../06-real-analysis/README.md): the derivative is a linear map, the Jacobian determinant rescales volume, and the Hessian test is a test for positive definiteness.
- [07 Topology](../07-topology/README.md): homology is computed by ranks of boundary matrices.
- [08 Geometry](../08-geometry/README.md): Klein's programme classifies geometries by matrix groups, and differential forms are exterior algebra on manifolds.
- [09 Advanced analysis](../09-advanced-analysis/README.md): Hilbert and Banach spaces, spectral theory and Fourier series are linear algebra in infinite dimension.
- [14 Applied and computational mathematics](../14-applied-and-computational-mathematics/README.md): numerical linear algebra makes elimination, eigenvalues and the singular value decomposition fast and stable.

## Connections across layers
- [10 Differential equations and dynamics](../10-differential-equations-and-dynamics/README.md): linear systems are solved by the matrix exponential, and stability is read from eigenvalues.
- [11 Probability and statistics](../11-probability-and-statistics/README.md): Markov chains converge to Perron vectors, and regression is orthogonal projection.
- [12 Number theory and algebraic geometry](../12-number-theory-and-algebraic-geometry/README.md): quadratic forms over ℚ and ℤ lead to the local-global principle and the class group.
- [13 Structure and metamathematics](../13-structure-and-metamathematics/README.md): the natural map V → V∗∗ motivated naturality, and tensor products are a model universal property.
- [15 Mathematics in context](../15-mathematics-in-context/README.md): elimination in ancient China and the long route from determinants to matrices are part of the history of mathematics.
- In computing, the same material is [linear algebra for computer science](../../cs-first-principles/01-mathematical-foundations/04-algebra/linear-algebra.md).

## Cross-cutting threads
- [Structure and morphism](../CROSS-CUTTING.md#structure-and-morphism): spaces studied through linear maps.
- [Invariants](../CROSS-CUTTING.md#invariants): dimension, rank, determinant, eigenvalues and signature.
- [Decomposition and classification](../CROSS-CUTTING.md#decomposition-and-classification): eigenspaces, Jordan blocks and the singular value decomposition.
- [Duality](../CROSS-CUTTING.md#duality): dual spaces, the transpose and annihilators.
- [Linearisation](../CROSS-CUTTING.md#linearisation): linear algebra is the target of every linear approximation.
- [Abstraction and generalisation](../CROSS-CUTTING.md#abstraction-and-generalisation): from ℝⁿ to arbitrary fields and from bilinear maps to tensors.
