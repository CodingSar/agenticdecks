# Inner Product Spaces

> **Layer:** [04 Linear Algebra](../README.md) › Inner Product Spaces
> **Children:** [Inner products and orthogonality](inner-products-and-orthogonality.md) · [The spectral theorem](the-spectral-theorem.md) · [Singular value decomposition](singular-value-decomposition.md) · [Quadratic forms and positive definiteness](quadratic-forms-and-positive-definiteness.md)

## What this area is about
A bare vector space has no lengths or angles. An inner product supplies them, and with them come perpendicularity, orthonormal bases, projections and the adjoint of a map. This extra structure changes what can be proved. Symmetric and normal matrices, the ones compatible with the inner product, are always diagonalisable by an orthonormal basis: the spectral theorem. Every matrix whatever, even a rectangular one, becomes a rotation, a scaling and another rotation: the singular value decomposition. And symmetric matrices, viewed as quadratic forms, are classified by the signs of their eigenvalues. This is the part of linear algebra used most in geometry, physics, statistics and computation, because it combines exact theory with numerical stability.

## How the children fit together
| Child | Its role in the whole | Depends on |
|---|---|---|
| [Inner products and orthogonality](inner-products-and-orthogonality.md) | Lengths, angles, Gram–Schmidt, projection, least squares, adjoints | Vector spaces and linear maps |
| [The spectral theorem](the-spectral-theorem.md) | Orthonormal eigenbases for symmetric and normal matrices | Inner products, eigenvalues |
| [Singular value decomposition](singular-value-decomposition.md) | A = UΣVᵀ for every matrix; best low-rank approximation; pseudo-inverse | Spectral theorem |
| [Quadratic forms and positive definiteness](quadratic-forms-and-positive-definiteness.md) | Signature, Sylvester's law, tests for positivity | Spectral theorem, determinants |

```
     inner products and orthogonality
                   |
           spectral theorem
            /             \
  singular value        quadratic forms and
  decomposition         positive definiteness
```

Inner products come first: they define orthogonality and the adjoint, and the adjoint is what "symmetric" and "normal" refer to. The spectral theorem is the hub. It says the self-adjoint and normal maps have orthonormal eigenbases, and both later children are applications of it. The singular value decomposition applies it to AᵀA, which is symmetric and positive semidefinite for every A, and so extends orthogonal diagonalisation to all matrices, at the cost of using two bases instead of one. Quadratic forms apply it to the symmetric matrix of a form, reading off the signature from the signs of the eigenvalues, and positive definiteness is what makes an inner product in the first place, closing the circle.

## Connections to sibling areas
- [Vector spaces and linear maps](../01-vector-spaces-and-linear-maps/README.md): the inner product gives the canonical isomorphism V ≅ V∗ that dual spaces lack, and least squares replaces unsolvable linear systems.
- [Determinants and eigenvalues](../02-determinants-and-eigenvalues/README.md): the spectral theorem is the case where diagonalisation never fails, and leading minors test positive definiteness.
- [Multilinear algebra](../04-multilinear-algebra/README.md): an inner product is a symmetric tensor, and on ℝ³ it combines with the exterior algebra to give the cross product through the Hodge star.

## Connections across layers
- Below, the area uses [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md), [the complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md) and [variance](../../03-combinatorics-and-graph-theory/03-discrete-probability/expectation-and-variance.md).
- Above, [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md) and [spectral theory](../../09-advanced-analysis/03-functional-analysis/spectral-theory.md) extend the theory to infinite dimension; the Hessian test is in [several-variable calculus](../../06-real-analysis/04-calculus-of-several-variables/extrema-and-lagrange-multipliers.md); [Riemannian manifolds](../../08-geometry/02-differential-geometry/riemannian-manifolds.md) carry an inner product at each point; [regression](../../11-probability-and-statistics/04-statistical-inference/linear-models-and-regression.md) is projection; [numerical linear algebra](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-linear-algebra.md) relies on orthogonal transformations.
- In computing, principal components drive [unsupervised learning](../../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md) and unitary matrices are [quantum gates](../../../cs-first-principles/02-theory-of-computation/05-quantum-computation/qubits-and-quantum-circuits.md).

## Cross-cutting threads
- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): orthogonal projection and Eckart–Young give best approximations.
- [Extremal principles and optimisation](../../CROSS-CUTTING.md#extremal-principles-and-optimisation): eigenvalues as maxima of the Rayleigh quotient; least squares as minimisation.
- [Symmetry](../../CROSS-CUTTING.md#symmetry): orthogonal and unitary groups are the symmetries of an inner product.
- [Invariants](../../CROSS-CUTTING.md#invariants): the signature of a quadratic form survives every change of variables.
