# Crash Consistency and Journaling

> **Layer:** [07 Operating Systems](../README.md) › [Storage and file systems](README.md)
> **Builds on:** [File system implementation](file-system-implementation.md), [Correctness and invariants](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md), [Reliability and redundancy](../../00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md)
> **Enables:** [Recovery and logging](../../09-data-management/04-transactions/recovery-and-logging.md), [ACID](../../09-data-management/04-transactions/acid.md), [LSM-trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md), [Replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md)

## Essence

Most file system operations change several blocks: appending to a file updates a data block, the inode (size, block map) and the free-space bitmap. A device writes blocks one at a time and may lose power between any two, so a crash can leave the on-disk structure inconsistent: a block marked used but owned by no file, or an inode pointing at garbage. **Crash consistency** is the guarantee that after any crash the structure can be returned to a state that some sequence of complete operations would have produced. The dominant technique is **journaling** (write-ahead logging): first write a description of the whole update to a log, then apply it in place, so recovery can replay or discard it. Copy-on-write and log-structured designs reach the same goal by never overwriting live data.

## Core tenets

1. **Atomicity across blocks must be constructed; the device gives at most single-sector atomicity.** Drives guarantee (at best) that a single 512-byte or 4 KiB sector write is all-or-nothing. Any invariant spanning blocks (bitmap agrees with inodes, directory entries point at allocated inodes) can be broken by a crash in mid-update. The file system's job is to build multi-block atomic updates from single-block ones, the same problem databases solve for transactions.

2. **The old answer was to repair after the fact.** Early Unix file systems wrote in place and ran `fsck` at boot to scan every inode, bitmap and directory, find inconsistencies and fix them. This only restores *metadata* consistency (it cannot know what data was intended), and its cost grows with disk size: hours on multi-terabyte volumes. It was abandoned as the default when disks grew.

3. **Journaling turns many writes into one atomic commit.** To update blocks B1..Bn: write their new contents (or a description) into the journal, then write a commit record, wait for it to reach the device, then *checkpoint* by writing B1..Bn to their home locations, then mark the journal entry free. If a crash happens before the commit record is durable, recovery ignores the partial entry; after it, recovery replays the entry. Either way, the update is all or nothing. ext3/ext4, XFS and NTFS all journal.

   ```
   journal: [TxBegin | B1' | B2' | B3'] --flush--> [TxCommit] --flush--> write B1',B2',B3' home --> free tx
   crash before commit durable: discard     crash after: replay
   ```

4. **Ordering, enforced by flushes, is what makes a journal correct.** The commit record must not reach the platter before the blocks it commits, or recovery would replay garbage. Devices reorder writes in their caches for speed, so the file system issues cache-flush or Force Unit Access (FUA) commands as barriers. A device that ignores flushes (some consumer drives have) silently defeats journaling. This is the persistence analogue of a memory fence.

5. **Most file systems journal only metadata, by default, to save bandwidth.** Full data journaling writes every data block twice. ext4's default *ordered* mode journals only metadata but writes the data blocks to their final location *before* committing the metadata that points to them, so a file never points at stale blocks. The structure stays consistent, but recently written file *contents* may still be lost, which is why applications need `fsync`.

6. **Copy-on-write file systems never overwrite live data.** ZFS, Btrfs and Apple's APFS write every modified block to a new location, then update parents up to the root, and finally switch the root pointer (the uberblock in ZFS) atomically. The old tree remains valid until the switch, so a crash simply leaves the previous consistent version. Snapshots come almost free: keep an old root. The costs are fragmentation and write amplification up the tree.

7. **Log-structured file systems make the log the only copy.** Rosenblum and Ousterhout's Log-structured File System (LFS, 1991) wrote all changes sequentially to a log and never updated in place, turning random writes into sequential ones at full disk bandwidth; a cleaner reclaims space from obsolete segments. The idea fits flash, which cannot overwrite in place: Solid-State Drive (SSD) firmware, Samsung's F2FS and the Log-Structured Merge-trees (LSM-trees) of databases like RocksDB are all log-structured.

8. **The file system's guarantee ends where the application's begins.** A consistent file system can still hold an application file that is half old and half new. Applications must build their own atomic updates on the primitives the file system offers: `fsync` for ordering and durability, `rename` for atomic replacement, or their own write-ahead log (as SQLite and PostgreSQL do). This is the [end-to-end argument](../../CROSS-CUTTING.md#the-end-to-end-argument): only the application knows what "consistent" means for its data.

## Key concepts

| Term | Meaning |
|---|---|
| Crash consistency | After any crash, on-disk state can be made equivalent to some sequence of complete operations |
| `fsck` | File system checker that scans and repairs metadata after a crash |
| Journal (write-ahead log) | Area where updates are recorded and committed before being applied in place |
| Commit record | The single-block write that makes a journal transaction durable |
| Checkpoint | Writing journaled blocks to their home locations and freeing the log space |
| Ordered mode | Data written before the metadata that refers to it is committed |
| Copy-on-write (COW) | Never overwrite live blocks; write new copies and switch a root pointer |
| Log-structured file system | All writes appended to a log, which is the only copy of the data |
| Write barrier / flush | Device command ensuring earlier writes are durable before later ones |

## How it fits

- **Below:** relies on device guarantees about sector atomicity and flush ordering ([DRAM and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md)) and on stating [invariants](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md) that must survive any crash point.
- **Above:** databases use the same write-ahead principle for transactions ([recovery and logging](../../09-data-management/04-transactions/recovery-and-logging.md), [ACID](../../09-data-management/04-transactions/acid.md)); log-structured storage became [LSM-trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md); replicated logs are the heart of [replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md).
- **Siblings:** protects the structures described in [file system implementation](file-system-implementation.md) and gives meaning to the durability promises in [file system abstractions](file-system-abstractions.md).

## Common misconceptions

- **"A journaling file system never loses data."** It keeps metadata consistent; in the default ordered mode, recent file contents not yet `fsync`ed can be lost.
- **"Journaling halves write performance."** Metadata-only journaling adds little; the journal is written sequentially and checkpoints are batched.
- **"Copy-on-write file systems do not need `fsync`."** They guarantee a consistent snapshot, but the latest writes are durable only after the next commit, which `fsync` forces.

## Go deeper

- Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (2018), "Crash Consistency: FSCK and Journaling" and "Log-structured File Systems".
- Mendel Rosenblum and John K. Ousterhout, "The Design and Implementation of a Log-Structured File System" (1991).
- Vijayan Prabhakaran, Andrea C. Arpaci-Dusseau and Remzi H. Arpaci-Dusseau, "Analysis and Evolution of Journaling File Systems" (USENIX ATC 2005).
- C. Mohan et al., "ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging" (1992): the database counterpart.
