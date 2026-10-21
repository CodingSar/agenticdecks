# Multicore and Cache Coherence

> **Layer:** [04 Computer Architecture](../README.md) › [Parallel Architecture](README.md)
> **Builds on:** [Cache design](../03-memory-hierarchy/cache-design.md), [Finite-state machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md), [Power and the end of scaling](../06-performance/power-and-the-end-of-scaling.md)
> **Enables:** [Memory consistency models](memory-consistency-models.md), [Locks and semaphores](../../07-operating-systems/03-concurrency/locks-and-semaphores.md), [Lock-free synchronization](../../07-operating-systems/03-concurrency/lock-free-synchronization.md), [Threads](../../07-operating-systems/02-process-management/threads.md)

## Essence

A multicore processor puts several complete cores on one chip, each with private level-1 (L1) and usually level-2 (L2) caches, sharing a last-level cache and main memory. Private caches mean the same memory line can have several copies, and if one core writes its copy, the others become stale. Cache coherence is the hardware protocol that prevents this: it guarantees that all cores see a single, agreed history of writes to each memory location. The usual mechanism is to allow either one writer or many readers of a line at any time, and to invalidate other copies before a write. Coherence makes shared-memory programming possible, but it has a cost in traffic and latency that shapes how fast parallel programs can be.

## Core tenets

1. **Multicore was a response to the power wall, not a preference.** From about 2005, raising a single core's frequency or width cost too much power for the gain, while transistor budgets kept doubling. Putting two, then four, then dozens of cores on a die (64–192 cores in mid-2020s server chips such as AMD EPYC and Ampere) turns transistors into throughput, but only for software that exposes thread-level parallelism.

2. **Coherence is defined per location.** A memory system is coherent if, for each location, (a) a read returns the value of the most recent write in some single global order of writes to that location, and (b) all cores agree on that order. Formally this is the Single-Writer/Multiple-Reader (SWMR) invariant plus a data-value invariant: at any moment a line has either one core allowed to write it or any number allowed only to read it, and a read sees the last write.

3. **MESI is the canonical protocol state machine.** Each cached line is in one of four states: Modified (only copy, dirty), Exclusive (only copy, clean), Shared (possibly other clean copies), or Invalid. A core writing a Shared line must first send an invalidation and wait for others to drop their copies; reading a line that another core holds Modified forces that core to supply or write back the data. Real protocols add states such as Owned (MOESI, AMD) or Forward (MESIF, Intel) to reduce memory traffic.

4. **Snooping broadcasts, directories track.** In snooping protocols every cache watches a shared bus for requests to lines it holds; this is simple but does not scale beyond a few tens of cores because every miss is broadcast to everyone. Directory protocols keep, for each line, a record of which caches hold it and send messages only to them. Large multicores and multi-socket servers use directories (often distributed with the level-3 (L3) cache slices) or snoop filters, connected by on-chip meshes or rings.

5. **Coherence works on lines, so unrelated data can collide (false sharing).** If two threads repeatedly write different variables that happen to share one 64-byte line, the line bounces between their caches on every write, even though they share no data. Performance can drop by an order of magnitude. Padding or aligning per-thread data to line boundaries fixes it.

6. **Sharing is expensive even when correct.** Transferring a line from another core's cache costs tens of nanoseconds on the same chip and over 100 ns across sockets. A lock or counter written by many cores becomes a hot line that serialises them. Scalable software minimises shared writes: per-core counters, partitioned data, read-mostly structures.

7. **Atomic read-modify-write instructions are built on coherence.** Compare-and-swap (x86 `lock cmpxchg`), fetch-and-add, and load-linked/store-conditional (ARM `ldxr`/`stxr`, RISC-V `lr`/`sc`) work by obtaining the line in an exclusive state and holding it for the duration of the operation. Every lock, semaphore and lock-free data structure rests on these instructions.

8. **Memory access is often non-uniform.** In multi-socket systems and large chips, each core is closer to some memory controllers than others. Non-Uniform Memory Access (NUMA) means local Dynamic Random-Access Memory (DRAM) may take about 80–100 ns while remote DRAM takes 1.5–2 times longer. Operating systems and runtimes try to place threads near their data.

## Key concepts

| Term | Meaning |
|---|---|
| Multicore | Several independent processor cores on one chip |
| Cache coherence | Guarantee that all cores agree on the sequence of values of each memory location |
| SWMR invariant | At any time a line has either a single writer or multiple readers |
| MESI | Coherence protocol with Modified, Exclusive, Shared and Invalid line states |
| Snooping | Coherence by broadcasting requests that every cache observes |
| Directory | Per-line record of which caches hold copies, enabling point-to-point coherence messages |
| False sharing | Coherence traffic caused by unrelated data in the same cache line |
| Atomic instruction | Read-modify-write that executes indivisibly with respect to other cores |
| NUMA | Non-Uniform Memory Access: memory latency depends on which core accesses which memory |

## How it fits

- **Below:** coherence extends [cache design](../03-memory-hierarchy/cache-design.md) with sharing states; each line's protocol is a [finite-state machine](../../03-digital-logic/03-sequential-logic/finite-state-machines.md); the motivation is the [power wall](../06-performance/power-and-the-end-of-scaling.md).
- **Above:** [threads](../../07-operating-systems/02-process-management/threads.md), [locks](../../07-operating-systems/03-concurrency/locks-and-semaphores.md), [lock-free algorithms](../../07-operating-systems/03-concurrency/lock-free-synchronization.md) and [race conditions](../../07-operating-systems/03-concurrency/race-conditions-and-critical-sections.md) all assume coherent shared memory; [parallel programming models](../../10-distributed-and-parallel-computing/01-parallel-computing/parallel-programming-models.md) are designed to minimise sharing; coherence is a small, fast, hardware version of [replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md).
- **Siblings:** coherence orders writes to one location; [memory consistency models](memory-consistency-models.md) order operations across locations. Graphics Processing Units (GPUs; see [SIMD and GPUs](simd-and-gpus.md)) offer weaker, explicitly managed coherence to save cost.

## Common misconceptions

- **"Coherent caches mean threads see a consistent view of memory."** Coherence covers one location at a time; two writes to different locations may be observed in different orders by different cores, which is the business of the consistency model.
- **"More cores means proportionally more speed."** Serial sections ([Amdahl's law](../06-performance/amdahls-law.md)), shared-line contention and memory bandwidth limit scaling well before core count does.
- **"Atomic instructions are cheap."** An uncontended atomic on a line already in the local cache costs tens of cycles; a contended one costs a cross-core transfer each time.

## Go deeper

- Nagarajan, Sorin, Hill and Wood, *A Primer on Memory Consistency and Cache Coherence* (2nd ed., 2020): the clearest modern treatment of both topics.
- Papamarcos and Patel, *A Low-Overhead Coherence Solution for Multiprocessors with Private Cache Memories* (ISCA 1984): the Illinois protocol, essentially MESI.
- Culler, Singh and Gupta, *Parallel Computer Architecture: A Hardware/Software Approach* (1999): snooping and directory designs in depth.
