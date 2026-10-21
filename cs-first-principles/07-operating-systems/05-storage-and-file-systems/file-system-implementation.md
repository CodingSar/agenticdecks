# File System Implementation

> **Layer:** [07 Operating Systems](../README.md) › [Storage and file systems](README.md)
> **Builds on:** [File system abstractions](file-system-abstractions.md), [DRAM and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md), [Search trees](../../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md), [Page replacement](../04-memory-management/page-replacement.md)
> **Enables:** [Crash consistency and journaling](crash-consistency-and-journaling.md), [B-trees](../../09-data-management/02-storage-and-indexing/b-trees.md), [LSM-trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md)

## Essence

A file system implementation is a data structure laid out on a block device. Its core pieces are a **superblock** describing the whole file system, **allocation maps** recording which blocks and inodes are free, **inodes** holding each file's metadata and a map from file offsets to disk blocks, **directories** stored as files of name-to-inode entries, and the **data blocks** themselves. Performance comes from two forces: storage is orders of magnitude slower than memory, so the kernel caches aggressively in the **page cache**; and storage strongly favours large sequential transfers, so good implementations keep related blocks together and describe files with **extents** (contiguous runs) rather than individual block pointers.

## Core tenets

1. **Every file system is a tree of indirection from names to blocks.** Resolving `/a/b` reads the root directory's inode, then its data to find `a`'s inode number, then `a`'s data to find `b`, then `b`'s inode, then its block map. Each step may be a device read, so path lookups are cached in memory (Linux's dentry cache) and recently used inodes stay resident.

   ```
   superblock | block bitmap | inode bitmap | inode table | data blocks ...
   inode 2 (/) -> dir block {"a": 12} -> inode 12 -> dir block {"b": 31} -> inode 31 -> extents
   ```

2. **The block map must handle tiny and huge files efficiently.** The classic Unix inode holds 12 direct block pointers plus single, double and triple indirect pointers, so small files (the large majority by count) need no extra reads while files of terabytes remain addressable. Modern file systems (ext4, XFS, NTFS, APFS) use *extents*, pairs of (start block, length), often stored in a B-tree, so a contiguous 1 GiB file needs a handful of entries rather than 262,144 pointers.

3. **Layout follows the device's physics.** On a Hard Disk Drive (HDD) a random access costs ~5–10 ms of seek and rotation while sequential transfer runs at ~100–250 MB/s, so a random 4 KiB read is about a thousand times slower per byte than streaming. The Berkeley Fast File System (FFS, 1984) introduced cylinder groups that put a file's inode, its data and its directory near each other. Solid-State Drives (SSDs) have no seek, but write in pages and erase in much larger blocks, and their Flash Translation Layer (FTL) remaps writes internally; they still favour large, aligned, sequential writes and benefit from `TRIM` hints about freed blocks.

4. **Free-space management trades allocation speed against fragmentation.** Bitmaps (one bit per block) are compact and make finding contiguous runs straightforward; extent trees of free space scale better on very large volumes. *Delayed allocation* (ext4, XFS) waits until writeback to choose blocks, when the file's final size is better known, which yields more contiguous files.

5. **The page cache is where most file I/O actually happens.** Reads are served from cached pages when possible, and the kernel reads ahead when it detects sequential access. Writes dirty pages in memory and return; background writeback flushes them later, coalescing many small writes into fewer large ones. In Linux the page cache is unified with virtual memory, so the same frames serve `read`, `mmap` and executable loading, and [page replacement](../04-memory-management/page-replacement.md) decides which file pages stay.

6. **A virtual file system layer lets many implementations share one interface.** Linux's Virtual File System (VFS) defines generic objects (superblock, inode, dentry, file) with operation tables that each concrete file system (ext4, XFS, Btrfs, NFS client, `procfs`, Filesystem in Userspace (FUSE)) fills in. System calls operate on the generic objects, so programs work identically on any of them. This is [interface vs implementation](../../CROSS-CUTTING.md#interface-vs-implementation) at kernel scale; Windows NT achieves the same with its I/O manager and file system drivers.

7. **Integrity needs end-to-end checksums because devices fail silently.** Disks and SSDs occasionally return wrong data without reporting an error (bit rot, misdirected writes, firmware bugs). Traditional file systems trust the device. ZFS and Btrfs store a checksum of every block in its parent pointer, so corruption is detected on read and, with redundant copies (mirroring or parity), repaired automatically.

8. **Redundancy across devices is a separate layer or built in.** Redundant Array of Independent Disks (RAID) combines devices for capacity, speed (striping) or survival of failures (mirroring, parity). It can sit below the file system as a block device (Linux md) or be integrated, as in ZFS, where the file system knows which blocks are live and can rebuild only those.

## Key concepts

| Term | Meaning |
|---|---|
| Superblock | Block describing the file system's size, layout and state |
| Inode | Per-file metadata and map from file offsets to blocks |
| Extent | A contiguous run of blocks described by start and length |
| Indirect block | A block of pointers to further blocks, extending an inode's map |
| Bitmap | One bit per block or inode recording allocated or free |
| Page cache | In-memory cache of file data, unified with virtual memory |
| Read-ahead | Prefetching file blocks on detecting sequential access |
| VFS | Virtual File System: the kernel's generic file interface |
| Checksum | Hash of a block's contents used to detect corruption |

## How it fits

- **Below:** shaped by device characteristics ([DRAM and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md)) and uses tree structures from [search trees](../../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md) and [external-memory algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md).
- **Above:** databases make the same layout choices ([B-trees](../../09-data-management/02-storage-and-indexing/b-trees.md), [LSM-trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md), [storage layouts](../../09-data-management/02-storage-and-indexing/storage-layouts.md)); distributed file systems and object stores extend it across machines ([partitioning](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md), [replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md)).
- **Siblings:** realizes [file system abstractions](file-system-abstractions.md); [crash consistency and journaling](crash-consistency-and-journaling.md) makes multi-block updates to these structures survive crashes.

## Common misconceptions

- **"SSDs make layout irrelevant."** They remove seek cost but not write amplification, erase-block granularity or the benefits of large sequential I/O.
- **"A directory is a special list maintained by the kernel."** It is a file of entries, often indexed (ext4's hashed B-tree "htree") so lookup in a directory of millions of names stays fast.
- **"RAID is a backup."** RAID survives device failure, but faithfully replicates deletions, corruption from software bugs and ransomware.

## Go deeper

- Marshall K. McKusick, William N. Joy, Samuel J. Leffler and Robert S. Fabry, "A Fast File System for UNIX" (1984).
- Jeff Bonwick et al., "The Zettabyte File System" (2003): end-to-end checksums and pooled storage.
- Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (2018), "File System Implementation" and "Locality and The Fast File System".
