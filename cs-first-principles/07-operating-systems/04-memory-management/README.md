# Memory Management

> **Layer:** [07 Operating Systems](../README.md) › Memory management
> **Children:** [Address spaces and paging](address-spaces-and-paging.md) · [Page replacement](page-replacement.md) · [Memory allocation](memory-allocation.md)

## What this area is about

This area is how the Operating System (OS) virtualizes memory. Physical memory is one shared array of bytes of fixed size; each program wants a large, private, contiguous address space that starts at the same place every time and is protected from every other program. The OS provides that illusion by translating every address a program issues through per-process **page tables**, which the hardware Memory Management Unit (MMU) walks and caches in a Translation Lookaside Buffer (TLB). Translation then lets the OS do far more than isolate: share code between processes, map files into memory, allocate memory lazily, copy on write, and use disk as an overflow area when physical memory runs out.

The unifying idea is **indirection at page granularity**. Because every access goes through a mapping the OS controls, the OS can change where (or whether) a page lives without the program noticing, and decides which pages deserve scarce physical frames.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Address spaces and paging](address-spaces-and-paging.md) | The mechanism: virtual addresses, page tables, the TLB, page faults, sharing and copy-on-write | [Virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md) |
| [Page replacement](page-replacement.md) | The policy when memory is full: which page to evict, and how to avoid thrashing | Paging |
| [Memory allocation](memory-allocation.md) | Carving memory into objects: kernel frame allocators, slab caches, user-space `malloc` | Paging |

```
  program's virtual address
        |
        v
   [TLB hit?] --yes--> physical frame --> cache/DRAM
        | no
        v
   page-table walk --present--> fill TLB
        | not present
        v
   page fault -> kernel: allocate / read from disk / copy-on-write / kill
                       (page replacement picks a victim if no frame is free)
```

Read paging first: it is the mechanism the other two use. Page replacement is the caching policy that decides which virtual pages occupy physical frames. Allocation works at two levels: the kernel hands out physical frames and kernel objects, and user-space allocators (`malloc`, language runtimes) carve the virtual pages they receive from the kernel into objects.

## Connections to sibling areas

- **[Kernel and abstractions](../01-kernel-and-abstractions/README.md):** page-table protection bits are what stop user code touching kernel memory; Meltdown showed what happens when hardware leaks across that line.
- **[Process management](../02-process-management/README.md):** an address space is most of what a process is; switching processes means switching page tables, which is why context switches can flush the TLB.
- **[Concurrency](../03-concurrency/README.md):** threads share one address space; changing a mapping on one core requires a TLB shootdown on the others.
- **[Storage and file systems](../05-storage-and-file-systems/README.md):** the page cache unifies file data and memory pages; `mmap` maps a file directly into an address space.
- **[Input/output (I/O) and devices](../06-io-and-devices/README.md):** Direct Memory Access (DMA) buffers must be pinned in physical memory, and an Input-Output Memory Management Unit (IOMMU) translates device addresses as the MMU does for the Central Processing Unit (CPU).
- **[Virtualization](../07-virtualization/README.md):** hypervisors add a second level of translation (guest-physical to host-physical) with nested page tables.

## Connections across layers

Hardware support comes from [04 Computer Architecture](../../04-computer-architecture/README.md): [virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md), [locality and caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md) and [Dynamic Random-Access Memory (DRAM) and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md). Above, [language runtimes](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md) build heaps on OS pages; databases build buffer pools that replace the OS's eviction policy ([storage layouts](../../09-data-management/02-storage-and-indexing/storage-layouts.md)); and security depends on address-space isolation and randomization ([memory safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md)).

## Cross-cutting threads

- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): virtual addresses are names resolved by page tables.
- [Virtualization](../../CROSS-CUTTING.md#virtualization): one physical memory becomes many private address spaces.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): the TLB caches translations; physical memory caches disk.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): page size trades TLB reach against internal fragmentation.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): huge pages and slab caches amortize per-object overheads.
