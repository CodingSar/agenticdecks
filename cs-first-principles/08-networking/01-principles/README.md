# Principles

> **Layer:** [08 Networking](../README.md) › Principles
> **Children:** [Layering and the End-to-End Principle](layering-and-the-end-to-end-principle.md) · [Packet Switching](packet-switching.md) · [Latency, Bandwidth and Queueing](latency-bandwidth-and-queueing.md)

## What this area is about

Before any specific protocol, three ideas decide the shape of every network built since the 1970s. First, *where* should a function live: in the network or at its edges? Second, *how* should a shared link be divided among many conversations: by reserving capacity in advance or by sending self-describing packets on demand? Third, *what* limits how fast data gets from one end to the other: distance, link rate, or waiting in line?

The unifying idea is that a network is a shared resource with no central controller, and every design choice trades simplicity in the core for work at the edges. The Internet chose a dumb, best-effort, packet-switched core with smart endpoints. That choice explains why IP drops packets without apology, why TCP lives in end hosts, and why queueing delay, not wire speed, dominates latency on a busy path.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Layering and the End-to-End Principle](layering-and-the-end-to-end-principle.md) | Decides how responsibilities are split across layers and between core and edge | Abstraction from lower layers |
| [Packet Switching](packet-switching.md) | Decides how capacity is shared: statistical multiplexing of independent packets | Layering |
| [Latency, Bandwidth and Queueing](latency-bandwidth-and-queueing.md) | Quantifies the cost: propagation, transmission and queueing delay; the bandwidth-delay product | Packet switching, probability |

Read them in order. Layering says the network core should do little. Packet switching is the minimal thing it does: forward independent packets, store them briefly when links are busy, drop them when buffers fill. Queueing theory then explains the price of that choice: delay that grows sharply as utilisation approaches one, and loss when buffers overflow. Every later layer either lives with these costs (IP) or repairs them end to end (TCP).

## Connections to sibling areas

- **[Link Layer](../02-link-layer/README.md):** the link layer is the first place packet switching meets a physical medium; media access protocols are statistical multiplexing on a shared wire or radio channel.
- **[Network Layer](../03-network-layer/README.md):** IP is the end-to-end principle made concrete, a deliberately minimal best-effort service, and routers are the store-and-forward switches of packet switching.
- **[Transport Layer](../04-transport-layer/README.md):** reliability and congestion control are the end-to-end functions the core declined to provide; window sizes are set by the bandwidth-delay product.
- **[Application Layer](../05-application-layer/README.md):** latency, not bandwidth, limits most web page loads, which is why caching and connection reuse matter more than faster links.

## Connections across layers

These principles take [abstraction](../../12-software-engineering/01-design/abstraction-and-interfaces.md) and [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) from below and the physical speed limits of [signals](../../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md). They give [distributed systems](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md) the asynchronous, lossy message model, and give [security](../../11-security-and-cryptography/01-security-principles/security-design-principles.md) the argument that protection must be end to end.

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): each protocol layer uses only the service of the layer beneath.
- [The end-to-end argument](../../CROSS-CUTTING.md#the-end-to-end-argument): originated here, in the design of the Internet.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): circuit vs packet switching trades guaranteed service for efficiency; buffer size trades loss for delay.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): propagation delay is bounded by the speed of light.
