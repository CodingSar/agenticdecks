# Congestion Control

> **Layer:** [08 Networking](../README.md) › [Transport Layer](README.md)
> **Builds on:** [Reliable Delivery](reliable-delivery.md), [Latency, Bandwidth and Queueing](../01-principles/latency-bandwidth-and-queueing.md), [Feedback and Control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md), [Packet Switching](../01-principles/packet-switching.md)
> **Enables:** [HTTP and the Web](../05-application-layer/http-and-the-web.md), [Content Delivery and Caching](../05-application-layer/content-delivery-and-caching.md), [Scalability Patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md)

## Essence

When senders inject packets faster than a bottleneck link can drain them, queues grow, delay rises and packets are dropped; senders retransmit, adding more load, and useful throughput can collapse. The Internet has no central authority to assign rates, so each sender must infer the network's state from what it can observe (loss, delay, acknowledgement timing) and adjust its own rate. The classic scheme, Additive Increase Multiplicative Decrease (AIMD), probes for spare capacity by growing slowly and backs off sharply on loss. When all senders follow it, they converge to a fair and efficient share of the bottleneck.

## Core tenets

1. **Uncontrolled retransmission causes congestion collapse.** In October 1986, throughput between Lawrence Berkeley Laboratory and UC Berkeley, a few hundred metres apart, dropped from 32 kbit/s to 40 bit/s. Senders were retransmitting packets that were merely queued, so most link capacity carried duplicates. Jacobson's 1988 algorithms for TCP fixed this, and they are why the Internet scaled.

2. **The sender keeps a congestion window.** In addition to the receiver's window (rwnd), the sender maintains a congestion window (cwnd) and keeps at most min(cwnd, rwnd) bytes unacknowledged. Rate is roughly cwnd / RTT, where RTT is the Round-Trip Time. Congestion control is the rule for updating cwnd.

3. **Acknowledgements clock the sender.** In steady state, a new packet is sent only when an acknowledgement shows an old one has left the network. Because acknowledgements return at the bottleneck's rate, this "self-clocking" automatically paces the sender to the bottleneck without measuring it explicitly.

4. **AIMD converges to fairness.** In congestion avoidance, cwnd grows by about one segment per RTT (additive increase) and halves on loss (multiplicative decrease). Chiu and Jain (1989) showed that for two flows sharing a link, additive increase moves both rates equally while multiplicative decrease shrinks the larger one more, so repeated cycles drive them toward equal shares. Other combinations (such as multiplicative increase with additive decrease) do not converge.

5. **Slow start finds capacity quickly.** A new connection does not know the path's capacity. It starts with a small cwnd (commonly 10 segments today) and doubles it every RTT until it sees loss or reaches a threshold, then switches to additive increase. Despite the name, this is exponential growth; it reaches a 10,000-segment window in about ten RTTs.

6. **Loss is an imperfect signal.** Classic TCP (Reno, and CUBIC, the Linux default since 2006) treats packet loss as congestion. That works when buffers are modest and loss is rare otherwise. It fails on wireless links where loss comes from noise, and with very large buffers, where loss only occurs after queues have added large delays. Explicit Congestion Notification (ECN) lets routers mark packets instead of dropping them.

7. **Delay- and model-based controllers aim to avoid queues.** Rising RTT means a queue is building, before any loss. Bottleneck Bandwidth and RTT (BBR, Google, 2016) estimates the bottleneck rate and minimum RTT and paces packets at that rate, targeting a full pipe with an empty queue. The challenge is coexistence: delay-sensitive flows back off earlier and can lose share to loss-based flows.

8. **Throughput depends on RTT and loss rate.** For Reno-style AIMD, steady-state throughput is roughly (MSS / RTT) × 1.22 / √p, where MSS is the Maximum Segment Size and p the loss rate (Mathis et al., 1997). Flows with longer RTT get less throughput at the same loss rate, and very high-speed long-distance paths need extremely low loss rates, which motivated more aggressive growth curves such as CUBIC.

9. **Congestion control is a social contract.** Nothing in IP enforces it. A sender that ignores it grabs more bandwidth. The Internet works because almost all traffic uses compatible algorithms implemented in a few operating systems and browsers. Router-side fair queueing and active queue management add some enforcement.

## Key concepts

| Term | Meaning |
|---|---|
| Congestion collapse | Throughput falls as offered load rises, because capacity is wasted on duplicates or dropped work |
| cwnd | Congestion window: sender's estimate of what the network can absorb |
| AIMD | Additive Increase Multiplicative Decrease |
| Slow start | Exponential growth of cwnd at connection start |
| Self-clocking | ACK arrivals pacing new transmissions |
| ECN | Router marks packets to signal congestion without dropping |
| CUBIC | Loss-based algorithm with cubic window growth; default in Linux |
| BBR | Model-based algorithm estimating bottleneck bandwidth and RTT |
| TCP-friendly | Achieving no more throughput than standard TCP under the same conditions |

## How it fits

- **Below:** it is a distributed [feedback control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md) loop with delayed, noisy measurements; queue behaviour comes from [latency, bandwidth and queueing](../01-principles/latency-bandwidth-and-queueing.md); it rides on the acknowledgement machinery of [reliable delivery](reliable-delivery.md).
- **Above:** slow start dominates the load time of short [HTTP](../05-application-layer/http-and-the-web.md) transfers, which is why connection reuse and [CDNs](../05-application-layer/content-delivery-and-caching.md) (shorter RTT) help so much. The same AIMD and backoff ideas reappear in load shedding and retry policies in [scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md).
- **Siblings:** [reliable delivery](reliable-delivery.md) protects the receiver with rwnd; congestion control protects the network with cwnd; [UDP](udp-and-tcp.md) has neither, so UDP-based protocols (QUIC, media) must implement their own.

## Common misconceptions

- **"Routers do congestion control."** Routers drop or mark packets; the control loop that adjusts rates runs in end hosts.
- **"Slow start is slow."** It grows exponentially; "slow" referred to starting small rather than blasting the full receiver window.
- **"Packet loss always means congestion."** On wireless and some other links it can mean noise; treating it as congestion wastes capacity.

## Go deeper

- V. Jacobson, *Congestion Avoidance and Control* (SIGCOMM 1988): the paper that saved the Internet.
- D.-M. Chiu, R. Jain, *Analysis of the Increase and Decrease Algorithms for Congestion Avoidance in Computer Networks* (1989): why AIMD is fair.
- N. Cardwell et al., *BBR: Congestion-Based Congestion Control* (ACM Queue, 2016): the model-based alternative.
