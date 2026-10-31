# Ideals and the Class Group

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Algebraic Number Theory](README.md)
> **Builds on:** [Number Fields and Algebraic Integers](number-fields-and-algebraic-integers.md), [Rings and Ideals](../../05-abstract-algebra/02-rings-and-fields/rings-and-ideals.md), [Factorisation in Integral Domains](../../05-abstract-algebra/02-rings-and-fields/factorisation-in-integral-domains.md), [Homomorphisms and Quotient Groups](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md)
> **Enables:** [Class Field Theory](class-field-theory.md), [Algebraic Curves and Riemann–Roch](../03-algebraic-geometry/algebraic-curves-and-riemann-roch.md), [Schemes](../03-algebraic-geometry/schemes.md), [Fermat's Last Theorem](../04-elliptic-curves-and-modular-forms/fermats-last-theorem.md)

## Essence

When numbers stop factoring uniquely, pass from numbers to ideals. In the ring of integers 𝒪_K of a number field, every non-zero ideal is a product of prime ideals in exactly one way, because 𝒪_K is a Dedekind domain. The class group Cl(K) measures how far ideals are from numbers: it is trivial exactly when elements factor uniquely as well. It is always finite, and its order, the class number h_K, controls questions as concrete as which primes are x² + 5y² and which cases of Fermat's Last Theorem Kummer could prove.

## Core tenets

1. **A Dedekind domain is the right setting.** It is a Noetherian integral domain, integrally closed in its field of fractions, in which every non-zero prime ideal is maximal. 𝒪_K qualifies: its ideals are subgroups of ℤⁿ, hence finitely generated; it is integrally closed by construction; and 𝒪_K/𝔭 is a finite integral domain, hence a field. Each condition matters. In ℤ[√−3], which is not integrally closed, 𝔭 = (2, 1 + √−3) satisfies 𝔭² = 2𝔭 with 𝔭 ≠ (2), so ideals cannot be cancelled. In k[x, y], where the prime (x) is not maximal, the ideal (x, y²) lies strictly between (x, y)² and (x, y) and is no product of prime ideals.

2. **Ideals factor uniquely into prime ideals.** The key step is that every non-zero ideal 𝔞 has an inverse 𝔞⁻¹ = {x ∈ K : x𝔞 ⊆ 𝒪_K} with 𝔞𝔞⁻¹ = 𝒪_K. So to contain is to divide: 𝔞 ⊇ 𝔟 exactly when 𝔟 = 𝔞𝔠 for an ideal 𝔠, and the proof for ℤ goes through with prime ideals in place of primes. In ℤ[√−5], with 𝔭₂ = (2, 1 + √−5), 𝔭₃ = (3, 1 + √−5) and 𝔭₃′ = (3, 1 − √−5):

   ```
   (2) = 𝔭₂²     (3) = 𝔭₃·𝔭₃′     (1 + √−5) = 𝔭₂·𝔭₃     (1 − √−5) = 𝔭₂·𝔭₃′
   ```

   The two factorisations of 6 regroup the same four prime ideals.

3. **The class group measures the failure.** Fractional ideals, such as (1/2)𝒪_K, form a group, free on the prime ideals. The principal ones (x) form a subgroup, and Cl(K) is the quotient. Cl(K) is trivial exactly when 𝒪_K is a Principal Ideal Domain (PID), and for a Dedekind domain that happens exactly when it is a Unique Factorisation Domain (UFD). For the second step: in a UFD each non-zero prime ideal contains an irreducible π, and (π) is prime, hence maximal, hence the whole ideal; so every ideal, a product of primes, is principal.

4. **The class group is finite.** The norm N(𝔞) = #(𝒪_K/𝔞) is multiplicative and N((α)) = ∣N(α)∣. Minkowski's convex body theorem, applied to the lattice of an ideal, shows that every class contains an ideal of norm at most

   ```
   M_K = (n!/nⁿ)·(4/π)^(r₂)·√∣d_K∣
   ```

   where n is the degree, r₂ the number of pairs of complex embeddings and d_K the discriminant. There are finitely many ideals of bounded norm, so h_K = #Cl(K) is finite. For ℚ(√−5), M_K = (2/π)·√20 ≈ 2.85, so every class contains (1) or 𝔭₂, the only ideal of norm 2. No element has norm a² + 5b² = 2, so 𝔭₂ is not principal and h = 2.

5. **Kummer proved Fermat's Last Theorem for regular primes.** Fermat's Last Theorem (FLT) for an odd prime p says that xᵖ + yᵖ = zᵖ has no solution in positive integers. With ζ = ζ_p a primitive p-th root of unity, the equation factors in ℤ[ζ] as ∏ (x + ζⁱy) = zᵖ, over 0 ≤ i < p. When p ∤ xyz (the case p ∣ xyz needs a further descent), the factors generate coprime ideals, so each is a p-th power: (x + ζy) = 𝔞ᵖ. If p does not divide the class number of ℚ(ζ) (p is regular), the class of 𝔞 has order dividing both p and h, so 𝔞 is principal; then x + ζy is a unit times a p-th power, and Kummer's lemma on units gives a contradiction. Lamé had assumed that ℤ[ζ] always factors uniquely, but ℚ(ζ₂₃) has class number 3.

6. **Regularity is decided by Bernoulli numbers.** Kummer's criterion: p is regular exactly when p divides none of the numerators of the Bernoulli numbers B₂, B₄, …, B_(p−3). Since 37 divides 7709321041217, the numerator of B₃₂, the prime 37 is irregular; it is the first, followed by 59 and 67. Jensen proved that infinitely many primes are irregular. Whether infinitely many are regular is open as of 2026, though heuristics suggest about 61% of primes are.

7. **Class numbers are hard to predict.** The imaginary quadratic fields ℚ(√d) with class number 1 are exactly those with d = −1, −2, −3, −7, −11, −19, −43, −67, −163. Gauss conjectured this list. Heegner proved it in 1952, in a paper accepted only later, and Baker and Stark proved it independently in the 1960s. Gauss also expected infinitely many real quadratic fields of class number 1; that is open as of 2026.

## Key concepts

| Term | Meaning |
|---|---|
| Dedekind domain | Noetherian, integrally closed, every non-zero prime ideal maximal |
| Fractional ideal | A non-zero finitely generated 𝒪_K-submodule of K |
| Ideal norm N(𝔞) | The number of elements of 𝒪_K/𝔞 |
| Class group Cl(K) | Fractional ideals modulo principal ones |
| Class number h_K | The order of Cl(K) |
| Minkowski bound M_K | Every ideal class contains an ideal of norm at most M_K |
| Regular prime | A prime p not dividing the class number of ℚ(ζ_p) |

## How it fits

- **Below:** [factorisation in integral domains](../../05-abstract-algebra/02-rings-and-fields/factorisation-in-integral-domains.md) defines PIDs and UFDs; [quotient groups](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md) give Cl(K).
- **Above:** the coordinate ring of a smooth affine curve is also a Dedekind domain, and its class group is the Picard group of [algebraic curves](../03-algebraic-geometry/algebraic-curves-and-riemann-roch.md) and [schemes](../03-algebraic-geometry/schemes.md). Kummer's argument is the classical prelude to [Fermat's Last Theorem](../04-elliptic-curves-and-modular-forms/fermats-last-theorem.md).
- **Siblings:** [number fields](number-fields-and-algebraic-integers.md) supply the rings; [class field theory](class-field-theory.md) builds an extension whose Galois group is Cl(K); the [class number formula](../02-analytic-number-theory/primes-in-arithmetic-progressions.md) computes h_K from an L-function.

## Common misconceptions

- **"Ideals are a formal trick"**: prime ideals are the kernels of maps from 𝒪_K onto finite fields, the points of an arithmetic curve.
- **"Unique factorisation of ideals gives unique factorisation of numbers"**: only when h_K = 1; ℤ[√−5] factors ideals uniquely and has h = 2.
- **"Kummer proved FLT for almost all primes"**: it is not even known that infinitely many primes are regular.

## Go deeper

- Daniel A. Marcus, *Number Fields* (1977): ideal factorisation and the Minkowski bound, with many class-number computations.
- Ian Stewart and David Tall, *Algebraic Number Theory and Fermat's Last Theorem*: a first reading, through to Kummer's argument.
- Lawrence C. Washington, *Introduction to Cyclotomic Fields* (2nd edition, 1997): regular primes, Bernoulli numbers and Kummer's methods in depth.
