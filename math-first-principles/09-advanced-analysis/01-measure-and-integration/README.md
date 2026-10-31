# Measure and Integration

> **Layer:** [09 Advanced Analysis](../README.md) › Measure and Integration
> **Children:** [Measure and σ-Algebras](measure-and-sigma-algebras.md) · [The Lebesgue Integral](the-lebesgue-integral.md) · [Lᵖ Spaces](lp-spaces.md) · [The Radon–Nikodym Theorem](the-radon-nikodym-theorem.md) · [Hausdorff Dimension and Fractals](hausdorff-dimension-and-fractals.md)

## What this area is about

The Riemann integral of [layer 06](../../06-real-analysis/README.md) works for continuous functions on intervals, but it breaks under limits: a pointwise limit of integrable functions need not be integrable, and the space of Riemann integrable functions is not complete. Measure theory repairs this at the root. It first decides which sets have a size and requires sizes to add up over countable disjoint unions. Integration is then defined by measuring the sets where a function takes given values. The resulting Lebesgue integral comes with theorems that say exactly when a limit can be taken inside an integral.

The same machine, applied to a measure of total mass 1, is probability theory; applied to functions, it produces the complete spaces Lᵖ on which functional and harmonic analysis are built. It also has a price and a bonus. The price is that, under the axiom of choice, not every set can be measured. The bonus is that one construction gives measures of every dimension, including fractional ones.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Measure and σ-Algebras](measure-and-sigma-algebras.md) | Which sets have a size, and how to build Lebesgue measure | Riemann integral, countability, choice |
| [The Lebesgue Integral](the-lebesgue-integral.md) | Integration by measuring level sets; exchanging limit and integral | Measure |
| [Lᵖ Spaces](lp-spaces.md) | Functions as points of complete normed spaces | Lebesgue integral |
| [The Radon–Nikodym Theorem](the-radon-nikodym-theorem.md) | When one measure is a density times another | Integral, Lᵖ |
| [Hausdorff Dimension and Fractals](hausdorff-dimension-and-fractals.md) | Measures and dimensions of every real order | Measure, metric spaces |

```
          measure and σ-algebras ─────────────────► Hausdorff dimension
                     │                             (same construction,
                     ▼                              new outer measure)
            the Lebesgue integral
             │                 │
             ▼                 ▼
         Lᵖ spaces ──────► Radon–Nikodym
   (to functional analysis)  (to conditional expectation in 11)
```

The narrative is one of restriction followed by power. Vitali's set shows that length cannot be defined on every subset of ℝ, so [measure](measure-and-sigma-algebras.md) is defined on a σ-algebra, and Carathéodory's construction produces Lebesgue measure on a σ-algebra large enough for any set that arises in practice. [Integration](the-lebesgue-integral.md) then needs only the measure of sets like {f > t}, and countable additivity becomes monotone and dominated convergence. Those theorems prove the Riesz–Fischer theorem, so the [Lᵖ spaces](lp-spaces.md) are complete. The [Radon–Nikodym theorem](the-radon-nikodym-theorem.md) relates two measures on one space, and its densities are L¹ functions. [Hausdorff measure](hausdorff-dimension-and-fractals.md) takes the outer-measure step and changes only the weight of a cover, from length to (diameter)ˢ.

## Connections to sibling areas

- **[Complex Analysis](../02-complex-analysis/README.md):** complex analysis needs only path integrals of continuous functions, but Hardy spaces and the Riemann mapping theorem's boundary behaviour use measure; Fourier series are the boundary values of holomorphic functions on the disc.
- **[Functional Analysis](../03-functional-analysis/README.md):** Lᵖ spaces are its founding examples, and L² is the model Hilbert space; von Neumann's proof of the Radon–Nikodym theorem is a Riesz representation.
- **[Harmonic Analysis](../04-harmonic-analysis/README.md):** Fourier coefficients and transforms are Lebesgue integrals, Plancherel's theorem lives in L², and Haar measure is the translation-invariant measure on a group.

## Connections across layers

Downward, the area rests on [the Riemann integral](../../06-real-analysis/02-calculus-of-one-variable/the-riemann-integral.md) and [metric spaces](../../06-real-analysis/04-metric-spaces/metric-spaces-and-continuity.md) in 06, and on [countable sets](../../01-sets-and-foundations/02-infinity-and-cardinality/countable-sets.md) and [the axiom of choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md) in 01. Upward, [probability spaces](../../11-probability-and-statistics/01-measure-theoretic-probability/probability-spaces-and-kolmogorovs-axioms.md) and [conditional expectation](../../11-probability-and-statistics/01-measure-theoretic-probability/conditional-expectation.md) in 11 are measure theory with total mass 1; [Sobolev spaces](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md) and [ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md) in 10 need Lᵖ and invariant measures; [forcing](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md) in 13 settles what can be measured without choice; [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md) in 14 estimate integrals by sampling.

## Cross-cutting threads

- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): monotone and dominated convergence say when a limit passes through an integral.
- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): the Riesz–Fischer theorem makes Lᵖ complete where Riemann integration was not.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): Vitali's set rules out a length for every subset of ℝ.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): Carathéodory's theorem builds measures from their values on simple sets.
- [Infinity and size](../../CROSS-CUTTING.md#infinity-and-size): measure, cardinality and dimension are three different notions of how big a set is.
- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): expectation is a Lebesgue integral.
