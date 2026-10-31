# Algebraic and Transcendental Numbers

> **Layer:** [02 Number Systems](../README.md) › [Constructing the Numbers](README.md)
> **Builds on:** [Countable Sets](../../01-sets-and-foundations/02-infinity-and-cardinality/countable-sets.md), [The Real Numbers](the-real-numbers.md), [The Complex Numbers](the-complex-numbers.md)
> **Enables:** [Field Extensions](../../05-abstract-algebra/02-rings-and-fields/field-extensions.md), [Ruler and Compass Constructions](../../05-abstract-algebra/03-galois-theory/ruler-and-compass-constructions.md), [Number Fields and Algebraic Integers](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/number-fields-and-algebraic-integers.md), [Open Problems](../../15-mathematics-in-context/open-problems.md)

## Essence

A complex number is algebraic if it is a root of a non-zero polynomial with integer coefficients, as √2 is a root of x² − 2, and transcendental otherwise. Cantor's counting argument shows that the algebraic numbers are countable, so almost every number is transcendental, yet proving any particular number transcendental is hard. The tools are approximation and auxiliary functions: an algebraic number cannot be approximated too well by rationals (Liouville, 1844), and e and π are transcendental because a carefully built integral would otherwise be a non-zero integer smaller than 1 (Hermite, 1873; Lindemann, 1882). Simple questions, such as whether e + π is rational, are open as of 2026.

## Core tenets

1. **The algebraic numbers are countable (Cantor, 1874), so almost all numbers are transcendental.** Give the polynomial aₙxⁿ + ⋯ + a₀ the height n + |aₙ| + ⋯ + |a₀|. Only finitely many polynomials have a given height, and each has at most n roots, so listing roots height by height enumerates every algebraic number. Since ℝ is uncountable, transcendental numbers exist, and the algebraic reals even have measure zero ([measure and σ-algebras](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md)). The argument proves existence without exhibiting a single example.

2. **The algebraic numbers form a field, and that field is algebraically closed.** An algebraic α has a minimal polynomial, the monic polynomial over ℚ of least degree with root α, and that degree is the dimension of ℚ(α) as a vector space over ℚ. For algebraic α and β, the field ℚ(α, β) has dimension at most deg α · deg β, so the powers of α + β, or of αβ, are linearly dependent over ℚ, which is a polynomial equation they satisfy. A root of a polynomial with algebraic coefficients is algebraic by the same counting of dimensions, so the field ℚ̄ of algebraic numbers is algebraically closed, and countable.

3. **Liouville (1844): an algebraic α of degree d ≥ 2 satisfies |α − p/q| > c/qᵈ for some c > 0 and every rational p/q, and this gave the first explicit transcendental numbers.** Let f be an irreducible integer polynomial of degree d with f(α) = 0. Then f(p/q) ≠ 0, so qᵈ · f(p/q) is a non-zero integer and |f(p/q)| ≥ 1/qᵈ, while the mean value theorem bounds |f(p/q)| by a constant times |α − p/q|. Liouville's number L = ∑ 10^(−k!) = 0.110001000… has rational approximations far better than any such bound, so it is transcendental. Roth (1955) lowered the exponent d to 2 + ε for every ε > 0, which is best possible.

4. **Hermite (1873): e is transcendental.** Suppose a₀ + a₁e + ⋯ + aₙeⁿ = 0 with integers aᵢ not all 0. From a polynomial with zeros of high order at 0, 1, …, n, chosen using a large prime p, one builds a combination of integrals of e^(−x) times that polynomial which the equation forces to be an integer. Divisibility by p shows that it is not 0, and estimating the integrals shows that its absolute value is below 1 once p is large. This template, a quantity that must be a non-zero integer yet is tiny, drives the subject.

5. **Lindemann (1882): eᵅ is transcendental for every non-zero algebraic α, so π is transcendental and the circle cannot be squared.** Since e^(iπ) = −1 is algebraic, iπ is not algebraic, so neither is π. Ruler and compass produce only algebraic numbers, so they cannot construct √π, the side of a square with the area of the unit disc, settling a problem from Greek geometry ([ruler and compass constructions](../../05-abstract-algebra/03-galois-theory/ruler-and-compass-constructions.md)). Weierstrass (1885) proved the general form: for distinct algebraic α₁, …, αₙ, the numbers e^(α₁), …, e^(αₙ) are linearly independent over ℚ̄.

6. **Gelfond–Schneider (1934): if a and b are algebraic, a ≠ 0, 1, and b is not rational, then every value of aᵇ is transcendental.** This solved the seventh of Hilbert's problems (1900). Examples are 2^√2 and e^π, a value of (−1)^(−i), since (e^(iπ))^(−i) = e^π. The hypotheses matter: √2 raised to the rational power 2 is 2, and the theorem says nothing about e^e, because e is not algebraic. Baker (1966) extended it to linear forms in many logarithms, a tool for bounding the solutions of Diophantine equations.

7. **Many natural questions are open as of 2026.** Nobody knows whether e + π, eπ, π^e or e^e is rational, though e + π and eπ cannot both be algebraic: they are the coefficients of (x − e)(x − π) = x² − (e + π)x + eπ, and e would then be algebraic. Whether the Euler–Mascheroni constant γ = lim (1 + 1/2 + ⋯ + 1/n − log n) is irrational is also open. Partial results include Apéry's proof (1978) that ζ(3) = 1 + 1/2³ + 1/3³ + ⋯ is irrational and Nesterenko's (1996) that π and e^π are algebraically independent. Schanuel's conjecture, open as of 2026, would settle most such questions at once.

## Key concepts

| Term | Meaning |
|---|---|
| Algebraic number | A root of a non-zero polynomial with integer coefficients |
| Transcendental number | A complex number that is not algebraic |
| Minimal polynomial | The monic polynomial over ℚ of least degree with root α |
| ℚ̄ | The field of all algebraic numbers, countable and algebraically closed |
| Liouville number | An irrational x such that for every n some p/q with q ≥ 2 has \|x − p/q\| < 1/qⁿ |
| Algebraically independent | Satisfying no non-zero polynomial equation with rational coefficients |

## How it fits

- **Below:** countability (01) gives existence for free; [the real numbers](the-real-numbers.md) and [the complex numbers](the-complex-numbers.md) are where these numbers live.
- **Above:** field extensions (05) explain the degree counting; Galois theory (05) uses Lindemann for squaring the circle; algebraic number theory (12) studies the algebraic integers, the roots of monic integer polynomials, inside ℚ̄; [open problems](../../15-mathematics-in-context/open-problems.md) (15) lists the questions above.
- **Siblings:** ℚ̄ is a countable, algebraically closed field inside [the complex numbers](the-complex-numbers.md), as good as ℂ for algebra but full of holes; the irrationality of √2 in [integers and rational numbers](integers-and-rational-numbers.md) is the first such question.

## Common misconceptions

- **"Transcendental numbers are rare and exotic"**: almost every number is transcendental; the algebraic numbers are the countable exception. What is rare is a proof for a specific number.
- **"Irrational means transcendental"**: √2 is irrational but algebraic; transcendence rules out every polynomial relation, not only linear ones.
- **"π contains every finite string of digits"**: that would follow if π were normal in base 10, which is open as of 2026; transcendence alone does not imply it.

## Go deeper

- Alan Baker, *Transcendental Number Theory* (1975): from Liouville to linear forms in logarithms, short and complete.
- Ivan Niven, *Irrational Numbers* (1956): irrationality and transcendence proofs at an elementary level.
