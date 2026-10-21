# Partitioning

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Distributed data](README.md)
> **Builds on:** [Hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md), [Search trees](../../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md), [Replication](../03-consensus-and-replication/replication.md)
> **Enables:** [Distributed transactions](distributed-transactions.md), [Batch and stream processing](../05-large-scale-systems/batch-and-stream-processing.md), [Scalability patterns](../05-large-scale-systems/scalability-patterns.md)

## Essence

Partitioning (also called sharding) splits a dataset into disjoint pieces stored on different nodes, so that storage and write throughput grow with the number of nodes. Replication copies data for fault tolerance; partitioning divides it for scale, and real systems do both, replicating each partition. The central design decision is the **partitioning function** from key to partition: by key range (keeps order, supports range scans, risks hot spots) or by hash of key (spreads load, destroys order). Everything else, rebalancing, request routing, secondary indexes, and cross-partition queries, follows from that choice and from the fact that the set of nodes changes over time.

## Core tenets

1. **Range partitioning preserves order; hash partitioning spreads load.** Assigning contiguous key ranges to partitions (as in Bigtable, HBase and Spanner) makes range scans efficient, because neighbouring keys live together, but sequential keys such as timestamps send all new writes to one partition. Hashing the key first (as in Dynamo-style stores and Cassandra by default) spreads writes evenly but turns any range query into a query to every partition. Compound keys combine them: hash a user identifier to pick the partition, keep that user's rows sorted by time within it.

2. **Naive modulo hashing makes rebalancing catastrophic.** With partition = hash(key) mod N, changing N from 10 to 11 moves about 10/11 of all keys. Consistent hashing (Karger et al., 1997) places nodes and keys on a ring and assigns each key to the next node clockwise, so adding or removing a node moves only about 1/N of the keys. Using many virtual nodes per physical node evens out the load. A simpler alternative is a fixed number of partitions, many more than nodes, with whole partitions moved between nodes.

3. **Skew defeats any static scheme.** Even with perfect hashing, one key can be hot: a celebrity's account, a viral product. All requests for that key hit one partition. Mitigations are application-level: split the hot key by adding a random suffix and fan reads across the pieces, cache it, or replicate it more widely. Load balancing by key count is not load balancing by work.

4. **Routing is an indirection that must itself be consistent.** A client must find which node holds a key. Options are: any node forwards the request; a routing tier consults a partition map; or the client caches the map. The map is cluster metadata that changes during rebalancing and failover, so it is usually stored in a consensus-backed coordination service (ZooKeeper, etcd) or spread by a gossip protocol, with version numbers to detect stale routes.

5. **Secondary indexes force a choice between scatter writes and scatter reads.** A *local* index (each partition indexes only its own rows) makes writes cheap but a query by secondary attribute must ask every partition (scatter-gather), whose latency is set by the slowest partition. A *global* index is itself partitioned by the indexed value, so reads touch one index partition but a write may need to update index partitions on other nodes, which requires a distributed transaction or accepts an index that lags.

6. **Cross-partition operations are where costs concentrate.** Joins, aggregates and transactions over several partitions need data movement or coordination. Good schema and key design co-locates data that is used together (all of a customer's orders in the customer's partition), so common operations stay single-partition. The rule of thumb from parallel computing applies: choose the decomposition so that most work is local.

7. **Rebalancing must not destroy availability.** Moving a partition means copying gigabytes while it keeps taking writes, then switching ownership atomically. Systems copy a snapshot, stream the changes made during the copy, briefly pause writes, and update the routing map. Fully automatic rebalancing on suspected failure can turn a slow node into a cascade of data movement, so many operators keep a human in the loop.

## Key concepts

| Term | Meaning |
|---|---|
| Partition (shard) | Disjoint subset of the data, owned by one replica group |
| Range partitioning | Contiguous key intervals assigned to partitions |
| Hash partitioning | Partition chosen by hash of the key |
| Consistent hashing | Ring-based assignment so membership changes move about 1/N of keys |
| Virtual node | Many ring positions per physical node to smooth load |
| Hot spot | Partition receiving disproportionate load |
| Partition map | Metadata mapping key ranges or hashes to nodes |
| Local index | Secondary index covering only one partition's data |
| Global index | Secondary index partitioned by the indexed value |
| Scatter-gather | Query sent to all partitions, results combined |

## How it fits

- **Below:** hash partitioning is a [hash table](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) whose buckets are machines; range partitioning is the top level of a [search tree](../../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md) or [B-tree](../../09-data-management/02-storage-and-indexing/b-trees.md); each partition stores data in [B-trees or LSM-trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md); each partition is a [replicated group](../03-consensus-and-replication/replication.md).
- **Above:** [distributed transactions](distributed-transactions.md) handle operations spanning partitions; [batch and stream engines](../05-large-scale-systems/batch-and-stream-processing.md) shuffle data by key between stages; [scalability patterns](../05-large-scale-systems/scalability-patterns.md) treat sharding as the main way to scale writes; [content delivery networks](../../08-networking/05-application-layer/content-delivery-and-caching.md) use consistent hashing to pick cache servers.
- **Siblings:** [distributed transactions](distributed-transactions.md) pay for coordination across partitions; [CRDTs](eventual-consistency-and-crdts.md) avoid coordination among replicas within one.

## Common misconceptions

- **"Hashing guarantees even load."** It evens out key counts, not request rates; a single hot key still lands on one node.
- **"Consistent hashing is a consistency mechanism."** It is about stable placement under membership change, not about data consistency.
- **"Sharding is free scale."** Every query that cannot be routed to one shard becomes a fan-out whose latency is the slowest shard's.

## Go deeper

- Kleppmann, *Designing Data-Intensive Applications* (2017), chapter "Partitioning".
- Karger et al., "Consistent Hashing and Random Trees", STOC (1997).
- Chang et al., "Bigtable: A Distributed Storage System for Structured Data", OSDI (2006): range partitioning with tablets.
- DeCandia et al., "Dynamo: Amazon's Highly Available Key-value Store", SOSP (2007): consistent hashing with virtual nodes.
