# Measure-Theoretic Probability

> **Layer:** [11 Probability and Statistics](../README.md) › Measure-Theoretic Probability
> **Children:** [Probability Spaces and Kolmogorov's Axioms](probability-spaces-and-kolmogorovs-axioms.md) · [Random Variables and Distributions](random-variables-and-distributions.md) · [Independence and Zero–One Laws](independence-and-zero-one-laws.md) · [Conditional Expectation](conditional-expectation.md)

## What this area is about

Finite probability counts: the probability of an event is the sum of the probabilities of its outcomes. That breaks as soon as an experiment is infinite (toss a coin forever, pick a point of an interval, follow a particle), because every single outcome then has probability 0. This area rebuilds probability on measure theory, following Andrey Kolmogorov (1933), through four translations: chance becomes a measure of total mass 1; a random quantity becomes a measurable function with a law; independence becomes a product rule for σ-algebras; and information becomes a σ-algebra, with conditional expectation as projection onto it.

The unifying idea is that probability is measure theory plus two genuinely probabilistic notions, independence and conditioning. Everything else in the layer (limit theorems, stochastic processes, statistical inference) is assembled from what these four files set up.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Probability spaces and Kolmogorov's axioms](probability-spaces-and-kolmogorovs-axioms.md) | The framework (Ω, ℱ, P); why countable additivity, and why not every set is an event | Nothing in this layer |
| [Random variables and distributions](random-variables-and-distributions.md) | Measurable functions, laws, densities as Radon–Nikodym derivatives, characteristic functions | Probability spaces |
| [Independence and zero–one laws](independence-and-zero-one-laws.md) | Product structure, the Borel–Cantelli lemmas, and why tail events have probability 0 or 1 | Probability spaces, random variables |
| [Conditional expectation](conditional-expectation.md) | Conditioning on information as orthogonal projection; the Borel–Kolmogorov paradox | Random variables, independence |

Read them in order. The first fixes the stage and the second puts numbers on it. The third and fourth describe the two ways random variables relate to one another: not at all (independence) or through shared information (conditioning). The two meet in one rule: E[X ∣ 𝒢] = E[X] when X is independent of 𝒢, so knowing 𝒢 does not change the best prediction of X.

```
                 (Ω, ℱ, P)   probability space
                /                         \
   X : Ω → ℝ measurable             σ-algebras 𝒢 ⊆ ℱ
   law μ, F, density, φ             (information)
               |                          |
   independence:                   conditional expectation:
   product rule for σ-algebras     projection X ↦ E[X ∣ 𝒢]
                \                        /
              E[X ∣ 𝒢] = E[X]  when X is independent of 𝒢
```

## Connections to sibling areas

- **[Limit theorems](../02-limit-theorems/README.md):** take independent sequences from here, use the Borel–Cantelli lemmas to turn summable bounds into almost sure statements, and use characteristic functions to prove the central limit theorem.
- **[Stochastic processes](../03-stochastic-processes/README.md):** Kolmogorov's extension theorem builds a process as a measure on a space of paths; filtrations model time; the Markov and martingale properties are both statements about conditional expectation.
- **[Statistical inference](../04-statistical-inference/README.md):** a statistical model is a family of laws; a posterior is a regular conditional distribution; the Rao–Blackwell theorem and least squares are both the Pythagorean theorem for a projection.

## Connections across layers

From below, the area uses the [measure and integration](../../09-advanced-analysis/01-measure-and-integration/README.md) of 09 (σ-algebras, the Lebesgue integral, Lᵖ spaces, the Radon–Nikodym theorem), [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md) for projection, the [inner-product spaces](../../04-linear-algebra/03-inner-product-spaces/README.md) of 04 for the finite-dimensional picture, and the [discrete probability](../../03-combinatorics-and-graph-theory/03-discrete-probability/README.md) of 03, which it generalises. The [axiom of choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md) produces a set with no probability, and Solovay's [forcing](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md) model in 13 shows that, granted an inaccessible cardinal, some choice is needed to do so.

Upward, what probability *means* is a question for the [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md), while [mathematical finance](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/mathematical-finance.md) and [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md) in 14 are written in this language. The computer-science view of the same material is the [probability](../../../cs-first-principles/01-mathematical-foundations/06-probability-and-statistics/probability.md) leaf of the sibling tree.

## Cross-cutting threads

- [Abstraction and generalisation](../../CROSS-CUTTING.md#abstraction-and-generalisation): probability becomes measure theory with total mass 1, and finite probability is the special case.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): Vitali's set shows that no rotation-invariant probability is defined on every subset of the circle.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): extension theorems build infinite product measures, and Radon–Nikodym proves that conditional expectations exist without giving a formula.
- [Infinity and size](../../CROSS-CUTTING.md#infinity-and-size): null events can be uncountable, so probability is a size that does not see cardinality.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): conditioning is orthogonal projection, which turns prediction into Hilbert-space geometry.
- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): zero–one laws show that the long-run behaviour of independent trials is deterministic.
