# Graph Algorithms

> **Layer:** [05 Algorithms and Data Structures](../README.md) › Graph Algorithms
> **Children:** [Graph Traversal](graph-traversal.md) · [Shortest Paths](shortest-paths.md) · [Minimum Spanning Trees](minimum-spanning-trees.md) · [Network Flow](network-flow.md)

## What this area is about

A graph is a set of vertices joined by edges. It is the most general model of relationships: road networks, the Internet, social networks, call graphs, dependency graphs, state spaces, circuits. A huge range of practical questions reduce to a few graph problems: *what can I reach?* (traversal), *what is the cheapest route?* (shortest paths), *what is the cheapest way to connect everything?* (spanning trees), and *how much can flow through?* (network flow). This area gives the efficient algorithms for each, usually linear or near-linear in the size of the graph.

The unifying idea is **systematic exploration with a frontier**. Breadth-First Search (BFS), Depth-First Search (DFS), Dijkstra's algorithm and Prim's algorithm are all the same skeleton: keep a set of discovered-but-unfinished vertices and repeatedly take one out, differing only in *which* one (oldest, newest, closest, cheapest edge). The data structure holding the frontier (queue, stack, priority queue) determines the algorithm. Flow algorithms add a second idea: improve a feasible solution along augmenting paths until a matching dual bound (a minimum cut) proves optimality.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Graph Traversal](graph-traversal.md) | BFS, DFS, topological sort, connected and strongly connected components | [Stacks and queues](../02-fundamental-data-structures/stacks-and-queues.md), [graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md) |
| [Shortest Paths](shortest-paths.md) | Dijkstra, Bellman–Ford, Floyd–Warshall, A* | Traversal, [heaps](../02-fundamental-data-structures/heaps-and-priority-queues.md), [dynamic programming](../03-design-paradigms/dynamic-programming.md) |
| [Minimum Spanning Trees](minimum-spanning-trees.md) | Kruskal, Prim, Borůvka; cut property; union-find | Traversal, [greedy](../03-design-paradigms/greedy-algorithms.md), heaps, [amortized analysis](../01-foundations/amortized-analysis.md) |
| [Network Flow](network-flow.md) | Max-flow min-cut, augmenting paths, matching | Traversal (to find augmenting paths), shortest paths |

```
                       frontier = ?
   graph traversal ──── queue ──► BFS (unweighted shortest paths)
         │         └─── stack ──► DFS (cycles, topological order, components)
         │
         ├── priority queue keyed by distance ──► Dijkstra (shortest paths)
         ├── priority queue keyed by edge weight ► Prim (minimum spanning tree)
         └── repeated BFS for augmenting paths ──► Edmonds–Karp (max flow)
```

Read traversal first; everything else is traversal with a different frontier or repeated traversal. Shortest paths and spanning trees are both greedy over a priority queue but optimise different things (distance from a source vs total edge weight). Flow is the most general and connects to linear programming duality.

## Connections to sibling areas

- **[Foundations](../01-foundations/README.md):** Dijkstra's correctness is a textbook invariant proof; union-find's near-constant cost is a textbook amortized bound.
- **[Fundamental Data Structures](../02-fundamental-data-structures/README.md):** graphs are stored as adjacency lists (arrays of lists) or matrices; frontiers are queues, stacks and heaps.
- **[Design Paradigms](../03-design-paradigms/README.md):** Dijkstra, Prim and Kruskal are greedy; Bellman–Ford and Floyd–Warshall are dynamic programming; graph colouring and Hamiltonian paths need backtracking.
- **[Sorting and Searching](../04-sorting-and-searching/README.md):** Kruskal sorts edges; topological sort orders a partial order.
- **[String Algorithms](../06-string-algorithms/README.md):** automata are graphs; string matching with automata is a walk on a graph.
- **[Advanced Topics](../07-advanced-topics/README.md):** many NP-hard graph problems (vertex cover, travelling salesperson) have approximation algorithms; massive graphs need external-memory and streaming techniques.

## Connections across layers

Graphs come from [graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md), and the hard graph problems ([colouring, Hamiltonian cycle](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md)) mark the edge of tractability. Above: [routing protocols](../../08-networking/03-network-layer/routing-algorithms.md) run Dijkstra and Bellman–Ford; [garbage collectors](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md) are graph traversals; [deadlock detection](../../07-operating-systems/03-concurrency/deadlock.md) finds cycles; [build systems](../../12-software-engineering/04-operations/build-and-continuous-delivery.md) topologically sort dependencies; [compilers](../../06-programming-languages/03-compilers/intermediate-representations.md) analyse control-flow graphs; [Artificial Intelligence (AI) planners](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md) search implicit state graphs.

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): one graph model covers roads, packets, objects in memory and task dependencies.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): the finished set in Dijkstra, the cut property in Minimum Spanning Trees (MSTs), flow conservation.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): max-flow equals min-cut; many neighbouring problems are NP-hard.
- [Composition](../../CROSS-CUTTING.md#composition): complex algorithms are built from traversal plus a frontier policy.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): union-find with path compression.
