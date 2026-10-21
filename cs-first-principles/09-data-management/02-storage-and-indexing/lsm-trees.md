# LSM-Trees

> **Layer:** [09 Data Management](../README.md) › [Storage and Indexing](README.md)
> **Builds on:** [Storage Layouts](storage-layouts.md), [B-Trees](b-trees.md), [Comparison Sorting](../../05-algorithms-and-data-structures/04-sorting-and-searching/comparison-sorting.md), [Randomized Algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md), [DRAM and Storage Devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md)
> **Enables:** [Non-Relational Models](../01-data-models/non-relational-models.md), [Recovery and Logging](../04-transactions/recovery-and-logging.md), [Partitioning](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md)

## Essence

A Log-Structured Merge-tree (LSM-tree) makes writes cheap by never updating data in place. New writes go to a sorted in-memory buffer (the memtable) and to a sequential log for durability. When the buffer fills, it is written out as an immutable sorted file (a Sorted String Table, SSTable). Background *compaction* merges these files into larger sorted runs, discarding overwritten and deleted values. Every device write is therefore a large sequential write, which is what disks and flash do best. Reads pay the price: a key may be in the memtable or in any of several files, so reads consult several places, helped by in-memory indexes and Bloom filters. Bigtable, LevelDB, RocksDB, Cassandra and HBase are all built this way.

## Core tenets

1. **Turn random writes into sequential writes by buffering and sorting.** Updating a B-tree in place dirties a random page for each random key. An LSM-tree absorbs thousands of writes in memory, sorts them, and writes them as one sequential file. On hard disks sequential bandwidth is ~100× random; on Solid-State Drives (SSDs) sequential writes also reduce internal garbage collection and wear. This is batching and amortisation applied to storage.

2. **Immutability simplifies concurrency and recovery.** Once an SSTable is written, it never changes. Readers need no locks on it; crash recovery only needs to replay the write-ahead log into a fresh memtable; snapshots are just a list of files. Deletion is a write too: a *tombstone* marking the key deleted, removed only when compaction proves no older version survives below it.

3. **Reads merge across levels, newest first.** A point lookup checks the memtable, then each SSTable from newest to oldest, stopping at the first hit. A range scan merges sorted iterators over all relevant files, the k-way merge step of merge sort. More files mean more work per read.

4. **Bloom filters avoid most useless reads.** Each SSTable carries a Bloom filter: a bit array plus k hash functions that answers "definitely not here" or "maybe here". With about 10 bits per key the false-positive rate is about 1%, so a point lookup for a key in only one file touches roughly one file's data on device. Filters do not help range scans.

5. **Compaction policy sets the read/write/space balance.** *Leveled* compaction (LevelDB, RocksDB default) keeps each level a single sorted run about 10× larger than the previous, giving few files per lookup and little dead space but rewriting data many times (write amplification of 10–30×). *Tiered* (size-tiered) compaction merges several similar-sized runs at once, writing each byte fewer times but leaving more runs to search and more temporary space. No policy minimises all three amplifications.

6. **Write amplification is the hidden cost.** Each logical byte written may be rewritten at every level it passes through. On flash, this consumes device endurance and bandwidth. Compaction also competes with foreground work for Input/Output (I/O), producing latency spikes if it falls behind; production systems throttle writes when compaction debt grows.

7. **LSM-trees and B-trees occupy opposite corners of the trade-off.** B-trees: about one read per lookup, in-place writes with higher random I/O. LSM-trees: more read work, much lower write cost, better compression (files are dense and immutable). Write-heavy workloads (logging, time series, messaging, large key-value stores) favour LSM; read-heavy transactional workloads with range scans have traditionally favoured B-trees.

8. **The idea generalises: logs as the primary data structure.** The log-structured file system (Rosenblum and Ousterhout, 1991) applied the same idea to file systems; flash translation layers inside SSDs do it in firmware; replicated logs are the basis of distributed databases. Whenever writes are expensive to place, write them sequentially first and organise later.

## Key concepts

| Term | Meaning |
|---|---|
| Memtable | In-memory sorted buffer receiving new writes |
| SSTable | Immutable on-disk file of sorted key-value pairs with an index |
| Write-ahead log | Sequential log ensuring memtable contents survive crashes |
| Compaction | Background merge of sorted runs, discarding stale versions |
| Tombstone | Marker recording that a key was deleted |
| Bloom filter | Probabilistic set membership test with no false negatives |
| Leveled compaction | One sorted run per level, levels growing geometrically |
| Size-tiered compaction | Merge several runs of similar size into one larger run |
| Read / write / space amplification | Extra reads, writes and storage relative to the logical data |

## How it fits

- **Below:** sorting and k-way merge from [comparison sorting](../../05-algorithms-and-data-structures/04-sorting-and-searching/comparison-sorting.md); Bloom filters from [randomized algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md); motivated by device asymmetries in [DRAM and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md); built from the pages and files of [storage layouts](storage-layouts.md).
- **Above:** the storage engine of most wide-column and key-value [non-relational stores](../01-data-models/non-relational-models.md); its write-ahead log follows the rules of [recovery and logging](../04-transactions/recovery-and-logging.md); sorted runs split naturally into key ranges for [partitioning](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md).
- **Siblings:** [B-trees](b-trees.md) are the read-optimised alternative; many systems use both (an LSM-tree for primary data, B-tree-like indexes inside each SSTable).

## Common misconceptions

- **"LSM-trees are always faster for writes."** Their sustained write rate is limited by compaction throughput; if compaction falls behind, writes stall.
- **"Deletes free space immediately."** A delete adds a tombstone; space is reclaimed only after compaction reaches the oldest copy.
- **"Bloom filters make LSM reads as cheap as B-tree reads."** They help point lookups for keys in few files, but range scans and lookups of recently overwritten keys still touch several runs.

## Go deeper

- P. O'Neil, E. Cheng, D. Gawlick, E. O'Neil, *The Log-Structured Merge-Tree (LSM-Tree)* (Acta Informatica, 1996): the original design and analysis.
- M. Rosenblum, J. K. Ousterhout, *The Design and Implementation of a Log-Structured File System* (SOSP 1991): the same idea for file systems.
- B. H. Bloom, *Space/Time Trade-offs in Hash Coding with Allowable Errors* (1970): the filter that makes LSM reads practical.
