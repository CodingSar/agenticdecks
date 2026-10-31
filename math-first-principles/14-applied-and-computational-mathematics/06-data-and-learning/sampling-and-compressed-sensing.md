# Sampling and Compressed Sensing

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Data and Learning](README.md)
> **Builds on:** [The Fourier Transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md), [Fourier Series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md), [Linear Systems and Rank–Nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md), [Linear Programming](../02-optimisation/linear-programming.md), [High-Dimensional Geometry and Random Matrices](high-dimensional-geometry-and-random-matrices.md)
> **Enables:** [Sampling and Quantization (CS)](../../../cs-first-principles/00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md), [Digital Media and Compression (CS)](../../../cs-first-principles/14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md), [Error-Correcting Codes](../03-information-codes-and-cryptography/error-correcting-codes.md)

## Essence

A continuous signal has infinitely many values, yet a digital device stores only finitely many samples. The sampling theorem says when nothing is lost: a signal containing no frequencies above B is determined by its values at 2B equally spaced points per second. Compressed sensing, developed by Emmanuel Candès, Justin Romberg and Terence Tao and by David Donoho in 2006, replaces "few frequencies" by the weaker and more common assumption "few nonzero coefficients in some basis". It shows that a sparse vector of length N can be recovered from far fewer than N random linear measurements, by an efficient convex programme: minimise the ℓ¹ norm, the sum of absolute values. Both trade a structural assumption for fewer measurements.

## Core tenets

1. **A band-limited signal is determined by samples at twice its top frequency.** Suppose the Fourier transform f̂ vanishes outside [−B, B]. Then

   ```
   f(t) = ∑ₙ f(n/(2B)) · sinc(2Bt − n),      sinc(x) = sin(πx)/(πx)
   ```

   Proof idea: repeat f̂ periodically with period 2B. The copies do not overlap, so f̂ is recovered by cutting out one period. The Fourier coefficients of the periodic function are, by Poisson summation, the samples f(n/(2B)), and transforming back the cut-off turns each into a sinc. Claude Shannon gave this proof in 1949; Edmund Whittaker, Harry Nyquist and Vladimir Kotelnikov had earlier versions.

2. **Sampling too slowly causes aliasing, which no processing can undo.** If samples are taken at a rate below 2B, the periodised copies of f̂ overlap and a frequency ν becomes indistinguishable from ν minus the sampling rate. This is why a filmed wheel can seem to turn backwards. Engineers filter out high frequencies before sampling; compact disc audio samples at 44,100 per second to capture hearing up to about 20,000 hertz.

3. **Sparsity, not bandwidth, is what most signals have.** A vector x in ℝ^N is s-sparse if at most s entries are nonzero. Photographs are nearly sparse in wavelet bases, which is why image compression works: most coefficients can be discarded. Measure y = Ax with an m × N matrix A and m much smaller than N. Every s-sparse x is determined by y if and only if every 2s columns of A are linearly independent, since two s-sparse solutions differ by a 2s-sparse vector in the kernel. So m = 2s measurements can suffice in principle. But searching for the sparsest solution is NP-hard in general: it means trying all supports.

4. **Minimising the ℓ¹ norm finds sparse solutions efficiently.** Basis pursuit solves: minimise ∣z∣₁ = ∑ ∣zᵢ∣ subject to Az = y. Writing z = u − v with u, v ≥ 0 makes this a linear programme. Geometrically, the ℓ¹ ball is a cross-polytope whose corners lie on the axes, so the smallest one touching the solution space typically touches it at a low-dimensional face, a sparse point. Minimising the Euclidean norm instead touches a round ball at a generic, dense point.

5. **The null space property is the exact condition for ℓ¹ recovery.** Basis pursuit recovers every s-sparse x if and only if every nonzero h in the kernel of A satisfies ∣h_S∣₁ < ∣h_T∣₁ whenever S has s indices and T is its complement. Proof: if x is supported on S and x + h is feasible, then ∣x + h∣₁ ≥ ∣x∣₁ − ∣h_S∣₁ + ∣h_T∣₁ > ∣x∣₁, so x is the unique minimiser; conversely, a kernel vector violating the inequality makes −h_S and h_T two solutions with the wrong one shorter.

6. **The restricted isometry property gives stable recovery, and random matrices have it.** A satisfies the restricted isometry property (RIP) of order k with constant δ if (1 − δ)∣x∣² ≤ ∣Ax∣² ≤ (1 + δ)∣x∣² for every k-sparse x: it acts almost as an isometry on sparse vectors. Candès (2008) showed that δ < √2 − 1 at order 2s implies exact recovery of s-sparse vectors and, with noisy data, error proportional to the noise plus the best s-term approximation error. A Gaussian random matrix has this property with high probability once m ≥ C·s·log(N/s): concentration controls each fixed set of s columns, as in the Johnson–Lindenstrauss lemma, and a union bound covers the at most (eN/s)^s choices of support.

7. **The ideas extend from vectors to matrices and reach the clinic.** A low-rank matrix can be completed from a small random subset of its entries by minimising the nuclear norm, the sum of singular values, which plays the role of ℓ¹ for rank (Candès and Recht, 2009). Magnetic resonance imaging (MRI) measures Fourier coefficients one at a time, so fewer measurements mean shorter scans; compressed sensing reconstruction is now used in clinical scanners.

## Key concepts

| Term | Meaning |
|---|---|
| Band-limited | Having Fourier transform zero outside a bounded interval [−B, B] |
| Nyquist rate | The minimal sampling rate 2B for a signal band-limited to B |
| Aliasing | High frequencies masquerading as low ones after undersampling |
| s-sparse | Having at most s nonzero entries |
| Basis pursuit | Minimise the ℓ¹ norm subject to the measurement equations |
| Null space property | Kernel vectors are never concentrated on s coordinates; equivalent to ℓ¹ recovery |
| Restricted isometry property | Near-preservation of length for all sparse vectors |
| Nuclear norm | Sum of singular values; the convex proxy for rank |

## How it fits

- **Below:** Fourier series and the Fourier transform give the sampling theorem; rank–nullity explains why sparsity is needed; linear programming solves basis pursuit; concentration of measure makes random matrices satisfy RIP.
- **Above:** the computing tree's [sampling and quantization](../../../cs-first-principles/00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md) and [digital media](../../../cs-first-principles/14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md) leaves carry these ideas into engineering.
- **Siblings:** [high-dimensional geometry](high-dimensional-geometry-and-random-matrices.md) supplies the probabilistic tools; [statistical learning theory](statistical-learning-theory.md) meets sparsity in the lasso, ℓ¹-penalised regression; [error-correcting codes](../03-information-codes-and-cryptography/error-correcting-codes.md) solve the finite-field analogue, recovering a sparse error from a syndrome.

## Common misconceptions

- **"The sampling theorem applies to any signal."** It needs a hard bandwidth limit; real signals must be filtered first, or aliasing corrupts them irreversibly.
- **"Compressed sensing gets something for nothing."** It works only for signals that are sparse in a known basis, and the number of measurements still grows with the sparsity.
- **"ℓ¹ minimisation always gives the sparsest solution."** Only under conditions like the null space property; for badly designed A it can fail.

## Go deeper

- S. Foucart and H. Rauhut, *A Mathematical Introduction to Compressive Sensing* (2013): the standard text, with full proofs.
- S. Mallat, *A Wavelet Tour of Signal Processing* (3rd ed., 2009): sampling, wavelets and sparse representations.
- D. L. Donoho, "Compressed Sensing" (2006): one of the two founding papers.
