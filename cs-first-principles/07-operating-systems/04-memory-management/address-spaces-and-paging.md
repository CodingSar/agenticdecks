# Address Spaces and Paging

> **Layer:** [07 Operating Systems](../README.md) › [Memory management](README.md)
> **Builds on:** [Virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md), [Locality and caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md), [Processes](../02-process-management/processes.md)
> **Enables:** [Page replacement](page-replacement.md), [Memory allocation](memory-allocation.md), [Virtual machines and hypervisors](../07-virtualization/virtual-machines-and-hypervisors.md), [Isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md)

## Essence

An **address space** is the range of virtual addresses a process can use, together with what each address maps to. **Paging** implements it: virtual memory is divided into fixed-size pages (typically 4 KiB), physical memory into frames of the same size, and a per-process **page table** maps each virtual page to a frame (or marks it absent) with permission bits. The Memory Management Unit (MMU) translates every load, store and instruction fetch, caching recent translations in a Translation Lookaside Buffer (TLB). Because the Operating System (OS) owns the page tables, it gets isolation (processes cannot name each other's frames), flexibility (pages can live anywhere, or nowhere yet) and a hook (the page fault) to intervene on any access.

## Core tenets

1. **Translation gives isolation by construction.** A process can only issue virtual addresses, and its page table maps them only to frames the OS chose for it. There is no address it can form that reaches another process's frame unless the OS deliberately maps it in both. Permission bits (read, write, execute, user/supervisor) add finer rules: code pages are read-only and executable, data pages are writable but non-executable (the no-execute (NX) bit, which blocks classic code-injection attacks), and kernel pages are inaccessible from user mode.

2. **Fixed-size pages beat variable-size segments for allocation.** Earlier systems used segmentation (base and bound registers per region), which suffers external fragmentation: free memory is split into holes too small to use. With pages, any free frame can hold any page, so allocation is trivial. The cost is internal fragmentation (on average half a page wasted per region) and the size of the mapping tables.

3. **Page tables are multi-level trees so that sparse address spaces are cheap.** A flat table for a 48-bit address space with 4 KiB pages would need 2^36 entries per process. x86-64 instead uses a four-level radix tree (five levels for 57-bit addresses), each level indexed by 9 bits of the virtual address, and only allocates the parts of the tree that are in use. The price is that a TLB miss may need four memory reads to walk the tree.

   ```
   VA[47:39] -> L4 -> VA[38:30] -> L3 -> VA[29:21] -> L2 -> VA[20:12] -> L1 -> frame + VA[11:0]
   ```

4. **The TLB makes translation nearly free, and its reach limits performance.** Programs touch the same pages repeatedly, so a TLB of a few thousand entries hits on the vast majority of accesses. TLB reach is entries times page size: 1,536 entries × 4 KiB covers about 6 MiB, too little for a database or a large Java heap. Huge pages (2 MiB or 1 GiB on x86-64) multiply reach by 512 or more, which is why databases and virtual machines enable them. Switching address spaces can flush the TLB; Process-Context Identifiers (PCIDs) or Address-Space Identifiers (ASIDs) tag entries to avoid this.

5. **A page fault is a feature, not only an error.** When the MMU finds no valid mapping or a permission violation, it traps to the kernel, which decides what the access *means*. It may be a first touch of lazily allocated memory (allocate a zeroed frame), a page that was swapped or never loaded from a file (read it in), a write to a copy-on-write page (copy it), a stack growing downward (extend it), or a genuine bug (deliver `SIGSEGV`). Demand paging means programs start fast and only use memory they actually touch.

6. **Sharing and copy-on-write come from mapping one frame in several places.** Shared libraries such as libc are mapped read-only into every process that uses them, so they occupy physical memory once. `fork` marks all writable pages read-only in both parent and child and copies a page only when one side writes. `mmap` maps a file's pages into an address space so that reading memory reads the file through the page cache.

7. **Virtual memory overcommits physical memory, so something must give.** Because allocation is lazy, the sum of address spaces can far exceed physical memory. When frames run out, the kernel must evict pages ([page replacement](page-replacement.md)) or, on Linux, invoke the Out-Of-Memory (OOM) killer to terminate a process. Linux's default heuristic overcommit lets `malloc` succeed for memory that may never be backed.

8. **Changing mappings on a multicore is expensive.** Each core caches translations in its own TLB, and hardware does not keep TLBs coherent on x86. When the kernel unmaps or downgrades a page used by several threads, it must send inter-processor interrupts to make other cores invalidate their entries, a TLB shootdown costing microseconds.

## Key concepts

| Term | Meaning |
|---|---|
| Virtual address | An address issued by a program, translated before reaching memory |
| Page / frame | Fixed-size unit of virtual / physical memory (commonly 4 KiB) |
| Page table entry (PTE) | Maps one virtual page: frame number, present, permission, accessed and dirty bits |
| TLB | Translation Lookaside Buffer: a small cache of recent translations |
| Page fault | Trap raised when a translation is missing or an access is not permitted |
| Copy-on-write | Share a page read-only and copy it on the first write |
| TLB shootdown | Invalidating stale translations on other cores via inter-processor interrupts |

## How it fits

- **Below:** the page-table format and walk are defined by [virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md); the TLB works because of [locality](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md).
- **Above:** language heaps and garbage collectors request and release pages ([memory management and garbage collection](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md)); address-space layout randomization and non-executable pages defend against [memory safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md); hypervisors add a second translation layer ([virtual machines and hypervisors](../07-virtualization/virtual-machines-and-hypervisors.md)).
- **Siblings:** [page replacement](page-replacement.md) decides which pages stay resident; [memory allocation](memory-allocation.md) supplies frames and carves pages into objects.

## Common misconceptions

- **"Virtual memory means swapping to disk."** Swapping is one use. The core of virtual memory is translation, which gives isolation, sharing and lazy allocation even on machines with no swap (most phones).
- **"`malloc` returning non-NULL means the memory exists."** Under overcommit, physical frames are assigned on first touch; a process can be killed later when it uses memory it was "given".

## Go deeper

- Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (2018), the memory virtualization chapters.
- Peter J. Denning, "Virtual Memory" (ACM Computing Surveys, 1970): the classic survey.
