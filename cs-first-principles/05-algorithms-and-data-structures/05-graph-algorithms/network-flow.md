# Network Flow

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Graph Algorithms](README.md)
> **Builds on:** [Graph Traversal](graph-traversal.md), [Shortest Paths](shortest-paths.md), [Optimization](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md), [Linear Algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md)
> **Enables:** [Approximation Algorithms](../07-advanced-topics/approximation-algorithms.md), [Computer Vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md), [Scheduling](../../07-operating-systems/02-process-management/scheduling.md), [Latency, Bandwidth and Queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md)

## Essence

A flow network is a directed graph where each edge has a capacity, with a source s and a sink t. A flow assigns to each edge an amount up to its capacity so that, at every vertex except s and t, inflow equals outflow. The maximum-flow problem asks for the most that can travel from s to t. Its central theorem, max-flow min-cut, says this maximum equals the smallest total capacity of edges whose removal disconnects t from s. The Ford–Fulkerson method finds it by repeatedly pushing flow along *augmenting paths* in a residual graph that also allows cancelling earlier flow. Because so many problems (bipartite matching, assignment, scheduling, image segmentation, edge-disjoint paths) reduce to flow, it is one of the most useful algorithmic tools.

## Core tenets

1. **Flow obeys two constraints: capacity and conservation.** On each edge, 0 ≤ f(u, v) ≤ c(u, v). At each internal vertex, flow in equals flow out. The value of the flow is the net amount leaving s. These are linear constraints, so max flow is a Linear Programming (LP) problem, but specialised algorithms are much faster than general LP solvers.

2. **The residual graph lets an algorithm undo bad choices.** For each edge with flow f and capacity c, the residual graph has a forward edge with capacity c − f (room to add) and a backward edge with capacity f (room to cancel). Without backward edges, a greedy choice of path can block the optimum. With them, any improvement to the flow appears as a simple s–t path in the residual graph.

3. **Ford–Fulkerson: augment until no path remains.** Find any s–t path in the residual graph, push the minimum residual capacity along it, update, repeat. When no augmenting path exists, the flow is maximum. With integer capacities each augmentation adds at least 1, so it terminates, but it can take time proportional to the flow value, and with irrational capacities a bad path choice may never terminate.

4. **Max-flow equals min-cut, and each certifies the other.** For any flow f and any s–t cut (S, T), the flow value is at most the cut's capacity, since everything from s to t must cross the cut. When Ford–Fulkerson stops, the vertices reachable from s in the residual graph form a cut whose edges are all saturated, so flow value = cut capacity, and both are optimal (Ford and Fulkerson; Elias, Feinstein and Shannon; both 1956). This is an instance of LP duality, and it gives a proof of optimality you can check.

5. **Choosing paths wisely gives polynomial time.** Edmonds–Karp (1972) always augments along a shortest path (found by Breadth-First Search (BFS)), which bounds the number of augmentations by O(VE), giving O(VE²) total. Dinic's algorithm augments along all shortest paths at once in blocking flows: O(V²E) in general and O(E√V) for unit-capacity bipartite matching (Hopcroft–Karp). Push-relabel algorithms (Goldberg and Tarjan, 1988) work locally and run in O(V³) or better, and are often fastest in practice. In 2022, Chen, Kyng, Liu, Peng, Probst Gutenberg and Sachdeva gave an almost-linear-time max-flow algorithm, m^(1+o(1)), a theoretical milestone not yet used in practice.

6. **Integer capacities give integer flows.** If all capacities are integers, Ford–Fulkerson produces an integer maximum flow, since every augmentation is by an integer amount. This *integrality theorem* is what makes flow a tool for combinatorial problems: a flow of 0 or 1 on an edge can mean "chosen" or "not chosen".

7. **Many problems reduce to flow.** Maximum bipartite matching: connect s to every left vertex and every right vertex to t with capacity 1; max flow = max matching. Menger's theorem: the number of edge-disjoint s–t paths equals the minimum number of edges whose removal separates s from t. Project selection, baseball elimination, and binary image segmentation (graph cuts) are min-cut problems in disguise. Recognising a reduction is often the whole solution.

8. **Min-cost flow and its dual add prices.** Min-cost flow sends a required amount at the least total cost per unit, solved by successive shortest augmenting paths with vertex potentials or by network simplex. It generalises shortest paths, assignment (the Hungarian algorithm) and transportation problems, and is widely used in logistics and in data-centre and cluster scheduling.

## Key concepts

| Term | Meaning |
|---|---|
| Capacity | Maximum flow allowed on an edge |
| Flow conservation | Inflow equals outflow at every vertex except source and sink |
| Residual graph | Graph of remaining capacity, including backward edges to cancel flow |
| Augmenting path | s–t path in the residual graph with positive capacity |
| s–t cut | Partition (S, T) with s ∈ S, t ∈ T; capacity is the sum over edges from S to T |
| Max-flow min-cut theorem | Maximum flow value equals minimum cut capacity |
| Integrality theorem | Integer capacities admit an integer maximum flow |
| Push-relabel | Max-flow method that pushes excess locally using vertex heights |

## How it fits

- **Below:** is a special [linear program](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md) whose constraint matrix is totally unimodular (the [linear-algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md) reason flows are integral); uses BFS from [graph traversal](graph-traversal.md) and potentials from [shortest paths](shortest-paths.md).
- **Above:** graph-cut segmentation in [computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md); bipartite matching in task assignment and cluster [scheduling](../../07-operating-systems/02-process-management/scheduling.md); [network capacity](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) and traffic engineering; LP rounding in [approximation algorithms](../07-advanced-topics/approximation-algorithms.md); reliability analysis (min-cut as the weakest set of links).
- **Siblings:** generalises [shortest paths](shortest-paths.md) (min-cost flow of one unit) and relies on [traversal](graph-traversal.md); unlike [minimum spanning trees](minimum-spanning-trees.md), greedy alone fails here, which is why backward residual edges exist.

## Common misconceptions

- **"Greedily pushing flow along paths finds the maximum."** Without residual backward edges it can get stuck at a suboptimal flow.
- **"Ford–Fulkerson is polynomial."** Its running time depends on capacities and path choice; Edmonds–Karp's shortest-path rule is what makes it polynomial.
- **"Min-cut is a separate hard problem."** It falls out of any max-flow computation for free, as the set of vertices reachable from s in the final residual graph.

## Go deeper

- L. R. Ford Jr. and D. R. Fulkerson, *Flows in Networks* (1962): the founding book.
- Jon Kleinberg and Éva Tardos, *Algorithm Design* (2005): chapter 7, with an excellent catalogue of reductions to flow.
- Ravindra Ahuja, Thomas Magnanti, James Orlin, *Network Flows: Theory, Algorithms, and Applications* (1993): the comprehensive reference.
