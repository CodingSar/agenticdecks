# I/O and Devices

> **Layer:** [07 Operating Systems](../README.md) › I/O and devices
> **Children:** [Device drivers and interrupt handling](device-drivers-and-interrupt-handling.md) · [I/O models](io-models.md)

## What this area is about

Computers exist to take in and emit data, yet devices are wildly diverse (keyboards, disks, network cards, Graphics Processing Units (GPUs)) and wildly slower or faster than the Central Processing Unit (CPU) expects. This area answers two questions. Inside the kernel: how does the Operating System (OS) talk to a device it may know nothing about, and react when the device has something to say? At the system-call interface: how should a program wait for input/output (I/O) without wasting the CPU or a thread per operation?

The unifying idea is **decoupling the CPU from device time**. Devices work asynchronously, signalling completion with interrupts and moving data by Direct Memory Access (DMA). The OS's job is to hide that asynchrony behind a uniform interface where it helps (a blocking `read`) and to expose it efficiently where programs need it (`epoll`, `io_uring`, I/O completion ports).

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Device drivers and interrupt handling](device-drivers-and-interrupt-handling.md) | The kernel side: driver model, device registers, interrupts, DMA, deferring work | [Buses and interrupts](../../04-computer-architecture/05-io-and-interconnect/buses-and-interrupts.md), [DMA and devices](../../04-computer-architecture/05-io-and-interconnect/dma-and-devices.md) |
| [I/O models](io-models.md) | The program side: blocking, non-blocking, multiplexed, asynchronous I/O | Drivers, [threads](../02-process-management/threads.md) |

```
  application: read() / epoll_wait() / io_uring
  ------------------------------------------------ system call
  VFS / sockets / block layer (queues, scheduling)
  device driver: program registers, set up DMA, sleep
  ------------------------------------------------
  device: transfer by DMA -> raise interrupt
  interrupt handler: acknowledge, defer work -> wake waiting thread
```

Read drivers first: they show where completion events come from. I/O models then show how those events reach programs, and why the right model (thread per connection, event loop, or completion queue) depends on how many operations are in flight at once.

## Connections to sibling areas

- **[Kernel and abstractions](../01-kernel-and-abstractions/README.md):** drivers are most of a monolithic kernel's code and most of its bugs, the main argument for microkernels and user-space drivers.
- **[Process management](../02-process-management/README.md):** blocking I/O moves a thread to the blocked state; the completion interrupt makes it runnable again.
- **[Concurrency](../03-concurrency/README.md):** interrupt handlers run concurrently with the code they interrupt; queues between them are protected by spinlocks with interrupts disabled.
- **[Memory management](../04-memory-management/README.md):** DMA targets physical addresses, so buffers are pinned, and an Input-Output Memory Management Unit (IOMMU) confines devices to permitted memory.
- **[Storage and file systems](../05-storage-and-file-systems/README.md):** the block layer and its request queues connect file systems to storage drivers.
- **[Virtualization](../07-virtualization/README.md):** device emulation, paravirtual drivers (virtio) and device passthrough are the main costs and techniques of virtual I/O.

## Connections across layers

The hardware mechanisms are in [04 Computer Architecture](../../04-computer-architecture/README.md): [buses and interrupts](../../04-computer-architecture/05-io-and-interconnect/buses-and-interrupts.md) and [DMA and devices](../../04-computer-architecture/05-io-and-interconnect/dma-and-devices.md). Upward, the I/O models shape [08 Networking](../../08-networking/README.md) servers ([Hypertext Transfer Protocol (HTTP) and the web](../../08-networking/05-application-layer/http-and-the-web.md)), language async runtimes in [06](../../06-programming-languages/README.md), and [scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md) in large systems.

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): the driver interface hides each device behind a generic class.
- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): DMA and asynchronous I/O overlap device work with computation.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): interrupt coalescing and submission queues amortize per-event costs.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): interrupts versus polling, latency versus CPU efficiency.
