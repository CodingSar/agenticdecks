# Lock-Free Synchronization

> **Layer:** [07 Operating Systems](../README.md) › [Concurrency](README.md)
> **Builds on:** [Memory consistency models](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md), [Multicore and cache coherence](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md), [Race conditions and critical sections](race-conditions-and-critical-sections.md)
> **Enables:** [Parallel programming models](../../10-distributed-and-parallel-computing/01-parallel-computing/parallel-programming-models.md), [Memory management and garbage collection](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md), [Eventual consistency and CRDTs](../../10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md)

## Essence

Lock-free (more generally, non-blocking) synchronization lets threads share data structures without mutual exclusion. Instead of locking, a thread reads the current state, computes a new state privately, and installs it with a single atomic **compare-and-swap (CAS)** that succeeds only if nobody changed the state in between; if someone did, it retries. Because no thread ever holds a lock, a thread that is preempted, slow or crashed cannot block others, so there is no deadlock and no priority inversion. The price is subtle reasoning: about memory ordering, about the ABA problem, and above all about **when memory can safely be freed**, which leads to schemes like read-copy-update (RCU) and hazard pointers.

## Core tenets

1. **CAS is the universal building block.** `CAS(addr, expected, new)` atomically writes `new` only if `*addr == expected`, and reports whether it did. Herlihy (1991) proved that CAS (and load-linked/store-conditional, LL/SC) has infinite *consensus number*: it can implement any concurrent object for any number of threads without waiting on locks, whereas plain reads and writes, or test-and-set, cannot. A lock-free stack push:

   ```c
   do { old = top; n->next = old; } while (!CAS(&top, old, n));
   ```

2. **Progress guarantees form a hierarchy.** *Blocking* (locks): a stalled thread can stop everyone. *Obstruction-free*: a thread running alone finishes. *Lock-free*: some thread always makes progress, though an individual thread may retry forever. *Wait-free*: every thread finishes in a bounded number of its own steps. Lock-free is the common practical target; wait-free is stronger and usually slower.

3. **Correctness means linearizability.** A concurrent object is linearizable if every operation appears to take effect at one instant (its linearization point, usually the successful CAS) between its call and return, consistent with a sequential specification. This lets programmers reason about a lock-free queue as if it were an ordinary queue. The same definition is used for replicated objects in distributed systems ([consistency models](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consistency-models.md)).

4. **Memory ordering must be explicit.** Without a lock's built-in barriers, the programmer chooses orderings: in C11 and C++11, `memory_order_release` on the store that publishes a node and `memory_order_acquire` on the load that reads it guarantee that the node's contents are visible before the pointer to it. Weaker orderings run faster on ARM and POWER; getting them wrong produces bugs that may never appear on x86, whose model is stronger ([memory consistency models](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md)).

5. **The ABA problem: same value does not mean unchanged.** Thread 1 reads top = A and is preempted; thread 2 pops A, pops B, pushes A back. Thread 1's CAS sees A and succeeds, linking to the now-freed B. Fixes include tagging pointers with a version counter (double-width CAS), using LL/SC (which fails on any intervening write), or ensuring nodes are not reused while anyone may hold a reference.

6. **Safe memory reclamation is the hardest part.** In a lock-free structure, a thread may still be reading a node that another thread has just unlinked, so it cannot be freed immediately. Garbage-collected languages get this for free, which is one reason lock-free structures flourished in Java. Otherwise: *hazard pointers* (Michael, 2004) let readers announce which nodes they are using; *epoch-based reclamation* frees a node only after every thread has passed a quiescent point.

7. **Read-copy-update makes reads almost free.** Linux's RCU, used tens of thousands of times in the kernel, lets readers traverse a structure with no locks, atomics or writes at all. A writer copies the part it changes, publishes the new version with one pointer store, and frees the old version only after a *grace period* in which every Central Processing Unit (CPU) has passed through a quiescent state (for example, a context switch), proving no reader can still hold the old pointer. It suits read-mostly data like routing tables and module lists.

8. **Lock-free is not automatically faster.** CAS on a contended cache line still bounces the line between cores, and retries waste work, so a hot lock-free counter can perform no better than a lock. The benefits are robustness (no deadlock, no lock-holder preemption, usable in interrupt and signal handlers) and scalability for read-mostly or low-contention patterns. Avoiding sharing (per-CPU counters summed on read) often beats both.

## Key concepts

| Term | Meaning |
|---|---|
| Compare-and-swap (CAS) | Atomic "if value equals expected, replace it" |
| LL/SC | Load-linked/store-conditional: the store fails if the location was written since the load |
| Lock-free | Some thread always completes an operation in a finite number of steps |
| Wait-free | Every thread completes each operation in a bounded number of its own steps |
| Linearizability | Each operation appears atomic at a point between its invocation and response |
| ABA problem | A CAS succeeds because a value returned to its old state after changing |
| Hazard pointer | A per-thread published pointer marking a node as in use |
| RCU | Read-copy-update: lock-free readers, deferred reclamation after a grace period |

## How it fits

- **Below:** atomic instructions from [cache coherence](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md) and ordering rules from [memory consistency models](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md).
- **Above:** concurrent collections in language runtimes, work-stealing schedulers ([parallel programming models](../../10-distributed-and-parallel-computing/01-parallel-computing/parallel-programming-models.md)), and garbage collectors ([memory management and garbage collection](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md)). Conflict-free replicated data types ([CRDTs](../../10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md)) push the "no coordination" idea across machines.
- **Siblings:** the alternative to [locks](locks-and-semaphores.md); immune to [deadlock](deadlock.md) but solves the same [race conditions](race-conditions-and-critical-sections.md) problem.

## Common misconceptions

- **"Lock-free means no waiting."** Lock-free threads may retry indefinitely; only wait-free guarantees per-thread bounds.
- **"Atomics make code correct."** Each atomic is indivisible, but a sequence of them is not; the algorithm must still be linearizable and handle ABA and reclamation.
- **"It works on my x86 machine, so it works."** x86's strong ordering hides missing barriers that fail on ARM.

## Go deeper

- Maurice Herlihy, "Wait-Free Synchronization" (1991): consensus numbers and the power of CAS.
- Maurice Herlihy and Jeannette M. Wing, "Linearizability: A Correctness Condition for Concurrent Objects" (1990).
- Paul E. McKenney, *Is Parallel Programming Hard, And, If So, What Can You Do About It?* (free online book): RCU from its main author.
- Maged M. Michael, "Hazard Pointers: Safe Memory Reclamation for Lock-Free Objects" (2004).
