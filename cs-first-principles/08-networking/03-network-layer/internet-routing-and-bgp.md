# Internet Routing and BGP

> **Layer:** [08 Networking](../README.md) › [Network Layer](README.md)
> **Builds on:** [Routing Algorithms](routing-algorithms.md), [IP Addressing and Forwarding](ip-addressing-and-forwarding.md), [Graph Theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md)
> **Enables:** [Content Delivery and Caching](../05-application-layer/content-delivery-and-caching.md), [Network Attacks and Defenses](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md), [Cloud Computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md)

## Essence

The Internet is not one network but about 75,000 independently operated networks called Autonomous Systems (ASes), circa mid-2020s. Inside each, operators run whatever routing they like. Between them, a single protocol, the Border Gateway Protocol (BGP), decides how traffic crosses from one AS to another. BGP is not a shortest-path protocol. Each AS chooses routes by *policy*, usually money: prefer routes through customers who pay you, then through peers who exchange traffic for free, and only then through providers you pay. ASes advertise whole paths, which lets each one detect loops and apply its own rules without revealing its internal network or its contracts.

## Core tenets

1. **Inter-domain routing is about policy, not distance.** Each AS is a business with contracts. An AS will not carry traffic between two of its providers for free, even if that would be the shortest path on the graph. So the global routing system must let each AS express private preferences and still produce working paths. No common metric exists across ASes.

2. **BGP is a path-vector protocol.** Each route advertisement carries a destination prefix and the full list of ASes it traverses (the AS path). A router rejects any route whose path already contains its own AS number, which prevents loops without the count-to-infinity problem of distance-vector routing. The AS path also lets policies inspect who the traffic would pass through.

3. **Business relationships shape what is advertised.** In the common Gao-Rexford model, ASes have customer, provider and peer links. An AS exports its customers' routes to everyone (it earns money carrying them), but exports routes learned from peers or providers only to its customers. The result is "valley-free" paths: traffic climbs up provider links, crosses at most one peer link, and descends to customers. When all ASes follow these rules and no AS is, through a chain of contracts, its own provider, BGP is guaranteed to converge.

4. **Route selection is a ranked list of rules.** A BGP router picks among candidate routes by local preference (set by policy, typically customer > peer > provider), then shortest AS path, then several tie-breakers. AS path length counts ASes, not hops or delay, so BGP paths are often longer than the best possible path in latency.

5. **BGP has two halves: external and internal.** External BGP (eBGP) sessions run between neighbouring ASes. Internal BGP (iBGP) distributes those external routes to all border routers inside one AS, while an interior protocol such as Open Shortest Path First (OSPF) or Intermediate System to Intermediate System (IS-IS) (see [routing algorithms](routing-algorithms.md)) computes paths to reach those borders. The two layers of routing mirror the two levels of address hierarchy.

6. **Arbitrary policies can make BGP oscillate forever.** Policy preferences are not guaranteed to have a stable solution. Griffin and Wilfong showed (1999) that deciding whether a BGP configuration has a stable outcome is NP-complete, and some configurations ("dispute wheels") oscillate indefinitely. In practice, economic incentives push ASes toward Gao-Rexford-like policies that do converge.

7. **BGP trusts what neighbours say.** By default a router accepts an AS's claim to originate a prefix. A misconfigured or malicious AS can announce someone else's prefix, or a more specific one, and attract their traffic: a route hijack or leak. Pakistan Telecom's 2008 announcement of a YouTube prefix took YouTube offline globally for about two hours. Resource Public Key Infrastructure (RPKI) lets prefix holders sign which AS may originate them; validating the full path remains largely undeployed.

8. **Convergence is slow and the table is big.** A global BGP change can take tens of seconds to minutes to propagate, and routers damp rapidly flapping routes to protect themselves. A full table holds around a million IPv4 prefixes plus a growing IPv6 table (circa mid-2020s), stressing router memory. Address aggregation is the main tool to keep it bounded.

9. **Anycast uses BGP for load distribution.** Announcing the same prefix from many locations makes each user's traffic go to the "closest" site in BGP terms. Root Domain Name System (DNS) servers and content delivery networks rely on this to serve users from nearby and to absorb attacks.

## Key concepts

| Term | Meaning |
|---|---|
| AS | Autonomous System: network under one administrative policy, identified by an AS number |
| BGP | Border Gateway Protocol: path-vector protocol between ASes |
| AS path | List of ASes a route advertisement has traversed |
| eBGP / iBGP | BGP between ASes / BGP distributing external routes inside one AS |
| Local preference | Policy-assigned priority that dominates route choice |
| Customer / provider / peer | Paid transit downstream / paid transit upstream / settlement-free exchange |
| Valley-free path | Path consistent with economic export rules |
| Route hijack | Announcing a prefix one does not legitimately hold |
| RPKI | Signed attestations of which AS may originate a prefix |
| IXP | Internet Exchange Point: facility where many ASes interconnect |

## How it fits

- **Below:** uses [IP prefixes](ip-addressing-and-forwarding.md) as the unit of routing and relies on an interior [routing algorithm](routing-algorithms.md) within each AS. The AS-level Internet is a [graph](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md) with labelled edge types.
- **Above:** anycast underpins [content delivery](../05-application-layer/content-delivery-and-caching.md) and DNS; [cloud providers](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) run their own global backbones connected by BGP. Hijacks and route leaks are major [network attacks](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md).
- **Siblings:** [routing algorithms](routing-algorithms.md) optimise a shared metric inside one trust domain; BGP coordinates mutually distrustful parties with private objectives.

## Common misconceptions

- **"Internet paths are shortest paths."** They are policy-compliant paths; studies routinely find many paths substantially longer than the best available.
- **"BGP is a security protocol."** Classic BGP has no authentication of route origin or path; RPKI adds origin validation only.
- **"The Internet has a central routing authority."** Address blocks are allocated centrally by registries, but every routing decision is made by individual ASes.

## Go deeper

- Y. Rekhter, T. Li, S. Hares, *RFC 4271: A Border Gateway Protocol 4 (BGP-4)* (2006): the protocol specification.
- L. Gao, J. Rexford, *Stable Internet Routing Without Global Coordination* (2001): why commercial policies converge.
- T. G. Griffin, F. B. Shepherd, G. Wilfong, *The Stable Paths Problem and Interdomain Routing* (2002): the theory of BGP convergence and divergence.
