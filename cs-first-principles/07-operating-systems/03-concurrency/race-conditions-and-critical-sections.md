# Race Conditions and Critical Sections

> **Layer:** [07 Operating Systems](../README.md) › [Concurrency](README.md)
> **Builds on:** [Threads](../02-process-management/threads.md), [Memory consistency models](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md), [Correctness and invariants](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md)
> **Enables:** [Locks and semaphores](locks-and-semaphores.md), [Lock-free synchronization](lock-free-synchronization.md), [Concurrency control](../../09-data-management/04-transactions/concurrency-control.md)

## Essence

A **race condition** is a bug where a program's result depends on the timing of operations in concurrent threads. It arises when two or more threads access the same data, at least one writes, and nothing forces an order between them. The fix is to identify each **critical section** (a stretch of code that accesses shared data and must not run concurrently with other critical sections on the same data) and make it execute as if it were indivisible. Any solution must provide mutual exclusion without deadlocking or starving anyone, and it must work despite preemption at any instruction and despite hardware that reorders memory operations.

## Core tenets

1. **High-level statements are not atomic.** `counter++` compiles to load, add, store. If two threads both load 5, both add 1 and both store 6, one increment is lost. The scheduler can switch threads between any two machine instructions, and on multiple cores the instructions truly overlap. Two threads each incrementing a shared counter a million times routinely produce a total well below two million.

   ```
   T1: load r=5         T2: load r=5
   T1: r=6              T2: r=6
   T1: store 6          T2: store 6      -> one update lost
   ```

2. **A data race needs three ingredients, and removing any one cures it.** Shared data, at least one writer, and no enforced ordering. So: do not share (give each thread private data and combine at the end), do not mutate (immutable data is safe to share freely), or enforce order (locks, atomics, message passing). Functional languages and Rust's ownership rules attack the first two at compile time.

3. **A correct critical-section solution has three properties.** *Mutual exclusion*: at most one thread is in the critical section. *Progress*: if none is inside and some want in, one gets in (no livelock by indecision). *Bounded waiting*: a thread that asks will get in after a bounded number of others go first (no starvation). Dijkstra posed this problem in 1965; Peterson's 1981 algorithm solves it for two threads using only ordinary loads and stores.

4. **Software-only solutions fail on modern hardware without fences.** Peterson's algorithm assumes sequential consistency: that each thread's loads and stores happen in program order and are seen in one global order. Real processors and compilers reorder: x86 lets a later load pass an earlier store to a different address, and ARM and POWER reorder much more. That reordering breaks Peterson's algorithm unless memory fences are inserted ([memory consistency models](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md)). This is why practical synchronization relies on hardware atomic instructions with defined ordering.

5. **Atomicity and ordering are separate guarantees, and both are needed.** Atomicity means an operation is not observed half-done. Ordering means other threads see writes in a sensible order relative to other writes. A lock provides both: acquire acts as a barrier so the critical section's accesses cannot move above it, and release makes them visible before the lock appears free. Language memory models (C11, C++11, Java) define a data race as conflicting accesses not ordered by *happens-before*; in C and C++ such a race makes the whole program's behaviour undefined.

6. **Check-then-act is a race even when each step is safe.** `if (!exists(file)) create(file)` or `if (balance >= x) balance -= x` can fail when another thread acts between the check and the act. The critical section must cover the whole compound operation that maintains the invariant, not each access separately. In the kernel, the same pattern across the user/kernel boundary is the time-of-check-to-time-of-use (TOCTOU) vulnerability.

7. **Races are hard to find because they are rare and timing-dependent.** A race window may be a few nanoseconds wide and appear once in millions of runs, and adding logging changes the timing (a "Heisenbug"). The Therac-25 radiation overdoses (1985–1987) were caused partly by a race triggered only by fast operator input. Tools help: dynamic race detectors such as ThreadSanitizer track happens-before at run time, and static analysis or [model checking](../../06-programming-languages/05-formal-methods/model-checking.md) can explore interleavings systematically.

## Key concepts

| Term | Meaning |
|---|---|
| Race condition | Outcome depends on the relative timing of concurrent operations |
| Data race | Two unordered accesses to the same location, at least one a write |
| Critical section | Code that accesses shared state and must execute without interference |
| Mutual exclusion | At most one thread in a critical section at a time |
| Atomic operation | An operation that other threads observe as all-or-nothing |
| Happens-before | The partial order of events that a memory model guarantees threads observe |
| Memory fence (barrier) | An instruction that prevents reordering of memory operations across it |
| TOCTOU | Time-of-check-to-time-of-use: a check invalidated before its result is used |

## How it fits

- **Below:** the problem exists because of preemptive [threads](../02-process-management/threads.md) and [multicore hardware](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md); its solutions are bounded by the [memory consistency model](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md).
- **Above:** databases restate the problem as isolation between transactions ([concurrency control](../../09-data-management/04-transactions/concurrency-control.md), [isolation levels](../../09-data-management/04-transactions/isolation-levels.md)); distributed systems restate it across machines without shared memory ([time, clocks and ordering](../../10-distributed-and-parallel-computing/02-distributed-foundations/time-clocks-and-ordering.md)).
- **Siblings:** [locks and semaphores](locks-and-semaphores.md) and [lock-free synchronization](lock-free-synchronization.md) are the two families of solution; [condition variables](condition-variables-and-monitors.md) handle waiting for state; [deadlock](deadlock.md) is the price of locking.

## Common misconceptions

- **"`volatile` makes a variable thread-safe."** In C and C++ `volatile` stops the compiler caching a value in a register but gives neither atomicity nor inter-thread ordering; use atomics or locks. (Java's `volatile` does give ordering, but `count++` on it is still not atomic.)
- **"If tests pass, there is no race."** Races may need an interleaving that occurs once in millions of runs or only on a different processor; absence of failures is not evidence of absence.
- **"Reads never need protection."** A read concurrent with a write can see a torn or stale value, and a read used to make a decision is part of a check-then-act.

## Go deeper

- Edsger W. Dijkstra, "Solution of a Problem in Concurrent Programming Control" (1965): the critical-section problem stated and solved.
- Gary L. Peterson, "Myths About the Mutual Exclusion Problem" (1981): the two-thread algorithm.
- Hans-J. Boehm, "Threads Cannot Be Implemented as a Library" (PLDI 2005): why the language must define a memory model.
- Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (2018), "Concurrency: An Introduction".
