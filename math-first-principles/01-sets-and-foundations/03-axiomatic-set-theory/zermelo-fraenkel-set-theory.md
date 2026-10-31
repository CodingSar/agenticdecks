# Zermelo–Fraenkel Set Theory

> **Layer:** [01 Sets and Foundations](../README.md) › [Axiomatic Set Theory](README.md)
> **Builds on:** [Paradoxes and naive set theory](paradoxes-and-naive-set-theory.md), [Ordinal numbers and transfinite induction](../02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md), [Predicate logic and quantifiers](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md), [Axioms, definitions and theorems](../../00-logic-and-proof/03-the-axiomatic-method/axioms-definitions-and-theorems.md), [Consistency and independence](../../00-logic-and-proof/03-the-axiomatic-method/consistency-and-independence.md)
> **Enables:** [The axiom of choice](the-axiom-of-choice.md), [Natural numbers and the Peano axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md), [Models and the Löwenheim–Skolem theorems](../../13-structure-and-metamathematics/03-model-theory-and-independence/models-and-the-lowenheim-skolem-theorems.md), [Forcing and independence](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md), [Gödel's incompleteness theorems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md)

## Essence

Zermelo–Fraenkel set theory (ZF) is a first-order theory with one relation symbol, ∈, and a short list of axioms saying which sets exist. Zermelo proposed the first version in 1908 to avoid the paradoxes; Fraenkel and Skolem added replacement in 1922, and foundation took its present form with von Neumann in the 1920s. With the axiom of choice it becomes ZFC (Zermelo–Fraenkel set theory with choice), in which essentially all of ordinary mathematics can be written. Its intended model is the cumulative hierarchy, built in stages indexed by ordinals. ZFC cannot prove its own consistency and leaves questions such as the continuum hypothesis (CH) open.

## Core tenets

1. **A few axioms rebuild ordinary mathematics.** Pairing and union give {a, b} and a ∪ b; with separation, ordered pairs and Cartesian products follow. Infinity gives ω, which is ℕ; power set gives 𝒫(ℕ), hence functions ℕ → ℕ and sets of rationals. From there ℤ and ℚ are quotients, ℝ is a set of Dedekind cuts, and functions, spaces and measures are sets of these. No new axiom is needed until choice.

2. **The cumulative hierarchy is the intended picture.** Define V₀ = ∅, V_(α+1) = 𝒫(V_α), and V_λ = the union of earlier stages at limits λ. The rank of a set is the stage at which it first appears. Foundation says every set has a rank, so the universe is the union of the V_α:

```
stage      size
V₀         0          the empty set
V₁         1          {∅}
V₂         2
V₃         4
V₄         16
V₅         65,536     = 2^16
V_ω        ℵ₀         the hereditarily finite sets
V_(ω+1)    2^ℵ₀       includes every subset of ℕ
```

3. **Replacement is what lets constructions run transfinitely.** It says the image of a set under a definable map is a set. Without it, ω + ω cannot be proved to exist: V_(ω+ω) satisfies every axiom except replacement and contains no ω + ω. Replacement is used whenever a [transfinite recursion](../02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md) runs past ω, and it matters below the realm of large sets: Martin (1975) proved Borel determinacy, a statement about sets of reals, and Friedman (1971) showed that any proof needs uncountably many iterations of the power set.

4. **Encodings are chosen for convenience, and they produce junk theorems.** With von Neumann's numerals, 2 = {0, 1} and 3 = {0, 1, 2}, so "2 ∈ 3" is a theorem. Nobody believes 2 is literally a set; what matters is that the encoding has the right properties, such as Peano's axioms for ω. Any two encodings of ℕ satisfying those axioms are isomorphic, so no theorem of arithmetic depends on the choice.

5. **Consistency is relative.** By Gödel's second incompleteness theorem, ZFC cannot prove its own consistency unless it is inconsistent. What can be proved are relative results: if ZF is consistent then so is ZFC (Gödel, 1938, using the constructible universe L), and so is ZF with the negation of choice (Cohen, 1963, using [forcing](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md)).

6. **Natural questions are independent of ZFC.** CH, that every infinite set of reals is countable or of the size of ℝ, is neither provable nor refutable. Shelah (1974) showed the same for the Whitehead problem in abelian group theory, and the existence of large cardinals cannot be proved from ZFC. An independent statement is one the axioms do not decide; whether it has a "true" answer is a philosophical question, not a mathematical one.

7. **ZF has countable models, which is not a contradiction.** If ZFC is consistent, the [Löwenheim–Skolem theorem](../../13-structure-and-metamathematics/03-model-theory-and-independence/models-and-the-lowenheim-skolem-theorems.md) gives it a countable model, in which a set satisfies "uncountable". This is Skolem's paradox (1922). It dissolves once "uncountable" is read inside the model: the model lacks a bijection with ω, although one exists outside it.

## Key concepts

| Term | Meaning |
|---|---|
| Extensionality | sets with the same members are equal |
| Pairing, union | {a, b} exists; the union of the members of a set exists |
| Power set | the set of all subsets of a set exists |
| Infinity | a set containing ∅ and closed under x ↦ x ∪ {x} exists |
| Separation | {x ∈ A : φ(x)} exists for each formula φ |
| Replacement | the image of a set under a definable map is a set |
| Foundation | every non-empty set has an ∈-minimal element |
| Choice | every family of non-empty sets has a choice function |
| Cumulative hierarchy | the stages V_α, each the power set of the last |
| Rank | the stage at which a set first appears |
| Relative consistency | if one theory is consistent then so is another |

## How it fits

- **Below:** ZF is a theory in [predicate logic](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md), built as [axioms](../../00-logic-and-proof/03-the-axiomatic-method/axioms-definitions-and-theorems.md) chosen to avoid [the paradoxes](paradoxes-and-naive-set-theory.md); its stages are indexed by [ordinals](../02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md); its consistency questions belong to [consistency and independence](../../00-logic-and-proof/03-the-axiomatic-method/consistency-and-independence.md).
- **Above:** [the natural numbers](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md) are ω; [incompleteness](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md), [Löwenheim–Skolem](../../13-structure-and-metamathematics/03-model-theory-and-independence/models-and-the-lowenheim-skolem-theorems.md) and [forcing](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md) study what ZFC can and cannot prove.
- **Siblings:** [the axiom of choice](the-axiom-of-choice.md) is the one axiom set apart; [type theory](type-theory-and-alternative-foundations.md) is the main alternative foundation.

## Common misconceptions

- **"ZF says that numbers are sets"**: it shows that sets can model numbers; mathematics uses only their structure.
- **"An independent statement has no answer"**: it has none from these axioms; stronger axioms may decide it, as replacement decides that ω + ω exists.
- **"ZFC has been proved consistent"**: only relative to stronger theories; its consistency is an assumption supported by long use, as of 2026.

## Go deeper

- Herbert B. Enderton, *Elements of Set Theory* (1977): the axioms and how ordinary mathematics is built from them.
- Kenneth Kunen, *Set Theory: An Introduction to Independence Proofs* (1980): the cumulative hierarchy, L and forcing.
- Thomas Jech, *Set Theory* (3rd millennium edition, 2003): the comprehensive reference.
