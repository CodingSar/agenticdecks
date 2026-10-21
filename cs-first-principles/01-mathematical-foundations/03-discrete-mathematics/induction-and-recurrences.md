# Induction and Recurrences

> **Layer:** [01 Mathematical Foundations](../README.md) › [Discrete Mathematics](README.md)
> **Builds on:** [Proof Techniques](../01-logic/proof-techniques.md), [Relations and Orders](../02-sets-relations-functions/relations-and-orders.md)
> **Enables:** [Divide and Conquer](../../05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md), [Dynamic Programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md), [Correctness and Invariants](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md), [Asymptotic Analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md), [Hoare Logic and Program Proofs](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md)

## Essence

Induction and recursion are the same idea seen from two sides. Recursion *defines* something for all sizes by saying what to do at the smallest size and how to build size *n* from smaller sizes; induction *proves* something for all sizes by the same two steps. A recurrence is an equation that defines a quantity, usually an algorithm's running time, in terms of its value on smaller inputs, such as T(n) = 2T(n/2) + n for merge sort. Solving recurrences turns the structure of a recursive algorithm into a closed-form cost. Together these tools let you reason about loops, recursive functions and recursive data structures of unbounded size with a finite argument.

## Core tenets

1. **Induction works because the naturals are well-founded.** Any non-empty set of natural numbers has a least element. If `P` failed somewhere, there would be a least failing `n`; the base case says `n ≠ 0`, and the step from `n − 1` says `P(n)` holds after all. The same argument works on any [well-founded order](../02-sets-relations-functions/relations-and-orders.md), so induction is not special to numbers.

2. **Strong induction lets the step use every smaller case.** Assume `P(0), …, P(k)` and prove `P(k+1)`. It is equivalent in power to ordinary induction but matches divide-and-conquer, where size *n* depends on size *n/2*, not *n − 1*. Proving that every integer above 1 has a prime factorisation is a typical use.

3. **Structural induction proves properties of recursive data and programs.** A list is empty or a head plus a list; a tree is a leaf or a node with subtrees; a program is built from smaller statements. Prove the property for the base constructors and show each constructor preserves it. Compilers and type checkers are justified this way: [type soundness](../../06-programming-languages/02-semantics-and-types/type-systems.md) is proved by induction on typing derivations.

4. **A loop invariant is induction on iterations.** Show the invariant holds before the first iteration (base) and that one iteration preserves it (step); then it holds at exit, and combined with the exit condition it gives the postcondition. Termination is a separate induction: find a quantity in a well-founded order (often a natural number) that strictly decreases each iteration. This is the core of [algorithm correctness](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md) and [Hoare logic](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md).

5. **Recurrences capture the cost of recursion.** A recursive algorithm that splits size *n* into *a* subproblems of size *n/b* and does *f(n)* extra work costs T(n) = aT(n/b) + f(n). Binary search is T(n) = T(n/2) + O(1) = O(log n); merge sort is T(n) = 2T(n/2) + O(n) = O(n log n); naive Fibonacci is T(n) = T(n−1) + T(n−2) + O(1), which grows like φ^n with φ ≈ 1.618.

6. **The master theorem compares the split work with the combine work.** For T(n) = aT(n/b) + f(n), compare f(n) with n^(log_b a), the number of leaves of the recursion tree. If leaves dominate, T = Θ(n^(log_b a)); if they balance, an extra log factor appears; if the top-level work dominates (and a regularity condition holds), T = Θ(f(n)). Karatsuba multiplication splits into 3 half-size problems, giving Θ(n^(log₂3)) ≈ Θ(n^1.585) instead of the schoolbook Θ(n²).

7. **Linear recurrences have exponential closed forms.** A recurrence like a(n) = c₁a(n−1) + c₂a(n−2) is solved by the roots of its characteristic polynomial x² = c₁x + c₂; the solution is a combination of r^n terms for each root r. This explains why Fibonacci numbers grow like φ^n, why the naive recursion is exponential, and why the matrix form [[1,1],[1,0]]^n computes them in O(log n) multiplications by repeated squaring, a direct use of [linear algebra](../04-algebra/linear-algebra.md).

8. **Memoisation turns overlapping recursion into dynamic programming.** When a recursion re-solves the same subproblems, as naive Fibonacci does, storing each answer once reduces exponential time to the number of distinct subproblems times the work per subproblem. The recurrence is the specification; [dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md) is the evaluation order.

## Key concepts

| Term | Meaning |
|---|---|
| Base case | The smallest instance, proved or defined directly |
| Inductive step | Proof that the property passes from smaller to larger instances |
| Strong induction | Step may assume all smaller cases |
| Structural induction | Induction over the constructors of a recursive structure |
| Well-founded order | No infinite descending chains; licenses induction and termination proofs |
| Recurrence | Equation defining a sequence in terms of earlier terms |
| Recursion tree | Diagram of the subproblems a recursion creates, with their costs |
| Master theorem | Closed form for T(n) = aT(n/b) + f(n) |
| Characteristic polynomial | Polynomial whose roots give the closed form of a linear recurrence |
| Memoisation | Caching results of recursive calls by argument |

## How it fits

- **Below:** Induction is a [proof technique](../01-logic/proof-techniques.md) justified by [well-founded orders](../02-sets-relations-functions/relations-and-orders.md).
- **Above:** [Divide and conquer](../../05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md) is analysed with recurrences; [dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md) evaluates them; [asymptotic analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md) states their solutions. Recursive types and functions in [functional programming](../../06-programming-languages/01-paradigms/functional.md) are reasoned about by structural induction. [Proof assistants](../../06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md) generate induction principles automatically from datatype definitions.
- **Siblings:** [Combinatorics](combinatorics.md) uses recurrences to count; [graph theory](graph-theory.md) uses induction on vertices, edges and path length.

## Common misconceptions

- **"The base case is a formality."** Without it the step proves nothing: "all horses are the same colour" fails exactly because the step breaks between sizes 1 and 2.
- **"A recurrence with two recursive calls is O(n log n)."** It depends on sizes: T(n) = 2T(n/2) + n is O(n log n), but T(n) = 2T(n−1) + 1 is O(2^n).
- **"Recursion is inherently slower than loops."** Tail-recursive functions compile to loops, and memoised recursion is dynamic programming. The cost is in the recurrence, not the syntax.

## Go deeper

- Thomas Cormen, Charles Leiserson, Ronald Rivest and Clifford Stein, *Introduction to Algorithms* (4th ed., 2022): the master theorem and recursion-tree method.
- Ronald Graham, Donald Knuth and Oren Patashnik, *Concrete Mathematics* (2nd ed., 1994): recurrences and their solution in depth.
- Benjamin Pierce, *Types and Programming Languages* (2002): structural induction as the workhorse of language proofs.
