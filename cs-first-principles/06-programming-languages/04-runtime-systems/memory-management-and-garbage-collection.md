# Memory Management and Garbage Collection

> **Layer:** [06 Programming Languages](../README.md) › [Runtime Systems](README.md)
> **Builds on:** [Graph traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md), [Amortized analysis](../../05-algorithms-and-data-structures/01-foundations/amortized-analysis.md), [Locality and caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md), [Binding, scope and closures](../02-semantics-and-types/binding-scope-and-closures.md)
> **Enables:** [Memory-safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md), [Memory allocation](../../07-operating-systems/04-memory-management/memory-allocation.md), [Reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md)

## Essence

Programs create data whose lifetime does not follow the call stack: objects shared between parts of a program, closures that outlive their scope, nodes in a growing graph. Such data lives on the heap, and something must decide when each heap object can be freed. Manual management (C's `malloc` and `free`) leaves that to the programmer, who gets it wrong in two ways: freeing too late leaks memory, and freeing too early leaves dangling pointers that corrupt memory and enable exploits. Automatic memory management, or garbage collection (GC), replaces the question "is this object still needed?", which is undecidable, with "is this object still reachable from the program's roots?", which can be computed by graph traversal. The single idea is **reachability as a safe approximation of liveness**: anything unreachable can never be used again, so reclaiming it is always safe.

## Core tenets

1. **Stack, static and heap storage exist because lifetimes differ.** Static data lives for the whole run; stack data lives exactly as long as its procedure call, so last-in first-out allocation is free. Heap data has lifetimes known only at run time, and that is the only part that needs a manager. Escape analysis moves non-escaping objects back onto the stack.
2. **Manual management fails in characteristic ways.** Use-after-free, double free and leaks are the classic bugs. The first two are among the most exploited [memory-safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md): about 70% of serious security bugs in large C and C++ codebases such as Chrome and Windows have been memory-safety bugs, according to both Google and Microsoft. GC eliminates use-after-free and double free by construction.
3. **Reference counting reclaims immediately but cannot collect cycles.** Each object counts the references to it and is freed when the count reaches zero. Reclamation is prompt and incremental, which suits Python, Swift and C++'s `shared_ptr`. But two objects that point to each other never reach zero, so cycles leak unless a backup tracing collector or weak references handle them, and every pointer update costs a counter update (an atomic one, if threads share objects).
4. **Tracing collectors find the live set by graph traversal.** Starting from roots (registers, stack slots, globals), mark every reachable object, then reclaim the rest. Mark-sweep frees unmarked objects in place, which can fragment memory. Copying collectors (Cheney, 1970) move live objects into a fresh space, compacting them for free; their cost is proportional to live data, not heap size, but they need spare space.

   ```
   roots --> A --> B        mark: A, B, D reachable
             |              sweep: C, E unreachable -> freed
             v              (C <-> E is a cycle: refcounting would leak it)
             D      C <-> E
   ```

5. **The generational hypothesis makes tracing cheap.** Most objects die young (Ungar, 1984; Lieberman and Hewitt, 1983). A generational collector allocates into a small nursery and collects it often; since few objects survive, each minor collection copies little. Survivors are promoted to an old generation collected rarely. A write barrier records pointers from old objects to young ones so the nursery can be collected without scanning the whole heap.
6. **Allocation with a compacting collector is a pointer bump.** Because the nursery is contiguous free space, allocating an object is incrementing a pointer and checking a limit, a handful of instructions. This is often cheaper than `malloc`, which must search free lists, and the cost of reclamation is [amortised](../../05-algorithms-and-data-structures/01-foundations/amortized-analysis.md) over many allocations.
7. **Every collector trades throughput, pause time and memory overhead.** Stop-the-world collectors are simplest and have the best throughput but pause the program. Concurrent and incremental collectors (Java's G1, ZGC, Go's collector) do most work alongside the program, using barriers to track mutations, and achieve pauses of around a millisecond or less at the cost of extra Central Processing Unit (CPU) work and memory headroom. Tracing collectors typically need the heap to be a few times larger than the live data to run efficiently.
8. **Ownership is a third path: static lifetime checking without a collector.** Rust's compiler tracks which variable owns each heap object and frees it when the owner goes out of scope; borrowing rules forbid dangling references and data races at compile time. This gives manual-management performance and memory safety, at the cost of a stricter programming model.

## Key concepts

| Term | Meaning |
|---|---|
| Heap | Memory for objects whose lifetimes are not tied to procedure calls |
| Root set | References the program can use directly: registers, stack slots, globals |
| Reachability | An object is reachable if a chain of references leads to it from a root |
| Reference counting | Freeing an object when the number of references to it drops to zero |
| Mark-sweep | Tracing that marks reachable objects, then frees unmarked ones in place |
| Copying collection | Tracing that evacuates live objects to a new space, compacting them |
| Generational GC | Collecting a young generation often and an old one rarely |
| Write barrier | Code run on pointer stores to keep collector bookkeeping correct |
| Stop-the-world pause | A period when the program is halted so the collector can work |
| Ownership | A static discipline where each object has one owner responsible for freeing it |

## How it fits

- **Below:** Tracing is [graph traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md) over the object graph; GC cost analysis is [amortised](../../05-algorithms-and-data-structures/01-foundations/amortized-analysis.md). Compaction improves [locality](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md); scanning a large heap pollutes caches. Concurrent collectors must respect the hardware [memory consistency model](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md). The need for a heap comes from [escaping closures and objects](../02-semantics-and-types/binding-scope-and-closures.md).
- **Above:** Runtimes obtain large regions from the kernel and manage them with techniques shared with operating-system [memory allocation](../../07-operating-systems/04-memory-management/memory-allocation.md). Memory-safe languages remove most [memory-safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md). Pause times appear in tail latency, a concern of [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md).
- **Siblings:** Collectors are built into [virtual machines](interpreters-and-virtual-machines.md) and depend on [just-in-time compilers](jit-compilation.md) to emit barriers and stack maps describing where pointers live in compiled frames.

## Common misconceptions

- **"Garbage collection is slow."** With enough heap headroom, generational GC can match or beat manual allocation in throughput; its real costs are memory overhead and pause unpredictability.
- **"GC prevents memory leaks."** It reclaims unreachable objects; objects kept reachable by mistake (a growing cache, a forgotten listener) leak just as in manual code.

## Go deeper

- Richard Jones, Antony Hosking and Eliot Moss, *The Garbage Collection Handbook* (2nd ed., 2023): the definitive reference.
- David Bacon, Perry Cheng and V. T. Rajan, "A Unified Theory of Garbage Collection" (2004): tracing and reference counting as duals.
