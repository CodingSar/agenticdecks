# Kernel and Abstractions

> **Layer:** [07 Operating Systems](../README.md) › Kernel and abstractions
> **Children:** [The role of the OS](the-role-of-the-os.md) · [Kernel mode and system calls](kernel-mode-and-system-calls.md) · [Kernel architectures](kernel-architectures.md)

## What this area is about

This area answers two questions: what is an Operating System (OS) *for*, and how does a piece of software get the authority to do it? The answer to the first is that the OS turns raw, shared, dangerous hardware into safe, private, convenient abstractions. The answer to the second is the **protection boundary**: the Central Processing Unit (CPU) runs the kernel in a privileged mode and everything else in an unprivileged one, and the only way across is through entry points the kernel controls.

The unifying idea is that abstraction plus enforcement equals an operating system. A library can offer abstractions; only a kernel, protected by hardware, can make every program use them.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [The role of the OS](the-role-of-the-os.md) | Why an OS exists: virtualization, concurrency, persistence; mechanism versus policy | Hardware (layer 04) |
| [Kernel mode and system calls](kernel-mode-and-system-calls.md) | The mechanism: privilege modes, traps, interrupts, the system-call path and its cost | The role of the OS |
| [Kernel architectures](kernel-architectures.md) | How much code to put on the privileged side: monolithic, microkernel, hybrid, exokernel/unikernel | Both of the above |

```
   user programs           user programs
        |  syscall / fault       ^  return-from-trap
  ======|========================|====== protection boundary
        v                        |
     trap handler --> kernel service --> (maybe) scheduler
```

Read in order. The first file sets the goals; the second shows the one hardware mechanism that achieves them; the third asks a design question that every real kernel answers differently: how big should the privileged part be? Linux and Windows NT put most services in kernel mode for speed; seL4 keeps about 8,700 lines of C there so that it can be formally verified.

## Connections to sibling areas

- **[Process management](../02-process-management/README.md):** a process is the kernel's container for a protected execution; the timer interrupt described here is what lets the scheduler preempt it.
- **[Concurrency](../03-concurrency/README.md):** the kernel is entered by many CPUs and interrupts at once, so it is itself a concurrent program that needs locks.
- **[Memory management](../04-memory-management/README.md):** the page tables the kernel installs are what make the protection boundary cover memory, not just instructions.
- **[Storage and file systems](../05-storage-and-file-systems/README.md):** files are the OS's persistence abstraction, reached through system calls like `open`, `read` and `fsync`.
- **[Input/output (I/O) and devices](../06-io-and-devices/README.md):** device drivers are the largest part of a monolithic kernel and the reason microkernels move drivers out.
- **[Virtualization](../07-virtualization/README.md):** a hypervisor adds one more privilege level beneath the kernel and plays the same game one level down.

## Connections across layers

From [04 Computer Architecture](../../04-computer-architecture/README.md) this area takes privilege levels ([the Instruction Set Architecture (ISA) contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md)) and [interrupts](../../04-computer-architecture/05-io-and-interconnect/buses-and-interrupts.md). It gives [11 Security](../../11-security-and-cryptography/README.md) its foundational reference monitor and the trusted computing base idea ([security design principles](../../11-security-and-cryptography/01-security-principles/security-design-principles.md)), and gives [12 Software Engineering](../../12-software-engineering/README.md) a classic case of [modularity](../../12-software-engineering/01-design/modularity-and-information-hiding.md) versus performance.

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): the system-call interface is the abstraction applications program against.
- [Interface vs implementation](../../CROSS-CUTTING.md#interface-vs-implementation): the Portable Operating System Interface (POSIX) is an interface; Linux, macOS and FreeBSD implement it differently.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): the kernel is the trusted computing base; smaller kernels are easier to verify.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): monolithic speed against microkernel isolation.
