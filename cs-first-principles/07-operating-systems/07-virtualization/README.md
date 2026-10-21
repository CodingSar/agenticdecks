# Virtualization

> **Layer:** [07 Operating Systems](../README.md) › Virtualization
> **Children:** [Virtual machines and hypervisors](virtual-machines-and-hypervisors.md) · [Containers](containers.md)

## What this area is about

The Operating System (OS) virtualizes the Central Processing Unit (CPU) and memory for processes. This area applies the same trick one level further, to isolate whole software environments from each other on shared hardware. Two designs dominate. A **virtual machine** (VM) virtualizes the *hardware interface*: a hypervisor gives each guest the illusion of a complete computer, so each can run its own kernel (Linux next to Windows). A **container** virtualizes the *OS interface*: one kernel gives each group of processes its own view of process IDs, file systems, network interfaces and resource limits, so each looks like a separate machine while sharing the kernel.

The unifying idea is the one that runs through this whole layer: **interpose on every access to a resource, and you can multiplex it, isolate it and move it.** VMs interpose at the hardware boundary (privileged instructions, page tables, devices); containers interpose at the system-call boundary (namespaces and control groups inside the kernel).

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Virtual machines and hypervisors](virtual-machines-and-hypervisors.md) | Running multiple OS kernels on one machine: trap-and-emulate, hardware assists, nested paging, paravirtual I/O | [Kernel mode and system calls](../01-kernel-and-abstractions/kernel-mode-and-system-calls.md), [address spaces and paging](../04-memory-management/address-spaces-and-paging.md) |
| [Containers](containers.md) | Isolating process groups under one kernel: namespaces, cgroups, layered images | [Processes](../02-process-management/processes.md), [file system abstractions](../05-storage-and-file-systems/file-system-abstractions.md) |

```
   VMs                                     containers
 +--------+ +--------+                  +------+ +------+ +------+
 | app    | | app    |                  | app  | | app  | | app  |
 | guest  | | guest  |                  | libs | | libs | | libs |
 | kernel | | kernel |                  +------+ +------+ +------+
 +--------+ +--------+                  |  one host kernel        |
 |     hypervisor     |                 |  (namespaces + cgroups) |
 +--------------------+                 +-------------------------+
 |      hardware      |                 |        hardware         |
```

Read VMs first: they show the classical theory (Popek and Goldberg) and the hardware support that made it practical. Containers then show the lighter alternative: less isolation (a shared kernel is a shared attack surface) in exchange for near-zero overhead and fast start-up. Real clouds combine them: containers inside VMs, or lightweight VMs like Firecracker that run one container each.

## Connections to sibling areas

- **[Kernel and abstractions](../01-kernel-and-abstractions/README.md):** a hypervisor is a kernel for kernels; small hypervisors resemble microkernels.
- **[Process management](../02-process-management/README.md):** virtual CPUs are scheduled like threads; containers are process groups.
- **[Concurrency](../03-concurrency/README.md):** a descheduled virtual CPU holding a guest spinlock stalls other virtual CPUs, which paravirtual spinlocks address.
- **[Memory management](../04-memory-management/README.md):** nested page tables add a second level of translation; memory ballooning and page sharing manage overcommit between guests.
- **[Storage and file systems](../05-storage-and-file-systems/README.md):** virtual disks are files; container images are stacks of read-only layers merged by overlay file systems.
- **[I/O and devices](../06-io-and-devices/README.md):** device emulation is the slowest part of virtualization; virtio and IOMMU passthrough fix it.

## Connections across layers

Hardware support comes from [04 Computer Architecture](../../04-computer-architecture/README.md) ([the ISA contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md), [virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md)). Language VMs in [06](../../06-programming-languages/04-runtime-systems/interpreters-and-virtual-machines.md) are a different kind of virtual machine (a virtual instruction set rather than a virtual copy of real hardware). Upward, virtualization is the foundation of [cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) and of [isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md), and containers underpin [build and continuous delivery](../../12-software-engineering/04-operations/build-and-continuous-delivery.md).

## Cross-cutting threads

- [Virtualization](../../CROSS-CUTTING.md#virtualization): the defining principle, applied to the whole machine or to the OS interface.
- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): nested page tables and per-container namespaces.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): the size of the shared trusted base decides isolation strength.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): VM isolation versus container density and start-up time.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): each layer can be virtualized by interposing on the interface beneath it.
