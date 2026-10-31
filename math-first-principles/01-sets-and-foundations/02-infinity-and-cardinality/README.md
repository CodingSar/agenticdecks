# Infinity and Cardinality

> **Layer:** [01 Sets and Foundations](../README.md) › Infinity and Cardinality
> **Children:** [Countable sets](countable-sets.md) · [Cantor's diagonal argument](cantors-diagonal-argument.md) · [Cardinal numbers](cardinal-numbers.md) · [Ordinal numbers and transfinite induction](ordinal-numbers-and-transfinite-induction.md)

## What this area is about

This area answers two questions that finite mathematics never has to separate: how many elements a set has, and how long a well-ordered list of them is. For finite sets the answers are the same number. For infinite sets they come apart, and both need new definitions. Size becomes "there is a bijection", which makes ℕ, ℤ and ℚ the same size and makes ℝ strictly larger. Length becomes the shape of a well-order, which makes ω and ω + 1 different although both are countable.

The unifying idea is that *size and length are defined by maps, not by counting*. Size is preserved by bijections, length by order isomorphisms, and every theorem here is about which maps exist and which cannot.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Countable sets](countable-sets.md) | bijection as "same size"; ℕ, ℤ, ℚ, ℕ × ℕ and finite strings all have size ℵ₀ | functions, orders |
| [Cantor's diagonal argument](cantors-diagonal-argument.md) | ∣X∣ < ∣𝒫(X)∣, ℝ is uncountable; the pattern behind undecidability and incompleteness | countable sets |
| [Cardinal numbers](cardinal-numbers.md) | comparison, arithmetic and the continuum 2^ℵ₀; the continuum hypothesis | countable sets, diagonal |
| [Ordinal numbers and transfinite induction](ordinal-numbers-and-transfinite-induction.md) | ω, ω + 1, …, ω₁; induction and recursion past the finite | orders, cardinals |

```
 countable sets ──► Cantor's diagonal argument ──► cardinal numbers
 (ℕ ≅ ℤ ≅ ℚ ≅ ℕ×ℕ)  (∣X∣ < ∣𝒫(X)∣, ℝ uncountable)   (≤, arithmetic, 2^ℵ₀, CH)
        │                                                │
        └──────────► ordinal numbers ◄───────────────────┘
                     (ω, ω+1, …, ω₁; transfinite induction)
```

Read in order. Countable sets show that many sets which look bigger than ℕ are not. The diagonal argument shows that some sets are bigger, and that there is no biggest. Cardinal numbers organise the resulting ladder of sizes, and ordinals supply the well-ordered scale on which, with choice, every cardinal sits. The last two leaves lean on each other: the cardinals leaf defines ∣A∣ as the least ordinal of that size, a forward pointer, while ω₁ and the ordinal arithmetic of the ordinals leaf use countability and size. A reader who prefers definitions before use can read the ordinals leaf first; otherwise read in order and return to tenet 1 of the cardinals leaf afterwards.

Two warnings run through the area. First, several innocent-looking steps (a countable union of countable sets is countable, every infinite set has a countably infinite subset, any two sizes are comparable) quietly use the axiom of choice. Second, the most natural question about sizes, the continuum hypothesis (CH) that nothing lies between ℵ₀ and 2^ℵ₀, cannot be settled by the standard axioms.

## Connections to sibling areas

- **[Sets, Relations and Functions](../01-sets-relations-and-functions/README.md)** supplies bijections, injections, well-orders and the power set. Cardinality is the quotient of sets by "there is a bijection", in the sense of the equivalence-relations leaf.
- **[Axiomatic Set Theory](../03-axiomatic-set-theory/README.md)** turns the paradoxes hidden here (no set of all sets, no set of all ordinals) into axioms. It states Zermelo–Fraenkel set theory (ZF), which needs replacement to prove that every well-order has an ordinal, and adds the axiom of choice to get ZFC, which makes all cardinals comparable.

## Connections across layers

- **Below:** induction along ℕ is [mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md), and transfinite induction extends it.
- **Above:** counting proves that most reals are [transcendental](../../02-number-systems/01-constructing-the-numbers/algebraic-and-transcendental-numbers.md); the finite case of "same size" is the [pigeonhole principle](../../03-combinatorics-and-graph-theory/01-enumeration/inclusion-exclusion-and-the-pigeonhole-principle.md); dimension is the size of a [basis](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md); [measure](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md) separates length from size, as the Cantor set shows; [computability](../../13-structure-and-metamathematics/02-computability-and-incompleteness/computable-functions-and-the-church-turing-thesis.md) begins from the countability of programs; [forcing](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md) and [large cardinals](../../13-structure-and-metamathematics/03-model-theory-and-independence/large-cardinals.md) take up what the standard axioms leave open.

## Cross-cutting threads

- [Infinity and size](../../CROSS-CUTTING.md#infinity-and-size): bijection, not intuition about parts, decides size.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): the diagonal argument is the template for proofs that something cannot exist.
- [Induction and recursion](../../CROSS-CUTTING.md#induction-and-recursion): transfinite induction is induction along any well-order.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): diagonal proofs construct their witness, while comparability of sizes needs choice.
