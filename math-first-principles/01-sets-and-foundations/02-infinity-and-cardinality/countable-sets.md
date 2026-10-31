# Countable Sets

> **Layer:** [01 Sets and Foundations](../README.md) › [Infinity and Cardinality](README.md)
> **Builds on:** [Functions](../01-sets-relations-and-functions/functions.md), [Relations and orders](../01-sets-relations-and-functions/relations-and-orders.md), [Mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md)
> **Enables:** [Cantor's diagonal argument](cantors-diagonal-argument.md), [Cardinal numbers](cardinal-numbers.md), [Algebraic and transcendental numbers](../../02-number-systems/01-constructing-the-numbers/algebraic-and-transcendental-numbers.md), [Computable functions and the Church–Turing thesis](../../13-structure-and-metamathematics/02-computability-and-incompleteness/computable-functions-and-the-church-turing-thesis.md)

## Essence

Two sets have the same size when their elements can be matched one to one, which agrees with counting for finite sets and surprises for infinite ones. A set is countable when it can be listed as a sequence x₀, x₁, x₂, …, repeats allowed, or equivalently when it injects into ℕ. The integers, the rationals, all finite strings over a finite alphabet and all algebraic numbers are countable: each looks larger than ℕ, but a clever listing shows it is not. Countability is the size of everything that can be finitely described, from formulas and proofs to programs.

## Core tenets

1. **Size is defined by bijection, and an infinite set can be as large as a proper part of itself.** ∣A∣ = ∣B∣ means some bijection A → B exists. For finite sets this agrees with counting: by the pigeonhole principle, proved by induction on n, there is no bijection between {1, …, m} and {1, …, n} when m ≠ n. For infinite sets it overrides intuition about parts: n ↦ 2n matches ℕ with the even numbers, as Galileo noticed for n ↦ n² (1638), and Dedekind (1888) took this property as the definition of an infinite set.

2. **Countable means "fits inside ℕ".** A is countable if some injection A → ℕ exists; for non-empty A this is equivalent to a surjection ℕ → A, a listing that may repeat. From a surjection, send each a to the least n listed as a; from an injection, list the elements in the order of their codes. Every infinite S ⊆ ℕ is in bijection with ℕ, by listing S in increasing order, which uses the well-ordering of ℕ. So a countable set is either finite or of exactly the size of ℕ, written ℵ₀ (aleph-null), and every subset of a countable set is countable.

3. **Pairs of naturals are countable, so ℤ and ℚ are too.** The Cantor pairing function π(m, n) = (m + n)(m + n + 1)/2 + n is a bijection ℕ × ℕ → ℕ: it walks the diagonals m + n = 0, 1, 2, … in turn, so (m, n) gets the number of pairs on earlier diagonals plus its position on its own.

```
n=3 │ 9
n=2 │ 5  8
n=1 │ 2  4  7
n=0 │ 0  1  3  6
    └──────────── m = 0, 1, 2, 3
```

   By induction ℕᵏ is countable for every k. ℤ is listed as 0, 1, −1, 2, −2, …, and ℚ is the image of ℤ × (ℕ ∖ {0}) under (p, q) ↦ p/q, hence countable.

4. **A countable union of countable sets is countable, but the proof makes choices.** If A₀, A₁, … are countable, choose a listing of each Aₙ and send the m-th element of Aₙ to (n, m); the union then injects into the countable set ℕ × ℕ. "Choose a listing of each" makes infinitely many arbitrary choices and needs the axiom of countable choice: Feferman and Levy built a model of Zermelo–Fraenkel set theory (ZF), the standard axioms without choice, in which ℝ is a countable union of countable sets. When the listings come with the sets, no choice is needed.

5. **Everything finitely describable is countable.** The set Σ* of finite strings over a finite alphabet Σ is the union of the finite sets Σⁿ, listed by length and then alphabetically, with no choice involved. So there are countably many formulas, proofs, programs and definitions. The algebraic numbers, roots of non-zero integer polynomials, are countable because each polynomial is a finite string with finitely many roots (Cantor, 1874). Since ℝ is uncountable, as [Cantor's diagonal argument](cantors-diagonal-argument.md) shows, most reals are transcendental, and most are computed by no program.

6. **ℵ₀ is the smallest infinite size.** Every infinite set A contains a countably infinite subset: pick a₀ ∈ A, then a₁ ≠ a₀, then a₂ outside {a₀, a₁}, and so on, which never gets stuck because A is infinite. Making all these choices at once needs a weak form of choice (countable choice suffices). Without any choice there can be infinite sets with no countably infinite subset, so "infinite" and Dedekind's "equinumerous with a proper subset" can come apart.

7. **ℚ is the only countable dense order without endpoints.** Cantor proved that any two countable dense linear orders without endpoints are order-isomorphic; the standard proof is the back-and-forth method: list both sets, then alternately extend a finite order-preserving matching to cover the next unmatched element of one side, then of the other; density and the lack of endpoints guarantee a partner always exists. So ℚ, ℚ ∩ (0, 1) and the dyadic rationals k/2ⁿ have the same order type. Each hypothesis matters: ℤ is not dense, ℚ ∩ [0, 1] has endpoints, and ℝ is uncountable. The method returns in [model theory](../../13-structure-and-metamathematics/03-model-theory-and-independence/models-and-the-lowenheim-skolem-theorems.md), where it shows that certain theories have exactly one countable model up to isomorphism.

## Key concepts

| Term | Meaning |
|---|---|
| Equinumerous, ∣A∣ = ∣B∣ | some bijection A → B exists |
| Finite | equinumerous with {1, …, n} for some n ∈ ℕ, where n = 0 gives ∅ |
| Countable | injects into ℕ: finite or countably infinite |
| Countably infinite | equinumerous with ℕ; of size ℵ₀ |
| Pairing function | a bijection ℕ × ℕ → ℕ |
| Dedekind-infinite | equinumerous with a proper subset of itself |
| Algebraic number | a root of a non-zero polynomial with integer coefficients |
| Countable choice | from any sequence of non-empty sets, a sequence of chosen elements |

## How it fits

- **Below:** bijections and injections come from [functions](../01-sets-relations-and-functions/functions.md), the increasing listing of a subset of ℕ from the well-ordering in [relations and orders](../01-sets-relations-and-functions/relations-and-orders.md), and finite counting from [mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md).
- **Above:** [measure theory](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md) rests on countable additivity, and every countable set of reals has Lebesgue measure zero; [computability](../../13-structure-and-metamathematics/02-computability-and-incompleteness/computable-functions-and-the-church-turing-thesis.md) starts from the countability of programs, and the existence of non-computable functions is a counting argument.
- **Siblings:** [Cantor's diagonal argument](cantors-diagonal-argument.md) shows that not everything is countable; [cardinal numbers](cardinal-numbers.md) extend the comparison to all sizes; [ordinal numbers](ordinal-numbers-and-transfinite-induction.md) well-order a countable set in many ways: ω, ω + 1, ω + ω, …

## Common misconceptions

- **"A countable set can be listed in increasing order"**: ℚ has none, since between any two rationals lie others; a listing ignores the order.
- **"A countable union of countable sets is obviously countable"**: the proof picks a listing of each set, and without countable choice the statement can fail.

## Go deeper

- Paul R. Halmos, *Naive Set Theory* (1960): the short classic on cardinality.
- Karel Hrbacek and Thomas Jech, *Introduction to Set Theory* (3rd edition, 1999): countable sets, choice and cardinality with full proofs.
