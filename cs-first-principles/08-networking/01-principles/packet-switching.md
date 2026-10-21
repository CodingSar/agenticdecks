# Packet Switching

> **Layer:** [08 Networking](../README.md) › [Principles](README.md)
> **Builds on:** [Layering and the End-to-End Principle](layering-and-the-end-to-end-principle.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Stacks and Queues](../../05-algorithms-and-data-structures/02-fundamental-data-structures/stacks-and-queues.md)
> **Enables:** [Latency, Bandwidth and Queueing](latency-bandwidth-and-queueing.md), [IP Addressing and Forwarding](../03-network-layer/ip-addressing-and-forwarding.md), [Congestion Control](../04-transport-layer/congestion-control.md)

## Essence

Packet switching breaks data into self-contained packets, each carrying its destination address, and lets every link be shared on demand by whoever has packets to send. The alternative, circuit switching, reserves a fixed slice of every link along a path for the whole conversation, as the telephone network did. Computer traffic is bursty: a host sends a lot, then nothing for seconds. Reserving capacity for silent conversations wastes most of it, while sharing on demand lets many bursty users fill a link that none could fill alone. The price is that packets sometimes arrive at a busy link at the same time, so they wait in queues or get dropped.

## Core tenets

1. **Bursty traffic makes reservation wasteful.** If each of 35 users is active 10% of the time at 1 Mbit/s, circuit switching on a 10 Mbit/s link supports only 10 of them. With packet switching, the probability that more than 10 of 35 are active at once is under 0.1%, so all 35 can share the link almost always without delay. This gain from sharing is called *statistical multiplexing*.

2. **Every packet carries what it needs to be forwarded.** A packet's header holds the destination address. Each switch looks it up in a forwarding table and sends the packet out the right port. No setup is needed and no per-conversation state is kept in the switch, so the network survives switch failures and new hosts can talk instantly.

3. **Store-and-forward adds per-hop delay.** A switch must usually receive a whole packet (to check it and read its header) before sending it on. For a packet of L bits on links of rate R across N links, the transmission component alone is N·L/R. Large packets amortise header overhead but increase this delay and the chance of a bit error spoiling the whole packet; this tension keeps packets in the range of a few hundred to a few thousand bytes (Ethernet's 1,500-byte limit, set around 1980, also reflected the cost of buffer memory then).

4. **Contention is resolved by queueing, then by dropping.** When packets for one output port arrive faster than it can transmit, they wait in a buffer. Buffers are finite, so sustained overload means loss. Loss is not a malfunction: it is the network's main signal that demand exceeds capacity, and Transmission Control Protocol (TCP) congestion control uses it as exactly that.

5. **Datagrams and virtual circuits are the two packet-switching styles.** In datagram networks (the Internet Protocol, IP) each packet is routed independently and may take a different path or arrive out of order. In virtual-circuit networks (X.25, Asynchronous Transfer Mode (ATM), and today's Multiprotocol Label Switching (MPLS) inside carrier networks) a path is set up first and packets carry a short label naming it. Virtual circuits make per-flow guarantees easier but put state back into switches.

6. **Best effort means no guarantees about delivery, order, delay or duplication.** IP promises only to try. This is a deliberate choice: the weakest useful service is the easiest to build over every kind of link and to keep running through failures. Stronger guarantees are added end to end where they are needed.

7. **Fairness is not automatic.** A packet network shares capacity among whoever sends most aggressively. Without cooperation, one heavy flow can starve the rest. Fair sharing comes either from end-host congestion control that backs off when it sees loss, or from schedulers in routers (fair queueing) that serve flows in turn.

## Key concepts

| Term | Meaning |
|---|---|
| Circuit switching | Reserve a fixed share of each link on a path for one conversation's lifetime |
| Packet switching | Send independent addressed packets; share links on demand |
| Statistical multiplexing | Sharing gain from the fact that bursty sources rarely peak together |
| Store-and-forward | Receive the whole packet at a switch before transmitting it onward |
| Datagram | A packet routed independently with no prior setup |
| Virtual circuit | A pre-established path identified by labels; switches keep per-circuit state |
| Best-effort service | Delivery attempted but not guaranteed in time, order or at all |
| Buffer | Memory at a switch port where packets wait for the link |
| Fair queueing | Scheduling that serves competing flows in rotation to share capacity equally |

## How it fits

- **Below:** uses [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) (binomial and Poisson arrivals) to justify statistical multiplexing, and the [queue](../../05-algorithms-and-data-structures/02-fundamental-data-structures/stacks-and-queues.md) as the switch's core data structure. Assumes the link layer can move one frame across one hop.
- **Above:** IP is a datagram packet-switching service ([IP addressing and forwarding](../03-network-layer/ip-addressing-and-forwarding.md)). Loss in queues is the input to [congestion control](../04-transport-layer/congestion-control.md). [Distributed systems](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md) inherit the model of messages that can be delayed, reordered or lost.
- **Siblings:** [layering and the end-to-end principle](layering-and-the-end-to-end-principle.md) explains why the core stays this simple; [latency, bandwidth and queueing](latency-bandwidth-and-queueing.md) quantifies its delays.

## Common misconceptions

- **"Packet loss means something is broken."** In a packet network, loss under load is normal and expected; it is the congestion signal.
- **"Packets of one connection follow one path."** In IP, nothing guarantees this; load balancers and route changes can split a flow across paths, though routers usually try to keep a flow together to avoid reordering.
- **"Circuit switching is obsolete."** Carrier networks still build label-switched paths, and optical networks reserve wavelengths. Guarantees are sometimes worth the waste.

## Go deeper

- P. Baran, *On Distributed Communications* (RAND, 1964): early argument for packet switching for survivability.
- L. Kleinrock, *Queueing Systems, Volume 1: Theory* (1975): the mathematics of waiting lines underlying packet networks.
- A. Demers, S. Keshav, S. Shenker, *Analysis and Simulation of a Fair Queueing Algorithm* (1989): how routers can enforce fair sharing.
