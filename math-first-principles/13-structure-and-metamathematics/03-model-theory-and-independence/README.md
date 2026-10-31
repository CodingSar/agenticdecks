# Model Theory and Independence

> **Layer:** [13 Structure and Metamathematics](../README.md) › Model Theory and Independence
> **Children:** [Models and the Löwenheim–Skolem theorems](models-and-the-lowenheim-skolem-theorems.md) · [Quantifier elimination and decidable theories](quantifier-elimination-and-decidable-theories.md) · [Forcing and independence](forcing-and-independence.md) · [Large cardinals](large-cardinals.md)

## What this area is about

A theory is a set of sentences; a model is a structure in which they are true. Layer 00 showed that the two sides match: a sentence follows from a theory if and only if it holds in every model. Model theory exploits this match in both directions. Building a model is how one shows a sentence is *not* provable, and analysing every model of a theory is how one shows it is complete or decidable. Applied to set theory, the method shows that Zermelo–Fraenkel set theory with choice (ZFC) leaves the continuum hypothesis (CH) open, and the search for new axioms leads to large cardinals.

The unifying idea is that *to show that a theory T does not prove φ, build a model of T together with ¬φ*. Compactness and the Löwenheim–Skolem theorems make such models plentiful; quantifier elimination describes all of them for tame theories; forcing manufactures them for set theory.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Models and the Löwenheim–Skolem theorems](models-and-the-lowenheim-skolem-theorems.md) | first-order theories cannot fix the size of their models; non-standard models; categoricity | 00 compactness, 01 cardinals |
| [Quantifier elimination and decidable theories](quantifier-elimination-and-decidable-theories.md) | complete and decidable theories: the real and complex fields, Presburger arithmetic | models, undecidable problems, Gödel |
| [Forcing and independence](forcing-and-independence.md) | Gödel's constructible universe and Cohen's forcing; CH is independent of ZFC | models, 01 ZFC and choice, Gödel |
| [Large cardinals](large-cardinals.md) | axioms of infinity beyond ZFC; the consistency-strength hierarchy | forcing, 01 ordinals, Gödel |

The first leaf sets out the basic tools and their first surprise: Peano arithmetic, the real field and ZFC all have models their authors did not intend. The second goes to the opposite extreme, theories so well behaved that every sentence is decided, and explains why: they cannot define the integers with both operations, so Gödel's coding has nothing to grip. The third and fourth return to set theory. Forcing builds models of ZFC in which CH is false, as Gödel's L gives one in which it is true; large cardinals are the strongest candidates for new axioms, and they settle much about sets of reals but not CH.

```
 completeness and compactness (layer 00)
                 |
 models, Löwenheim–Skolem: many models of every size
          |                          |
 tame theories                   set theory
 quantifier elimination          forcing: CH independent of ZFC
 (ℝ, ℂ, Presburger)                   |
                                 large cardinals: stronger axioms
```

## Connections to sibling areas

- **[Computability and incompleteness](../02-computability-and-incompleteness/README.md)** supplies the reason independence is unavoidable: by Gödel's second theorem ZFC cannot prove its own consistency, so independence results are relative consistency proofs, and large cardinals extend the scale of consistency strength that proof theory measures with ordinals.
- **[Category theory](../01-category-theory/README.md)** uses inaccessible cardinals for Grothendieck universes, and topos theory recasts forcing as passage to sheaves on the forcing poset.

## Connections across layers

- **Below:** It builds on [compactness](../../00-logic-and-proof/01-formal-logic/soundness-completeness-and-compactness.md) and [consistency and independence](../../00-logic-and-proof/03-the-axiomatic-method/consistency-and-independence.md) in layer 00 and on [cardinals](../../01-sets-and-foundations/02-infinity-and-cardinality/cardinal-numbers.md), [ZFC](../../01-sets-and-foundations/03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md) and [choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md) in layer 01. The independence of the parallel postulate in [non-Euclidean geometry](../../08-geometry/01-classical-geometry/non-euclidean-geometry.md) is the historical model for the method.
- **Above and sideways:** Quantifier elimination for algebraically closed fields gives a short proof of the [Nullstellensatz](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/varieties-and-the-nullstellensatz.md) and of the Ax–Grothendieck theorem, and model theory has since contributed to Diophantine geometry, notably Ehud Hrushovski's proof of the function-field Mordell–Lang conjecture (1996). Fourier–Motzkin elimination in [linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md) is quantifier elimination for linear inequalities. The [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) asks whether CH has a truth value, and the search for new axioms is among the [open problems](../../15-mathematics-in-context/open-problems.md).

## Cross-cutting threads

- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): the theorems of layer 00 are the engine that produces models.
- [Infinity and size](../../CROSS-CUTTING.md#infinity-and-size): models of every infinite cardinality, the size of the continuum, cardinals too large for ZFC.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): independence is shown by constructing a model, ultrapowers and generic extensions among them.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): no first-order theory pins down an infinite structure, and ZFC cannot settle CH.
- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): Morley's theorem and quantifier elimination classify models and definable sets.
