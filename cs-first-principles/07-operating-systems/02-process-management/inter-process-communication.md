# Inter-Process Communication

> **Layer:** [07 Operating Systems](../README.md) › [Process management](README.md)
> **Builds on:** [Processes](processes.md), [Address spaces and paging](../04-memory-management/address-spaces-and-paging.md), [Condition variables and monitors](../03-concurrency/condition-variables-and-monitors.md), [Stacks and queues](../../05-algorithms-and-data-structures/02-fundamental-data-structures/stacks-and-queues.md)
> **Enables:** [I/O models](../06-io-and-devices/io-models.md), [UDP and TCP](../../08-networking/04-transport-layer/udp-and-tcp.md), [Parallel programming models](../../10-distributed-and-parallel-computing/01-parallel-computing/parallel-programming-models.md), [Isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md)

## Essence

Inter-Process Communication (IPC) is the set of kernel-mediated channels that open a controlled hole in the isolation between processes. There are two families. In **message passing** (pipes, sockets, message queues) the kernel copies data from sender to receiver through its own buffer, so the channel also synchronizes them. In **shared memory** the kernel maps the same physical frames into both address spaces once; afterwards the processes communicate at memory speed without the kernel, but must synchronize themselves. **Signals** carry almost no data and serve as asynchronous notifications. The core choice is between copying (safe and simple, slower for bulk data) and sharing (fast, but every concurrency hazard returns).

## Core tenets

1. **Every IPC channel is a hole in isolation, so the kernel controls who can open it.** An anonymous pipe has no name: only its creator and the children that inherit its descriptors across `fork` can use it. Named channels (a named pipe or Unix-domain socket in the file system, a POSIX (Portable Operating System Interface) shared-memory object) are guarded by file permissions. Holding the descriptor is the authority to use it, a simple form of capability.

2. **A pipe is a bounded producer-consumer buffer inside the kernel.** A reader blocks while the buffer is empty, a writer blocks while it is full (64 KiB by default on Linux), and readers see end-of-file once every write end is closed. Writes of at most `PIPE_BUF` bytes (4,096 on Linux; POSIX requires at least 512) are atomic, so several writers do not interleave short messages. Pipes (Doug McIlroy's idea, added to Unix in 1973) let shells compose programs: `grep x log | sort | uniq -c` runs three processes concurrently, with flow control built in.

3. **"Everything is a file descriptor" makes IPC compose with everything else.** Pipes, sockets, terminals and Linux's `eventfd` and `signalfd` all answer `read`, `write`, `close` and `poll`. One [event loop](../06-io-and-devices/io-models.md) can therefore wait on connections, child processes and timers at once, and a program reading standard input works whether fed by a file, pipe or socket. Older System V IPC used a separate key namespace outside this model, one reason it fell out of favour.

4. **Copying versus sharing is the central tradeoff.** Message passing copies data twice (sender to kernel, kernel to receiver) and makes at least one system call per message, so cost grows with size; in return the kernel provides buffering, blocking and a clean handoff. Shared memory (`shm_open` plus `mmap`) costs one setup, then no copies and no system calls per access. The price: the processes face [race conditions](../03-concurrency/race-conditions-and-critical-sections.md) and need process-shared locks or atomics, and a process that crashes mid-update leaves the shared data inconsistent. Hybrids send control messages over a socket and bulk data through a shared ring buffer, as `io_uring` does with the kernel. Pipes and stream sockets are byte streams, so receivers must frame messages; POSIX message queues and datagram sockets keep message boundaries.

5. **Sockets extend the same interface beyond one machine.** A Unix-domain socket can pass open file descriptors (`SCM_RIGHTS`) and the peer's credentials, letting a privileged process hand a sandboxed worker exactly the files it needs. Switching the address family to the Internet Protocol (IP) turns the same `connect`, `read` and `write` code into networked communication ([User Datagram Protocol (UDP) and Transmission Control Protocol (TCP)](../../08-networking/04-transport-layer/udp-and-tcp.md)). The interface is the same; the failure model is not, since a remote peer can vanish or stall silently.

6. **Signals are asynchronous software interrupts with almost no payload.** A signal is a small integer delivered when the target next returns to user mode, interrupting whatever it was doing; a handler may call only async-signal-safe functions. Standard signals are not queued: two pending `SIGCHLD`s collapse into one. `SIGKILL` and `SIGSTOP` cannot be caught, so the kernel keeps final control. Robust programs turn signals into descriptor events (`signalfd` or a self-pipe).

7. **In a microkernel, IPC cost is the system's cost.** When file systems and drivers are user-mode servers ([kernel architectures](../01-kernel-and-abstractions/kernel-architectures.md)), every `read` becomes a request and a reply: at least two traps and two context switches. Mach's general, buffered IPC took on the order of 100 µs on early-1990s hardware. Liedtke (1993) cut that about twentyfold with synchronous rendezvous (no kernel buffering), short messages in registers, and a direct switch to the receiving thread that bypasses the scheduler. L4-family kernels such as seL4 now take hundreds of cycles per call, and bulk data still travels through shared memory. QNX, Android's Binder and macOS's Mach ports are IPC-centric designs in production.

## Key concepts

| Term | Meaning |
|---|---|
| Pipe | One-way, bounded, in-kernel byte buffer between a writer and a reader |
| Unix-domain socket | Local socket supporting streams, datagrams and descriptor passing |
| Shared memory | The same physical frames mapped into several address spaces |
| Message queue | Kernel queue that preserves message boundaries and priorities |
| Signal | Asynchronous notification identified by a small integer |
| `PIPE_BUF` | Largest pipe write guaranteed to be atomic |
| Async-signal-safe | Safe to call from a handler that interrupted arbitrary code |

## How it fits

- **Below:** relies on the isolation of [processes](processes.md) and on [page tables](../04-memory-management/address-spaces-and-paging.md) to map shared frames; a pipe is a kernel [queue](../../05-algorithms-and-data-structures/02-fundamental-data-structures/stacks-and-queues.md) guarded by the [condition-variable](../03-concurrency/condition-variables-and-monitors.md) pattern.
- **Above:** sockets are the entry to [networking](../../08-networking/04-transport-layer/udp-and-tcp.md); message passing versus shared memory is the basic split in [parallel programming models](../../10-distributed-and-parallel-computing/01-parallel-computing/parallel-programming-models.md); browser sandboxes confine renderers and talk to them over IPC ([isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md)).
- **Siblings:** [processes](processes.md) create the isolation IPC crosses; [threads](threads.md) share memory with no IPC at all, faster and riskier; [scheduling](scheduling.md) decides when a woken receiver runs.

## Common misconceptions

- **"Shared memory is always the fastest IPC."** For bulk data, yes; for small, frequent messages the synchronization it needs (and a futex wake-up when the peer sleeps) can make it no faster than a pipe.
- **"Signals are a messaging system."** They carry no data, coalesce when pending and interrupt code at arbitrary points; they are for notification only.

## Go deeper

- W. Richard Stevens, *UNIX Network Programming, Volume 2: Interprocess Communications* (2nd ed., 1999): the classic detailed treatment.
- Michael Kerrisk, *The Linux Programming Interface* (2010): exact Linux semantics of pipes, signals, sockets and POSIX IPC.
- Jochen Liedtke, "Improving IPC by Kernel Design" (SOSP 1993): how microkernel IPC became fast.
