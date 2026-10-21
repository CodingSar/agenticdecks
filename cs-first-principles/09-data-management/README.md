# 09 Data Management

> **Layer:** 09 Data Management
> **Children:** [Data Models](01-data-models/README.md) · [Storage and Indexing](02-storage-and-indexing/README.md) · [Query Processing](03-query-processing/README.md) · [Transactions](04-transactions/README.md)

## What this area is about

Data management is the discipline of *durable, shared, queryable state*. Durable: data survives crashes and power loss. Shared: many users and programs read and change it at once without corrupting it. Queryable: users say *what* data they want and the system works out *how* to get it efficiently, even as data grows from kilobytes to petabytes and the physical layout changes underneath.

The unifying idea is **data independence**: separate the logical description of data (tables, relationships, constraints) from its physical storage (files, pages, indexes) and from the procedures that access it. A Database Management System (DBMS) owns everything below the logical interface. That separation lets it pick access paths automatically, reorganise storage without breaking applications, and enforce correctness rules (transactions) that individual programs could never coordinate on their own.

## Why this layer sits here

Data management builds on three lower layers:

- **[01 Mathematical Foundations](../01-mathematical-foundations/README.md):** a relation is a [set](../01-mathematical-foundations/02-sets-relations-functions/sets.md) of tuples, a subset of a Cartesian product, and a query is a formula of [predicate logic](../01-mathematical-foundations/01-logic/predicate-logic.md). Relational algebra is set theory plus logic, which is why queries can be rewritten and optimised by algebraic laws.
- **[05 Algorithms and Data Structures](../05-algorithms-and-data-structures/README.md):** indexes are [search trees](../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md) and [hash tables](../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) adapted to disk; joins are [sorting](../05-algorithms-and-data-structures/04-sorting-and-searching/comparison-sorting.md) and hashing; the cost model is the [external-memory model](../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md), which counts block transfers rather than instructions.
- **[07 Operating Systems](../07-operating-systems/README.md):** databases sit on [file systems](../07-operating-systems/05-storage-and-file-systems/file-system-abstractions.md) or raw devices, use the same [crash-consistency techniques](../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md) (write-ahead logging), and solve the same [concurrency](../07-operating-systems/03-concurrency/race-conditions-and-critical-sections.md) problems with locks at a finer, logical granularity.

It sits above [08 Networking](../08-networking/README.md) because modern databases are client/server and replicated: clients speak wire protocols over TCP, and logs are shipped across networks. It contributes to the stack one abstraction: **a transaction over declaratively queried, durable shared state**, a unit of work that appears to run alone and either completes entirely or not at all. [Distributed systems (10)](../10-distributed-and-parallel-computing/README.md) extend that abstraction across machines; [AI and machine learning (13)](../13-artificial-intelligence/README.md) consume the data it manages.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [01 Data Models](01-data-models/README.md) | The logical interface: what data looks like, how it is queried, how redundancy is avoided | Sets, logic (01) |
| [02 Storage and Indexing](02-storage-and-indexing/README.md) | The physical layer: pages, row vs column layout, B-trees, LSM-trees | Data structures (05), file systems (07) |
| [03 Query Processing](03-query-processing/README.md) | The bridge: turns a declarative query into an efficient plan over storage | Data models, storage |
| [04 Transactions](04-transactions/README.md) | Correctness under concurrency and failure: ACID, concurrency control, isolation, recovery | Storage, OS concurrency and crash consistency |

```
        SQL query                       application transaction
            |                                     |
   [parser -> optimizer -> plan]        [concurrency control | logging]
            |                                     |
   [execution: scans, joins, sorts] ------ [buffer pool / storage engine]
                                                  |
                                    [pages on disk: heap files, B-trees, LSM]
```

Read data models first: they define the contract. Storage and indexing show how the contract is laid out on hardware that is slow for random access. Query processing connects the two, choosing among many equivalent plans by estimated cost. Transactions cut across everything: they decide which interleavings of concurrent work are allowed and how to recover after a crash. Each child can be read alone, but the payoff is seeing how the logical/physical separation lets each evolve independently.

## Connections to neighbouring layers

- **[01 Mathematical Foundations](../01-mathematical-foundations/README.md):** relational algebra and calculus; functional dependencies are a theory of [relations](../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md) and [functions](../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md); cardinality estimation uses [statistics](../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md).
- **[04 Computer Architecture](../04-computer-architecture/README.md):** the gap between [DRAM and storage devices](../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md) shapes everything; column stores exploit [SIMD](../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) and caches.
- **[05 Algorithms and Data Structures](../05-algorithms-and-data-structures/README.md):** B-trees, hashing, external sorting and graph search underlie storage and execution.
- **[06 Programming Languages](../06-programming-languages/README.md):** SQL is the most successful [declarative language](../06-programming-languages/01-paradigms/logic-and-declarative.md); query compilers use [compiler techniques](../06-programming-languages/03-compilers/optimization.md).
- **[07 Operating Systems](../07-operating-systems/README.md):** buffer pools duplicate and often bypass the OS page cache; logging generalises journaling.
- **[08 Networking](../08-networking/README.md):** client/server protocols, and the latency cost of chatty access patterns.
- **[10 Distributed and Parallel Computing](../10-distributed-and-parallel-computing/README.md):** [replication](../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md), [partitioning](../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md) and [distributed transactions](../10-distributed-and-parallel-computing/04-distributed-data/distributed-transactions.md) extend this layer's ideas across machines.
- **[13 Artificial Intelligence](../13-artificial-intelligence/README.md):** training data pipelines, feature stores and vector search depend on data management.

## Connections across layers

This layer takes logic and sets from 01, external-memory algorithms from 05 and crash consistency from 07, and returns a durable, transactional, declaratively queried store. Above it, distributed systems inherit the vocabulary of transactions and isolation, security relies on [access control](../11-security-and-cryptography/03-system-security/access-control.md) over data, and [software engineering](../12-software-engineering/01-design/software-architecture.md) organises applications around a database as the system of record.

## Cross-cutting threads

- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): logical and physical data independence.
- [Interface vs implementation](../CROSS-CUTTING.md#interface-vs-implementation): SQL states what; the optimizer chooses how.
- [Caching and locality](../CROSS-CUTTING.md#caching-and-locality): the buffer pool and index node caching.
- [Batching and amortization](../CROSS-CUTTING.md#batching-and-amortization): group commit, LSM compaction, vectorised execution.
- [Invariants and correctness](../CROSS-CUTTING.md#invariants-and-correctness): integrity constraints and serializability.
- [State and time](../CROSS-CUTTING.md#state-and-time): concurrency control and multiversioning.
- [Redundancy and fault tolerance](../CROSS-CUTTING.md#redundancy-and-fault-tolerance): write-ahead logs and replicas.
- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): read vs write amplification, isolation vs throughput, normalisation vs join cost.
- [Encoding and representation](../CROSS-CUTTING.md#encoding-and-representation): row vs column layout decides what is cheap.
