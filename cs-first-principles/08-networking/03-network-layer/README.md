# Network Layer

> **Layer:** [08 Networking](../README.md) › Network Layer
> **Children:** [IP Addressing and Forwarding](ip-addressing-and-forwarding.md) · [Routing Algorithms](routing-algorithms.md) · [Internet Routing and BGP](internet-routing-and-bgp.md)

## What this area is about

The network layer delivers a packet from any host to any other host across many independent links and networks. It answers two separate questions. *Forwarding*: when a packet arrives at a router, which output port should it leave by? That decision must take nanoseconds and uses only a local table. *Routing*: how are those tables filled, so that the local decisions add up to a sensible global path? That computation runs in the background over seconds to minutes and requires routers to exchange information.

The unifying idea is the Internet Protocol (IP): one global address space with hierarchical, aggregatable addresses, and one best-effort packet format that every network agrees to carry. Hierarchy is what lets roughly a million routing table entries describe billions of hosts. Routing protocols then come in two kinds, because the Internet is two kinds of problem: inside one organisation, find the shortest path; between organisations, respect business policy.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [IP Addressing and Forwarding](ip-addressing-and-forwarding.md) | The data plane: address structure, the packet format, longest-prefix-match forwarding, Network Address Translation (NAT), fragmentation | Link layer, principles |
| [Routing Algorithms](routing-algorithms.md) | The control plane within one domain: link-state and distance-vector shortest paths | Forwarding, graph algorithms |
| [Internet Routing and BGP](internet-routing-and-bgp.md) | The control plane between domains: policy-based path-vector routing that glues ~75,000 networks together | Routing algorithms |

```
         control plane (slow, global)       data plane (fast, local)
  routing protocol messages --> RIB --> FIB --> per-packet lookup
  (OSPF, IS-IS inside; BGP between)              (longest prefix match)
```

Read addressing first: it defines what routing must produce, a table mapping address prefixes to next hops. Routing algorithms show how to compute that table from a graph when everyone cooperates. Border Gateway Protocol (BGP) shows what changes when the graph is owned by competing businesses who will not reveal their internals and choose routes by money, not distance.

## Connections to sibling areas

- **[Principles](../01-principles/README.md):** IP is the narrow waist and the purest embodiment of best-effort datagram service; routers are store-and-forward switches with queues.
- **[Link Layer](../02-link-layer/README.md):** every hop is a link-layer frame; Address Resolution Protocol (ARP) maps the next-hop IP address to a link address. Switches handle forwarding within a Local Area Network (LAN); routers between them.
- **[Transport Layer](../04-transport-layer/README.md):** the network layer delivers to a host; transport demultiplexes to a process using ports. Routers usually ignore transport headers, except Network Address Translators (NATs) and firewalls that rewrite them.
- **[Application Layer](../05-application-layer/README.md):** Domain Name System (DNS) maps names to IP addresses; content delivery networks use routing tricks (anycast) to send users to nearby servers.

## Connections across layers

Routing is [graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md) and [shortest paths](../../05-algorithms-and-data-structures/05-graph-algorithms/shortest-paths.md) made distributed; forwarding uses [tries](../../05-algorithms-and-data-structures/06-string-algorithms/tries-and-suffix-structures.md) and specialised hardware memories. Routing protocols must converge despite failures and inconsistent views, a gentle introduction to the problems of [distributed systems](../../10-distributed-and-parallel-computing/README.md). BGP's reliance on trust between operators makes it a target for [network attacks](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md).

## Cross-cutting threads

- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): addresses name locations; NAT and anycast decouple names from machines.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): hierarchical addressing hides the internal structure of each network behind one prefix.
- [Interface vs implementation](../../CROSS-CUTTING.md#interface-vs-implementation): the separation of control plane (what routes exist) from data plane (how packets move).
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): routing recomputes paths around failed links.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): BGP accepts neighbours' claims, and route hijacks exploit it.
