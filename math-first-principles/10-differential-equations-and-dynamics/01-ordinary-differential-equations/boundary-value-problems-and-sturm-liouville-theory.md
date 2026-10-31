# Boundary Value Problems and Sturm–Liouville Theory

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Ordinary Differential Equations](README.md)
> **Builds on:** [Existence and uniqueness](existence-and-uniqueness.md), [The spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md), [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md), [Spectral theory](../../09-advanced-analysis/03-functional-analysis/spectral-theory.md), [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md)
> **Enables:** [The heat equation](../02-partial-differential-equations/the-heat-equation.md), [The wave equation](../02-partial-differential-equations/the-wave-equation.md), [The Euler–Lagrange equation](../03-calculus-of-variations/the-euler-lagrange-equation.md), [The mathematics of quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md)

## Essence

A boundary value problem (BVP) asks for a solution of a differential equation that meets conditions at both ends of an interval, like a string fixed at both ends. Unlike an initial value problem it may have no solution or infinitely many, depending on a parameter; the parameter values where non-zero solutions exist are eigenvalues. Sturm–Liouville theory, begun by Charles Sturm and Joseph Liouville in the 1830s, shows that for the symmetric operator −(py′)′ + qy these eigenvalues increase to infinity and the eigenfunctions form an orthonormal basis. It is the spectral theorem for a differential operator, and Fourier series are its simplest case.

## Core tenets

1. **Two-point problems can have no solution or many.** y″ + λy = 0 with y(0) = y(π) = 0 has the non-zero solutions sin nx exactly when λ = n², n = 1, 2, …, and only y ≡ 0 otherwise. At an eigenvalue the forced problem is delicate: y″ + y = 1 with the same conditions has no solution, because multiplying by sin x and integrating by parts turns the equation into 0 = ∫₀^π sin x dx = 2. This is the Fredholm alternative: either the homogeneous problem has only the zero solution and every forcing gives exactly one solution, or a solution exists only when the forcing is orthogonal to every homogeneous solution.

2. **Regular Sturm–Liouville theorem.** Let p be C¹ and positive, q continuous, and w continuous and positive on [a, b], and impose separated conditions α₁y(a) + α₂y′(a) = 0 and β₁y(b) + β₂y′(b) = 0, with (α₁, α₂) and (β₁, β₂) non-zero. Then −(py′)′ + qy = λwy has eigenvalues λ₁ < λ₂ < … → ∞, each with a one-dimensional eigenspace; the n-th eigenfunction has exactly n − 1 zeros in (a, b); and the normalised eigenfunctions form an orthonormal basis of L²(w), the square-integrable functions with inner product ⟨f, g⟩ = ∫ f·g·w dx.

3. **Symmetry makes eigenvalues real and eigenfunctions orthogonal.** For Ly = −(py′)′ + qy, integrating by parts twice gives Lagrange's identity

   ```
   ∫ from a to b of (Ly·z − y·Lz) dx  =  [ p·(y·z′ − y′·z) ] evaluated from a to b,
   ```

   and separated conditions make the right side vanish. The argument for symmetric matrices then applies: if Ly = λwy and Lz = μwz, then (λ − μ)·∫y·z·w = 0. Each eigenvalue is simple because the Wronskian p(yz′ − y′z) of two eigenfunctions is constant and vanishes at a, so they are proportional.

4. **Completeness comes from a compact inverse.** If 0 is not an eigenvalue (shift q by a constant if it is), Ly = f is solved by y(x) = ∫ G(x, s)·f(s) ds, with a continuous symmetric kernel G, the Green's function. That integral operator is compact and self-adjoint, and the spectral theorem for such operators gives an orthonormal basis of eigenfunctions with eigenvalues 1/λₙ → 0, which is the statement for L. The zero count comes from Sturm's comparison theorem: larger λ makes solutions oscillate faster, so each eigenvalue adds one zero.

5. **Singular problems give special functions and continuous spectrum.** When p vanishes at an endpoint or the interval is infinite, the theory survives with modified conditions and yields the special functions: Legendre's equation −((1 − x²)y′)′ = λy on [−1, 1], with bounded solutions, has eigenvalues n(n + 1) and polynomial eigenfunctions. On the whole line −y″ = λy has no square-integrable eigenfunctions; the spectrum is the continuous set [0, ∞), and the expansion becomes the [Fourier transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md).

6. **The lowest eigenvalue minimises the Rayleigh quotient.** For Dirichlet conditions y(a) = y(b) = 0, λ₁ is the minimum of R(y) = ∫(p·y′² + q·y²)/∫w·y² over y ≠ 0, attained by the first eigenfunction. Any trial function bounds it from above: for −y″ = λy on [0, 1], y = x(1 − x) gives R = (1/3)/(1/30) = 10, close to the true λ₁ = π² ≈ 9.87. Higher eigenvalues are min–max values of the same quotient, which is how finite elements estimate frequencies.

7. **Separation of variables reduces partial differential equations to these problems.** Seeking u = X(x)·T(t) for the heat equation uₜ = uₓₓ on [0, π], with u = 0 at both ends and initial value g, gives −X″ = λX with Dirichlet conditions, so

   ```
   u(x, t) = ∑ over n ≥ 1 of bₙ·e^(−n²t)·sin nx,   bₙ = (2/π)·∫ from 0 to π of g(x)·sin nx dx.
   ```

   Completeness guarantees that every initial temperature can be expanded. For the wave equation the same modes oscillate as cos nt and sin nt: the harmonics of a string.

## Key concepts

| Term | Meaning |
|---|---|
| Boundary value problem | A differential equation with conditions imposed at two or more points |
| Eigenvalue | A value of λ for which the homogeneous problem has a non-zero solution |
| Sturm–Liouville operator | Ly = −(py′)′ + qy, with weight w in the eigenproblem Ly = λwy |
| Self-adjoint | ⟨Ly, z⟩ = ⟨y, Lz⟩ for all functions meeting the boundary conditions |
| Green's function | The kernel G(x, s) of the integral operator that solves Ly = f |
| Fredholm alternative | Unique solvability for every forcing, or solvability only for forcing orthogonal to the homogeneous solutions |
| Rayleigh quotient | R(y) = ∫(p·y′² + q·y²)/∫w·y² |

## How it fits

- **Below:** the [spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md) for symmetric matrices, extended to compact self-adjoint operators on [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md) by [spectral theory](../../09-advanced-analysis/03-functional-analysis/spectral-theory.md); [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md) are the case p = w = 1, q = 0.
- **Above:** separation of variables for the [heat](../02-partial-differential-equations/the-heat-equation.md) and [wave](../02-partial-differential-equations/the-wave-equation.md) equations; energy levels in [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) are eigenvalues of −ψ″ + Vψ; minimising the Rayleigh quotient is a problem of the [calculus of variations](../03-calculus-of-variations/the-euler-lagrange-equation.md) whose Euler–Lagrange equation is the eigenvalue equation.
- **Siblings:** unlike the problems of [existence and uniqueness](existence-and-uniqueness.md), data at two ends do not determine a solution; [linear systems](linear-systems-and-the-matrix-exponential.md) diagonalise a matrix, this leaf diagonalises a differential operator.

## Common misconceptions

- **"Two conditions on a second-order equation always fix one solution."**: that holds for initial conditions at one point; at two points tenet 1 shows that none or infinitely many can occur.
- **"Eigenfunction expansions converge at every point."**: they converge in the L² sense; at a jump the partial sums overshoot by about 9% of the jump however many terms are taken (the Gibbs phenomenon).
- **"Orthogonality depends on the formulas for the eigenfunctions."**: it follows from the symmetry of the operator alone, which is why sines, Legendre polynomials and Bessel functions are orthogonal for one and the same reason.

## Go deeper

- Richard Courant and David Hilbert, *Methods of Mathematical Physics*, Volume I (1953): the classical source for eigenfunction expansions and the variational view of eigenvalues.
- Earl A. Coddington and Norman Levinson, *Theory of Ordinary Differential Equations* (1955): complete proofs for regular and singular problems.
- Walter A. Strauss, *Partial Differential Equations: An Introduction* (2nd edition): separation of variables and Fourier series at an introductory pace.
