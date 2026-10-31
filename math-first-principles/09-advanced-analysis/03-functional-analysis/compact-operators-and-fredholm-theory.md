# Compact Operators and Fredholm Theory

> **Layer:** [09 Advanced Analysis](../README.md) › [Functional Analysis](README.md)
> **Builds on:** [Spectral Theory](spectral-theory.md), [Banach Spaces](banach-spaces.md), [Hilbert Spaces](hilbert-spaces.md), [Hahn–Banach and Baire Category](hahn-banach-and-baire-category.md), [Compactness in Metric Spaces](../../06-real-analysis/03-metric-spaces/compactness-in-metric-spaces.md)
> **Enables:** [Boundary Value Problems and Sturm–Liouville Theory](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md), [Weak Solutions and Sobolev Spaces](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md), [Laplace's Equation and Harmonic Functions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md), [The Mathematics of Quantum Mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md)

## Essence

Ivar Fredholm's 1903 paper on integral equations f(x) − ∫ k(x, y)·f(y) dy = g(x) found that they behave like square linear systems: either there is exactly one solution for every g, or the homogeneous equation has solutions, and then g must satisfy finitely many conditions. Frigyes Riesz isolated the reason: the integral operator is compact, close to finite rank, so the identity minus it is a matrix problem in disguise. Fredholm theory widens the class to operators that are invertible up to a compact error, and attaches to each one an integer, the index, which no compact or small perturbation can change. That integer is where analysis first meets topology.

## Core tenets

1. **Compact operators are the norm limits of finite-rank ones, on Hilbert space.** An operator K is compact if it maps the unit ball to a set with compact closure. A norm limit of finite-rank operators is compact, since a set within ε of a bounded finite-dimensional set is totally bounded. On a Hilbert space the converse holds: compose K with the orthogonal projection onto the span of its first n singular vectors. On general Banach spaces it fails; Per Enflo (1973) built a separable Banach space without this approximation property.

2. **Integral operators with continuous kernels are compact.** If k is continuous on [a, b]², then K maps the unit ball of C[a, b] to a bounded family whose members all share the modulus of continuity of k, so by the Arzelà–Ascoli theorem its closure is compact. On L² every kernel with ∫∫ ∣k∣² < ∞ gives a compact Hilbert–Schmidt operator, being the limit of the finite-rank truncations of its expansion in an orthonormal basis. Inverses of elliptic differential operators are of this kind, which is how compactness enters differential equations.

3. **I − K has finite-dimensional kernel and closed range.** On the kernel of I − K the operator K is the identity, so the unit ball of the kernel is the image of a bounded set under K and is compact; by Riesz's lemma the kernel is finite-dimensional. A similar subsequence argument shows the range is closed. Applying this to K − λ for λ ≠ 0 gives the picture of [spectral theory](spectral-theory.md): non-zero spectrum consists of eigenvalues of finite multiplicity accumulating only at 0.

4. **The Fredholm alternative: injective implies surjective.** For compact K, I − K is one-to-one if and only if it is onto, and the dimension of its kernel equals that of the kernel of I − K∗. Juliusz Schauder showed that K∗ is compact when K is. Proof idea: the range is closed, so it is the annihilator of the kernel of the adjoint (a consequence of [Hahn–Banach](hahn-banach-and-baire-category.md)); the equality of dimensions then follows from tenet 6, since I − tK for t from 0 to 1 joins I − K to the identity.

5. **Fredholm operators and the index.** A bounded operator T is Fredholm if its kernel and cokernel, the quotient of the target by the range, are finite-dimensional. Its index is ind T = dim ker T − dim coker T. On ℂⁿ every operator has index n − n = 0, by rank–nullity. In infinite dimensions the right shift S(x₁, x₂, …) = (0, x₁, x₂, …) on ℓ² is injective with range of codimension 1, so ind S = −1; its adjoint, the left shift, has index +1. Index is additive under composition, so Sⁿ has index −n.

6. **The index is a homotopy invariant.** Fredholm operators form an open set, and the index is constant on its connected components: it is unchanged by adding a compact operator or one of small norm. Proof idea: a perturbation of T can be split into a part that acts on a finite-dimensional complement of the kernel and a part that is invertible, and on finite-dimensional pieces the index reduces to rank–nullity. So I − K, joined to I through I − tK, has index 0, which is tenet 4.

7. **Atkinson's theorem: Fredholm means invertible modulo compacts.** Frederick Atkinson (1951) proved T is Fredholm exactly when there is an S with ST − I and TS − I compact. Compact operators form a closed two-sided ideal, and the quotient algebra, the Calkin algebra, sees Fredholm operators as its invertible elements. On a separable Hilbert space two Fredholm operators lie in the same component if and only if they have the same index.

8. **Indices count topology.** For a continuous non-vanishing function φ on the circle, the Toeplitz operator that multiplies by φ and projects back onto the Hardy space of functions with only non-negative Fourier coefficients is Fredholm, with index equal to minus the winding number of φ about 0. Elliptic differential operators on compact manifolds are Fredholm, by Rellich's compact embedding of Sobolev spaces, and the Atiyah–Singer index theorem, announced in 1963, computes their index from topology alone; the Gauss–Bonnet and Riemann–Roch theorems are special cases.

## Key concepts

| Term | Meaning |
|---|---|
| Compact operator | Maps bounded sets to sets with compact closure |
| Finite-rank operator | An operator with finite-dimensional range |
| Hilbert–Schmidt operator | Integral operator on L² with square-integrable kernel; always compact |
| Fredholm alternative | For compact K, I − K is injective if and only if it is surjective |
| Fredholm operator | Bounded operator with finite-dimensional kernel and cokernel |
| Index | dim ker T − dim coker T, stable under compact and small perturbations |
| Calkin algebra | Bounded operators modulo compact ones on a Hilbert space |

## How it fits

- **Below:** [compactness](../../06-real-analysis/03-metric-spaces/compactness-in-metric-spaces.md) and Arzelà–Ascoli from 06 supply the examples; [Banach spaces](banach-spaces.md) explain why compactness must be put into the operator rather than the ball; rank–nullity from 04 is the finite-dimensional index.
- **Above:** [Sturm–Liouville theory](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md) and [weak solutions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md) use the Fredholm alternative to decide when boundary value problems are solvable; [potential theory](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md) reduces the Dirichlet problem to a Fredholm integral equation, Fredholm's original aim; [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) uses compact resolvents for discrete energy levels.
- **Siblings:** [spectral theory](spectral-theory.md) gives compact self-adjoint operators their eigenbasis; [Hilbert spaces](hilbert-spaces.md) make every compact operator approximable; the Toeplitz index lives on the circle of [Fourier series](../04-harmonic-analysis/fourier-series.md).

## Common misconceptions

- **"The identity is compact, being as simple as an operator can be"**: in infinite dimensions the unit ball is not compact, so the identity is the standard non-compact operator.
- **"An injective operator from a space to itself is onto"**: true for I − K with K compact and in finite dimensions, false in general; the right shift is injective with index −1.
- **"The index is a property of one equation"**: it is an invariant of a whole connected family of operators, which is why topology can compute it.

## Go deeper

- Peter D. Lax, *Functional Analysis* (2002): Riesz–Schauder theory, Fredholm operators and the index, with applications.
- Haim Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations* (2011): compact operators and the Fredholm alternative, applied to elliptic problems.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (1972): compact operators, Hilbert–Schmidt and trace class.
