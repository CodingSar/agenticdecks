# Reliable Delivery

> **Layer:** [08 Networking](../README.md) › [Transport Layer](README.md)
> **Builds on:** [UDP and TCP](udp-and-tcp.md), [Latency, Bandwidth and Queueing](../01-principles/latency-bandwidth-and-queueing.md), [Encoding and Framing](../02-link-layer/encoding-and-framing.md), [Correctness and Invariants](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md)
> **Enables:** [Congestion Control](congestion-control.md), [System Models and Failures](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md), [Replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md)

## Essence

Reliable delivery turns a channel that can lose, corrupt, duplicate and reorder packets into one that delivers every byte exactly once and in order. The mechanism has four parts: checksums to detect corruption, sequence numbers to detect gaps, duplicates and reordering, acknowledgements to tell the sender what arrived, and timers to retransmit what was not acknowledged. Doing this one packet at a time wastes most of a long path, so practical protocols keep a *window* of unacknowledged packets in flight. The window also gives the receiver a way to say how much buffer it has left (flow control).

## Core tenets

1. **Detection plus retransmission gives reliability over any lossy channel.** The receiver discards corrupted packets (checksum) and acknowledges good ones. The sender retransmits anything not acknowledged within a timeout. As long as each attempt has some nonzero chance of success, every packet eventually arrives. This is Automatic Repeat reQuest (ARQ).

2. **Sequence numbers make retransmission safe.** If an acknowledgement is lost, the sender resends a packet the receiver already has. Without numbering, the receiver would deliver it twice. Sequence numbers let the receiver discard duplicates and put reordered packets back in order. The Transmission Control Protocol (TCP) numbers bytes, not packets, so retransmissions can be re-segmented.

3. **Stop-and-wait wastes the pipe; sliding windows fill it.** Sending one packet per Round-Trip Time (RTT) on a 1 Gbit/s path with 50 ms RTT and 1,500-byte packets uses 240 kbit/s, 0.024% of capacity. A sliding window lets the sender have up to W bytes unacknowledged. Throughput is about W / RTT, so filling the path needs W ≥ bandwidth × RTT (the bandwidth-delay product).

4. **Go-Back-N and Selective Repeat differ in what is resent.** With cumulative acknowledgements ("I have everything up to byte n"), a single loss can force resending the whole window after it (Go-Back-N). Selective Acknowledgements (SACK) report which later blocks arrived, so the sender resends only the gaps. Selective Repeat needs receiver buffering for out-of-order data and a sequence space at least twice the window to avoid ambiguity.

5. **Timeout choice is an estimation problem.** Too short and the sender retransmits packets that were only delayed, adding load exactly when the network is busy. Too long and recovery stalls. TCP keeps a smoothed RTT (SRTT) and its mean deviation (RTTVAR) and sets the Retransmission Timeout (RTO) ≈ SRTT + 4 × RTTVAR (Jacobson, 1988), doubling it after each timeout. It also ignores RTT samples from retransmitted segments, whose acknowledgements are ambiguous (Karn's algorithm).

6. **Duplicate acknowledgements detect loss faster than timers.** When the receiver gets segments after a gap, it repeats its last cumulative acknowledgement. Three duplicate acknowledgements (ACKs) signal that one segment is probably lost while later ones arrive, so the sender retransmits immediately ("fast retransmit") rather than waiting a full RTO.

7. **Flow control protects the receiver.** Each acknowledgement carries the receiver's advertised window (rwnd): how much free buffer it has. The sender never has more than rwnd unacknowledged bytes outstanding. A slow application reading slowly shrinks rwnd to zero and pauses the sender, so a fast sender cannot overrun a slow receiver.

8. **Exactly-once delivery is achievable only within one connection's lifetime.** TCP guarantees bytes are delivered once and in order while the connection lives. If the connection breaks, the sender cannot know which of its last bytes the application processed. Higher-level protocols that retry across connections must make operations idempotent or deduplicate with request IDs; the end-to-end argument again.

## Key concepts

| Term | Meaning |
|---|---|
| ARQ | Automatic Repeat reQuest: detect loss, retransmit |
| Sequence number | Position of data in the stream, used to order and deduplicate |
| Cumulative ACK | Acknowledges all data up to a point |
| SACK | Selective Acknowledgement: reports out-of-order blocks received |
| Sliding window | Bound on unacknowledged data in flight |
| Go-Back-N / Selective Repeat | Resend everything after a loss / resend only lost pieces |
| RTO | Retransmission Timeout, adapted from measured RTT |
| Fast retransmit | Retransmit after three duplicate ACKs, before RTO expires |
| rwnd | Receiver's advertised window for flow control |
| Idempotent | Applying an operation twice has the same effect as once |

## How it fits

- **Below:** sits on the unreliable service of [UDP and TCP's](udp-and-tcp.md) underlying Internet Protocol (IP); checksums extend the [link-layer error detection](../02-link-layer/encoding-and-framing.md) end to end; window sizing comes from [latency and bandwidth](../01-principles/latency-bandwidth-and-queueing.md). Correctness is argued with [invariants](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md) such as "everything below the cumulative ACK has been delivered in order".
- **Above:** retry, deduplication and idempotency reappear in every [distributed system](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md); log shipping in [replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md) uses the same sequence-and-acknowledge pattern.
- **Siblings:** [congestion control](congestion-control.md) adds a second window (cwnd) that protects the network; the effective window is min(cwnd, rwnd).

## Common misconceptions

- **"Reliable means the message will get through."** It means the sender will eventually know whether it was acknowledged; if the path is down, TCP gives up and reports an error.
- **"Exactly-once delivery is a transport guarantee."** It is bounded by the connection; across failures, applications must handle duplicates.
- **"Flow control and congestion control are the same thing."** Flow control protects the receiver's buffer; congestion control protects the shared network.

## Go deeper

- V. Jacobson, *Congestion Avoidance and Control* (SIGCOMM 1988): RTT estimation and retransmission timer design.
- P. Karn, C. Partridge, *Improving Round-Trip Time Estimates in Reliable Transport Protocols* (1987): Karn's algorithm.
- J. F. Kurose, K. W. Ross, *Computer Networking: A Top-Down Approach*: builds reliable data transfer step by step from a perfect channel to a lossy one.
