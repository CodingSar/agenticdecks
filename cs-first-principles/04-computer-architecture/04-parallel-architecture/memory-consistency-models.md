# Memory Consistency Models

> **Layer:** [04 Computer Architecture](../README.md) › [Parallel Architecture](README.md)
> **Builds on:** [Multicore and cache coherence](multicore-and-cache-coherence.md), [Superscalar and out-of-order](../02-processor-microarchitecture/superscalar-and-out-of-order.md), [Relations and orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md)
> **Enables:** [Lock-free synchronization](../../07-operating-systems/03-concurrency/lock-free-synchronization.md), [Race conditions and critical sections](../../07-operating-systems/03-concurrency/race-conditions-and-critical-sections.md), [Consistency models](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consistency-models.md), [Syntax and semantics](../../06-programming-languages/02-semantics-and-types/syntax-and-semantics.md)

## Essence

A memory consistency model is the part of the Instruction Set Architecture (ISA) that says which values a load may return when several cores read and write shared memory. The intuitive answer, sequential consistency, says the result must look like some interleaving of each core's operations in program order. Real hardware does not provide this, because store buffers, out-of-order execution and caches would have to be crippled to do so. Instead, ISAs define weaker models (x86's Total Store Order, the much weaker ARM and RISC-V models) and give programmers fences and ordered atomic instructions to restore order where it matters. Programming languages then build their own models (C++11, Java) on top, promising sequential consistency to programs that are free of data races.

## Core tenets

1. **Sequential Consistency (SC) is the reference point.** Lamport (1979) defined it: the result of any execution is the same as if all operations were executed in some single total order, and each core's operations appear in that order in the sequence specified by its program. SC is what most programmers assume, and what makes reasoning about interleavings possible.

2. **Hardware reorders for speed, so SC is expensive.** A store that misses in the cache would stall the core for hundreds of cycles if later loads had to wait for it. Cores therefore put stores in a store buffer and let later loads run ahead. To a single thread this is invisible (loads check the store buffer), but another core can see the effects in a different order than the program wrote them.

3. **Store buffering breaks Dekker-style code under TSO.** Total Store Order (TSO, the model of x86 and SPARC) allows exactly one relaxation: a load may complete before an earlier store to a *different* address becomes visible. In the classic test, thread 1 runs `x = 1; r1 = y` and thread 2 runs `y = 1; r2 = x`, both starting at zero; under TSO both `r1` and `r2` can be 0, an outcome impossible under SC. Peterson's and Dekker's mutual exclusion algorithms fail unless a fence (`mfence`) separates the store from the load.

4. **Weak models allow almost any reordering of independent accesses.** ARMv8, RISC-V's RVWMO and IBM POWER let loads and stores to different addresses be reordered in most ways, as seen by other cores. This permits simpler, faster hardware. Programs that share data must state the ordering they need explicitly.

5. **Fences and ordered atomics restore order at a price.** A full fence forces all earlier memory operations to complete before any later one; it can cost tens to hundreds of cycles. Lighter primitives express only what is needed: acquire (no later access may move before this load) and release (no earlier access may move after this store), provided on ARMv8 as `ldar`/`stlr`. A lock acquire is an acquire, a lock release is a release, and that pairing is enough to make a critical section behave as if under SC.

6. **Languages define models that compilers and hardware must jointly implement.** The compiler also reorders memory operations, so a hardware model alone is not enough. The Java Memory Model (2004) and the C/C++11 model define atomics with orderings (`seq_cst`, `acquire`, `release`, `relaxed`) and promise "SC for data-race-free programs": if all conflicting accesses are synchronised, the program behaves sequentially consistently. Compilers translate each atomic to the appropriate fences for each ISA.

7. **Data races are the boundary of the guarantee.** A data race is two unsynchronised accesses to the same location, at least one a write. In C and C++ a racy program has undefined behaviour; in Java its behaviour is constrained but surprising.

8. **Consistency is not coherence.** Coherence guarantees agreement on the order of writes to a single location; consistency governs the order of operations across different locations. A system can be fully coherent and still show the TSO store-buffering outcome above.

## Key concepts

| Term | Meaning |
|---|---|
| Memory consistency model | Specification of the allowed orders and values of memory operations across threads |
| Sequential consistency | All operations appear in one total order respecting each thread's program order |
| TSO | Total Store Order: SC except that a store may be delayed past later loads (x86, SPARC) |
| Weak / relaxed model | Model permitting most reorderings of independent accesses (ARM, RISC-V, POWER) |
| Store buffer | Queue holding a core's committed stores until they reach the cache |
| Fence (barrier) | Instruction that prevents reordering of memory operations across it |
| Acquire / release | One-directional orderings attached to a load / store, used for synchronisation |
| Data race | Conflicting unsynchronised accesses to one location, at least one a write |
| SC-for-DRF | Guarantee that data-race-free programs behave sequentially consistently |

## How it fits

- **Below:** program order and visibility order are [partial and total orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md); the reorderings come from [store buffers and out-of-order cores](../02-processor-microarchitecture/superscalar-and-out-of-order.md).
- **Above:** [lock-free algorithms](../../07-operating-systems/03-concurrency/lock-free-synchronization.md) and [locks](../../07-operating-systems/03-concurrency/locks-and-semaphores.md) must be written against it; language [semantics](../../06-programming-languages/02-semantics-and-types/syntax-and-semantics.md) and [compiler optimizations](../../06-programming-languages/03-compilers/optimization.md) must respect it; distributed [consistency models](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consistency-models.md) (linearizability, causal, eventual) are the same idea across a network.
- **Siblings:** builds directly on [coherence](multicore-and-cache-coherence.md); Graphics Processing Units (GPUs; see [SIMD and GPUs](simd-and-gpus.md)) use scoped, even weaker models.

## Common misconceptions

- **"`volatile` makes C code thread-safe."** In C and C++ `volatile` prevents some compiler optimisations but provides no atomicity or inter-thread ordering; use atomics. (Java's `volatile` is different and does give ordering.)
- **"x86 is sequentially consistent."** It is TSO; the store-buffering outcome is observable on real x86 hardware.
- **"Code that works on x86 will work on ARM."** Lock-free code that relies, knowingly or not, on TSO can break on weaker ARM and RISC-V cores; this surfaced widely when software moved to Apple Silicon and ARM servers.

## Go deeper

- Lamport, *How to Make a Multiprocessor Computer That Correctly Executes Multiprocess Programs* (IEEE Transactions on Computers, 1979): the definition of sequential consistency.
- Adve and Gharachorloo, *Shared Memory Consistency Models: A Tutorial* (IEEE Computer, 1996): the standard introduction.
- Sorin, Hill and Wood, *A Primer on Memory Consistency and Cache Coherence* (2nd ed., 2020): SC, TSO and relaxed models side by side.
- Boehm and Adve, *Foundations of the C++ Concurrency Memory Model* (PLDI 2008): how a language model is built on hardware models.
