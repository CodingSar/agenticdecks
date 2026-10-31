# Modular Arithmetic

> **Layer:** [02 Number Systems](../README.md) › [Elementary Number Theory](README.md)
> **Builds on:** [Divisibility and the Euclidean Algorithm](divisibility-and-the-euclidean-algorithm.md), [Primes and Unique Factorisation](primes-and-unique-factorisation.md), [Equivalence Relations and Quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md)
> **Enables:** [Fermat, Euler and Primitive Roots](fermat-euler-and-primitive-roots.md), [Groups and Subgroups](../../05-abstract-algebra/01-groups/groups-and-subgroups.md), [Finite Fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md), [Cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md), [Integers and Two's Complement (computer science)](../../../cs-first-principles/03-digital-logic/01-number-representation/integers-and-twos-complement.md)

## Essence

Two integers are congruent modulo n when n divides their difference, a ≡ b (mod n). Congruence is an equivalence relation that respects addition and multiplication, so the n classes form a finite ring ℤ/n in which arithmetic is exact, like clock arithmetic. Gauss introduced the notation in 1801 and made it the language of number theory. Working modulo n throws information away on purpose: a statement false modulo some n is false in ℤ, so congruences prove impossibility cheaply, and the Chinese remainder theorem shows how information modulo several coprime numbers reassembles.

## Core tenets

1. **Congruence respects the ring operations, so ℤ/n is a ring.** If a ≡ a′ and b ≡ b′ (mod n), then a + b ≡ a′ + b′, and ab − a′b′ = a(b − b′) + b′(a − a′) is a multiple of n, so ab ≡ a′b′. The operations on classes are therefore well defined, exactly as for the quotient constructions of ℤ and ℚ. Casting out nines is an instance: 10 ≡ 1 (mod 9), so every number is congruent to its digit sum, and a multiplication can be checked by comparing digit sums.

2. **a has a multiplicative inverse modulo n if and only if gcd(a, n) = 1.** If gcd(a, n) = 1, where gcd is the greatest common divisor, Bézout gives ax + ny = 1, so ax ≡ 1. Conversely ax ≡ 1 means ax + ny = 1 for some y, so any common divisor of a and n divides 1. The invertible classes form a group (ℤ/n)ˣ of size φ(n), Euler's function, the number of k in 1, …, n coprime to n. Cancellation needs an inverse: 2·1 ≡ 2·4 (mod 6), though 1 ≢ 4.

3. **ℤ/n is a field if and only if n is prime.** If n = p is prime, every non-zero class is coprime to p and so invertible. If n = ab with 1 < a, b < n, then a · b ≡ 0 with neither factor zero. Over the field ℤ/p a polynomial of degree d has at most d roots, by the same argument as over ℝ (each root splits off a linear factor). Modulo a composite this fails: x² ≡ 1 (mod 8) has the four roots 1, 3, 5 and 7.

4. **The Chinese remainder theorem: if m and n are coprime, the map ℤ/mn → ℤ/m × ℤ/n is a ring isomorphism.** The map x ↦ (x mod m, x mod n) is a ring homomorphism; its kernel is the multiples of both m and n, which are the multiples of mn because they are coprime, so it is injective, and both sides have mn elements. Explicitly, from mu + nv = 1, the number x = a·nv + b·mu solves x ≡ a (mod m) and x ≡ b (mod n). The problem in the Chinese *Sunzi Suanjing* asks for a number leaving remainders 2, 3 and 2 on division by 3, 5 and 7; the least answer is 23. Coprimality matters: ℤ/4 is not ℤ/2 × ℤ/2, since 1 has order 4 in the first and every element has order at most 2 in the second.

5. **Euler's function is multiplicative, and φ(n) = n ∏ (1 − 1/p) over the primes p dividing n.** Under the Chinese remainder theorem, units correspond to pairs of units, so φ(mn) = φ(m)φ(n) for coprime m, n. For a prime power, the non-units modulo pᵏ are the pᵏ⁻¹ multiples of p, so φ(pᵏ) = pᵏ − pᵏ⁻¹. Unique factorisation assembles the formula; for instance φ(12) = 12 · (1/2) · (2/3) = 4.

6. **Reduction modulo n proves impossibility.** Squares are 0 or 1 modulo 4, so no number of the form 4k + 3 is a sum of two squares; squares are 0, 1 or 4 modulo 8, so no number of the form 8k + 7 is a sum of three squares. An equation with no solution modulo some n has no solution in integers; the converse fails, as [Diophantine equations](diophantine-equations.md) shows.

7. **Modular arithmetic is efficient, and computers use it all the time.** Powers are computed by repeated squaring: 13 = 8 + 4 + 1, and modulo 7 we have 3² ≡ 2, 3⁴ ≡ 4, 3⁸ ≡ 2, so 3¹³ ≡ 2 · 4 · 3 ≡ 3, in a number of multiplications proportional to the number of digits of the exponent. Machine integers of w bits are arithmetic in ℤ/2ʷ, which is why overflow wraps around and why two's complement represents −1 as 2ʷ − 1.

## Key concepts

| Term | Meaning |
|---|---|
| a ≡ b (mod n) | n ∣ (a − b) |
| Residue class | The set of integers congruent to a given one; an element of ℤ/n |
| ℤ/n | The ring of n residue classes |
| Unit modulo n | A class with a multiplicative inverse, exactly those coprime to n |
| (ℤ/n)ˣ | The group of units modulo n |
| Euler's function φ(n) | The number of units modulo n |
| Chinese remainder theorem | ℤ/mn ≅ ℤ/m × ℤ/n when gcd(m, n) = 1 |
| Repeated squaring | Computing aᵏ mod n using the binary digits of k |

## How it fits

- **Below:** ℤ/n is the quotient of ℤ by an [equivalence relation](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md); [divisibility](divisibility-and-the-euclidean-algorithm.md) supplies inverses and [primes](primes-and-unique-factorisation.md) supply the fields ℤ/p.
- **Above:** groups and quotient rings (05) generalise ℤ/n; finite fields (05) extend ℤ/p; cryptography (14) and [integer representation](../../../cs-first-principles/03-digital-logic/01-number-representation/integers-and-twos-complement.md) in computer science compute in it.
- **Siblings:** [Fermat, Euler and primitive roots](fermat-euler-and-primitive-roots.md) study the group (ℤ/n)ˣ; [quadratic reciprocity](quadratic-reciprocity.md) asks which classes are squares.

## Common misconceptions

- **"You can always cancel in a congruence"**: only a factor coprime to the modulus; 2·1 ≡ 2·4 (mod 6).
- **"A polynomial has at most as many roots modulo n as its degree"**: true modulo a prime, false in general; x² ≡ 1 (mod 8) has four.
- **"An equation with non-trivial solutions modulo every n has one in integers"**: only the reverse implication holds; Selmer's cubic in [Diophantine equations](diophantine-equations.md) is a counterexample.

## Go deeper

- Carl Friedrich Gauss, *Disquisitiones Arithmeticae* (1801): the origin of congruence notation, still readable in translation.
- Kenneth Ireland and Michael Rosen, *A Classical Introduction to Modern Number Theory* (2nd edition, 1990): congruences and the structure of (ℤ/n)ˣ.
- Victor Shoup, *A Computational Introduction to Number Theory and Algebra* (2nd edition, 2009): modular arithmetic as computer scientists use it.
