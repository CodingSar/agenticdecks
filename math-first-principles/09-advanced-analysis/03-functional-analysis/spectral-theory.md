# Spectral Theory

> **Layer:** [09 Advanced Analysis](../README.md) › [Functional Analysis](README.md)
> **Builds on:** [Banach Spaces](banach-spaces.md), [Hilbert Spaces](hilbert-spaces.md), [Hahn–Banach and Baire Category](hahn-banach-and-baire-category.md), [The Spectral Theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md), [Cauchy's Theorem and Its Consequences](../02-complex-analysis/cauchys-theorem-and-its-consequences.md)
> **Enables:** [The Mathematics of Quantum Mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), [Boundary Value Problems and Sturm–Liouville Theory](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md), [The Heat Equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md), [Markov Chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md)

## Essence

In finite dimensions a symmetric matrix is diagonal in an orthonormal basis of eigenvectors, and its eigenvalues are the numbers λ for which A − λ fails to be invertible. Spectral theory carries this to operators on infinite-dimensional spaces. The first surprise is that eigenvalues are no longer enough: T − λ can be injective without being onto, so the spectrum is defined as the set of λ for which T − λ has no bounded inverse, and it can be large while there are no eigenvalues at all. The second is that for compact self-adjoint operators the finite-dimensional picture survives almost intact, which is why vibrating strings, heat flow and integral equations decompose into modes.

## Core tenets

1. **The spectrum is where T − λ is not invertible, and it is more than the eigenvalues.** For a bounded operator T on a complex Banach space, σ(T) is the set of λ ∈ ℂ for which T − λI has no bounded inverse; by the bounded inverse theorem this means T − λI is not a bijection. Eigenvalues belong to it, but so do λ where T − λ is injective with a range that is not everything. The right shift S(x₁, x₂, …) = (0, x₁, x₂, …) on ℓ² is injective with no eigenvalues, yet σ(S) is the closed unit disc. Multiplication by x on L²[0,1] has no eigenvalues, since xf = λf forces f = 0 almost everywhere, and its spectrum is [0, 1].

2. **The spectrum is compact.** If ∣λ∣ > ‖T‖, then T − λ = −λ(I − T/λ) is inverted by a Neumann series, so σ(T) lies in the closed disc of radius ‖T‖. If T − λ₀ is invertible, small perturbations remain invertible, so the complement of σ(T), the resolvent set, is open.

3. **The spectrum is non-empty, by Liouville's theorem.** Suppose σ(T) were empty. Then the resolvent R(λ) = (T − λ)⁻¹ would be defined on all of ℂ, and for every bounded functional φ on the operators, φ(R(λ)) would be an entire function tending to 0 as ∣λ∣ → ∞. By [Liouville's theorem](../02-complex-analysis/cauchys-theorem-and-its-consequences.md) each would be identically 0, and by [Hahn–Banach](hahn-banach-and-baire-category.md) so would R(λ), which is absurd for an inverse. Complex scalars are needed: rotation by 90° on ℝ² has no real eigenvalue. Gelfand's formula, also from complex analysis, gives the spectral radius as r(T) = lim ‖Tⁿ‖^(1/n).

4. **Compact operators behave like matrices away from 0.** An operator is compact if it maps bounded sets to sets with compact closure; limits of finite-rank operators are compact, and integral operators (Kf)(x) = ∫ k(x, y)·f(y) dy with square-integrable kernel k are compact on L². For compact T, every non-zero point of σ(T) is an eigenvalue of finite multiplicity, and the eigenvalues can accumulate only at 0. The Fredholm alternative follows: for λ ≠ 0, either (T − λ)x = y has a unique solution for every y, or the homogeneous equation has non-trivial solutions, exactly as for square matrices. Compactness matters: the identity on ℓ² is not compact, and 1 is an eigenvalue of infinite multiplicity.

5. **The spectral theorem for compact self-adjoint operators.** Let T be compact and self-adjoint, ⟨Tx, y⟩ = ⟨x, Ty⟩, on a Hilbert space H. Then H has an orthonormal basis of eigenvectors of T, the eigenvalues λₙ are real and tend to 0 if there are infinitely many, and

   ```
   T x = ∑ₙ λₙ ⟨x, eₙ⟩ eₙ
   ```

   Proof idea: maximise ∣⟨Tx, x⟩∣ over the unit sphere. A maximising sequence has a weakly convergent subsequence, and compactness turns weak convergence of x into norm convergence of Tx, so the maximum is attained; the Lagrange condition says the maximiser is an eigenvector with eigenvalue ±‖T‖. Self-adjointness makes the orthogonal complement of an eigenvector invariant, so one repeats there. Without self-adjointness, the Volterra operator (Vf)(x) = ∫₀ˣ f is compact with spectrum {0} and no eigenvectors at all.

6. **Differential equations are diagonalised through their inverses.** The operator −d²/dx² on [0, π] with zero boundary values is unbounded, but its inverse is an integral operator with a continuous kernel, Green's function, which is compact and self-adjoint. Its eigenfunctions sin(nx), with eigenvalues 1/n², form, once normalised, an orthonormal basis, which is why [Sturm–Liouville problems](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md) have complete sets of modes and why the [heat equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md) is solved by ∑ e^(−n²t)·bₙ·sin(nx).

7. **Beyond compactness the spectrum becomes continuous.** A bounded self-adjoint operator satisfies a spectral theorem in which the sum becomes an integral against a projection-valued measure: it is unitarily a multiplication operator, like x on L²[0,1]. Unbounded self-adjoint operators, such as the position, momentum and energy observables of [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), need von Neumann's theory of domains and are treated in 14. There the energy spectrum has a discrete part, the bound states whose differences give atomic spectral lines, and a continuous part for scattering.

## Key concepts

| Term | Meaning |
|---|---|
| Spectrum σ(T) | The λ ∈ ℂ for which T − λI has no bounded inverse |
| Resolvent | R(λ) = (T − λI)⁻¹, holomorphic on the complement of σ(T) |
| Spectral radius | r(T) = max ∣λ∣ over σ(T) = lim ‖Tⁿ‖^(1/n) |
| Adjoint T∗ | The operator with ⟨Tx, y⟩ = ⟨x, T∗y⟩ |
| Self-adjoint | T = T∗; its spectrum is real |
| Compact operator | Maps bounded sets to relatively compact sets |
| Fredholm alternative | For compact T and λ ≠ 0, T − λ is invertible or has a kernel |
| Hilbert–Schmidt operator | An integral operator with square-integrable kernel |

## How it fits

- **Below:** the finite-dimensional [spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md) of 04 is the model; [Liouville's theorem](../02-complex-analysis/cauchys-theorem-and-its-consequences.md) and [Hahn–Banach](hahn-banach-and-baire-category.md) give non-emptiness; [Hilbert spaces](hilbert-spaces.md) give the orthonormal bases.
- **Above:** [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) in 14; [Sturm–Liouville theory](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md) and the [heat equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md) in 10; spectral gaps govern the mixing of [Markov chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md) in 11.
- **Siblings:** [Fourier series](../04-harmonic-analysis/fourier-series.md) are the eigenfunction expansion of d/dx on the circle; the [Fourier transform](../04-harmonic-analysis/the-fourier-transform.md) diagonalises every translation-invariant operator on ℝ, an example of continuous spectrum.

## Common misconceptions

- **"The spectrum is the set of eigenvalues"**: the right shift and multiplication by x have large spectra and no eigenvalues.
- **"Every compact operator has an eigenvector"**: the Volterra operator has none; self-adjointness is what guarantees them.
- **"Self-adjoint just means symmetric"**: for unbounded operators the domains must match exactly, a distinction with physical consequences.

## Go deeper

- Peter D. Lax, *Functional Analysis* (2002): spectral theory from compact operators to the general theorem.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (1972): the spectral theorem aimed at quantum mechanics.
- Elias M. Stein and Rami Shakarchi, *Real Analysis* (2005): compact operators and the spectral theorem in L².
