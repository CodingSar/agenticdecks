# Scalability Patterns

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Large-scale systems](README.md)
> **Builds on:** [Partitioning](../04-distributed-data/partitioning.md), [Replication](../03-consensus-and-replication/replication.md), [Latency, bandwidth and queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md), [Locality and caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md)
> **Enables:** [Software architecture](../../12-software-engineering/01-design/software-architecture.md), [Reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md), [Observability](../../12-software-engineering/04-operations/observability.md)

## Essence

A system scales if adding resources adds proportional capacity without a redesign. Request-serving systems reach that goal with a small set of recurring patterns: keep servers **stateless** so any one can handle any request, **cache** reads close to users, **partition** state so writes spread out, move slow work onto **queues** processed asynchronously, and protect the system from overload with **backpressure, timeouts and load shedding**. Behind them all is queueing theory: as utilisation approaches 100%, waiting time grows without bound, and in a system that fans requests out, the slowest component sets the response time. Scaling well is mostly about removing shared bottlenecks and managing those tails.

## Core tenets

1. **Statelessness makes horizontal scaling trivial.** If a web or application server keeps no session state between requests (state lives in a database, cache or client token), a load balancer can send any request to any server, a failed server is just removed, and capacity grows by adding copies. The hard scaling problem is pushed down into the stateful tier, where partitioning and replication handle it.

2. **Caching trades freshness for load and latency.** A cache in front of a database can absorb most reads, because access patterns are skewed toward popular items. The costs are invalidation (when to drop stale entries), consistency (readers see old data), and failure modes: if the cache is lost, the full load hits the backing store at once (a thundering herd), which may not survive it. Request coalescing and gradual warm-up mitigate this.

3. **Queueing delay explodes near saturation.** In the simple M/M/1 queue (Poisson arrivals, exponential service, one server), mean time in system is service time / (1 − ρ), where ρ is utilisation: at 50% load it is 2× the service time, at 90% 10×, at 99% 100×. Little's law (L = λW: items in the system equal arrival rate times time in system) holds for any stable queue. So systems are run with headroom, and latency, not throughput, is the first casualty of high load.

4. **Fan-out makes tail latency the common case.** If a request touches 100 servers and each is slow 1% of the time, about 63% of requests (1 − 0.99¹⁰⁰) hit at least one slow server. The 99th-percentile latency of each component becomes the median of the whole. Techniques include hedged requests (send a duplicate after a short delay and take the first reply), reducing fan-out, and engineering the tail of each component (Dean and Barroso, "The Tail at Scale", 2013).

5. **Asynchrony decouples rates.** Placing a durable queue between a front end and slow work (sending email, transcoding video) lets the front end respond immediately and lets workers process at their own rate, absorbing bursts. Consumers must be idempotent, because queues deliver at least once, and the queue length becomes a signal for autoscaling.

6. **Overload must be refused early, or it spreads.** Without limits, an overloaded service accumulates queued work it will finish too late to be useful, while clients retry and multiply the load. Defences are bounded queues and backpressure (tell callers to slow down), timeouts with deadlines propagated along the call chain, retries with exponential backoff and jitter, circuit breakers that stop calling a failing dependency, and load shedding that drops low-priority work first. Cascading failures in large systems usually begin with retries amplifying a small overload.

7. **Service decomposition scales teams as much as machines.** Splitting a monolith into services lets each scale, deploy and fail independently, and lets separate teams own them, but replaces function calls with network calls that can fail, adds latency, and turns transactions into sagas. The boundaries usually follow team structure ([Conway's law](../../12-software-engineering/02-process/conways-law-and-teams.md)), so the choice is organisational as well as technical.

## Key concepts

| Term | Meaning |
|---|---|
| Horizontal scaling | Adding more machines (scale out) |
| Vertical scaling | Using a bigger machine (scale up) |
| Stateless service | Holds no per-client state between requests |
| Load balancer | Distributes requests across equivalent servers |
| Cache invalidation | Removing or updating cached entries when the source changes |
| Utilisation ρ | Fraction of time a server is busy |
| Little's law | L = λW for any stable queueing system |
| Tail latency | High-percentile response time, such as p99 |
| Backpressure | Signalling upstream to slow down when downstream is full |
| Circuit breaker | Stops calls to a failing dependency for a cooling-off period |
| Load shedding | Rejecting some work deliberately to protect the rest |

## How it fits

- **Below:** caching is the [memory hierarchy](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md) idea at service scale and [content delivery](../../08-networking/05-application-layer/content-delivery-and-caching.md) at network scale; queueing results come from [latency and queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) and [probability](../../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md); exponential backoff mirrors [TCP congestion control](../../08-networking/04-transport-layer/congestion-control.md); state tiers rely on [partitioning](../04-distributed-data/partitioning.md), [replication](../03-consensus-and-replication/replication.md) and [eventual consistency](../04-distributed-data/eventual-consistency-and-crdts.md).
- **Above:** these patterns are the vocabulary of [software architecture](../../12-software-engineering/01-design/software-architecture.md); [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md) sets the error budgets they defend; [observability](../../12-software-engineering/04-operations/observability.md) measures their tails.
- **Siblings:** [cloud computing](cloud-computing.md) provides elastic capacity; [batch and stream processing](batch-and-stream-processing.md) handles work moved off the request path.

## Common misconceptions

- **"Average latency describes user experience."** Users with fan-out requests experience the tail; averages hide it.
- **"Retries make a system more reliable."** Unbounded, immediate retries turn a brief overload into a lasting outage; retries need budgets, backoff and jitter.
- **"Microservices are inherently more scalable."** They allow independent scaling, but add network hops and partial failures; many systems scale fine as a well-partitioned monolith.

## Go deeper

- Dean and Barroso, "The Tail at Scale", *Communications of the ACM* (2013).
- Beyer, Jones, Petoff and Murphy (eds.), *Site Reliability Engineering* (2016): chapters on overload and cascading failures.
- Kleppmann, *Designing Data-Intensive Applications* (2017): the stateful side of scaling.
- Harchol-Balter, *Performance Modeling and Design of Computer Systems* (2013): queueing theory for systems engineers.
