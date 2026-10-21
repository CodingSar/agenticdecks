# Page Replacement

> **Layer:** [07 Operating Systems](../README.md) › [Memory management](README.md)
> **Builds on:** [Address spaces and paging](address-spaces-and-paging.md), [Locality and caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md), [Streaming and online algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/streaming-and-online-algorithms.md)
> **Enables:** [File system implementation](../05-storage-and-file-systems/file-system-implementation.md), [Storage layouts](../../09-data-management/02-storage-and-indexing/storage-layouts.md), [Content delivery and caching](../../08-networking/05-application-layer/content-delivery-and-caching.md)

## Essence

When physical memory is full and a process touches a page that is not resident, the Operating System (OS) must choose a **victim** page to evict, writing it to disk first if it has been modified. Page replacement is cache management: physical memory is a cache for the much larger virtual memory backed by disk, and a miss (a major page fault) costs around 10–100 µs from a Solid-State Drive (SSD) or about 10 ms from a spinning disk, versus ~100 ns for a memory access. The optimal policy evicts the page used furthest in the future, which is unknowable; practical policies approximate **Least Recently Used (LRU)** using cheap hardware hints, and the system must also detect when the working set simply does not fit (**thrashing**) and reduce load.

## Core tenets

1. **The optimal policy is known but needs the future.** Bélády's MIN algorithm (1966) evicts the page whose next use is furthest away and provably minimizes misses. It cannot be implemented online, but it is the yardstick: a practical policy is judged by how close it comes on real traces.

2. **LRU works because of temporal locality, but exact LRU is too expensive.** Pages used recently tend to be used again soon, so evicting the least recently used page approximates MIN well. Exact LRU would mean updating an ordered list on *every* memory access, which is impossible at hardware speed. Instead the Memory Management Unit (MMU) sets an *accessed* bit in the page table entry on each use, and the OS samples and clears these bits periodically.

3. **The clock algorithm approximates LRU with one bit per page.** Frames are arranged in a circle with a hand. On eviction, the hand advances: if the frame's accessed bit is set, clear it and move on (a "second chance"); if clear, evict it. Pages that are used keep getting their bit set and survive. Preferring clean pages (dirty bit clear) to dirty ones avoids a disk write before reuse.

4. **First-in-first-out eviction can get worse with more memory; stack algorithms cannot.** First In, First Out (FIFO) eviction exhibits Bélády's anomaly: on some reference strings, adding frames increases faults. LRU and MIN are *stack algorithms* (the set of pages resident with k frames is always a subset of those with k+1), so more memory never hurts them. This inclusion property is why LRU-like policies are preferred.

5. **Plain LRU is fooled by scans, so real systems use multiple lists.** A one-time sequential read of a large file would flush every hot page under LRU. Linux therefore keeps *active* and *inactive* lists (newly read pages enter inactive and are promoted only on a second access) and, since kernel 6.1, offers a Multi-Generational LRU. Database and research policies like LRU-K, 2Q and the Adaptive Replacement Cache (ARC, used in ZFS) balance recency against frequency for the same reason.

6. **Thrashing happens when the working set exceeds memory, and no replacement policy can fix it.** Denning's working set is the set of pages a process has used in a recent window. If the sum of working sets of running processes exceeds physical memory, every process faults constantly, the disk becomes the bottleneck, and the Central Processing Unit (CPU) sits idle while utilization of useful work collapses. The only cures are to reduce the load (suspend or kill processes, as Linux's Out-Of-Memory (OOM) killer does) or add memory.

7. **Not all pages are equal to evict.** *Clean file-backed* pages can simply be dropped, since they can be re-read from the file. *Dirty file-backed* pages must be written back first. *Anonymous* pages (heap, stack) must go to swap space, or cannot be evicted at all if there is none. Kernels balance reclaiming the page cache against swapping anonymous memory (Linux's `swappiness` tunes this), and run background writeback so clean victims are available when needed.

8. **Applications that know their access pattern often do better than the OS.** The OS sees only page touches. A database knows that a table scan will not revisit pages, or that an index root is hot. So databases bypass the page cache (`O_DIRECT`) and manage their own buffer pool, and applications give hints with `madvise` or `posix_fadvise`. This is the [end-to-end argument](../../CROSS-CUTTING.md#the-end-to-end-argument) applied to caching.

## Key concepts

| Term | Meaning |
|---|---|
| Page fault (major / minor) | A miss needing disk input/output (I/O) / one satisfiable from memory (e.g. a page already in the page cache) |
| Victim | The page chosen for eviction |
| MIN (Bélády's optimal) | Evict the page used furthest in the future |
| LRU | Least Recently Used: evict the page untouched for longest |
| Clock (second chance) | One-bit LRU approximation sweeping frames in a circle |
| Accessed / dirty bit | Hardware-set page table entry (PTE) bits recording use and modification |
| Working set | Pages a process referenced in a recent time window |
| Thrashing | Constant paging because working sets exceed memory |

## How it fits

- **Below:** relies on [accessed and dirty bits](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md) and on the [locality](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md) of real programs; eviction is an [online problem](../../05-algorithms-and-data-structures/07-advanced-topics/streaming-and-online-algorithms.md) (LRU is k-competitive against MIN).
- **Above:** the same policies drive the file system's page cache ([file system implementation](../05-storage-and-file-systems/file-system-implementation.md)), database buffer pools ([storage layouts](../../09-data-management/02-storage-and-indexing/storage-layouts.md)) and web caches ([content delivery and caching](../../08-networking/05-application-layer/content-delivery-and-caching.md)).
- **Siblings:** [address spaces and paging](address-spaces-and-paging.md) supplies the fault mechanism; [memory allocation](memory-allocation.md) consumes the frames that reclaim frees.

## Common misconceptions

- **"Any swap use means the system is slow."** Evicting cold pages that are never touched again frees memory for the page cache; the problem is a high *rate* of major faults, not swap occupancy.
- **"Free memory is wasted memory, so the OS should never evict."** The OS keeps memory full of cache on purpose, but must keep a reserve of quickly reclaimable pages so allocations do not stall.
- **"A better replacement policy solves thrashing."** If the working sets do not fit, every policy faults; only reducing load or adding memory helps.

## Go deeper

- L. A. Bélády, "A Study of Replacement Algorithms for a Virtual-Storage Computer" (1966): the MIN algorithm. The FIFO anomaly came later (Bélády, Nelson and Shedler, 1969).
- Peter J. Denning, "The Working Set Model for Program Behavior" (1968).
- Nimrod Megiddo and Dharmendra S. Modha, "ARC: A Self-Tuning, Low Overhead Replacement Cache" (FAST 2003).
