# Locality and Caching

> **Layer:** [04 Computer Architecture](../README.md) › [Memory Hierarchy](README.md)
> **Builds on:** [The ISA contract](../01-instruction-set-architecture/the-isa-contract.md), [Electromagnetism and charge](../../00-engineering-foundations/01-physics-of-computation/electromagnetism-and-charge.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md)
> **Enables:** [Cache design](cache-design.md), [Page replacement](../../07-operating-systems/04-memory-management/page-replacement.md), [External-memory and cache-oblivious algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md), [Content delivery and caching](../../08-networking/05-application-layer/content-delivery-and-caching.md)

## Essence

Real programs do not touch memory at random. They reuse data they touched recently (temporal locality) and touch addresses near ones they touched recently (spatial locality). A cache exploits this by keeping copies of recently used neighbourhoods of memory in a small, fast storage close to the processor. If most accesses hit in the cache, the average access time approaches the cache's speed while the capacity is that of the large memory below it. Because fast memory must be small (physics) and slow memory can be large (economics), every level of a computer from registers to content delivery networks is built as a cache of the level beneath.

## Core tenets

1. **Small means fast, and the reason is physical.** Signal delay grows with wire length and capacitance, and a larger memory has longer word and bit lines and more decoding levels. A Static Random-Access Memory (SRAM) array of 32 KiB next to the core answers in about 1 ns; a Dynamic Random-Access Memory (DRAM) chip centimetres away, with gigabytes of capacitor cells, takes about 60–100 ns (2020s figures). Cost per bit runs in the opposite direction, so no single technology is both large and fast.

2. **Temporal locality comes from program structure.** Loops execute the same instructions repeatedly; local variables, loop counters and stack frames are touched again and again; hot data structures (a hash table's bucket array, a tree's root) are revisited. Keeping recently used data close therefore pays off: if it was used once, it is likely to be used again soon.

3. **Spatial locality comes from data layout and sequential code.** Instructions execute mostly in sequence; arrays are traversed element by element; structure fields sit next to each other. Caches therefore fetch whole blocks (lines of 64 bytes on nearly all 2020s Central Processing Units (CPUs)), so one miss brings in the neighbours that are likely to be needed next. This is why traversing a two-dimensional array in the wrong order runs many times slower.

4. **Average Memory Access Time (AMAT) is the governing equation.** AMAT = hit time + miss rate × miss penalty, applied recursively per level. With a 1 ns level-1 (L1) cache, 5% miss rate, 4 ns level-2 (L2) cache, 20% L2 local miss rate and 80 ns DRAM: AMAT = 1 + 0.05 × (4 + 0.2 × 80) = 2 ns. Small changes in miss rate matter enormously because the penalty is so large: with a 1 ns hit time and a 100 ns penalty, dropping from a 99% to a 98% hit rate raises AMAT from 2 ns to 3 ns, a 50% slowdown from a one-point change.

5. **Caches are invisible to correctness but not to performance.** The Instruction Set Architecture (ISA) promises that loads return the last stored value regardless of caching; caches are microarchitecture. But two programs computing the same result can differ by 10x in speed purely through access patterns. Performance-aware code (blocked matrix multiply, structure-of-arrays layouts, B-trees with node size matched to a block) is code written to the hierarchy.

6. **The same principle recurs at every scale.** Registers cache L1, L1 caches L2, DRAM caches pages from storage, the Operating System (OS) page cache caches files, browsers and Content Delivery Networks (CDNs) cache web objects, and databases keep a buffer pool. The questions are always the same: what unit to move, where to put it, what to evict, and how to handle writes.

7. **Locality has a working set, and exceeding it is a cliff.** A program's working set is the data it uses during a phase of execution. If it fits in a level, that level's hit rate is high; if it is even slightly larger, a policy like Least Recently Used (LRU) can evict each item just before it is needed again, and the hit rate collapses. This is why performance often drops sharply, not gradually, as a problem size crosses a cache size, and why thrashing appears in virtual memory.

## Key concepts

| Term | Meaning |
|---|---|
| Temporal locality | Tendency to reuse recently accessed data soon |
| Spatial locality | Tendency to access addresses near recently accessed ones |
| Cache line (block) | Unit of transfer between levels, typically 64 bytes in CPU caches |
| Hit / miss | Whether the requested data is present in the cache |
| Hit time | Time to access data when it is in the cache |
| Miss penalty | Additional time to fetch data from the next level |
| AMAT | Average Memory Access Time = hit time + miss rate × miss penalty |
| Working set | The set of data a program actively uses over an interval |
| Memory wall | The growing gap between processor speed and DRAM latency |

## How it fits

- **Below:** the speed–size tradeoff is set by physics ([electromagnetism](../../00-engineering-foundations/01-physics-of-computation/electromagnetism-and-charge.md), [capacitance and timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md)); the ISA's flat address space is what is being cached.
- **Above:** the Random Access Machine (RAM) model in [models of computation](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md) ignores this; [external-memory algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md) restore it. The OS applies the same logic in [page replacement](../../07-operating-systems/04-memory-management/page-replacement.md); networks apply it in [content delivery](../../08-networking/05-application-layer/content-delivery-and-caching.md); databases in [storage layouts](../../09-data-management/02-storage-and-indexing/storage-layouts.md).
- **Siblings:** [cache design](cache-design.md) turns this principle into hardware; [virtual memory](virtual-memory-hardware.md) uses DRAM as a cache for storage; [DRAM and storage](dram-and-storage-devices.md) explains why the lower levels are slow.

## Common misconceptions

- **"Memory access is O(1)."** In the abstract RAM model, yes; on real hardware a load costs anywhere from 1 ns to 100 ns or more depending on where the data lives, which can dominate the cost of an algorithm.
- **"A bigger cache is always better."** A larger cache has a longer hit time; designers add levels instead of growing L1, because L1 hit time sits on the pipeline's critical path.
- **"Locality is a property of the hardware."** It is a property of the program and its data layout; the hardware only rewards it.

## Go deeper

- Denning, *The Working Set Model for Program Behavior* (CACM, 1968): the original formulation of locality.
- Hennessy and Patterson, *Computer Architecture: A Quantitative Approach* (6th ed., 2017), Chapter 2 and Appendix B: memory hierarchy design with numbers.
- Drepper, *What Every Programmer Should Know About Memory* (2007): a long, practical tour from DRAM cells to cache-friendly code.
- Wulf and McKee, *Hitting the Memory Wall: Implications of the Obvious* (1995): the short paper that named the gap.
