# Dynamic Programming

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Design Paradigms](README.md)
> **Builds on:** [Divide and Conquer](divide-and-conquer.md), [Induction and Recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md), [Hash Tables](../02-fundamental-data-structures/hash-tables.md)
> **Enables:** [Shortest Paths](../05-graph-algorithms/shortest-paths.md), [String Matching](../06-string-algorithms/string-matching.md), [Query Optimization](../../09-data-management/03-query-processing/query-optimization.md), [Reinforcement Learning](../../13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md), [Lexing and Parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md)

## Essence

Dynamic programming (DP) solves a problem by expressing its answer as a recurrence over smaller subproblems, then computing each distinct subproblem exactly once and storing the result. It applies when two conditions hold: *optimal substructure* (the best solution is built from best solutions to subproblems) and *overlapping subproblems* (the recursion visits the same subproblems many times). Storing answers turns an exponential recursion into a polynomial table fill: the running time becomes (number of distinct subproblems) × (work per subproblem). The name comes from Richard Bellman in the 1950s; "programming" meant planning, as in "linear programming", not coding.

## Core tenets

1. **Overlap is what makes plain recursion exponential and DP polynomial.** Recursive Fibonacci F(n) = F(n−1) + F(n−2) makes Θ(φⁿ) calls (φ ≈ 1.618) but has only n + 1 distinct subproblems. Storing each result once gives Θ(n). The same collapse happens in every DP: the recursion tree is exponential, but its distinct nodes form a small Directed Acyclic Graph (DAG).

2. **Every DP is a shortest or longest path in a DAG of subproblems.** Nodes are subproblems, edges are "depends on", and the recurrence combines a node's answer from its predecessors. Solving the subproblems in any topological order guarantees each dependency is ready when needed. This view explains why DP needs acyclic dependencies: a cycle means no valid order exists.

3. **The hard part is choosing the subproblem.** A good subproblem definition is small enough to enumerate and rich enough to recombine. Typical shapes: prefixes of one sequence (longest increasing subsequence), pairs of prefixes (edit distance, longest common subsequence: O(nm)), intervals (matrix-chain order, optimal binary search trees: O(n³)), subsets (travelling salesperson via Held–Karp: O(n²2ⁿ)), and "first k items with capacity w" (knapsack: O(nW)).

4. **Top-down memoization and bottom-up tabulation are equivalent in what they compute.** Memoization keeps the natural recursion and caches results in a table or hash map; it only solves subproblems actually reached. Tabulation fills an array in topological order with loops; it avoids recursion overhead and stack depth limits and lets you see the access pattern. Bottom-up often allows space reduction: edit distance needs only the previous row, so O(min(n, m)) space suffices for the distance itself.

5. **Running time is subproblems × choices per subproblem.** Edit distance has nm subproblems with 3 choices each: Θ(nm). Bellman–Ford shortest paths has n·k subproblems ("shortest path using at most k edges") with deg(v) choices: Θ(nm) total. Floyd–Warshall all-pairs shortest paths has n³ subproblems with O(1) work each: Θ(n³).

6. **Pseudo-polynomial is not polynomial.** The 0/1 knapsack DP runs in O(nW), where W is the capacity. That looks polynomial, but W is a number written in log W bits, so O(nW) is exponential in the input *size*. Knapsack is NP-hard; DP gives a fast algorithm only when W is small. The same distinction underlies the [approximation scheme](../07-advanced-topics/approximation-algorithms.md) for knapsack, which rounds values to make the table small.

7. **Reconstructing the solution needs back-pointers.** The table holds optimal *values*. To recover the optimal *choice sequence* (the alignment, the path, the chosen items), store which choice achieved each optimum, or re-derive it by walking back through the table. Space-reduced DPs lose this information; Hirschberg's algorithm (1975) recovers an optimal alignment in linear space by divide and conquer.

8. **DP is the mathematics of sequential decisions.** Bellman's principle of optimality, "whatever the first decision, the remaining decisions must be optimal for the resulting state", is the same idea in control theory and reinforcement learning, where the Bellman equation defines the value of a state as the best immediate reward plus the value of the next state. Viterbi decoding of hidden Markov models, the Cocke–Younger–Kasami (CYK) parser for context-free grammars, and sequence alignment in bioinformatics are all DP.

## Key concepts

| Term | Meaning |
|---|---|
| Optimal substructure | An optimal solution is composed of optimal solutions to subproblems |
| Overlapping subproblems | The same subproblem recurs many times in the naive recursion |
| Memoization | Top-down recursion with a cache of computed results |
| Tabulation | Bottom-up filling of a table in dependency order |
| State | The parameters identifying one subproblem |
| Subproblem DAG | Graph of dependencies between subproblems; must be acyclic |
| Pseudo-polynomial | Polynomial in the numeric value of the input, exponential in its bit length |
| Bellman equation | Recursive definition of optimal value in sequential decision problems |

## How it fits

- **Below:** correctness is [induction](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) over the subproblem order; memo tables are [arrays or hash tables](../02-fundamental-data-structures/hash-tables.md); the pseudo-polynomial trap comes from [complexity theory](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md).
- **Above:** [query optimizers](../../09-data-management/03-query-processing/query-optimization.md) choose join orders with the System R DP; [distance-vector routing](../../08-networking/03-network-layer/routing-algorithms.md) is distributed Bellman–Ford; [CYK and Earley parsing](../../06-programming-languages/03-compilers/lexing-and-parsing.md) are DP; [reinforcement learning](../../13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md) and [probabilistic reasoning](../../13-artificial-intelligence/01-classical-ai/probabilistic-reasoning.md) (Viterbi, forward–backward) generalise it; `diff` in [version control](../../12-software-engineering/02-process/version-control.md) is a longest-common-subsequence variant.
- **Siblings:** [divide and conquer](divide-and-conquer.md) without overlap needs no table; [greedy](greedy-algorithms.md) is DP where one choice is provably enough; [backtracking](backtracking-and-branch-and-bound.md) explores the same choice tree without merging repeated states.

## Common misconceptions

- **"DP is a specific algorithm."** It is a technique: define subproblems, write a recurrence, evaluate each subproblem once.
- **"Knapsack in O(nW) shows P = NP."** O(nW) is exponential in the number of bits of W, so it is not polynomial in input size.
- **"Memoization is always better because it skips unneeded subproblems."** Bottom-up loops usually have smaller constants, predictable memory access and no recursion depth limit.

## Go deeper

- Richard Bellman, *Dynamic Programming* (1957): the origin of the method and the principle of optimality.
- Jon Kleinberg and Éva Tardos, *Algorithm Design* (2005): chapter 6, careful development of subproblem design.
- Sanjoy Dasgupta, Christos Papadimitriou, Umesh Vazirani, *Algorithms* (2006): chapter 6, which presents DP as paths in a DAG.
