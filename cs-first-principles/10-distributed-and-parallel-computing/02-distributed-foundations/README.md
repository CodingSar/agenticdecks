# Distributed Foundations

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › Distributed foundations
> **Children:** [System models and failures](system-models-and-failures.md) · [Time, clocks and ordering](time-clocks-and-ordering.md) · [Impossibility results](impossibility-results.md)

## What this area is about

A distributed system is a set of computers that cooperate only by sending messages over a network, where any computer or link can fail independently. Leslie Lamport's quip states the problem: "A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable." This area defines the ground rules before any algorithm is designed: what can fail and how, what can be known about time, and which goals are therefore impossible.

The unifying idea is **uncertainty about other machines' state**. A node learns about others only from messages, messages take unknown time, and a silent node may be crashed, slow or cut off. Every correctness argument in this layer starts by stating exactly how much uncertainty is assumed. Change the assumptions and the same problem can move from easy to impossible.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [System models and failures](system-models-and-failures.md) | States the assumptions: timing (synchronous, asynchronous, partially synchronous) and failure types (crash, omission, Byzantine) | Networking, probability |
| [Time, clocks and ordering](time-clocks-and-ordering.md) | Builds a usable notion of "before" without a global clock: physical sync, Lamport clocks, vector clocks | System models |
| [Impossibility results](impossibility-results.md) | Proves what no algorithm can do under given models: the Fischer–Lynch–Paterson (FLP) result, the Consistency–Availability–Partition tolerance (CAP) theorem, Two Generals, the 3f+1 bound | System models, clocks |

The order is deliberate. You cannot state a theorem until you fix a model, and you cannot reason about consistency until you know what "happened before" means without shared time. The impossibility results then mark the edges of the design space, and every algorithm in [consensus and replication](../03-consensus-and-replication/README.md) is best read as a way of stepping around one of them (by adding timing assumptions, randomness, or by weakening the guarantee).

```
   model (timing + failures)
        |
        +--> what can be ordered?   (happened-before, logical clocks)
        |
        +--> what can be agreed?    (FLP, CAP, Two Generals, 3f+1)
                    |
                    v
        algorithms that escape by changing an assumption
```

## Connections to sibling areas

- **[Parallel computing](../01-parallel-computing/README.md):** shares message passing and synchronisation, but parallel models assume reliable processors and known communication costs; this area removes those guarantees.
- **[Consensus and replication](../03-consensus-and-replication/README.md):** applies these foundations; Paxos and Raft are safe in the asynchronous model and live only under partial synchrony, exactly as FLP requires.
- **[Distributed data](../04-distributed-data/README.md):** vector clocks and version vectors detect concurrent writes; CAP explains why partitioned data stores choose between consistency and availability.
- **[Large-scale systems](../05-large-scale-systems/README.md):** timeouts, retries, leases and idempotency in production systems are engineering consequences of the asynchronous model.

## Connections across layers

From [08 Networking](../../08-networking/README.md) this area takes the facts that [packets](../../08-networking/01-principles/packet-switching.md) can be delayed and dropped and that [queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) makes delay unbounded in practice. From [04 Computer Architecture](../../04-computer-architecture/README.md) it takes the [memory consistency model](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md) idea of "which orders are visible". From [02 Theory of Computation](../../02-theory-of-computation/README.md) it borrows the style of impossibility proof seen in the [halting problem](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md). It gives [11 Security](../../11-security-and-cryptography/README.md) the Byzantine failure model and gives [12 Software Engineering](../../12-software-engineering/04-operations/reliability-engineering.md) its vocabulary for failure.

## Cross-cutting threads

- [State and time](../../CROSS-CUTTING.md#state-and-time): happened-before replaces a global clock.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): FLP, CAP and the Byzantine bound.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): safety and liveness split every specification.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): failure models decide how many copies are enough.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): Byzantine models assume nothing about faulty nodes.
