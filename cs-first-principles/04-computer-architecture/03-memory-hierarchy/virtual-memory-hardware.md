# Virtual Memory Hardware

> **Layer:** [04 Computer Architecture](../README.md) › [Memory Hierarchy](README.md)
> **Builds on:** [Cache design](cache-design.md), [The ISA contract](../01-instruction-set-architecture/the-isa-contract.md), [Functions and cardinality](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md)
> **Enables:** [Address spaces and paging](../../07-operating-systems/04-memory-management/address-spaces-and-paging.md), [Processes](../../07-operating-systems/02-process-management/processes.md), [Virtual machines and hypervisors](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md), [Isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md)

## Essence

Virtual memory gives every program its own private address space by inserting a translation between the addresses a program uses (virtual) and the locations in physical memory. Memory is divided into fixed-size pages (4 KiB by default on x86-64 and most ARM and RISC-V systems), and a page table maps each virtual page to a physical frame, together with permission bits. A hardware Memory Management Unit (MMU) performs this translation on every instruction fetch, load and store, and a Translation Lookaside Buffer (TLB) caches recent translations so that the lookup usually costs nothing extra. If a page is not mapped or the access is not permitted, the hardware raises a page fault and hands control to the Operating System (OS). This single mechanism provides isolation, protection, sharing, and the illusion of more memory than physically exists.

## Core tenets

1. **Translation is indirection on every access.** A virtual address splits into a virtual page number and a page offset (12 bits for 4 KiB pages). The page number is translated; the offset passes through unchanged. Because translation happens below the Instruction Set Architecture's (ISA's) view of addresses, programs are compiled as if they owned the whole address space starting at the same addresses, and the OS can place them anywhere in physical memory.

2. **Page tables are trees to keep them small.** A flat table for a 48-bit address space with 4 KiB pages would need 2^36 entries per process. x86-64 instead uses a four-level radix tree (five levels for 57-bit addresses since Intel Ice Lake): each level indexes 9 bits of the virtual page number into a 512-entry, 4 KiB table. Unmapped regions need no lower-level tables, so sparse address spaces are cheap. The CR3 register (x86) or SATP (RISC-V) or TTBR (ARM) holds the root, and switching processes means switching this one register.

3. **The TLB makes translation fast.** Walking four levels of tables costs up to four memory accesses per load, which would be ruinous. A TLB is a small cache of recent translations (typically 64 entries for the L1 data TLB and 1,000–3,000 entries for the L2 TLB on 2020s cores); hit rates are usually above 99% because of locality. On a miss, a hardware page-table walker (x86, ARM, most RISC-V) reads the tables, often finding them in the data caches.

4. **Permission bits turn translation into protection.** Each entry carries bits for present, writable, user-accessible, and no-execute (NX, introduced to x86-64 by AMD in 2003). The MMU checks them on every access. A user-mode program cannot even name another process's memory, because it has no mapping to it, and cannot touch kernel pages because they are marked supervisor-only. This is the hardware basis of process isolation.

5. **A page fault is a precise exception that the OS turns into a feature.** When an entry is not present or a permission check fails, the hardware stops the instruction, saves its address, and traps to the kernel. The OS can then load the page from disk (demand paging), allocate a zeroed page (lazy allocation), copy a shared page (copy-on-write after `fork`), or kill the program (segmentation fault). The faulting instruction is then restarted, which requires precise exceptions.

6. **Large pages trade flexibility for TLB reach.** A TLB with 1,536 entries of 4 KiB covers only 6 MiB. Using 2 MiB or 1 GiB pages (x86-64), or 16 KiB and 64 KiB pages on ARM, extends reach by orders of magnitude and shortens page walks, which matters for databases and large in-memory workloads. The cost is coarser allocation and harder memory management.

7. **Caches and translation must be designed together.** To overlap TLB lookup with L1 access, many L1 caches are virtually indexed, physically tagged: the index comes from the page-offset bits, which are the same in virtual and physical addresses, while the tag check uses the translated address. This is why an L1 of 32 KiB with 8 ways (4 KiB per way) fits exactly with 4 KiB pages, and why L1 size grows by adding ways or using larger pages rather than more sets.

8. **Address-space identifiers and nested paging support many contexts.** Without tags, a context switch must flush the TLB. Address Space Identifiers (ASIDs; Process-Context Identifiers, PCIDs, on x86) tag entries so translations from several processes coexist. For virtual machines, hardware nested paging (Intel EPT, AMD NPT, around 2008) adds a second translation from guest-physical to host-physical, at the cost of much longer page walks on a TLB miss.

```
 virtual address (48 bits, x86-64, 4 KiB pages)
 | L4 idx 9 | L3 idx 9 | L2 idx 9 | L1 idx 9 | offset 12 |
     |          |          |          |
  CR3 -> table -> table -> table -> table -> physical frame + offset
         (TLB caches the whole chain: VPN -> frame, perms)
```

## Key concepts

| Term | Meaning |
|---|---|
| Virtual address | Address used by a program, translated before reaching memory |
| Page / frame | Fixed-size block of virtual / physical memory |
| Page table | Data structure mapping virtual pages to physical frames and permissions |
| MMU | Memory Management Unit: hardware that translates and checks every access |
| TLB | Translation Lookaside Buffer: cache of recent page translations |
| Page-table walk | Reading the page-table levels to resolve a TLB miss |
| Page fault | Exception raised when a translation is missing or an access is not permitted |
| Huge page | Larger page size (2 MiB, 1 GiB) that increases TLB reach |
| ASID / PCID | Tag that lets TLB entries from different address spaces coexist |

## How it fits

- **Below:** translation is a [function](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md) from virtual to physical pages, partial and not necessarily injective (shared pages); the TLB is built like any [cache](cache-design.md); faults rely on [the ISA's](../01-instruction-set-architecture/the-isa-contract.md) precise exceptions and privilege modes.
- **Above:** the OS builds [address spaces and paging](../../07-operating-systems/04-memory-management/address-spaces-and-paging.md), [processes](../../07-operating-systems/02-process-management/processes.md) and [page replacement](../../07-operating-systems/04-memory-management/page-replacement.md) on this; hypervisors use nested paging for [virtual machines](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md); [sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md) depends on page permissions.
- **Siblings:** DRAM acts as a cache for pages stored on [storage devices](dram-and-storage-devices.md); [locality](locality-and-caching.md) is what makes both the TLB and demand paging work.

## Common misconceptions

- **"Virtual memory means swapping to disk."** Swapping is one use. The essential functions are isolation, protection, relocation and sharing; many phones and servers run with little or no swap.
- **"Translation costs a memory access per load."** With TLB hit rates above 99%, translation is usually overlapped with the L1 lookup and costs nothing visible; the cost shows up only on TLB misses.
- **"The OS translates addresses."** The OS *writes* the page tables; hardware performs every translation. The OS runs only on faults.

## Go deeper

- Denning, *Virtual Memory* (ACM Computing Surveys, 1970): the classic account of why and how.
- Kilburn et al., *One-Level Storage System* (IRE Transactions, 1962): the Atlas computer, the first virtual memory.
- Arpaci-Dusseau and Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (2018), chapters on paging and TLBs: clear hardware–OS division of labour.
- Bhattacharjee and Lustig, *Architectural and Operating System Support for Virtual Memory* (2017): modern TLB and page-walk design.
