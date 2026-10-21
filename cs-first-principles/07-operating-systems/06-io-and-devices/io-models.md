# I/O Models

> **Layer:** [07 Operating Systems](../README.md) › [I/O and devices](README.md)
> **Builds on:** [Device drivers and interrupt handling](device-drivers-and-interrupt-handling.md), [Threads](../02-process-management/threads.md), [Kernel mode and system calls](../01-kernel-and-abstractions/kernel-mode-and-system-calls.md)
> **Enables:** [HTTP and the web](../../08-networking/05-application-layer/http-and-the-web.md), [Scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md), [Interpreters and virtual machines](../../06-programming-languages/04-runtime-systems/interpreters-and-virtual-machines.md)

## Essence

An input/output (I/O) model is the contract for how a program waits for I/O. In **blocking** I/O, `read` puts the thread to sleep until data arrives: simple, but each in-flight operation needs a thread. In **non-blocking** I/O, calls return immediately with "would block", and the program must find out when to retry. **I/O multiplexing** (`select`, `poll`, Linux `epoll`, the Berkeley Software Distribution (BSD) `kqueue`) lets one thread wait for readiness on thousands of descriptors at once, which gives the **event loop** architecture of nginx and Node.js. **Asynchronous** I/O (Windows I/O Completion Ports, Linux `io_uring`) goes further: the program submits operations and later collects completions, so the kernel does the work while the program does something else. The right model depends on how many operations are in flight and what each costs.

## Core tenets

1. **Blocking I/O plus threads is the simplest correct model, and it scales to a point.** Each connection gets a thread that runs straight-line code (`read`, process, `write`), blocking freely; the kernel's scheduler does the multiplexing. This is easy to write and debug. Its limit is per-thread cost: kilobytes to megabytes of stack, kernel structures, and context switches. Ten thousand mostly idle connections, the "C10K problem" (Kegel, 1999), made this expensive on servers of that era.

2. **Readiness multiplexing lets one thread serve many connections.** `select` and `poll` take the full set of descriptors on every call and scan it, costing O(n) per call. `epoll` (Linux 2.5.44 in 2002, stable in 2.6) and `kqueue` (FreeBSD, 2000) keep the interest set in the kernel and return only descriptors that are ready, so cost scales with activity rather than with connections. An event loop waits on `epoll_wait`, then performs non-blocking reads and writes on ready sockets, and never blocks.

   ```
   loop:
     events = epoll_wait(epfd)          # sleeps until some fd is ready
     for fd in events:
         n = read(fd, buf)              # will not block: data is there
         handle(fd, buf[:n])            # must not block either
   ```

3. **Readiness and completion are different contracts.** Readiness models (epoll) say "a `read` now would not block"; the program still performs the copy itself. Completion models (I/O Completion Ports (IOCP), `io_uring`, POSIX (Portable Operating System Interface) asynchronous I/O (AIO)) say "the operation you submitted has finished, and here is the result". Readiness fits sockets, where "data has arrived" is a real state; it does not fit regular files, which Linux always reports as ready even when a read would wait for the disk. Completion works for both.

4. **Event-driven code trades blocking for inverted control flow.** In an event loop, a computation that waits must be split into callbacks or a state machine, and any accidentally blocking call (a synchronous disk read, a long computation) stalls every connection on that loop. Language features restore sequential-looking code on top: async/await (C#, JavaScript, Rust, Python) compiles a function into a state machine that yields at each `await`, and lightweight threads (Go goroutines, Java virtual threads) let the runtime park a cheap thread on an event loop.

5. **`io_uring` amortizes the boundary crossing with shared rings.** Introduced in Linux 5.1 (2019), `io_uring` shares two ring buffers between the application and kernel: a submission queue and a completion queue. The program writes many requests into the submission ring and makes one system call (or none, with kernel-side polling); the kernel posts results in the completion ring. This batches system calls, works uniformly for files and sockets, and mirrors how Non-Volatile Memory Express (NVMe) hardware queues work. It also enlarged the kernel attack surface, and some environments disable it for that reason.

6. **Copying costs dominate at high bandwidth, so zero-copy paths exist.** A naive file-to-socket transfer copies data from the page cache into user space and back into the kernel. `sendfile` and `splice` move data between descriptors inside the kernel; `mmap` avoids a copy for reads; registered buffers in `io_uring` and kernel-bypass stacks let devices use Direct Memory Access (DMA) straight into application memory.

7. **Choose the model by concurrency level and latency needs.** A handful of concurrent operations: blocking I/O with threads is simplest. Thousands to millions of mostly idle connections: an event loop or lightweight threads on epoll/kqueue. Very high operation rates on fast storage or networks: completion-based submission queues, or polling from dedicated cores. The model is a tradeoff among programmer effort, Central Processing Unit (CPU) efficiency and tail latency.

## Key concepts

| Term | Meaning |
|---|---|
| Blocking I/O | The calling thread sleeps until the operation can complete |
| Non-blocking I/O | Calls return immediately with an error if they would block |
| I/O multiplexing | Waiting on many descriptors at once for readiness (`select`, `poll`, `epoll`, `kqueue`) |
| Readiness notification | Report that an operation would not block now |
| Completion notification | Report that a submitted operation has finished |
| Event loop | A single thread that waits for events and dispatches non-blocking handlers |
| `io_uring` | Linux shared submission/completion ring interface for asynchronous I/O |
| Zero-copy | Moving data without copying it through user-space buffers |

## How it fits

- **Below:** completions originate in [device drivers and interrupt handling](device-drivers-and-interrupt-handling.md); every model pays the cost of [system calls](../01-kernel-and-abstractions/kernel-mode-and-system-calls.md) and relies on the scheduler to sleep and wake [threads](../02-process-management/threads.md).
- **Above:** web servers and proxies ([Hypertext Transfer Protocol (HTTP) and the web](../../08-networking/05-application-layer/http-and-the-web.md)), language async runtimes ([interpreters and virtual machines](../../06-programming-languages/04-runtime-systems/interpreters-and-virtual-machines.md)) and service architectures ([scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md)) are built on these models; [Transmission Control Protocol (TCP) sockets](../../08-networking/04-transport-layer/udp-and-tcp.md) are the main thing multiplexed.
- **Siblings:** [device drivers](device-drivers-and-interrupt-handling.md) face the same interrupt-versus-polling tradeoff inside the kernel that programs face between readiness and completion outside it.

## Common misconceptions

- **"Asynchronous means faster."** Async improves concurrency and CPU efficiency under many waiting operations; for a few operations, blocking code is as fast and simpler.
- **"Non-blocking file reads work like non-blocking socket reads."** On Linux, `O_NONBLOCK` has no effect on regular files; a read can still wait for the disk. Use a thread pool or `io_uring`.

## Go deeper

- W. Richard Stevens, Bill Fenner and Andrew M. Rudoff, *UNIX Network Programming, Volume 1* (3rd ed., 2003): the five I/O models compared.
- Dan Kegel, "The C10K problem" (1999, web article): the motivation for scalable event notification.
- Jens Axboe, "Efficient IO with io_uring" (2019): the design document by its author.
