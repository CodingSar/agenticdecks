# Locks and Semaphores

> **Layer:** [07 Operating Systems](../README.md) › [Concurrency](README.md)
> **Builds on:** [Race conditions and critical sections](race-conditions-and-critical-sections.md), [Multicore and cache coherence](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md), [Scheduling](../02-process-management/scheduling.md)
> **Enables:** [Condition variables and monitors](condition-variables-and-monitors.md), [Deadlock](deadlock.md), [Concurrency control](../../09-data-management/04-transactions/concurrency-control.md)

## Essence

A **lock** (mutex) is an object with two operations, acquire and release, that guarantees at most one thread holds it at a time; wrapping a critical section in acquire/release makes it mutually exclusive. Locks are built from a hardware atomic read-modify-write instruction (test-and-set, exchange, compare-and-swap) that lets exactly one thread observe "free" and set "taken" in one indivisible step. A thread that finds the lock taken either **spins** (keeps retrying, cheap if the wait is short) or **sleeps** (asks the kernel to block it until release, cheap if the wait is long). A **semaphore** generalizes the lock to a counter, so it can admit N threads at once or signal events between threads.

## Core tenets

1. **Mutual exclusion needs an atomic read-modify-write.** Ordinary load then store leaves a window in which two threads can both see "free". An instruction such as x86 `xchg` or `lock cmpxchg`, or RISC-V's `amoswap` and load-reserved/store-conditional, reads and writes a location as one step that cache coherence serializes across cores. A minimal spinlock:

   ```c
   void lock(int *l)   { while (atomic_exchange(l, 1) == 1) /* spin */ ; }
   void unlock(int *l) { atomic_store(l, 0); }
   ```

2. **Spinning wastes the Central Processing Unit (CPU); sleeping costs a context switch.** A spinning thread burns its core and, if it preempted the lock holder on a single core, makes no progress at all. Sleeping costs two context switches (microseconds). Spinning is therefore right only when critical sections are very short and the holder is running on another core, which is why kernels use spinlocks for short sections, often with interrupts or preemption disabled so the holder cannot be descheduled.

3. **Practical mutexes spin briefly, then sleep, and enter the kernel only under contention.** Linux's futex ("fast user-space mutex", 2002) keeps the lock word in user memory: an uncontended acquire is one atomic instruction with no system call; only when a thread must wait does it call `futex_wait` to sleep on that address, and the releaser calls `futex_wake`. glibc's `pthread_mutex` and most language mutexes are built this way. Windows offers a similar `WaitOnAddress` and critical-section objects with spin-then-wait behaviour.

4. **Contention, not the lock itself, is what costs performance.** An uncontended lock costs tens of nanoseconds. A contended lock forces the lock's cache line to bounce between cores and serializes threads, so speedup stalls ([Amdahl's law](../../04-computer-architecture/06-performance/amdahls-law.md)). Remedies are finer-grained locks (one per hash bucket rather than one per table), reader-writer locks when reads dominate, per-CPU data that needs no lock, and queue-based locks (MCS locks, named after Mellor-Crummey and Scott, used inside Linux's qspinlock) where each waiter spins on its own cache line.

5. **Fairness must be designed in.** A plain test-and-set lock lets whichever core happens to win the cache line take it, so one thread can starve. Ticket locks hand out increasing numbers and serve them in order, giving first-come-first-served fairness. Strict fairness can hurt throughput (a lock convoy, where every release forces a handoff to a sleeping thread), so many mutexes allow limited barging.

6. **A semaphore is a counter with blocking.** Dijkstra's semaphore (1965) supports `P` (wait: decrement, block if the result would be negative) and `V` (signal: increment, wake one waiter). Initialized to 1 it is a lock; initialized to N it limits concurrency to N (a connection pool); initialized to 0 it lets one thread wait for an event another thread signals. The classic bounded buffer uses three: a mutex, a count of empty slots and a count of full slots.

7. **Semaphores are powerful but unstructured.** Unlike a lock, a semaphore has no owner: any thread may signal it, so a missing or extra `V` anywhere in the program corrupts the protocol, and priority inheritance cannot be applied. That is why modern code uses mutexes for exclusion and [condition variables](condition-variables-and-monitors.md) for waiting, and reserves semaphores for counting resources.

8. **Locks protect invariants, not variables.** The rule is: every access to the data covered by an invariant happens while holding the lock that guards it. Documenting which lock guards which data (annotations like Clang's `GUARDED_BY`) and acquiring locks in a consistent global order are the habits that keep large lock-based systems such as the Linux kernel manageable.

## Key concepts

| Term | Meaning |
|---|---|
| Mutex | A lock providing mutual exclusion, usually sleeping when contended |
| Spinlock | A lock whose waiters busy-wait |
| Test-and-set / exchange | Atomically write a value and return the old one |
| Compare-and-swap (CAS) | Atomically replace a value only if it equals an expected value |
| Futex | Linux primitive: user-space atomic fast path, kernel sleep/wake slow path |
| Reader-writer lock | Many concurrent readers or one writer |
| Ticket lock | A FIFO (First In, First Out) spinlock using a counter of issued and served tickets |
| Semaphore | An integer with atomic wait (decrement/block) and signal (increment/wake) |
| Contention | Several threads trying to take the same lock at once |

## How it fits

- **Below:** atomic instructions and [cache coherence](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md) make locks possible; the [scheduler](../02-process-management/scheduling.md) makes sleeping possible.
- **Above:** databases use lock managers for [two-phase locking](../../09-data-management/04-transactions/concurrency-control.md); distributed systems build leases and lock services on [consensus](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md); language runtimes expose `synchronized`, `Mutex<T>` and friends.
- **Siblings:** [condition variables](condition-variables-and-monitors.md) add waiting for a condition; [deadlock](deadlock.md) is the main hazard of using several locks; [lock-free synchronization](lock-free-synchronization.md) avoids locks entirely.

## Common misconceptions

- **"Locks are slow."** Uncontended locks are cheap; the cost is contention and the serialization it implies.
- **"A spinlock is always faster than a mutex."** Only if the holder is running and the wait is shorter than a context switch; otherwise spinning wastes the very CPU the holder needs.
- **"A binary semaphore is the same as a mutex."** A semaphore has no owner, so any thread can release it; a mutex is released by its holder, which enables priority inheritance and error checking.

## Go deeper

- Edsger W. Dijkstra, "Cooperating Sequential Processes" (1965): introduces semaphores.
- John M. Mellor-Crummey and Michael L. Scott, "Algorithms for Scalable Synchronization on Shared-Memory Multiprocessors" (1991): MCS locks and why contention kills.
- Ulrich Drepper, "Futexes Are Tricky" (2004): how real mutexes are built on futexes.
- Maurice Herlihy and Nir Shavit, *The Art of Multiprocessor Programming* (2008): locks and their theory.
