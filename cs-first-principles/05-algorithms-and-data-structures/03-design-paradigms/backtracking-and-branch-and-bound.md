# Backtracking and Branch and Bound

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Design Paradigms](README.md)
> **Builds on:** [P, NP and NP-Completeness](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md), [Stacks and Queues](../02-fundamental-data-structures/stacks-and-queues.md), [Combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md), [Optimization](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md)
> **Enables:** [Constraint Satisfaction](../../13-artificial-intelligence/01-classical-ai/constraint-satisfaction.md), [Search and Planning](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md), [Model Checking](../../06-programming-languages/05-formal-methods/model-checking.md), [Logic and Declarative Programming](../../06-programming-languages/01-paradigms/logic-and-declarative.md)

## Essence

Many important problems (scheduling, satisfiability, puzzles, routing with constraints) have no known structure that greedy, divide and conquer or dynamic programming can exploit, and are NP-hard, so no polynomial algorithm is expected. The remaining option is to search the space of candidate solutions, but to do it cleverly. **Backtracking** builds a solution one decision at a time and abandons a partial solution the moment it cannot be completed validly. **Branch and bound** does the same for optimisation problems, also abandoning a partial solution when a computed bound proves it cannot beat the best solution found so far. Both are exponential in the worst case. Their value is that good pruning makes them fast on the instances that occur in practice.

## Core tenets

1. **The search space is a tree of partial decisions.** Each level fixes one variable (place the next queen, assign the next Boolean variable, choose the next city). Leaves are complete candidates. Exhaustive enumeration visits every leaf: 2ⁿ for n Boolean variables, n! for orderings. Backtracking walks the tree depth-first with a stack (or recursion), so memory is only O(depth).

2. **Pruning a node removes its whole subtree.** If a partial assignment already violates a constraint, every completion violates it too, so the search returns ("backtracks") immediately. Cutting at depth d removes up to bᵏ leaves below it, where b is the branching factor and k the remaining depth. Early detection is worth more than fast evaluation; checking constraints as soon as their variables are assigned is the core of practical backtracking.

3. **Constraint propagation shrinks the tree before branching.** After each decision, deduce forced consequences: remove values that are now impossible from other variables' domains (forward checking, arc consistency), or derive implied literals in a Boolean formula (unit propagation). A Sudoku solver that propagates constraints rarely needs to guess at all. Propagation trades more work per node for exponentially fewer nodes.

4. **Variable and value ordering change the tree's size dramatically.** Choose the most constrained variable first ("fail first": the one with the fewest remaining values) so dead ends appear near the root, where pruning them saves the most. Choose the least constraining value first so a solution, if one exists, is found sooner. These heuristics do not change the worst case but often change practical running time by orders of magnitude.

5. **Branch and bound prunes by comparing a bound with the incumbent.** For a minimisation problem, keep the best complete solution found so far (the incumbent). At each node, compute a lower bound on the cost of any completion. If the bound is no better than the incumbent, prune. Bounds come from *relaxations*: drop a hard constraint to get an easier problem whose optimum can only be better. The Linear Programming (LP) relaxation of an integer program, which drops integrality, is the workhorse; it is how Mixed-Integer Programming (MIP) solvers work.

6. **Tighter bounds and better incumbents both shrink the search.** A good heuristic solution found early (for example, by a greedy algorithm) raises the bar every node must clear. A tight bound prunes higher in the tree. Best-first search, which expands the node with the best bound, minimises nodes expanded but can use exponential memory; depth-first finds incumbents quickly with little memory. Real solvers mix both.

7. **Modern SAT solvers learn from failure.** Conflict-Driven Clause Learning (CDCL), the basis of Boolean Satisfiability (SAT) solvers since the late 1990s, analyses each dead end, derives a new clause that explains it, and adds it to the formula so the same conflict is never revisited. It then jumps back non-chronologically to the decision that caused the conflict. With restarts and good heuristics, CDCL routinely solves industrial instances with millions of variables, despite SAT being NP-complete.

8. **Worst-case exponential does not mean useless.** NP-hardness is a statement about the hardest instances. Structured real instances (hardware verification, scheduling, package dependency resolution) often have small effective search spaces once propagation and learning are applied. Conversely, random instances near a phase transition (for 3-SAT, around 4.27 clauses per variable) are reliably hard.

## Key concepts

| Term | Meaning |
|---|---|
| State-space tree | Tree whose nodes are partial solutions and leaves complete ones |
| Backtracking | Depth-first search that retreats as soon as a partial solution is infeasible |
| Pruning | Discarding a subtree without exploring it |
| Constraint propagation | Deducing forced values or eliminated options after each decision |
| Branch and bound | Optimisation search that prunes nodes whose bound cannot beat the incumbent |
| Incumbent | Best complete solution found so far |
| Relaxation | Easier problem obtained by dropping constraints; its optimum bounds the original |
| CDCL | SAT-solving method that learns a new clause from each conflict |

## How it fits

- **Below:** [NP-completeness](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) explains why search is unavoidable in the worst case; [combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md) counts the space; LP relaxations come from [optimisation](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md); the search uses a [stack](../02-fundamental-data-structures/stacks-and-queues.md).
- **Above:** [constraint satisfaction](../../13-artificial-intelligence/01-classical-ai/constraint-satisfaction.md) and [planning](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md) in Artificial Intelligence (AI); [Prolog's](../../06-programming-languages/01-paradigms/logic-and-declarative.md) execution model is backtracking; [model checkers](../../06-programming-languages/05-formal-methods/model-checking.md) and Satisfiability Modulo Theories (SMT) solvers build on CDCL; [regular-expression engines](../06-string-algorithms/string-matching.md) with backreferences backtrack, sometimes catastrophically.
- **Siblings:** [dynamic programming](dynamic-programming.md) explores the same choices but merges identical states; [greedy](greedy-algorithms.md) explores only one branch; [randomized](randomized-algorithms.md) restarts and local search are the main alternatives; [approximation algorithms](../07-advanced-topics/approximation-algorithms.md) trade optimality for guaranteed polynomial time.

## Common misconceptions

- **"Backtracking is brute force."** Brute force enumerates every leaf. Backtracking with propagation and learning often visits a tiny fraction.
- **"NP-complete means impractical."** SAT and MIP solvers solve huge industrial instances daily. Hardness bites on worst-case and adversarial instances, not necessarily on yours.
- **"Branch and bound always finds the optimum quickly."** It always finds the optimum eventually, with a proof of optimality, but the time to close the gap can be exponential.

## Go deeper

- Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach* (4th ed., 2020): constraint satisfaction chapter on backtracking, ordering and propagation.
- Armin Biere, Marijn Heule, Hans van Maaren, Toby Walsh (eds.), *Handbook of Satisfiability* (2nd ed., 2021): CDCL and modern SAT solving.
- Ailsa Land and Alison Doig, "An Automatic Method of Solving Discrete Programming Problems" (1960): the original branch and bound.
