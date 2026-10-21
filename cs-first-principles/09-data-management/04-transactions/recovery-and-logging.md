# Recovery and Logging

> **Layer:** [09 Data Management](../README.md) › [Transactions](README.md)
> **Builds on:** [ACID](acid.md), [Storage Layouts](../02-storage-and-indexing/storage-layouts.md), [Crash Consistency and Journaling](../../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md), [DRAM and Storage Devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md)
> **Enables:** [Replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md), [Distributed Transactions](../../10-distributed-and-parallel-computing/04-distributed-data/distributed-transactions.md), [Batch and Stream Processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md)

## Essence

Recovery provides atomicity and durability when the system crashes and loses everything in memory. The core tool is the write-ahead log (WAL): before any change to a data page reaches disk, a log record describing that change must reach disk first, and before a transaction is reported committed, all its log records must be on disk. After a crash, the system replays the log to *redo* changes of committed transactions whose pages had not yet been written, and *undo* changes of uncommitted transactions whose pages had been written. This lets the buffer pool write pages whenever convenient, while turning the commit itself into one cheap sequential log append.

## Core tenets

1. **The buffer pool creates the problem.** For speed, updated pages stay in memory and are written later. A crash can therefore leave committed changes missing from disk, and, if the buffer pool wrote a page early to free a frame, uncommitted changes present on disk. Recovery must fix both.

2. **Two policy choices define the recovery work.** *Steal*: may a page with uncommitted changes be written to disk? If yes, recovery needs undo. *Force*: must all pages a transaction changed be written before it commits? If no, recovery needs redo. Steal/no-force gives the buffer pool maximum freedom and commit maximum speed, and needs both undo and redo. It is what nearly all serious databases choose.

3. **The write-ahead rule makes undo and redo possible.** (a) A log record for a change must be on disk before the changed page is. (b) All of a transaction's log records, including its commit record, must be on disk before commit is acknowledged. Each log record carries a Log Sequence Number (LSN), and each page remembers the LSN of the last change applied to it, so recovery can tell whether a change is already on the page.

4. **Commit cost becomes a sequential log flush.** Instead of writing scattered data pages at commit, the system appends a few records to the log tail and flushes it. *Group commit* batches commits from many concurrent transactions into one flush, so a device that can do a few thousand flushes per second supports far more commits per second.

5. **ARIES recovers in three passes.** The Algorithm for Recovery and Isolation Exploiting Semantics (ARIES, Mohan et al., 1992) is the standard design. *Analysis* scans from the last checkpoint to find which transactions were active and which pages might be dirty. *Redo* repeats history: it reapplies every logged change not yet on its page, including changes by transactions that will be undone, restoring the exact pre-crash state. *Undo* then rolls back losers in reverse order, writing compensation log records so that a crash during recovery does not undo work twice.

6. **Checkpoints bound recovery time.** Without them, recovery would replay the whole log from the beginning. A fuzzy checkpoint records the active transactions and dirty pages without stopping the system; recovery starts from it. Checkpoint frequency trades steady-state overhead against restart time.

7. **Physical, logical and physiological logging trade size for flexibility.** Physical logging records byte changes on a page (simple, idempotent, large). Logical logging records operations ("insert key k into index I") (compact, but replay must be careful about structure). ARIES uses *physiological* logging: a record names a page, and describes a logical change within it, which is compact and still redoable page by page.

8. **The log is the database's ground truth.** Data pages are a cache of the log's effects. This view underlies replication (ship the log to replicas and replay it), point-in-time recovery (replay up to a chosen moment), change data capture (stream the log to other systems) and LSM-trees (where the log plus sorted runs is the storage). Durability against device loss comes from copying the log elsewhere.

9. **Durability depends on the storage stack telling the truth.** Flushing the log means calling fsync or using direct, synchronous writes and trusting that drive caches honour flush commands. Bugs and misconfigurations at the OS (Operating System) or device layer have caused committed data loss in production databases; PostgreSQL's 2018 discovery that failed fsync calls could silently drop dirty pages is a well-known example.

## Key concepts

| Term | Meaning |
|---|---|
| WAL | Write-ahead log: log record reaches disk before the data it describes |
| Steal / no-steal | Uncommitted changes may / may not be written to disk |
| Force / no-force | Pages must / need not be written at commit |
| Undo / redo | Reverse uncommitted changes / reapply committed ones |
| LSN | Log Sequence Number, a monotonically increasing log position |
| pageLSN | LSN of the last change applied to a page |
| Checkpoint | Recorded state that bounds how far back recovery must read |
| ARIES | Analysis, redo (repeating history), undo with compensation records |
| CLR | Compensation Log Record: logs an undo action so it is never repeated |
| Group commit | One log flush shared by many committing transactions |

## How it fits

- **Below:** the same idea as file system [journaling](../../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md), applied with transaction semantics; depends on [storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md) honouring flush ordering; interacts with the buffer pool of [storage layouts](../02-storage-and-indexing/storage-layouts.md). Implements the A and D of [ACID](acid.md).
- **Above:** log shipping is the basis of [replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md); the prepare phase of two-phase commit in [distributed transactions](../../10-distributed-and-parallel-computing/04-distributed-data/distributed-transactions.md) is a forced log write; log-centric architectures feed [stream processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md).
- **Siblings:** [concurrency control](concurrency-control.md) must keep locks on a transaction's writes until undo is no longer possible; [ACID](acid.md) states the guarantees this leaf delivers.

## Common misconceptions

- **"Committing writes the changed rows to disk."** It writes log records; the data pages are written later, possibly much later.
- **"Recovery just undoes incomplete transactions."** With no-force it must also redo committed work, and ARIES redoes everything before undoing.
- **"The log is only for crashes."** It also drives replication, backups, auditing and change streams.

## Go deeper

- C. Mohan, D. Haderle, B. Lindsay, H. Pirahesh, P. Schwarz, *ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging* (ACM TODS, 1992): the standard algorithm.
- T. Härder, A. Reuter, *Principles of Transaction-Oriented Database Recovery* (1983): the steal/force taxonomy.
- J. Gray, A. Reuter, *Transaction Processing: Concepts and Techniques* (1993): logging and recovery in full detail.
