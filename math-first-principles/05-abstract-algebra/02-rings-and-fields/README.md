# Rings and Fields

> **Layer:** [05 Abstract Algebra](../README.md) › Rings and Fields
> **Children:** [Rings and Ideals](rings-and-ideals.md) · [Factorisation in Integral Domains](factorisation-in-integral-domains.md) · [Polynomial Rings](polynomial-rings.md) · [Field Extensions](field-extensions.md) · [Finite Fields](finite-fields.md)

## What this area is about

Groups have one operation; most of arithmetic has two. A ring adds and multiplies, as ℤ, polynomials and matrices do, and a field also divides, as ℚ, ℝ, ℂ and ℤ/p do. This area takes the familiar facts of school arithmetic, such as division with remainder, unique factorisation into primes and the roots of polynomials, and asks which hypotheses each one really needs. The answers are precise: ideals replace numbers, quotients by maximal ideals manufacture fields, unique factorisation holds in some rings and fails in others, and field extensions become vector spaces whose dimensions obey a multiplication law.

The area ends with two complete classifications: every finite field is 𝔽_q for a prime power q, and every algebraic extension sits inside an algebraic closure. These are the raw materials of Galois theory, number theory, algebraic geometry and coding theory.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Rings and Ideals](rings-and-ideals.md) | Rings, ideals as kernels, quotient rings, prime and maximal ideals | Quotient groups |
| [Factorisation in Integral Domains](factorisation-in-integral-domains.md) | When factorisation is unique: Euclidean ⇒ principal ideal domain ⇒ unique factorisation; ℤ[√−5] fails | Rings and ideals |
| [Polynomial Rings](polynomial-rings.md) | F[x] as a Euclidean domain; irreducibility tests; building fields as F[x]/(f) | Factorisation |
| [Field Extensions](field-extensions.md) | Degree, the tower law, splitting fields, algebraic closure, separability | Polynomial rings |
| [Finite Fields](finite-fields.md) | Existence and uniqueness of 𝔽_q; its cyclic multiplicative group | Field extensions |

The order is a funnel. Rings and ideals supply the general language; factorisation studies the best-behaved rings; polynomial rings over a field are the most useful of those, and their quotients by irreducible polynomials are fields. Field extensions then measure how far a new field is from an old one by a dimension, and finite fields are the case where everything can be computed.

```
rings and ideals ──> factorisation ──> polynomial rings ──> field extensions ──> finite fields
        │                                     │                     │
        v                                     v                     v
     modules                         solvability (Eisenstein)   Galois theory
```

## Connections to sibling areas

- [Groups](../01-groups/README.md): a ring is an abelian group under addition, ideals mirror normal subgroups, and the units of a ring form a group; Lagrange's theorem proves that 𝔽_q^× has order dividing q − 1.
- [Galois Theory](../03-galois-theory/README.md): it studies field extensions through their automorphism groups; finite fields give its simplest example.
- [Modules and Representations](../04-modules-and-representations/README.md): a module is a vector space over a ring; the structure theorem works because the ring is a principal ideal domain.

## Connections across layers

- Below: ℤ/n and Euclid's algorithm from [elementary number theory](../../02-number-systems/02-elementary-number-theory/divisibility-and-the-euclidean-algorithm.md); degree as [dimension](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md); maximal ideals from [the axiom of choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md).
- Above: [ideals and the class group](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/ideals-and-the-class-group.md) and [varieties](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/varieties-and-the-nullstellensatz.md) grow from this area; [error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md) and [cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md) compute in finite fields.

## Cross-cutting threads

- [Equivalence and quotients](../../CROSS-CUTTING.md#equivalence-and-quotients): quotient rings and fields built as F[x]/(f).
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): Kronecker's construction of roots, and algebraic closures by Zorn's lemma.
- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): unique factorisation, and the classification of finite fields.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): ideals of polynomial rings as geometry.
