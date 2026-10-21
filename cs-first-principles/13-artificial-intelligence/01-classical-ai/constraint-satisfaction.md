# Constraint Satisfaction

> **Layer:** [13 Artificial Intelligence](../README.md) › [Classical AI](README.md)
> **Builds on:** [Backtracking and branch and bound](../../05-algorithms-and-data-structures/03-design-paradigms/backtracking-and-branch-and-bound.md), [P, NP and NP-completeness](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md), [Propositional logic](../../01-mathematical-foundations/01-logic/propositional-logic.md), [Search and planning](search-and-planning.md)
> **Enables:** [Model checking](../../06-programming-languages/05-formal-methods/model-checking.md), [Knowledge representation and reasoning](knowledge-representation-and-reasoning.md), [Query optimization](../../09-data-management/03-query-processing/query-optimization.md)

## Essence

A Constraint Satisfaction Problem (CSP) asks for values for a set of variables such that every constraint among them holds: colour a map so neighbours differ, schedule exams so no student has two at once, fill a Sudoku. Unlike path search, only the final assignment matters, and the problem has *structure*: each constraint mentions only a few variables. That structure is the lever. Solvers interleave guessing (backtracking search) with **propagation**, which deletes values that cannot appear in any solution, so most of the exponential search space is never visited. Boolean satisfiability (SAT) is the special case where every variable is true or false and constraints are clauses; modern SAT solvers routinely handle industrial instances with millions of variables even though SAT is NP-complete.

## Core tenets

1. **A CSP is variables, domains and constraints.** Each variable X_i has a finite domain D_i, and each constraint restricts the allowed combinations of a small subset of variables. This factored representation lets a generic solver see *why* a partial assignment fails, which path search over opaque states cannot.

2. **General CSPs are NP-complete, so worst cases are exponential.** SAT was the first problem proved NP-complete (Cook, 1971), and graph colouring and scheduling reduce to it. No known algorithm avoids exponential time on all instances. Practical success comes from exploiting the structure of real instances, which are rarely worst-case.

3. **Backtracking assigns one variable at a time and undoes on failure.** Depth-first search over partial assignments checks constraints as soon as their variables are set, so a bad early choice is abandoned without enumerating its completions. Variable order matters greatly: choosing the *most constrained* variable first (minimum remaining values) fails fast and prunes high in the tree.

4. **Propagation shrinks domains before and during search.** Arc consistency removes a value from X's domain if no value of a neighbour Y satisfies the constraint between them, and repeats until nothing changes (the AC-3 algorithm runs in O(ed³) for e constraints and domain size d). Propagation is cheap polynomial inference that often eliminates most branches; in easy Sudokus it solves the puzzle with no search at all.

5. **Learning from conflicts turns failure into knowledge.** Conflict-Driven Clause Learning (CDCL), the core of modern SAT solvers, analyses each dead end, derives a new clause that explains it, and jumps back to the decision that caused it rather than the most recent one. The learned clause prevents the same conflict anywhere else in the search. Combined with efficient unit propagation and restarts, this is why SAT went from toy sizes in the 1990s to an everyday engineering tool.

6. **Tree-structured problems are easy.** If the constraint graph is a tree, the CSP is solvable in O(nd²) time by enforcing consistency from leaves to root and then assigning top-down. More generally, the cost is exponential only in the graph's *treewidth*, so decomposing a problem into loosely coupled parts can turn an intractable instance into a tractable one.

7. **Optimisation is constraint satisfaction with an objective.** Integer Linear Programming (ILP), Maximum Satisfiability (MaxSAT) and constraint optimisation add a cost to minimise. Branch and bound prunes any partial assignment whose optimistic bound is worse than the best solution found, using linear-programming relaxations as the bound.

## Key concepts

| Term | Meaning |
|---|---|
| Domain | Finite set of values a variable may take |
| Constraint graph | Graph with a node per variable and an edge between variables sharing a constraint |
| Arc consistency | Every value of X has a supporting value in each neighbour's domain |
| Forward checking | After assigning X, delete inconsistent values from its neighbours' domains |
| Minimum remaining values | Heuristic: assign next the variable with the fewest legal values left |
| SAT | Deciding whether a Boolean formula in conjunctive normal form has a satisfying assignment |
| CDCL | SAT algorithm that learns a clause from each conflict and backjumps non-chronologically |
| Treewidth | How far a graph is from a tree; bounds the exponent of structured CSP algorithms |

## How it fits

- **Below:** The search is [backtracking](../../05-algorithms-and-data-structures/03-design-paradigms/backtracking-and-branch-and-bound.md) from Layer 05; the encoding into clauses uses [propositional logic](../../01-mathematical-foundations/01-logic/propositional-logic.md); hardness results come from [NP-completeness](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md).
- **Above:** SAT and its extension Satisfiability Modulo Theories (SMT) power [model checking](../../06-programming-languages/05-formal-methods/model-checking.md), program verification, test generation and package dependency resolution. Constraint solvers schedule airlines, chips and cloud placement.
- **Siblings:** Compared with [search and planning](search-and-planning.md), constraint satisfaction has no path cost and gains propagation. It is the computational engine behind [logical reasoning](knowledge-representation-and-reasoning.md), and its counting version (how many solutions?) is closely related to inference in [probabilistic models](probabilistic-reasoning.md).

## Common misconceptions

- **"NP-complete means unsolvable in practice."** NP-completeness is a worst-case statement. Industrial SAT and ILP instances with millions of variables are solved routinely because they have exploitable structure.
- **"Propagation is just an optimisation."** Propagation is inference: each deleted value is a proved fact. Strong enough propagation alone decides some problem classes, such as tree-structured CSPs.
- **"Machine learning has made constraint solvers obsolete."** Learned models produce plausible answers; solvers produce answers that provably satisfy every constraint, or a proof that none exists. As of the mid-2020s they are increasingly combined rather than substituted.

## Go deeper

- Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach* (4th ed., 2020), chapter 6: a compact introduction to CSP search and propagation.
- Armin Biere, Marijn Heule, Hans van Maaren and Toby Walsh (eds.), *Handbook of Satisfiability* (2009; 2nd ed. 2021): the reference for CDCL and modern SAT.
- Francesca Rossi, Peter van Beek and Toby Walsh (eds.), *Handbook of Constraint Programming* (2006): consistency, global constraints and solver design.
