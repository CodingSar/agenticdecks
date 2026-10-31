# Formal Logic

> **Layer:** [00 Logic and Proof](../README.md) › Formal Logic
> **Children:** [Propositional Logic](propositional-logic.md) · [Predicate Logic and Quantifiers](predicate-logic-and-quantifiers.md) · [Formal Proof Systems](formal-proof-systems.md) · [Soundness, Completeness and Compactness](soundness-completeness-and-compactness.md)

## What this area is about

Formal logic makes mathematical reasoning itself an object of study. It fixes a precise language of formulas, says what it means for a formula to be true in a structure, and gives purely mechanical rules for deriving formulas from others. That separates two relations: Γ ⊨ φ, φ is true in every structure where Γ is true (semantics), and Γ ⊢ φ, φ can be derived from Γ by the rules (syntax).

The unifying idea is that these two relations coincide for first-order logic. Soundness says every derivation preserves truth; Gödel's completeness theorem (1930) says every consequence has a derivation. "Provable" and "true in all models" are then one notion, which is why a mathematician may reason about meanings and trust that a formal proof exists, or check a formal proof and trust that the statement holds.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Propositional Logic](propositional-logic.md) | Connectives, truth tables, tautologies and the satisfiability problem | nothing earlier |
| [Predicate Logic and Quantifiers](predicate-logic-and-quantifiers.md) | Quantifiers, structures and truth in a structure: the semantics ⊨ | Propositional Logic |
| [Formal Proof Systems](formal-proof-systems.md) | Hilbert systems, natural deduction, sequents and resolution: the syntax ⊢ | Propositional, Predicate |
| [Soundness, Completeness and Compactness](soundness-completeness-and-compactness.md) | The theorems that make ⊢ and ⊨ agree, and their consequences | all three, plus induction and basic sets |

Read them in order. The first two build the semantic side, the third the syntactic side, and the fourth joins them. The comparison of logics that runs through the area:

```
                 complete proof system   decidable validity      compact
propositional    yes (Post, 1921)        yes, by truth tables     yes
first-order      yes (Gödel, 1930)       no (Church, Turing 1936) yes
second-order     no effective one        no                       no
```

First-order logic sits at a balance point: expressive enough for almost all of mathematics, yet still complete and compact, with valid formulas that can be listed by an algorithm though not decided.

## Connections to sibling areas

- [Methods of Proof](../02-methods-of-proof/README.md) is the informal practice whose idealisation this area studies: each everyday proof pattern (assume P, let x be arbitrary, split into cases) is a rule of natural deduction, and the inductions that prove soundness and completeness are taken from there.
- [The Axiomatic Method](../03-the-axiomatic-method/README.md) uses soundness and completeness to turn questions about axiom systems into questions about models: consistency by one model, independence by two. Its constructive leaf drops two rules of the systems defined here and asks what survives.

## Connections across layers

The soundness leaf builds models from [sets and relations](../../01-sets-and-foundations/README.md), the one place where layer 00 leans on layer 01. Upward, [Structure and Metamathematics](../../13-structure-and-metamathematics/README.md) takes the subject further: incompleteness of arithmetic, undecidability, model theory and proof theory all start from the definitions here. In computing, the same logic underlies circuits, satisfiability solvers and program verification ([Logic in computer science](../../../cs-first-principles/01-mathematical-foundations/01-logic/README.md)).

## Cross-cutting threads

- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): the completeness theorem and compactness of first-order logic are the logical original of the pattern.
- [Duality](../../CROSS-CUTTING.md#duality): syntax and semantics, ⊢ and ⊨, two views of one relation; also De Morgan duality of ∧ and ∨, ∀ and ∃.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): a single countermodel proves that no derivation exists.
- [Induction and recursion](../../CROSS-CUTTING.md#induction-and-recursion): formulas and derivations are defined recursively and reasoned about by structural induction.
