# 07 Operating Systems

> **Layer:** 07 Operating Systems
> **Children:** [Kernel and abstractions](01-kernel-and-abstractions/README.md) · [Process management](02-process-management/README.md) · [Concurrency](03-concurrency/README.md) · [Memory management](04-memory-management/README.md) · [Storage and file systems](05-storage-and-file-systems/README.md) · [I/O and devices](06-io-and-devices/README.md) · [Virtualization](07-virtualization/README.md)

## What this area is about

An Operating System (OS) is the program that turns one bare machine into a safe, shared, convenient one. Bare hardware offers a handful of cores, a flat physical memory, some disks and some devices, all reachable by any instruction that happens to run. Many programs, written by people who do not trust each other, want to use that hardware at once, and each wants to believe it has the machine to itself.

Following Remzi and Andrea Arpaci-Dusseau's *Operating Systems: Three Easy Pieces* (OSTEP), the OS has three jobs:

1. **Virtualize hardware.** Make one Central Processing Unit (CPU) look like many (processes and threads), and make one physical memory look like many private address spaces. Each program gets the illusion of a machine of its own.
2. **Mediate concurrency.** Once many activities share memory and devices, their interleavings create bugs that no single program has. The OS supplies the primitives (locks, condition variables, atomic operations) and uses them on itself, since the kernel is the most concurrent program on the machine.
3. **Provide persistence.** Turn blocks on a device that can lose power at any instant into named files and directories that survive crashes.

All three jobs rest on a single mechanism: the **protection boundary**. The kernel runs with hardware privilege; applications do not. The only ways across are the system call, the interrupt and the exception, each of which enters the kernel at an address the kernel chose. Because of that boundary, the OS can *enforce* its abstractions instead of merely offering them.

## Why this layer sits here

The OS needs three things from [04 Computer Architecture](../04-computer-architecture/README.md): privilege modes in the [Instruction Set Architecture (ISA) contract](../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md), a Memory Management Unit (MMU) that translates every address through tables the kernel controls ([virtual memory hardware](../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md)), and [interrupts](../04-computer-architecture/05-io-and-interconnect/buses-and-interrupts.md) that let a timer or device take the CPU away from running code. Without a timer interrupt the OS could never take back a CPU from a program that loops forever; without an MMU it could not stop one program from writing another's memory.

It needs [06 Programming Languages](../06-programming-languages/README.md) because kernels are programs: written mostly in C (Linux, Windows NT) or verified C (seL4), compiled, and linked ([linking and loading](../06-programming-languages/04-runtime-systems/linking-and-loading.md)). Language runtimes and the OS co-depend: a garbage collector asks the OS for pages, and the OS loads the runtime.

It needs [05 Algorithms and Data Structures](../05-algorithms-and-data-structures/README.md) for its internals: scheduler run queues are [priority queues](../05-algorithms-and-data-structures/02-fundamental-data-structures/heaps-and-priority-queues.md) or red-black trees, page caches are [hash tables](../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md), file systems use [search trees](../05-algorithms-and-data-structures/02-fundamental-data-structures/search-trees.md), and deadlock detection is cycle finding in a graph.

What the layers above need is **the process abstraction behind a system-call interface**: an isolated address space, one or more threads of control, and handles (file descriptors) to files, sockets and devices. [08 Networking](../08-networking/README.md) is implemented as a kernel protocol stack reached through sockets. [09 Data Management](../09-data-management/README.md) builds on files, `fsync` and the page cache. [10 Distributed and Parallel Computing](../10-distributed-and-parallel-computing/README.md) treats the OS process as the unit that crashes and the thread as the unit of parallelism. [11 Security and Cryptography](../11-security-and-cryptography/README.md) uses the kernel as the reference monitor that enforces access control and isolation.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [01 Kernel and abstractions](01-kernel-and-abstractions/README.md) | The protection boundary, system calls, and how the kernel is structured | 04 privilege modes |
| [02 Process management](02-process-management/README.md) | Virtualizing the CPU: processes, threads, scheduling; communication between processes | 01 |
| [03 Concurrency](03-concurrency/README.md) | Making shared-memory interleavings correct | 02 (threads) |
| [04 Memory management](04-memory-management/README.md) | Virtualizing memory: address spaces, paging, allocation | 01, 02 |
| [05 Storage and file systems](05-storage-and-file-systems/README.md) | Persistence: files, directories, crash consistency | 03, 04 (page cache), 06 |
| [06 Input/output (I/O) and devices](06-io-and-devices/README.md) | Drivers, interrupts and how programs wait for I/O | 01, 03 |
| [07 Virtualization](07-virtualization/README.md) | Applying the OS's own tricks to whole machines and OS instances | all of the above |

```
          applications, runtimes, databases, servers
  ---------------- system-call interface (the protection boundary) ----------------
   processes &      concurrency      memory        file systems      I/O models
   scheduling (02)  primitives (03)  manager (04)  (05)              (06)
        \              |               |               |               /
         +------------ kernel core: traps, interrupts, protection (01) +
  ---------------- hardware: CPU modes, MMU, timer, devices (04) ------------------
             virtualization (07) repeats the trick one level down
```

Read 01 first: everything else is a use of the protection boundary. Then 02 (the CPU), 03 (what goes wrong when the CPU is shared), and 04 (memory). 05 and 06 are the persistence and device half. 07 closes the loop: a hypervisor virtualizes a whole machine using the same mechanisms the OS used to virtualize a CPU and memory, and a container virtualizes the OS's own namespaces.

## Connections to neighbouring layers

- **[04 Computer Architecture](../04-computer-architecture/README.md):** the hardware contract the OS programs against. Page tables, Translation Lookaside Buffers (TLBs), interrupts, Direct Memory Access (DMA) and [cache coherence](../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md) are defined there and managed here. Hardware virtualization extensions (Intel VT-x, AMD-V) exist because of OS needs.
- **[06 Programming Languages](../06-programming-languages/README.md):** compilers, loaders and runtimes are the OS's main clients; the language [memory model](../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md) and the OS's synchronization primitives must agree. Memory-unsafe kernel languages are the root of many kernel vulnerabilities.
- **[08 Networking](../08-networking/README.md):** the Transmission Control Protocol/Internet Protocol (TCP/IP) stack lives in the kernel; sockets are file descriptors; [I/O models](06-io-and-devices/io-models.md) like `epoll` exist mainly for network servers.
- **[09 Data Management](../09-data-management/README.md):** databases reimplement parts of the OS (buffer pools, their own scheduling, write-ahead logging) because general-purpose policies like the page cache's eviction do not know the query's access pattern.
- **[10 Distributed and Parallel Computing](../10-distributed-and-parallel-computing/README.md):** single-machine concurrency is the small case of distributed coordination; [cloud computing](../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) is built on hypervisors and containers.
- **[11 Security and Cryptography](../11-security-and-cryptography/README.md):** the kernel enforces [access control](../11-security-and-cryptography/03-system-security/access-control.md) and is the base of [isolation and sandboxing](../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md); [side channels](../11-security-and-cryptography/03-system-security/side-channels.md) like Meltdown broke the kernel/user boundary and forced kernel page-table isolation.

## Connections across layers

The OS is where hardware mechanisms become software policies. From below it takes privilege, translation and interrupts; to the layers above it gives processes, files and sockets. The idea of a trusted, small, mediating component reappears as the reference monitor in security, the hypervisor in the cloud, and the coordinator in distributed systems.

## Cross-cutting threads

- [Virtualization](../CROSS-CUTTING.md#virtualization): processes, virtual memory, files and hypervisors all make one resource look like many.
- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): the system-call interface hides devices, scheduling and placement.
- [Indirection and naming](../CROSS-CUTTING.md#indirection-and-naming): page tables, file descriptors, inodes and path names.
- [Caching and locality](../CROSS-CUTTING.md#caching-and-locality): TLBs, the page cache and page replacement.
- [State and time](../CROSS-CUTTING.md#state-and-time): races, locks and memory ordering.
- [Redundancy and fault tolerance](../CROSS-CUTTING.md#redundancy-and-fault-tolerance): journaling and copy-on-write file systems.
- [Trust and verification](../CROSS-CUTTING.md#trust-and-verification): the kernel as trusted computing base; seL4's machine-checked proof.
- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): monolithic versus microkernel, throughput versus latency in scheduling.
