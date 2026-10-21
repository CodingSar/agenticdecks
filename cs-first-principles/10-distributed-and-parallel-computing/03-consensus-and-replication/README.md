# Consensus and Replication

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › Consensus and replication
> **Children:** [Replication](replication.md) · [Consensus](consensus.md) · [Consistency models](consistency-models.md) · [Byzantine fault tolerance](byzantine-fault-tolerance.md)

## What this area is about

To survive the loss of a machine, a system keeps copies of its state on several machines. The moment there are copies, they can disagree: a write reaches one copy and not another, or two clients write different copies at once. This area asks how copies are kept in agreement while machines crash and networks misbehave, and what exactly "in agreement" should promise to the clients who read them.

The unifying idea is the **replicated state machine**: if every replica starts in the same state and applies the same deterministic commands in the same order, every replica ends in the same state. Replication then reduces to agreeing on the order of commands, which is the consensus problem. Consistency models say what clients observe when the system takes shortcuts around full consensus, and Byzantine fault tolerance extends the whole approach to replicas that may lie.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Replication](replication.md) | The structures: leader-based, multi-leader and leaderless replication, synchronous versus asynchronous, quorums | System models |
| [Consensus](consensus.md) | The core algorithm: agreeing on one value, then on a log of values (Paxos, Raft) despite crashes | Replication, impossibility results |
| [Consistency models](consistency-models.md) | The contract: what reads may return, from linearizability down to eventual consistency | Clocks and ordering, replication |
| [Byzantine fault tolerance](byzantine-fault-tolerance.md) | The same goal when replicas may behave arbitrarily: 3f + 1 replicas, signatures, Practical Byzantine Fault Tolerance (PBFT) | Consensus, cryptography |

```
  clients --> consistency model (the promise)
                  |
                  v
          replication scheme (who accepts writes, who must ack)
                  |
                  v
          consensus on a log  --crash faults-->  Paxos / Raft  (2f+1)
                              --arbitrary faults--> PBFT-style (3f+1)
```

Read replication first to see the design space and its failure modes (split brain, lost writes, stale reads). Consensus then shows the one mechanism that closes those holes without trusting timing for safety. Consistency models give the vocabulary to compare the strong option (consensus on every operation) with cheaper options. Byzantine fault tolerance comes last because it is the same story with a stronger adversary and higher costs.

## Connections to sibling areas

- **[Distributed foundations](../02-distributed-foundations/README.md):** supplies the failure and timing models; FLP explains why consensus relies on partial synchrony for liveness, and CAP explains why strong consistency costs availability during partitions.
- **[Parallel computing](../01-parallel-computing/README.md):** hardware cache coherence is a replication protocol on a reliable bus, and memory consistency models are the shared-memory twin of the consistency models here.
- **[Distributed data](../04-distributed-data/README.md):** each partition of a distributed database is usually a replica group running consensus; distributed transactions sit on top of those groups; CRDTs are the coordination-free alternative.
- **[Large-scale systems](../05-large-scale-systems/README.md):** coordination services such as ZooKeeper and etcd package consensus for leader election, configuration and locks used across a cluster.

## Connections across layers

From [09 Data Management](../../09-data-management/README.md) this area takes the [write-ahead log](../../09-data-management/04-transactions/recovery-and-logging.md): a replicated log is a write-ahead log that several machines agree on. From [04 Computer Architecture](../../04-computer-architecture/README.md) it takes [coherence](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md) and [memory consistency](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md). From [11 Security](../../11-security-and-cryptography/README.md) Byzantine protocols take [digital signatures and MACs](../../11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md). It provides the reliable core of [cloud platforms](../05-large-scale-systems/cloud-computing.md) and is what [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md) depends on when it promises that data survives a machine loss. [Model checking](../../06-programming-languages/05-formal-methods/model-checking.md), notably TLA+ specifications, is routinely used to verify these protocols.

## Cross-cutting threads

- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): copies plus quorums survive f failures.
- [State and time](../../CROSS-CUTTING.md#state-and-time): replication is agreement on the order of state changes.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): "at most one value is chosen" is kept by quorum intersection.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): stronger consistency costs latency and availability.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): BFT replaces trust in each replica with trust in a two-thirds majority.
