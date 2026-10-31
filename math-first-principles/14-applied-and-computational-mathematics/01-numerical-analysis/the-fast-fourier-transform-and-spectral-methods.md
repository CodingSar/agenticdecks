# The Fast Fourier Transform and Spectral Methods

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Numerical Analysis](README.md)
> **Builds on:** [Fourier Series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md), [Fourier Analysis on Groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md), [Interpolation and Approximation](interpolation-and-approximation.md), [Numerical Linear Algebra](numerical-linear-algebra.md)
> **Enables:** [Numerical Methods for Differential Equations](numerical-methods-for-differential-equations.md), [Error-Correcting Codes](../03-information-codes-and-cryptography/error-correcting-codes.md), [Cryptography](../03-information-codes-and-cryptography/cryptography.md), [Sampling and Compressed Sensing](../06-data-and-learning/sampling-and-compressed-sensing.md)

## Essence

The Discrete Fourier Transform (DFT) turns n samples of a signal into n frequency coefficients. Done directly it costs n² operations; the Fast Fourier Transform (FFT) needs O(n log n), which made Fourier analysis a routine computation. Two consequences dominate. Convolution becomes pointwise multiplication, so filtering, polynomial multiplication and translation-invariant linear systems become fast. And smooth functions can be differentiated and integrated through their Fourier or Chebyshev coefficients with errors that fall faster than any power of the grid spacing: these are spectral methods.

## Core tenets

1. **The DFT is a unitary matrix, up to scale.** With ω = e^(−2πi/n), the DFT of a vector f is Ff, where F has entries ω^(jk) for j, k = 0, …, n − 1. Its rows are sampled characters of the cyclic group of order n, which are orthogonal, so FᴴF = nI, where Fᴴ is the conjugate transpose. Because F/√n is unitary, the transform is perfectly conditioned.

2. **The FFT factors F into log₂ n sparse stages.** For n = 2m, splitting f into even and odd entries writes a DFT of length n as two of length m combined by n further operations, so the cost T(n) = 2T(m) + O(n) gives O(n log n). James Cooley and John Tukey published the algorithm in 1965; Carl Friedrich Gauss had used the idea around 1805, in work printed only after his death. In floating point the computed transform has relative error of order u log n, where u is the unit roundoff, smaller than the order u·n bound for summing the definition directly.

3. **The DFT diagonalises every circulant matrix, so cyclic convolution is pointwise multiplication.** A circulant matrix C has each row the previous one shifted cyclically, so Cx is the cyclic convolution c ∗ x of its first column with x. Each character is an eigenvector of every shift, hence of C, and so C = F⁻¹ diag(Fc) F. Solving Cx = b takes three FFTs. Multiplying two polynomials of degree below n is a convolution of their coefficient vectors, padded to length 2n, and integer multiplication follows: Arnold Schönhage and Volker Strassen (1971) reached O(n log n log log n) bit operations, and David Harvey and Joris van der Hoeven reached O(n log n) in 2019.

4. **On a grid, frequencies alias.** On the n points xⱼ = 2πj/n, the modes e^(ikx) and e^(i(k + n)x) take identical values, so a grid sees only n distinct frequencies. The DFT therefore gives the coefficients of the trigonometric interpolant of degree about n/2, and every higher frequency is folded onto a lower one: the aliasing of the sampling theorem.

5. **Spectral differentiation converges faster than any fixed order.** To differentiate a periodic function from its samples, take the DFT, multiply coefficient k by ik, and invert. The error equals the error of the trigonometric interpolant, which for an analytic periodic function falls geometrically in n. For u = e^(sin x) with n = 32 points the maximum error in u′ is about 3 × 10⁻¹⁵, against 0.026 for second-order centred differences and 1.1 × 10⁻³ for fourth-order ones. A stencil of order p errs like hᵖ; the spectral derivative uses all n points, and for infinitely differentiable u its error falls faster than any power of 1/n.

6. **Chebyshev points carry spectral accuracy to non-periodic problems.** Under x = cos θ a function on [−1, 1] becomes an even periodic function of θ, and its Chebyshev coefficients are its Fourier cosine coefficients. Values at the Chebyshev extreme points cos(πj/n) are therefore converted to Chebyshev coefficients by one fast cosine transform. Clenshaw–Curtis quadrature (Charles Clenshaw and Alan Curtis, 1960) integrates the interpolant this way, and Chebyshev spectral methods solve smooth boundary-value problems on intervals to near machine precision with a few dozen points.

7. **Discontinuities destroy spectral accuracy.** Truncated Fourier series of a function with a jump overshoot near it by about 9% of the jump however many terms are kept, the Gibbs phenomenon, and converge only like 1/n away from it. Spectral methods are therefore used for smooth solutions, as in turbulence simulation and global weather models, while shocks call for local methods.

8. **The same algorithm works over finite fields.** If n divides p − 1 for a prime p, the field 𝔽_p contains a primitive n-th root of unity, and the FFT with it, the number-theoretic transform, computes exact cyclic convolutions with no rounding at all. Exact big-integer arithmetic and lattice-based cryptography use it, and Reed–Solomon encoding is a DFT of this kind.

## Key concepts

| Term | Meaning |
|---|---|
| Discrete Fourier transform | Multiplication by the n × n matrix with entries ω^(jk) |
| Fast Fourier transform | Any O(n log n) algorithm for the DFT, usually by recursive splitting |
| Circulant matrix | A matrix whose rows are cyclic shifts of the first; diagonalised by the DFT |
| Aliasing | Frequencies differing by a multiple of n are identical on an n-point grid |
| Spectral accuracy | Error falling faster than any power of 1/n for smooth data |
| Gibbs phenomenon | The persistent overshoot of truncated Fourier series at a jump |
| Number-theoretic transform | The DFT over a finite field, exact and free of rounding |

## How it fits

- **Below:** [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md) supply the convergence theory and the Gibbs phenomenon; [Fourier analysis on groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md) explains why characters diagonalise shifts; roots of unity in [finite fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md) give the exact version.
- **Above:** [error-correcting codes](../03-information-codes-and-cryptography/error-correcting-codes.md) and lattice [cryptography](../03-information-codes-and-cryptography/cryptography.md) use transforms over finite fields; [sampling theory](../06-data-and-learning/sampling-and-compressed-sensing.md) and magnetic resonance imaging reconstruct signals from Fourier data; the computing tree treats the FFT as a model [divide-and-conquer](../../../cs-first-principles/05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md) algorithm.
- **Siblings:** spectral accuracy is [interpolation](interpolation-and-approximation.md) at well-chosen nodes; circulant solves and fast preconditioners belong to [numerical linear algebra](numerical-linear-algebra.md); spectral methods compete with finite differences and finite elements in [numerical methods for differential equations](numerical-methods-for-differential-equations.md), where von Neumann's stability analysis is also a DFT.

## Common misconceptions

- **"The FFT approximates the Fourier transform"**: it computes the DFT exactly, up to rounding; approximation enters when a continuous signal is sampled or truncated.
- **"The FFT needs n to be a power of two"**: mixed-radix and prime-length algorithms give O(n log n) for every n.

## Go deeper

- Lloyd N. Trefethen, *Spectral Methods in MATLAB* (2000): short programs that show spectral accuracy at work.
- John P. Boyd, *Chebyshev and Fourier Spectral Methods* (2nd edition, 2001): a comprehensive practical guide.
- William L. Briggs and Van Emden Henson, *The DFT: An Owner's Manual for the Discrete Fourier Transform* (1995): sampling, aliasing and the FFT.
