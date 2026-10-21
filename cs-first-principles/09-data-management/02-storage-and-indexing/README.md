# Storage and Indexing

> **Layer:** [09 Data Management](../README.md) › Storage and Indexing
> **Children:** [Storage Layouts](storage-layouts.md) · [B-Trees](b-trees.md) · [LSM-Trees](lsm-trees.md)

## What this area is about

Storage and indexing answer the physical question: given relations defined logically, how should their bytes be arranged on devices so that the queries and updates that matter are cheap? The governing fact is the memory hierarchy. Reading a byte from Dynamic Random-Access Memory (DRAM) (Dynamic Random-Access Memory) takes ~100 ns; a random read from a Solid-State Drive (SSD) takes ~10–100 µs; from a spinning disk, ~5–10 ms. Devices transfer data in blocks or pages of kilobytes, and sequential access is far faster than random access. So the cost of a database operation is counted in page transfers, not instructions.

The unifying idea is that every physical design is a trade among three costs: reading, writing and space. A heap file appends cheaply but must be scanned to find anything. A B-tree makes point and range reads take a few page accesses but updates pages in place. An LSM-tree (Log-Structured Merge-tree) turns all writes into sequential appends but makes reads consult several places. Row layouts favour fetching whole records; column layouts favour scanning a few attributes over many records. No design wins on all three axes, a result sometimes summarised as the RUM conjecture (Read, Update, Memory).

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Storage Layouts](storage-layouts.md) | Pages, records, heap files, row vs column organisation, the buffer pool | Memory hierarchy (04), file systems (07) |
| [B-Trees](b-trees.md) | The read-optimised, update-in-place index: balanced, high fan-out, logarithmic page accesses | Storage layouts, search trees (05) |
| [LSM-Trees](lsm-trees.md) | The write-optimised index: buffer in memory, flush sorted runs, merge in the background | Storage layouts, external sorting (05) |

```
              read cost  write cost  space   typical use
  heap file      high       low       low    unordered base data
  B-tree         low        medium    medium OLTP indexes, primary keys
  LSM-tree       medium     low       medium write-heavy key-value stores
  column store   low*       high      low    analytics (*for scans of few columns)
```

Read storage layouts first: they introduce pages, the buffer pool and the row/column choice that every index sits on. B-trees and LSM-trees are then two opposite answers to keeping data ordered by key on block devices, one optimising reads and the other writes.

## Connections to sibling areas

- **[Data Models](../01-data-models/README.md):** physical data independence lets this layer change (add an index, switch to columns) without changing queries.
- **[Query Processing](../03-query-processing/README.md):** the optimizer chooses among access paths (scan, index lookup, index range scan) by estimating their page costs; indexes make some joins cheap.
- **[Transactions](../04-transactions/README.md):** page-level logging and latching protect these structures during concurrent updates and crashes; LSM-trees and multiversion storage simplify some of that work by never overwriting.

## Connections across layers

The cost model is the [external-memory model](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md); devices are described in [DRAM and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md); the buffer pool is a [page-replacement](../../07-operating-systems/04-memory-management/page-replacement.md) cache that often bypasses the Operating System (OS)'s own. File systems themselves use B-trees and logs ([file system implementation](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md)). Above, the same structures appear in distributed stores ([partitioning](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md)) and in analytical engines for [batch processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md).

## Cross-cutting threads

- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): the buffer pool keeps hot pages in memory; B-tree upper levels almost always hit.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): LSM-trees batch writes into sequential runs.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): read, write and space amplification cannot all be minimised.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): row vs column layout and compression decide which queries are cheap.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): B-tree balance and sorted order are maintained by every operation.
