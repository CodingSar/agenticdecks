# Memory Hierarchy

> **Layer:** [04 Computer Architecture](../README.md) › Memory Hierarchy
> **Children:** [Locality and caching](locality-and-caching.md) · [Cache design](cache-design.md) · [Virtual memory hardware](virtual-memory-hardware.md) · [DRAM and storage devices](dram-and-storage-devices.md)

## What this area is about

Programs want memory that is large, fast and cheap. Physics allows any two. Small memories close to the logic (registers, Static Random-Access Memory (SRAM) caches) are fast but expensive per bit; large memories (Dynamic Random-Access Memory (DRAM), flash, disk) are cheap but far away and slow. The memory hierarchy combines them so that, for programs with locality, the whole looks almost as fast as the top level and almost as large as the bottom.

The gap it bridges is enormous and has grown. Since the 1980s processor speed improved far faster than DRAM latency (the "memory wall", named by Wulf and McKee in 1995). Approximate figures for 2020s hardware:

| Level | Typical size | Latency | Relative to an L1 hit |
|---|---|---|---|
| Registers | ~1 KiB architectural, a few KiB physical | 0 cycles (operand) | n/a |
| L1 cache | 32–64 KiB per core (data), similar for instructions | ~1 ns (4–5 cycles) | 1x |
| L2 cache | 256 KiB – 2 MiB per core (more on some designs) | ~3–5 ns | ~4x |
| L3 (last-level) cache | 8–100+ MiB shared | ~10–20 ns | ~15x |
| DRAM | 8 GiB – several TiB | ~60–120 ns | ~100x |
| NVMe flash SSD | 0.5–30 TB | ~10–100 µs | ~10^4–10^5x |
| Hard disk | 1–30 TB | ~5–10 ms | ~10^7x |

The unifying idea is **caching driven by locality**, applied at every level, plus **virtual memory**, which adds a layer of naming so that each program sees its own private address space that the hardware and Operating System (OS) map onto physical memory.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Locality and caching](locality-and-caching.md) | Why a hierarchy works at all: temporal and spatial locality, and the average memory access time model | ISA |
| [Cache design](cache-design.md) | How hardware caches are organised: lines, associativity, replacement, write policy, the 3 Cs of misses | Locality and caching |
| [Virtual memory hardware](virtual-memory-hardware.md) | Address translation and protection: page tables, the MMU and TLB | Cache design, ISA privilege |
| [DRAM and storage devices](dram-and-storage-devices.md) | The bottom levels: how DRAM, flash and disks work and why they are slow in the ways they are | Locality and caching |

Start with [locality and caching](locality-and-caching.md): everything else is an application of it. [Cache design](cache-design.md) gives the concrete mechanisms. [Virtual memory hardware](virtual-memory-hardware.md) is a second hierarchy layered on the first: a Translation Lookaside Buffer (TLB) caches translations, and DRAM acts as a cache for pages on storage. [DRAM and storage devices](dram-and-storage-devices.md) explains the physical behaviour (rows, banks, erase blocks, seeks) that the upper levels are designed to hide.

## Connections to sibling areas

- **[Instruction Set Architecture](../01-instruction-set-architecture/README.md)**: defines the flat address space being cached, and the page-table format and privilege checks the MMU enforces.
- **[Processor Microarchitecture](../02-processor-microarchitecture/README.md)**: out-of-order cores exist largely to tolerate miss latency; L1 hit time is part of the pipeline's critical path.
- **[Parallel Architecture](../04-parallel-architecture/README.md)**: once each core has private caches, copies of the same line must be kept coherent, and the order in which writes become visible must be defined.
- **[I/O and Interconnect](../05-io-and-interconnect/README.md)**: devices write memory directly through Direct Memory Access (DMA), which must interact correctly with caches; storage devices are reached through the I/O system.
- **[Performance](../06-performance/README.md)**: memory stalls are often the largest term in cycles per instruction; the roofline model judges whether code is limited by bandwidth or compute.

## Connections across layers

SRAM cells and DRAM capacitors come from [00 Engineering Foundations](../../00-engineering-foundations/03-semiconductor-devices/cmos.md) and [capacitance](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md). Upward, the hierarchy is why [external-memory and cache-oblivious algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md) and [B-trees](../../09-data-management/02-storage-and-indexing/b-trees.md) exist, why [arrays beat linked lists](../../05-algorithms-and-data-structures/02-fundamental-data-structures/arrays-and-linked-lists.md) in practice, and what the OS manages in [address spaces and paging](../../07-operating-systems/04-memory-management/address-spaces-and-paging.md) and [page replacement](../../07-operating-systems/04-memory-management/page-replacement.md). Storage device behaviour shapes [file systems](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md) and [LSM trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md).

## Cross-cutting threads

- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): the central principle, visible at every level.
- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): virtual addresses are names resolved by page tables.
- [Virtualization](../../CROSS-CUTTING.md#virtualization): each process sees a private address space larger than physical memory.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): the speed of light and wire capacitance make large memories slow.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): whole cache lines, DRAM rows and disk blocks are transferred to amortise access cost.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): data layout (arrays of structures vs structures of arrays) decides how many lines a loop touches.
