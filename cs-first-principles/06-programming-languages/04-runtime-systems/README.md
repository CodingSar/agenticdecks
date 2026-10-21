# Runtime Systems

> **Layer:** [06 Programming Languages](../README.md) › Runtime Systems
> **Children:** [Linking and Loading](linking-and-loading.md) · [Interpreters and Virtual Machines](interpreters-and-virtual-machines.md) · [JIT Compilation](jit-compilation.md) · [Memory Management and Garbage Collection](memory-management-and-garbage-collection.md)

## What this area is about

A compiler finishes its work before the program starts; a runtime system is everything a language implementation still needs while the program runs. Even a C program depends on a runtime: a loader to put it in memory, a dynamic linker to bind library calls, start-up code that sets up the stack and calls `main`, and an allocator behind `malloc`. Managed languages such as Java, C#, Python and JavaScript need far more: an interpreter or virtual machine to execute portable code, a Just-In-Time (JIT) compiler to make it fast, and a garbage collector to reclaim memory automatically.

The unifying idea is **deferring decisions to run time, when more is known**. A linker defers the addresses of library functions until load time, so libraries can be shared and updated. An interpreter defers translation entirely, so code can be portable and start instantly. A JIT compiler defers optimisation until it has seen which types and paths the program actually uses. A garbage collector defers the decision of when memory is dead until it can check reachability directly. Each deferral buys flexibility or information at the cost of run-time work, and the art is in keeping that cost small.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Linking and Loading](linking-and-loading.md) | Combines separately compiled code, resolves names to addresses, maps the program into memory | Code generation, virtual memory |
| [Interpreters and Virtual Machines](interpreters-and-virtual-machines.md) | Executes a program or a portable bytecode directly, without native compilation | Semantics, intermediate representations |
| [JIT Compilation](jit-compilation.md) | Compiles hot code to native instructions at run time, using observed behaviour | Interpreters, the whole compiler pipeline |
| [Memory Management and Garbage Collection](memory-management-and-garbage-collection.md) | Allocates objects and reclaims the ones the program can no longer reach | Graph traversal, the memory hierarchy |

```
 ahead of time:  source --compiler--> object files --linker--> executable
                                                                  |
 run time:              loader + dynamic linker  <----------------+
                              |
         +--------------------+---------------------+
         | native code                              | bytecode
         v                                          v
  processor executes             interpreter --(hot code)--> JIT --> native code
         \                                          /
          +------ heap managed by allocator / garbage collector ------+
```

Read linking and loading first: it applies to every compiled program. Interpreters come next as the simplest way to run code, and JIT compilation is the bridge from an interpreter back to native speed. Memory management is orthogonal to how code executes, but it is central to every managed runtime and interacts with the JIT (which must tell the collector where pointers are) and the loader (which lays out the heap).

## Connections to sibling areas

- **[Paradigms](../01-paradigms/README.md).** Functional and object-oriented languages allocate many small, short-lived objects, which is what generational garbage collectors optimise for. Dynamic dispatch is what JIT inline caches speed up.
- **[Semantics and Types](../02-semantics-and-types/README.md).** An interpreter is an executable semantics. Dynamic typing moves type checks into the runtime; static types let a runtime omit them. Escaping closures are why heap allocation and collection are needed.
- **[Compilers](../03-compilers/README.md).** Compilers produce the object files the linker combines; JIT compilers reuse compiler intermediate representations and back ends at run time. The boundary between "compiler" and "runtime" is a design choice, not a law.
- **[Formal Methods](../05-formal-methods/README.md).** Garbage collectors and JIT compilers are notoriously hard to get right; verified collectors and translation validation apply formal methods to runtimes themselves.

## Connections across layers

Runtimes sit directly on the [Operating System (OS)](../../07-operating-systems/README.md): loaders use [address spaces and paging](../../07-operating-systems/04-memory-management/address-spaces-and-paging.md) and memory-mapped files, garbage collectors and allocators request memory from the kernel and build on [memory allocation](../../07-operating-systems/04-memory-management/memory-allocation.md) techniques, and threads come from [the OS](../../07-operating-systems/02-process-management/threads.md). From [layer 04](../../04-computer-architecture/README.md), runtimes care about the [memory hierarchy](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md) (collector locality), [virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md) and [branch prediction](../../04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md) (interpreter dispatch). Upward, runtimes are [isolation boundaries](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md) (the browser's JavaScript engine is a sandbox), garbage collection removes most [memory-safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md), and collector pauses matter for [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md) of latency-sensitive services.

## Cross-cutting threads

- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): symbol resolution, procedure linkage tables, handles and forwarding pointers.
- [Virtualization](../../CROSS-CUTTING.md#virtualization): a process virtual machine presents a portable machine on top of a real one.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): JIT code caches, inline caches, and the cache effects of garbage collection.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): bump allocation and tracing collectors amortise reclamation over many objects.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): start-up time vs peak speed; throughput vs pause time vs memory overhead.
- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): JITs recompile from profiles; collectors tune heap size from observed pause times.
