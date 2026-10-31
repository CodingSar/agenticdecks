# The Riemann Zeta Function

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Analytic Number Theory](README.md)
> **Builds on:** [Analytic Continuation and Riemann Surfaces](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md), [Singularities and Residues](../../09-advanced-analysis/02-complex-analysis/singularities-and-residues.md), [The Fourier Transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md), [Series](../../06-real-analysis/01-limits-and-convergence/series.md), [Primes and Unique Factorisation](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md)
> **Enables:** [The Prime Number Theorem](the-prime-number-theorem.md), [Primes in Arithmetic Progressions](primes-in-arithmetic-progressions.md), [Modular Forms](../04-elliptic-curves-and-modular-forms/modular-forms.md), [Open Problems](../../15-mathematics-in-context/open-problems.md), [High-Dimensional Geometry and Random Matrices](../../14-applied-and-computational-mathematics/06-data-and-learning/high-dimensional-geometry-and-random-matrices.md)

## Essence

The zeta function ζ(s) = ∑ 1/nˢ packages all the integers into one function, and Euler's product formula shows that it packages all the primes too. Riemann's paper of 1859 treated s as a complex variable, extended ζ to the whole plane, found a symmetry s ↔ 1 − s, and saw that the primes are controlled by the zeros of ζ. Each zero contributes one wave to the distribution of primes, and the size of those waves depends on how far the zeros lie from the line Re s = 1/2. The Riemann Hypothesis (RH), that all non-trivial zeros lie on that line, is open as of 2026 and is the most famous unsolved problem in mathematics.

## Core tenets

1. **The Euler product encodes unique factorisation.** For Re s > 1,

   ```
   ζ(s) = ∑_(n≥1) n^(−s) = ∏_p (1 − p^(−s))^(−1)
   ```

   because expanding each factor as a geometric series 1 + p^(−s) + p^(−2s) + ⋯ and multiplying produces every n^(−s) exactly once, by unique factorisation. As s → 1 the sum diverges like 1/(s − 1), so the product must have infinitely many factors: there are infinitely many primes. Taking logarithms gives ∑ 1/pˢ ≈ log(1/(s − 1)), so even ∑ 1/p diverges.

2. **ζ extends to the whole plane with one pole.** The series converges only for Re s > 1. The alternating version η(s) = ∑ (−1)ⁿ⁺¹n^(−s) = (1 − 2^(1−s))·ζ(s) converges for Re s > 0, which already continues ζ across the line Re s = 1 with a simple pole at s = 1 of residue 1. Riemann's method reaches everywhere: write π^(−s/2)Γ(s/2)ζ(s), with Γ the gamma function, as an integral of the theta function θ(x) = ∑_(n∈ℤ) e^(−πn²x) against x^(s/2), and use the identity θ(1/x) = √x·θ(x), which is Poisson summation applied to the Gaussian, the function that is its own Fourier transform.

3. **The functional equation is a symmetry about Re s = 1/2.** The completed function ξ(s) = π^(−s/2)Γ(s/2)ζ(s) satisfies ξ(s) = ξ(1 − s). The proof is the theta identity: splitting the integral at x = 1 and substituting x ↦ 1/x swaps the two halves. The factor π^(−s/2)Γ(s/2) is the contribution of the real place, the "prime at infinity", so ξ is a product over all places.

4. **The zeros come in two kinds.** Γ(s/2) has poles at s = 0, −2, −4, …, so ζ has trivial zeros at −2, −4, −6, …. The Euler product shows ζ(s) ≠ 0 for Re s > 1, and the functional equation reflects this to Re s < 0 apart from the trivial zeros. All other zeros, the non-trivial ones ρ, lie in the critical strip 0 ≤ Re s ≤ 1, symmetric about the real axis and about Re s = 1/2. Special values are rational multiples of powers of π or of Bernoulli numbers: ζ(2) = π²/6, ζ(0) = −1/2 and ζ(−1) = −1/12. The last is a value of the continuation, not a sum of the divergent series 1 + 2 + 3 + ⋯.

5. **The explicit formula: primes are a sum of waves over zeros.** Let Λ(n) = log p when n is a power of a prime p and 0 otherwise, and ψ(x) = ∑_(n≤x) Λ(n). For x > 1 not a prime power, von Mangoldt proved Riemann's formula in the form

   ```
   ψ(x) = x − ∑_ρ x^ρ/ρ − log(2π) − ½·log(1 − x^(−2))
   ```

   summed over non-trivial zeros in order of ∣Im ρ∣. The term x comes from the pole, each zero ρ = β + iγ gives an oscillation of size x^β, and the last term comes from the trivial zeros. The proof writes ψ(x) as a contour integral of −ζ′(s)/ζ(s)·xˢ/s and moves the contour left, collecting residues.

6. **The Riemann Hypothesis, and what is known.** RH states that every non-trivial zero has real part 1/2; it is open as of 2026 and is one of the Clay Millennium Prize Problems. Hardy proved in 1914 that infinitely many zeros lie on the line, Selberg in 1942 that a positive proportion do, and computations have checked that the first several trillion zeros do. RH is equivalent to π(x) = li(x) + O(√x·log x), where π(x) counts primes up to x and li(x) = ∫₂ˣ dt/log t: the primes are as regular as a random sequence can be.

7. **Why it is hard, and why it is believed.** No zero-free strip of the form Re s > 1 − δ is known for any δ > 0. The analogue for curves over finite fields is proved, by Weil in the 1940s and for all varieties by Deligne in 1974, where the zeros are eigenvalues of a Frobenius operator; the Hilbert–Pólya idea seeks such an operator for ζ. Montgomery's pair-correlation work and later computations show the zeros spaced like eigenvalues of large random Hermitian matrices, a heuristic but striking match. Many results are proved conditionally on RH or the Generalised Riemann Hypothesis (GRH) for Dirichlet L-functions; for example, under GRH Miller's primality test becomes deterministic and runs in polynomial time.

## Key concepts

| Term | Meaning |
|---|---|
| Euler product | ζ(s) = ∏ (1 − p^(−s))^(−1), unique factorisation analytically |
| Analytic continuation | The unique extension of ζ to ℂ minus the pole at 1 |
| Functional equation | ξ(s) = ξ(1 − s) for ξ(s) = π^(−s/2)Γ(s/2)ζ(s) |
| Critical strip | 0 ≤ Re s ≤ 1, containing all non-trivial zeros |
| Von Mangoldt function Λ(n) | log p on powers of p, zero elsewhere |
| Explicit formula | ψ(x) as x minus a sum over zeros |
| Riemann Hypothesis | All non-trivial zeros have real part 1/2; open as of 2026 |

## How it fits

- **Below:** [analytic continuation](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md) defines ζ beyond its series; [residues](../../09-advanced-analysis/02-complex-analysis/singularities-and-residues.md) give the explicit formula; the [Fourier transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md) gives Poisson summation.
- **Above:** RH heads the list of [open problems](../../15-mathematics-in-context/open-problems.md); the zeros' statistics match [random matrices](../../14-applied-and-computational-mathematics/06-data-and-learning/high-dimensional-geometry-and-random-matrices.md).
- **Siblings:** [the prime number theorem](the-prime-number-theorem.md) needs only that no zero lies on Re s = 1; [Dirichlet L-functions](primes-in-arithmetic-progressions.md) twist ζ by characters; [L-functions of modular forms](../04-elliptic-curves-and-modular-forms/modular-forms.md) and of [curves](../03-algebraic-geometry/algebraic-curves-and-riemann-roch.md) follow the same pattern.

## Common misconceptions

- **"ζ(−1) = −1/12 means 1 + 2 + 3 + ⋯ = −1/12"**: the series diverges; −1/12 is the value of the continued function.
- **"Numerical checks of trillions of zeros make RH nearly proved"**: phenomena in number theory can first appear at enormous heights, so evidence is not proof.
- **"RH is needed for the prime number theorem"**: the theorem needs only the absence of zeros on Re s = 1.

## Go deeper

- H. M. Edwards, *Riemann's Zeta Function* (1974): Riemann's paper, read line by line.
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function* (2nd edition, revised by D. R. Heath-Brown, 1986): the standard reference.
- Barry Mazur and William Stein, *Prime Numbers and the Riemann Hypothesis* (2016): a short, gentle and visual account.
