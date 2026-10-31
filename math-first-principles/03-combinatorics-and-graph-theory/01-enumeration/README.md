# Enumeration

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › Enumeration
> **Children:** [Counting principles and binomial coefficients](counting-principles-and-binomial-coefficients.md) · [Inclusion–exclusion and the pigeonhole principle](inclusion-exclusion-and-the-pigeonhole-principle.md) · [Generating functions](generating-functions.md) · [Recurrence relations](recurrence-relations.md) · [Combinatorial sequences](combinatorial-sequences.md)

## What this area is about
Enumeration answers "how many?" exactly. Its raw material is finite sets and bijections, and its basic move is to count the same set in two ways or to exhibit a bijection with a set already counted. From the sum and product rules it builds binomial coefficients, corrects for overlaps with inclusion–exclusion, packages whole sequences of counts as formal power series, and solves the recurrences that counting problems produce. It also contains the pigeonhole principle, the first tool for showing that something must exist rather than counting how many there are. Nothing here needs a limit: generating functions are treated as formal algebraic objects, and analysis enters only when one asks how fast a count grows.

## How the children fit together
| Child | Its role in the whole | Depends on |
|---|---|---|
| [Counting principles and binomial coefficients](counting-principles-and-binomial-coefficients.md) | Sum, product and bijection rules; C(n, k), the binomial theorem and double counting | Layers 00–02 only |
| [Inclusion–exclusion and the pigeonhole principle](inclusion-exclusion-and-the-pigeonhole-principle.md) | Exact counting of unions by signed sums; existence by overfilling boxes | Counting principles |
| [Generating functions](generating-functions.md) | Sequences as formal power series, turning constructions into equations | Counting principles |
| [Recurrence relations](recurrence-relations.md) | Defining and solving sequences step by step; linear recurrences are rational series | Generating functions |
| [Combinatorial sequences](combinatorial-sequences.md) | The catalogue: Fibonacci, Catalan, Stirling, Bell and partition numbers | All four above |

```
            counting principles
             /               \
   inclusion–exclusion    generating functions
   and pigeonhole               |
             \            recurrence relations
              \               /
            combinatorial sequences
```

Counting principles come first because everything else is built from the sum and product rules and the binomial coefficients. Two methods then branch off. Inclusion–exclusion repairs the sum rule when sets overlap and, through the union bound, becomes the first inequality of probability; its sibling, the pigeonhole principle, turns counting into existence proofs. Generating functions take the opposite route: instead of correcting one count, they encode a whole sequence of counts in one algebraic object, so that a recursive description of the objects becomes an equation for the series. Recurrence relations sit next to them because the two languages are equivalent for linear recurrences: a sequence satisfies a linear recurrence with constant coefficients exactly when its generating function is rational. Combinatorial sequences close the area by showing all four methods at work on the numbers that recur everywhere, and by marking where exact methods stop, as with the partition numbers, whose growth needs analysis.

## Connections to sibling areas
- [Graph theory](../02-graph-theory/README.md): graphs are counted with these tools (Cayley's formula for labelled trees, the handshake lemma as a double count), and Catalan numbers count binary trees.
- [Discrete probability](../03-discrete-probability/README.md): a uniform finite probability is a ratio of counts, the union bound is truncated inclusion–exclusion, and probability generating functions are generating functions.
- [Extremal combinatorics](../04-extremal-combinatorics/README.md): the pigeonhole principle is the base case of Ramsey theory, and double counting proves Sperner's theorem and the Kővári–Sós–Turán bound.

## Connections across layers
- Below, the area uses [mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md), [functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md) and [primes](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md).
- Above, formal power series are a ring studied in [polynomial rings](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md); counting up to symmetry is [group actions](../../05-abstract-algebra/01-groups/group-actions.md); linear recurrences are matrix powers in [eigenvalues and diagonalisation](../../04-linear-algebra/02-determinants-and-eigenvalues/eigenvalues-and-diagonalisation.md); asymptotics come from [singularities and residues](../../09-advanced-analysis/02-complex-analysis/singularities-and-residues.md); partition congruences from [modular forms](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/modular-forms.md); sieves in [analytic number theory](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/sieves-and-additive-problems.md).
- In computing, the same tools size search spaces and analyse algorithms ([discrete mathematics for computing](../../../cs-first-principles/01-mathematical-foundations/03-discrete-mathematics/README.md)).

## Cross-cutting threads
- [Induction and recursion](../../CROSS-CUTTING.md#induction-and-recursion): recursive decompositions become recurrences and functional equations.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): bijective proofs construct; pigeonhole proofs only show existence.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): constructions on objects translate into algebra on series.
- [Equivalence and quotients](../../CROSS-CUTTING.md#equivalence-and-quotients): dividing by k! counts subsets as classes of ordered selections.
