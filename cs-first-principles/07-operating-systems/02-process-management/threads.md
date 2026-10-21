# Threads

> **Layer:** [07 Operating Systems](../README.md) › [Process management](README.md)
> **Builds on:** [Processes](processes.md), [Multicore and cache coherence](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md), [Stacks and queues](../../05-algorithms-and-data-structures/02-fundamental-data-structures/stacks-and-queues.md)
> **Enables:** [Race conditions and critical sections](../03-concurrency/race-conditions-and-critical-sections.md), [Scheduling](scheduling.md), [Parallel programming models](../../10-distributed-and-parallel-computing/01-parallel-computing/parallel-programming-models.md), [I/O models](../06-io-and-devices/io-models.md)

## Essence

A thread is a single sequential flow of control: a program counter, a register set and a stack. A process may contain many threads that share its address space, heap, global variables and open files, while each has its own stack and registers. Threads exist to separate *who owns resources* (the process) from *who executes* (the thread). That separation gives two things: **parallelism**, because threads of one process can run on several cores at once, and **overlap**, because one thread can block on I/O while another computes. The price is that shared memory without isolation makes every shared variable a potential race.

## Core tenets

1. **Threads share everything except their execution context.** All threads of a process see the same code, globals, heap and file descriptors. Each has its own registers, stack, and thread-local storage. Creating a thread therefore needs only a new stack and a kernel record, not a new address space, which makes thread creation and thread switching much cheaper than process creation and switching (no page-table change, so the Translation Lookaside Buffer (TLB) stays warm).

2. **Threads let a program use multiple cores.** A single-threaded process can occupy at most one core no matter how many exist. Since roughly 2005, when clock speeds stopped rising and core counts started to grow ([power and the end of scaling](../../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md)), threads (or multiple processes) became the only way for one program to get faster on new hardware. Their benefit is bounded by the serial fraction of the work ([Amdahl's law](../../04-computer-architecture/06-performance/amdahls-law.md)).

3. **Threads let a program overlap waiting with work.** A server that handles each request in its own thread can block on a disk read or a network reply in one thread while others continue. This keeps sequential, readable code ("read request, query database, write reply") while still serving many clients. The alternative is event-driven code that never blocks ([I/O models](../06-io-and-devices/io-models.md)).

4. **Kernel threads and user threads differ in who schedules them.** A *kernel* thread is known to the Operating System (OS), which schedules it on cores and can run it in parallel; Linux implements threads as tasks that share an address space (`clone` with `CLONE_VM`), so its threads and processes are the same kernel object with different sharing. *User-level* (green) threads are multiplexed by a runtime library onto kernel threads; they switch in tens of nanoseconds without a system call but cannot run in parallel unless mapped onto several kernel threads, and one blocking system call can stall them all. Modern runtimes use an M:N mapping: Go's goroutines and Java's virtual threads (Java Development Kit (JDK) 21) multiplex millions of lightweight threads onto a few kernel threads.

5. **Each thread's stack holds its private call history.** Local variables and return addresses live on the thread's stack, typically a few kilobytes to 8 MB of reserved virtual memory per thread on Linux. Data on one thread's stack is private only by convention: another thread holding a pointer can still read it, because the address space is shared. Thread-local storage gives each thread its own copy of a global (`errno` is thread-local in modern C libraries).

6. **Preemption makes interleaving arbitrary.** The scheduler may stop a thread between any two instructions, and on a multicore machine threads run truly simultaneously. Hence a statement like `count++`, which compiles to load, add and store, can lose updates when two threads execute it together. Correctness must hold under every possible interleaving, which is the subject of [concurrency](../03-concurrency/README.md).

7. **Fewer, well-used threads often beat many.** Each kernel thread costs memory (stack plus kernel structures) and scheduling work, and context switches cost microseconds plus cache disruption. Thread pools cap the number of threads near the core count for Central Processing Unit (CPU)-bound work, and asynchronous I/O or lightweight runtime threads handle very large numbers of concurrent connections.

## Key concepts

| Term | Meaning |
|---|---|
| Thread | An independent flow of control with its own registers and stack, inside a process |
| Kernel thread | A thread the OS kernel schedules directly |
| User-level (green) thread | A thread scheduled by a user-space runtime, invisible to the kernel |
| M:N threading | Multiplexing M user threads onto N kernel threads |
| Thread-local storage | Per-thread copies of variables that look global |
| Thread pool | A fixed set of worker threads that take tasks from a queue |
| `pthread_create` / `pthread_join` | POSIX (Portable Operating System Interface) calls to start a thread and wait for it to finish |
| Preemption | Involuntary interruption of a running thread by the scheduler |

## How it fits

- **Below:** threads are how software uses [multicore hardware](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md); their view of shared memory is governed by the [memory consistency model](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md).
- **Above:** language runtimes build async/await, actors and goroutines on them ([interpreters and virtual machines](../../06-programming-languages/04-runtime-systems/interpreters-and-virtual-machines.md)); parallel frameworks build task and data parallelism ([data and task parallelism](../../10-distributed-and-parallel-computing/01-parallel-computing/data-and-task-parallelism.md)).
- **Siblings:** [processes](processes.md) supply the isolated container; [scheduling](scheduling.md) chooses among runnable threads. The shared address space is what makes the [concurrency](../03-concurrency/README.md) area necessary.

## Common misconceptions

- **"More threads means more speed."** Beyond the core count, CPU-bound threads only add switching and contention; speedup is capped by the serial fraction and by lock contention.
- **"Threads on a single core cannot race."** Preemption can interleave them at any instruction, so races occur on one core too; multicore only makes them more frequent.
- **"Async code removes the need for threads."** Async runtimes still run on threads; they avoid blocking a thread per connection but CPU-bound work still needs cores.

## Go deeper

- Andrew D. Birrell, "An Introduction to Programming with Threads" (1989): a classic, practical guide.
- John Ousterhout, "Why Threads Are A Bad Idea (for most purposes)" (1996): the counter-argument for events.
- Rob von Behren, Jeremy Condit and Eric Brewer, "Why Events Are A Bad Idea (for high-concurrency servers)" (HotOS 2003): the reply.
