# Logic and Declarative Programming

> **Layer:** [06 Programming Languages](../README.md) › [Paradigms](README.md)
> **Builds on:** [Predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md), [Backtracking and branch and bound](../../05-algorithms-and-data-structures/03-design-paradigms/backtracking-and-branch-and-bound.md), [Relations and orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md)
> **Enables:** [Relational algebra and SQL](../../09-data-management/01-data-models/relational-algebra-and-sql.md), [Knowledge representation and reasoning](../../13-artificial-intelligence/01-classical-ai/knowledge-representation-and-reasoning.md), [Constraint satisfaction](../../13-artificial-intelligence/01-classical-ai/constraint-satisfaction.md)

## Essence

Declarative programming states *what* result is wanted and leaves *how* to compute it to an engine. Logic programming is its purest form: a program is a set of facts and rules in a fragment of [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md), and running the program means asking whether a query follows from them, with the engine searching for values that make it true. Prolog (Colmerauer and Roussel, 1972; theory by Kowalski) is the classic language. The same idea appears in Structured Query Language (SQL), regular expressions, build systems, configuration languages and constraint solvers. Kowalski summarised it as "Algorithm = Logic + Control": separate the specification of the answer from the strategy for finding it, and the engine can change the strategy without changing the program.

## Core tenets

1. **Programs are relations, not functions.** A Prolog predicate relates its arguments without fixing which are inputs. The same `append` definition can join two lists, split a list in every possible way, or check a claim, depending on which arguments are unknown.

   ```prolog
   append([], Ys, Ys).
   append([X|Xs], Ys, [X|Zs]) :- append(Xs, Ys, Zs).
   ?- append(A, B, [1,2]).   % A=[],B=[1,2] ; A=[1],B=[2] ; A=[1,2],B=[]
   ```

2. **Unification is two-way pattern matching.** To use a rule, the engine finds the most general substitution that makes the goal and the rule head identical, binding variables on both sides. Robinson's unification algorithm (1965) is the same machinery that Hindley–Milner [type inference](../02-semantics-and-types/polymorphism-and-type-inference.md) uses to solve type equations.
3. **Execution is proof search.** Prolog uses Selective Linear Definite clause resolution (SLD resolution): pick the leftmost goal, try matching rules in order, and backtrack on failure. This is depth-first [backtracking](../../05-algorithms-and-data-structures/03-design-paradigms/backtracking-and-branch-and-bound.md) over a tree of possible derivations. Because the strategy is fixed, clause order matters in practice: a left-recursive rule can loop forever even when the logic is correct.
4. **Restricting the logic buys decidability and speed.** Full first-order logic is only semi-decidable. Prolog restricts programs to Horn clauses (one positive conclusion per rule), which makes resolution efficient. Datalog restricts further (no function symbols, so the set of possible facts is finite), which guarantees termination and allows bottom-up evaluation to a fixed point. Datalog now powers program analysers and some database query engines.
5. **Negation is "not provable", not "false".** Prolog's `\+ G` succeeds when the engine fails to prove `G`, under the closed-world assumption that everything true is stated. This differs from classical negation and can give surprising answers when variables are unbound.
6. **Declarative queries let the engine optimise.** An SQL query states the rows wanted, not the loops to find them. Because the meaning is fixed by [relational algebra](../../09-data-management/01-data-models/relational-algebra-and-sql.md), a [query optimiser](../../09-data-management/03-query-processing/query-optimization.md) may reorder joins, choose indexes or parallelise, and the answer cannot change. A hand-written loop over files cannot be reorganised this way without proving its equivalence.
7. **Constraint programming generalises unification to arithmetic and finite domains.** Constraint Logic Programming (CLP) and Satisfiability Modulo Theories (SMT) solvers accept constraints such as `X + Y = 10, X > Y` and prune the search space by propagation. This drives scheduling, verification and [model checking](../05-formal-methods/model-checking.md).

## Key concepts

| Term | Meaning |
|---|---|
| Declarative program | A description of the desired result, with evaluation order left to an engine |
| Horn clause | A rule with at most one positive conclusion: `H :- B1, ..., Bn` |
| Unification | Finding the most general substitution that makes two terms identical |
| Resolution | An inference rule that derives new clauses; the engine of logic programming |
| Backtracking | Undoing choices and trying the next alternative after failure |
| Closed-world assumption | Whatever cannot be proved is assumed false |
| Datalog | A terminating subset of Prolog without function symbols, evaluated to a fixed point |
| Constraint solver | An engine that finds values satisfying a set of constraints, pruning by propagation |

## How it fits

- **Below:** The semantics comes from [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md) and [proof techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md); the execution strategy is [backtracking search](../../05-algorithms-and-data-structures/03-design-paradigms/backtracking-and-branch-and-bound.md). The limit comes from [undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md): no complete strategy can always terminate for full first-order logic.
- **Above:** SQL and the [relational model](../../09-data-management/01-data-models/the-relational-model.md) are the most widely deployed declarative languages. Classical AI built [knowledge representation](../../13-artificial-intelligence/01-classical-ai/knowledge-representation-and-reasoning.md) and [constraint satisfaction](../../13-artificial-intelligence/01-classical-ai/constraint-satisfaction.md) on these ideas. Static analysers use Datalog to express program facts.
- **Siblings:** [Imperative](imperative-and-procedural.md) code fixes both logic and control. [Functional](functional.md) code fixes the dependency structure but lets the compiler choose order. Logic code fixes only the logic, and that is why it is both the most flexible and the hardest to predict for performance.

## Common misconceptions

- **"Declarative programs have no control flow."** The control exists; it belongs to the engine. Programmers still need to understand it, because a correct but badly ordered Prolog program can run forever, and a correct but badly written SQL query can scan a billion rows.
- **"Prolog is a theorem prover for logic."** Its depth-first strategy is incomplete, and its negation is negation as failure, so it is a programming language with a logical reading, not a complete prover.
- **"Logic programming died with the Fifth Generation project."** General Prolog use is niche, but its descendants (SQL, Datalog, SMT solvers, type-inference engines) are everywhere.

## Go deeper

- Robert Kowalski, "Algorithm = Logic + Control" (1979): the founding statement of the paradigm.
- Leon Sterling and Ehud Shapiro, *The Art of Prolog* (2nd ed., 1994): how to think in relations.
- Serge Abiteboul, Richard Hull and Victor Vianu, *Foundations of Databases* (1995): Datalog and query languages on a formal footing.
