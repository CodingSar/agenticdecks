# The Spectral Theorem

> **Layer:** [04 Linear Algebra](../README.md) › [Inner Product Spaces](README.md)
> **Builds on:** [Inner products and orthogonality](inner-products-and-orthogonality.md), [Eigenvalues and diagonalisation](../02-determinants-and-eigenvalues/eigenvalues-and-diagonalisation.md), [The complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md)
> **Enables:** [Singular value decomposition](singular-value-decomposition.md), [Quadratic forms and positive definiteness](quadratic-forms-and-positive-definiteness.md), [Spectral theory](../../09-advanced-analysis/03-functional-analysis/spectral-theory.md), [The mathematics of quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), [Boundary value problems and Sturm–Liouville theory](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md)

## Essence
The spectral theorem says that the matrices compatible with an inner product are exactly as simple as one could hope. A real symmetric matrix has real eigenvalues and an orthonormal basis of eigenvectors, so it is a rotation, a scaling along perpendicular axes, and the rotation back. Over ℂ the same holds for normal matrices, those commuting with their conjugate transpose, with unitary changes of basis. Unlike general diagonalisation, there is no failure case and no numerical fragility. Principal axes of an ellipse, normal modes of a vibrating system, energy levels of a quantum system and principal components of data are all instances.

## Core tenets
1. **The statement has a real and a complex form.** (a) If A is a real symmetric matrix, A = Aᵀ, then A = QDQᵀ with Q orthogonal and D real diagonal. (b) A complex matrix is unitarily diagonalisable, A = UDU∗ with U unitary and D diagonal, if and only if it is normal: AA∗ = A∗A. Hermitian matrices (A = A∗) are the normal ones with real eigenvalues; unitary matrices are the normal ones with eigenvalues of absolute value 1.

2. **Self-adjoint maps have real eigenvalues and orthogonal eigenspaces.** If A = A∗ and Av = λv with v ≠ 0, then λ⟨v, v⟩ = ⟨Av, v⟩ = ⟨v, Av⟩ = λ̄⟨v, v⟩, so λ is real. If Av = λv and Aw = μw with λ ≠ μ, then λ⟨v, w⟩ = ⟨Av, w⟩ = ⟨v, Aw⟩ = μ⟨v, w⟩, so ⟨v, w⟩ = 0.

3. **The proof is induction on an invariant complement.** A real symmetric A has a real eigenvalue λ by tenet 2, and A − λI is then a real singular matrix, so a real eigenvector v exists. Its orthogonal complement is invariant, since ⟨v, w⟩ = 0 implies ⟨v, Aw⟩ = ⟨Av, w⟩ = λ⟨v, w⟩ = 0. Restrict A to the complement and induct. For normal matrices, one first triangularises unitarily (the Schur form A = UTU∗) and checks that a normal upper triangular matrix must be diagonal.

4. **Eigenvalues are optimisation problems.** For symmetric A with eigenvalues λ₁ ≥ ⋯ ≥ λₙ, the Rayleigh quotient R(x) = ⟨Ax, x⟩/⟨x, x⟩ has maximum λ₁ and minimum λₙ, attained at eigenvectors; this is a case of [Lagrange multipliers](../../06-real-analysis/04-calculus-of-several-variables/extrema-and-lagrange-multipliers.md). The Courant–Fischer theorem characterises every λₖ as a max-min over subspaces of dimension k. A corollary is Weyl's inequality: adding a symmetric E moves each eigenvalue by at most the largest ∣eigenvalue∣ of E.

5. **The hypotheses are sharp.** [[1, 1], [0, 2]] (rows listed in turn) is diagonalisable, but its eigenvectors (1, 0) and (1, 1) are not orthogonal, because it is not symmetric. The rotation by 90° is normal but has no real eigenvalues, so the real form needs symmetry, not normality. The complex symmetric [[1, i], [i, −1]] squares to zero without being zero, so it is not diagonalisable at all: over ℂ, symmetry must be replaced by the Hermitian condition. In infinite dimension, multiplication by x on L²[0, 1] is self-adjoint but has no eigenvectors, which is why [spectral theory](../../09-advanced-analysis/03-functional-analysis/spectral-theory.md) needs measures in place of sums.

6. **A spectral decomposition defines functions of a matrix.** Write A = λ₁P₁ + ⋯ + λₖPₖ, with Pᵢ the orthogonal projection onto the i-th eigenspace. Then f(A) = f(λ₁)P₁ + ⋯ + f(λₖ)Pₖ for any function f on the eigenvalues. This defines √A for positive semidefinite A, e^(iAt) in quantum dynamics, and every other matrix function, consistently with power series.

7. **The theorem explains physics, data and graphs.** Small vibrations of a system with positive definite mass matrix M and stiffness matrix K split into independent normal modes: the eigenvectors of the symmetric matrix M^(−1/2)KM^(−1/2). In [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), observables are self-adjoint and measured values are eigenvalues. The principal components of data are eigenvectors of a covariance matrix. The [graph Laplacian](../../03-combinatorics-and-graph-theory/02-graph-theory/spectral-graph-theory-and-expanders.md) is symmetric, and its eigenvalues measure connectivity. [Sturm–Liouville theory](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md) is the spectral theorem for differential operators.

## Key concepts
| Term | Meaning |
|---|---|
| Symmetric matrix | Real A with A = Aᵀ |
| Hermitian matrix | Complex A with A = A∗ |
| Normal matrix | AA∗ = A∗A |
| Unitary diagonalisation | A = UDU∗ with U unitary |
| Rayleigh quotient | ⟨Ax, x⟩/⟨x, x⟩ |
| Spectral decomposition | A = Σ λᵢPᵢ with orthogonal projections Pᵢ |
| Schur form | A = UTU∗ with T upper triangular |
| Normal modes | Independent vibrations along eigenvectors |

## How it fits
- **Below:** [inner products](inner-products-and-orthogonality.md) give adjoints; [eigenvalues](../02-determinants-and-eigenvalues/eigenvalues-and-diagonalisation.md) give the problem; [the complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md) give conjugation.
- **Above:** [spectral theory](../../09-advanced-analysis/03-functional-analysis/spectral-theory.md) for operators; [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md); the shape operator of a surface is symmetric, and its eigenvalues are the principal curvatures ([Gaussian curvature](../../08-geometry/02-differential-geometry/surfaces-and-gaussian-curvature.md)).
- **Siblings:** the [singular value decomposition](singular-value-decomposition.md) applies the theorem to AᵀA; [quadratic forms](quadratic-forms-and-positive-definiteness.md) are diagonalised by it.

## Common misconceptions
- **"Diagonalisable matrices are symmetric."**: [[1, 1], [0, 2]] is diagonalisable but not symmetric. Symmetry is what makes the eigenvectors orthogonal.
- **"Complex symmetric matrices behave like real symmetric ones."**: the matrix in tenet 5 is a counterexample; the right complex condition is Hermitian.
- **"A symmetric matrix with positive entries has positive eigenvalues."**: [[1, 2], [2, 1]] has eigenvalues 3 and −1.

## Go deeper
- Sheldon Axler, *Linear Algebra Done Right* (4th edition, 2024): the real and complex spectral theorems.
- Peter D. Lax, *Linear Algebra and Its Applications* (2nd edition, 2007): variational principles and applications.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (1985): normal matrices, Courant–Fischer and Weyl.
