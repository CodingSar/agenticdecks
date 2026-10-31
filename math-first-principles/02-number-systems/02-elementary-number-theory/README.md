# Elementary Number Theory

> **Layer:** [02 Number Systems](../README.md) › Elementary Number Theory
> **Children:** [Divisibility and the Euclidean Algorithm](divisibility-and-the-euclidean-algorithm.md) · [Primes and Unique Factorisation](primes-and-unique-factorisation.md) · [Modular Arithmetic](modular-arithmetic.md) · [Fermat, Euler and Primitive Roots](fermat-euler-and-primitive-roots.md) · [Quadratic Reciprocity](quadratic-reciprocity.md) · [Diophantine Equations](diophantine-equations.md)

## What this area is about

Elementary number theory studies the integers using nothing beyond ℤ itself, induction and a little algebra: no complex analysis, no algebraic geometry. "Elementary" describes the tools, not the difficulty. Its questions are about divisibility, primes, remainders and integer solutions of equations, and its answers form a short chain of theorems. Division with remainder gives Euclid's algorithm; the algorithm gives Bézout's identity; Bézout gives Euclid's lemma and hence unique factorisation, and also inverses modulo n and hence the arithmetic of ℤ/n. The finite groups (ℤ/n)ˣ give Fermat's and Euler's theorems and primitive roots; squares modulo p obey quadratic reciprocity; and all of these combine to solve, or to rule out solutions of, Diophantine equations.

The area is also where some of the oldest open problems live. Twin primes and Goldbach's conjecture, both open as of 2026, can be stated to a child, and Hilbert's tenth problem shows that no single method can settle every equation.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Divisibility and the Euclidean Algorithm](divisibility-and-the-euclidean-algorithm.md) | the root: division with remainder, greatest common divisors, Bézout | ℕ and ℤ from the sibling area |
| [Primes and Unique Factorisation](primes-and-unique-factorisation.md) | the atoms of multiplication; Euclid's lemma; infinitely many primes | divisibility |
| [Modular Arithmetic](modular-arithmetic.md) | the rings ℤ/n, units, the Chinese remainder theorem | divisibility, primes |
| [Fermat, Euler and Primitive Roots](fermat-euler-and-primitive-roots.md) | the group of units: Euler's theorem, cyclicity modulo p, public-key cryptography | modular arithmetic |
| [Quadratic Reciprocity](quadratic-reciprocity.md) | which residues are squares, and the law linking p and q | Fermat, Euler and primitive roots |
| [Diophantine Equations](diophantine-equations.md) | the payoff: integer solutions, obstructions, undecidability | all of the above |

```
   division with remainder
            │
     Euclid's algorithm ──► continued fractions ──────────────────┐
            │                                                     │
     Bézout's identity                                            │
        │           │                                             │
   Euclid's lemma   inverses modulo n                             │
        │           │                                             │
   unique         ℤ/n and the Chinese remainder theorem           │
   factorisation    │                                             │
        │         Fermat–Euler, primitive roots                   │
        │           │                                             │
        │         quadratic reciprocity                           │
        │           │                                             │
        └───────────┴──────► Diophantine equations ◄──────────────┘
```

Bézout's identity is the hinge. One branch runs through Euclid's lemma to unique factorisation, the multiplicative structure of ℤ. The other runs through inverses to the finite rings ℤ/n, the additive structure seen through remainders. The two meet again in the last leaf, where factorisation, congruences, reciprocity and continued fractions each solve a family of equations. The leaves are ordered so that every proof uses only earlier ones.

## Connections to sibling areas

[Constructing the numbers](../01-constructing-the-numbers/README.md) supplies ℤ, the well-ordering of ℕ behind division with remainder, and the induction behind every existence proof here. In return, this area proves √2 irrational by divisibility, and its congruences modulo pᵏ are the finite shadows of the p-adic numbers in the sibling's last leaf. Gaussian integers ℤ[i] link sums of two squares to factorisation in ℂ.

## Connections across layers

- **Above in algebra:** [rings and ideals](../../05-abstract-algebra/02-rings-and-fields/rings-and-ideals.md) and [factorisation in integral domains](../../05-abstract-algebra/02-rings-and-fields/factorisation-in-integral-domains.md) (05) abstract Bézout and unique factorisation; [finite fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md) extend ℤ/p.
- **Above in number theory:** [algebraic number theory](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/ideals-and-the-class-group.md) repairs factorisation with ideals; [analytic number theory](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-prime-number-theorem.md) counts primes; [Fermat's Last Theorem](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/fermats-last-theorem.md) closes the oldest Diophantine question.
- **Logic:** [undecidable problems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/undecidable-problems.md) (13) contains Hilbert's tenth problem.
- **Applications:** [cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md) (14) and [number theory for computer science](../../../cs-first-principles/01-mathematical-foundations/03-discrete-mathematics/number-theory.md) run on modular exponentiation and the hardness of factoring.

## Cross-cutting threads

- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): every integer decomposes uniquely into primes, and ℤ/n into prime-power parts.
- [Local to global](../../CROSS-CUTTING.md#local-to-global): the Chinese remainder theorem assembles residues, and the Hasse principle asks when local solutions give global ones.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): congruences rule out solutions; Hilbert's tenth problem rules out an algorithm.
- [Induction and recursion](../../CROSS-CUTTING.md#induction-and-recursion): Euclid's algorithm is a recursion, and infinite descent is induction.
- [Invariants](../../CROSS-CUTTING.md#invariants): residues modulo n and the Legendre symbol are invariants that detect impossibility.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): reciprocity is the first entry in the dictionary that the Langlands programme extends.
