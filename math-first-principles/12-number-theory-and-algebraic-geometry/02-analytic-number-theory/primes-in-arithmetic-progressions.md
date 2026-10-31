# Primes in Arithmetic Progressions

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Analytic Number Theory](README.md)
> **Builds on:** [The Riemann Zeta Function](the-riemann-zeta-function.md), [Fourier Analysis on Groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md), [Representations of Finite Groups](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md), [Modular Arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md), [Fermat, Euler and Primitive Roots](../../02-number-systems/02-elementary-number-theory/fermat-euler-and-primitive-roots.md)
> **Enables:** [Sieves and Additive Problems](sieves-and-additive-problems.md), [Modular Forms](../04-elliptic-curves-and-modular-forms/modular-forms.md), [The Langlands Programme](../04-elliptic-curves-and-modular-forms/the-langlands-programme.md)

## Essence

Dirichlet proved in 1837 that if a and q have greatest common divisor (gcd) 1, then infinitely many primes are congruent to a mod q. His method created analytic number theory. To isolate one residue class he used characters, the Fourier analysis of the finite group (ℤ/q)^×, and attached to each character χ a function L(s, χ) with an Euler product like ζ. The theorem then reduces to one analytic fact, L(1, χ) ≠ 0 for every non-trivial χ, and the hardest case of that fact turns out to be a statement about class numbers. In the strong form, the primes are equidistributed: each of the φ(q) admissible classes receives a share 1/φ(q).

## Core tenets

1. **The statement, and why the condition is needed.** If gcd(a, q) = 1, the arithmetic progression a, a + q, a + 2q, … contains infinitely many primes, and the sum of 1/p over them diverges. If gcd(a, q) = d > 1, every term is divisible by d, so the class contains at most one prime. Here φ(q) is Euler's function, the number of classes prime to q.

2. **Euclid-style arguments reach only some classes.** For primes ≡ 3 mod 4: if p₁, …, p_k are all of them, then 4p₁⋯p_k − 1 is ≡ 3 mod 4, so it has a prime factor ≡ 3 mod 4, and that factor is new. For 1 mod 4, a prime factor of (2p₁⋯p_k)² + 1 must be ≡ 1 mod 4, since −1 is a square modulo it. Arguments of this kind are known to work only for classes with a² ≡ 1 mod q, so the general case needs a different idea.

3. **Characters pick out residue classes.** A Dirichlet character mod q is a homomorphism χ: (ℤ/q)^× → ℂ^×, extended by 0 to integers not prime to q. There are φ(q) of them, and they satisfy orthogonality:

   ```
   (1/φ(q)) · ∑_χ χ̄(a)·χ(n) = 1 if n ≡ a mod q,  and 0 otherwise
   ```

   For q = 4 the characters are χ₀, trivial on odd numbers, and χ₄(n) = (−1)^((n−1)/2) for odd n. The indicator of 1 mod 4 on odd numbers is (χ₀ + χ₄)/2. This is [Fourier analysis on a finite abelian group](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md).

4. **L-functions reduce the theorem to L(1, χ) ≠ 0.** Since χ is completely multiplicative, L(s, χ) = ∑ χ(n)n^(−s) = ∏_p (1 − χ(p)p^(−s))^(−1) for s > 1. Taking logarithms, ∑_p χ(p)p^(−s) = log L(s, χ) + (bounded). Combine with orthogonality:

   ```
   ∑_(p ≡ a mod q) p^(−s) = (1/φ(q)) · ∑_χ χ̄(a)·log L(s, χ) + (bounded)
   ```

   As s → 1, the trivial character gives log ζ(s) → ∞. If every other L(s, χ) has a finite non-zero limit at s = 1, nothing cancels the divergence, so there are infinitely many primes ≡ a mod q.

5. **Complex characters are easy, real ones are the crux.** For real s > 1 the product of all the L(s, χ) mod q is at least 1, since its logarithm is φ(q) times a sum of positive terms over the prime powers ≡ 1 mod q. If L(1, χ) = 0 for a complex χ, then also L(1, χ̄) = 0, and two zeros would beat the single pole of ζ, forcing the product to 0. A real χ is its own conjugate, so the argument fails. Dirichlet's way out was the class number formula; another is that ζ(s)·L(s, χ) is the zeta function of a quadratic field, whose non-negative coefficients rule out a zero at s = 1.

6. **The class number formula ties L(1, χ) to arithmetic.** For a negative discriminant D, with χ_D the corresponding real character, h the class number of ℚ(√D) and w its number of roots of unity, L(1, χ_D) = 2πh/(w·√∣D∣). Since h ≥ 1, the value is non-zero. Checks: D = −4 gives 1 − 1/3 + 1/5 − ⋯ = π/4, Leibniz's series; D = −3 gives π/(3√3).

7. **Quantitative versions reach the limits of current knowledge.** De la Vallée Poussin's method gives π(x; q, a) ∼ li(x)/φ(q) as x → ∞ for fixed q, where π(x; q, a) counts primes p ≤ x with p ≡ a mod q. Uniformity in q is the problem. A real zero of some L(s, χ) very close to 1, a Siegel zero, is not ruled out unconditionally (open as of 2026), though the Generalised Riemann Hypothesis (GRH) excludes it. So the Siegel–Walfisz theorem, valid for q up to a power of log x, has constants that cannot be computed. The Bombieri–Vinogradov theorem of 1965 proves GRH-strength equidistribution on average over q up to about √x, which is often enough.

## Key concepts

| Term | Meaning |
|---|---|
| Euler's function φ(q) | The number of residue classes mod q prime to q |
| Dirichlet character | A homomorphism (ℤ/q)^× → ℂ^×, extended by 0 |
| Orthogonality | Averages of characters isolate one residue class |
| Dirichlet L-function | L(s, χ) = ∑ χ(n)n^(−s), with an Euler product |
| Class number formula | L(1, χ_D) = 2πh/(w·√∣D∣) for D < 0 |
| Siegel zero | A hypothetical real zero of some L(s, χ) very near s = 1 |
| Equidistribution | Each admissible class gets the share 1/φ(q) of the primes |

## How it fits

- **Below:** [the zeta function](the-riemann-zeta-function.md) is the case of the trivial character; [Fourier analysis on groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md) and [characters of finite groups](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md) give orthogonality; [primitive roots](../../02-number-systems/02-elementary-number-theory/fermat-euler-and-primitive-roots.md) describe (ℤ/q)^×.
- **Above:** Hecke's L-functions of [modular forms](../04-elliptic-curves-and-modular-forms/modular-forms.md) generalise L(s, χ); [the Langlands programme](../04-elliptic-curves-and-modular-forms/the-langlands-programme.md) treats Dirichlet characters as its simplest automorphic forms.
- **Siblings:** [sieves](sieves-and-additive-problems.md) use Bombieri–Vinogradov as their main input; Chebotarev's theorem in [class field theory](../01-algebraic-number-theory/class-field-theory.md) generalises Dirichlet's theorem to splitting in any Galois extension; the formula links to [the class group](../01-algebraic-number-theory/ideals-and-the-class-group.md).

## Common misconceptions

- **"Dirichlet's theorem is a counting statement"**: the original proves divergence of ∑ 1/p over the class, hence infinitude; the asymptotic count came in 1896.
- **"Each admissible class gets its share at every height"**: in the limit yes, but the primes ≡ 3 mod 4 up to x usually outnumber those ≡ 1 mod 4, an effect called Chebyshev's bias.

## Go deeper

- Harold Davenport, *Multiplicative Number Theory* (3rd edition, 2000): the classic route from Dirichlet to Bombieri–Vinogradov.
- Tom M. Apostol, *Introduction to Analytic Number Theory* (1976): Dirichlet's theorem in full, at undergraduate level.
- Jean-Pierre Serre, *A Course in Arithmetic* (1973): a short, elegant proof of Dirichlet's theorem.
