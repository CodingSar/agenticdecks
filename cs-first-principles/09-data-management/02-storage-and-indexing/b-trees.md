# B-Trees

> **Layer:** [09 Data Management](../README.md) › [Storage and Indexing](README.md)
> **Builds on:** [Search Trees](../../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md), [Storage Layouts](storage-layouts.md), [External Memory and Cache-Oblivious Algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md), [Correctness and Invariants](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md)
> **Enables:** [Query Optimization](../03-query-processing/query-optimization.md), [Join Algorithms](../03-query-processing/join-algorithms.md), [Concurrency Control](../04-transactions/concurrency-control.md), [File System Implementation](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md)

## Essence

A B-tree is a balanced search tree whose nodes are disk pages, each holding hundreds of keys and child pointers. Because every node has so many children, the tree is extremely shallow: a few levels index billions of keys, so any lookup costs a handful of page reads, and the top levels almost always sit in memory. Nodes split when full and merge when sparse, keeping every leaf at the same depth. The B+-tree variant, used by nearly every relational database, stores all records (or record pointers) in leaves linked in key order, so range scans become sequential leaf walks. Since 1970 it has been the default index for data that must support point lookups, range queries and in-place updates.

## Core tenets

1. **High fan-out makes trees shallow, and shallowness is what matters on block devices.** A binary tree over 10^9 keys has depth ~30, each level potentially a separate page read. A B-tree node of 16 KB holding ~500 keys has depth log_500(10^9) ≈ 3.3, so four levels suffice. Since a page read costs the same whether it holds 1 key or 500, packing a node to the page size minimises I/O per lookup: O(log_B N) transfers, where B is keys per page.

2. **Balance is maintained by splitting and merging at the leaves upward.** Insert into the correct leaf; if it overflows, split it into two half-full nodes and insert the separator key into the parent, which may split in turn. When the root splits, the tree grows one level, at the top. So all leaves stay at the same depth without any rotations. Deletions borrow from or merge with siblings to keep nodes at least half full (many systems relax this and let nodes underflow).

3. **The invariant is ordered keys with separators bounding subtrees.** Within a node, keys are sorted; for separator k_i between children c_i and c_{i+1}, every key in c_i is less than k_i and every key in c_{i+1} is greater or equal. Search at each node is a binary search within the page, then descent into one child. Every operation must restore this invariant before it finishes.

4. **B+-trees put data only in leaves and chain the leaves.** Interior nodes hold only separator keys and pointers, maximising fan-out. Leaves hold keys with records or Record Identifiers (RIDs), and each leaf points to its right neighbour. A range query `WHERE x BETWEEN a AND b` descends once to `a` and then walks leaves until `b`, reading consecutive pages.

5. **Clustered vs secondary indexes differ in what the leaves hold.** A clustered (primary) index stores the rows themselves in key order, so a range scan reads contiguous data. A secondary index stores (key, pointer) pairs; each matching entry may require a random read of the base table. That is why a query matching 20% of rows through a secondary index can be slower than a full sequential scan, and why optimizers estimate selectivity before choosing an index.

6. **Upper levels are almost always cached.** With fan-out 500, the root and second level together are ~500 pages (~8 MB at 16 KB per page), which stay in the buffer pool. A point lookup in a billion-row table typically needs one or two actual device reads.

7. **In-place updates make B-trees read-optimised and write-costly.** Changing one 100-byte record rewrites a whole page (write amplification), and random inserts dirty random pages. Durability needs a write-ahead log in addition to the page writes. Concurrency needs latch protocols (latch crabbing, or B-link trees with right-sibling pointers) so that splits do not corrupt concurrent searches. These costs motivate LSM-trees for write-heavy workloads.

8. **Prefix and suffix tricks extend fan-out.** Interior separators only need to distinguish subtrees, so they can be truncated to the shortest distinguishing prefix. Leaf keys sharing a prefix can be compressed. Every byte saved raises fan-out and lowers height.

## Key concepts

| Term | Meaning |
|---|---|
| Fan-out | Number of children per interior node; hundreds in practice |
| Order / B | Maximum keys or children per node, set by page size |
| Split / merge | Restructuring when a node overflows / underflows |
| B+-tree | B-tree variant with data only in leaves and linked leaves |
| Separator key | Interior key routing searches to the correct child |
| Clustered index | Index whose leaves store the table rows in key order |
| Secondary index | Index whose leaves store pointers to rows stored elsewhere |
| Selectivity | Fraction of rows a predicate matches |
| Latch crabbing | Acquiring child latch before releasing parent during traversal |
| Write amplification | Bytes written to storage per byte of logical update |

## How it fits

- **Below:** a generalisation of balanced [search trees](../../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md) to the [external-memory model](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md); nodes are [slotted pages](storage-layouts.md) in the buffer pool; correctness rests on [maintained invariants](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md).
- **Above:** index access paths are the main choices in [query optimization](../03-query-processing/query-optimization.md); index nested-loop joins use them ([join algorithms](../03-query-processing/join-algorithms.md)); key-range locks in [concurrency control](../04-transactions/concurrency-control.md) lock B-tree intervals. File systems such as XFS, Btrfs and NTFS also use B-tree variants ([file system implementation](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md)).
- **Siblings:** [LSM-trees](lsm-trees.md) trade read cost for much cheaper writes; [storage layouts](storage-layouts.md) supply pages and the buffer pool.

## Common misconceptions

- **"B stands for binary."** It does not; Bayer and McCreight never said what B stands for, and B-trees are deliberately far from binary.
- **"An index always speeds up a query."** For low-selectivity predicates through a secondary index, random lookups can be slower than a full scan, and every index slows writes.
- **"B-tree lookups cost O(log N) disk reads."** They cost O(log_B N), with B in the hundreds, and the top levels are cached, so in practice one to three reads.

## Go deeper

- R. Bayer, E. McCreight, *Organization and Maintenance of Large Ordered Indexes* (1972): the original B-tree paper.
- D. Comer, *The Ubiquitous B-Tree* (ACM Computing Surveys, 1979): classic survey of variants.
- G. Graefe, *Modern B-Tree Techniques* (Foundations and Trends in Databases, 2011): concurrency, recovery and compression in real systems.
- P. L. Lehman, S. B. Yao, *Efficient Locking for Concurrent Operations on B-Trees* (1981): B-link trees.
