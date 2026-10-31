# 03 Combinatorics and Graph Theory

> **Layer:** 03 Combinatorics and Graph Theory
> **Children:** [Enumeration](01-enumeration/README.md) · [Graph Theory](02-graph-theory/README.md) · [Discrete Probability](03-discrete-probability/README.md) · [Extremal Combinatorics](04-extremal-combinatorics/README.md)

## What this area is about
Combinatorics is the mathematics of finite structures: how many there are, how they are arranged, and which patterns they cannot avoid. Its objects are the simplest in mathematics, such as subsets, permutations, graphs and colourings. Its questions are easy to state and often very hard to answer. This layer covers four areas. Enumeration counts structures exactly, through bijections, inclusion–exclusion, generating functions and recurrences. Graph theory studies pairwise connections: connectivity, trees, matchings, flows, colourings and planar drawings. Discrete probability treats chance on finite and countable sets as weighted counting and turns it into a method for proving existence. Extremal combinatorics asks how large or disordered a structure can be before a pattern is forced, from Ramsey's theorem to Szemerédi's theorem on arithmetic progressions.

The basic abstraction is **the finite structure studied by counting and by extremal choice**. Most proofs here either count something in two ways, or choose an extreme object (a longest path, a smallest counterexample, a maximum matching) and show that it has the required property. The style of the field is a large stock of problems and techniques, held together by a few powerful methods rather than by a single axiomatic theory.

## Why this layer sits here
From [logic and proof](../00-logic-and-proof/README.md) it takes [induction](../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md), the most used proof method in the layer. From [sets and foundations](../01-sets-and-foundations/README.md) it takes [functions](../01-sets-and-foundations/01-sets-relations-and-functions/functions.md), [relations and orders](../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md), [equivalence relations](../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md) and [countable sets](../01-sets-and-foundations/02-infinity-and-cardinality/countable-sets.md). From [number systems](../02-number-systems/README.md) it takes the integers, the rationals, the complex numbers that appear as roots of recurrences, and the [primes](../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md) and [congruences](../02-number-systems/02-elementary-number-theory/modular-arithmetic.md) of additive combinatorics. It needs nothing else. Generating functions are treated as formal power series, which are infinite lists of coefficients with algebraic operations and no notion of convergence. Probability stays on finite and countable spaces, where every probability is a sum. So the layer can come before linear algebra and analysis, and it shows early that serious mathematics can be done with finite objects.

The layers above use it in turn. [Linear algebra](../04-linear-algebra/README.md) gets spectral graph theory, determinant formulas for counting spanning trees and matrices with non-negative entries. [Abstract algebra](../05-abstract-algebra/README.md) counts orbits of group actions and studies Cayley graphs. [Topology](../07-topology/README.md) generalises Euler's formula to the Euler characteristic. [Probability](../11-probability-and-statistics/README.md) extends discrete chance to measure theory. [Applied mathematics](../14-applied-and-computational-mathematics/README.md) uses flows, matchings and linear programming duality in optimisation, and random codes in information theory.

## How the children fit together
| Child | Its role in the whole | Depends on |
|---|---|---|
| [Enumeration](01-enumeration/README.md) | Exact counting: binomial coefficients, inclusion–exclusion, pigeonhole, generating functions, recurrences, classical sequences | Layers 00–02 |
| [Graph Theory](02-graph-theory/README.md) | Connections: connectivity, trees, matchings and flows, colouring and planarity | Enumeration |
| [Discrete Probability](03-discrete-probability/README.md) | Weighted counting: probability spaces, expectation and variance, the probabilistic method | Enumeration, graph theory |
| [Extremal Combinatorics](04-extremal-combinatorics/README.md) | Forced structure: Ramsey, Turán, Sperner, Szemerédi, Green–Tao | All three above |

```
            enumeration
           /           \
   graph theory ────> discrete probability
           \           /
       extremal combinatorics
```

Enumeration comes first because every later area counts. Graph theory adds the main object of study. Discrete probability reinterprets counting as averaging, and the probabilistic method applies it to graphs. Extremal combinatorics draws on all three: upper bounds come from counting and graph structure, and lower bounds come from random constructions. Read top to bottom, the layer moves from exact answers (how many trees on n labelled vertices?) to asymptotic ones (how large must n be to force a monochromatic K₅?). Some of the latter are open as of 2026.

## Connections to neighbouring layers
- [00 Logic and Proof](../00-logic-and-proof/README.md): induction, the pigeonhole principle, and combinatorial independence results such as the Paris–Harrington theorem.
- [01 Sets and Foundations](../01-sets-and-foundations/README.md): graphs are relations, posets are orders, and infinite Ramsey theory is set theory.
- [02 Number Systems](../02-number-systems/README.md): partitions, Möbius inversion and Euler's φ, and the primes in additive combinatorics.
- [04 Linear Algebra](../04-linear-algebra/README.md): adjacency and Laplacian matrices, the matrix-tree theorem, and the linear algebra method for set families.
- [05 Abstract Algebra](../05-abstract-algebra/README.md): orbit counting, representation theory of the symmetric group, and finite fields in extremal constructions.
- [07 Topology](../07-topology/README.md): Euler's formula, graphs on surfaces, and the topological proof of Kneser's conjecture.
- [11 Probability and Statistics](../11-probability-and-statistics/README.md): discrete probability grows into the measure-theoretic theory.
- [14 Applied and Computational Mathematics](../14-applied-and-computational-mathematics/README.md): network flows, linear programming duality, codes and learning theory.

## Connections across layers
- Higher: Szemerédi's theorem links to [ergodic theory](../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md) and [Fourier analysis on groups](../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md); Green–Tao and sumsets link to [analytic number theory](../12-number-theory-and-algebraic-geometry/README.md); the four colour theorem is a landmark of [computers and proof](../15-mathematics-in-context/computers-and-proof.md).
- In other fields: this layer underlies [discrete mathematics for computing](../../cs-first-principles/01-mathematical-foundations/03-discrete-mathematics/README.md) and [graph algorithms](../../cs-first-principles/05-algorithms-and-data-structures/05-graph-algorithms/README.md).

## Cross-cutting threads
- [Induction and recursion](../CROSS-CUTTING.md#induction-and-recursion): recurrences, leaf removal and smallest counterexamples.
- [Invariants](../CROSS-CUTTING.md#invariants): degree parity, Euler's V − E + F and the chromatic number.
- [Duality](../CROSS-CUTTING.md#duality): Hall, König, Menger, max-flow min-cut and Dilworth.
- [Existence and construction](../CROSS-CUTTING.md#existence-and-construction): bijective proofs, augmenting paths and the non-constructive probabilistic method.
- [Extremal principles and optimisation](../CROSS-CUTTING.md#extremal-principles-and-optimisation): extremal choices in proofs and extremal problems as results.
- [Randomness and averaging](../CROSS-CUTTING.md#randomness-and-averaging): linearity of expectation and random constructions.
- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): odd cycles, Kuratowski's forbidden graphs and Ramsey's theorem.
- [Dictionaries between fields](../CROSS-CUTTING.md#dictionaries-between-fields): generating functions link counting to algebra, and Furstenberg's correspondence links density to dynamics.
- [Infinity and size](../CROSS-CUTTING.md#infinity-and-size): König's lemma and infinite Ramsey theory.
