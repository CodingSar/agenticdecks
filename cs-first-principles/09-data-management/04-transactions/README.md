# Transactions

> **Layer:** [09 Data Management](../README.md) › Transactions
> **Children:** [ACID](acid.md) · [Concurrency Control](concurrency-control.md) · [Isolation Levels](isolation-levels.md) · [Recovery and Logging](recovery-and-logging.md)

## What this area is about

Many users change a shared database at once, and the machine can crash at any moment. Without help, every application would have to reason about every possible interleaving with every other program and every possible point of failure. A transaction is the abstraction that removes that burden: a group of reads and writes that appears to execute alone (isolation) and entirely or not at all (atomicity), whose effects survive crashes once committed (durability), and which takes the database from one valid state to another (consistency). Together they are known by the acronym Atomicity, Consistency, Isolation, Durability (ACID). The programmer writes sequential code; the system makes it safe.

The unifying idea is that two mechanisms deliver the abstraction. *Concurrency control* decides which interleavings of concurrent transactions are allowed, so the result equals some serial order. *Recovery*, built on a write-ahead log, undoes the effects of transactions that did not commit and redoes those that did but had not reached disk when the crash happened. Isolation levels are the dial between correctness and throughput that practical systems expose.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [ACID](acid.md) | The contract: what each property means and what it costs | Data model constraints |
| [Concurrency Control](concurrency-control.md) | Mechanisms for isolation: serializability, two-phase locking, optimistic and multiversion schemes | ACID, operating-system locking |
| [Isolation Levels](isolation-levels.md) | The weaker guarantees systems actually offer, and the anomalies each permits | Concurrency control |
| [Recovery and Logging](recovery-and-logging.md) | Mechanisms for atomicity and durability: write-ahead logging, Algorithm for Recovery and Isolation Exploiting Semantics (ARIES), checkpoints | ACID, storage, crash consistency |

```
             ACID contract
           /              \
  isolation                 atomicity + durability
     |                           |
 concurrency control        recovery (WAL, undo/redo)
 (2PL, OCC, MVCC)                |
     |                       checkpoints, group commit
 isolation levels (dial)
```

Read ACID first: it states the promise. Concurrency control and recovery are independent mechanisms behind it, readable in either order. Isolation levels come after concurrency control, because each level is defined by which anomalies a weakened mechanism lets through.

## Connections to sibling areas

- **[Data Models](../01-data-models/README.md):** integrity constraints are the invariants transactions preserve; the consistency in ACID is defined by them.
- **[Storage and Indexing](../02-storage-and-indexing/README.md):** recovery controls when buffer pool pages may be written; indexes need their own latching and logging; multiversion storage keeps old row versions for concurrent readers.
- **[Query Processing](../03-query-processing/README.md):** long-running queries interact with locks and versions; snapshot reads let analytics run without blocking writers.

## Connections across layers

Concurrency control generalises the [locks](../../07-operating-systems/03-concurrency/locks-and-semaphores.md) and [deadlock](../../07-operating-systems/03-concurrency/deadlock.md) handling of operating systems to logical data items; recovery generalises [crash consistency and journaling](../../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md). Serializability is close kin to the [memory consistency models](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md) of hardware. Above, [distributed transactions](../../10-distributed-and-parallel-computing/04-distributed-data/distributed-transactions.md) and [consistency models](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consistency-models.md) extend these ideas across machines, and [replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md) ships the same log.

## Cross-cutting threads

- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): serializability preserves any invariant each transaction preserves alone.
- [State and time](../../CROSS-CUTTING.md#state-and-time): ordering conflicting operations is the whole problem.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): the log is a redundant record that makes crashes survivable.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): group commit shares one log flush among many transactions.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): isolation level trades anomalies for concurrency.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): a transaction hides concurrency and failure behind sequential code.
