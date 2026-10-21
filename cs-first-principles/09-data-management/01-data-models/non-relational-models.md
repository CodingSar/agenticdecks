# Non-Relational Models

> **Layer:** [09 Data Management](../README.md) › [Data Models](README.md)
> **Builds on:** [The Relational Model](the-relational-model.md), [Normalization](normalization.md), [Hash Tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md), [Graph Theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md)
> **Enables:** [LSM-Trees](../02-storage-and-indexing/lsm-trees.md), [Partitioning](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md), [Eventual Consistency and CRDTs](../../10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md), [Knowledge Representation and Reasoning](../../13-artificial-intelligence/01-classical-ai/knowledge-representation-and-reasoning.md)

## Essence

Non-relational data models (often grouped under the label "NoSQL") give up some part of the relational design (fixed schema, joins, general transactions or declarative queries) in exchange for a better fit to a particular access pattern or easier horizontal scaling. Key-value stores reduce the interface to get and put by key. Document stores keep nested, self-describing records. Wide-column stores organise sparse rows by partition and sort keys. Graph databases make relationships first-class and traversals cheap. Each is a different answer to "which queries must be fast, and which may be slow or impossible?" The trade is real, and the history since about 2010 shows many systems adding back schemas, Structured Query Language (SQL) and transactions once they hit the problems relational systems had already solved.

## Core tenets

1. **Every model is optimised for its access path.** A relational schema is neutral: any query can be expressed, and the optimizer finds a path. Non-relational models choose the path at design time. If the application always fetches "a user and all their orders together", embedding orders in the user document turns a join into a single read. If later it needs "all orders for a product", that model makes the query awkward or slow.

2. **Key-value stores are distributed hash tables.** The only operations are get, put and delete by key, sometimes with range scans if keys are sorted. Because each operation touches one key, data can be partitioned across many machines by hashing the key, and each request goes to one partition. This gives near-linear scale-out and predictable latency, at the cost of no queries over values.

3. **Document models trade joins for locality.** A document (usually JavaScript Object Notation (JSON), or a binary variant) nests related data in one record. Reading a whole aggregate is one lookup and one contiguous read. But data shared across documents must be duplicated (with update anomalies) or referenced by identifier (with application-side joins). The model fits one-to-many tree-shaped data; it strains on many-to-many relationships.

4. **"Schemaless" means schema-on-read.** The database does not enforce a structure, but the application still assumes one. Schema changes move from a migration at write time to code that handles every historical shape at read time. This is flexible for evolving or heterogeneous data, and risky when many programs share the data.

5. **Wide-column stores are sorted maps partitioned across machines.** In the Bigtable lineage (Bigtable, HBase, Cassandra), data is addressed by (row key, column, timestamp). Rows are kept sorted by key and split into ranges or hash partitions across servers, so range scans within a partition are fast. They are usually backed by log-structured storage, which suits high write rates.

6. **Graph models make relationships first-class.** Nodes and edges both carry properties; queries are path patterns ("friends of friends who like X"). In a relational system, each hop is a join; in a native graph store, each hop follows a stored adjacency, so multi-hop traversals cost proportional to the edges visited rather than to table sizes. This suits social networks, fraud detection and knowledge graphs.

7. **Scale-out pressure drove weaker consistency.** Early NoSQL systems (Amazon's Dynamo, 2007; Cassandra) chose availability and partition tolerance, replicating data asynchronously and accepting temporarily divergent replicas. This is a distributed-systems trade-off, not a property of the data model, and later systems such as Spanner showed that relational semantics with strong consistency can scale out too.

8. **The models are converging.** Relational systems added JSON columns, full-text and graph queries; document and wide-column stores added secondary indexes, SQL-like languages and multi-document transactions. The lasting lesson is that the logical model and the distribution strategy are separate choices.

## Key concepts

| Term | Meaning |
|---|---|
| Key-value store | Get/put/delete by key; values opaque to the database |
| Document | Nested, self-describing record, usually JSON-like |
| Aggregate | Cluster of related data read and written as one unit |
| Schema-on-read | Structure interpreted by the reader rather than enforced on write |
| Wide-column store | Sparse rows addressed by row key, column and timestamp, partitioned by key |
| Property graph | Nodes and edges with key-value properties |
| Traversal | Following edges from node to node in a query |
| Polyglot persistence | Using several data models in one system, each for what it does best |

## How it fits

- **Below:** key-value stores are [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) spread across machines; graph models are [graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md) with properties attached; the trade-offs are measured against [the relational model](the-relational-model.md) and [normalization](normalization.md).
- **Above:** wide-column and key-value stores typically use [LSM-trees](../02-storage-and-indexing/lsm-trees.md); they are designed around [partitioning](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md) and often [eventual consistency](../../10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md). Knowledge graphs connect to [knowledge representation](../../13-artificial-intelligence/01-classical-ai/knowledge-representation-and-reasoning.md) in Artificial Intelligence (AI).
- **Siblings:** [relational algebra and SQL](relational-algebra-and-sql.md) is what these models give up and often later re-adopt; [normalization](normalization.md) explains the anomalies embedding reintroduces.

## Common misconceptions

- **"NoSQL is faster than SQL."** It is faster for the access patterns it was designed around and slower or unable for others; a relational system with the right index is often as fast for key lookups.
- **"Schemaless means no schema."** The schema moves into application code, where it is harder to see and enforce.
- **"Non-relational systems cannot do transactions."** Many now support single-document or multi-document Atomicity, Consistency, Isolation, Durability (ACID) transactions; the original absence was a scaling choice.

## Go deeper

- F. Chang et al., *Bigtable: A Distributed Storage System for Structured Data* (OSDI 2006): the wide-column model.
- G. DeCandia et al., *Dynamo: Amazon's Highly Available Key-value Store* (SOSP 2007): key-value design for availability.
- M. Kleppmann, *Designing Data-Intensive Applications* (2017): balanced comparison of data models and their trade-offs.
