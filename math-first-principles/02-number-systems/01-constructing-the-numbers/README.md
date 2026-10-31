# Constructing the Numbers

> **Layer:** [02 Number Systems](../README.md) › Constructing the Numbers
> **Children:** [Natural Numbers and the Peano Axioms](natural-numbers-and-the-peano-axioms.md) · [Integers and Rational Numbers](integers-and-rational-numbers.md) · [The Real Numbers](the-real-numbers.md) · [The Complex Numbers](the-complex-numbers.md) · [Algebraic and Transcendental Numbers](algebraic-and-transcendental-numbers.md) · [Extending Number Systems](extending-number-systems.md)

## What this area is about

This area builds the number systems instead of assuming them. It starts from the natural numbers, pinned down by Peano's axioms and modelled by von Neumann's sets, and climbs: ℤ and ℚ as quotients of pairs, ℝ by completing ℚ, ℂ as pairs of reals. Each step is forced by an equation the previous system cannot solve: x + 5 = 3 in ℕ, 5x = 3 in ℤ, x² = 2 in ℚ, x² = −1 in ℝ. Each step also costs something. ℤ loses the well-ordering of ℕ, ℝ loses countability and computability of most of its elements, and ℂ loses its order. After ℂ, which is algebraically closed, the area looks at where else one can go: inside ℂ, to sort its elements into algebraic and transcendental; upwards, to the quaternions and octonions; and sideways, to the p-adic completions of ℚ.

The point is not that anyone doubts that 2 + 2 = 4. It is that every number system is characterised by a few properties, and that each is unique up to isomorphism, so the familiar numbers can be defined, not merely used.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Natural Numbers and the Peano Axioms](natural-numbers-and-the-peano-axioms.md) | the base: zero, successor and induction, and a set-theoretic model | 00 induction, 01 sets |
| [Integers and Rational Numbers](integers-and-rational-numbers.md) | the first quotients: pairs of naturals, then fractions; √2 is irrational | natural numbers, 01 quotients |
| [The Real Numbers](the-real-numbers.md) | completion of ℚ by cuts or Cauchy sequences, both 1872; uniqueness | integers and rationals |
| [The Complex Numbers](the-complex-numbers.md) | ℝ² with a new multiplication; the fundamental theorem of algebra | the real numbers |
| [Algebraic and Transcendental Numbers](algebraic-and-transcendental-numbers.md) | which numbers are roots of rational polynomials; e and π are not | complex numbers, countability |
| [Extending Number Systems](extending-number-systems.md) | quaternions, octonions, the limits of Frobenius and Hurwitz, and the p-adics | complex and real numbers |

Four moves do all the work. **Quotient**: take formal pairs and identify those that should be equal, which gives ℤ from ℕ and ℚ from ℤ. **Completion**: add limits of Cauchy sequences, or fill the gaps by cuts, which gives ℝ, and with a different distance ℚₚ. **Adjunction**: add a root of an equation, which gives ℂ = ℝ(i). **Doubling**: the Cayley–Dickson construction, which gives ℂ from ℝ again and then ℍ and 𝕆.

```
   ℕ ──quotient──► ℤ ──quotient──► ℚ ──complete──► ℝ ──adjoin i──► ℂ ──double──► ℍ ──double──► 𝕆
   induction      subtraction     division   │    limits        roots    │      lose          lose
                                             │                           │      commutativity associativity
                                             └──complete for |·|ₚ──► ℚₚ  └── ℚ̄ ⊂ ℂ: the algebraic numbers
```

The order of the leaves follows the ladder. The first four build ℕ, ℤ, ℚ, ℝ and ℂ, each needing only its predecessor. The algebraic-and-transcendental leaf then looks inside ℂ, using the countability argument from 01 to show that almost every number is transcendental while proving it for any particular number is hard. The last leaf leaves the ladder, upwards and sideways, and explains why the upward road ends at dimension eight.

## Connections to sibling areas

[Elementary number theory](../02-elementary-number-theory/README.md) lives inside ℤ, built in the second leaf, and uses well-ordering from the first for division with remainder. Traffic runs both ways: irrationality of √2 is a divisibility argument, the p-adic numbers of the last leaf formalise working modulo every power of p, and the failure of unique factorisation in ℤ[√−5] is a statement about algebraic integers in the sense of the fifth leaf.

## Connections across layers

- **Below:** [mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md) (00) is the fifth Peano axiom; [equivalence relations and quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md) (01) build ℤ and ℚ; Cantor's counting (01) separates ℚ from ℝ.
- **Above:** [real analysis](../../06-real-analysis/README.md) (06) starts from the completeness of ℝ; [abstract algebra](../../05-abstract-algebra/README.md) (05) recasts fields of fractions, adjunction and the fundamental theorem of algebra; complex analysis (09) gives the slickest proof of that theorem; algebraic number theory (12) develops ℚₚ and ℚ̄.
- **Computing:** machine numbers are finite stand-ins for ℤ and ℝ; see [floating point](../../../cs-first-principles/03-digital-logic/01-number-representation/floating-point.md) in the computer science tree.

## Cross-cutting threads

- [Equivalence and quotients](../../CROSS-CUTTING.md#equivalence-and-quotients): ℤ, ℚ and ℝ by Cauchy sequences are all quotients.
- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): ℝ and ℚₚ are completions of ℚ.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): each system is built from the one below, then shown unique.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): no order on ℂ, no division algebra in dimension 3, no proof yet that e + π is irrational.
- [Infinity and size](../../CROSS-CUTTING.md#infinity-and-size): ℚ and ℚ̄ are countable, ℝ is not.
- [Induction and recursion](../../CROSS-CUTTING.md#induction-and-recursion): ℕ is the structure on which induction and recursion are defined.
