# Inner Products and Orthogonality

> **Layer:** [04 Linear Algebra](../README.md) › [Inner Product Spaces](README.md)
> **Builds on:** [Linear independence, bases and dimension](../01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md), [Dual spaces](../01-vector-spaces-and-linear-maps/dual-spaces.md), [The real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md), [The complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md)
> **Enables:** [The spectral theorem](the-spectral-theorem.md), [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md), [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md), [Linear models and regression](../../11-probability-and-statistics/04-statistical-inference/linear-models-and-regression.md), [Euclidean geometry](../../08-geometry/01-classical-geometry/euclidean-geometry.md)

## Essence
An inner product adds geometry to a vector space: lengths, angles and, above all, perpendicularity. The dot product on ℝⁿ is the model, but the same axioms apply to functions, where the inner product is an integral, and to random variables, where it is a covariance. Orthogonality makes computation easy, because coordinates in an orthonormal basis are just inner products, and it makes approximation possible, because the closest point of a subspace is found by dropping a perpendicular. Least squares, Fourier series and the quantum state space are all instances of this one picture.

## Core tenets
1. **An inner product is a positive definite symmetric (or Hermitian) form.** On a real space it is a map ⟨x, y⟩ that is linear in each argument, symmetric, and has ⟨x, x⟩ > 0 for x ≠ 0. On a complex space symmetry becomes ⟨y, x⟩ = conjugate of ⟨x, y⟩, and the standard example is ⟨x, y⟩ = x₁ȳ₁ + ⋯ + xₙȳₙ; without the conjugate, (1, i) would have length zero. Every inner product on ℝⁿ has the form ⟨x, y⟩ = xᵀMy for a symmetric positive definite matrix M. The length is ‖x‖ = √⟨x, x⟩.

2. **The Cauchy–Schwarz inequality makes angles and distances meaningful.** ∣⟨x, y⟩∣ ≤ ‖x‖‖y‖, with equality exactly when x and y are dependent. In the real case, the quadratic ‖x + ty‖² = ‖x‖² + 2t⟨x, y⟩ + t²‖y‖² is never negative, so its discriminant is not positive, which is the inequality. It gives the triangle inequality, so ‖x − y‖ is a [metric](../../06-real-analysis/03-metric-spaces/metric-spaces-and-continuity.md), and it lets one define the angle by cos θ = ⟨x, y⟩ / (‖x‖‖y‖).

3. **Orthonormal bases make coordinates into inner products.** If e₁, …, eₙ are orthonormal, then x = ⟨x, e₁⟩e₁ + ⋯ + ⟨x, eₙ⟩eₙ and ‖x‖² = ∣⟨x, e₁⟩∣² + ⋯ + ∣⟨x, eₙ⟩∣², Pythagoras in n dimensions. No linear system needs solving to find coordinates.

4. **Gram–Schmidt turns any basis into an orthonormal one.** Subtract from each vector its components along the previous orthonormal vectors and normalise the remainder. The procedure is named after Jørgen Gram (1883) and Erhard Schmidt (1907). In matrix terms it factors any matrix with independent columns as A = QR, with Q having orthonormal columns and R upper triangular.

5. **The closest point in a subspace is the orthogonal projection.** For a subspace U, every x splits uniquely as x = p + r with p in U and r perpendicular to U, and p is the point of U nearest x, by Pythagoras. If Ax = b has no solution, the least-squares solution makes Ax the projection of b onto the column space, and solves the normal equations AᵀAx = Aᵀb. Fitting y = mx + c to the points (0, 0), (1, 1), (2, 3) gives y = 1.5x − 1/6, with residuals 1/6, −1/3, 1/6, which are perpendicular to both columns.

6. **Inner products identify a space with its dual.** In finite dimension every functional φ has the form φ(x) = ⟨x, w⟩ for a unique w: if e₁, …, eₙ is orthonormal, w = Σ c̄ᵢeᵢ where cᵢ = φ(eᵢ). This is the Riesz representation in finite dimension, and it gives every map T an adjoint T∗ with ⟨Tx, y⟩ = ⟨x, T∗y⟩; for a real matrix, T∗ is the transpose and for a complex one the conjugate transpose.

7. **Maps preserving the inner product are orthogonal or unitary.** A real matrix Q with QᵀQ = I preserves lengths and angles; these form the orthogonal group O(n), and their complex counterparts with U∗U = I the unitary group U(n). Because they do not magnify errors, algorithms built from them are the backbone of stable [floating-point computation](../../14-applied-and-computational-mathematics/01-numerical-analysis/floating-point-conditioning-and-stability.md). Quantum gates are unitary matrices ([qubits and quantum circuits](../../../cs-first-principles/02-theory-of-computation/05-quantum-computation/qubits-and-quantum-circuits.md)).

8. **Functions are vectors too.** On functions on [−π, π], ⟨f, g⟩ = ∫ f(x)g(x) dx is an inner product, and 1, cos x, sin x, cos 2x, sin 2x, … are orthogonal. A Fourier coefficient is the projection onto one of them. Completing such spaces under the norm gives L² and the theory of [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md).

## Key concepts
| Term | Meaning |
|---|---|
| Inner product | Positive definite symmetric or Hermitian form ⟨x, y⟩ |
| Norm | ‖x‖ = √⟨x, x⟩ |
| Orthogonal | ⟨x, y⟩ = 0 |
| Orthonormal basis | Mutually orthogonal unit vectors that form a basis |
| Orthogonal projection | Nearest point of a subspace; the residual is perpendicular to it |
| Gram–Schmidt | Orthonormalisation; gives A = QR |
| Adjoint | T∗ with ⟨Tx, y⟩ = ⟨x, T∗y⟩ |
| Orthogonal matrix | QᵀQ = I; preserves lengths |

## How it fits
- **Below:** [bases](../01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md) and [dual spaces](../01-vector-spaces-and-linear-maps/dual-spaces.md) supply the algebra; [the reals](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md) and [the complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md) supply positivity and conjugation.
- **Above:** [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md) and [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md) take the picture to infinite dimension; [regression](../../11-probability-and-statistics/04-statistical-inference/linear-models-and-regression.md) is projection; a [Riemannian metric](../../08-geometry/02-differential-geometry/riemannian-manifolds.md) is an inner product on each tangent space; [Euclidean geometry](../../08-geometry/01-classical-geometry/euclidean-geometry.md) is the geometry of ℝⁿ with its dot product.
- **Siblings:** [the spectral theorem](the-spectral-theorem.md) needs adjoints; [quadratic forms](quadratic-forms-and-positive-definiteness.md) generalise inner products by dropping positivity.

## Common misconceptions
- **"The dot product is the only inner product."**: ⟨x, y⟩ = 2x₁y₁ + 3x₂y₂ on ℝ² is another, and changes which vectors count as perpendicular.
- **"Orthogonality is a property of the vectors alone."**: it depends on the inner product. (1, 0) and (1, 1) are not perpendicular for the dot product but are for ⟨x, y⟩ = xᵀMy with M = [[1, −1], [−1, 2]] (rows listed in turn).
- **"Solve least squares by forming AᵀA."**: the normal equations square the condition number and can lose half the accurate digits; the QR factorisation avoids this.

## Go deeper
- Sheldon Axler, *Linear Algebra Done Right* (4th edition, 2024): inner product spaces and adjoints.
- Gilbert Strang, *Introduction to Linear Algebra* (6th edition, 2023): projections and least squares.
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra* (1997): QR and stable least squares.
