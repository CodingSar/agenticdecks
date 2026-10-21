# Routing Algorithms

> **Layer:** [08 Networking](../README.md) › [Network Layer](README.md)
> **Builds on:** [IP Addressing and Forwarding](ip-addressing-and-forwarding.md), [Shortest Paths](../../05-algorithms-and-data-structures/05-graph-algorithms/shortest-paths.md), [Graph Theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md), [Dynamic Programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md)
> **Enables:** [Internet Routing and BGP](internet-routing-and-bgp.md), [System Models and Failures](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md)

## Essence

A routing algorithm fills every router's forwarding table so that hop-by-hop decisions deliver packets along good paths. The network is a graph: routers are nodes, links are edges weighted by a cost such as delay or inverse bandwidth. Within one organisation, the goal is shortest paths, and two families compute them in a distributed way. In *link-state* routing, every router learns the whole graph and runs Dijkstra's algorithm itself. In *distance-vector* routing, each router knows only its neighbours' distance estimates and runs a distributed Bellman-Ford. The hard part is not the algorithm but keeping it correct while links fail and routers disagree about the current graph.

## Core tenets

1. **Routing is a distributed shortest-path problem with changing inputs.** Each router must compute the next hop toward every destination prefix. Paths must be loop-free and adapt to failures within seconds. No router has authority over the others, and messages about changes travel through the same network that is changing.

2. **Link-state: flood the graph, compute locally.** Each router floods a Link-State Advertisement (LSA) describing its own links to every other router. Once all have the same map, each runs Dijkstra's algorithm, O(E + V log V) with a heap, from itself. Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS) work this way. Consistency follows from everyone having the same data and the same deterministic algorithm.

3. **Distance-vector: share estimates with neighbours only.** Each router keeps a table of its best known distance to every destination and periodically sends it to neighbours. On receiving a neighbour's vector it applies the Bellman-Ford update D(x) = min over neighbours v of [c(self, v) + D_v(x)]. This is dynamic programming over paths, run asynchronously. It converges to correct shortest paths when the graph stops changing. The Routing Information Protocol (RIP) is the classic example.

4. **Bad news travels slowly in distance-vector: count to infinity.** If A–B–C is a chain and the link B–C fails, B may hear from A that A can reach C in 2 hops (via B itself) and believe it, setting its own cost to 3; A then updates to 4; and so on. The two routers bounce increasing estimates until they reach a configured "infinity" (16 in RIP). Split horizon and poison reverse fix two-node loops but not longer ones, which is why distance-vector protocols limit network diameter.

5. **Link-state trades memory and flooding for fast, consistent convergence.** Every router stores the whole topology and recomputes on any change, which costs more memory and Central Processing Unit (CPU) time, but convergence takes roughly the flooding time plus one Dijkstra run. Large link-state networks are divided into areas so that each router holds the detailed map of its own area and summaries of others: hierarchy again.

6. **Transient inconsistency causes loops and black holes.** Between a failure and full convergence, some routers use the old map and some the new. A packet can loop between two routers that disagree. The Internet Protocol (IP) Time To Live (TTL) bounds the damage. Fast-reroute techniques precompute backup next hops so traffic moves within milliseconds while the protocol reconverges.

7. **Link cost choice encodes the operator's goal.** Hop count, delay, inverse capacity and administrative weights all give different "shortest" paths. Making costs depend on current load seems attractive but causes oscillation: traffic moves to the lightly loaded path, which then becomes heavy, so traffic moves back. The ARPANET saw this in the 1980s. Stable routing uses mostly static costs and leaves load response to traffic engineering and congestion control.

8. **Centralised computation is an alternative.** Software-Defined Networking (SDN) moves route computation to a logically central controller that sees the whole network and installs forwarding entries in switches. It simplifies policy and traffic engineering inside data centres and wide-area backbones, at the cost of making the controller a critical, replicated service ([data center networks and SDN](data-center-networks-and-sdn.md)).

## Key concepts

| Term | Meaning |
|---|---|
| Control plane | Protocols and computation that decide routes |
| Data plane | Per-packet forwarding using the computed table |
| Link-state | Each router learns full topology and computes shortest paths locally |
| Distance-vector | Routers exchange distance estimates with neighbours (Bellman-Ford) |
| Convergence | Reaching a consistent, correct set of routes after a change |
| Count to infinity | Slow divergence of distance estimates after a failure in distance-vector |
| Split horizon / poison reverse | Not advertising (or advertising infinite cost for) a route back to the neighbour it came from |
| Area | Partition of a link-state domain to bound topology size |
| SDN | Route computation in a central controller rather than in each router |

## How it fits

- **Below:** routing is [graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md) plus [shortest-path algorithms](../../05-algorithms-and-data-structures/05-graph-algorithms/shortest-paths.md); distance-vector is [dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md) executed by many processors asynchronously. It produces the table used by [IP forwarding](ip-addressing-and-forwarding.md).
- **Above:** routing protocols are among the first widely deployed distributed algorithms; their convergence problems foreshadow [system models and failures](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md). SDN controllers are replicated with [consensus](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md).
- **Siblings:** these algorithms optimise one shared metric inside one organisation; [BGP](internet-routing-and-bgp.md) handles many organisations with private policies, where "shortest" is not the goal; [data center networks](data-center-networks-and-sdn.md) replace per-router computation with a central controller and spread traffic over many equal-cost paths.

## Common misconceptions

- **"Routers find the fastest path for each packet."** They compute paths from configured costs in the background; per-packet forwarding is a table lookup that does not consider current queue lengths.
- **"Dijkstra and Bellman-Ford give different answers."** On the same static graph with non-negative weights both find shortest paths; they differ in what each node must know and how they behave during change.
- **"Routing loops are a bug."** Transient loops are an expected consequence of distributed, asynchronous updates; protocols bound them rather than eliminate them.

## Go deeper

- E. W. Dijkstra, *A Note on Two Problems in Connexion with Graphs* (1959): the shortest-path algorithm at the heart of link-state routing.
- J. M. McQuillan, I. Richer, E. C. Rosen, *The New Routing Algorithm for the ARPANET* (1980): the first link-state routing in practice.
- R. Perlman, *Interconnections* (2nd ed., 1999): IS-IS, distance-vector pathologies, and design trade-offs from a protocol designer.
