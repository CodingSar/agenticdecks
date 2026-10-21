# The Role of the OS

> **Layer:** [07 Operating Systems](../README.md) › [Kernel and abstractions](README.md)
> **Builds on:** [The ISA contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md), [Virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md), [Buses and interrupts](../../04-computer-architecture/05-io-and-interconnect/buses-and-interrupts.md)
> **Enables:** [Kernel mode and system calls](kernel-mode-and-system-calls.md), [Processes](../02-process-management/processes.md), [File system abstractions](../05-storage-and-file-systems/file-system-abstractions.md), [Access control](../../11-security-and-cryptography/03-system-security/access-control.md)

## Essence

An Operating System (OS) is the software that sits between hardware and programs and does three jobs: it **virtualizes** the hardware (one Central Processing Unit (CPU) becomes many processes, one physical memory becomes many private address spaces), it **mediates concurrency** among everything that shares the machine, and it provides **persistence** (named files that survive power loss). It is at once an *illusionist*, giving each program a simpler machine than the real one, and a *referee*, allocating scarce resources and stopping programs from harming each other. The single idea that makes the referee role possible is hardware-enforced privilege: the kernel can do things that applications cannot, so its rules cannot be bypassed.

## Core tenets

1. **The OS exists because hardware is shared by programs that do not trust each other.** On a single-program machine with no adversaries, a library of device routines would be enough (early batch monitors and MS-DOS were close to this). Once several programs run together, someone must decide who gets the CPU next, stop one from overwriting another's memory, and arbitrate access to the disk. That someone must be more privileged than the programs it governs.

2. **Virtualization gives each program the illusion of a private machine.** Time-sharing the CPU (switching between processes every few milliseconds) and space-sharing memory (mapping each process's addresses to different physical frames) let a program be written as if it owned the computer. This is why the same binary runs unchanged whether one or a thousand other processes are present. The illusion is cheap because hardware helps: a timer interrupt forces switches, and a Memory Management Unit (MMU) translates every address.

3. **Abstractions are chosen to hide device detail and enable sharing.** A file hides sectors, flash erase blocks and controller commands behind "a named, growable array of bytes". A socket hides network cards and retransmission behind "a byte stream to a remote endpoint". Good OS abstractions are few and general: Unix's "everything is a file descriptor" lets the same `read`/`write` code work on files, terminals and the [pipes and sockets](../02-process-management/inter-process-communication.md) that connect processes.

4. **Separate mechanism from policy.** The *mechanism* is how something is done (context switch, page-table update); the *policy* is what is decided (which process runs, which page is evicted). Keeping them apart lets the policy change without rewriting the mechanism: Linux replaced its O(1) scheduler with the Completely Fair Scheduler (CFS) in 2007 and with Earliest Eligible Virtual Deadline First (EEVDF) scheduling in 2023 without changing how context switches work. This principle, articulated in Hydra (Wulf et al., 1974), shapes every subsystem.

5. **Protection requires mediation of every access.** The kernel can only enforce a rule if every sensitive operation passes through it. Hardware gives this: privileged instructions trap in user mode, every memory access is translated through kernel-controlled page tables, and devices are reachable only through kernel-mapped registers. If even one path escapes mediation (an unchecked Direct Memory Access (DMA) engine, a speculative-execution leak), isolation fails.

6. **The OS is a resource manager with conflicting goals.** It trades throughput (total work done) against latency (response time for any one task), fairness against priority, and efficiency against isolation. No policy is best for all workloads: a batch-compute server and a phone's user interface want different schedulers. This is why real OSs expose tunables (Linux `nice`, cgroups) and why databases sometimes bypass OS policies entirely.

7. **The OS must be robust to its own clients.** Any argument a program passes to the kernel may be malicious: a pointer into kernel memory, a length that overflows. The kernel copies and validates user data at the boundary (`copy_from_user` in Linux) and must stay correct under any sequence of calls. Kernel bugs are the most severe class because the kernel is in every program's trusted computing base.

## Key concepts

| Term | Meaning |
|---|---|
| Kernel | The part of the OS that runs in privileged mode and is always resident |
| Virtualization | Presenting a physical resource as one or more logical copies with a simpler interface |
| Abstraction | A simplified interface (process, file, socket) that hides hardware detail |
| Mechanism vs policy | How something is done versus the decision about what to do |
| Protection | Preventing one principal from accessing another's resources without permission |
| Trusted Computing Base (TCB) | All the code whose correctness the system's security depends on |
| System call | The controlled entry point a program uses to request a kernel service |
| Time-sharing | Multiplexing a CPU among processes by rapid switching |

## How it fits

- **Below:** relies on [privilege modes](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md), [address translation](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md) and [interrupts](../../04-computer-architecture/05-io-and-interconnect/buses-and-interrupts.md). It assumes the hardware enforces these faithfully.
- **Above:** language runtimes ([interpreters and virtual machines](../../06-programming-languages/04-runtime-systems/interpreters-and-virtual-machines.md)), networking ([sockets and Transmission Control Protocol (TCP)](../../08-networking/04-transport-layer/udp-and-tcp.md)), databases and distributed systems all program against OS abstractions. Security's [access control](../../11-security-and-cryptography/03-system-security/access-control.md) is enforced by the kernel.
- **Siblings:** [Kernel mode and system calls](kernel-mode-and-system-calls.md) is the mechanism behind these goals; [kernel architectures](kernel-architectures.md) decides how much code is trusted to pursue them.

## Common misconceptions

- **"The OS is the user interface."** The shell, desktop and window manager are applications. The OS proper is the kernel plus the services that enforce sharing; it would still be needed on a headless server.
- **"The OS runs alongside programs all the time."** The kernel runs only when entered: by a system call, an exception or an interrupt. Most of the time the CPU is running user code directly at full speed.
- **"Virtualization is just about virtual machines."** Processes and virtual memory are virtualization too; hypervisors apply the same idea to the whole machine.

## Go deeper

- Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (2018): the virtualization/concurrency/persistence framing used here.
- Dennis M. Ritchie and Ken Thompson, "The UNIX Time-Sharing System" (1974): a short paper showing how few abstractions a powerful OS needs.
- Butler W. Lampson, "Hints for Computer System Design" (1983): design principles drawn largely from OS experience.
