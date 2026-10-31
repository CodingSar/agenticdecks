# Quadratic Forms and Positive Definiteness

> **Layer:** [04 Linear Algebra](../README.md) › [Inner Product Spaces](README.md)
> **Builds on:** [The spectral theorem](the-spectral-theorem.md), [Determinants](../02-determinants-and-eigenvalues/determinants.md), [Linear independence, bases and dimension](../01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md)
> **Enables:** [Extrema and Lagrange multipliers](../../06-real-analysis/04-calculus-of-several-variables/extrema-and-lagrange-multipliers.md), [Convex optimisation and duality](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md), [Riemannian manifolds](../../08-geometry/02-differential-geometry/riemannian-manifolds.md), [p-adic numbers and local fields](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/p-adic-numbers-and-local-fields.md), [The geometry of general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md)

## Essence
A quadratic form is a homogeneous polynomial of degree two, such as q(x, y) = x² + 4xy + y², or in matrix language q(x) = xᵀAx with A symmetric. Quadratic forms describe the shape of a function near a critical point, the energy of a mechanical system, the variance of a combination of random variables and the metric of spacetime. Over the reals each form can be brought, by a change of variables, to a sum of squares with signs, and Sylvester's law of inertia says the number of plus and minus signs does not depend on how this is done. Whether all signs are plus, positive definiteness, is the most important single property, and there are several equivalent tests for it.

## Core tenets
1. **Quadratic forms correspond to symmetric matrices.** Away from characteristic 2, q(x) = xᵀAx with A symmetric, and the form recovers the symmetric bilinear form by polarisation: ⟨x, y⟩_A = (q(x + y) − q(x) − q(y))/2. A change of variables x = Py replaces A by PᵀAP, called congruence; this is not similarity, and the eigenvalues change, but some information survives.

2. **Completing the square diagonalises a form.** x² + 4xy + y² = (x + 2y)² − 3y², so in the variables u = x + 2y, v = y the form is u² − 3v², and rescaling v gives u² − w². Repeating this, or applying [the spectral theorem](the-spectral-theorem.md) with orthogonal P and then scaling, brings every real form to a sum of terms +yᵢ², −yᵢ² and 0.

3. **Sylvester's law of inertia: the numbers of signs are invariant.** In any diagonalisation, the numbers n₊ of plus signs and n₋ of minus signs are the same; (n₊, n₋) is the signature. Proof: if two diagonalisations had n₊ ≠ n₊', say n₊ > n₊', the subspace where the first is positive definite has dimension n₊, the subspace where the second is at most zero has dimension n − n₊', and their dimensions sum to more than n, so they share a non-zero vector on which q is both positive and not positive. James Joseph Sylvester published the law in 1852. Over ℂ every non-degenerate form becomes a sum of squares and the rank is the only invariant; over ℚ the Hasse–Minkowski theorem reduces the classification to the reals and the [p-adic numbers](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/p-adic-numbers-and-local-fields.md).

4. **Positive definiteness has five equivalent tests.** For real symmetric A, these are equivalent: xᵀAx > 0 for all x ≠ 0; all eigenvalues are positive; all leading principal minors (determinants of the top-left k × k blocks) are positive; all pivots in elimination without row swaps are positive; A = RᵀR for some invertible R (Cholesky when R is upper triangular). For A = [[2, 1], [1, 2]] (rows listed in turn) the minors are 2 and 3, the pivots 2 and 3/2, and the eigenvalues 1 and 3.

5. **Semidefiniteness needs all principal minors.** A is positive semidefinite when xᵀAx ≥ 0 for all x. The leading minors no longer suffice: diag(0, −1) has leading minors 0 and 0, yet q(0, 1) = −1. All principal minors, from every choice of rows and the same columns, must be non-negative. Covariance matrices are the basic example: the variance of a combination cᵀX of random variables is cᵀCc ≥ 0, with C the covariance matrix ([expectation and variance](../../03-combinatorics-and-graph-theory/03-discrete-probability/expectation-and-variance.md)).

6. **The second-derivative test is a statement about the Hessian.** At a critical point of a smooth function, a positive definite Hessian means a strict local minimum, negative definite a strict local maximum, and indefinite a saddle; if the Hessian is only semidefinite the test is silent, as x² + y⁴ (a minimum) and x² − y⁴ (a saddle) show. This is the multivariable test in [extrema and Lagrange multipliers](../../06-real-analysis/04-calculus-of-several-variables/extrema-and-lagrange-multipliers.md). A function with positive semidefinite Hessian everywhere is convex, and then every local minimum is global, the basis of [convex optimisation](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md).

7. **Indefinite forms are geometry and arithmetic too.** Spacetime in special relativity carries the Minkowski form t² − x² − y² − z², with signature (1, 3), and [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md) puts such a form on each tangent space. Over the integers, binary forms ax² + bxy + cy² were classified up to integral change of variables by Joseph-Louis Lagrange in the 1770s and Carl Friedrich Gauss in 1801; Gauss's composition of forms became the [class group](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/ideals-and-the-class-group.md).

## Key concepts
| Term | Meaning |
|---|---|
| Quadratic form | q(x) = xᵀAx with A symmetric |
| Congruence | A ↦ PᵀAP for invertible P |
| Signature | (n₊, n₋), numbers of positive and negative squares |
| Positive definite | q(x) > 0 for all x ≠ 0 |
| Positive semidefinite | q(x) ≥ 0 for all x |
| Indefinite | Takes both signs |
| Leading principal minor | Determinant of the top-left k × k block |
| Cholesky factorisation | A = RᵀR with R upper triangular, for positive definite A |

## How it fits
- **Below:** [the spectral theorem](the-spectral-theorem.md) diagonalises forms orthogonally; [determinants](../02-determinants-and-eigenvalues/determinants.md) give the minors; [dimension counting](../01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md) proves Sylvester's law.
- **Above:** the Hessian test in [several-variable calculus](../../06-real-analysis/04-calculus-of-several-variables/extrema-and-lagrange-multipliers.md); convexity in [optimisation](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md); metrics on [Riemannian manifolds](../../08-geometry/02-differential-geometry/riemannian-manifolds.md); the local-global principle over [p-adic fields](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/p-adic-numbers-and-local-fields.md).
- **Siblings:** an [inner product](inner-products-and-orthogonality.md) is a positive definite form; AᵀA in the [singular value decomposition](singular-value-decomposition.md) is positive semidefinite.

## Common misconceptions
- **"A symmetric matrix with positive entries is positive definite."**: [[1, 2], [2, 1]] gives q(1, −1) = −2. Conversely [[2, −1], [−1, 2]], with negative entries, is positive definite.
- **"Non-negative leading minors mean positive semidefinite."**: diag(0, −1) is the counterexample of tenet 5.
- **"A zero Hessian determinant means no extremum."**: it means only that the test is inconclusive; x⁴ + y⁴ has a minimum at the origin with zero Hessian.

## Go deeper
- Gilbert Strang, *Introduction to Linear Algebra* (6th edition, 2023): the tests for positive definiteness.
- Peter D. Lax, *Linear Algebra and Its Applications* (2nd edition, 2007): quadratic forms, inertia and convexity.
- J.-P. Serre, *A Course in Arithmetic* (1973): quadratic forms over ℚ and the Hasse–Minkowski theorem.
