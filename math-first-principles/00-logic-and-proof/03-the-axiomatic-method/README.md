# The Axiomatic Method

> **Layer:** [00 Logic and Proof](../README.md) › The Axiomatic Method
> **Children:** [Axioms, Definitions and Theorems](axioms-definitions-and-theorems.md) · [Consistency and Independence](consistency-and-independence.md) · [Constructive and Intuitionistic Logic](constructive-and-intuitionistic-logic.md)

## What this area is about

The axiomatic method organises mathematics as theorems derived from explicitly stated axioms by explicitly stated logic. This area asks what such a system is, what can be known about it as a whole, and what changes when the logic itself is varied. Since Hilbert's geometry of 1899, axioms are not self-evident truths about a single subject but conditions that define a class of structures, and a theorem is a statement true in every structure of that class.

The unifying idea is that questions about axiom systems become questions about models, through the soundness and completeness theorems. A system is consistent if it has a model; a statement is independent if it holds in one model and fails in another. Changing the logic, as constructive mathematics does by dropping excluded middle, changes which models count and what a proof delivers.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Axioms, Definitions and Theorems](axioms-definitions-and-theorems.md) | What an axiom system is, how definitions extend it, and the vocabulary of results | What a Proof Is, Predicate Logic, Soundness |
| [Consistency and Independence](consistency-and-independence.md) | Properties of a whole system, shown with one model or two | Axioms, Soundness, Direct Proof |
| [Constructive and Intuitionistic Logic](constructive-and-intuitionistic-logic.md) | The same method with a weaker logic in which proofs carry constructions | Direct Proof, Cases, Formal Proof Systems, Soundness |

Read the axioms leaf first: it ends with four questions to ask of any system (consistency, independence, completeness, categoricity), and the consistency leaf answers the first two. The constructive leaf can be read after either. It holds the axioms fixed and varies the logic, and its negative translation gives one of the relative consistency results the consistency leaf describes.

## Connections to sibling areas

- [Formal Logic](../01-formal-logic/README.md) is what this area stands on: its soundness theorem lets a model prove consistency, and its completeness theorem guarantees that a consistent first-order system has a model. It is also where the distinction between completeness of the logic and completeness of a theory is drawn, which this area applies to particular systems.
- [Methods of Proof](../02-methods-of-proof/README.md) supplies the arguments used inside an axiom system. Constructive logic reclassifies them: proving a negation by contradiction survives, while concluding a positive statement from the impossibility of its negation does not.

## Connections across layers

This area is where the rest of mathematics plugs into logic. [Sets and Foundations](../../01-sets-and-foundations/README.md) applies the method to set theory, producing Zermelo–Fraenkel set theory and the axiom of choice; [Number Systems](../../02-number-systems/README.md) gives the Peano axioms; [Geometry](../../08-geometry/README.md) holds the parallel postulate and the models that proved it independent. [Structure and Metamathematics](../../13-structure-and-metamathematics/README.md) takes consistency and independence to their full depth with incompleteness, forcing and large cardinals, and its homotopy type theory grows from the constructive leaf. [Mathematics in Context](../../15-mathematics-in-context/README.md) weighs the philosophical positions behind these choices.

## Cross-cutting threads

- [Abstraction and generalisation](../../CROSS-CUTTING.md#abstraction-and-generalisation): axioms with many models let one proof serve every instance.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): independence results prove that no proof exists.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): constructive logic demands a witness for every existence claim.
- [Structure and morphism](../../CROSS-CUTTING.md#structure-and-morphism): categoricity asks whether all models are isomorphic.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): the Curry–Howard correspondence translates proofs into programs and propositions into types.
