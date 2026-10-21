# Minimum Spanning Trees

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Graph Algorithms](README.md)
> **Builds on:** [Greedy Algorithms](../03-design-paradigms/greedy-algorithms.md), [Heaps and Priority Queues](../02-fundamental-data-structures/heaps-and-priority-queues.md), [Union–Find](../02-fundamental-data-structures/union-find.md), [Amortized Analysis](../01-foundations/amortized-analysis.md), [Graph Theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md)
> **Enables:** [Approximation Algorithms](../07-advanced-topics/approximation-algorithms.md), [Unsupervised Learning](../../13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md), [Media Access and Ethernet](../../08-networking/02-link-layer/media-access-and-ethernet.md)

## Essence

Given a connected undirected graph with edge weights, a Minimum Spanning Tree (MST) is a set of V − 1 edges that connects all V vertices with the smallest possible total weight. It models the cheapest way to wire a network, and it is a building block for clustering and approximation. The problem is solved exactly by simple greedy algorithms because of one structural fact, the *cut property*: for any division of the vertices into two groups, the lightest edge crossing between them belongs to some MST. Kruskal's algorithm adds edges globally from lightest to heaviest, skipping those that form a cycle; Prim's grows one tree outward from a start vertex; Borůvka's grows all components in parallel. All run in O(E log V).

## Core tenets

1. **The cut property makes greed safe.** Take any cut (S, V − S) and its lightest crossing edge e. If an MST T omitted e, adding e to T creates a cycle that crosses the cut at least twice; removing the other crossing edge on that cycle gives a spanning tree no heavier than T. So some MST contains e. Every MST algorithm is a different way of choosing cuts and adding their lightest edges.

2. **The cycle property is the mirror image.** The heaviest edge on any cycle (if strictly heaviest) is in no MST, because removing it and reconnecting through the rest of the cycle never costs more. This justifies algorithms that delete edges ("reverse-delete") and lets you verify an MST: a spanning tree is minimum if and only if every non-tree edge is the heaviest on the cycle it would close.

3. **Kruskal's algorithm needs fast "same component?" queries.** Sort edges by weight (O(E log E) = O(E log V)), then scan them, adding an edge if its endpoints are in different components. The invariant: the chosen edges form a forest contained in some MST. Component queries use a [union–find](../02-fundamental-data-structures/union-find.md) (disjoint-set) structure, so the sort dominates. Kruskal is natural when edges are already sorted or arrive as a list.

4. **Union–find is nearly constant time per operation.** Each component is a tree of parent pointers whose root names it. *Union by rank* hangs the shorter tree under the taller; *path compression* repoints every node on a find path to the root. Together, m operations cost O(m·α(n)), where α is the inverse Ackermann function, at most 4 for any realistic n (Tarjan, 1975). The bound is tight: Tarjan showed the algorithm really needs it, and Fredman and Saks (1989) showed no union–find structure can do asymptotically better. Kruskal therefore runs in O(E log E) for the sort plus O(E·α(V)) for the scan.

5. **Prim's algorithm is Dijkstra with a different key.** Grow a single tree from any vertex; repeatedly add the lightest edge leaving the tree. A priority queue keyed by each outside vertex's cheapest connecting edge gives O((V + E) log V) with a binary heap, O(E + V log V) with a Fibonacci heap, or Θ(V²) with a plain array (best for dense graphs). The cut each step is (tree, rest).

6. **Borůvka's algorithm is the oldest and the most parallel.** In each round, every component picks its lightest outgoing edge, and all are added at once (ties broken consistently to avoid cycles). Each round at least halves the number of components, so there are O(log V) rounds of O(E) work. Because components act independently, it suits parallel and distributed settings; it dates from 1926, for planning an electrical network in Moravia.

7. **The theoretical frontier is near-linear.** Randomized MST runs in expected O(E) time (Karger, Klein and Tarjan, 1995). The best deterministic bound is O(E·α(E, V)) (Chazelle, 2000), and an optimal deterministic algorithm is known whose running time is unknown but provably optimal (Pettie and Ramachandran, 2002). In practice Kruskal or Prim with a binary heap is fast enough for graphs with hundreds of millions of edges.

8. **MSTs underpin clustering and approximation.** Deleting the k − 1 heaviest MST edges yields the k-clustering that maximises the minimum distance between clusters (single-linkage clustering). Doubling an MST and shortcutting repeated vertices gives a tour at most twice the optimal for the metric Travelling Salesperson Problem (TSP); Christofides' algorithm improves this to 1.5. The minimum spanning tree is a lower bound on any tour, since removing one edge from a tour leaves a spanning tree.

## Key concepts

| Term | Meaning |
|---|---|
| Spanning tree | Acyclic subgraph connecting all vertices; has exactly V − 1 edges |
| Cut | Partition of vertices into two sets; crossing edges join them |
| Cut property | The lightest edge across any cut is in some MST |
| Cycle property | The unique heaviest edge on any cycle is in no MST |
| Union–find (disjoint set) | Structure supporting union and find on partitions; O(α(n)) amortized |
| Path compression | Pointing nodes on a find path directly at the root |
| Kruskal / Prim / Borůvka | Global sorted scan / single growing tree / all components grow in parallel |
| Single-linkage clustering | Clusters obtained by removing heaviest MST edges |

## How it fits

- **Below:** trees and cycles from [graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md); correctness is the [greedy](../03-design-paradigms/greedy-algorithms.md) exchange argument and, abstractly, spanning forests form a matroid; costs use [heaps](../02-fundamental-data-structures/heaps-and-priority-queues.md), [sorting](../04-sorting-and-searching/comparison-sorting.md) and [amortized analysis](../01-foundations/amortized-analysis.md).
- **Above:** the Spanning Tree Protocol in [Ethernet](../../08-networking/02-link-layer/media-access-and-ethernet.md) builds a loop-free tree (a spanning tree, shortest-path rather than minimum) over bridges; single-linkage [clustering](../../13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md); [approximation](../07-advanced-topics/approximation-algorithms.md) for travelling salesperson and Steiner tree; image segmentation in [computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md).
- **Siblings:** Prim mirrors Dijkstra from [shortest paths](shortest-paths.md); [union–find](../02-fundamental-data-structures/union-find.md) answers incremental connectivity (edges added, never removed) where [traversal](graph-traversal.md) would recompute components from scratch; [network flow](network-flow.md) studies a different global quantity of the same graphs.

## Common misconceptions

- **"The MST contains the shortest path between every pair of vertices."** It minimises total weight, not individual paths; MST paths can be much longer than shortest paths.
- **"The MST is unique."** Only if edge weights are distinct; with ties there may be many, all with the same total weight.
- **"Union–find is O(log n) per operation."** With both union by rank and path compression it is O(α(n)) amortized, effectively constant.

## Go deeper

- Robert Tarjan, "Efficiency of a Good But Not Linear Set Union Algorithm" (1975): the inverse-Ackermann analysis of union-find.
- Joseph B. Kruskal, "On the Shortest Spanning Subtree of a Graph and the Traveling Salesman Problem" (1956).
- Jon Kleinberg and Éva Tardos, *Algorithm Design* (2005): chapter 4 on MSTs via the cut property and clustering.
