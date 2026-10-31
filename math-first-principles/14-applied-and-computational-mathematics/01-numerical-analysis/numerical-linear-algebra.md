# Numerical Linear Algebra

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Numerical Analysis](README.md)
> **Builds on:** [Floating Point, Conditioning and Stability](floating-point-conditioning-and-stability.md), [Linear Systems and Rank–Nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md), [Inner Products and Orthogonality](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md), [The Spectral Theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md), [Quadratic Forms and Positive Definiteness](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md)
> **Enables:** [Numerical Methods for Differential Equations](numerical-methods-for-differential-equations.md), [Gradient Methods](../02-optimisation/gradient-methods.md), [High-Dimensional Geometry and Random Matrices](../06-data-and-learning/high-dimensional-geometry-and-random-matrices.md), [Linear Algebra (CS)](../../../cs-first-principles/01-mathematical-foundations/04-algebra/linear-algebra.md)

## Essence

At its core, most scientific computing solves linear systems Ax = b, fits least squares or finds eigenvalues. Numerical linear algebra factorises the matrix into triangular, orthogonal or diagonal pieces that are cheap to use, and judges each method by two questions: is it backward stable, and what does it cost? Direct methods factorise; iterative methods need only products Av, all that large sparse problems allow. Eigenvalues are different in kind: no finite formula computes them, so every eigenvalue algorithm is an iteration.

## Core tenets

1. **Gaussian elimination is LU factorisation, and it needs pivoting to be stable.** Eliminating below the diagonal writes A = LU, with L unit lower triangular (the multipliers) and U upper triangular, in about (2/3)n³ floating-point operations (flops); then each solve is two triangular substitutions. A tiny pivot is fatal: for A = [[10⁻²⁰, 1], [1, 1]] and b = (1, 2), elimination without row exchanges gives x₁ = 0 in double precision, while the true x₁ ≈ 1, although the condition number κ(A) = ‖A‖ ‖A⁻¹‖ is only about 2.6. Partial pivoting swaps the largest entry of the column into the pivot position (PA = LU, P a permutation), so no multiplier exceeds 1 in size. The backward error is then controlled by the growth of entries during elimination, which can reach 2^(n−1) on contrived matrices but is small in practice, for reasons only partly understood.

2. **Orthogonal transformations never amplify errors, so QR is the stable route to least squares.** An orthogonal Q (QᵀQ = I) preserves Euclidean length, so κ(Q) = 1. Householder reflections I − 2vvᵀ/(vᵀv) (Alston Householder, 1958) zero a column below the diagonal in one step and build A = QR with R upper triangular; minimising ‖Ax − b‖ then reduces to the triangular system Rx = Qᵀb. The normal equations AᵀAx = Aᵀb give the same answer in exact arithmetic but square the condition number, κ(AᵀA) = κ(A)², doubling the digits lost.

3. **A symmetric positive definite matrix factors as A = LLᵀ without pivoting.** Cholesky factorisation takes about n³/3 flops, half the work of LU, and needs no pivoting, because the diagonal identity aᵢᵢ = ∑ₖ lᵢₖ² bounds every entry of L by √aᵢᵢ: nothing can grow. It doubles as a test: for symmetric A it succeeds, with positive pivots, if and only if A is positive definite.

4. **Iterative methods trade exactness for cheap products with A.** For a sparse matrix with millions of rows, the LU factors fill in and stop fitting in memory, while Av costs one operation per nonzero entry. Splitting A = M − N with M easy to invert gives x_(k+1) = M⁻¹(Nxₖ + b), whose error is multiplied by G = M⁻¹N at each step (Jacobi: M diagonal; Gauss–Seidel: M lower triangular). It converges from every start if and only if the spectral radius ρ(G) is below 1, because Gᵏ → 0 exactly when ρ(G) < 1.

5. **Conjugate gradients minimise the error over a growing Krylov subspace.** For symmetric positive definite A, the Conjugate Gradient (CG) method of Magnus Hestenes and Eduard Stiefel (1952) picks xₖ in x₀ + span{r₀, Ar₀, …, A^(k−1)r₀}, where r₀ = b − Ax₀, to minimise the energy norm ‖x − x*‖_A, where ‖e‖_A² = eᵀAe, with one product by A per step. Since xₖ − x* = p(A)(x₀ − x*) for the best polynomial p of degree k with p(0) = 1, a Chebyshev polynomial gives the bound ‖xₖ − x*‖_A ≤ 2((√κ − 1)/(√κ + 1))ᵏ ‖x₀ − x*‖_A: with κ = κ(A), the step count grows like √κ, not κ. Preconditioning, replacing A by a better-conditioned M⁻¹A, is most of the practical art.

6. **Eigenvalues must be computed by iteration.** Every monic polynomial is the characteristic polynomial of its companion matrix, so a finite procedure of arithmetic and root extractions for the eigenvalues of every 5 × 5 matrix would solve every quintic by radicals, contradicting the Abel–Ruffini theorem. The simplest, power iteration v ↦ Av/‖Av‖, converges to an eigenvector for the eigenvalue λ₁ of largest absolute value, its error shrinking by ∣λ₂/λ₁∣ per step when ∣λ₂∣ < ∣λ₁∣.

7. **The QR algorithm finds all eigenvalues at once.** Factor Aₖ = QₖRₖ and set A_(k+1) = RₖQₖ = QₖᵀAₖQₖ. Each step is a similarity, so the eigenvalues never change, and under mild conditions the iterates converge to triangular form with the eigenvalues on the diagonal: it is power iteration on a whole basis at once. Found by John Francis and, independently, Vera Kublanovskaya around 1961, it is made fast by a first reduction to Hessenberg form (zero below the first subdiagonal), which cuts each step from n³ to n² flops, and by shifts, which make convergence typically quadratic, and cubic for symmetric matrices. For symmetric A it stably computes the decomposition the spectral theorem promises.

## Key concepts

| Term | Meaning |
|---|---|
| LU factorisation | A = LU, lower times upper triangular; with partial pivoting, PA = LU |
| QR factorisation | A = QR with Q orthogonal and R upper triangular |
| Cholesky factorisation | A = LLᵀ for symmetric positive definite A |
| Spectral radius ρ(G) | Largest absolute value of an eigenvalue of G |
| Krylov subspace | span{r, Ar, …, A^(k−1)r}, built from k − 1 products by A |
| Preconditioner | An easily inverted M ≈ A that makes M⁻¹A better conditioned |

## How it fits

- **Below:** [rank–nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md) says when Ax = b is solvable; [orthogonality](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md) and [the spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md) say what QR and eigenvalue algorithms compute; Cholesky and CG need [positive definiteness](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md).
- **Above:** interior-point methods for [linear programming](../02-optimisation/linear-programming.md) solve a linear system per iteration; PageRank is power iteration, justified by [Perron–Frobenius theory](../../04-linear-algebra/02-determinants-and-eigenvalues/non-negative-matrices-and-perron-frobenius.md); [random matrices](../06-data-and-learning/high-dimensional-geometry-and-random-matrices.md) explain random sketching.
- **Siblings:** [Newton's method](root-finding-and-newtons-method.md) in n dimensions is a sequence of linear solves; [differential equation solvers](numerical-methods-for-differential-equations.md) produce the large sparse systems that CG and preconditioners attack; [interpolation](interpolation-and-approximation.md) meets badly conditioned Vandermonde matrices.

## Common misconceptions

- **"To solve Ax = b, compute A⁻¹"**: the inverse costs about three times as much as LU and is less accurate; the LU factors serve every right-hand side.
- **"A determinant near zero means nearly singular"**: the 100 × 100 matrix 10⁻¹I has determinant 10⁻¹⁰⁰ and κ = 1. Nearness to singularity is measured by κ, not by det.
- **"Find eigenvalues as roots of the characteristic polynomial"**: roots can be violently sensitive to coefficients (see [root-finding](root-finding-and-newtons-method.md)), so algorithms work with the matrix.

## Go deeper

- Gene H. Golub and Charles F. Van Loan, *Matrix Computations* (4th edition, 2013): the encyclopaedia of the field.
- James W. Demmel, *Applied Numerical Linear Algebra* (1997): careful on stability and on eigenvalue algorithms.
- Yousef Saad, *Iterative Methods for Sparse Linear Systems* (2nd edition, 2003): Krylov methods and preconditioning.
