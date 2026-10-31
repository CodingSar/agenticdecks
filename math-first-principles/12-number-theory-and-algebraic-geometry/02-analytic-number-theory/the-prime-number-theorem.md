# The Prime Number Theorem

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Analytic Number Theory](README.md)
> **Builds on:** [The Riemann Zeta Function](the-riemann-zeta-function.md), [Cauchy's Theorem and Its Consequences](../../09-advanced-analysis/02-complex-analysis/cauchys-theorem-and-its-consequences.md), [Singularities and Residues](../../09-advanced-analysis/02-complex-analysis/singularities-and-residues.md), [Primes and Unique Factorisation](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md)
> **Enables:** [Primes in Arithmetic Progressions](primes-in-arithmetic-progressions.md), [Sieves and Additive Problems](sieves-and-additive-problems.md), [Cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md), [Open Problems](../../15-mathematics-in-context/open-problems.md)

## Essence

The Prime Number Theorem (PNT) says that the number π(x) of primes up to x satisfies π(x) ∼ x/log x: near x, about one integer in log x is prime. Gauss and Legendre guessed it from tables around 1800; Hadamard and de la Vallée Poussin proved it independently in 1896 by following Riemann's plan. The proof turns counting primes into a contour integral of the zeta function, and the single fact that decides the matter is that ζ(s) has no zeros on the line Re s = 1. Elementary proofs, without complex analysis, came only in 1948–1949, from Selberg and Erdős.

## Core tenets

1. **Three equivalent forms.** With log the natural logarithm, li(x) = ∫₂ˣ dt/log t, and ψ(x) = ∑_(pᵏ≤x) log p, the statements

   ```
   π(x) ∼ x/log x        π(x) ∼ li(x)        ψ(x) ∼ x
   ```

   are equivalent, where f ∼ g means f/g → 1. Partial summation passes between them, since prime powers pᵏ with k ≥ 2 contribute only O(√x·log x) to ψ. The last form is the natural one: weighting each prime by log p makes the expected density exactly 1. As an approximation, li(x) is far better than x/log x.

2. **Chebyshev got the order of magnitude with binomial coefficients.** Around 1850 Chebyshev proved that π(x) lies between two constant multiples of x/log x, close to 1. The middle binomial coefficient (2n choose n) lies between 4ⁿ/(2n + 1) and 4ⁿ. It is divisible by every prime in (n, 2n], which gives the upper bound, and each prime power dividing it is at most 2n, which gives the lower bound. This method cannot reach the limit 1: it sees sizes, not cancellation.

3. **The analytic proof converts primes into an integral.** The logarithmic derivative of the Euler product is a Dirichlet series over primes, −ζ′(s)/ζ(s) = ∑ Λ(n)n^(−s), where Λ(n) = log p on powers of p. Perron's formula, an application of [Cauchy's theorem](../../09-advanced-analysis/02-complex-analysis/cauchys-theorem-and-its-consequences.md), writes ψ(x) as the integral of −ζ′(s)/ζ(s)·xˢ/s along a vertical line Re s = c > 1. Moving the line left, the pole of ζ at s = 1 contributes the main term x, and each zero ρ contributes x^ρ/ρ.

4. **No zeros on Re s = 1 is the crux.** A zero at 1 + iγ would contribute a term of size x itself, oscillating as x^(iγ), and ψ(x)/x would not tend to 1. So the PNT is essentially equivalent to ζ(1 + it) ≠ 0 for real t. The proof uses an inequality noticed by Mertens:

   ```
   3 + 4cos θ + cos 2θ = 2(1 + cos θ)² ≥ 0   ⇒   ∣ζ(σ)³·ζ(σ + it)⁴·ζ(σ + 2it)∣ ≥ 1   for σ > 1
   ```

   The second follows by taking logarithms of the Euler product term by term. As σ → 1, ζ(σ)³ has a pole of order 3, while a zero at 1 + it would give ζ(σ + it)⁴ a zero of order at least 4, and ζ(σ + 2it) stays bounded; the product would tend to 0.

5. **A Tauberian step converts the analytic fact into the asymptotic.** Knowing ζ has no zeros on Re s = 1 does not immediately give ψ(x) ∼ x; one needs to control the integral near the line. Newman found in 1980 a short route through a theorem about Laplace transforms, using only Cauchy's integral formula and Chebyshev's bound ψ(x) = O(x). It is now the standard quick proof.

6. **The error term is controlled by the zeros.** De la Vallée Poussin showed in 1899 that ζ has no zeros in a region σ > 1 − c/log ∣t∣, giving π(x) = li(x) + O(x·exp(−c√log x)) for some constant c > 0. Wider zero-free regions, due to Vinogradov and Korobov, improve this only slightly. The Riemann Hypothesis is equivalent to the error O(√x·log x). Littlewood showed in 1914 that π(x) − li(x) changes sign infinitely often, although li(x) exceeds π(x) for every x that has been checked.

7. **Elementary proofs exist, but are not simpler.** In 1948 Selberg proved the identity

   ```
   ∑_(p≤x) (log p)² + ∑_(pq≤x) log p·log q = 2x·log x + O(x)      (p, q prime)
   ```

   by elementary manipulation of divisor sums. From it Selberg and Erdős derived the PNT without complex analysis. The proof refuted the belief that the theorem needed complex function theory, but it did not displace the analytic proof, which gives better error terms and generalises.

8. **The density of primes sizes real systems.** By the PNT a random integer near 2¹⁰²⁴ is prime with probability about 1/log(2¹⁰²⁴) ≈ 1/710, so generating Rivest–Shamir–Adleman (RSA) keys for [cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md) needs a few hundred primality tests. Cramér's model, which treats each n as prime independently with probability 1/log n, predicts many finer facts, but it is a heuristic and is known to fail in some ranges.

## Key concepts

| Term | Meaning |
|---|---|
| π(x) | The number of primes p ≤ x |
| Logarithmic integral li(x) | ∫₂ˣ dt/log t, the best simple approximation to π(x) |
| Chebyshev function ψ(x) | ∑ log p over prime powers pᵏ ≤ x |
| Perron's formula | ψ(x) as a contour integral of −ζ′/ζ·xˢ/s |
| Zero-free region | A region near Re s = 1 containing no zeros of ζ |
| Tauberian theorem | A result turning information about a transform into asymptotics of the original |
| Selberg's formula | The elementary identity behind the 1948–1949 proofs |

## How it fits

- **Below:** [the zeta function](the-riemann-zeta-function.md) and its explicit formula; [Cauchy's theorem](../../09-advanced-analysis/02-complex-analysis/cauchys-theorem-and-its-consequences.md) and [residues](../../09-advanced-analysis/02-complex-analysis/singularities-and-residues.md) supply the contour argument.
- **Above:** prime density sizes key generation in [cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md); the sharp error term is the Riemann Hypothesis among the [open problems](../../15-mathematics-in-context/open-problems.md).
- **Siblings:** [primes in arithmetic progressions](primes-in-arithmetic-progressions.md) refine the count by residue class; [sieves](sieves-and-additive-problems.md) count primes with extra conditions, where zeta methods alone fail.

## Common misconceptions

- **"The PNT says the n-th prime is n·log n"**: it gives the asymptotic pₙ ∼ n·log n, with a large relative error for any fixed n.
- **"li(x) is always larger than π(x)"**: Littlewood's theorem says the sign changes infinitely often, though no crossing has been observed.
- **"The PNT needs the Riemann Hypothesis"**: it needs only that no zero lies on the line Re s = 1.

## Go deeper

- G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers* (6th edition, 2008): Chebyshev's bounds and the elementary proof.
- Tom M. Apostol, *Introduction to Analytic Number Theory* (1976): the classical analytic proof in full.
- D. Zagier, "Newman's short proof of the prime number theorem", *American Mathematical Monthly* (1997): the whole proof in four pages.
