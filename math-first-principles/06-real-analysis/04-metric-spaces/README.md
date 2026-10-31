# Metric Spaces

> **Layer:** [06 Real Analysis](../README.md) › Metric Spaces
> **Children:** [Metric spaces and continuity](metric-spaces-and-continuity.md) · [Completeness and the contraction mapping principle](completeness-and-the-contraction-mapping-principle.md) · [Compactness in metric spaces](compactness-in-metric-spaces.md)

## What this area is about

The theorems of one-variable analysis seem to be about numbers, but their proofs use very little of ℝ: a distance, the triangle inequality, completeness, and the fact that closed bounded intervals trap sequences. This area isolates those ingredients. A metric space is any set with a distance obeying three axioms, and once the definitions of limit and continuity are phrased through the distance, they apply unchanged to points of ℝⁿ, to continuous functions, to binary strings and to p-adic numbers.

Two properties then do most of the work. Completeness says that sequences which ought to converge do converge, and its sharpest form is the contraction mapping principle, which finds solutions by iteration. Compactness says that every sequence has a convergent subsequence, and it gives maxima, uniform continuity and, through the Arzelà–Ascoli theorem, convergent sequences of functions. Between them they supply most of the existence theorems of analysis.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Metric spaces and continuity](metric-spaces-and-continuity.md) | The axioms, the main examples, open and closed sets, three equivalent forms of continuity | Sequences, continuity, inequalities (area 01) |
| [Completeness and the contraction mapping principle](completeness-and-the-contraction-mapping-principle.md) | Cauchy sequences, completions, and Banach's fixed-point theorem with its error bound | Metric spaces and continuity; the real numbers (layer 02) |
| [Compactness in metric spaces](compactness-in-metric-spaces.md) | Sequential and cover compactness, Heine–Borel, extreme values, Heine–Cantor, Arzelà–Ascoli | Metric spaces and continuity; completeness |

```
           limits and convergence  (area 01)
                        │
          metric spaces and continuity
                        │
   completeness and the contraction mapping principle
                        │
          compactness in metric spaces
            (= complete + totally bounded)
```

Start with the first child, which sets up the language and the examples that later leaves test their theorems against: the sup and L¹ metrics on functions, the discrete metric, and ℚ. Completeness comes next because compactness is defined partly in terms of it: a metric space is compact if and only if it is complete and totally bounded. The contraction mapping principle is the first serious theorem in the area and the first time a fixed point is found by an argument that works in any complete space. Compactness then upgrades the theorems of [continuity](../01-limits-and-convergence/continuity.md) from [a, b] to every compact space, and shows, by counterexamples in ℓ² and C[0, 1], that in infinite dimensions closed and bounded is no longer enough.

This area deliberately does not depend on [calculus of several variables](../03-calculus-of-several-variables/README.md). The arrows run the other way: the inverse function theorem there is proved by a contraction, and existence of constrained extrema rests on compactness.

## Connections to sibling areas

- [Limits and convergence](../01-limits-and-convergence/README.md): every definition here generalises one there. Bolzano–Weierstrass becomes compactness, the Cauchy criterion becomes completeness, and uniform convergence becomes convergence in the sup metric.
- [Calculus of one variable](../02-calculus-of-one-variable/README.md): the fundamental theorem of calculus turns a differential equation into an integral equation, which the contraction principle solves.
- [Calculus of several variables](../03-calculus-of-several-variables/README.md): uses the contraction principle for the inverse and implicit function theorems, and compactness for the existence of extrema.

## Connections across layers

This area sits between analysis and topology. [Topological spaces](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md) keep only the open sets and drop the distance; [compactness](../../07-topology/01-point-set-topology/compactness.md) is defined there by open covers, and [metrisability](../../07-topology/01-point-set-topology/separation-axioms-and-metrisability.md) asks which topologies come from a metric. Complete normed spaces are [Banach spaces](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md), where the [Baire category theorem](../../09-advanced-analysis/03-functional-analysis/hahn-banach-and-baire-category.md) drives the main results. The contraction principle proves [existence and uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md) for differential equations, and compactness proves the [existence of minimisers](../../10-differential-equations-and-dynamics/03-calculus-of-variations/existence-of-minimisers.md). The p-adic metric leads to [p-adic numbers](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/p-adic-numbers-and-local-fields.md), and the Hamming metric to [error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md).

## Cross-cutting threads

- [Abstraction and generalisation](../../CROSS-CUTTING.md#abstraction-and-generalisation): a metric space keeps exactly what the proofs about ℝ used, and nothing more.
- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): the two properties that make limits exist, stated in their natural generality.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): the contraction principle constructs its fixed point by iteration, while compactness proves existence without a construction.
- [Local to global](../../CROSS-CUTTING.md#local-to-global): finite subcovers turn bounds near each point into bounds on the whole space.
