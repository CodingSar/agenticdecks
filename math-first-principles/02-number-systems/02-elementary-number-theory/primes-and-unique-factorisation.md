# Primes and Unique Factorisation

> **Layer:** [02 Number Systems](../README.md) › [Elementary Number Theory](README.md)
> **Builds on:** [Divisibility and the Euclidean Algorithm](divisibility-and-the-euclidean-algorithm.md), [Mathematical Induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md), [Direct Proof, Contraposition and Contradiction](../../00-logic-and-proof/02-methods-of-proof/direct-proof-contraposition-and-contradiction.md)
> **Enables:** [Factorisation in Integral Domains](../../05-abstract-algebra/02-rings-and-fields/factorisation-in-integral-domains.md), [Ideals and the Class Group](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/ideals-and-the-class-group.md), [The Riemann Zeta Function](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md), [The Prime Number Theorem](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-prime-number-theorem.md), [Primes in Arithmetic Progressions](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/primes-in-arithmetic-progressions.md)

## Essence

A prime is an integer p > 1 whose only positive divisors are 1 and p. Every integer greater than 1 is a product of primes in exactly one way, apart from order: the fundamental theorem of arithmetic. Existence is easy; uniqueness is not, and it rests entirely on Euclid's lemma, that a prime dividing a product divides one of the factors, which in turn rests on Bézout's identity. The theorem makes the primes the atoms of multiplication, and the question of how those atoms are spread among the integers starts analytic number theory. Its failure in rings such as ℤ[√−5] starts algebraic number theory.

## Core tenets

1. **Every integer n > 1 is a product of primes.** Suppose not, and let n be the least counterexample, by well-ordering. Then n is not prime, so n = ab with 1 < a, b < n; both a and b are products of primes because they are smaller than n, and so n is too, a contradiction. This is strong induction in disguise.

2. **Euclid's lemma: if a prime p divides ab, then p ∣ a or p ∣ b.** If p ∤ a, then gcd(p, a) = 1, where gcd is the greatest common divisor, so px + ay = 1 by Bézout; multiplying by b gives b = pbx + aby, and p divides both terms. Two notions are at work. An irreducible element has no factorisation into two non-units; a prime element satisfies Euclid's lemma. In ℤ they coincide, but only because of Bézout, and in general rings they part company.

3. **The factorisation is unique.** If p₁ ⋯ pᵣ = q₁ ⋯ qₛ, then p₁ divides the right-hand side, so by Euclid's lemma it divides some qⱼ, and being prime, equals it. Cancel and repeat; induction on r finishes the proof. Euclid's *Elements* (Book VII) contains the lemma, but the first clear statement and proof of the full theorem is in Gauss's *Disquisitiones Arithmeticae* (1801).

4. **There are infinitely many primes.** Given primes p₁, …, pₖ, the number N = p₁ ⋯ pₖ + 1 leaves remainder 1 on division by each, so its prime factors are new (*Elements* IX.20). The number N need not itself be prime: 2·3·5·7·11·13 + 1 = 30031 = 59·509. Euler gave an analytic proof: unique factorisation is exactly the identity ∑ 1/nˢ = ∏ (1 − p^(−s))^(−1) for s > 1, and as s → 1 the left side diverges, so the product cannot be finite. Pushing further shows that ∑ 1/p diverges, so the primes are much denser than the squares.

5. **The primes thin out, at a predictable rate.** Gaps can be arbitrarily long, since n! + 2, n! + 3, …, n! + n are all composite. Yet the prime number theorem (Hadamard and de la Vallée Poussin, independently, 1896) says the number of primes up to x is asymptotic to x/ln x, and Dirichlet (1837) proved that every progression a, a + q, a + 2q, … with gcd(a, q) = 1 contains infinitely many primes. Both proofs need complex analysis, developed in layer 12.

6. **Simple questions about primes remain open.** As of 2026 it is not known whether there are infinitely many twin primes p, p + 2, nor whether every even number greater than 2 is a sum of two primes (Goldbach's conjecture). Partial results: Zhang (2013) proved that some gap below 70,000,000 occurs infinitely often, later lowered to 246 by the Polymath project (2014), and Helfgott's proof (announced 2013) that every odd number greater than 5 is a sum of three primes.

7. **Unique factorisation can fail.** In ℤ[√−5] = {a + b√−5 : a, b ∈ ℤ}, use the norm N(a + b√−5) = a² + 5b², which is multiplicative:

   ```
   6 = 2 · 3 = (1 + √−5)(1 − √−5)       norms: 4 · 9 = 6 · 6
   ```

   No element has norm 2 or 3, so all four factors are irreducible, and 2 divides the product (1 + √−5)(1 − √−5) without dividing either factor: 2 is irreducible but not prime. Lamé announced a proof of Fermat's Last Theorem in 1847 that assumed unique factorisation in rings of this kind; Kummer had already found it can fail, and his "ideal numbers", recast by Dedekind as ideals, restore uniqueness at the level of ideals.

## Key concepts

| Term | Meaning |
|---|---|
| Prime | An integer p > 1 with no positive divisors other than 1 and p |
| Composite | An integer n > 1 that is not prime |
| Euclid's lemma | p ∣ ab implies p ∣ a or p ∣ b |
| Fundamental theorem of arithmetic | Factorisation into primes exists and is unique up to order |
| p-adic valuation vₚ(n) | The exponent of p in n; greatest common divisors and least common multiples take minimum and maximum exponents |
| Irreducible element | A non-unit with no factorisation into two non-units |
| Prime element | A non-unit satisfying Euclid's lemma |
| Euler product | ∑ 1/nˢ = ∏ (1 − p^(−s))^(−1), unique factorisation in analytic form |

## How it fits

- **Below:** [divisibility and the Euclidean algorithm](divisibility-and-the-euclidean-algorithm.md) supplies Bézout, and well-ordering from the [Peano axioms](../01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md) supplies existence.
- **Above:** factorisation in integral domains (05) separates irreducible from prime; ideals and the class group (12) measure the failure in ℤ[√−5]; the zeta function and the prime number theorem (12) study the distribution.
- **Siblings:** [modular arithmetic](modular-arithmetic.md) uses primes to build fields ℤ/p, [Fermat, Euler and primitive roots](fermat-euler-and-primitive-roots.md) tests primality, and [Diophantine equations](diophantine-equations.md) factor to solve.

## Common misconceptions

- **"Euclid's number p₁ ⋯ pₖ + 1 is always prime"**: it only has a prime factor outside the list; 30031 = 59·509.
- **"1 is a prime"**: excluding it is what makes the factorisation unique; otherwise 6 = 2·3 = 1·2·3.
- **"Uniqueness is obvious"**: in the multiplicative system {1, 5, 9, 13, …} of numbers that are 1 modulo 4, the numbers 9, 21 and 49 have no proper factors within the system, yet 441 = 9·49 = 21·21. Uniqueness needs Euclid's lemma, which needs addition through Bézout.

## Go deeper

- G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers* (1938; 6th edition 2008): the fundamental theorem and the elementary theory of prime distribution.
- Kenneth Ireland and Michael Rosen, *A Classical Introduction to Modern Number Theory* (2nd edition, 1990): unique factorisation in ℤ and in other rings.
- Richard Crandall and Carl Pomerance, *Prime Numbers: A Computational Perspective* (2nd edition, 2005): finding, testing and factoring primes in practice.
