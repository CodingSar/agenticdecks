# Predicate Logic

> **Layer:** [01 Mathematical Foundations](../README.md) › [Logic](README.md)
> **Builds on:** [Propositional Logic](propositional-logic.md), [Sets](../02-sets-relations-functions/sets.md), [Relations and Orders](../02-sets-relations-functions/relations-and-orders.md)
> **Enables:** [Hoare Logic and Program Proofs](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md), [The Relational Model](../../09-data-management/01-data-models/the-relational-model.md), [Logic and Declarative Programming](../../06-programming-languages/01-paradigms/logic-and-declarative.md), [Halting Problem and Undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md)

## Essence

Predicate logic (first-order logic) extends propositional logic with *objects*, *predicates* that hold of objects, *functions* on objects, and the quantifiers "for all" (∀) and "there exists" (∃). It lets you say "every element of the array is sorted" or "some process holds the lock", which propositional logic cannot express without one variable per object. Its formulas are interpreted in a *structure*: a domain of objects plus a meaning for each symbol. It is the language in which program specifications, database queries and most of mathematics are written. The price of this expressiveness is that validity is no longer decidable.

## Core tenets

1. **Quantifiers range over a domain, so meaning depends on the structure.** `∀x. x + 1 > x` is true over the integers and false over 8-bit unsigned integers, where 255 + 1 = 0. A formula is *valid* only if true in every structure. This is the formal reason a correctness proof over mathematical integers says nothing about machine integers unless the model includes overflow.

2. **Quantifier order changes meaning.** `∀x ∃y. y > x` (every number has a larger one) is true over the integers; `∃y ∀x. y > x` (one number beats them all) is false. The outer quantifier's choice is fixed before the inner one is made. In specifications this distinguishes "every request eventually gets a response" from "there is a time after which all requests are answered".

3. **Negation pushes through quantifiers by duality.** `¬∀x. P(x) ≡ ∃x. ¬P(x)` and `¬∃x. P(x) ≡ ∀x. ¬P(x)`. To refute a universal claim you need one counterexample; to refute an existential claim you must rule out every candidate. Testing finds counterexamples to ∀-claims; it can never establish them.

4. **Free and bound variables obey scoping rules, just like programs.** In `∀x. P(x, y)`, `x` is bound and `y` is free. Renaming a bound variable does not change meaning, but substituting a term that contains `x` under the quantifier would "capture" it and change meaning. The same capture-avoiding substitution problem reappears in [lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md) and in [closures](../../06-programming-languages/02-semantics-and-types/binding-scope-and-closures.md).

5. **First-order logic is complete but undecidable.** Gödel's completeness theorem (1929) says every valid first-order formula has a finite proof, so valid formulas can be enumerated by a machine. But Church and Turing (1936) showed validity is undecidable: no algorithm answers "is this valid?" for every formula. The valid formulas are *semi-decidable*: a search finds a proof if one exists but may run forever otherwise. Automated theorem provers live with this by using timeouts and heuristics.

6. **Restricted fragments regain decidability, and Computer Science (CS) lives in them.** Satisfiability Modulo Theories (SMT) solvers decide combinations of decidable theories, such as linear arithmetic, bit-vectors and arrays, which covers most verification conditions from real code. Datalog and relational calculus restrict quantification to finite database contents, so queries always terminate. Choosing a decidable fragment is a central engineering decision in verification tools.

7. **Arithmetic is incomplete.** Gödel's incompleteness theorem (1931) shows that any consistent, effectively axiomatised theory strong enough to express arithmetic of natural numbers contains true statements it cannot prove. This is the logical twin of the [halting problem](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md): both come from self-reference, and both mean there is no general mechanical oracle for program properties.

## Key concepts

| Term | Meaning |
|---|---|
| Predicate | A symbol `P(x₁,…,xₙ)` that is true or false of a tuple of objects |
| Term | An expression denoting an object: a variable, constant or function application |
| Quantifier | ∀ (for all) or ∃ (there exists), binding a variable over the domain |
| Structure (model) | A domain plus an interpretation of every constant, function and predicate symbol |
| Free / bound variable | Not / inside the scope of a quantifier binding it |
| Validity | Truth in every structure under every assignment |
| Semi-decidable | A machine halts with "yes" on every yes-instance but may loop on no-instances |
| Theory | A set of axioms; its models are the structures satisfying them |
| SMT | Satisfiability checking for formulas combined with background theories such as arithmetic |

## How it fits

- **Below:** It extends [propositional logic](propositional-logic.md) and needs [sets](../02-sets-relations-functions/sets.md) for domains and [relations](../02-sets-relations-functions/relations-and-orders.md) for the meaning of predicates.
- **Above:** Loop invariants and pre/postconditions in [Hoare logic](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md) are first-order formulas. Structured Query Language (SQL) `WHERE` clauses and [relational calculus](../../09-data-management/01-data-models/relational-algebra-and-sql.md) are first-order queries over a finite structure. Prolog is a programming language built on a fragment of it ([logic programming](../../06-programming-languages/01-paradigms/logic-and-declarative.md)). Type systems with dependent types extend it toward higher-order logic ([proof assistants](../../06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md)). [Knowledge representation](../../13-artificial-intelligence/01-classical-ai/knowledge-representation-and-reasoning.md) in Artificial Intelligence (AI) uses it directly.
- **Siblings:** [Propositional logic](propositional-logic.md) is the decidable, quantifier-free core. [Proof techniques](proof-techniques.md) are how humans discharge quantified claims: ∀ by an arbitrary element or induction, ∃ by a witness.

## Common misconceptions

- **"Undecidable means nothing can be proved automatically."** Undecidability rules out a procedure that works on *every* formula. Provers and SMT solvers succeed on a large share of the formulas engineers actually write.
- **"Incompleteness means mathematics is unreliable."** It says some truths are unprovable in a given system, not that provable things may be false. Consistent systems remain sound.
- **"∀x ∃y and ∃y ∀x are interchangeable."** Swapping them turns a weak claim into a much stronger one; many specification bugs are this swap.

## Go deeper

- Herbert Enderton, *A Mathematical Introduction to Logic* (2nd ed., 2001): standard rigorous treatment, including completeness.
- Michael Huth and Mark Ryan, *Logic in Computer Science* (2nd ed., 2004): first-order logic with program verification in view.
- Daniel Kroening and Ofer Strichman, *Decision Procedures: An Algorithmic Point of View* (2nd ed., 2016): how SMT solvers decide useful fragments.
