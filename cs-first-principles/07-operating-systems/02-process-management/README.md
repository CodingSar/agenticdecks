# Process Management

> **Layer:** [07 Operating Systems](../README.md) › Process management
> **Children:** [Processes](processes.md) · [Threads](threads.md) · [Scheduling](scheduling.md)

## What this area is about

This area is how the Operating System (OS) virtualizes the Central Processing Unit (CPU). A machine has a few cores; users want hundreds of programs running at once, each written as if it had a processor to itself. The OS answers with two abstractions and one policy. A **process** is a running program with its own protected address space and resources. A **thread** is a single stream of execution (a program counter, registers and a stack) inside a process. **Scheduling** decides which thread runs on which core, and for how long.

The unifying idea is that execution state is just data. A paused computation is its saved registers plus its memory; the kernel can store it, restore it and switch between many such states fast enough that each appears to run continuously.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Processes](processes.md) | The unit of isolation and resource ownership; creation, the process lifecycle, context switching | [Kernel mode and system calls](../01-kernel-and-abstractions/kernel-mode-and-system-calls.md) |
| [Threads](threads.md) | The unit of execution; several per process sharing one address space | Processes |
| [Scheduling](scheduling.md) | The policy that picks which runnable thread uses each core | Processes, threads |

```
 process  = address space + open files + credentials + one or more threads
 thread   = registers + program counter + stack (+ kernel stack)
 scheduler: runnable threads --(policy)--> cores, re-decided on every
            timer tick, block, wake-up or exit
```

Read processes first: they are the container. Threads split "who owns resources" from "who executes", which is why a web server can run hundreds of threads in one address space. Scheduling is the policy layer on top of the context-switch mechanism, and it is where the OS's competing goals (throughput, latency, fairness) meet.

## Connections to sibling areas

- **[Kernel and abstractions](../01-kernel-and-abstractions/README.md):** the timer interrupt and trap mechanism are what make preemption and context switching possible.
- **[Concurrency](../03-concurrency/README.md):** threads sharing memory create races; preemption at arbitrary instructions is why synchronization is needed even on one core.
- **[Memory management](../04-memory-management/README.md):** each process's address space is a page table; `fork` is cheap because of copy-on-write pages.
- **[Storage and file systems](../05-storage-and-file-systems/README.md):** a process's open-file table holds descriptors that name files, pipes and sockets.
- **[Input/output (I/O) and devices](../06-io-and-devices/README.md):** threads block on I/O and become runnable when the device interrupts; the scheduler is the bridge.
- **[Virtualization](../07-virtualization/README.md):** a virtual CPU is scheduled like a thread by the hypervisor; containers are groups of processes with restricted views.

## Connections across layers

From [04 Computer Architecture](../../04-computer-architecture/README.md) this area takes [multicore processors](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md) and the registers that make up a context. From [05 Algorithms](../../05-algorithms-and-data-structures/README.md) it takes [priority queues](../../05-algorithms-and-data-structures/02-fundamental-data-structures/heaps-and-priority-queues.md) and [online algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/streaming-and-online-algorithms.md). It gives [10 Distributed and Parallel Computing](../../10-distributed-and-parallel-computing/README.md) its basic unit of execution and failure, and [06 Programming Languages](../../06-programming-languages/README.md) runtimes (green threads, async executors) something to multiplex on.

## Cross-cutting threads

- [Virtualization](../../CROSS-CUTTING.md#virtualization): one CPU becomes many processes.
- [State and time](../../CROSS-CUTTING.md#state-and-time): a context switch freezes and restores state at any instruction.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): throughput versus latency, fairness versus priority.
- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): multi-level feedback queues infer a job's nature from its past behaviour.
