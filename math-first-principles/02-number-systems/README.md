# 02 Number Systems

> **Layer:** 02 Number Systems
> **Children:** [Constructing the Numbers](01-constructing-the-numbers/README.md) · [Elementary Number Theory](02-elementary-number-theory/README.md)

## What this area is about

This layer is where the two roots of the knowledge base first produce the objects everyone uses. From logic it takes induction; from set theory it takes quotients, completions and the counting of infinite sets. With these it builds the number systems in order, ℕ, ℤ, ℚ, ℝ and ℂ, shows that each is characterised by a few axioms and is unique up to isomorphism, and then looks beyond ℂ to the quaternions, the octonions and the p-adic numbers. Its second area studies the integers themselves: divisibility, primes, congruences, quadratic reciprocity and Diophantine equations, using nothing beyond ℤ, induction and a little algebra.

The basic abstraction is **the number system as a structure fixed by its axioms**. "The real numbers" means any complete ordered field, and all of them are isomorphic, so the question of what a real number really is (a cut, a class of Cauchy sequences, an infinite decimal) has many equally good answers and does not matter afterwards. The same habit, define by properties, construct one model, prove uniqueness, recurs in every later layer.

## Why this layer sits here

Everything below is about language and size; everything above needs numbers. [00 Logic and Proof](../00-logic-and-proof/README.md) supplies induction, which is the fifth Peano axiom, and the methods of proof used throughout. [01 Sets and Foundations](../01-sets-and-foundations/README.md) supplies von Neumann's model of ℕ, the equivalence classes that build ℤ and ℚ, and Cantor's theorem that ℝ is uncountable while ℚ and the algebraic numbers are not.

Elementary number theory sits here, rather than with algebraic and analytic number theory in layer 12, because it needs nothing beyond ℤ and induction. Ideals, class groups and the zeta function need rings and Galois theory (05) and complex analysis (09), so they wait. The split by method keeps both halves in dependency order, and the pointers forward mark the places where the elementary theory reaches its limits: the failure of unique factorisation in ℤ[√−5], the prime number theorem, and Fermat's Last Theorem.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Constructing the Numbers](01-constructing-the-numbers/README.md) | builds ℕ, ℤ, ℚ, ℝ and ℂ, sorts numbers into algebraic and transcendental, and extends to ℍ, 𝕆 and ℚₚ | 00 induction, 01 quotients and cardinality |
| [Elementary Number Theory](02-elementary-number-theory/README.md) | divisibility, primes, ℤ/n, Fermat and Euler, reciprocity, Diophantine equations | ℕ and ℤ from the first area |

```
   00 induction              01 sets, quotients, cardinality
          │                              │
          └──────────────┬───────────────┘
                         ▼
   ℕ ──► ℤ ──► ℚ ──► ℝ ──► ℂ ──► ℍ, 𝕆        (constructing the numbers)
         │      │                 ℚₚ
         ▼      ▼
   divisibility ──► primes, ℤ/n ──► Fermat–Euler ──► reciprocity ──► Diophantine
                                              (elementary number theory)
```

The first area runs up the ladder; the second stops at the second rung and looks closely. Most of the second area needs only ℤ, but irrationality of √2 uses ℚ, the sum-of-two-squares theorem is factorisation in ℤ[i] ⊂ ℂ, and congruences modulo pᵏ are approximations in ℚₚ. In the other direction, the transcendence and irrationality proofs of the first area use divisibility arguments from the second.

## Connections to neighbouring layers

- **[00 Logic and Proof](../00-logic-and-proof/README.md):** induction defines ℕ and proves existence of factorisations; infinite descent is induction run backwards.
- **[01 Sets and Foundations](../01-sets-and-foundations/README.md):** quotients build ℤ, ℚ and ℝ; cardinality separates countable ℚ̄ from uncountable ℝ.
- **[03 Combinatorics and Graph Theory](../03-combinatorics-and-graph-theory/README.md):** the pigeonhole principle proves Thue's lemma; counting units uses inclusion–exclusion.
- **[04 Linear Algebra](../04-linear-algebra/README.md):** ℂ is ℝ², quaternions act on ℝ³, and finite fields ℤ/p are scalars.
- **[05 Abstract Algebra](../05-abstract-algebra/README.md):** groups, rings and fields abstract ℤ/n, Bézout and fields of fractions; Galois theory explains why the fundamental theorem of algebra needs analysis.
- **[06 Real Analysis](../06-real-analysis/README.md):** starts from the completeness of ℝ built here.
- **[12 Number Theory and Algebraic Geometry](../12-number-theory-and-algebraic-geometry/README.md):** algebraic, analytic and arithmetic-geometric number theory continue the second area.
- **[13 Structure and Metamathematics](../13-structure-and-metamathematics/README.md):** non-standard models of arithmetic and Hilbert's tenth problem.
- **[14 Applied and Computational Mathematics](../14-applied-and-computational-mathematics/README.md):** cryptography runs on modular arithmetic; numerical analysis on floating-point approximations of ℝ.

## Connections across layers

Two results here are limits that recur higher up. Every complete ordered field is ℝ, and every finite-dimensional associative real division algebra is ℝ, ℂ or ℍ: classification theorems with very short lists. And Hilbert's tenth problem, solved negatively in 1970, shows that number theory contains the halting problem, a fact developed in [13](../13-structure-and-metamathematics/02-computability-and-incompleteness/undecidable-problems.md) and in the [computer science tree](../../cs-first-principles/02-theory-of-computation/03-computability/halting-problem-and-undecidability.md). Computers meet this layer constantly: [machine integers](../../cs-first-principles/03-digital-logic/01-number-representation/integers-and-twos-complement.md) are ℤ/2ʷ and [floating-point numbers](../../cs-first-principles/03-digital-logic/01-number-representation/floating-point.md) are a finite subset of ℚ standing in for ℝ.

## Cross-cutting threads

- [Equivalence and quotients](../CROSS-CUTTING.md#equivalence-and-quotients): ℤ, ℚ, ℝ and ℤ/n are all quotients.
- [Completeness and compactness](../CROSS-CUTTING.md#completeness-and-compactness): ℝ and ℚₚ complete ℚ for different notions of size.
- [Existence and construction](../CROSS-CUTTING.md#existence-and-construction): build a model, then prove uniqueness up to isomorphism.
- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): irrationality, transcendence, congruence obstructions and undecidability.
- [Local to global](../CROSS-CUTTING.md#local-to-global): the Chinese remainder theorem and the Hasse principle.
- [Decomposition and classification](../CROSS-CUTTING.md#decomposition-and-classification): unique factorisation and the theorems of Frobenius and Hurwitz.
- [Induction and recursion](../CROSS-CUTTING.md#induction-and-recursion): ℕ is where induction lives, and Euclid's algorithm is the first recursion.
