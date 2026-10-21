# Storage Layouts

> **Layer:** [09 Data Management](../README.md) › [Storage and Indexing](README.md)
> **Builds on:** [DRAM and Storage Devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md), [File System Implementation](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md), [Page Replacement](../../07-operating-systems/04-memory-management/page-replacement.md), [External Memory and Cache-Oblivious Algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md)
> **Enables:** [B-Trees](b-trees.md), [LSM-Trees](lsm-trees.md), [Join Algorithms](../03-query-processing/join-algorithms.md), [Recovery and Logging](../04-transactions/recovery-and-logging.md)

## Essence

A database stores relations as records packed into fixed-size pages (typically 4–16 KB), and pages into files or raw device regions. Pages are the unit of transfer between storage and memory, and a buffer pool in memory caches the pages in use. The key layout decision is which values share a page. A row store keeps each record's attributes together, so fetching or updating one record touches one page. A column store keeps each attribute's values together, so a query that reads three columns of a billion rows touches only those columns and compresses them well. Transactional systems choose rows; analytical systems choose columns.

## Core tenets

1. **Cost is measured in page transfers because devices are block-oriented.** A Solid-State Drive (SSD) or disk reads a whole page at roughly the same cost as one byte, and random access is far costlier than sequential: on a hard disk, ~100 random reads per second versus ~100+ MB/s sequential; on an SSD, the gap is smaller but still large. Database algorithms are therefore designed and analysed in the external-memory model: minimise the number of blocks moved.

2. **Slotted pages hold variable-length records.** A page header holds a slot array of offsets; records grow from the other end of the page. A Record Identifier (RID) is (page number, slot number). Records can move within a page (when resized or compacted) without changing their RID, because only the slot entry changes. This is indirection used to keep references stable.

3. **A heap file is the default, unordered table.** Records go wherever there is space. Inserts are cheap; finding a record by value requires a full scan. Indexes (B-trees, hash indexes) are separate structures mapping key values to Record Identifiers (RIDs). A *clustered* (or index-organised) table instead stores the records in key order inside the index itself, making range scans on that key sequential.

4. **The buffer pool is the database's own cache.** It holds a fixed number of page frames, maps page identifiers to frames with a hash table, pins pages in use and evicts unpinned ones with a Least Recently Used (LRU)-like policy. Databases often bypass the Operating System (OS) page cache (with direct Input/Output (I/O)) because they know their access patterns better (a sequential scan should not evict the hot index root) and must control exactly when dirty pages reach disk for recovery.

5. **Row stores suit transactions; column stores suit analytics.** Online Transaction Processing (OLTP) reads and writes a few whole records at a time, so a row layout touches one page per record. Online Analytical Processing (OLAP) scans many rows but few columns ("average price by region over the last year"), so a column layout reads only the needed columns. With 100 columns and a query touching 3, a column store reads roughly 3% of the data.

6. **Columns compress dramatically.** Values in one column share a type and often repeat or sort well, so run-length encoding, dictionary encoding and bit-packing commonly shrink data 5–10×. Compression trades cheap Central Processing Unit (CPU) work for scarce I/O bandwidth, and many operators can work directly on compressed data.

7. **Columnar execution exploits the processor.** Processing a column as a tight loop over an array of same-typed values uses Single Instruction, Multiple Data (SIMD) instructions and keeps caches and branch predictors happy. Vectorised engines process batches of a few thousand values per operator call, amortising interpretation overhead. Updating single rows in a column store is costly, so writes are usually buffered and merged in bulk.

8. **Hybrid and in-memory layouts blur the line.** Some systems keep a row-oriented write store and a column-oriented read store and merge between them. When the working set fits in Dynamic Random-Access Memory (DRAM), page-based indirection costs more than it saves and in-memory engines use pointers and cache-conscious structures instead; but durability still needs a log on persistent storage.

## Key concepts

| Term | Meaning |
|---|---|
| Page / block | Fixed-size unit of storage I/O and buffering |
| Slotted page | Page with an offset array allowing variable-length, movable records |
| RID | Record identifier: (page, slot) |
| Heap file | Unordered collection of pages holding a table's records |
| Clustered index | Table stored in index key order |
| Buffer pool | Database-managed in-memory cache of pages |
| Pin / dirty | Page in use and must not be evicted / page modified in memory |
| Row store (NSM) | N-ary Storage Model: all attributes of a record together |
| Column store (DSM) | Decomposition Storage Model: each attribute stored separately |
| Vectorised execution | Operators processing batches of column values per call |

## How it fits

- **Below:** device behaviour comes from [DRAM and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md); the cost model from [external-memory algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md); the buffer pool reimplements [page replacement](../../07-operating-systems/04-memory-management/page-replacement.md) and sits on or beside [file system implementation](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md). Column execution exploits [SIMD](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md).
- **Above:** indexes ([B-trees](b-trees.md), [LSM-trees](lsm-trees.md)) organise pages by key; [join algorithms](../03-query-processing/join-algorithms.md) are designed around buffer pool size; [recovery](../04-transactions/recovery-and-logging.md) controls when dirty pages may be written.
- **Siblings:** B-trees and LSM-trees are two ways to impose key order on these pages.

## Common misconceptions

- **"The OS page cache makes a buffer pool unnecessary."** The database needs control over eviction and write ordering for performance and for correct recovery; double caching also wastes memory.
- **"Column stores are just transposed tables."** Their advantage comes from compression and vectorised execution as much as from reading fewer bytes.
- **"SSDs make layout irrelevant."** SSDs narrow the random/sequential gap but still read in pages and wear out with writes, so layout and write patterns still matter.

## Go deeper

- J. M. Hellerstein, M. Stonebraker, J. Hamilton, *Architecture of a Database System* (2007): how real engines are organised, including the buffer pool.
- D. J. Abadi, S. R. Madden, N. Hachem, *Column-Stores vs. Row-Stores: How Different Are They Really?* (SIGMOD 2008): where column store speedups come from.
- P. Boncz, M. Zukowski, N. Nes, *MonetDB/X100: Hyper-Pipelining Query Execution* (CIDR 2005): vectorised execution.
