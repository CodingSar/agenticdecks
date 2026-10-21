# Distributed Data

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › Distributed data
> **Children:** [Partitioning](partitioning.md) · [Distributed transactions](distributed-transactions.md) · [Eventual consistency and conflict-free replicated data types](eventual-consistency-and-crdts.md)

## What this area is about

When a dataset or its write load outgrows one machine, it must be split across many. This area asks how to spread data so that load is even and most operations touch one machine, how to keep operations that span machines correct, and how to let replicas accept writes independently and still converge. It is where the single-node database of [09 Data Management](../../09-data-management/README.md) meets the replication and consensus machinery of this layer.

The unifying idea is **minimising coordination**. Every operation that needs several machines to agree costs round trips and is exposed to their failures. Good partitioning keeps most operations on one partition; distributed transactions pay for coordination only when an operation truly spans partitions; conflict-free replicated data types (CRDTs) remove coordination entirely by designing data whose concurrent updates always merge.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Partitioning](partitioning.md) | Splitting data across nodes by key range or hash; rebalancing; routing | Hash tables, search trees, replication |
| [Distributed transactions](distributed-transactions.md) | Atomic, isolated operations across partitions: two-phase commit, distributed concurrency control | Partitioning, consensus, single-node transactions |
| [Eventual consistency and CRDTs](eventual-consistency-and-crdts.md) | Coordination-free replication where merges are guaranteed to converge | Clocks, consistency models |

```
                 one logical dataset
                        |
          partition by key (range / hash)
        /               |                \
   partition A     partition B      partition C     each = replica group
   (consensus)     (consensus)      (consensus)
        \_______ 2PC across groups ______/          strong path
   or: replicas accept writes locally, merge via CRDT   available path
```

Read partitioning first, since it creates the problem the other two solve. Distributed transactions are the strong path: they keep ACID (Atomicity, Consistency, Isolation and Durability) guarantees across partitions at the cost of coordination. CRDTs are the available path: they give up cross-replica coordination and accept eventual consistency, but with a mathematical guarantee of convergence. Real systems use both, choosing per data type.

## Connections to sibling areas

- **[Consensus and replication](../03-consensus-and-replication/README.md):** each partition is typically a replicated group running Raft or Paxos; modern distributed databases put two-phase commit on top of those groups so a coordinator crash cannot block forever.
- **[Distributed foundations](../02-distributed-foundations/README.md):** version vectors come from vector clocks; the CAP (Consistency, Availability, Partition tolerance) theorem explains why the strong and available paths differ.
- **[Parallel computing](../01-parallel-computing/README.md):** partitioning data so most work is local is the same goal as data-parallel decomposition with good locality.
- **[Large-scale systems](../05-large-scale-systems/README.md):** batch and stream engines repartition (shuffle) data between stages; scalability patterns such as sharding and caching are this area applied.

## Connections across layers

From [09 Data Management](../../09-data-management/README.md): [transactions](../../09-data-management/04-transactions/acid.md), [concurrency control](../../09-data-management/04-transactions/concurrency-control.md), [isolation levels](../../09-data-management/04-transactions/isolation-levels.md), [B-trees](../../09-data-management/02-storage-and-indexing/b-trees.md) and [log-structured merge (LSM) trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md), and [join algorithms](../../09-data-management/03-query-processing/join-algorithms.md) that become distributed joins. From [05 Algorithms](../../05-algorithms-and-data-structures/README.md): [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) and [search trees](../../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md). From [01 Mathematics](../../01-mathematical-foundations/README.md): the [lattices and semilattices](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md) that make CRDT merges sound. Upward, it supports [machine learning data pipelines](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md) and collaborative applications in [human-computer interaction](../../14-human-and-visual-computing/01-human-computer-interaction/README.md).

## Cross-cutting threads

- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): coordination buys consistency at the price of latency and availability.
- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): routing tables map keys to partitions and let data move.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): atomic commit keeps "all or nothing" across machines.
- [State and time](../../CROSS-CUTTING.md#state-and-time): version vectors detect concurrent updates.
- [Composition](../../CROSS-CUTTING.md#composition): CRDTs compose because merge is a join in a semilattice.
