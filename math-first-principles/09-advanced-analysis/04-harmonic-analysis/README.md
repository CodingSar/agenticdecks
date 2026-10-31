# Harmonic Analysis

> **Layer:** [09 Advanced Analysis](../README.md) › Harmonic Analysis
> **Children:** [Fourier Series](fourier-series.md) · [The Fourier Transform](the-fourier-transform.md) · [Distributions](distributions.md) · [Fourier Analysis on Groups](fourier-analysis-on-groups.md)

## What this area is about

Harmonic analysis decomposes functions into oscillations. A sound is a sum of pitches, a periodic temperature profile a sum of sine waves, an image a sum of spatial frequencies. The decomposition matters because the operations that commute with translation, such as filtering, smoothing, differentiation and the evolution of linear differential equations with constant coefficients, act on each frequency separately by multiplication. Turning a function into its frequencies therefore turns calculus into algebra.

The subject began with Fourier's 1822 theory of heat and became a driving force of analysis. The question of when a Fourier series converges led Cantor to set theory, Lebesgue to his integral, and Hilbert and Riesz to the spaces of functional analysis. The Fourier transform on the line brought Plancherel's theorem and the uncertainty principle; distributions extended it to the Dirac delta; and the realisation that only the group structure matters carried it to finite groups, number theory and fast algorithms.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Fourier Series](fourier-series.md) | Periodic functions as sums of e^(inx); the convergence problem | Hilbert spaces, Lᵖ, uniform boundedness |
| [The Fourier Transform](the-fourier-transform.md) | Functions on ℝ; convolution, Plancherel, uncertainty | Fourier series, Lebesgue integral |
| [Distributions](distributions.md) | Generalised functions: δ, weak derivatives, fundamental solutions | Fourier transform, duality |
| [Fourier Analysis on Groups](fourier-analysis-on-groups.md) | Characters, Pontryagin duality, the Fast Fourier Transform | Series, transform, group theory |

```
                  Fourier series  (on 𝕋)
                   │            │
                   ▼            ▼
      Fourier transform ──►  Fourier analysis on groups
          (on ℝ)               (𝕋, ℝ, ℤ/n: one theory)
             │
             ▼
        distributions
     (δ, weak derivatives)
```

[Fourier series](fourier-series.md) come first: the circle is compact, its frequencies are the integers, and L² theory gives a complete answer, while pointwise convergence gives a hard one that ended only with Carleson's theorem in 1966. [The Fourier transform](the-fourier-transform.md) replaces the circle by the line and the integers by a continuum of frequencies; Plancherel's theorem and the uncertainty principle are its central facts. [Distributions](distributions.md) enlarge the domain of the transform and of differentiation until both apply to everything one meets in practice, including δ, and so provide the language for weak solutions of differential equations. [Fourier analysis on groups](fourier-analysis-on-groups.md) explains why all of this works: the circle, the line and the cyclic groups are locally compact abelian groups, and Pontryagin duality is the single theorem behind series, transform and Discrete Fourier Transform alike.

## Connections to sibling areas

- **[Measure and Integration](../01-measure-and-integration/README.md):** Fourier coefficients are Lebesgue integrals, the convergence theorems need Lᵖ, and Haar measure is the invariant measure that general harmonic analysis integrates against.
- **[Complex Analysis](../02-complex-analysis/README.md):** a Fourier series is a Laurent series on the unit circle, transforms are evaluated by residues, and compactly supported functions have entire transforms.
- **[Functional Analysis](../03-functional-analysis/README.md):** L² theory is Hilbert-space theory, divergence of Fourier series is uniform boundedness, distributions are a dual space, and the transform diagonalises translation-invariant operators as the spectral theorem diagonalises self-adjoint ones.

## Connections across layers

Harmonic analysis builds on the [exponential and trigonometric functions](../../06-real-analysis/02-calculus-of-one-variable/the-exponential-and-trigonometric-functions.md) and [uniform convergence](../../06-real-analysis/01-limits-and-convergence/uniform-convergence.md) of 06, on [group representations](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md) of 05 and on [modular arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md) of 02. Upward, it solves the [heat](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md) and [wave](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-wave-equation.md) equations and underlies [weak solutions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md) in 10; it proves the [central limit theorem](../../11-probability-and-statistics/02-limit-theorems/the-central-limit-theorem.md) in 11; it gives Dirichlet's theorem on [primes in progressions](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/primes-in-arithmetic-progressions.md) and part of the [Langlands programme](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/the-langlands-programme.md) in 12; and it supports [sampling](../../14-applied-and-computational-mathematics/06-data-and-learning/sampling-and-compressed-sensing.md), [codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md) and [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) in 14. In the sibling trees it reappears as [Fourier analysis for computing](../../../cs-first-principles/01-mathematical-foundations/05-continuous-mathematics/fourier-analysis.md) and in [magnetic resonance imaging](../../../medicine-first-principles/11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/magnetic-resonance-imaging.md).

## Cross-cutting threads

- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): every function splits into characters, as every vector splits into eigenvectors.
- [Duality](../../CROSS-CUTTING.md#duality): Pontryagin duality pairs a group with its frequencies, and the transform exchanges smoothness with decay.
- [Symmetry](../../CROSS-CUTTING.md#symmetry): characters are the functions that transform simply under translation.
- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): when partial sums converge, and in which sense, is the founding question.
- [Linearisation](../../CROSS-CUTTING.md#linearisation): the transform turns linear differential equations with constant coefficients into multiplication.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): the same theorem serves heat flow, primes, codes and medical imaging.
