# Containers

> **Layer:** [07 Operating Systems](../README.md) › [Virtualization](README.md)
> **Builds on:** [Processes](../02-process-management/processes.md), [File system abstractions](../05-storage-and-file-systems/file-system-abstractions.md), [Scheduling](../02-process-management/scheduling.md), [Virtual machines and hypervisors](virtual-machines-and-hypervisors.md)
> **Enables:** [Cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md), [Build and continuous delivery](../../12-software-engineering/04-operations/build-and-continuous-delivery.md), [Isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md)

## Essence

A container is a group of ordinary processes that the kernel shows a private view of the system: their own process IDs, mount tree, network interfaces, hostname and users, with limits on how much Central Processing Unit (CPU), memory and I/O they may consume. It virtualizes the **Operating System (OS) interface** rather than the hardware: there is one shared kernel, and isolation is enforced inside it. On Linux the building blocks are **namespaces** (what a process can see), **control groups** (cgroups: how much it can use) and security filters (seccomp, capabilities, Linux Security Modules (LSMs)), combined with a **layered image** of the application's files. Docker (2013) packaged these existing kernel features into a convenient tool and image format; the Open Container Initiative (OCI) now standardizes it.

## Core tenets

1. **A container is not a kernel object; it is a configuration of ordinary processes.** Linux has no "container" type. A runtime such as runc creates a process with `clone` flags that give it new namespaces, places it in a cgroup, changes its root file system, drops privileges, and executes the application. From the host, `ps` shows the containerized processes as normal processes. This is why containers start in milliseconds: there is no kernel to boot.

2. **Namespaces virtualize names, so processes see only their own resources.** Each namespace type wraps one global kernel table: *PID* (process identifiers; the first process in the container is PID 1), *mount* (the file-system tree), *network* (interfaces, routing tables, ports), *UTS* (UNIX Time-Sharing: hostname), *IPC* (Inter-Process Communication: System V shared memory and message queues), *user* (user and group IDs, so root inside can map to an unprivileged user outside), *cgroup* and *time*. The idea descends from Plan 9's per-process namespaces, FreeBSD jails (2000) and Solaris Zones (2004).

3. **Control groups limit and account for resources, the other half of isolation.** Hiding resources is not enough; a container must not starve its neighbours. cgroups (contributed by Google engineers, merged in Linux 2.6.24 in 2008; unified v2 hierarchy since 4.5) arrange processes in a tree and attach controllers: CPU weight and quota (enforced by the scheduler), memory limits (enforced by reclaim and the Out-Of-Memory (OOM) killer within the group), block I/O bandwidth and process counts. Kubernetes' CPU and memory "requests" and "limits" become cgroup settings.

4. **Images are layered, content-addressed file trees.** A container image is a stack of read-only layers (base OS libraries, runtime, application), each identified by a cryptographic hash of its contents. An overlay file system (OverlayFS) merges them into one view with a thin writable layer on top, using copy-on-write for modified files. Layers shared between images are stored and downloaded once. Because the image bundles every user-space dependency, "works on my machine" becomes "works on any machine with a compatible kernel".

5. **The shared kernel is both the advantage and the weakness.** Containers avoid a guest kernel, so they use less memory, start faster and pack more densely than virtual machines (VMs), with near-native performance. But every container makes system calls into the same kernel, so a kernel vulnerability can let one container compromise the host and all others (container escape). The attack surface is the full system-call interface, hundreds of calls, versus a VM's narrow virtual-hardware interface.

6. **Defence in depth narrows the shared interface.** Container runtimes drop most root *capabilities* (fine-grained pieces of root's power such as `CAP_SYS_ADMIN`), apply a seccomp filter that blocks rarely needed system calls, use user namespaces so container root is not host root, and add mandatory access control (AppArmor, SELinux). For untrusted multi-tenant code, providers go further: gVisor intercepts system calls with a user-space kernel, and Firecracker or Kata Containers wrap each container in a lightweight VM.

7. **Containers changed deployment more than they changed isolation.** The technical pieces existed for years; what Docker added was a portable image format, a registry, and a simple build recipe (Dockerfile). Immutable images make deployment reproducible and rollback trivial, and orchestration systems (Kubernetes, descended from Google's Borg) schedule containers across clusters. Containers thus link OS mechanisms to software-delivery practice and cloud scheduling.

## Key concepts

| Term | Meaning |
|---|---|
| Container | Processes isolated by namespaces and limited by cgroups, sharing the host kernel |
| Namespace | Per-group view of one kernel resource table (PIDs, mounts, network, users...) |
| cgroup | Control group: a hierarchy that limits and accounts resources for its processes |
| Container image | Layered, content-addressed file-system snapshot plus run configuration |
| OverlayFS | Union file system that merges read-only layers with a writable upper layer |
| Capability (Linux) | One divisible portion of root privilege |
| seccomp | Kernel filter restricting which system calls a process may make |
| Container runtime | Program (runc, crun) that sets up namespaces and cgroups and starts the process |
| Orchestrator | Cluster system (Kubernetes) that schedules and manages containers across machines |

## How it fits

- **Below:** built from [processes](../02-process-management/processes.md), mount namespaces over [file system abstractions](../05-storage-and-file-systems/file-system-abstractions.md), and the cgroup-aware [scheduler](../02-process-management/scheduling.md) and [memory manager](../04-memory-management/page-replacement.md).
- **Above:** the unit of deployment in [cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) and [build and continuous delivery](../../12-software-engineering/04-operations/build-and-continuous-delivery.md); a building block of [isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md) governed by [access control](../../11-security-and-cryptography/03-system-security/access-control.md).
- **Siblings:** [virtual machines](virtual-machines-and-hypervisors.md) give stronger isolation with a separate kernel per tenant; the two are often stacked (containers in VMs) or merged (microVMs).

## Common misconceptions

- **"Containers are lightweight VMs."** They share the host kernel; there is no virtual hardware and no guest OS, which is the source of both their speed and their weaker isolation.
- **"Root in a container is harmless."** Without user namespaces, container root is host root restricted only by capabilities and filters; a kernel bug or misconfiguration (a mounted Docker socket, `--privileged`) yields host control.
- **"Containers make software portable across OSs."** A Linux container needs a Linux kernel; on macOS and Windows, Docker runs a Linux VM underneath.

## Go deeper

- Paul Menage, "Adding Generic Process Containers to the Linux Kernel" (Ottawa Linux Symposium 2007): the origin of cgroups.
- Poul-Henning Kamp and Robert N. M. Watson, "Jails: Confining the Omnipotent Root" (SANE 2000).
- Abhishek Verma et al., "Large-scale Cluster Management at Google with Borg" (EuroSys 2015).
- Brendan Burns, Brian Grant, David Oppenheimer, Eric Brewer and John Wilkes, "Borg, Omega, and Kubernetes" (ACM Queue, 2016).
