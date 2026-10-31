# Eigenvalues and Diagonalisation

> **Layer:** [04 Linear Algebra](../README.md) › [Determinants and Eigenvalues](README.md)
> **Builds on:** [Determinants](determinants.md), [Linear maps and matrices](../01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md), [The complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md), [Recurrence relations](../../03-combinatorics-and-graph-theory/01-enumeration/recurrence-relations.md)
> **Enables:** [Jordan normal form](jordan-normal-form.md), [The spectral theorem](../03-inner-product-spaces/the-spectral-theorem.md), [Linear systems and the matrix exponential](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/linear-systems-and-the-matrix-exponential.md), [Stability and phase portraits](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/stability-and-phase-portraits.md), [Spectral theory](../../09-advanced-analysis/03-functional-analysis/spectral-theory.md)

## Essence
An eigenvector of a linear map T is a non-zero vector that T merely stretches: Tv = λv, and the stretch factor λ is the eigenvalue. Along an eigenvector a map is just multiplication by a number, so if a basis of eigenvectors exists the map is diagonal in that basis, and its powers, exponentials and long-term behaviour become transparent. Eigenvalues are the roots of the characteristic polynomial det(λI − A), so they are invariants of the map, independent of the basis. Not every map can be diagonalised, but the ones that can cover a great deal of applied mathematics, from vibrations to population growth to the Fibonacci numbers.

## Core tenets
1. **Eigenvalues are the roots of the characteristic polynomial.** Tv = λv for some v ≠ 0 means λI − T has a non-zero kernel, which holds if and only if det(λI − T) = 0. For an n × n matrix this is a polynomial of degree n, the same for similar matrices. Over ℂ it factors as (λ − λ₁)⋯(λ − λₙ), so the trace is λ₁ + ⋯ + λₙ and the determinant is λ₁⋯λₙ.

2. **The field matters: over ℂ, eigenvalues always exist.** Rotation of ℝ² by 90°, with matrix [[0, −1], [1, 0]] (rows listed in turn), fixes no direction, and its characteristic polynomial λ² + 1 has no real root. Over ℂ the roots are ±i, with eigenvectors (1, ∓i). The fundamental theorem of algebra guarantees that every complex square matrix has an eigenvalue, which is why complex scalars are the natural setting.

3. **Eigenvectors for distinct eigenvalues are independent.** Suppose a dependence among such eigenvectors exists, and take one with the fewest terms, a₁v₁ + ⋯ + aₖvₖ = 0. Applying T − λₖI kills the last term and multiplies each other term by λᵢ − λₖ ≠ 0, giving a shorter dependence, a contradiction. So an n × n matrix with n distinct eigenvalues is diagonalisable: A = PDP⁻¹, with eigenvectors as the columns of P and eigenvalues on the diagonal of D.

4. **Diagonalisable means enough eigenvectors.** The algebraic multiplicity of λ is its multiplicity as a root; the geometric multiplicity is dim ker(λI − A), at most the algebraic one. A is diagonalisable over a field containing its eigenvalues if and only if the two agree for every λ. The shear [[1, 1], [0, 1]] has eigenvalue 1 twice but only one independent eigenvector, (1, 0), so it is not diagonalisable.

5. **Diagonalisation makes powers and exponentials easy.** Aᵏ = PDᵏP⁻¹, and Dᵏ just raises the diagonal entries to the k-th power. The Fibonacci recurrence is vₖ₊₁ = Mvₖ with M = [[1, 1], [1, 0]], whose eigenvalues φ = (1 + √5)/2 and ψ = (1 − √5)/2 give Binet's formula Fₖ = (φᵏ − ψᵏ)/√5. Likewise e^(At) = Pe^(Dt)P⁻¹ solves x' = Ax, and all solutions decay to 0 if and only if every eigenvalue has negative real part; for non-diagonalisable A this still holds, by the [Jordan form](jordan-normal-form.md).

6. **Commuting maps share eigenvectors.** If AB = BA, then B maps each eigenspace of A into itself, and two commuting diagonalisable matrices can be diagonalised by one basis. Translation-invariant operators all commute with shifts, and that is why the exponentials e^(ikx) diagonalise them all at once: the root of [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md).

7. **Finding eigenvalues is hard in principle but routine in practice.** Every monic polynomial is the characteristic polynomial of its companion matrix, so by the [Abel–Ruffini theorem](../../05-abstract-algebra/03-galois-theory/solvability-by-radicals.md) there is no formula in radicals for eigenvalues of 5 × 5 matrices. Numerically one iterates instead: the power method repeatedly applies A and normalises, converging to an eigenvector for an eigenvalue strictly largest in absolute value; the QR algorithm, which repeatedly factors A as an orthogonal matrix times an upper triangular one and multiplies them back in reverse order, converges under suitable conditions to all eigenvalues at once.

## Key concepts
| Term | Meaning |
|---|---|
| Eigenvector | Non-zero v with Tv = λv |
| Eigenvalue | The scalar λ in Tv = λv |
| Eigenspace | ker(λI − T), all eigenvectors for λ together with 0 |
| Characteristic polynomial | det(λI − A), degree n, a similarity invariant |
| Algebraic multiplicity | Multiplicity of λ as a root |
| Geometric multiplicity | Dimension of the eigenspace |
| Diagonalisable | A = PDP⁻¹ with D diagonal; a basis of eigenvectors exists |
| Companion matrix | Matrix with a prescribed characteristic polynomial |

## How it fits
- **Below:** [determinants](determinants.md) define the characteristic polynomial; [the complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md) provide its roots; [recurrences](../../03-combinatorics-and-graph-theory/01-enumeration/recurrence-relations.md) are the first application.
- **Above:** eigenvalues decide [stability](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/stability-and-phase-portraits.md) and give [the matrix exponential](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/linear-systems-and-the-matrix-exponential.md); [spectral theory](../../09-advanced-analysis/03-functional-analysis/spectral-theory.md) extends them to operators; in [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) measured values are eigenvalues.
- **Siblings:** the [Jordan form](jordan-normal-form.md) handles the non-diagonalisable case; [Perron–Frobenius](non-negative-matrices-and-perron-frobenius.md) controls the largest eigenvalue of a non-negative matrix.

## Common misconceptions
- **"Every square matrix is diagonalisable."**: the shear [[1, 1], [0, 1]] is not, over any field. Over ℂ, however, the diagonalisable matrices are dense, so an arbitrarily small perturbation makes any matrix diagonalisable.
- **"The eigenvalues of A + B are the sums of eigenvalues of A and B."**: [[0, 1], [0, 0]] and [[0, 0], [1, 0]] have only the eigenvalue 0, yet their sum has eigenvalues ±1.
- **"Eigenvalues inside the unit disc mean vectors never grow."**: [[0.5, 100], [0, 0.5]] has both eigenvalues equal to 0.5, yet it stretches (0, 1) about 100 times in one step. Eigenvalues govern the long run, not the transient.

## Go deeper
- Sheldon Axler, *Linear Algebra Done Right* (4th edition, 2024): eigenvectors without determinants.
- Gilbert Strang, *Introduction to Linear Algebra* (6th edition, 2023): diagonalisation and its applications.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (1985): the standard reference on eigenvalues of matrices.
