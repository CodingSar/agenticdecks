# Cantor's Diagonal Argument

> **Layer:** [01 Sets and Foundations](../README.md) › [Infinity and Cardinality](README.md)
> **Builds on:** [Countable sets](countable-sets.md), [Functions](../01-sets-relations-and-functions/functions.md), [Direct proof, contraposition and contradiction](../../00-logic-and-proof/02-methods-of-proof/direct-proof-contraposition-and-contradiction.md)
> **Enables:** [Cardinal numbers](cardinal-numbers.md), [Paradoxes and naive set theory](../03-axiomatic-set-theory/paradoxes-and-naive-set-theory.md), [Undecidable problems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/undecidable-problems.md), [Gödel's incompleteness theorems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md), [Halting problem (CS)](../../../cs-first-principles/02-theory-of-computation/03-computability/halting-problem-and-undecidability.md)

## Essence

Given any list of objects of a certain kind, the diagonal argument builds a new object of that kind that differs from the n-th entry at the n-th place, so it is missing from the list. Applied to subsets it proves Cantor's theorem: no set maps onto its own power set, so there is no largest infinity. Applied to decimal expansions it proves that ℝ is uncountable; Cantor published the argument in 1891, for sequences of two symbols. The same move, a self-application followed by a twist, proves that the halting problem is undecidable and builds the self-referential sentence in Gödel's incompleteness theorem.

## Core tenets

1. **Cantor's theorem: no function X → 𝒫(X) is surjective.** Given f: X → 𝒫(X), let D = {x ∈ X : x ∉ f(x)}. If D = f(d) for some d, then d ∈ D ⇔ d ∉ f(d) ⇔ d ∉ D, a contradiction, so D is not in the range. Since x ↦ {x} is an injection X → 𝒫(X), we get ∣X∣ < ∣𝒫(X)∣. The proof is constructive (it names the missing set), uses no choice, and covers X = ∅, where 𝒫(∅) = {∅} has one element.

2. **The table picture explains the name.** Write a 1 in row f(x), column y, when y ∈ f(x). D is built by reading the diagonal and flipping every entry, so it differs from row n in column n:

```
          x₀  x₁  x₂  x₃  …
  f(x₀)  [1]  0   1   1
  f(x₁)   0  [0]  1   0
  f(x₂)   1   1  [1]  0
  f(x₃)   0   1   0  [1]
  D       0   1   0   0     ← differs from row n in column n
```

3. **ℝ is uncountable.** Given any list x₀, x₁, … of reals in (0, 1), define a decimal d = 0.d₀d₁d₂… with dₙ = 4 if the n-th digit of xₙ is 5, and dₙ = 5 otherwise. Then d differs from each xₙ at the n-th digit. Since d uses no 0s or 9s, its decimal expansion is unique, so the argument does not trip over 0.4999… = 0.5000…. Cantor's first proof (1874) used nested intervals instead; the diagonal form came in 1891 and applies to any set of sequences.

4. **One fixed-point theorem behind every diagonal argument.** Lawvere (1969) isolated the pattern: if e: A → Yᴬ is surjective, then every map g: Y → Y has a fixed point. Define h(a) = g(e(a)(a)); by surjectivity h = e(a₀) for some a₀, and then h(a₀) = g(e(a₀)(a₀)) = g(h(a₀)). Read contrapositively: since "not" on {0, 1} has no fixed point, no X maps onto {0, 1}ˣ ≅ 𝒫(X). Every hypothesis matters: the argument shows nothing about ℚ, because the diagonal number built from a list of rationals need not be rational, so it lies outside the set being listed.

5. **The halting problem is a diagonal argument.** List the programs P₀, P₁, … and suppose a program H decides whether Pₙ halts on input n. Build D: on input n, run H, and loop for ever if H says Pₙ halts on n, else stop. D is some Pₖ, and on input k it halts exactly when it does not. So no such H exists (Turing, 1936). The rows are programs, the columns inputs, and the twist is "halt ↔ loop"; see [undecidable problems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/undecidable-problems.md) and the computer science view in [halting problem and undecidability](../../../cs-first-principles/02-theory-of-computation/03-computability/halting-problem-and-undecidability.md).

6. **Gödel's diagonal lemma makes a sentence talk about itself.** In Peano arithmetic (PA), the first-order axioms for the natural numbers, every formula has a numerical code ⌜φ⌝. Let diag(x) be the code of the result of substituting x into the formula coded by x. Given φ(x), set θ(x) = φ(diag(x)), let k = ⌜θ⌝ and let G be θ(k). Then diag(k) = ⌜G⌝, so PA proves G ⇔ φ(⌜G⌝). Taking φ to say "is not provable" gives a sentence asserting its own unprovability, the core of [Gödel's first incompleteness theorem](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md) (1931).

7. **Russell's paradox is the diagonal applied to everything.** If there were a set V of all sets, take f: V → 𝒫(V) with f(x) = x when x is a set. The diagonal set D = {x : x ∉ x} is Russell's set, and the contradiction shows that V cannot exist. Equivalently, there is no largest cardinal.

8. **The first gap: ℵ₀ < 2^ℵ₀.** Binary expansions match 𝒫(ℕ) with ℝ up to a countable set, so ∣ℝ∣ = ∣𝒫(ℕ)∣ = 2^ℵ₀ > ℵ₀. The diagonal argument says the continuum is bigger than ℕ but not how much bigger. The continuum hypothesis (CH), that no set lies strictly between them in size, can be neither proved nor refuted from the standard axioms; see [cardinal numbers](cardinal-numbers.md).

## Key concepts

| Term | Meaning |
|---|---|
| Diagonal set | D = {x : x ∉ f(x)}, the set missing from the range of f |
| Cantor's theorem | ∣X∣ < ∣𝒫(X)∣ for every set X |
| Uncountable | not countable; ℝ and 𝒫(ℕ) are examples |
| Continuum, 2^ℵ₀ | the size of ℝ and of 𝒫(ℕ) |
| Fixed point | a point y with g(y) = y |
| Lawvere's theorem | a surjection A → Yᴬ forces every map Y → Y to have a fixed point |
| Halting problem | deciding whether a program halts on a given input; undecidable |
| Diagonal lemma | every formula φ(x) has a sentence G with PA ⊢ G ⇔ φ(⌜G⌝) |

## How it fits

- **Below:** the argument needs [countable sets](countable-sets.md) for what a list is, [functions](../01-sets-relations-and-functions/functions.md) for surjections and indicator functions, and [proof by contradiction](../../00-logic-and-proof/02-methods-of-proof/direct-proof-contraposition-and-contradiction.md).
- **Above:** it drives [undecidability](../../13-structure-and-metamathematics/02-computability-and-incompleteness/undecidable-problems.md), [incompleteness](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md), Tarski's undefinability of truth, and the time and space hierarchy theorems behind [complexity classes](../../../cs-first-principles/02-theory-of-computation/04-complexity/complexity-classes.md). It is the model case of [impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction).
- **Siblings:** [cardinal numbers](cardinal-numbers.md) turn ∣X∣ < ∣𝒫(X)∣ into an unending ladder of sizes; the Burali-Forti paradox in [ordinal numbers](ordinal-numbers-and-transfinite-induction.md) and Russell's paradox in [paradoxes and naive set theory](../03-axiomatic-set-theory/paradoxes-and-naive-set-theory.md) are diagonal arguments that rule out a set of everything.

## Common misconceptions

- **"The same argument shows ℚ is uncountable"**: the diagonal decimal built from a list of rationals is usually irrational, so it is not a rational missing from the list.
- **"It depends on the quirk that 0.999… = 1"**: the quirk is a nuisance, avoided by using only the digits 4 and 5; the argument for 𝒫(X) has no digits at all.
- **"It is non-constructive"**: it builds the missing object explicitly. Applied to a list of the algebraic numbers, it computes a specific transcendental number digit by digit.

## Go deeper

- Georg Cantor, "Über eine elementare Frage der Mannigfaltigkeitslehre" (1891): the original four-page diagonal paper.
- F. William Lawvere, "Diagonal arguments and Cartesian closed categories" (1969): the fixed-point theorem behind all of them.
- Noson S. Yanofsky, "A universal approach to self-referential paradoxes, incompleteness and fixed points", *Bulletin of Symbolic Logic* (2003): Lawvere's theorem with many examples, from the liar to the halting problem.
