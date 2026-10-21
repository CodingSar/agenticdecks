# Propositional Logic

> **Layer:** [01 Mathematical Foundations](../README.md) › [Logic](README.md)
> **Builds on:** [Sets](../02-sets-relations-functions/sets.md) (informally; propositional logic needs almost nothing)
> **Enables:** [Boolean Algebra](../04-algebra/boolean-algebra.md), [Logic Gates](../../03-digital-logic/02-combinational-logic/logic-gates.md), [P, NP and NP-Completeness](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md), [Model Checking](../../06-programming-languages/05-formal-methods/model-checking.md)

## Essence

Propositional logic is the study of statements that are either true or false, combined with connectives such as AND, OR, NOT and IMPLIES. It separates *syntax* (which strings of symbols are well-formed formulas) from *semantics* (which truth values those formulas take under an assignment to their variables). The single idea that makes it work is compositionality: the truth value of a compound formula depends only on the truth values of its parts. That makes every formula a finite Boolean function, which is exactly what a circuit computes and what a Satisfiability (SAT) solver searches over. It is the smallest logic in which "valid argument" can be defined precisely and checked mechanically.

## Core tenets

1. **Meaning is defined by truth tables, so it is compositional.** Each connective is a function from truth values to a truth value: `¬p` flips, `p ∧ q` is true only when both are, `p ∨ q` is false only when both are false. Because the value of a formula is computed bottom-up from its parse tree, a formula with *n* variables denotes one of the 2^(2^n) Boolean functions of *n* inputs. A compiler evaluating `a && b`, and a gate network computing `AND`, are both just evaluating this tree.

2. **Implication is "not (true then false)", nothing more.** `p → q` is defined as `¬p ∨ q`: it is false only when `p` is true and `q` is false. So "if 2 + 2 = 5 then the moon is cheese" is true (vacuous truth). This matters in specifications: a precondition that is never met makes a Hoare triple trivially true, and a guard that is always false makes an assertion pass without testing anything.

3. **Validity, satisfiability and equivalence are the three questions.** A formula is *valid* (a tautology) if true under every assignment, *satisfiable* if true under at least one, and two formulas are *equivalent* if they agree on every assignment. They reduce to each other: φ is valid exactly when ¬φ is unsatisfiable, and φ ≡ ψ exactly when `φ ↔ ψ` is valid. So one SAT-solving engine answers all three, which is why SAT solvers sit inside hardware verifiers, package managers and test generators.

4. **A small set of connectives is functionally complete.** Every Boolean function can be written in Disjunctive Normal Form (DNF), an OR of ANDs (one term per true row of its truth table), so {∧, ∨, ¬} suffice. NAND alone suffices too, since `¬p = p NAND p` and the others follow. This is why a chip can be built from one gate type, and why [logic minimization](../../03-digital-logic/02-combinational-logic/logic-minimization.md) is a search over equivalent formulas rather than a design from scratch.

5. **Normal forms trade size for structure.** Conjunctive Normal Form (CNF), an AND of clauses each an OR of literals, is the input format of SAT solvers. Converting naively can blow up exponentially, but the Tseitin transformation produces an *equisatisfiable* CNF of linear size by naming every subformula with a fresh variable. Equisatisfiable is weaker than equivalent, and that is exactly enough for the satisfiability question.

6. **Proof systems recover truth syntactically.** A proof system (natural deduction, resolution) derives formulas by rules that manipulate symbols, without truth tables. *Soundness* says everything provable is valid; *completeness* says everything valid is provable. Propositional logic has both, so "provable" and "true in every assignment" coincide. Resolution, which derives `(A ∨ B)` from `(A ∨ x)` and `(B ∨ ¬x)`, is the basis of modern Conflict-Driven Clause Learning (CDCL) SAT solvers.

7. **Deciding satisfiability is easy in principle and hard in the worst case.** A truth table with 2^n rows always decides it, so propositional logic is decidable. But SAT is the first problem proven NP-complete (Cook 1971), so no known algorithm avoids exponential worst-case time. In practice, CDCL solvers handle industrial instances with millions of variables because real formulas have structure the worst case lacks.

## Key concepts

| Term | Meaning |
|---|---|
| Proposition | A statement with a definite truth value, represented by a variable such as `p` |
| Assignment (valuation) | A map from variables to {true, false} |
| Tautology | A formula true under every assignment |
| Satisfiable | True under at least one assignment |
| Logical equivalence (≡) | Two formulas with identical truth tables |
| Literal / clause | A variable or its negation / an OR of literals |
| CNF / DNF | AND of clauses / OR of conjunctions of literals |
| Functional completeness | A connective set that can express every Boolean function |
| Soundness / completeness | Provable implies valid / valid implies provable |
| De Morgan's laws | `¬(p ∧ q) ≡ ¬p ∨ ¬q` and `¬(p ∨ q) ≡ ¬p ∧ ¬q` |

## How it fits

- **Below:** It needs only the idea of a two-element set of truth values and finite functions on it. It is a root of the formal pillar and does not depend on physics.
- **Above:** [Boolean algebra](../04-algebra/boolean-algebra.md) restates it as an algebra. [Digital logic](../../03-digital-logic/README.md) realises it in transistors. [SAT and NP-completeness](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) make it the reference hard problem. [Model checking](../../06-programming-languages/05-formal-methods/model-checking.md) and [constraint satisfaction](../../13-artificial-intelligence/01-classical-ai/constraint-satisfaction.md) encode questions into it. Every `if` condition in a program is a propositional formula over comparisons.
- **Siblings:** [Predicate logic](predicate-logic.md) adds objects and quantifiers, at the cost of decidability. [Proof techniques](proof-techniques.md) are the informal, human-scale use of the inference rules defined here.

## Common misconceptions

- **"`p → q` means p causes q."** Material implication says nothing about cause or relevance. It is only a constraint on truth values, which is why a false premise makes any implication true.
- **"Equivalent and equisatisfiable are the same."** Tseitin's CNF has extra variables and different models; it only preserves *whether* a satisfying assignment exists.
- **"NP-complete means SAT solvers are useless."** NP-completeness is a worst-case statement. Hardware and software verification run SAT solvers on huge instances every day.

## Go deeper

- Michael Huth and Mark Ryan, *Logic in Computer Science: Modelling and Reasoning about Systems* (2nd ed., 2004): logic taught with verification as the motivation.
- Stephen Cook, "The Complexity of Theorem-Proving Procedures" (1971): the paper that made SAT the first NP-complete problem.
- Armin Biere et al. (eds.), *Handbook of Satisfiability* (2009, 2nd ed. 2021): how practical SAT solvers work.
