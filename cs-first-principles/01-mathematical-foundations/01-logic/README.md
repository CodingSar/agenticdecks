# Logic

> **Layer:** [01 Mathematical Foundations](../README.md) › Logic
> **Children:** [Propositional Logic](propositional-logic.md) · [Predicate Logic](predicate-logic.md) · [Proof Techniques](proof-techniques.md)

## What this area is about

Logic answers the question "when does a conclusion follow from premises?" and answers it precisely enough that a machine can check the answer. It is the first area of the formal root because every other piece of mathematics, and every specification of a program, is written in its language. The unifying idea of the three children is the split between *syntax* and *semantics*: formulas are strings manipulated by rules, and they also have a meaning (truth in a model). Soundness and completeness theorems say when those two views agree, and decidability results say when the agreement can be turned into an algorithm.

For a computer scientist logic is doubly fundamental. It is the *subject* of hardware, since a digital circuit computes a propositional formula, and it is the *tool* of correctness, since a specification is a predicate-logic formula and a correctness argument is a proof. The same handful of ideas therefore appear at the bottom of the stack, in [digital logic](../../03-digital-logic/README.md), and near the top, in [formal methods](../../06-programming-languages/05-formal-methods/README.md) and [knowledge representation](../../13-artificial-intelligence/01-classical-ai/knowledge-representation-and-reasoning.md).

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Propositional Logic](propositional-logic.md) | True/false statements and connectives; decidable; the logic of circuits and Satisfiability (SAT) | Nothing beyond a two-element set |
| [Predicate Logic](predicate-logic.md) | Adds objects, predicates and quantifiers; expressive enough for specifications and mathematics; undecidable in general | Propositional logic, sets |
| [Proof Techniques](proof-techniques.md) | The practical shapes of argument (contradiction, induction, diagonalisation, reduction) that humans use to establish claims | Both logics |

Read them in order. Propositional logic establishes the vocabulary (validity, satisfiability, normal forms, soundness, completeness) in a setting simple enough that everything is decidable by truth tables. Predicate logic keeps that vocabulary but adds quantifiers, and with them the first hard limits: validity becomes semi-decidable, and arithmetic becomes incomplete. Proof techniques then turn the inference rules of both logics into working methods.

```
propositional logic ──► predicate logic ──► proof techniques
  (connectives,           (∀, ∃, models,       (how to build
   truth tables, SAT)      undecidability)       arguments)
```

The progression shows a trade-off that recurs throughout Computer Science (CS): the more a language can express, the less can be decided automatically about it. Propositional logic is decidable but cannot say "for every element"; first-order logic can say it but has no decision procedure. Verification tools live at chosen points on this curve.

## Connections to sibling areas

- **[Sets, Relations and Functions](../02-sets-relations-functions/README.md):** Sets are described by predicates and predicates are interpreted as sets; the two areas are built together. Russell's paradox is where they collide.
- **[Discrete Mathematics](../03-discrete-mathematics/README.md):** Induction, the most used proof technique in CS, is developed there for recurrences and recursive structures.
- **[Algebra](../04-algebra/README.md):** [Boolean algebra](../04-algebra/boolean-algebra.md) is propositional logic restated as equations, the form hardware designers use.
- **[Continuous Mathematics](../05-continuous-mathematics/README.md):** Limits and convergence are defined with nested quantifiers (∀ε ∃δ), a direct use of predicate logic.
- **[Probability and Statistics](../06-probability-and-statistics/README.md):** Events combine with ∧, ∨ and ¬ like propositions; probability extends two-valued truth to degrees of belief.

## Connections across layers

Logic needs nothing from [00 Engineering Foundations](../../00-engineering-foundations/README.md). Upward, it feeds [computability](../../02-theory-of-computation/03-computability/README.md) (undecidability is the logical twin of incompleteness), [complexity](../../02-theory-of-computation/04-complexity/README.md) (SAT is the first NP-complete problem, where NP is Nondeterministic Polynomial time), [combinational logic](../../03-digital-logic/02-combinational-logic/README.md), [semantics and types](../../06-programming-languages/02-semantics-and-types/README.md) (types correspond to propositions), [logic programming](../../06-programming-languages/01-paradigms/logic-and-declarative.md), the [relational model](../../09-data-management/01-data-models/the-relational-model.md), and [security reductions](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md).

## Cross-cutting threads

- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): specifications and invariants are logical formulas; proofs keep them holding.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): undecidability of first-order validity and Gödel incompleteness.
- [Recursion and self-reference](../../CROSS-CUTTING.md#recursion-and-self-reference): diagonal arguments and self-referential sentences drive the impossibility results.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): sound proof systems let you check a proof without trusting its author.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): syntax versus semantics is the first separation of a description from what it means.
