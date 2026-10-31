# Axiomatic Set Theory

> **Layer:** [01 Sets and Foundations](../README.md) › Axiomatic Set Theory
> **Children:** [Paradoxes and naive set theory](paradoxes-and-naive-set-theory.md) · [Zermelo–Fraenkel set theory](zermelo-fraenkel-set-theory.md) · [The axiom of choice](the-axiom-of-choice.md) · [Type theory and alternative foundations](type-theory-and-alternative-foundations.md)

## What this area is about

The first two areas of this layer use sets freely. This area asks what justifies that use. Around 1900 the naive principle that every property defines a set turned out to be contradictory, and mathematicians responded by writing down exactly which sets exist. The result, Zermelo–Fraenkel set theory (ZF), plus the axiom of choice (AC), gives ZFC, the theory in which almost all mathematics is now formally written. Writing the axioms down also made it possible to ask what they cannot prove, and the answer includes AC itself relative to ZF, and the continuum hypothesis (CH) relative to ZFC.

The unifying idea is that *a foundation is a theory, and theories have limits*. A foundation is chosen for what it makes possible and safe; no foundation decides everything or proves its own consistency.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Paradoxes and naive set theory](paradoxes-and-naive-set-theory.md) | why unrestricted set formation fails, and the two kinds of repair | sets, diagonal argument, ordinals |
| [Zermelo–Fraenkel set theory](zermelo-fraenkel-set-theory.md) | the axioms, the cumulative hierarchy, relative consistency and independence | paradoxes, ordinals |
| [The axiom of choice](the-axiom-of-choice.md) | well-ordering, Zorn's lemma, their consequences and weaker forms | ZF, ordinals, cardinals |
| [Type theory and alternative foundations](type-theory-and-alternative-foundations.md) | types, Martin-Löf type theory, the elementary theory of the category of sets (ETCS), proof assistants | paradoxes, ZF, choice |

```
             paradoxes (Russell 1901, Cantor, Burali-Forti)
              │                                    │
   restrict comprehension                     stratify by type
              ▼                                    ▼
   Zermelo–Fraenkel set theory (ZF) ───────► type theories, ETCS
              │                                (Russell 1908, Church 1940,
              ▼                                 Martin-Löf, Lawvere 1964)
   + axiom of choice = ZFC
              │
              ▼
   independence: AC from ZF, CH from ZFC (Gödel 1938/1940, Cohen 1963)
```

Read the paradoxes first: they explain the shape of every axiom. Zermelo–Fraenkel set theory then shows how little is needed to rebuild mathematics. The axiom of choice gets its own leaf because it is the one axiom mathematicians argued about and still track, and because so many theorems turn out to be equivalent to it. The type theory leaf closes the area by showing that the same mathematics can rest on a different primitive, and why computers prefer it.

## Connections to sibling areas

- **[Sets, Relations and Functions](../01-sets-relations-and-functions/README.md)** is the informal practice this area justifies: every subset, product, power set and quotient formed there is licensed by an axiom here.
- **[Infinity and Cardinality](../02-infinity-and-cardinality/README.md)** supplies the diagonal argument behind the paradoxes and the ordinals that index the cumulative hierarchy; in return, this area shows which of its results need choice and which questions, such as CH, are independent.

## Connections across layers

- **Below:** ZF is a theory in [predicate logic](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md), and its consistency questions are those of [consistency and independence](../../00-logic-and-proof/03-the-axiomatic-method/consistency-and-independence.md).
- **Above:** ω is [the natural numbers](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md); choice gives [bases](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md), [maximal ideals](../../05-abstract-algebra/02-rings-and-fields/rings-and-ideals.md), [Tychonoff's theorem](../../07-topology/01-point-set-topology/compactness.md) and [non-measurable sets](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md); [metamathematics](../../13-structure-and-metamathematics/README.md) develops incompleteness, forcing and large cardinals; [mathematics in context](../../15-mathematics-in-context/README.md) covers the foundational crisis and proof assistants.

## Cross-cutting threads

- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): choice asserts existence without a construction.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): the paradoxes and the independence results both prove that something cannot be done.
- [Infinity and size](../../CROSS-CUTTING.md#infinity-and-size): the paradoxes of size separate sets from proper classes.
- [Structure and morphism](../../CROSS-CUTTING.md#structure-and-morphism): category-theoretic foundations take maps, not membership, as primitive.
