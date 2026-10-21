# Greedy Algorithms

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Design Paradigms](README.md)
> **Builds on:** [Correctness and Invariants](../01-foundations/correctness-and-invariants.md), [Heaps and Priority Queues](../02-fundamental-data-structures/heaps-and-priority-queues.md), [Proof Techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md)
> **Enables:** [Minimum Spanning Trees](../05-graph-algorithms/minimum-spanning-trees.md), [Shortest Paths](../05-graph-algorithms/shortest-paths.md), [Approximation Algorithms](../07-advanced-topics/approximation-algorithms.md), [Source Coding and Compression](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md)

## Essence

A greedy algorithm builds a solution one piece at a time, always taking the choice that looks best right now, and never going back. That is fast (often just a sort or a priority queue plus a linear scan) but usually wrong. It is right only when the problem has two properties: the *greedy-choice property* (some optimal solution starts with the locally best choice) and *optimal substructure* (after that choice, the rest is a smaller instance of the same problem). The design work is not the algorithm, which is usually obvious, but the proof that greed is safe, most often by an *exchange argument*. When greed is not optimal, it is still often a good *approximation*.

## Core tenets

1. **Greedy commits early and never reconsiders.** Each step picks the best-looking option by a fixed rule and adds it to the solution permanently. Contrast this with dynamic programming, which evaluates every option at every step. Greedy is a dynamic program in which provably only one branch ever needs exploring, so it is much faster.

2. **Correctness must be proved, because intuition fails.** Making change with the fewest coins by always taking the largest coin works for US coins (25, 10, 5, 1) but fails for coins (4, 3, 1) and amount 6: greedy gives 4+1+1, the optimum is 3+3. The rule "looks best now" has no built-in guarantee; the guarantee comes from problem structure.

3. **The exchange argument is the standard proof.** Take any optimal solution O. Show that if O differs from the greedy solution G at the first point of difference, you can swap O's choice for G's without making O worse. Repeating the swap turns O into G, so G is optimal. The invariant is "the greedy partial solution extends to some optimal solution."

4. **Interval scheduling shows the pattern cleanly.** To fit the most non-overlapping intervals, repeatedly pick the interval that *finishes earliest* and discard those that overlap it. Picking the shortest or the earliest-starting interval both fail on simple counterexamples. Earliest-finish works because it leaves the most room for the rest: any optimal schedule can swap its first interval for the earliest-finishing one. Cost: O(n log n) for sorting, then O(n).

5. **Cut and cycle properties make graph problems greedy.** For a Minimum Spanning Tree (MST), the lightest edge crossing any cut is safe to add (cut property), and the heaviest edge on any cycle is safe to exclude (cycle property). Kruskal's and Prim's algorithms are two orders of applying the cut property. Dijkstra's algorithm is greedy too: the unvisited vertex with the smallest tentative distance has its final distance, provided no edge weight is negative.

6. **Matroids characterise exactly when greedy is optimal.** A matroid is a set system where independent sets are closed under subsets and satisfy an exchange property (a smaller independent set can always be extended by an element of a larger one). For any weights, "sort by weight, add if still independent" finds the maximum-weight independent set if and only if the system is a matroid (Rado 1957, Edmonds 1971). Spanning forests of a graph form a matroid, which is why Kruskal works.

7. **Huffman coding is greedy over a priority queue.** To build an optimal prefix code, repeatedly merge the two least frequent symbols into a new node. An exchange argument shows the two rarest symbols can be siblings at the deepest level of some optimal tree. The result is within one bit per symbol of the entropy bound.

8. **When greedy is not optimal, it is often provably close.** For set cover (NP-hard), choosing the set covering the most uncovered elements gives a solution within a factor H(n) ≈ ln n of optimal, and no polynomial algorithm can do substantially better unless P = NP. Greedy is a main source of [approximation algorithms](../07-advanced-topics/approximation-algorithms.md) and of fast online heuristics (load balancing, caching).

## Key concepts

| Term | Meaning |
|---|---|
| Greedy-choice property | Some optimal solution contains the locally best first choice |
| Optimal substructure | An optimal solution contains optimal solutions to its subproblems |
| Exchange argument | Transform any optimum into the greedy solution step by step without loss |
| "Greedy stays ahead" | Proof that after each step greedy's partial solution is at least as good as any other's |
| Cut property | The lightest edge across a cut belongs to some MST |
| Matroid | Set system on which greedy is optimal for every weight function |
| Huffman code | Optimal prefix-free code built by repeatedly merging two least-frequent symbols |

## How it fits

- **Below:** proofs use [induction and contradiction](../../01-mathematical-foundations/01-logic/proof-techniques.md); implementations rely on sorting and [priority queues](../02-fundamental-data-structures/heaps-and-priority-queues.md).
- **Above:** [Huffman coding](../../02-theory-of-computation/01-information-theory/source-coding-and-compression.md) inside DEFLATE (zip, gzip) and Joint Photographic Experts Group (JPEG) images, [link-state routing](../../08-networking/03-network-layer/routing-algorithms.md) via Dijkstra, greedy [register allocation](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md) heuristics, [schedulers](../../07-operating-systems/02-process-management/scheduling.md) (shortest-job-first minimises average waiting time by an exchange argument), and greedy decoding in [language models](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md).
- **Siblings:** a special case of [dynamic programming](dynamic-programming.md); the fallback when greed fails and exactness is needed is [backtracking and branch and bound](backtracking-and-branch-and-bound.md).

## Common misconceptions

- **"Greedy is a heuristic, so it is never optimal."** For matroids, MSTs, interval scheduling and Huffman coding it is provably optimal.
- **"If greedy works on my examples, it is correct."** Counterexamples are often small but non-obvious, as with coin systems. Without an exchange proof, assume it is wrong.
- **"Dijkstra works with negative edges if no negative cycles exist."** It does not: a negative edge can lower the distance of an already-finalised vertex. Use Bellman–Ford.

## Go deeper

- Jon Kleinberg and Éva Tardos, *Algorithm Design* (2005): chapter 4, the clearest treatment of "greedy stays ahead" and exchange arguments.
- David A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes" (1952).
- Jack Edmonds, "Matroids and the Greedy Algorithm" (1971).
