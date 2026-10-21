# Condition Variables and Monitors

> **Layer:** [07 Operating Systems](../README.md) › [Concurrency](README.md)
> **Builds on:** [Locks and semaphores](locks-and-semaphores.md), [Stacks and queues](../../05-algorithms-and-data-structures/02-fundamental-data-structures/stacks-and-queues.md), [Object-oriented](../../06-programming-languages/01-paradigms/object-oriented.md)
> **Enables:** [Device drivers and interrupt handling](../06-io-and-devices/device-drivers-and-interrupt-handling.md), [I/O models](../06-io-and-devices/io-models.md), [Parallel programming models](../../10-distributed-and-parallel-computing/01-parallel-computing/parallel-programming-models.md)

## Essence

Locks stop threads from interfering, but threads also need to **wait for something to become true**: a queue to become non-empty, a child to finish, a buffer to have space. Spinning on a flag wastes the Central Processing Unit (CPU) and races with the writer. A **condition variable** is a queue of sleeping threads, always used with a mutex: `wait(cv, m)` atomically releases the mutex and sleeps, and on wake-up reacquires the mutex; `signal(cv)` wakes one waiter and `broadcast(cv)` wakes all. A **monitor** packages shared data, the lock guarding it and its condition variables into one module whose procedures run under mutual exclusion automatically, so the programmer cannot forget to lock.

## Core tenets

1. **Waiting must release the lock atomically, or a wake-up is lost.** If a thread checks "queue empty", releases the lock, and then goes to sleep as separate steps, a producer can add an item and signal in the gap; the signal finds no sleeper and is lost, and the consumer sleeps forever. `wait` exists to close that gap: releasing the mutex and joining the sleep queue happen as one step from the signaller's point of view.

2. **Always wait in a loop that re-checks the condition.** The canonical pattern is:

   ```c
   pthread_mutex_lock(&m);
   while (!condition)            // not "if"
       pthread_cond_wait(&cv, &m);
   /* condition holds and we hold m */
   pthread_mutex_unlock(&m);
   ```

   The loop is needed because under the usual semantics a woken thread is only made runnable; by the time it reacquires the mutex another thread may have consumed the item. POSIX (Portable Operating System Interface) also permits spurious wake-ups. The loop makes correctness depend only on the condition, not on why the thread woke.

3. **Mesa semantics won over Hoare semantics because they are simpler to implement and more robust.** Under Hoare's original monitors (1974), `signal` hands the lock and CPU directly to the waiter, so the condition is guaranteed true when it runs. Under Mesa semantics (Lampson and Redell, 1980), `signal` is just a hint that moves the waiter to the ready queue and the signaller keeps running. Mesa semantics need the `while` loop but avoid extra context switches and tolerate broadcasts. POSIX threads, Java and C# all use Mesa semantics.

4. **The condition lives in shared state, not in the condition variable.** A condition variable has no memory: signalling with nobody waiting does nothing (unlike a semaphore's `V`, which is remembered in its count). The truth of "queue non-empty" is in the shared data, which is why the waiter checks the data under the lock, and the signaller changes the data under the lock before signalling.

5. **Producer-consumer is the canonical use.** A bounded buffer has two conditions: "not full" (producers wait) and "not empty" (consumers wait). Using two condition variables lets each side wake only the threads that can make progress. This pattern appears everywhere: kernel pipes, input/output (I/O) request queues between drivers and interrupt handlers, thread-pool work queues, and channels in Go.

6. **Use broadcast when you cannot tell which waiter should wake.** If waiters wait for different conditions on the same variable (for example, allocators waiting for different amounts of memory), signalling one may wake a thread that cannot proceed while the right one sleeps. `broadcast` wakes all; each re-checks its own condition. It is always correct under Mesa semantics, at the cost of a thundering herd of wake-ups.

7. **Monitors move synchronization into the language.** Brinch Hansen's Concurrent Pascal and Hoare's monitors made mutual exclusion a property of the module, not something each caller remembers. Java's `synchronized` methods with `wait`/`notify`/`notifyAll` are a direct descendant: every object has an intrinsic lock and one condition queue. Making the compiler enforce the discipline removes a whole class of "forgot to lock" bugs, though not deadlock.

## Key concepts

| Term | Meaning |
|---|---|
| Condition variable | A queue of threads waiting for some condition, used with a mutex |
| `wait(cv, m)` | Atomically release `m` and sleep; reacquire `m` before returning |
| `signal` / `notify` | Wake at least one waiting thread |
| `broadcast` / `notifyAll` | Wake all waiting threads |
| Monitor | A module whose data is accessed only via mutually exclusive procedures, with condition variables |
| Mesa semantics | Signal is a hint; the woken thread must re-check its condition |
| Hoare semantics | Signal transfers control immediately to the woken thread |
| Spurious wake-up | Return from `wait` without a matching signal |
| Lost wake-up | A signal sent before the waiter sleeps, so it is never received |

## How it fits

- **Below:** built from a [mutex](locks-and-semaphores.md) plus the scheduler's ability to block and wake threads ([scheduling](../02-process-management/scheduling.md)); a waiting queue is a [queue](../../05-algorithms-and-data-structures/02-fundamental-data-structures/stacks-and-queues.md).
- **Above:** language concurrency features (Java monitors, Go channels, futures and promises) and [parallel programming models](../../10-distributed-and-parallel-computing/01-parallel-computing/parallel-programming-models.md) are built on this pattern; the encapsulation idea is [object-oriented](../../06-programming-languages/01-paradigms/object-oriented.md) design applied to synchronization.
- **Siblings:** [semaphores](locks-and-semaphores.md) can express the same patterns but remember signals and lack ownership; [deadlock](deadlock.md) can still occur if a thread waits while holding a second lock.

## Common misconceptions

- **"`if (!cond) wait()` is fine if I am careful."** Under Mesa semantics another thread can run between the signal and the wake-up, and spurious wake-ups are allowed; only a loop is correct.
- **"Signalling with no waiter saves the signal for later."** Condition variables are stateless; the signal is dropped. Only the shared state remembers.
- **"Condition variables replace locks."** They require a lock; without it, the check of the condition and the sleep race with the signaller.

## Go deeper

- C. A. R. Hoare, "Monitors: An Operating System Structuring Concept" (1974).
- Butler W. Lampson and David D. Redell, "Experience with Processes and Monitors in Mesa" (1980): why practical monitors use hints.
- Andrew D. Birrell, "An Introduction to Programming with Threads" (1989): idioms and pitfalls of condition variables.
