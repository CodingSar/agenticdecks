# Large Cardinals

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Model theory and independence](README.md)
> **Builds on:** [Ordinal numbers and transfinite induction](../../01-sets-and-foundations/02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md), [Cardinal numbers](../../01-sets-and-foundations/02-infinity-and-cardinality/cardinal-numbers.md), [Zermelo–Fraenkel set theory](../../01-sets-and-foundations/03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md), [Gödel's incompleteness theorems](../02-computability-and-incompleteness/godels-incompleteness-theorems.md), [Forcing and independence](forcing-and-independence.md)
> **Enables:** [Categories and functors](../01-category-theory/categories-and-functors.md), [Philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md), [Open problems](../../15-mathematics-in-context/open-problems.md)

## Essence

A large cardinal is an infinite cardinal so big that its existence cannot be proved in Zermelo–Fraenkel set theory with choice (ZFC), usually because a set of that size would contain a model of ZFC. Large cardinal axioms are the natural way to strengthen set theory: they continue the axiom of infinity upward, they are linearly ordered by consistency strength in every known case, and the stronger ones settle questions about sets of real numbers that ZFC leaves open. They do not settle the continuum hypothesis (CH), but they calibrate the strength of almost every other statement independent of ZFC.

## Core tenets

1. **Inaccessible cardinals are closed under the operations that build sets.** An uncountable cardinal κ is (strongly) inaccessible if it is regular, so not a union of fewer than κ smaller sets, and a strong limit, so 2^λ < κ for every λ < κ. Then V_κ, the sets of rank below κ, is closed under power sets and replacement, and is a model of ZFC. These are the Grothendieck universes of [category theory](../01-category-theory/categories-and-functors.md).

2. **ZFC cannot prove that inaccessibles exist, if it is consistent.** If ZFC proved that an inaccessible κ exists, it would prove that V_κ is a model of ZFC, hence prove Con(ZFC), contradicting Gödel's second theorem. More strongly, ZFC cannot even prove Con(ZFC) → Con(ZFC + an inaccessible exists), unless the latter theory is inconsistent: otherwise that theory, which proves Con(ZFC), would prove its own consistency.

3. **Measurable cardinals are defined by elementary embeddings.** Stanisław Ulam (1930) called κ measurable if there is a non-principal ultrafilter on κ closed under intersections of fewer than κ sets. Equivalently there is an elementary embedding j: V → M into a transitive class M, with κ the least ordinal moved; the ultrafilter is U = {X ⊆ κ : κ ∈ j(X)}, and conversely M is the ultrapower of V by U. Measurable cardinals are inaccessible and have many inaccessibles below them. Kenneth Kunen (1971) showed with the axiom of choice that no non-trivial j: V → V exists, which bounds the hierarchy from above.

4. **A measurable cardinal is incompatible with V = L.** Dana Scott (1961) proved that if a measurable cardinal exists, not every set is constructible. If V = L and κ is the least measurable, with j: V → M, then M is an inner model, so M = L = V; by elementarity j(κ) is the least measurable cardinal in M = V, yet j(κ) > κ, a contradiction. Large cardinals thus point away from L, which is part of why many set theorists reject V = L.

5. **Large cardinals decide questions about sets of reals.** In L there is a well-ordering of the reals simple enough (Δ¹₂) to yield non-measurable sets defined by short formulas. Donald Martin (1970) showed that a measurable cardinal makes every game on natural numbers with a coanalytic winning set determined. Martin and John Steel (1989) derived determinacy for all projective sets from infinitely many Woodin cardinals, so every projective set is then Lebesgue measurable and has the perfect set property. Under such cardinals the theory of the reals cannot be changed by forcing.

6. **The consistency-strength hierarchy is linear in practice.** Theories are compared by which proves the consistency of which. Familiar statements fall at precise levels: Solovay (1970) showed, assuming an inaccessible, that it is consistent with ZF and dependent choice that every set of reals is Lebesgue measurable, and Shelah (1984) showed the inaccessible is needed; the axiom of determinacy is equiconsistent with infinitely many Woodin cardinals. That all natural theories line up in this way is an observation, not a theorem, as of 2026.

   ```
   inaccessible < Mahlo < weakly compact < measurable < Woodin < supercompact
   ```

7. **The case for large cardinals is partly intrinsic, partly extrinsic.** They follow from reflection principles, the idea that any property of the universe should hold of some set; and they are justified by their consequences, a unified theory of the projective sets. Reinhardt cardinals, embeddings j: V → V, are inconsistent with choice by Kunen's theorem; whether they are consistent with ZF without choice is open as of 2026.

## Key concepts

| Term | Meaning |
|---|---|
| Inaccessible cardinal | An uncountable regular strong limit cardinal |
| V_κ | The sets of rank below κ; a model of ZFC when κ is inaccessible |
| Measurable cardinal | Carries a κ-complete non-principal ultrafilter |
| Elementary embedding | A map j preserving the truth of every formula |
| Critical point | The least ordinal moved by j |
| Woodin cardinal | A cardinal in the strength range that yields projective determinacy |
| Consistency strength | T is stronger than S if T proves Con(S) |

## How it fits

- **Below:** It continues the [ordinals](../../01-sets-and-foundations/02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md) and [cardinals](../../01-sets-and-foundations/02-infinity-and-cardinality/cardinal-numbers.md) of [ZFC](../../01-sets-and-foundations/03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md) past what ZFC can prove, as [Gödel's theorem](../02-computability-and-incompleteness/godels-incompleteness-theorems.md) forces.
- **Above:** The [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) asks what justifies new axioms, and the search for axioms deciding CH is among the [open problems](../../15-mathematics-in-context/open-problems.md).
- **Siblings:** [Forcing](forcing-and-independence.md) shows what large cardinals cannot settle, and [category theory](../01-category-theory/categories-and-functors.md) uses inaccessibles for universes.

## Common misconceptions

- **"Large cardinals are about very big numbers with no effect on ordinary mathematics."**: They imply new arithmetical statements, such as their own consistency, and settle the measurability of projective sets of reals.
- **"Large cardinals settle the continuum hypothesis."**: By the Lévy–Solovay theorem, small forcing preserves them, and such forcing can make CH true or false.

## Go deeper

- Akihiro Kanamori, *The Higher Infinite* (1994; 2nd edition 2003): the standard reference.
- Thomas Jech, *Set Theory* (3rd millennium edition, 2003): large cardinals in the context of the whole subject.
- Penelope Maddy, "Believing the Axioms, I" and "II", *Journal of Symbolic Logic* (1988): the arguments for new axioms.
