# Concurrency

> **Layer:** [07 Operating Systems](../README.md) › Concurrency
> **Children:** [Race conditions and critical sections](race-conditions-and-critical-sections.md) · [Locks and semaphores](locks-and-semaphores.md) · [Condition variables and monitors](condition-variables-and-monitors.md) · [Deadlock](deadlock.md) · [Lock-free synchronization](lock-free-synchronization.md)

## What this area is about

When several threads share memory, the result of a program can depend on the order in which their instructions interleave, and that order is chosen by the scheduler and the hardware, not by the programmer. This area answers: how do you write code that is correct under *every* interleaving? The Operating System (OS) is both the main supplier of the answer (it provides the primitives) and its hardest customer (the kernel itself runs on every core and is interrupted at any moment).

The unifying idea is **atomicity built from a tiny hardware primitive**. The hardware guarantees that a few instructions (atomic exchange, compare-and-swap, load-linked/store-conditional) cannot be interleaved. Everything else (locks, semaphores, condition variables, monitors, lock-free queues) is built on those instructions plus the kernel's ability to put a waiting thread to sleep.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Race conditions and critical sections](race-conditions-and-critical-sections.md) | The problem: what goes wrong and what a solution must guarantee | [Threads](../02-process-management/threads.md) |
| [Locks and semaphores](locks-and-semaphores.md) | Mutual exclusion, built from atomic instructions and sleeping | Race conditions |
| [Condition variables and monitors](condition-variables-and-monitors.md) | Waiting for a *condition*, not just for exclusive access | Locks |
| [Deadlock](deadlock.md) | The failure mode of using locks: cycles of waiting | Locks |
| [Lock-free synchronization](lock-free-synchronization.md) | Correctness without locks, via atomic read-modify-write and memory ordering | Race conditions, hardware atomics |

```
   hardware atomics (CAS, xchg, LL/SC) + memory fences
        |                         \
     spinlock --+--> mutex (sleep) \--> lock-free structures
                |        |
            semaphore  condition variable --> monitor
                         \_______ misuse ______/
                                deadlock
```

Read race conditions first: it states the correctness requirements (mutual exclusion, progress, bounded waiting). Locks satisfy mutual exclusion; condition variables add *ordering* (wait until something is true); deadlock is what happens when locks are combined carelessly. Lock-free synchronization is the alternative path that avoids blocking altogether, at the price of reasoning directly about memory ordering.

## Connections to sibling areas

- **[Kernel and abstractions](../01-kernel-and-abstractions/README.md):** interrupts are a source of concurrency inside the kernel; a handler can interrupt kernel code holding a lock, so kernels disable interrupts or use special locks around shared data.
- **[Process management](../02-process-management/README.md):** threads create the problem; the scheduler's ability to block and wake threads is what lets locks sleep instead of spin.
- **[Memory management](../04-memory-management/README.md):** page tables and allocator free lists are shared kernel structures protected by these primitives; Linux's read-copy-update (RCU) is heavily used in memory management.
- **[Storage and file systems](../05-storage-and-file-systems/README.md):** inode and directory locks, and the ordering of writes for crash consistency, are concurrency problems against a device.
- **[Input/output (I/O) and devices](../06-io-and-devices/README.md):** producer-consumer queues between interrupt handlers and drivers are the classic condition-variable pattern.
- **[Virtualization](../07-virtualization/README.md):** a virtual CPU can be descheduled while its guest holds a spinlock (lock-holder preemption), so hypervisors and guests cooperate with paravirtual spinlocks.

## Connections across layers

The foundation is in [04 Computer Architecture](../../04-computer-architecture/README.md): [cache coherence](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md) makes atomics possible and [memory consistency models](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md) say when writes become visible. [06 Programming Languages](../../06-programming-languages/README.md) exposes these as language memory models and verifies them with [model checking](../../06-programming-languages/05-formal-methods/model-checking.md). The same problems reappear at larger scale: [concurrency control](../../09-data-management/04-transactions/concurrency-control.md) in databases and [consensus](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md) in distributed systems.

## Cross-cutting threads

- [State and time](../../CROSS-CUTTING.md#state-and-time): the whole area is about who changes shared state, and in what order.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): locks protect invariants; condition variables wait for them.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): spinning versus sleeping, coarse versus fine-grained locks.
- [Composition](../../CROSS-CUTTING.md#composition): lock-based code does not compose; deadlock is the symptom.
