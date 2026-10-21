# Storage and File Systems

> **Layer:** [07 Operating Systems](../README.md) › Storage and file systems
> **Children:** [File system abstractions](file-system-abstractions.md) · [File system implementation](file-system-implementation.md) · [Crash consistency and journaling](crash-consistency-and-journaling.md)

## What this area is about

This area is the Operating System's (OS's) third job: **persistence**. Memory forgets everything when power fails; storage devices remember, but only as a flat array of fixed-size blocks with no names, no structure, no protection and no guarantee about which writes survive a crash. A file system turns that array into a hierarchy of named, protected, growable files that many programs can share, and that remain consistent even if the machine loses power halfway through an update.

The unifying idea is that a file system is an **on-disk data structure** (trees of metadata pointing at data blocks) that must be fast to traverse, cheap to update, and **always recoverable**: every sequence of block writes the device might complete before a crash must leave a structure that can be repaired to a consistent state.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [File system abstractions](file-system-abstractions.md) | The interface: files, directories, paths, descriptors, permissions, and what `write` and `fsync` promise | [Kernel mode and system calls](../01-kernel-and-abstractions/kernel-mode-and-system-calls.md) |
| [File system implementation](file-system-implementation.md) | The on-disk structures: superblock, inodes, bitmaps, directories, extents; the page cache; locality | Abstractions, [paging](../04-memory-management/address-spaces-and-paging.md) |
| [Crash consistency and journaling](crash-consistency-and-journaling.md) | Keeping those structures consistent across power loss: fsck, journaling, copy-on-write, log-structured | Implementation |

```
  open("/home/a/notes.txt") -> path walk -> inode -> extents -> blocks
       |                                                         |
  file descriptor --read/write--> page cache --writeback--> block layer --> device
                                                   \--- journal / COW ensures crash consistency
```

Read the abstractions first: they define what the implementation must deliver. Implementation shows the structures and the performance forces (seek time on disks, erase blocks on flash, caching in memory). Crash consistency is the hardest part: it explains why updates that touch several blocks need a journal or copy-on-write, and why applications must call `fsync`.

## Connections to sibling areas

- **[Kernel and abstractions](../01-kernel-and-abstractions/README.md):** the file is the OS's most successful abstraction; Unix extends the file-descriptor interface to pipes, devices and sockets.
- **[Process management](../02-process-management/README.md):** each process has a table of open file descriptors, inherited across `fork`, which is how shells wire up pipelines.
- **[Concurrency](../03-concurrency/README.md):** concurrent access to the same file or directory needs locks inside the file system, and ordering of writes is itself a concurrency problem against the device.
- **[Memory management](../04-memory-management/README.md):** the page cache is shared with virtual memory; `mmap` makes a file part of an address space, and page replacement decides which file pages stay cached.
- **[Input/output (I/O) and devices](../06-io-and-devices/README.md):** block device drivers, I/O schedulers and asynchronous I/O sit beneath the file system.
- **[Virtualization](../07-virtualization/README.md):** virtual disks are files on the host; container images are layered with union or overlay file systems.

## Connections across layers

From [04 Computer Architecture](../../04-computer-architecture/README.md) this area takes the properties of [Dynamic Random-Access Memory (DRAM) and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md) and [Direct Memory Access (DMA)](../../04-computer-architecture/05-io-and-interconnect/dma-and-devices.md); from [05 Algorithms](../../05-algorithms-and-data-structures/README.md), [search trees](../../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md) and [external-memory algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md). It gives [09 Data Management](../../09-data-management/README.md) the storage it builds on; databases reuse its ideas in [B-trees](../../09-data-management/02-storage-and-indexing/b-trees.md), [Log-Structured Merge-trees (LSM-trees)](../../09-data-management/02-storage-and-indexing/lsm-trees.md) and [recovery and logging](../../09-data-management/04-transactions/recovery-and-logging.md). Distributed file and object stores in [10](../../10-distributed-and-parallel-computing/README.md) replicate it across machines.

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): files hide blocks, devices and placement.
- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): paths name inodes; inodes name blocks.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): journals, checksums and copy-on-write survive crashes.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): the page cache and placement of related blocks together.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): on-disk invariants that must hold after every crash.
- [The end-to-end argument](../../CROSS-CUTTING.md#the-end-to-end-argument): applications must still `fsync` and check their own data.
