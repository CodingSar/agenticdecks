# Commutative Rings and Localisation

> **Layer:** [05 Abstract Algebra](../README.md) › [Rings and Fields](README.md)
> **Builds on:** [Rings and Ideals](rings-and-ideals.md), [Factorisation in Integral Domains](factorisation-in-integral-domains.md), [Polynomial Rings](polynomial-rings.md)
> **Enables:** [Varieties and the Nullstellensatz](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/varieties-and-the-nullstellensatz.md), [Schemes](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/schemes.md), [Ideals and the Class Group](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/ideals-and-the-class-group.md), [p-adic Numbers and Local Fields](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/p-adic-numbers-and-local-fields.md)

## Essence

Commutative algebra treats a ring as a space and its elements as functions on it. The points are the prime ideals, forming the prime spectrum Spec R, and f "vanishes" at P when f ∈ P. Localisation zooms in: inverting everything outside P keeps only what happens near P, as ℤ₍ₚ₎, the fractions with denominator prime to p, keeps only the arithmetic of p. The Noetherian finiteness condition keeps the spaces tame. These ideas bridge this layer to algebraic geometry and algebraic number theory.

## Core tenets

1. **Localisation inverts a multiplicative set, and is characterised by a universal property.** Let S ⊆ R contain 1 and be closed under multiplication. S⁻¹R consists of fractions r/s with s ∈ S, where r/s = r′/s′ when t(rs′ − r′s) = 0 for some t ∈ S; the extra t is needed when R has zero divisors. R → S⁻¹R makes every element of S a unit, and every homomorphism that does so factors through it uniquely. For a domain and S = R ∖ {0} this is the field of fractions; other cases are R_f = R[1/f] from the powers of f, and ℤ₍ₚ₎ from S = ℤ ∖ pℤ.

2. **The primes of S⁻¹R are the primes of R that miss S.** Sending P to S⁻¹P, and pulling back along R → S⁻¹R, are inverse order-preserving bijections between the primes of R disjoint from S and the primes of S⁻¹R. For a prime P and S = R ∖ P this gives R_P, a local ring: it has exactly one maximal ideal, P·R_P, because every prime of R_P comes from a prime inside P. So ℤ₍ₚ₎ has only two primes, (0) and (p).

3. **Being zero is a local property.** If m in an R-module M becomes zero in M_P for every maximal ideal P, then m = 0. Otherwise the annihilator {r : rm = 0} is a proper ideal, lying in some maximal P by Zorn's lemma, and no s outside P kills m.

4. **The nilradical is the intersection of all prime ideals.** A nilpotent f, with fⁿ = 0 ∈ P, lies in every prime P. Conversely, if f is not nilpotent, then 0 is not among its powers, so R_f is a non-zero ring; it has a maximal ideal, and its pullback to R is a prime that does not contain f. So f vanishes at every point exactly when it is nilpotent; the Nullstellensatz in [Rings and Ideals](rings-and-ideals.md) is a sharper relative.

5. **Spec R is a topological space, and ring maps give continuous maps backwards.** Its closed sets, forming the Zariski topology, are the V(I): the primes containing an ideal I. Spec ℤ has a closed point (p) for each prime p and one generic point (0), whose closure is everything. A homomorphism φ: R → A sends a prime Q of A to the prime φ⁻¹(Q), and this map is continuous. Maximal ideals alone would not do: ℤ → ℚ pulls the maximal ideal 0 back to the non-maximal prime (0). The open set where f does not vanish is a copy of Spec R_f.

6. **Noetherian rings: every ideal is finitely generated, equivalently every ascending chain of ideals stops.** The union of a chain I₁ ⊆ I₂ ⊆ ⋯ is an ideal; if it is finitely generated, the generators lie in some Iₙ, where the chain stops. Conversely, an ideal that is not finitely generated yields a strictly increasing chain (a₁) ⊂ (a₁, a₂) ⊂ ⋯. Fields and principal ideal domains are Noetherian, and by Hilbert's basis theorem in [Polynomial Rings](polynomial-rings.md) so is k[x₁, …, xₙ], but k[x₁, x₂, …] in infinitely many variables is not.

7. **In a Noetherian ring every radical ideal is a finite intersection of primes.** Noetherian rings allow a maximal counterexample I. It is not prime, so ab ∈ I with a, b ∉ I, and I is the intersection of the radicals of I + (a) and I + (b), which are larger, so finite intersections of primes; hence so is I. Geometrically, every algebraic variety is a finite union of irreducible pieces.

8. **Krull dimension counts the longest chain of primes.** It is the largest n with primes P₀ ⊊ P₁ ⊊ ⋯ ⊊ Pₙ. Fields have dimension 0; ℤ and every principal ideal domain that is not a field have dimension 1, from (0) ⊂ (p); k[x₁, …, xₙ] has dimension n, the dimension of n-space, and the chain (0) ⊂ (x₁) ⊂ (x₁, x₂) ⊂ ⋯ gives at least n. Nagata found Noetherian rings of infinite dimension, but Noetherian local rings always have finite dimension.

## Key concepts

| Term | Meaning |
|---|---|
| Localisation S⁻¹R | Fractions r/s with s ∈ S; elements of S become units |
| Local ring | A ring with exactly one maximal ideal, such as R_P |
| Nilradical | The nilpotent elements; the intersection of all primes |
| Spec R | The set of prime ideals with the Zariski topology |
| Generic point | A prime whose closure is a whole irreducible piece, such as (0) in Spec ℤ |
| Noetherian ring | Every ideal is finitely generated; ascending chains of ideals stop |
| Krull dimension | Length of the longest chain of prime ideals |

## How it fits

- **Below:** prime and maximal ideals and Zorn's lemma come from [Rings and Ideals](rings-and-ideals.md); the field of fractions generalises the passage from ℤ to ℚ in [integers and rational numbers](../../02-number-systems/01-constructing-the-numbers/integers-and-rational-numbers.md).
- **Above:** the points of [varieties](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/varieties-and-the-nullstellensatz.md) are the maximal ideals of their coordinate rings, and [schemes](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/schemes.md) glue spectra along the localisations R_f; rings of integers in [ideals and the class group](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/ideals-and-the-class-group.md) are Noetherian domains of dimension 1, and completing ℤ₍ₚ₎ gives the [p-adic integers](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/p-adic-numbers-and-local-fields.md).
- **Siblings:** [Factorisation in Integral Domains](factorisation-in-integral-domains.md) stops chains of principal ideals, a special case of tenet 6; [Polynomial Rings](polynomial-rings.md) supplies the Noetherian examples and uses fractions in Gauss's lemma; [Modules](../04-modules-and-representations/modules.md) localise just as rings do.

## Common misconceptions

- **"Localisation only adds elements."** R → S⁻¹R kills every element annihilated by some s ∈ S. In ℤ/6 the set {1, 3} is multiplicative, and inverting 3 kills 2 and 4, leaving ℤ/2.
- **"A subring of a Noetherian ring is Noetherian."** k[x₁, x₂, …] is not Noetherian, yet it sits inside its field of fractions, which is.
- **"The points of Spec R should be its maximal ideals."** Without non-maximal primes such as (0) in ℤ, ring maps would not induce maps of spaces (tenet 5).

## Go deeper

- Michael Atiyah and Ian Macdonald, *Introduction to Commutative Algebra* (1969): localisation in chapter 3, Noetherian rings in chapter 7.
- Miles Reid, *Undergraduate Commutative Algebra* (1995): the geometry behind Spec and the Nullstellensatz.
- David Eisenbud, *Commutative Algebra with a View Toward Algebraic Geometry* (1995): the full theory, geometry kept in sight.
