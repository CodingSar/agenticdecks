# Graph Traversal

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Graph Algorithms](README.md)
> **Builds on:** [Graph Theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md), [Stacks and Queues](../02-fundamental-data-structures/stacks-and-queues.md), [Arrays and Linked Lists](../02-fundamental-data-structures/arrays-and-linked-lists.md), [Relations and Orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md)
> **Enables:** [Shortest Paths](shortest-paths.md), [Network Flow](network-flow.md), [Memory Management and Garbage Collection](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md), [Deadlock](../../07-operating-systems/03-concurrency/deadlock.md), [Build and Continuous Delivery](../../12-software-engineering/04-operations/build-and-continuous-delivery.md)

## Essence

Graph traversal visits every vertex reachable from a starting point, each exactly once, in O(V + E) time for a graph with V vertices and E edges stored as adjacency lists. The two fundamental orders are Breadth-First Search (BFS), which explores in rings of increasing distance using a queue, and Depth-First Search (DFS), which goes as deep as possible before backing up, using a stack or recursion. BFS gives shortest paths in unweighted graphs. DFS gives a rich structure (discovery and finish times, tree and back edges) from which you get cycle detection, topological order, and connected and strongly connected components, all in linear time. Most graph algorithms are a traversal with extra bookkeeping.

## Core tenets

1. **Marking vertices as visited is what makes traversal linear.** Without a visited set, cycles cause infinite loops and shared substructure causes exponential re-exploration. With it, each vertex is processed once and each adjacency list is scanned once, so total work is O(V + E). On an adjacency matrix the same traversal costs Θ(V²), because finding a vertex's neighbours scans a whole row.

2. **Representation decides cost: adjacency lists for sparse graphs, matrices for dense.** Real graphs are usually sparse (E much less than V²: road networks average under 4 edges per vertex). Adjacency lists use Θ(V + E) space and enumerate neighbours in time proportional to degree. Matrices use Θ(V²) space but test "is (u, v) an edge?" in O(1). Compressed Sparse Row (CSR), all neighbour lists concatenated in one array plus an offset array, is the cache-friendly standard for large static graphs.

3. **BFS discovers vertices in non-decreasing distance order.** The queue holds the frontier: all vertices at distance d are dequeued before any at distance d + 1, because they were enqueued earlier. So the first time BFS reaches a vertex, it has found a path with the fewest edges, and recording the parent gives a shortest-path tree. This invariant is exactly what Dijkstra's algorithm generalises to weighted edges.

4. **DFS classifies edges, and back edges mean cycles.** In a directed graph, DFS labels each edge as tree, back (to an ancestor still on the stack), forward or cross. A directed graph has a cycle if and only if DFS finds a back edge. Undirected graphs have only tree and back edges, which is why DFS cleanly finds bridges and articulation points (single points of failure) via the low-link values introduced by Hopcroft and Tarjan.

5. **Reverse DFS finishing order is a topological sort.** A Directed Acyclic Graph (DAG) can be linearly ordered so every edge points forward. In DFS on a DAG, a vertex finishes only after everything reachable from it has finished, so listing vertices by decreasing finish time puts each before its successors. Kahn's algorithm achieves the same by repeatedly removing vertices with no incoming edges. Both are O(V + E) and both detect cycles as a by-product.

6. **Strongly connected components are found in linear time.** In a directed graph, a Strongly Connected Component (SCC) is a maximal set where every vertex reaches every other. Tarjan's algorithm (one DFS with low-links) and Kosaraju's (DFS on the graph, then DFS on the reversed graph in reverse finish order) both run in O(V + E). Collapsing SCCs yields a DAG, the condensation, which is how 2-SAT (satisfiability with two literals per clause) is solved in linear time and how compilers find loops and mutually recursive functions.

7. **Reachability is the essence of garbage collection and dependency analysis.** A tracing garbage collector marks everything reachable from the roots (stack, registers, globals) by traversal; unmarked objects are garbage. Build tools compute what must be rebuilt as everything reachable from a changed file in the reverse dependency graph. Deadlock detection looks for a cycle in the wait-for graph.

8. **Traversal order matters for memory and parallelism.** Recursive DFS on a graph with a long path (millions of vertices) overflows the call stack; use an explicit stack. BFS's frontier can hold Θ(V) vertices at once. On huge graphs, random neighbour access causes a cache miss per edge, which is why graph analytics frameworks reorder vertices for locality and process frontiers level-synchronously in parallel ("direction-optimising" BFS switches between pushing from and pulling into the frontier).

## Key concepts

| Term | Meaning |
|---|---|
| Adjacency list / matrix | Per-vertex neighbour lists, Θ(V + E) space / V × V bit or weight table, Θ(V²) |
| BFS | Queue-based traversal by increasing hop distance |
| DFS | Stack- or recursion-based traversal that goes deep first |
| Discovery / finish time | When DFS first reaches / last leaves a vertex |
| Back edge | DFS edge to an ancestor on the current path; signals a cycle |
| Topological order | Linear order of a DAG with every edge pointing forward |
| SCC | Maximal set of mutually reachable vertices in a directed graph |
| Condensation | DAG obtained by collapsing each SCC to one vertex |

## How it fits

- **Below:** graphs, paths and cycles come from [graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md); a topological order is a linear extension of a [partial order](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md); frontiers are [stacks and queues](../02-fundamental-data-structures/stacks-and-queues.md).
- **Above:** [garbage collection](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md), [deadlock detection](../../07-operating-systems/03-concurrency/deadlock.md), [build ordering](../../12-software-engineering/04-operations/build-and-continuous-delivery.md), web crawling, [control-flow analysis](../../06-programming-languages/03-compilers/intermediate-representations.md), [state-space exploration in model checking](../../06-programming-languages/05-formal-methods/model-checking.md), uninformed [search in Artificial Intelligence (AI)](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md), and dataflow scheduling in [stream processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md).
- **Siblings:** [shortest paths](shortest-paths.md) replaces the queue with a priority queue; [network flow](network-flow.md) repeatedly uses BFS to find augmenting paths; [minimum spanning trees](minimum-spanning-trees.md) use traversal-like growth (Prim) or connectivity queries (Kruskal); when edges arrive over time, [union–find](../02-fundamental-data-structures/union-find.md) maintains connected components incrementally instead of re-traversing.

## Common misconceptions

- **"DFS finds shortest paths."** It finds *a* path, often a long one. BFS finds fewest-edge paths; weighted graphs need Dijkstra or Bellman–Ford.
- **"Traversal is O(V²)."** Only with an adjacency matrix. With adjacency lists it is O(V + E), which for sparse graphs is near-linear in V.
- **"Topological sort works on any directed graph."** Only on DAGs; a cycle means no valid order exists, and the algorithm detects this.

## Go deeper

- Robert Tarjan, "Depth-First Search and Linear Graph Algorithms" (1972): DFS as an algorithmic tool; linear-time SCCs.
- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (4th ed., 2022): elementary graph algorithms chapter.
- Steven S. Skiena, *The Algorithm Design Manual* (3rd ed., 2020): practical guidance on graph representations and traversal applications.
