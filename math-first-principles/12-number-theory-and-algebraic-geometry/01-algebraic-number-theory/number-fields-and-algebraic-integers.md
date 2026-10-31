# Number Fields and Algebraic Integers

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Algebraic Number Theory](README.md)
> **Builds on:** [Field Extensions](../../05-abstract-algebra/02-rings-and-fields/field-extensions.md), [Rings and Ideals](../../05-abstract-algebra/02-rings-and-fields/rings-and-ideals.md), [Algebraic and Transcendental Numbers](../../02-number-systems/01-constructing-the-numbers/algebraic-and-transcendental-numbers.md), [Primes and Unique Factorisation](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md), [Determinants](../../04-linear-algebra/02-determinants-and-eigenvalues/determinants.md)
> **Enables:** [Ideals and the Class Group](ideals-and-the-class-group.md), [p-adic Numbers and Local Fields](p-adic-numbers-and-local-fields.md), [Class Field Theory](class-field-theory.md), [Schemes](../03-algebraic-geometry/schemes.md), [Cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md)

## Essence

A number field is a finite extension K of ℚ, such as ℚ(i) or ℚ(√−5). Inside it sits the ring of integers 𝒪_K, the analogue of ℤ: the elements that satisfy a monic polynomial with integer coefficients. Questions about ℤ often become simple in a larger ring: p = x² + y² says that p factors as (x + iy)(x − iy) in ℤ[i]. The price is that unique factorisation into irreducible elements can fail, and the subject grew out of repairing that failure. Two invariants from linear algebra, the norm and the discriminant, measure size and ramification, and a picture of 𝒪_K as a lattice makes the main finiteness theorems possible.

## Core tenets

1. **The algebraic integers in K form a ring.** Call α integral when it is a root of a monic polynomial in ℤ[x]. The polynomial of α + β is hard to write down, so closure needs a finiteness test: α is integral if and only if αM ⊆ M for some non-zero finitely generated ℤ-module M. If M is spanned by m₁, …, m_k, then α is an eigenvalue of the integer matrix expressing each αmᵢ in the mⱼ, so it is a root of a monic characteristic polynomial (the determinant trick). For integral α and β, the finitely generated module ℤ[α, β] is preserved by α + β and αβ.

2. **The ring of integers can be larger than it looks.** For square-free d, the ring of integers of ℚ(√d) is ℤ[√d] when d ≡ 2 or 3 mod 4, and ℤ[(1 + √d)/2] when d ≡ 1 mod 4. The reason is that a + b√d has minimal polynomial x² − 2a·x + (a² − d·b²), and integer coefficients allow half-integers a and b exactly when d ≡ 1 mod 4.

3. **Norm and trace are the determinant and trace of multiplication.** Multiplication by α is a ℚ-linear map of K, a vector space of dimension n = [K : ℚ]. Its determinant is the norm N(α) and its trace is Tr(α): the product and the sum of the n images of α under the embeddings K → ℂ. Both are integers for integral α, the norm is multiplicative, and the units are the elements of norm ±1. In ℤ[i], N(a + bi) = a² + b². If p ≡ 1 mod 4, then p divides some m² + 1 = (m + i)(m − i) but neither factor, so p is not prime in ℤ[i]. As ℤ[i] has unique factorisation, p = ππ′ with N(π) = p: a sum of two squares.

4. **𝒪_K is a lattice, and its discriminant records ramification.** 𝒪_K is free of rank n as a ℤ-module, with an integral basis ω₁, …, ωₙ. The discriminant d_K = det(Tr(ωᵢωⱼ)) does not depend on the basis, since a change of basis multiplies it by the square of a determinant ±1. For ℚ(√d), d_K = d when d ≡ 1 mod 4 and 4d otherwise. Its prime factors are exactly the ramified primes, those whose factorisation in 𝒪_K has a repeated factor. The real and complex embeddings place 𝒪_K in ℝⁿ as a lattice of covolume 2^(−r₂)·√∣d_K∣, where r₂ counts pairs of complex embeddings, so the [geometry of lattices](../../08-geometry/03-convex-and-discrete-geometry/lattices-and-sphere-packing.md) applies.

5. **Unique factorisation of elements can fail.** In ℤ[√−5], 6 = 2·3 = (1 + √−5)(1 − √−5). The four factors have norms 4, 9, 6 and 6. A proper factor of any of them would have norm 2 or 3, and a² + 5b² is never 2 or 3, so all four are irreducible. The only units are ±1, so the factorisations really differ. Dedekind's ideals restore uniqueness one level up ([the class group](ideals-and-the-class-group.md)).

6. **The units form a finitely generated group of known rank.** With r₁ real embeddings, Dirichlet's unit theorem says 𝒪_K^× ≅ μ_K × ℤ^(r₁ + r₂ − 1), where μ_K is the finite group of roots of unity in K. The proof maps u to the vector of the numbers log∣σ(u)∣ over the embeddings σ. The image lies in a hyperplane because N(u) = ±1; the hard part, done with Minkowski's convex body theorem, is that it is a full lattice there. For ℚ(√2) the units are ±(1 + √2)ᵏ, which solves Pell's equation x² − 2y² = ±1.

7. **Primes split as a polynomial factors mod p.** If 𝒪_K = ℤ[α] and α has minimal polynomial f, the Dedekind–Kummer theorem turns f ≡ ∏ gᵢ^(eᵢ) mod p, with distinct irreducible gᵢ, into p𝒪_K = ∏ 𝔭ᵢ^(eᵢ) with prime ideals 𝔭ᵢ = (p, gᵢ(α)). For ℤ[i] and x² + 1, a prime p ≡ 1 mod 4 splits into two primes, p ≡ 3 mod 4 stays prime, and 2 = −i(1 + i)² ramifies. The hypothesis can fail: Dedekind found a cubic field in which 2 splits into three primes, which in some ℤ[α] would need three distinct linear factors mod 2, and only x and x + 1 exist.

## Key concepts

| Term | Meaning |
|---|---|
| Number field | A finite extension K of ℚ, of degree n = [K : ℚ] |
| Algebraic integer | A root of a monic polynomial with integer coefficients |
| Ring of integers 𝒪_K | The algebraic integers in K, the analogue of ℤ |
| Norm N(α), trace Tr(α) | Determinant and trace of multiplication by α |
| Discriminant d_K | det(Tr(ωᵢωⱼ)) for an integral basis; its prime factors ramify |
| Unit | An invertible element of 𝒪_K, equivalently one of norm ±1 |
| Split, inert, ramified | A prime of ℤ factors into distinct primes, stays prime, or acquires a repeated factor |

## How it fits

- **Below:** [field extensions](../../05-abstract-algebra/02-rings-and-fields/field-extensions.md) give degrees; [unique factorisation in ℤ](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md) is what fails; [determinants](../../04-linear-algebra/02-determinants-and-eigenvalues/determinants.md) define norm and discriminant.
- **Above:** [schemes](../03-algebraic-geometry/schemes.md) treat 𝒪_K as the functions on an arithmetic curve. The number field sieve, the fastest known classical method for factoring the integers behind Rivest–Shamir–Adleman (RSA) [cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md), sieves in a number field.
- **Siblings:** [ideals](ideals-and-the-class-group.md) restore unique factorisation; [p-adic numbers](p-adic-numbers-and-local-fields.md) study one prime at a time; [class field theory](class-field-theory.md) describes the abelian extensions of K.

## Common misconceptions

- **"The integers of ℚ(√d) are the numbers a + b√d with a, b ∈ ℤ"**: for d ≡ 1 mod 4 half-integers are allowed. In ℤ[√−3], 2·2 = (1 + √−3)(1 − √−3) with irreducible factors, while the full ring ℤ[(1 + √−3)/2] has unique factorisation.
- **"Once unique factorisation fails, arithmetic is chaotic"**: prime ideals always factor uniquely, and a finite group measures the failure for elements.

## Go deeper

- Kenneth Ireland and Michael Rosen, *A Classical Introduction to Modern Number Theory* (2nd edition, 1990): a gentle road from congruences to number fields.
- Daniel A. Marcus, *Number Fields* (1977): the standard first course, built around exercises.
- Jürgen Neukirch, *Algebraic Number Theory* (1999): the modern graduate account, geometric throughout.
