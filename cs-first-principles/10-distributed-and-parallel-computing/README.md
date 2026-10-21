# 10 Distributed and Parallel Computing

> **Layer:** 10 Distributed and Parallel Computing
> **Children:** [Parallel computing](01-parallel-computing/README.md) · [Distributed foundations](02-distributed-foundations/README.md) · [Consensus and replication](03-consensus-and-replication/README.md) · [Distributed data](04-distributed-data/README.md) · [Large-scale systems](05-large-scale-systems/README.md)

## What this area is about

This layer asks how many computers, or many processors in one computer, can do one job together. Parallel computing uses many processors to finish a job faster. Distributed computing uses many machines because one machine is not big enough, not reliable enough, or not close enough to its users. The two overlap, but their defining problems differ.

Parallel computing is mostly a problem of *dividing work and moving data*: how much of the job can run at once, and what does communication cost? Distributed computing adds two harder problems that a single machine hides. The first is **partial failure**: one machine can crash, slow down or lose its network link while the others keep running, and the survivors often cannot tell which of these happened. The second is **the absence of a global clock**: each machine has its own clock, the clocks drift, and messages take unknown time, so "which event happened first?" has no free answer. Almost every idea in this layer (logical clocks, quorums, consensus, consistency models, idempotent retries) is a response to one of these two facts.

## Why this layer sits here

The layer needs four things from below.

- **Hardware parallelism and its rules** from [04 Computer Architecture](../04-computer-architecture/README.md). Multicore chips, [cache coherence](../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md) and [memory consistency models](../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md) are the small-scale version of the replication and consistency problems studied here. [Amdahl's law](../04-computer-architecture/06-performance/amdahls-law.md) bounds every speed-up.
- **Concurrency control on one machine** from [07 Operating Systems](../07-operating-systems/README.md). [Race conditions](../07-operating-systems/03-concurrency/race-conditions-and-critical-sections.md), [locks](../07-operating-systems/03-concurrency/locks-and-semaphores.md) and [deadlock](../07-operating-systems/03-concurrency/deadlock.md) reappear here, but without shared memory and with failures.
- **Messages between machines** from [08 Networking](../08-networking/README.md). The network may delay, drop, duplicate or reorder packets; the [Transmission Control Protocol (TCP)](../08-networking/04-transport-layer/udp-and-tcp.md) hides some of this inside one connection but cannot hide a crashed peer.
- **Transactions** from [09 Data Management](../09-data-management/README.md). [Atomicity, Consistency, Isolation and Durability (ACID)](../09-data-management/04-transactions/acid.md), [isolation levels](../09-data-management/04-transactions/isolation-levels.md) and [write-ahead logging](../09-data-management/04-transactions/recovery-and-logging.md) are the single-node definitions that distributed transactions and replicated logs must preserve across machines.

Upward, the layer gives **the illusion of one reliable, fast machine built from many unreliable ones**. That abstraction is what [13 Artificial Intelligence (AI)](../13-artificial-intelligence/README.md) uses to [train models at scale](../13-artificial-intelligence/03-deep-learning/training-at-scale.md), and what [12 Software Engineering](../12-software-engineering/README.md) has to run and repair in [operations](../12-software-engineering/04-operations/reliability-engineering.md). [11 Security](../11-security-and-cryptography/README.md) sits next to it and adds a stronger adversary: Byzantine faults are what you get when a failed node may also be malicious.

## How the children fit together

```
            05 Large-scale systems  (batch/stream, cloud, scalability patterns)
                       ^
            04 Distributed data     (partitioning, distributed transactions, conflict-free types)
                       ^
            03 Consensus & replication (replication, consensus, consistency, Byzantine)
                       ^
            02 Distributed foundations (system models, clocks, impossibility)
                       ^
 01 Parallel computing (work/span, decomposition, programming models)
```

| Child | Its role in the whole | Depends on |
|---|---|---|
| [01 Parallel computing](01-parallel-computing/README.md) | How to split work and what limits speed-up when nothing fails | 04, 05, 07 |
| [02 Distributed foundations](02-distributed-foundations/README.md) | The assumptions (failures, timing) and the theorems that say what is impossible | 01, 08 |
| [03 Consensus and replication](03-consensus-and-replication/README.md) | How copies of state stay in agreement despite failures | 02 |
| [04 Distributed data](04-distributed-data/README.md) | How a database spreads over many machines and keeps transactions correct | 03, 09 |
| [05 Large-scale systems](05-large-scale-systems/README.md) | How whole platforms (data pipelines, clouds, web services) are assembled from the above | 01–04 |

Read 01 first: it isolates the cost of coordination before failures enter. Then 02, because every algorithm in 03 and 04 is correct only under a stated system model, and the impossibility results tell you which guarantees you must trade away. 03 is the core: replication and consensus are the tools; consistency models are the vocabulary for what the tools promise. 04 applies them to data that is too large for one machine. 05 shows how practitioners combine all of it, usually by avoiding coordination wherever they can.

## Connections to neighbouring layers

- **[04 Computer Architecture](../04-computer-architecture/README.md):** a multicore chip is a tiny distributed system with a reliable, fast network. Coherence protocols are replication protocols; memory consistency models are the hardware ancestors of linearizability and sequential consistency.
- **[05 Algorithms and Data Structures](../05-algorithms-and-data-structures/README.md):** parallel algorithm analysis extends the Random Access Machine (RAM) model with work and span; [consistent hashing](04-distributed-data/partitioning.md) is a [hash table](../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) designed for membership change.
- **[07 Operating Systems](../07-operating-systems/README.md):** threads and locks are the shared-memory programming model; [virtual machines](../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md) and [containers](../07-operating-systems/07-virtualization/containers.md) are the units of [cloud computing](05-large-scale-systems/cloud-computing.md).
- **[08 Networking](../08-networking/README.md):** supplies the message-passing substrate and its latency numbers; the [end-to-end argument](../08-networking/01-principles/layering-and-the-end-to-end-principle.md) explains why applications still need idempotency even over TCP.
- **[09 Data Management](../09-data-management/README.md):** distributed databases are 09 plus partitioning and replication; [two-phase commit](04-distributed-data/distributed-transactions.md) extends atomicity across nodes.
- **[11 Security](../11-security-and-cryptography/README.md):** Byzantine fault tolerance assumes signatures and hashes from [cryptography](../11-security-and-cryptography/02-cryptography/README.md).
- **[12 Software Engineering](../12-software-engineering/README.md):** reliability engineering, observability and continuous delivery are how these systems are run day to day.
- **[13 Artificial Intelligence](../13-artificial-intelligence/README.md):** large-model training is data, tensor and pipeline parallelism over thousands of accelerators.

## Connections across layers

The layer converts three lower-level facts into design constraints. From physics ([00](../00-engineering-foundations/README.md)): signals travel at most at the speed of light, about 5 µs per kilometre of fibre, so a cross-continent round trip costs tens of milliseconds and no protocol can hide it. From probability ([01](../01-mathematical-foundations/06-probability-and-statistics/probability.md)): with thousands of machines, some machine is always failing, so failure is the normal case. From theory ([02](../02-theory-of-computation/README.md)): some agreement problems are provably unsolvable under weak assumptions, just as some functions are uncomputable.

## Cross-cutting threads

- [State and time](../CROSS-CUTTING.md#state-and-time): no global clock; ordering must be built from messages.
- [Limits and impossibility](../CROSS-CUTTING.md#limits-and-impossibility): the Fischer–Lynch–Paterson (FLP) result, the CAP (Consistency, Availability, Partition tolerance) theorem and the Byzantine bound shape every design.
- [Redundancy and fault tolerance](../CROSS-CUTTING.md#redundancy-and-fault-tolerance): replication and quorums survive crashes.
- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): consistency against availability and latency.
- [Pipelining and parallelism](../CROSS-CUTTING.md#pipelining-and-parallelism): work and span set the speed-up limit.
- [Batching and amortization](../CROSS-CUTTING.md#batching-and-amortization): batching messages amortizes round trips and consensus rounds.
- [Virtualization](../CROSS-CUTTING.md#virtualization): the cloud makes a data centre look like an elastic pool.
- [Invariants and correctness](../CROSS-CUTTING.md#invariants-and-correctness): safety and liveness properties define what "correct" means.
