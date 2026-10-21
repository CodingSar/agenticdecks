# Latency, Bandwidth and Queueing

> **Layer:** [08 Networking](../README.md) › [Principles](README.md)
> **Builds on:** [Packet Switching](packet-switching.md), [Random Variables and Distributions](../../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md), [Channel Capacity and Error Correction](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md), [Electromagnetism and Charge](../../00-engineering-foundations/01-physics-of-computation/electromagnetism-and-charge.md)
> **Enables:** [Reliable Delivery](../04-transport-layer/reliable-delivery.md), [Congestion Control](../04-transport-layer/congestion-control.md), [Content Delivery and Caching](../05-application-layer/content-delivery-and-caching.md), [Scalability Patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md)

## Essence

Two numbers describe a network path: *latency*, how long one bit takes to get from sender to receiver, and *bandwidth*, how many bits per second the path can carry. They are independent: a truck full of disks has huge bandwidth and terrible latency. End-to-end delay is the sum of four parts at every hop: processing, queueing, transmission and propagation. Propagation is fixed by distance and the speed of light, transmission by link rate, and queueing by how busy the link is. Queueing is the part that varies, and it grows without bound as a link's utilisation approaches 100%.

## Core tenets

1. **Delay at each hop has four components.** *Processing* (reading the header, looking up the route: nanoseconds to microseconds). *Queueing* (waiting behind other packets: zero to hundreds of milliseconds). *Transmission* (pushing L bits onto a link of rate R takes L/R: a 1,500-byte packet on 1 Gbit/s takes 12 µs). *Propagation* (distance divided by signal speed, about 2×10^8 m/s in fibre, so ~5 µs per km).

2. **The speed of light is a hard floor.** New York to London is ~5,600 km, so one-way fibre propagation is at least ~28 ms and a round trip at least ~56 ms; real paths are longer. No protocol or hardware upgrade removes this. It is why latency-sensitive services put servers close to users and why protocols try to save round trips.

3. **Bandwidth-delay product sets how much data must be in flight.** A path with rate R and Round-Trip Time (RTT) holds R × RTT bits "in the pipe". A 1 Gbit/s path with 100 ms RTT holds 100 Mbit (12.5 MB). A sender that waits for an acknowledgement after each small window can never fill such a pipe, so transport windows must be at least this large.

4. **For small transfers, latency dominates; for large ones, bandwidth does.** Time to deliver S bytes is roughly RTT × (round trips needed) + S/R. A 20 KB web object on a 1 Gbit/s link with 50 ms RTT spends ~0.16 ms transmitting and many tens of milliseconds waiting for handshakes. This is why upgrading bandwidth beyond a few tens of Mbit/s barely speeds up web browsing.

5. **Queueing delay explodes near full utilisation.** In the simplest queueing model (M/M/1: random Poisson arrivals, random service times, one server) the mean time in system is 1/(μ − λ), where λ is arrival rate and μ is service rate. Writing utilisation ρ = λ/μ, delay scales as 1/(1 − ρ): at 50% load it is 2× the service time, at 90% it is 10×, at 99% it is 100×. Variability, not average load, causes the waiting.

6. **Little's Law relates occupancy, rate and delay for any stable system.** L = λW: the average number in the system equals arrival rate times average time spent. It holds regardless of distributions. It lets you infer queueing delay from queue length, or required buffer space from rate and delay.

7. **Throughput is set by the bottleneck link.** End-to-end throughput is at most the minimum rate along the path, and queues build up just before that bottleneck. Adding capacity anywhere else changes nothing.

8. **Big buffers trade loss for delay, and too much buffering hurts.** A router with more buffer drops fewer packets but lets queues grow longer. When buffers are far larger than the bandwidth-delay product, loss-based congestion control fills them, adding seconds of delay for everyone: "bufferbloat". Active queue management (for example CoDel) drops or marks packets early to keep queues short.

9. **Tail latency matters more than the mean.** A user-facing request that fans out to 100 servers waits for the slowest. If each server is slow 1% of the time, about 63% of such requests hit at least one slow server. Variability compounds across fan-out, which is why large systems track 99th-percentile latency.

## Key concepts

| Term | Meaning |
|---|---|
| Latency | Time for a bit to travel from sender to receiver |
| Bandwidth (rate) | Bits per second a link or path can carry |
| Throughput | Bits per second actually delivered end to end |
| RTT | Round-trip time: time for a message and its reply |
| Bandwidth-delay product | Rate × RTT: bits that must be in flight to keep a path full |
| Utilisation ρ | Arrival rate divided by service rate |
| Little's Law | L = λW, valid for any stable queueing system |
| Bottleneck | The slowest link on a path; it caps throughput |
| Bufferbloat | Excess delay from oversized, persistently full buffers |
| Tail latency | High-percentile delay (p99, p99.9), dominated by rare slow events |

## How it fits

- **Below:** signal speed in a medium comes from [electromagnetism](../../00-engineering-foundations/01-physics-of-computation/electromagnetism-and-charge.md); maximum link rate is bounded by [channel capacity](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md); queueing models use [random variables and distributions](../../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md), especially exponential and Poisson.
- **Above:** [reliable delivery](../04-transport-layer/reliable-delivery.md) sizes windows by the bandwidth-delay product; [congestion control](../04-transport-layer/congestion-control.md) estimates bottleneck rate and RTT; [content delivery](../05-application-layer/content-delivery-and-caching.md) attacks propagation delay by moving data closer; [scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md) fight tail latency with hedged requests.
- **Siblings:** [packet switching](packet-switching.md) creates the queues analysed here; [layering](layering-and-the-end-to-end-principle.md) adds per-layer header and processing overhead.

## Common misconceptions

- **"More bandwidth makes everything faster."** Interactive workloads are latency-bound. Doubling bandwidth does nothing for a request dominated by round trips.
- **"A link at 80% utilisation has 20% headroom."** Queueing delay is already 5× the service time in the M/M/1 model; bursts will cause loss well before 100%.
- **"Larger router buffers always help."** Beyond roughly the bandwidth-delay product they mostly add delay.

## Go deeper

- L. Kleinrock, *Queueing Systems, Volume 1: Theory* (1975): M/M/1 and its relatives from first principles.
- J. D. C. Little, *A Proof for the Queuing Formula: L = λW* (1961): the general law.
- J. Dean, L. A. Barroso, *The Tail at Scale* (Communications of the ACM, 2013): why p99 dominates large systems.
- K. Nichols, V. Jacobson, *Controlling Queue Delay* (ACM Queue, 2012): CoDel and the bufferbloat problem.
