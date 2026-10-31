# Extremal Combinatorics

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › Extremal Combinatorics
> **Children:** [Ramsey theory](ramsey-theory.md) · [Extremal graph theory](extremal-graph-theory.md) · [Posets and extremal set theory](posets-and-extremal-set-theory.md) · [Additive combinatorics](additive-combinatorics.md)

## What this area is about
Extremal combinatorics asks how large or how disordered a finite structure can be before some pattern is forced. How many vertices force a monochromatic clique in any two-colouring? How many edges force a triangle? How many subsets of an n-set can avoid containing one another? How dense must a set of integers be to contain a progression of length k? Each answer has two halves: an upper bound proved by an argument that applies to every structure, and a construction, often random or algebraic, showing that the bound is close to the truth. Where the halves meet the answer is exact, as in Mantel's, Turán's, Sperner's and Erdős–Ko–Rado's theorems. Where they do not meet, the gap is a research frontier. Diagonal Ramsey numbers are the best-known example, and their gap is open as of 2026. The area is where Erdős's style of mathematics, with many simply stated problems and inventive methods, has had the most influence.

## How the children fit together
| Child | Its role in the whole | Depends on |
|---|---|---|
| [Ramsey theory](ramsey-theory.md) | Colouring forces structure: Ramsey numbers, van der Waerden, infinite Ramsey and independence | Pigeonhole, graphs, the probabilistic method |
| [Extremal graph theory](extremal-graph-theory.md) | Density forces structure: Mantel, Turán, Erdős–Stone, regularity and removal | Ramsey theory, colouring |
| [Posets and extremal set theory](posets-and-extremal-set-theory.md) | Families of sets: Dilworth, Sperner, Erdős–Ko–Rado, the linear algebra method | Orders, matchings, counting |
| [Additive combinatorics](additive-combinatorics.md) | Arithmetic structure: sumsets, Freiman, Szemerédi, Green–Tao | Ramsey theory, extremal graph theory |

```
   ramsey theory ──────────────> additive combinatorics
        |                                 ^
        v                                 |
   extremal graph theory ─────────────────┘

   posets and extremal set theory  (parallel strand on families of sets)
```

Ramsey theory comes first because it asks the weakest question: does any colouring avoid a pattern? Extremal graph theory sharpens colouring to density, asking for the threshold rather than mere existence, and its regularity lemma is the strongest structural tool in the area. Additive combinatorics combines the two strands in the integers. Van der Waerden's colouring theorem becomes Szemerédi's density theorem, and the graph removal lemma proves Roth's theorem. Posets and extremal set theory runs in parallel on families of subsets. Its tools are duality between chains and antichains, averaging over random orderings, and linear algebra.

## Connections to sibling areas
- [Enumeration](../01-enumeration/README.md): binomial coefficients and double counting are the basic bounding tools, and pigeonhole is the simplest Ramsey theorem.
- [Graph theory](../02-graph-theory/README.md): colouring supplies the chromatic number that governs Turán densities, and König's theorem proves Dilworth's theorem.
- [Discrete probability](../03-discrete-probability/README.md): random constructions give the lower bounds, and entropy arguments have recently solved problems in additive combinatorics and extremal set theory.

## Connections across layers
- Below: [orders](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md) and [primes](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md).
- Above: algebraic constructions use [finite fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md); the linear algebra method uses [linear independence](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md); Kneser's conjecture uses [fixed-point theorems](../../07-topology/02-algebraic-topology/fixed-point-theorems.md); Szemerédi's theorem has proofs through [Fourier analysis on groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md) and [ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md); Green–Tao meets [sieves](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/sieves-and-additive-problems.md); the Paris–Harrington theorem links to [incompleteness](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md); shattering links to [learning theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md).

## Cross-cutting threads
- [Extremal principles and optimisation](../../CROSS-CUTTING.md#extremal-principles-and-optimisation): every theorem here is a maximum under a constraint.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): complete disorder is impossible, and Turán graphs show which patterns can be avoided.
- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): random constructions for lower bounds, and the dichotomy between structure and randomness.
- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): infinite Ramsey implies finite Ramsey by compactness.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): Furstenberg's correspondence turns density theorems into ergodic theory.
