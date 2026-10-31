# The Axiom of Choice

> **Layer:** [01 Sets and Foundations](../README.md) › [Axiomatic Set Theory](README.md)
> **Builds on:** [Zermelo–Fraenkel set theory](zermelo-fraenkel-set-theory.md), [Ordinal numbers and transfinite induction](../02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md), [Cardinal numbers](../02-infinity-and-cardinality/cardinal-numbers.md), [Relations and orders](../01-sets-relations-and-functions/relations-and-orders.md), [Functions](../01-sets-relations-and-functions/functions.md)
> **Enables:** [Linear independence, bases and dimension](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md), [Compactness](../../07-topology/01-point-set-topology/compactness.md), [Measure and σ-algebras](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md), [Hahn–Banach and Baire category](../../09-advanced-analysis/03-functional-analysis/hahn-banach-and-baire-category.md), [Forcing and independence](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md)

## Essence

The axiom of choice (AC) says that for any family of non-empty sets there is a function picking one element from each. For finitely many sets this is provable, and for sets with a rule for picking it is unnecessary; AC is needed only for infinitely many arbitrary choices. Over Zermelo–Fraenkel set theory without choice (ZF) it is equivalent to the well-ordering theorem, to Zorn's lemma and to many statements from algebra and topology. It also produces objects nobody can describe, such as non-measurable sets and the Banach–Tarski decomposition. It is independent of ZF; adding it gives Zermelo–Fraenkel set theory with choice (ZFC).

## Core tenets

1. **Only infinitely many arbitrary choices need the axiom.** Russell's example: from infinitely many pairs of shoes one can choose the left shoe of each pair, but from infinitely many pairs of socks there is no rule, and a choice needs AC. Equivalent forms over ZF include "a product of non-empty sets is non-empty" and "every surjection has a right inverse", both from [functions](../01-sets-relations-and-functions/functions.md).

2. **Every set can be well-ordered (Zermelo, 1904).** Given a choice function c on the non-empty subsets of A, define by [transfinite recursion](../02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md) a_α = c(A ∖ {a_β : β < α}) until A is used up. The recursion must stop, because by Hartogs' theorem some ordinal does not inject into A. Conversely, a well-order of the union of a family gives a choice function: pick the least element of each set.

3. **Zorn's lemma: a partial order in which every chain has an upper bound has a maximal element.** From AC: climb transfinitely, using a choice function to pick a strict upper bound of the chain built so far; if the climb never reached a maximal element it would inject every ordinal into the order. Conversely, apply Zorn to partial choice functions ordered by extension; a maximal one is defined everywhere. The lemma is named after Zorn (1935); Hausdorff (1914) and Kuratowski (1922) had close relatives.

4. **Many familiar theorems are equivalent to AC over ZF.** Each of these implies AC, and AC implies each:
   - every vector space has a basis (Blass, 1984);
   - Tychonoff's theorem, that products of compact spaces are compact (Kelley, 1950);
   - every non-zero ring with 1 has a maximal ideal (Hodges, 1979), see [rings and ideals](../../05-abstract-algebra/02-rings-and-fields/rings-and-ideals.md);
   - any two sets are comparable in size (Hartogs, 1915).

   A basis of ℝ over ℚ, a Hamel basis, gives additive functions f(x + y) = f(x) + f(y) that are not linear.

5. **AC gives a set that cannot be measured.** Choose one point from each class of [0, 1] under x ~ y ⇔ x − y ∈ ℚ, giving the Vitali set V (1905). Its translates V + q for rationals q ∈ [−1, 1] are disjoint, contain [0, 1] and lie inside [−1, 2]. If V had length m, countable additivity and translation invariance would make the total a sum of countably many copies of m, either 0 or ∞, never between 1 and 3. So no translation-invariant [measure](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md) on all subsets of ℝ extends length.

6. **The Banach–Tarski paradox: a ball can be cut into five pieces and reassembled into two.** Banach and Tarski (1924) used a free group on two generators inside the rotations of space: the group splits into pieces that reassemble, by left multiplication, into two copies of itself. Choosing one point from each orbit transfers this to the ball, and five pieces is the minimum. No such paradox exists on the line or in the plane (Banach, 1923), because the groups of rigid motions there are solvable.

7. **AC is consistent and independent, and harmless for arithmetic.** Gödel (1938) showed that if ZF is consistent so is ZFC, since choice holds in the constructible universe L; Cohen (1963) showed that ZF plus the negation of AC is consistent too. Since arithmetic statements mean the same in L as in the whole universe, ZFC proves no statement about ℕ that ZF does not. In constructive settings the story differs: Diaconescu (1975) showed that AC implies excluded middle there, see [constructive logic](../../00-logic-and-proof/03-the-axiomatic-method/constructive-and-intuitionistic-logic.md).

8. **Weak forms suffice for most of analysis.** Countable choice, for sequences of non-empty sets, proves that countable unions of countable sets are countable, that every infinite set has a countably infinite subset, and that a function on ℝ that is sequentially continuous at a point is continuous there. Dependent choice, making a sequence of choices each depending on the last, is equivalent to the [Baire category theorem](../../09-advanced-analysis/03-functional-analysis/hahn-banach-and-baire-category.md) for complete metric spaces (Blair, 1977). Assuming an inaccessible cardinal, Solovay (1970) built a model of ZF with dependent choice in which every set of reals is measurable.

## Key concepts

| Term | Meaning |
|---|---|
| Choice function | a function picking an element of each set in a family |
| Well-ordering theorem | every set has a well-order |
| Zorn's lemma | if every chain has an upper bound, a maximal element exists |
| Countable choice | choice for countably many non-empty sets |
| Dependent choice | a sequence of choices, each depending on the previous one |
| Hamel basis | a basis of ℝ as a vector space over ℚ |
| Vitali set | one representative from each coset of ℚ in ℝ; not measurable |
| Banach–Tarski paradox | a ball decomposes into finitely many pieces that reassemble into two balls |

## How it fits

- **Below:** AC is an axiom added to [Zermelo–Fraenkel set theory](zermelo-fraenkel-set-theory.md); its proofs run by [transfinite recursion](../02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md); it makes [cardinals](../02-infinity-and-cardinality/cardinal-numbers.md) comparable; Zorn's lemma is about chains in [partial orders](../01-sets-relations-and-functions/relations-and-orders.md).
- **Above:** [bases](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md), [Tychonoff's theorem](../../07-topology/01-point-set-topology/compactness.md), maximal ideals, [Hahn–Banach](../../09-advanced-analysis/03-functional-analysis/hahn-banach-and-baire-category.md) and [non-measurable sets](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md); its independence is proved by [forcing](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md). It is the clearest case of [existence without construction](../../CROSS-CUTTING.md#existence-and-construction).
- **Siblings:** [Zermelo–Fraenkel set theory](zermelo-fraenkel-set-theory.md) without choice is the baseline; [type theory](type-theory-and-alternative-foundations.md) treats choice differently.

## Common misconceptions

- **"Every proof that says 'choose' uses AC"**: finitely many choices, and choices made by a rule, need nothing beyond ZF.
- **"Banach–Tarski shows that AC is false"**: it shows that some sets have no volume; the pieces cannot be measured, so nothing physical is duplicated.
- **"Mathematics without AC is safer"**: ZFC is consistent if ZF is, and without AC strange things happen too, such as ℝ being a countable union of countable sets.

## Go deeper

- Gregory H. Moore, *Zermelo's Axiom of Choice: Its Origins, Development, and Influence* (1982): the history and the controversy.
- Horst Herrlich, *Axiom of Choice* (Lecture Notes in Mathematics 1876, 2006): what fails without choice.
- Thomas Jech, *The Axiom of Choice* (1973): the independence results and the weak forms.
