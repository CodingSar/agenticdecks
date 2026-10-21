# Fourier Analysis

> **Layer:** [01 Mathematical Foundations](../README.md) › [Continuous Mathematics](README.md)
> **Builds on:** [Calculus](calculus.md), [Linear Algebra](../04-algebra/linear-algebra.md), [Induction and Recurrences](../03-discrete-mathematics/induction-and-recurrences.md)
> **Enables:** [Sampling and Quantization](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md), [Digital Media and Compression](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md), [Divide and Conquer](../../05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md), [Convolutional Networks](../../13-artificial-intelligence/03-deep-learning/convolutional-networks.md), [Quantum Algorithms](../../02-theory-of-computation/05-quantum-computation/quantum-algorithms.md)

## Essence

Fourier analysis writes a signal (a sound wave, an image row, a list of numbers) as a sum of sinusoids, each with its own frequency, amplitude and phase. It is a change of basis: the same information in coordinates where many operations become simple. It matters because sinusoids are the eigenvectors of every linear, shift-invariant system, so filtering, blurring, echo and convolution, which mix neighbouring samples in time, become one independent multiplication per frequency. The Fast Fourier Transform (FFT) performs this change of basis in O(N log N) time instead of O(N²), which made it the workhorse of signal processing, compression, imaging and fast multiplication.

## Core tenets

1. **Sinusoids are the eigenfunctions of linear shift-invariant systems.** If a system is linear and delaying its input only delays its output, then the input e^(iωt) comes out as the same e^(iωt) times a complex number H(ω): a gain and a phase shift. That is the [eigenvector](../04-algebra/linear-algebra.md) relation Av = λv, so the frequency domain diagonalises such systems.

2. **The Fourier transform is a change to an orthogonal basis.** Complex exponentials of different frequencies are orthogonal, so each coefficient is simply the inner product of the signal with one basis function, an integral from [calculus](calculus.md). Periodic signals need discrete frequencies (a Fourier series); general signals need a continuum. Parseval's theorem says energy is preserved: nothing is lost by changing coordinates.

3. **Convolution in time is multiplication in frequency.** Convolution (f ∗ g)(t) = Σ f(τ)g(t − τ) slides one signal across another and sums products; every linear filter, blur and moving average is one. The convolution theorem says the transform of f ∗ g is the pointwise product of the transforms, so an O(N²) convolution becomes transform, multiply, inverse transform: O(N log N). Multiplying polynomials is convolving their coefficient lists, so the FFT also multiplies polynomials and large integers fast.

4. **The Discrete Fourier Transform (DFT) is the exact, finite version computers use.** For N samples, X_k = Σₙ xₙ·ω^(kn) with ω = e^(−2πi/N), a primitive N-th root of unity. It is multiplication by an N×N matrix that, scaled by 1/√N, is unitary. The DFT treats its input as one period of an infinite repetition, so the convolution it diagonalises is *circular*: data must be zero-padded for ordinary convolution, and a jump between the last and first sample appears as spurious high frequencies.

5. **The FFT is divide and conquer on roots of unity.** Split the sum into even- and odd-indexed samples. Each half is a DFT of size N/2, because ω² is a primitive (N/2)-th root of unity, and the halves combine with O(N) work. The recurrence T(N) = 2T(N/2) + O(N) gives O(N log N) ([recurrences](../03-discrete-mathematics/induction-and-recurrences.md)). Cooley and Tukey published it in 1965; Gauss had the idea around 1805. FFT-based methods multiply n-bit integers in nearly linear time (Schönhage and Strassen, 1971), and O(n log n) is now known to suffice (Harvey and van der Hoeven, 2021).

6. **Sampling makes the spectrum periodic, so sampling too slowly aliases.** Sampling at rate f_s copies a signal's spectrum at every multiple of f_s. Frequencies above f_s/2 (the Nyquist frequency) overlap the copies and masquerade as low ones. Hence the sampling theorem: a signal band-limited below B hertz is exactly recoverable from more than 2B samples per second. Audio CDs sample at 44.1 kHz to cover hearing up to about 20 kHz, after a filter removes higher frequencies ([sampling](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md)). Jagged edges and moiré in [rendered images](../../14-human-and-visual-computing/02-computer-graphics/rasterization-pipeline.md) are aliasing in space.

7. **Time and frequency resolution trade off.** A signal cannot be sharply localised in both: a short click has a broad spectrum, and a pure tone must last. Analysing a finite window smears each frequency into neighbouring bins (spectral leakage); smooth window functions reduce it at some cost in resolution. Spectrograms and wavelets pick different points on this trade-off.

8. **Natural signals concentrate energy in few coefficients, which lossy compression exploits.** Images and sounds are mostly smooth, so most energy sits in low frequencies and most high-frequency coefficients are tiny. Codecs use the Discrete Cosine Transform (DCT), a real-valued cousin of the DFT that avoids the circular-boundary jump: JPEG on 8×8 blocks, MP3 in a modified form. They quantise small or imperceptible coefficients coarsely and entropy-code the rest ([media compression](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md), [source coding](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md)).

## Key concepts

| Term | Meaning |
|---|---|
| DFT | Exact transform of N samples into N frequency coefficients |
| FFT | O(N log N) algorithm computing the DFT |
| Convolution | Sliding weighted sum of one signal against another |
| Root of unity | Complex ω with ω^N = 1; the DFT matrix entries |
| Nyquist frequency | Half the sampling rate; highest frequency representable without aliasing |
| Aliasing | High frequencies appearing as low ones after undersampling |
| Spectral leakage | Smearing of frequencies caused by a finite analysis window |
| DCT | Real-valued Fourier-type transform used by codecs |

## How it fits

- **Below:** A unitary change of basis from [linear algebra](../04-algebra/linear-algebra.md), computed with the integrals and complex exponentials of [calculus](calculus.md); the FFT's cost is a divide-and-conquer [recurrence](../03-discrete-mathematics/induction-and-recurrences.md).
- **Above:** [Sampling](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md) and [wireless links](../../08-networking/02-link-layer/wireless-networks.md) (orthogonal frequency-division multiplexing is an FFT) are designed in frequency terms. [Media codecs](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md) and [computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md) filter in transformed coordinates. [Convolutional networks](../../13-artificial-intelligence/03-deep-learning/convolutional-networks.md) learn convolutions. The FFT is the classic [divide-and-conquer](../../05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md) algorithm, and the [Quantum Fourier Transform](../../02-theory-of-computation/05-quantum-computation/quantum-algorithms.md) behind Shor's algorithm is the DFT applied to amplitudes.
- **Siblings:** [Calculus](calculus.md) supplies integrals, series and complex exponentials. [Optimization](optimization.md) meets Fourier analysis in filter design and deconvolution, least-squares problems that decouple frequency by frequency.

## Common misconceptions

- **"The FFT approximates the Fourier transform."** It computes the DFT exactly (up to rounding), just faster. Approximation enters only when a finite DFT stands in for a continuous transform.
- **"Sampling at twice the highest frequency of interest is enough."** Only if nothing above half the sampling rate reaches the sampler; otherwise it aliases into the band.
- **"Frequency is a property of an instant."** Frequency is defined over an interval; exact time and exact frequency together run into the trade-off of tenet 7.

## Go deeper

- Alan Oppenheim and Ronald Schafer, *Discrete-Time Signal Processing* (3rd ed., 2010): the DFT, FFT, sampling and filtering in depth.
- James Cooley and John Tukey, "An Algorithm for the Machine Calculation of Complex Fourier Series" (1965): the paper that made the FFT standard.
- Thomas Cormen, Charles Leiserson, Ronald Rivest and Clifford Stein, *Introduction to Algorithms* (4th ed., 2022), chapter 30: the FFT for polynomial multiplication.
