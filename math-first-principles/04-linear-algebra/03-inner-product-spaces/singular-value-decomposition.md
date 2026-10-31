# Singular Value Decomposition

> **Layer:** [04 Linear Algebra](../README.md) › [Inner Product Spaces](README.md)
> **Builds on:** [The spectral theorem](the-spectral-theorem.md), [Inner products and orthogonality](inner-products-and-orthogonality.md), [Linear systems and rank–nullity](../01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md)
> **Enables:** [Numerical linear algebra](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-linear-algebra.md), [High-dimensional geometry and random matrices](../../14-applied-and-computational-mathematics/06-data-and-learning/high-dimensional-geometry-and-random-matrices.md), [Linear models and regression](../../11-probability-and-statistics/04-statistical-inference/linear-models-and-regression.md), [Floating point, conditioning and stability](../../14-applied-and-computational-mathematics/01-numerical-analysis/floating-point-conditioning-and-stability.md), [Unsupervised learning](../../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md)

## Essence
The Singular Value Decomposition (SVD) writes every matrix, square or not, as a rotation, a scaling along perpendicular axes, and another rotation: A = UΣVᵀ. Eigenvalues need a square matrix and can fail to exist or to give an orthogonal basis; singular values always exist and always come with orthonormal bases, one in the domain and one in the target. The SVD reveals the rank, gives the best low-rank approximation, defines the pseudo-inverse, and measures how close a matrix is to singular. Principal Component Analysis (PCA), the most widely used method of dimension reduction, is the SVD of a data matrix.

## Core tenets
1. **Every matrix has an SVD.** For a real m × n matrix A of rank r there are orthogonal U (m × m) and V (n × n) and an m × n matrix Σ, zero except for σ₁ ≥ σ₂ ≥ ⋯ ≥ σᵣ > 0 on its diagonal, with A = UΣVᵀ. Equivalently, A = σ₁u₁v₁ᵀ + ⋯ + σᵣuᵣvᵣᵀ, a sum of r rank-one pieces. Over ℂ the same holds with unitary U and V.

2. **The proof applies the spectral theorem to AᵀA.** AᵀA is symmetric and positive semidefinite, since xᵀAᵀAx = ‖Ax‖² ≥ 0, so it has an orthonormal eigenbasis v₁, …, vₙ with eigenvalues σᵢ² ≥ 0. Set uᵢ = Avᵢ/σᵢ for σᵢ > 0; these are orthonormal because ⟨Avᵢ, Avⱼ⟩ = ⟨AᵀAvᵢ, vⱼ⟩ = σᵢ²⟨vᵢ, vⱼ⟩. Extend the uᵢ to an orthonormal basis. So A maps the orthonormal vᵢ to σᵢ times the orthonormal uᵢ.

3. **Singular values are not eigenvalues.** [[0, 1], [0, 0]] (rows listed in turn) has both eigenvalues 0, but singular values 1 and 0: it sends v₁ = (0, 1) to u₁ = (1, 0) at full length. Singular values are the eigenvalues only for symmetric positive semidefinite matrices; for normal matrices they are the absolute values of the eigenvalues.

4. **The SVD gives orthonormal bases for the four fundamental subspaces.** v₁, …, vᵣ span the row space and vᵣ₊₁, …, vₙ the kernel; u₁, …, uᵣ span the column space and uᵣ₊₁, …, uₘ the kernel of Aᵀ. This is rank–nullity made orthogonal, and it shows that A restricted to its row space is an isomorphism onto its column space.

5. **Eckart–Young: truncating the SVD gives the best low-rank approximation.** Let Aₖ = σ₁u₁v₁ᵀ + ⋯ + σₖuₖvₖᵀ. Among all matrices B of rank at most k, Aₖ minimises ‖A − B‖, with error σₖ₊₁ in the operator norm and √(σₖ₊₁² + ⋯ + σᵣ²) in the Frobenius norm. For the operator norm: ker B has dimension at least n − k, and span(v₁, …, vₖ₊₁) has dimension k + 1; since (n − k) + (k + 1) > n they share a unit vector x, and ‖(A − B)x‖ = ‖Ax‖ ≥ σₖ₊₁. Carl Eckart and Gale Young proved the Frobenius case in 1936.

6. **The pseudo-inverse solves every least-squares problem.** A⁺ = VΣ⁺Uᵀ, where Σ⁺ inverts the non-zero σᵢ and transposes the shape. x = A⁺b is the least-squares solution of Ax = b of smallest length, and A⁺ = A⁻¹ when A is invertible. It was defined by E. H. Moore in 1920 and independently by Roger Penrose in 1955.

7. **Singular values measure sensitivity.** The operator norm is σ₁; the distance from a square A to the nearest singular matrix is σₙ; the condition number κ = σ₁/σₙ bounds how much relative errors in b are amplified in the solution of Ax = b. Each σᵢ moves by at most ‖E‖ when A becomes A + E, so singular values are stable to compute, and numerical rank, the number of σᵢ above a tolerance, is reliable where exact rank is not ([floating point and conditioning](../../14-applied-and-computational-mathematics/01-numerical-analysis/floating-point-conditioning-and-stability.md)).

8. **PCA is the SVD of centred data.** Put N data points in ℝᵈ as the rows of X, after subtracting the mean. The right singular vectors are the principal directions, and the variance of the data along vᵢ is σᵢ²/(N − 1). Projecting onto the first k directions keeps the most variance possible, by Eckart–Young. Karl Pearson introduced the idea in 1901 and Harold Hotelling developed it in 1933 ([unsupervised learning](../../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md)).

## Key concepts
| Term | Meaning |
|---|---|
| Singular values | σ₁ ≥ ⋯ ≥ σᵣ > 0, square roots of eigenvalues of AᵀA |
| Singular vectors | Orthonormal vᵢ (right) and uᵢ (left) with Avᵢ = σᵢuᵢ |
| Operator norm | Largest stretch ‖Ax‖/‖x‖; equals σ₁ |
| Frobenius norm | Square root of the sum of squared entries |
| Low-rank approximation | Aₖ, the first k terms of the SVD |
| Pseudo-inverse | A⁺ = VΣ⁺Uᵀ |
| Condition number | σ₁/σₙ for square invertible A |
| Principal component | Leading right singular vector of centred data |

## How it fits
- **Below:** [the spectral theorem](the-spectral-theorem.md) applied to AᵀA, [orthogonality](inner-products-and-orthogonality.md), and the four subspaces of [rank–nullity](../01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md).
- **Above:** [numerical linear algebra](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-linear-algebra.md) computes it stably; [random matrix theory](../../14-applied-and-computational-mathematics/06-data-and-learning/high-dimensional-geometry-and-random-matrices.md) studies singular values of random data; low-rank recovery in [compressed sensing](../../14-applied-and-computational-mathematics/06-data-and-learning/sampling-and-compressed-sensing.md); [regression](../../11-probability-and-statistics/04-statistical-inference/linear-models-and-regression.md) uses the pseudo-inverse.
- **Siblings:** for square A, the SVD gives the polar decomposition A = (UVᵀ)(VΣVᵀ), an orthogonal matrix times a positive semidefinite one; [quadratic forms](quadratic-forms-and-positive-definiteness.md) explain AᵀA.

## Common misconceptions
- **"Singular values are the absolute values of the eigenvalues."**: only for normal matrices; tenet 3 gives a counterexample.
- **"PCA finds the important variables."**: principal components are combinations of all variables, depend on their units, and capture variance, which need not be what matters.
- **"The SVD is unique."**: the σᵢ are, but signs of singular vectors can flip in pairs, and repeated singular values allow any orthonormal basis of the shared space.

## Go deeper
- Gilbert Strang, *Introduction to Linear Algebra* (6th edition, 2023): the SVD as the climax of the subject.
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra* (1997): computing and using the SVD.
- G. W. Stewart, "On the early history of the singular value decomposition", *SIAM Review* (1993): who discovered what.
