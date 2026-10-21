# Shortest Paths

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Graph Algorithms](README.md)
> **Builds on:** [Graph Traversal](graph-traversal.md), [Heaps and Priority Queues](../02-fundamental-data-structures/heaps-and-priority-queues.md), [Greedy Algorithms](../03-design-paradigms/greedy-algorithms.md), [Dynamic Programming](../03-design-paradigms/dynamic-programming.md)
> **Enables:** [Routing Algorithms](../../08-networking/03-network-layer/routing-algorithms.md), [Search and Planning](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md), [Network Flow](network-flow.md), [Internet Routing and BGP](../../08-networking/03-network-layer/internet-routing-and-bgp.md)

## Essence

Given a graph with weighted edges, find the cheapest path from a source to every other vertex (single-source) or between every pair (all-pairs). All algorithms rest on one operation, *relaxation*: if going to u and then along edge (u, v) is cheaper than the best known route to v, update v's distance. They differ in the order of relaxations. Dijkstra's algorithm relaxes greedily from the closest unfinished vertex and needs non-negative weights; it runs in O((V + E) log V) with a binary heap. Bellman–Ford relaxes every edge V − 1 times, handles negative weights and detects negative cycles in O(VE). Floyd–Warshall computes all pairs by dynamic programming in Θ(V³).

## Core tenets

1. **Relaxation maintains upper bounds that converge to true distances.** Keep d[v], an overestimate of the true distance δ(v), initially ∞ except d[source] = 0. Relaxing edge (u, v) sets d[v] = min(d[v], d[u] + w(u, v)). The invariant d[v] ≥ δ(v) always holds, and if relaxations are applied along a shortest path in order, d[v] reaches δ(v). Every algorithm here is a schedule of relaxations that guarantees that order.

2. **Shortest paths have optimal substructure.** Any prefix of a shortest path is itself a shortest path. That is why distances obey δ(v) = min over edges (u, v) of δ(u) + w(u, v) (the Bellman equation), and why a single shortest-path *tree* of parent pointers encodes shortest paths to all vertices from one source.

3. **Dijkstra's invariant: the closest unfinished vertex is final.** Repeatedly extract the vertex u with the smallest d[u] from a priority queue, mark it finished, and relax its outgoing edges. With non-negative weights, any other path to u must leave the finished set through some vertex whose d is already ≥ d[u] and can only add weight, so d[u] = δ(u). Cost: V extract-mins and up to E decrease-keys: O((V + E) log V) with a binary heap, O(E + V log V) with a Fibonacci heap.

4. **Negative edges break Dijkstra; negative cycles break the problem.** A negative edge can make a path through a not-yet-finished vertex cheaper than an already-finalised distance, violating Dijkstra's invariant. If a cycle has negative total weight and is reachable, "shortest" is undefined because you can loop forever. Bellman–Ford handles both: after V − 1 rounds of relaxing all edges, every shortest path (at most V − 1 edges) has been relaxed in order; if a V-th round still improves something, a negative cycle exists. Cost Θ(VE).

5. **On a DAG, one pass in topological order suffices.** If there are no cycles, relax each vertex's outgoing edges in topological order; every path is relaxed in order. This is O(V + E) and works with negative weights. It is the basis of critical-path scheduling, where you find the *longest* path by negating weights.

6. **All-pairs: Floyd–Warshall is DP over allowed intermediate vertices.** Let d_k[i][j] be the shortest path from i to j using only intermediates from {1..k}. Then d_k[i][j] = min(d_{k−1}[i][j], d_{k−1}[i][k] + d_{k−1}[k][j]). Three nested loops give Θ(V³) time and Θ(V²) space, with tiny constants and regular memory access. For sparse graphs, Johnson's algorithm (reweight with Bellman–Ford so all weights are non-negative, then run Dijkstra from each vertex) achieves O(VE + V² log V).

7. **Heuristics make point-to-point search fast without losing correctness.** A* search orders the frontier by d[v] + h(v), where h estimates the remaining distance. If h never overestimates (admissible) and satisfies the triangle inequality (consistent), A* returns optimal paths while expanding far fewer vertices than Dijkstra. Straight-line distance on maps is the classic h. Road-network services go further with preprocessing (contraction hierarchies, hub labels) and answer continental queries in microseconds to milliseconds.

8. **Distributed routing protocols are these algorithms run by routers.** Link-state protocols such as Open Shortest Path First (OSPF) flood the topology to every router, and each runs Dijkstra locally. Distance-vector protocols such as the Routing Information Protocol (RIP) are distributed Bellman–Ford: each router repeatedly tells neighbours its distances. Distributed Bellman–Ford converges slowly after failures (the "count-to-infinity" problem), which is a direct consequence of relaxing with stale information.

## Key concepts

| Term | Meaning |
|---|---|
| Relaxation | Update d[v] = min(d[v], d[u] + w(u, v)) |
| Shortest-path tree | Parent pointers encoding shortest paths from one source to all vertices |
| Dijkstra's algorithm | Greedy single-source algorithm for non-negative weights, O((V + E) log V) |
| Bellman–Ford | V − 1 rounds of relaxing all edges; handles negative weights; Θ(VE) |
| Negative cycle | Cycle with total weight < 0; makes shortest distances undefined |
| Floyd–Warshall | All-pairs dynamic programming over intermediate vertices, Θ(V³) |
| A* search | Dijkstra guided by an admissible heuristic estimate of remaining cost |
| Admissible heuristic | Never overestimates the true remaining distance |

## How it fits

- **Below:** traversal skeleton from [graph traversal](graph-traversal.md); frontier from [priority queues](../02-fundamental-data-structures/heaps-and-priority-queues.md); correctness from [greedy](../03-design-paradigms/greedy-algorithms.md) and [dynamic programming](../03-design-paradigms/dynamic-programming.md) arguments.
- **Above:** [intra-domain routing](../../08-networking/03-network-layer/routing-algorithms.md) (OSPF; Intermediate System to Intermediate System, IS-IS; RIP); [Border Gateway Protocol (BGP)](../../08-networking/03-network-layer/internet-routing-and-bgp.md), a path-vector relative that optimises policy rather than distance; [A\* planning](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md) in Artificial Intelligence (AI) and robotics; currency arbitrage detection (a negative cycle in −log exchange rates).
- **Siblings:** generalises BFS from [traversal](graph-traversal.md); [Prim's MST algorithm](minimum-spanning-trees.md) has the same code shape but keys the frontier by single edge weight, not total distance; [network flow](network-flow.md) uses shortest augmenting paths (Edmonds–Karp) and min-cost flow uses shortest paths with potentials.

## Common misconceptions

- **"Dijkstra works if I just add a constant to every weight to make them positive."** That changes which path is shortest by penalising paths with more edges. Johnson's reweighting uses vertex potentials instead, which preserves shortest paths.
- **"Dijkstra is the shortest path algorithm."** It is one of several; the right choice depends on negative weights, DAG structure, and single-pair vs all-pairs queries.
- **"A\* with any heuristic is optimal."** Only an admissible heuristic guarantees optimality; an overestimating one can return a suboptimal path faster.

## Go deeper

- Edsger W. Dijkstra, "A Note on Two Problems in Connexion with Graphs" (1959): the original shortest-path and spanning-tree algorithms in three pages.
- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (4th ed., 2022): single-source and all-pairs shortest paths chapters.
- Peter Hart, Nils Nilsson, Bertram Raphael, "A Formal Basis for the Heuristic Determination of Minimum Cost Paths" (1968): A*.
