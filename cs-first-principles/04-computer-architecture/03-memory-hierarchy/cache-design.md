# Cache Design

> **Layer:** [04 Computer Architecture](../README.md) › [Memory Hierarchy](README.md)
> **Builds on:** [Locality and caching](locality-and-caching.md), [Arithmetic and building blocks](../../03-digital-logic/02-combinational-logic/arithmetic-and-building-blocks.md), [Binary and positional notation](../../03-digital-logic/01-number-representation/binary-and-positional-notation.md), [Memory cells](../../03-digital-logic/03-sequential-logic/memory-cells.md)
> **Enables:** [Multicore and cache coherence](../04-parallel-architecture/multicore-and-cache-coherence.md), [Hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md), [Side channels](../../11-security-and-cryptography/03-system-security/side-channels.md)

## Essence

A hardware cache is a fixed-size table of recently used memory lines, searched by address in a few cycles. Four decisions define it: where a line may be placed (mapping and associativity), how to tell which line is present (tags), which line to evict when a set is full (replacement), and when writes reach the next level (write policy). Every decision trades hit time, miss rate, area and energy against each other. Misses fall into three classes, compulsory, capacity and conflict, and each design choice attacks a different class. Modern Central Processing Units (CPUs) stack three levels of such caches, each larger, slower and more associative than the one above.

## Core tenets

1. **An address splits into tag, index and offset.** With 64-byte lines, the low 6 bits are the offset within a line. The next bits select a set (the index): a 32 KiB, 8-way cache with 64-byte lines has 32768 / (64 × 8) = 64 sets, so 6 index bits. The remaining high bits are the tag, stored with the line and compared on every access to confirm a hit. With power-of-two sizes, the split is just wiring.

2. **Associativity trades conflict misses against hit time and energy.** A direct-mapped cache allows each line in exactly one place: fast and simple, but two hot addresses that share an index evict each other repeatedly. An n-way set-associative cache allows n places per set and compares n tags in parallel; fully associative allows anywhere. Typical 2020s choices are 8–12 ways for the level-1 (L1) cache, 8–16 for level 2 (L2) and 12–20 for level 3 (L3).

3. **Misses come in three kinds (the 3 Cs).** Compulsory misses are first touches; larger lines and prefetching reduce them. Capacity misses happen because the working set is larger than the cache; only a bigger cache or better locality helps. Conflict misses happen because too many hot lines map to one set; higher associativity helps. A fourth C, coherence misses, appears in multiprocessors when another core invalidates a line.

4. **Line size is a balance.** Larger lines exploit more spatial locality and amortise the fixed cost of a memory transfer, but they waste bandwidth when only part of the line is used and reduce the number of distinct lines a cache can hold. The industry settled on 64 bytes for CPU caches (Apple's M-series uses 128-byte lines). Graphics Processing Units (GPUs) often use 128-byte lines with smaller sectors.

5. **Replacement approximates "evict what will not be needed for longest".** The optimal policy (Bélády, 1966) needs knowledge of the future. Least Recently Used (LRU) approximates it well for many programs, but true LRU state is costly at high associativity, so hardware uses pseudo-LRU trees or newer adaptive policies (such as Re-Reference Interval Prediction (RRIP)) that resist being flushed by one large streaming scan.

6. **Write policy decides when memory sees a store.** Write-through sends every store to the next level (simple, consistent, bandwidth-hungry). Write-back marks the line dirty and writes it only on eviction, saving bandwidth because a line is often written many times; nearly all L2 and L3 caches and most L1s are write-back. On a write miss, write-allocate fetches the line first, which suits code that writes then reads the same data.

7. **Multi-level caches split the job.** L1 is optimised for hit time (a few cycles, small, split into instruction and data caches to avoid structural conflicts); L2 for hit rate at moderate latency; the shared L3 (last-level cache) for capacity and for sharing among cores. Inclusive L3s hold a copy of everything above, which simplifies coherence; exclusive or non-inclusive designs avoid duplicating data.

8. **Prefetching guesses misses before they happen.** Hardware prefetchers detect sequential and strided access streams and fetch lines ahead of demand; they turn many would-be compulsory misses into hits for array traversals. They cannot predict pointer-chasing (linked lists, trees), which is one reason those structures run slowly. Software prefetch instructions let compilers and programmers give hints.

## Key concepts

| Term | Meaning |
|---|---|
| Tag | High-order address bits stored with a line to identify which memory block it holds |
| Index | Address bits that select the set |
| Offset | Low-order bits selecting the byte within a line |
| Set-associative | Each address maps to one set of n possible line slots (ways) |
| Direct-mapped | One-way associative: each address has exactly one possible slot |
| Dirty bit | Marks a line modified since it was fetched, so it must be written back on eviction |
| Write-back / write-through | Defer writes until eviction / propagate every write immediately |
| 3 Cs | Compulsory, capacity and conflict misses |
| Prefetcher | Hardware that fetches lines predicted to be needed soon |
| Inclusive cache | Lower-level cache guaranteed to contain all lines held in upper levels |

## How it fits

- **Below:** tag comparison uses [comparators and multiplexers](../../03-digital-logic/02-combinational-logic/arithmetic-and-building-blocks.md); the index/tag split relies on [binary positional notation](../../03-digital-logic/01-number-representation/binary-and-positional-notation.md); cache arrays are Static Random-Access Memory (SRAM) [memory cells](../../03-digital-logic/03-sequential-logic/memory-cells.md), six transistors per bit, built in [Complementary Metal-Oxide-Semiconductor (CMOS)](../../00-engineering-foundations/03-semiconductor-devices/cmos.md); SRAM's area per bit is why caches stay small.
- **Above:** a set-associative cache is a hardware [hash table](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) with bounded buckets; the same eviction ideas appear in [page replacement](../../07-operating-systems/04-memory-management/page-replacement.md) and database buffer pools; timing differences between hits and misses enable [cache side channels](../../11-security-and-cryptography/03-system-security/side-channels.md).
- **Siblings:** implements [locality and caching](locality-and-caching.md); the Translation Lookaside Buffer (TLB) in [virtual memory hardware](virtual-memory-hardware.md) is a cache of translations designed the same way; [coherence](../04-parallel-architecture/multicore-and-cache-coherence.md) adds sharing state to each line.

## Common misconceptions

- **"A fully associative cache is always best."** It eliminates conflict misses but needs a comparator per line and is slow and power-hungry; that is why only small structures (some TLBs) use it.
- **"LRU is optimal."** LRU can be the worst possible policy for a loop slightly larger than the cache, where it evicts exactly the line needed next.
- **"Caches store variables."** They store fixed-size, aligned lines of bytes; two unrelated variables in the same line share its fate, which causes false sharing on multicores.

## Go deeper

- Smith, *Cache Memories* (ACM Computing Surveys, 1982): the classic survey of design choices.
- Hill and Smith, *Evaluating Associativity in CPU Caches* (IEEE Transactions on Computers, 1989): source of the 3 Cs model.
- Hennessy and Patterson, *Computer Architecture: A Quantitative Approach* (6th ed., 2017), Appendix B and Chapter 2: cache optimisations with data.
- Jaleel et al., *High Performance Cache Replacement Using Re-Reference Interval Prediction (RRIP)* (ISCA 2010): a modern replacement policy.
