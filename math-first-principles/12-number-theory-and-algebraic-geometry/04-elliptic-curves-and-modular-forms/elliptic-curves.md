# Elliptic Curves

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Elliptic Curves and Modular Forms](README.md)
> **Builds on:** [Algebraic Curves and Riemann–Roch](../03-algebraic-geometry/algebraic-curves-and-riemann-roch.md), [Projective Varieties and Bézout's Theorem](../03-algebraic-geometry/projective-varieties-and-bezouts-theorem.md), [p-adic Numbers and Local Fields](../01-algebraic-number-theory/p-adic-numbers-and-local-fields.md), [Finite Fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md)
> **Enables:** [Modular Forms](modular-forms.md), [Fermat's Last Theorem](fermats-last-theorem.md), [The Langlands Programme](the-langlands-programme.md), [Cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md), [Public-Key Cryptography (CS)](../../../cs-first-principles/11-security-and-cryptography/02-cryptography/public-key-cryptography.md)

## Essence

An elliptic curve is a smooth cubic curve with a chosen point, such as y² = x³ − 2. It is the simplest curve that is neither trivial nor hopeless: genus 0 curves have rational points that are easy to list, and curves of higher genus have only finitely many, but on an elliptic curve the rational points form a group. A line through two points meets the cubic in a third, and that defines an addition. The questions this group raises run through modern number theory: its rank is the subject of the Birch and Swinnerton-Dyer conjecture, its behaviour mod p is controlled by modular forms, and its version over finite fields secures much of the internet.

## Core tenets

1. **Every elliptic curve has a cubic equation.** An elliptic curve over a field k is a smooth projective curve of genus 1 with a point O defined over k. Riemann–Roch produces functions x and y with poles of order 2 and 3 at O and a cubic relation between them. If 2 and 3 are invertible in k, this simplifies to y² = x³ + ax + b, smooth exactly when 4a³ + 27b² ≠ 0, with O the point at infinity (0 : 1 : 0).

2. **Chords and tangents define a group.** By Bézout, a line meets the cubic in three points counted with multiplicity. Define P + Q + R = O whenever P, Q, R are collinear; so P + Q is the reflection in the x-axis of the third point on the line PQ, and −P is the reflection of P. For the slope λ of the line through P and Q, or of the tangent if P = Q, the sum has x₃ = λ² − x₁ − x₂ and y₃ = λ(x₁ − x₃) − y₁. On y² = x³ − 2, doubling P = (3, 5) uses λ = 3x²/(2y) = 27/10 and gives 2P = (129/100, −383/1000), a duplication Fermat knew. Associativity follows from Riemann–Roch: P ↦ the class of the divisor P − O is a bijection from the curve to its degree-zero Picard group, compatible with the two additions.

3. **Over ℂ an elliptic curve is a torus.** For a lattice Λ ⊂ ℂ, the Weierstrass function ℘ and its derivative satisfy ℘′² = 4℘³ − g₂℘ − g₃, and z ↦ (℘(z), ℘′(z)) identifies ℂ/Λ with a cubic curve, the group law becoming addition in ℂ. So the points of order n form a group (ℤ/n)². The name comes from elliptic integrals, which compute arc length on ellipses and are inverted by such functions.

4. **Rational points form a finitely generated group (Mordell, 1922).** For E over ℚ, E(ℚ) ≅ ℤʳ ⊕ T with T finite; r is the rank. The proof has two halves: E(ℚ)/2E(ℚ) is finite, by an argument using finiteness of class groups and units, and a height function, measuring the size of numerators and denominators, roughly quadruples under doubling, so a descent terminates. Weil extended this to number fields in 1928.

5. **Torsion is classified; rank is not.** Mazur proved in 1977 that T is one of 15 groups: ℤ/n for n = 1, …, 10 or 12, or ℤ/2 × ℤ/2n for n = 1, …, 4. Ranks are a different story. Elkies found a curve of rank at least 28 in 2006, and whether ranks over ℚ are bounded is open as of 2026. No algorithm is known that provably computes the rank of every curve.

6. **Reduction mod p obeys the Hasse bound.** Reducing the equation mod a prime p of good reduction gives a curve over 𝔽_p with #E(𝔽_p) = p + 1 − a_p points, and Hasse proved in the 1930s that ∣a_p∣ ≤ 2√p. For y² = x³ − 2 and p = 13 there are 19 points, so a₁₃ = −5. Hasse's theorem is the genus 1 case of the [Weil bound](../03-algebraic-geometry/algebraic-curves-and-riemann-roch.md). For curves without complex multiplication, the normalised a_p/(2√p) follow the semicircle law predicted by Sato and Tate, proved by Taylor and collaborators.

7. **The L-function should see the rank (BSD).** Packaging the a_p gives L(E, s) = ∏_p (1 − a_p·p^(−s) + p^(1−2s))^(−1) at good primes. The Birch and Swinnerton-Dyer (BSD) conjecture, from computations in the 1960s, says the order of vanishing of L(E, s) at s = 1 equals the rank, with a formula for the leading coefficient involving the Tate–Shafarevich group Ш. It is open as of 2026 and is a Clay Millennium Problem. It is proved when that order is 0 or 1, by Gross–Zagier (1986) and Kolyvagin (1989), using modularity.

8. **Over finite fields elliptic curves are cryptographic groups.** Given points P and Q = nP in E(𝔽_p), recovering n is the elliptic curve discrete logarithm problem. Koblitz and Miller independently proposed it for [cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md) in 1985. No general sub-exponential classical attack is known as of 2026, so a 256-bit curve gives security comparable to 3072-bit Rivest–Shamir–Adleman (RSA). Elliptic curve Diffie–Hellman and signatures are standard in [public-key cryptography](../../../cs-first-principles/11-security-and-cryptography/02-cryptography/public-key-cryptography.md), though Shor's quantum algorithm would break them. Lenstra's elliptic curve method also factors integers.

## Key concepts

| Term | Meaning |
|---|---|
| Weierstrass equation | y² = x³ + ax + b with 4a³ + 27b² ≠ 0 |
| Chord-and-tangent law | P + Q + R = O for collinear points |
| Mordell–Weil group | E(K), finitely generated for a number field K |
| Rank | The number r of independent points of infinite order |
| Torsion | Points of finite order; 15 possible groups over ℚ |
| a_p | p + 1 − #E(𝔽_p), with ∣a_p∣ ≤ 2√p |
| L(E, s) | The Euler product built from the a_p |
| Tate–Shafarevich group Ш | Measures failure of the local-to-global principle for E |

## How it fits

- **Below:** [Riemann–Roch](../03-algebraic-geometry/algebraic-curves-and-riemann-roch.md) gives the equation; [Bézout](../03-algebraic-geometry/projective-varieties-and-bezouts-theorem.md) the group law; [finite fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md) the reductions; [p-adic fields](../01-algebraic-number-theory/p-adic-numbers-and-local-fields.md) the local study behind Ш.
- **Above:** elliptic curve cryptography in [cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md).
- **Siblings:** [modular forms](modular-forms.md) have the a_p as coefficients; [Fermat's Last Theorem](fermats-last-theorem.md) follows from their modularity; they are the GL(2) test case of [the Langlands programme](the-langlands-programme.md).

## Common misconceptions

- **"An elliptic curve is an ellipse"**: it is a cubic of genus 1; ellipses have genus 0.
- **"The group law is just a geometric trick"**: it is addition on the torus ℂ/Λ and on the Picard group, which is why it is associative.

## Go deeper

- Joseph H. Silverman and John Tate, *Rational Points on Elliptic Curves* (2nd edition, 2015): an undergraduate introduction.
- Joseph H. Silverman, *The Arithmetic of Elliptic Curves* (2nd edition, 2009): the standard graduate text.
- Lawrence C. Washington, *Elliptic Curves: Number Theory and Cryptography* (2nd edition, 2008): the arithmetic with the applications.
