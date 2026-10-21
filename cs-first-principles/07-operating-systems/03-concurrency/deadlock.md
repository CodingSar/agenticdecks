# Deadlock

> **Layer:** [07 Operating Systems](../README.md) › [Concurrency](README.md)
> **Builds on:** [Locks and semaphores](locks-and-semaphores.md), [Graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md), [Graph traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md)
> **Enables:** [Concurrency control](../../09-data-management/04-transactions/concurrency-control.md), [Distributed transactions](../../10-distributed-and-parallel-computing/04-distributed-data/distributed-transactions.md)

## Essence

A **deadlock** is a state in which a set of threads each waits for a resource held by another thread in the set, so none can ever proceed. The classic case is two threads and two locks: T1 holds A and wants B, T2 holds B and wants A. Coffman and colleagues (1971) showed deadlock requires four conditions at once: mutual exclusion, hold-and-wait, no preemption and circular wait. Every strategy for handling deadlock works by breaking one of the four (prevention), steering around unsafe states (avoidance), or letting it happen and recovering (detection). In practice, Operating Systems (OSs) mostly prevent deadlock in their own code by **lock ordering**, and leave application deadlocks to the application.

## Core tenets

1. **Deadlock requires all four Coffman conditions simultaneously.** *Mutual exclusion*: a resource can be held by only one thread. *Hold and wait*: a thread holds one resource while waiting for another. *No preemption*: resources cannot be taken away; only the holder releases them. *Circular wait*: there is a cycle of threads each waiting for the next. Remove any one and deadlock is impossible, which turns a vague hazard into four concrete design levers.

2. **Deadlock is a cycle in a wait-for graph.** Draw an edge from each waiting thread to the thread holding what it wants. With single-instance resources, a deadlock exists exactly when this graph has a cycle, which [depth-first search](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md) detects in time linear in its size. Database lock managers and the Linux kernel's lockdep validator use this idea.

   ```
   T1 --waits for--> T2        T1 holds A, wants B
    ^                 |        T2 holds B, wants A
    +---waits for-----+        cycle => deadlock
   ```

3. **A global lock order breaks circular wait, and it is the workhorse in practice.** If every thread acquires locks in the same total order (by rank, or by address), no cycle can form, because a cycle would require some thread to acquire a lower-ranked lock while holding a higher one. The Linux kernel documents its lock orderings and its lockdep tool records every observed acquisition order at run time and warns when two orders conflict, catching potential deadlocks even if they never actually happened during the test.

4. **The other conditions can be broken too, at a price.** Breaking *hold and wait*: acquire all locks at once, or release everything and retry if any lock is busy (`trylock` with backoff), which can livelock. Breaking *no preemption*: let the system abort a holder and roll it back, which needs a way to undo work, as database transactions have. Breaking *mutual exclusion*: use lock-free data structures or immutable data, so there is nothing to hold.

5. **Avoidance needs knowledge the OS rarely has.** Dijkstra's banker's algorithm grants a request only if the system remains in a *safe state*, one from which some order lets every thread finish given its declared maximum claims. It is elegant but requires every thread to declare its maximum needs in advance and a fixed set of resources, so general-purpose OSs do not use it.

6. **Detection and recovery is the database approach.** A database lock manager lets transactions block freely, periodically searches the wait-for graph or uses timeouts, and on finding a cycle aborts one victim, whose effects are undone using the log. This works because transactions are designed to be abortable. Distributed systems often use timeouts instead, since a global wait-for graph is costly to assemble.

7. **Many systems simply ignore application deadlock.** Unix and Windows do not detect deadlock among user threads; they rely on programmers. This "ostrich algorithm" is a reasonable engineering choice when deadlocks are rare and detection is expensive. The kernel, by contrast, cannot afford it, which is why it invests in lock ordering and lockdep.

8. **Deadlock is one of several liveness failures.** In *livelock*, threads keep changing state in response to each other (both back off and retry in lockstep) without progress. In *starvation*, one thread waits indefinitely while others proceed. Priority inversion can look like deadlock but resolves when the low-priority holder finally runs. Randomized backoff breaks livelock; fair queuing breaks starvation.

## Key concepts

| Term | Meaning |
|---|---|
| Deadlock | A set of threads each waiting for a resource held by another in the set |
| Coffman conditions | Mutual exclusion, hold-and-wait, no preemption, circular wait |
| Wait-for graph | Directed graph with an edge from each waiter to the holder it waits on |
| Lock ordering | Acquiring locks in one global order to make cycles impossible |
| Safe state | A state from which some execution order lets all threads finish |
| Banker's algorithm | Avoidance algorithm that grants requests only if the state stays safe |
| Livelock | Threads active but making no progress |
| Starvation | A thread indefinitely denied a resource others obtain |

## How it fits

- **Below:** formalized with [graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md); detection is [graph traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md) for cycles.
- **Above:** databases handle it with detection and abort ([concurrency control](../../09-data-management/04-transactions/concurrency-control.md)); distributed transactions face distributed deadlock and blocking during commit ([distributed transactions](../../10-distributed-and-parallel-computing/04-distributed-data/distributed-transactions.md)); [model checking](../../06-programming-languages/05-formal-methods/model-checking.md) finds deadlocks in protocol designs.
- **Siblings:** deadlock is the hazard of [locks](locks-and-semaphores.md) and of waiting on [condition variables](condition-variables-and-monitors.md) while holding a second lock; [lock-free synchronization](lock-free-synchronization.md) avoids it by giving up mutual exclusion.

## Common misconceptions

- **"Deadlock needs many threads."** Two threads and two locks suffice; a single thread can even deadlock itself by re-acquiring a non-recursive lock it already holds.
- **"Timeouts fix deadlock."** They convert a hang into an error that must be handled, and if every party retries in step, into livelock.
- **"If the code has never deadlocked, it is deadlock-free."** The cycle may require a rare interleaving; tools like lockdep check orderings, not just observed hangs.

## Go deeper

- E. G. Coffman, M. J. Elphick and A. Shoshani, "System Deadlocks" (ACM Computing Surveys, 1971): the four conditions.
- Edsger W. Dijkstra, "Cooperating Sequential Processes" (1965): the banker's algorithm.
- Abraham Silberschatz, Peter B. Galvin and Greg Gagne, *Operating System Concepts* (10th ed., 2018), deadlock chapter: systematic treatment of prevention, avoidance and detection.
