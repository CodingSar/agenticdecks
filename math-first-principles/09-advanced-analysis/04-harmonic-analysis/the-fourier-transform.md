# The Fourier Transform

> **Layer:** [09 Advanced Analysis](../README.md) › [Harmonic Analysis](README.md)
> **Builds on:** [Fourier Series](fourier-series.md), [The Lebesgue Integral](../01-measure-and-integration/the-lebesgue-integral.md), [Lᵖ Spaces](../01-measure-and-integration/lp-spaces.md), [Hilbert Spaces](../03-functional-analysis/hilbert-spaces.md)
> **Enables:** [Distributions](distributions.md), [The Central Limit Theorem](../../11-probability-and-statistics/02-limit-theorems/the-central-limit-theorem.md), [The Heat Equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md), [Sampling and Compressed Sensing](../../14-applied-and-computational-mathematics/06-data-and-learning/sampling-and-compressed-sensing.md), [The Mathematics of Quantum Mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md)

## Essence

The Fourier transform is the Fourier series of a function on the whole line, where frequencies form a continuum instead of the integers. With the convention f̂(ξ) = ∫ f(x)·e^(−2πixξ) dx, it converts translation into multiplication by a phase, convolution into multiplication, and differentiation into multiplication by 2πiξ. So it diagonalises every linear operation that commutes with translation, turning differential equations with constant coefficients into algebra. On L² it is a unitary map, a rotation of function space that preserves energy, and it encodes a precise trade-off: a function and its transform cannot both be sharply concentrated.

## Core tenets

1. **The transform is defined on L¹ and its values decay.** For f ∈ L¹(ℝ) the integral converges absolutely, so f̂ is bounded by ‖f‖₁ and continuous by dominated convergence. The Riemann–Lebesgue lemma says f̂(ξ) → 0 as ∣ξ∣ → ∞: it holds for indicators of intervals by direct computation, and these are dense in L¹. The transform of an L¹ function need not be integrable: the indicator of [−½, ½] has transform sin(πξ)/(πξ), which is not in L¹.

2. **Convolution becomes multiplication.** The convolution (f ∗ g)(x) = ∫ f(x − y)·g(y) dy satisfies (f ∗ g)^ = f̂·ĝ, by Fubini's theorem and e^(−2πixξ) = e^(−2πi(x−y)ξ)·e^(−2πiyξ). Similarly, translating f by a multiplies f̂ by e^(−2πiaξ), and if f′ is integrable the transform of f′ is 2πiξ·f̂(ξ). The deeper reason is that the exponentials e^(2πixξ) are the joint eigenfunctions of all translations. Any operator that commutes with translations, such as a filter, a smoothing operator or a differential operator with constant coefficients, therefore acts on each frequency by multiplication.

3. **The Gaussian is its own transform, and this gives inversion.** The function e^(−πx²) satisfies ĝ = g: both satisfy the first-order equation y′ = −2πx·y, which differentiating under the integral sign shows, and both equal 1 at 0. Scaling it gives an approximate identity, and inserting it as a damping factor proves the inversion formula f(x) = ∫ f̂(ξ)·e^(2πixξ) dξ whenever f and f̂ are both integrable. In probability the same fact says the normal distribution is preserved under convolution after rescaling, the engine of the [central limit theorem](../../11-probability-and-statistics/02-limit-theorems/the-central-limit-theorem.md), proved through characteristic functions.

4. **Plancherel's theorem: the transform is unitary on L².** For f ∈ L¹ ∩ L², ‖f̂‖₂ = ‖f‖₂, proved by applying inversion to f ∗ f̃ with f̃(x) = conjugate of f(−x). Since L¹ ∩ L² is dense in L², the transform extends by continuity to a unitary map of L²(ℝ) onto itself, which Michel Plancherel established in 1910. The extension is not given by the integral, which need not converge for L² functions; it is the L² limit of transforms of truncations. This is the continuous analogue of the Parseval identity for [Fourier series](fourier-series.md).

5. **The uncertainty principle: concentration in x costs spread in ξ.** For f ∈ L² with ‖f‖₂ = 1,

   ```
   (∫ x² ∣f(x)∣² dx) · (∫ ξ² ∣f̂(ξ)∣² dξ) ≥ 1/(16π²)
   ```

   with equality exactly for Gaussians. Proof idea: integrate by parts to write 1 = ∫ ∣f∣² = −∫ x·(∣f∣²)′ dx, apply the Cauchy–Schwarz inequality, and use Plancherel to convert ∫ ∣f′∣² into 4π²·∫ ξ²∣f̂∣². In [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) position and momentum wavefunctions are Fourier transforms of each other, and this inequality is Heisenberg's uncertainty relation. A stronger qualitative statement: f and f̂ cannot both vanish outside bounded sets unless f = 0, because a compactly supported f has an entire transform, which cannot vanish on an interval without vanishing everywhere.

6. **Poisson summation and sampling connect the line to the circle and the integers.** For a well-behaved f, ∑ f(n) = ∑ f̂(k), both sums over the integers: periodising f and expanding in a Fourier series gives the identity. It proves the functional equation of the theta function and, through it, of the [Riemann zeta function](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md). Its engineering form is the sampling theorem: if f̂ vanishes outside [−B, B], then f is determined by its samples at spacing 1/(2B), and sampling more slowly folds high frequencies onto low ones, the aliasing discussed under [sampling and quantisation](../../../cs-first-principles/00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md).

7. **The transform solves equations and builds images.** The [heat equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md) uₜ = u_xx becomes ûₜ = −4π²ξ²·û, so û(ξ, t) = e^(−4π²ξ²t)·f̂(ξ), and the solution is convolution with a Gaussian of variance 2t. Magnetic Resonance Imaging (MRI) records samples of the two- or three-dimensional Fourier transform of the tissue's magnetisation and inverts it, as described in [magnetic resonance imaging](../../../medicine-first-principles/11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/magnetic-resonance-imaging.md). Computed Tomography (CT) rests on the projection-slice theorem: the one-dimensional transform of a projection of an image is a slice through its two-dimensional transform, as used in [radiography and computed tomography](../../../medicine-first-principles/11-clinical-method-and-diagnostics/03-imaging-and-physiological-measurement/radiography-and-computed-tomography.md).

## Key concepts

| Term | Meaning |
|---|---|
| Fourier transform | f̂(ξ) = ∫ f(x)·e^(−2πixξ) dx |
| Inversion formula | f(x) = ∫ f̂(ξ)·e^(2πixξ) dξ when both are integrable |
| Convolution | (f ∗ g)(x) = ∫ f(x − y)·g(y) dy; transformed to f̂·ĝ |
| Plancherel's theorem | ‖f̂‖₂ = ‖f‖₂; the transform is unitary on L² |
| Uncertainty principle | Spread in x times spread in ξ is at least 1/(16π²) |
| Poisson summation | ∑ f(n) = ∑ f̂(k) over the integers |
| Band-limited | f̂ vanishes outside a bounded interval |
| Characteristic function | The Fourier transform of a probability distribution |

## How it fits

- **Below:** [Fourier series](fourier-series.md) are the periodic case; the [Lebesgue integral](../01-measure-and-integration/the-lebesgue-integral.md) and [Lᵖ spaces](../01-measure-and-integration/lp-spaces.md) define it; [Hilbert spaces](../03-functional-analysis/hilbert-spaces.md) frame Plancherel.
- **Above:** constant-coefficient equations in 10; the [central limit theorem](../../11-probability-and-statistics/02-limit-theorems/the-central-limit-theorem.md) in 11; [compressed sensing](../../14-applied-and-computational-mathematics/06-data-and-learning/sampling-and-compressed-sensing.md) and quantum mechanics in 14; image compression, as in [digital media](../../../cs-first-principles/14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md).
- **Siblings:** [distributions](distributions.md) extend the transform to δ, constants and polynomials; [Fourier analysis on groups](fourier-analysis-on-groups.md) shows that ℝ is its own dual group; [residues](../02-complex-analysis/singularities-and-residues.md) compute many transforms.

## Common misconceptions

- **"The Fourier transform of an L² function is given by the integral"**: the integral may diverge; Plancherel defines the transform as a limit.
- **"A signal can be both time-limited and band-limited"**: only the zero signal is; real systems approximate one or the other.
- **"There is one Fourier transform"**: conventions differ by factors of 2π in the exponent and in front, and formulas change accordingly.

## Go deeper

- Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction* (2003): the transform on ℝ and ℝⁿ with applications.
- Thomas W. Körner, *Fourier Analysis* (1988): history, physics and probability around the transform.
- Robert S. Strichartz, *A Guide to Distribution Theory and Fourier Transforms* (1994): a quick, intuitive path to the general theory.
