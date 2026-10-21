# Correctness and Invariants

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Foundations](README.md)
> **Builds on:** [Induction and Recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md), [Predicate Logic](../../01-mathematical-foundations/01-logic/predicate-logic.md), [Proof Techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md)
> **Enables:** [Hoare Logic and Program Proofs](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md), [Search Trees](../02-fundamental-data-structures/search-trees.md), [Shortest Paths](../05-graph-algorithms/shortest-paths.md), [Testing](../../12-software-engineering/03-quality/testing.md)

## Essence

An algorithm is correct if, for every input satisfying its precondition, it halts and produces an output satisfying its postcondition. Testing samples a few inputs; proof covers all of them. The main proof tool is the *invariant*: a statement about the program's state that is true before a loop starts, stays true after every iteration, and, combined with the loop's exit condition, implies the result. Data structures have the same idea in a different form, the *representation invariant*, which every operation must preserve. Termination is proved separately with a *variant*: a quantity that strictly decreases and cannot decrease forever.

## Core tenets

1. **Correctness has two halves: partial correctness and termination.** Partial correctness says "if it halts, the answer is right." Termination says "it halts." Total correctness needs both. A loop that never exits is partially correct for every specification, which is why the halves are proved separately.

2. **A loop invariant is proved like an induction.** *Initialization:* it holds before the first iteration. *Maintenance:* if it holds before an iteration, it holds after. *Termination:* when the loop exits, invariant plus exit condition give the postcondition. This is mathematical induction on the iteration count. For insertion sort the invariant is "A[0..i) contains the original first i elements, in sorted order"; at exit i = n, so the whole array is sorted.

3. **Choosing the invariant is the creative step; checking it is mechanical.** The right invariant usually generalises the goal by replacing a constant with a variable ("sorted up to n" becomes "sorted up to i"). Once stated, each step is a small local check. This is why stating invariants in comments is one of the most useful habits in programming: it turns a global question into local ones.

4. **Termination is proved by a variant that decreases in a well-founded order.** Pick a quantity, typically a non-negative integer such as `hi - lo` in binary search, that every iteration strictly reduces. Because there is no infinite decreasing chain of naturals, the loop must stop. Recursive functions terminate by the same argument applied to the argument size. Undecidability of [halting](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) means no tool can find variants for every program, but humans find them for nearly every algorithm they design.

5. **Data structures are correct by preserving a representation invariant.** A binary search tree promises "every key in the left subtree is smaller than the node, every key in the right is larger." A heap promises "every parent is no greater than its children." A red–black tree adds colour and black-height rules. Each operation may break the invariant temporarily but must restore it before returning. If every operation preserves it, induction over the operation sequence shows it always holds.

6. **Greedy and dynamic-programming proofs are invariant proofs in disguise.** Dijkstra's algorithm maintains "every vertex in the finished set has its true shortest distance." Kruskal's maintains "the chosen edges are a subset of some minimum spanning tree." Dynamic programming maintains "every filled table cell holds the optimal value of its subproblem." Recognising the invariant tells you why the algorithm works and what breaks it (negative edges break Dijkstra's).

7. **Off-by-one errors are invariant errors.** Binary search is famously easy to get wrong: Jon Bentley reported that most professional programmers he tested could not write a correct one, and the Java standard library's version overflowed on `(lo + hi) / 2` for huge arrays until 2006. Writing the invariant ("if the key is present, it is in A[lo..hi)") forces you to decide whether bounds are inclusive and fixes the update rules.

8. **Specifications can be wrong even when proofs are right.** A proof shows the code meets the specification. It cannot show the specification captures intent. A sort specified only as "output is in order" is satisfied by returning an empty array; the correct specification also requires the output be a permutation of the input.

## Key concepts

| Term | Meaning |
|---|---|
| Precondition / postcondition | What the caller guarantees on entry / what the algorithm guarantees on exit |
| Partial correctness | If the program halts, its output satisfies the postcondition |
| Total correctness | Partial correctness plus guaranteed termination |
| Loop invariant | A predicate true before and after every loop iteration |
| Variant (ranking function) | A quantity in a well-founded order that strictly decreases each iteration |
| Representation invariant | The consistency condition a data structure's internal state must always satisfy |
| Abstraction function | Maps a concrete representation to the abstract value it represents |
| Exchange argument | Show any optimal solution can be transformed into the greedy one without getting worse |

## How it fits

- **Below:** uses [induction](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) and [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md); termination interacts with [undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md).
- **Above:** formalised as [Hoare logic](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md) and checked by [proof assistants](../../06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md). [Type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md) enforce simple invariants automatically. Database [consistency constraints](../../09-data-management/04-transactions/acid.md) and [lock-free](../../07-operating-systems/03-concurrency/lock-free-synchronization.md) data structures are also invariant-preservation problems, made harder by concurrency.
- **Siblings:** [models of computation](models-of-computation.md) fixes the cost measure; [amortized analysis](amortized-analysis.md) uses an invariant on stored credit (the potential is never negative).

## Common misconceptions

- **"Enough tests prove correctness."** Tests check finitely many inputs; an invariant proof covers all of them. Tests are still essential for catching wrong specifications and wrong proofs.
- **"An invariant must hold at every instant."** It must hold at specific points (loop head, between operations). Inside an iteration or an operation it may be temporarily false.
- **"Proof is only for academics."** Invariants are the cheapest form of proof and guide everyday code: assertions, careful bounds, and data structure checks are all invariant-based.

## Go deeper

- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (4th ed., 2022): uses loop invariants for nearly every algorithm.
- Jon Bentley, *Programming Pearls* (2nd ed., 1999): the binary search chapter on writing correct code via invariants.
- David Gries, *The Science of Programming* (1981): deriving programs from their invariants.
- Edsger W. Dijkstra, *A Discipline of Programming* (1976): weakest preconditions and invariant-first program design.
