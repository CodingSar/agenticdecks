# Memory Allocation

> **Layer:** [07 Operating Systems](../README.md) › [Memory management](README.md)
> **Builds on:** [Address spaces and paging](address-spaces-and-paging.md), [Arrays and linked lists](../../05-algorithms-and-data-structures/02-fundamental-data-structures/arrays-and-linked-lists.md), [Amortized analysis](../../05-algorithms-and-data-structures/01-foundations/amortized-analysis.md)
> **Enables:** [Memory management and garbage collection](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md), [Memory safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md), [Page replacement](page-replacement.md)

## Essence

Memory allocation hands out pieces of memory on request and takes them back. It happens at two levels. The **kernel** allocates physical frames (for page tables, page cache and user pages) and small kernel objects (process records, inodes, socket buffers). **User-space allocators** such as `malloc` obtain large regions of virtual memory from the kernel (`brk`, `mmap`) and carve them into objects of arbitrary sizes. Every allocator fights the same enemy, **fragmentation**: free memory split into pieces that do not fit the requests. Because objects cannot be moved in C, an allocator's placement decisions are permanent, so good allocators exploit the fact that programs allocate many objects of a few sizes with similar lifetimes.

## Core tenets

1. **Fragmentation is inevitable without moving objects.** *External* fragmentation is free memory scattered in holes between live objects; *internal* fragmentation is space wasted inside allocated blocks (rounding a 33-byte request up to 48). Robson (1971) showed that for any non-moving allocator there are request sequences that force worst-case memory use to grow with the logarithm of the ratio of largest to smallest object size. Allocators therefore cannot be optimal for every program and are tuned for typical ones.

2. **Free-list placement policies trade speed against fragmentation.** A simple allocator keeps a linked list of free blocks and chooses by *first fit* (first big-enough block), *best fit* (smallest big-enough) or *next fit*. Adjacent free blocks must be *coalesced* on free, or fragmentation grows; boundary tags (size fields at both ends of each block) let the allocator find neighbours in constant time. Studies (Wilson et al., 1995) found that first fit and best fit with coalescing waste little memory on real programs.

3. **Size classes and segregated free lists make the common case constant-time.** Modern allocators round requests to a few dozen size classes and keep a separate free list per class. Allocation pops from a list; free pushes onto it. Because objects of one size share pages, fragmentation stays bounded and lookups are trivial. This is the design of jemalloc (FreeBSD, Firefox), tcmalloc (Google) and mimalloc (Microsoft).

4. **The kernel uses a buddy allocator for frames and slab caches for objects.** The *buddy system* manages physical memory in power-of-two blocks: splitting a block yields two "buddies" whose addresses differ in one bit, so on free the buddy is found by exclusive-or (XOR) and merged if free. It gives fast, contiguous allocation at the cost of internal fragmentation. On top of it, the *slab allocator* (Bonwick, 1994, in SunOS; Linux's SLUB is a descendant) keeps per-type caches of pre-initialized objects, so allocating an inode is popping a ready-made one from a cache.

5. **Per-thread caches make allocation scale on multicores.** A single global allocator lock serializes every `malloc` in a multithreaded program. tcmalloc, jemalloc and mimalloc give each thread (or Central Processing Unit (CPU)) a small cache of free objects per size class and touch shared structures only in batches. Most allocations then need no synchronization, and objects stay near the core that uses them.

6. **Allocators get memory from the kernel in large chunks and return it reluctantly.** System calls and page-table changes are expensive ([address spaces and paging](address-spaces-and-paging.md)), so allocators request memory in megabyte-sized arenas, serve large requests directly with `mmap`, and return memory with `madvise(MADV_DONTNEED)` or `munmap` only after it has been free for a while. This [amortizes](../../05-algorithms-and-data-structures/01-foundations/amortized-analysis.md) the kernel cost but means a process's resident size can stay high after it frees memory.

7. **Manual allocation creates whole classes of bugs.** In C and C++, the programmer decides when to `free`. Freeing too early leaves a dangling pointer (use-after-free); freeing twice corrupts allocator metadata; never freeing leaks. Use-after-free and heap overflows are among the most exploited vulnerability classes, because allocator metadata and reused objects give attackers control. Hardened allocators add guard pages, randomization and checks; garbage collection and ownership types (Rust) remove the problem at the language level.

8. **Garbage-collected runtimes move the problem, not remove it.** A collector can compact the heap (moving objects and updating pointers), which eliminates external fragmentation, and bump-pointer allocation then costs a few instructions. The price is collection work and pauses. Such runtimes still sit on the Operating System's (OS's) page allocation and interact with it (large heaps want huge pages; idle heaps should return memory).

## Key concepts

| Term | Meaning |
|---|---|
| External fragmentation | Free memory split into holes too small for requests |
| Internal fragmentation | Unused space inside allocated blocks |
| Free list | A linked list of available blocks |
| Coalescing | Merging adjacent free blocks |
| Size class | A fixed allocation size that requests are rounded up to |
| Buddy allocator | Power-of-two block allocator whose free blocks merge with their "buddy" |
| Slab allocator | Per-type caches of preallocated kernel objects |
| Arena | A large region obtained from the kernel and subdivided by the allocator |
| Use-after-free | Accessing memory after it has been returned to the allocator |

## How it fits

- **Below:** uses virtual memory obtained through [paging](address-spaces-and-paging.md); free lists are [linked lists](../../05-algorithms-and-data-structures/02-fundamental-data-structures/arrays-and-linked-lists.md), and allocator costs are argued with [amortized analysis](../../05-algorithms-and-data-structures/01-foundations/amortized-analysis.md).
- **Above:** language runtimes build managed heaps and collectors on top ([memory management and garbage collection](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md)); allocator bugs underlie many [memory safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md).
- **Siblings:** [page replacement](page-replacement.md) reclaims frames when allocation runs short; [address spaces and paging](address-spaces-and-paging.md) decides when a virtual allocation actually consumes physical memory.

## Common misconceptions

- **"`free` returns memory to the OS."** Usually it returns memory to the allocator's free lists; the process's footprint shrinks only when whole pages or arenas are released.
- **"`malloc` is slow, so pool everything."** Modern allocators serve small requests in tens of nanoseconds from thread caches; custom pools often add fragmentation and bugs for little gain.
- **"Garbage collection eliminates memory leaks."** Objects reachable but unused (a growing cache, a forgotten listener) are never collected.

## Go deeper

- Paul R. Wilson, Mark S. Johnstone, Michael Neely and David Boles, "Dynamic Storage Allocation: A Survey and Critical Review" (1995).
- Jeff Bonwick, "The Slab Allocator: An Object-Caching Kernel Memory Allocator" (USENIX 1994).
- Donald E. Knuth, *The Art of Computer Programming*, Vol. 1, §2.5 "Dynamic Storage Allocation" (1968; 3rd ed. 1997): boundary tags and the buddy system.
- Jason Evans, "A Scalable Concurrent malloc(3) Implementation for FreeBSD" (BSDCan 2006): the jemalloc design.
