# Graph Theory

> **Layer:** [01 Mathematical Foundations](../README.md) › [Discrete Mathematics](README.md)
> **Builds on:** [Relations and Orders](../02-sets-relations-functions/relations-and-orders.md), [Combinatorics](combinatorics.md)
> **Enables:** [Graph Traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md), [Shortest Paths](../../05-algorithms-and-data-structures/05-graph-algorithms/shortest-paths.md), [Routing Algorithms](../../08-networking/03-network-layer/routing-algorithms.md), [Deadlock](../../07-operating-systems/03-concurrency/deadlock.md), [Code Generation and Register Allocation](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md)

## Essence

A graph is a set of vertices joined by edges; it is the mathematical form of "things and the connections between them". It abstracts away everything except connectivity, which is why the same theorems apply to road maps, computer networks, call graphs, dependency trees, state machines, social networks and the resource-wait graphs of an operating system. Graph theory asks structural questions: is everything connected, is there a cycle, what is the shortest route, can vertices be coloured so neighbours differ, how much can flow from one point to another. Its value to Computer Science (CS) is that once a problem is phrased as a graph question, decades of results tell you whether it is easy (shortest path, spanning tree, matching) or hard (colouring, Hamiltonian cycle, clique).

## Core tenets

1. **A graph is a relation drawn as a picture.** A directed graph on vertex set *V* is a binary [relation](../02-sets-relations-functions/relations-and-orders.md) `E ⊆ V × V`; an undirected graph is a symmetric one. Paths correspond to chains in the relation and reachability to its transitive closure. Weights, labels and capacities are functions on edges. This is why graph algorithms and relation algorithms are often the same algorithms.

2. **Representation decides cost.** An adjacency matrix uses Θ(V²) space and answers "is there an edge u→v?" in O(1); an adjacency list uses Θ(V + E) and lists a vertex's neighbours in time proportional to its degree. Most real graphs are sparse (E far below V²: a web page links to tens of pages, not billions), so lists win, and graph algorithms are stated in terms of V and E separately for this reason.

3. **The handshake lemma constrains every graph.** In an undirected graph, the sum of vertex degrees equals 2E, because each edge contributes to two endpoints. So the number of odd-degree vertices is even, and the average degree is 2E/V. Simple facts like this bound the work of algorithms that touch each edge from both ends.

4. **Trees are minimally connected graphs.** A tree on *n* vertices is connected and acyclic, and has exactly *n − 1* edges; adding any edge creates exactly one cycle and removing any edge disconnects it. Trees are the shape of hierarchies (file systems, parse trees, the Domain Name System (DNS)), of search structures, and of spanning trees that connect a network without loops, which is what Ethernet's spanning tree protocol and [minimum spanning tree](../../05-algorithms-and-data-structures/05-graph-algorithms/minimum-spanning-trees.md) algorithms compute.

5. **Directed acyclic graphs are partial orders, and cycles mean circular dependency.** A Directed Acyclic Graph (DAG) admits a topological order; a cycle forbids one. A cycle in a wait-for graph is a [deadlock](../../07-operating-systems/03-concurrency/deadlock.md); a cycle in a module dependency graph breaks a build; a cycle in a reference graph defeats reference counting. Detecting cycles by depth-first search is linear time, so these failures are cheap to find once modelled as graphs.

6. **Bipartiteness and colouring model conflicts.** A graph is 2-colourable (bipartite) exactly when it has no odd cycle, which is checkable in linear time. *k*-colouring for k ≥ 3 is NP-complete (as hard as any problem in Nondeterministic Polynomial time, NP). Register allocation colours an interference graph (variables that are live at the same time cannot share a register), exam scheduling and frequency assignment are colouring too, which is why compilers use heuristics rather than optimal allocators.

7. **Similar-sounding problems differ wildly in difficulty.** An Euler circuit (use every *edge* once) exists exactly when the graph is connected and every degree is even, a condition checkable in linear time. A Hamiltonian cycle (visit every *vertex* once) is NP-complete. Shortest path is polynomial; longest simple path is NP-hard. Learning which side of the line a problem falls on is one of the most practical skills graph theory gives.

8. **Cuts and flows are dual.** Menger's theorem and the max-flow min-cut theorem state that the maximum amount that can be pushed from *s* to *t* equals the minimum capacity of edges whose removal separates them. This duality gives polynomial algorithms for [network flow](../../05-algorithms-and-data-structures/05-graph-algorithms/network-flow.md) and bipartite matching, and it measures network resilience: the number of edge-disjoint paths is how many link failures a connection survives.

## Key concepts

| Term | Meaning |
|---|---|
| Vertex / edge | A node / a connection between two nodes |
| Directed / undirected | Edges have / lack a direction |
| Degree | Number of edges at a vertex (in-degree and out-degree if directed) |
| Path / cycle | A sequence of edges / a path that returns to its start |
| Connected component | A maximal set of mutually reachable vertices |
| Tree | Connected acyclic graph; n vertices, n − 1 edges |
| DAG | Directed graph with no directed cycle |
| Bipartite | Vertices split in two sides with edges only between sides |
| Colouring | Labelling vertices so adjacent ones differ |
| Cut | A set of edges whose removal disconnects the graph |
| Sparse / dense | E = O(V) roughly / E close to V² |

## How it fits

- **Below:** Graphs are [relations](../02-sets-relations-functions/relations-and-orders.md) with structure; counting graphs and paths uses [combinatorics](combinatorics.md); correctness proofs use [induction](induction-and-recurrences.md) on paths and trees.
- **Above:** [Graph algorithms](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md) implement these ideas. [Finite automata](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md) are labelled directed graphs. [Routing](../../08-networking/03-network-layer/routing-algorithms.md) is shortest paths on the network graph. Compilers use control-flow graphs, call graphs and interference graphs. [Garbage collection](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md) is reachability from roots. [Search and planning](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md) explores implicit state graphs; graph neural networks learn on them.
- **Siblings:** [Combinatorics](combinatorics.md) counts graph structures; [linear algebra](../04-algebra/linear-algebra.md) studies graphs through their adjacency matrices (spectral methods, PageRank).

## Common misconceptions

- **"Graph problems are all about the same difficulty."** Euler versus Hamiltonian, shortest versus longest path: tiny wording changes cross the P versus NP line.
- **"An adjacency matrix is the natural representation."** For sparse real-world graphs it wastes quadratic space and time.
- **"Trees and graphs are separate topics."** A tree is just a connected acyclic graph, and many graph algorithms work by building one.

## Go deeper

- Douglas West, *Introduction to Graph Theory* (2nd ed., 2001): the standard rigorous text.
- Reinhard Diestel, *Graph Theory* (5th ed., 2017): deeper theory, freely available online.
- Thomas Cormen, Charles Leiserson, Ronald Rivest and Clifford Stein, *Introduction to Algorithms* (4th ed., 2022): graph algorithms built on these definitions.
