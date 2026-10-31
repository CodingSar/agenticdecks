# Sieves and Additive Problems

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Analytic Number Theory](README.md)
> **Builds on:** [The Prime Number Theorem](the-prime-number-theorem.md), [Primes in Arithmetic Progressions](primes-in-arithmetic-progressions.md), [Inclusion–Exclusion and the Pigeonhole Principle](../../03-combinatorics-and-graph-theory/01-enumeration/inclusion-exclusion-and-the-pigeonhole-principle.md), [Additive Combinatorics](../../03-combinatorics-and-graph-theory/04-extremal-combinatorics/additive-combinatorics.md), [Fourier Series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md)
> **Enables:** [Open Problems](../../15-mathematics-in-context/open-problems.md), [Computers and Proof](../../15-mathematics-in-context/computers-and-proof.md), [Mathematical Practice and Discovery](../../15-mathematics-in-context/mathematical-practice-and-discovery.md)

## Essence

Zeta functions count all primes; many questions ask about primes with a twist. Are there infinitely many twin primes p, p + 2? Is every even number above 2 a sum of two primes (Goldbach)? Two tools attack such problems. Sieves count what survives after removing multiples of small primes, a refined inclusion–exclusion. The circle method writes the number of representations n = p₁ + p₂ + p₃ as a Fourier integral and estimates it. Both give spectacular partial results, such as bounded gaps between primes and Goldbach for three primes, while the twin prime and binary Goldbach conjectures remain open as of 2026.

## Core tenets

1. **The sieve of Eratosthenes is inclusion–exclusion, and its errors explode.** The number of n ≤ x free of prime factors up to z is ∑_(d∣P) μ(d)·⌊x/d⌋, where P is the product of the primes up to z and μ is the Möbius function, (−1)ᵏ on products of k distinct primes. Replacing ⌊x/d⌋ by x/d makes an error up to 1 for each of the 2^(π(z)) divisors, far more than the main term once z is a little larger than log x. Every sieve is a way to truncate this sum while keeping control.

2. **Brun's sieve gives upper bounds of the right size.** Brun cut the inclusion–exclusion off at a chosen depth, using the Bonferroni inequalities, which say that stopping after an even or odd number of terms gives an upper or lower bound. The result is that the twin primes up to x number O(x/(log x)²). So the sum of their reciprocals converges, to Brun's constant ≈ 1.902, unlike ∑ 1/p. The Hardy–Littlewood conjecture predicts the count is asymptotically a known constant times x/(log x)², but only the upper bound is proved.

3. **The parity problem limits sieves.** Selberg observed that sieve axioms cannot distinguish integers with an even number of prime factors from those with an odd number: there are sequences with exactly the same sieve data made only of products of two primes. So a sieve alone cannot produce primes from such data, only "almost primes" with few prime factors. Chen's theorem reaches the limit: every sufficiently large even number is p + P₂, a prime plus a number with at most two prime factors, and there are infinitely many primes p with p + 2 = P₂. Chen announced it in 1966 and published the full proof in 1973.

4. **The circle method turns additive problems into Fourier integrals.** Let S(α) = ∑_(p≤n) log p·e^(2πipα). Orthogonality of e^(2πikα) on [0, 1] gives

   ```
   ∑_(p₁+p₂+p₃=n) log p₁·log p₂·log p₃ = ∫₀¹ S(α)³·e^(−2πinα) dα
   ```

   Near rationals a/q with small q (the major arcs), S is computed from primes in progressions and gives the main term, of size n². Elsewhere (the minor arcs) S must be shown small. Hardy and Littlewood developed the method, assuming GRH, the Generalised Riemann Hypothesis, for this problem; Vinogradov in 1937 bounded S on the minor arcs unconditionally, proving that every sufficiently large odd number is a sum of three primes.

5. **Two primes are much harder than three.** With two primes the main term is of size n, but the trivial bound for the minor arcs is ∫ ∣S∣² ≈ n·log n, larger than the main term, so even a perfect bound for sup ∣S∣ on the minor arcs is not enough. With three primes, ∫ ∣S∣³ ≤ sup ∣S∣ · ∫ ∣S∣² leaves room. This is why binary Goldbach is open as of 2026, though checked by computer for every even number up to 4 × 10¹⁸.

6. **Ternary Goldbach is solved.** Vinogradov's "sufficiently large" was astronomically large. Helfgott, in preprints of 2013, sharpened the major and minor arc estimates until the remaining range was within reach of computation, verified with Platt, proving that every odd number greater than 5 is a sum of three primes.

7. **Bounded gaps between primes.** Goldston, Pintz and Yıldırım (GPY) showed in 2005 that weighted sieves detect primes close together if primes are equidistributed in progressions slightly beyond the Bombieri–Vinogradov range. In 2013 Zhang proved a weaker but sufficient form of that distribution for smooth moduli and deduced that infinitely many pairs of primes differ by less than 7 × 10⁷. Months later Maynard, and Tao independently, found multidimensional sieve weights that need no new distribution result: they give gaps of at most 600, and m primes in bounded intervals for every m. A collaborative Polymath project lowered the bound to 246. The parity problem stops these methods short of gap 2, so the twin prime conjecture is open as of 2026.

8. **Additive combinatorics adds structure.** Green and Tao proved, in 2004 with publication in 2008, that the primes contain arithmetic progressions of every length. They combined Szemerédi's theorem from [additive combinatorics](../../03-combinatorics-and-graph-theory/04-extremal-combinatorics/additive-combinatorics.md) with a sieve-built pseudorandom majorant of the primes.

## Key concepts

| Term | Meaning |
|---|---|
| Sieve | A method counting integers with no small prime factors |
| Möbius function μ | (−1)ᵏ on products of k distinct primes, 0 if a square divides |
| Almost prime P_r | An integer with at most r prime factors |
| Parity problem | Sieves cannot tell an odd number of prime factors from an even number |
| Circle method | Counting representations by integrating an exponential sum around the circle |
| Major and minor arcs | Neighbourhoods of rationals with small denominator, and the rest |
| Bounded gaps | Infinitely many pairs of primes differ by at most a fixed bound |

## How it fits

- **Below:** [inclusion–exclusion](../../03-combinatorics-and-graph-theory/01-enumeration/inclusion-exclusion-and-the-pigeonhole-principle.md) is the raw sieve; [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md) give the circle method; [primes in progressions](primes-in-arithmetic-progressions.md) feed both the major arcs and the bounded-gaps theorem.
- **Above:** twin primes and Goldbach head the [open problems](../../15-mathematics-in-context/open-problems.md); Helfgott's proof shows [computers in proof](../../15-mathematics-in-context/computers-and-proof.md); Polymath is a case study in [mathematical practice](../../15-mathematics-in-context/mathematical-practice-and-discovery.md).
- **Siblings:** [the prime number theorem](the-prime-number-theorem.md) supplies densities; [the zeta function](the-riemann-zeta-function.md) is often replaced here by combinatorial identities.

## Common misconceptions

- **"Bounded gaps proves the twin prime conjecture is nearly done"**: the parity problem blocks gap 2, and a new idea is needed.
- **"Ternary Goldbach was settled by Vinogradov"**: he proved it only for sufficiently large odd numbers; Helfgott closed the gap.

## Go deeper

- John Friedlander and Henryk Iwaniec, *Opera de Cribro* (2010): the modern treatise on sieves, including parity.
- R. C. Vaughan, *The Hardy–Littlewood Method* (2nd edition, 1997): the circle method in full.
- Andrew Granville, "Primes in intervals of bounded length", *Bulletin of the American Mathematical Society* (2015): a readable account of Zhang and Maynard.
