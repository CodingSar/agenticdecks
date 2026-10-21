# Transport Layer

> **Layer:** [08 Networking](../README.md) › Transport Layer
> **Children:** [UDP and TCP](udp-and-tcp.md) · [Reliable Delivery](reliable-delivery.md) · [Congestion Control](congestion-control.md)

## What this area is about

The network layer delivers packets between hosts, unreliably. Applications want something different: to talk to a specific *process* on that host, and usually to send a stream of bytes that arrives complete, in order and without overwhelming either the receiver or the network in between. The transport layer bridges that gap, and it does so entirely in the end hosts, because the end-to-end argument says only the endpoints can guarantee delivery to the application.

Three jobs unify the children. *Multiplexing*: port numbers let many conversations share one host address. *Reliability*: sequence numbers, acknowledgements and retransmission turn a lossy packet service into an exact byte stream. *Congestion control*: each sender infers how much the shared network can carry and slows down when it sees signs of overload, so millions of independent senders share links without collapse.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [UDP and TCP](udp-and-tcp.md) | The two classic service models: bare datagrams with ports, or a reliable connection-oriented byte stream; plus QUIC | Network layer |
| [Reliable Delivery](reliable-delivery.md) | The mechanisms inside TCP: sequence numbers, acknowledgements, timeouts, sliding windows, flow control | UDP and TCP, latency |
| [Congestion Control](congestion-control.md) | The feedback loop that sets sending rate from loss and delay signals | Reliable delivery, queueing |

```
 app writes bytes
       |
   [send buffer] --window = min(cwnd, rwnd)--> segments --> network
       ^                                                        |
       +---- ACKs (cumulative, SACK) <--- receiver <-------------+
   cwnd adjusted by congestion control; rwnd by receiver flow control
```

Start with UDP and TCP to see what each promises. Reliable delivery explains how TCP keeps its promise over a lossy channel. Congestion control explains the second constraint on the sender's window, the one that protects the network rather than the receiver. Window size ends up as the minimum of two limits: what the receiver can buffer, and what the network appears able to carry.

## Connections to sibling areas

- **[Principles](../01-principles/README.md):** transport is the end-to-end argument in action; windows are sized by the bandwidth-delay product; congestion is the queueing cost of packet switching.
- **[Link Layer](../02-link-layer/README.md):** link-layer retransmission on wireless hides loss that TCP would otherwise misread as congestion.
- **[Network Layer](../03-network-layer/README.md):** IP delivers to a host; transport adds ports to reach a process. NATs and firewalls rewrite or filter transport headers, which ossifies protocols.
- **[Application Layer](../05-application-layer/README.md):** HTTP runs over TCP or QUIC; DNS mostly over UDP. Application performance is dominated by transport handshakes and slow start.

## Connections across layers

Transport protocols are [finite-state machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md) at each endpoint, implemented in the kernel behind [sockets and I/O models](../../07-operating-systems/06-io-and-devices/io-models.md). Congestion control is [feedback control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md) applied to a distributed system. Reliable delivery is the template for every retry protocol in [distributed systems](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md), including their duplicate-suppression and idempotency problems. [TLS](../../11-security-and-cryptography/02-cryptography/secure-protocols-and-tls.md) sits directly on top of TCP (and inside QUIC).

## Cross-cutting threads

- [The end-to-end argument](../../CROSS-CUTTING.md#the-end-to-end-argument): reliability lives in hosts, not routers.
- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): congestion windows grow and shrink in response to network signals.
- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): sliding windows keep many segments in flight.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): retransmission repairs loss.
- [State and time](../../CROSS-CUTTING.md#state-and-time): sequence numbers order bytes; timeouts guess at failure.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): reliability and order versus latency (head-of-line blocking).
