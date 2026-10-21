# Isolation and Sandboxing

> **Layer:** [11 Security and Cryptography](../README.md) › [System security](README.md)
> **Builds on:** [Virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md), [Address spaces and paging](../../07-operating-systems/04-memory-management/address-spaces-and-paging.md), [Virtual machines and hypervisors](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md), [Containers](../../07-operating-systems/07-virtualization/containers.md)
> **Enables:** [Web security](../04-network-and-application-security/web-security.md), [Cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md), [Side channels](side-channels.md)

## Essence

Isolation confines a piece of code so that, even if it is buggy or malicious, it cannot read or modify anything outside an assigned set of resources. Sandboxing is isolation applied deliberately to code you do not trust: a browser tab, a document parser, a plug-in, a tenant's workload. Every isolation mechanism has the same structure: a **boundary** enforced by something more privileged (hardware page tables, the kernel, a hypervisor, a language runtime), a **narrow interface** through which the confined code requests services, and a **trusted computing base** whose bugs would break the boundary. Mechanisms differ in where the boundary is drawn, how large the trusted base is, and what crossing it costs.

## Core tenets

1. **Hardware privilege and virtual memory are the root of all isolation.** The processor runs the kernel in a privileged mode and applications in user mode; only privileged code can change page tables or talk to devices. Each process gets its own virtual address space, so it simply has no address for another process's memory. Every higher-level mechanism builds on these two hardware features, and a flaw in them (such as the Meltdown attack, which let user code read kernel memory through speculation) breaks everything above.

2. **The interface is the attack surface.** A process is confined only as well as the system-call interface is implemented, and Linux exposes several hundred system calls. Sandboxes shrink this: seccomp filters restrict which calls a process may make, and capability-oriented designs (OpenBSD's pledge and unveil, FreeBSD's Capsicum) let a program renounce rights it no longer needs. The smaller and simpler the interface, the less there is to get wrong.

3. **Privilege separation splits a program along trust lines.** Modern browsers run each site's renderer in a sandboxed process with almost no direct access to files or the network; the renderer must ask a privileged broker process, which validates every request. Site isolation (one process per site) also limits what a speculative-execution attack in one tab can read. An attacker must chain a renderer exploit with a sandbox escape, which is why browser compromises are expensive.

4. **Virtual machines isolate at the hardware interface; containers at the system-call interface.** A hypervisor presents virtual hardware, so each guest runs its own kernel and the boundary is the comparatively narrow virtual-device interface. Containers share one host kernel and are isolated by namespaces (separate views of processes, files, network) and control groups (resource limits), so the boundary is the much wider system-call interface. Containers are lighter and start faster; virtual machines give a stronger boundary. Lightweight virtual machines (such as Firecracker) and user-space kernels (such as gVisor) combine fast start-up with a smaller shared surface for multi-tenant clouds.

5. **Language-based isolation avoids hardware crossings.** A type-safe or verified runtime can confine code inside one address space: WebAssembly checks that modules only access their own linear memory and call only declared imports, and the Java Virtual Machine once sandboxed applets this way. Crossing such a boundary costs a function call rather than a context switch, but the trusted base now includes the compiler, verifier and runtime, and history shows those have bugs.

6. **Trusted execution environments invert the threat model.** Enclaves such as Intel Software Guard Extensions (SGX), and confidential virtual machines such as AMD SEV-SNP and Intel TDX, protect code and data *from* the operating system and hypervisor, using memory encryption and hardware attestation that proves to a remote party which code is running. They shrink the trusted base to the processor package and the enclave's code, but side-channel attacks have repeatedly extracted enclave secrets, so they are a hardening layer, not a guarantee.

7. **Isolation must cover resources, not just memory.** A sandboxed process that can consume all memory, processor time or disk bandwidth can deny service to its neighbours, and shared resources are also covert and side channels. Resource limits (control groups, hypervisor scheduling) and partitioning of shared hardware (cache allocation, dedicated cores) extend isolation to availability and to information flow.

## Key concepts

| Term | Meaning |
|---|---|
| Isolation boundary | Line across which one component cannot affect another except through a defined interface |
| Sandbox | Restricted environment for running untrusted code |
| Privilege separation | Splitting a program into privileged and unprivileged parts |
| seccomp | Linux mechanism to filter allowed system calls |
| Namespace / control group | Linux mechanisms giving containers separate views / resource limits |
| Hypervisor | Software that runs virtual machines and isolates them |
| Software fault isolation | Confining code in one address space by instrumentation or verification |
| Enclave / TEE | Hardware-protected region isolated even from the OS (trusted execution environment) |
| Attestation | Hardware-signed proof of what code is running |
| Sandbox escape | Exploit that breaks out of a confinement boundary |

## How it fits

- **Below:** built on [virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md), [kernel mode](../../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md), [address spaces](../../07-operating-systems/04-memory-management/address-spaces-and-paging.md), [virtual machines](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md), [containers](../../07-operating-systems/07-virtualization/containers.md) and [language virtual machines](../../06-programming-languages/04-runtime-systems/interpreters-and-virtual-machines.md); a small trusted base is the [microkernel argument](../../07-operating-systems/01-kernel-and-abstractions/kernel-architectures.md).
- **Above:** [multi-tenant cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md), browser architecture for [web security](../04-network-and-application-security/web-security.md), and safe execution of untrusted tools by [AI agents](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md) all depend on it.
- **Siblings:** [access control](access-control.md) is the policy that isolation enforces; [memory-safety bugs](memory-safety-vulnerabilities.md) are why sandboxes are needed; [side channels](side-channels.md) leak across even correct boundaries.

## Common misconceptions

- **"Containers are as isolated as virtual machines."** They share the host kernel, so a kernel bug can break every container on the host.
- **"A sandbox makes untrusted code safe."** It limits damage to what the interface allows; a sandbox with broad file or network access confines little.
- **"Enclaves remove the need to trust the hardware vendor."** They concentrate trust in the vendor's processor and attestation keys.

## Go deeper

- Saltzer and Schroeder, "The Protection of Information in Computer Systems", *Proceedings of the IEEE* (1975).
- Wahbe, Lucco, Anderson and Graham, "Efficient Software-Based Fault Isolation", SOSP (1993).
- Reis and Gribble, "Isolating Web Programs in Modern Browser Architectures", EuroSys (2009).
- Costan and Devadas, "Intel SGX Explained", IACR Cryptology ePrint Archive (2016).
