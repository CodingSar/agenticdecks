# Kernel Architectures

> **Layer:** [07 Operating Systems](../README.md) › [Kernel and abstractions](README.md)
> **Builds on:** [Kernel mode and system calls](kernel-mode-and-system-calls.md), [Hoare logic and program proofs](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md), [Proof assistants and dependent types](../../06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md)
> **Enables:** [Inter-process communication](../02-process-management/inter-process-communication.md), [Device drivers and interrupt handling](../06-io-and-devices/device-drivers-and-interrupt-handling.md), [Virtual machines and hypervisors](../07-virtualization/virtual-machines-and-hypervisors.md), [Security design principles](../../11-security-and-cryptography/01-security-principles/security-design-principles.md)

## Essence

A kernel architecture answers one question: which Operating System (OS) services run in privileged kernel mode, and which run as ordinary protected processes? A **monolithic** kernel (Linux, the Berkeley Software Distribution (BSD) family) puts the scheduler, memory manager, file systems, network stack and drivers in one privileged address space, so they call each other directly and fast, but a bug anywhere can crash or compromise everything. A **microkernel** (L4, seL4, QNX) keeps only address spaces, threads, Inter-Process Communication (IPC) and minimal scheduling privileged, and runs everything else as user-mode servers, trading extra boundary crossings for isolation and verifiability. Hybrid, exokernel and unikernel designs sit at other points on the same tradeoff.

## Core tenets

1. **The size of the privileged part is the size of the Trusted Computing Base (TCB).** Every line in kernel mode can read any memory and execute any instruction, so a single bug can defeat all isolation. Linux has tens of millions of lines (mostly drivers), all trusted; seL4 has about 8,700 lines of C (Klein et al., 2009). Minimizing the TCB is the microkernel's central argument, and it follows Saltzer and Schroeder's principle of least privilege.

2. **Monolithic kernels win on performance and simplicity of interaction.** When the file system needs a page from the memory manager, it calls a function and shares data structures. No messages, no copies, no context switches. This is why Linux dominates servers and phones, and why its modularity is provided by loadable kernel modules (which still run fully privileged) rather than by protection boundaries.

3. **Microkernels turn function calls into messages, and the cost of IPC decides their fate.** First-generation microkernels like Mach (1985) were slow, and many concluded the idea was flawed. Jochen Liedtke's L4 (1993) showed IPC could be made more than an order of magnitude faster (about 20 times faster than Mach's) by designing the kernel around it: small, register-passed messages, direct thread switching, minimal cache footprint. The lesson is that microkernel overhead is mostly an implementation choice, not a law.

4. **Isolation of services enables recovery and verification.** A crashed driver in a microkernel is a crashed process: the system can restart it, as MINIX 3 does. And a small kernel can be proved correct. seL4's functional-correctness proof (Klein et al., 2009) shows, in a machine-checked proof, that its C implementation matches its abstract specification, which rules out whole classes of bugs such as buffer overflows and null dereferences in the kernel itself.

5. **Most production kernels are hybrids driven by pragmatism.** Windows NT was designed with microkernel ideas (a small kernel plus subsystems), but moved graphics into kernel mode in NT 4.0 for speed. Apple's XNU combines a Mach core with a BSD layer in the same address space. These systems keep microkernel-style internal interfaces but run them without protection boundaries between components.

6. **Exokernels and unikernels shrink the abstraction, not just the privilege.** An exokernel (Massachusetts Institute of Technology (MIT), 1995) securely multiplexes raw resources and lets library OSs in each application implement their own abstractions, on the argument that a fixed abstraction is wrong for some application. A unikernel (MirageOS) compiles one application with just the library OS it needs into a single-address-space image run on a hypervisor; the hypervisor supplies the isolation.

7. **Moving code out of the kernel is a broader trend.** Even monolithic kernels now push work across the boundary in both directions: Filesystem in Userspace (FUSE) and user-space drivers (the Data Plane Development Kit (DPDK) for networking, the Storage Performance Development Kit (SPDK) for storage) move code out for flexibility or speed, while extended Berkeley Packet Filter (eBPF) moves verified, sandboxed user-supplied code *in* by statically checking it before it runs.

## Key concepts

| Term | Meaning |
|---|---|
| Monolithic kernel | All core services and drivers in one privileged address space |
| Microkernel | Minimal privileged core (address spaces, threads, IPC); services run as user processes |
| Hybrid kernel | Microkernel-style structure with many services kept in kernel mode for speed |
| IPC | Inter-Process Communication; in a microkernel, the path every service request takes |
| Loadable module | Code added to a running monolithic kernel; modular, but fully privileged |
| Exokernel | Kernel that exports raw resources securely and leaves abstractions to libraries |
| Unikernel | Single-application, single-address-space image built with a library OS |
| Formal verification | Machine-checked proof that code meets a specification |

## How it fits

- **Below:** every architecture uses the same [trap mechanism](kernel-mode-and-system-calls.md); they differ in how often it fires. Verification relies on [Hoare-style reasoning](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md) and [proof assistants](../../06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md) (seL4 was verified in Isabelle/HOL).
- **Above:** the kernel boundary is a classic case of [modularity](../../12-software-engineering/01-design/modularity-and-information-hiding.md) traded against speed; the TCB idea is foundational for [security design principles](../../11-security-and-cryptography/01-security-principles/security-design-principles.md); hypervisors such as Xen are structured much like microkernels ([virtual machines and hypervisors](../07-virtualization/virtual-machines-and-hypervisors.md)).
- **Siblings:** [The role of the OS](the-role-of-the-os.md) states the goals; [kernel mode and system calls](kernel-mode-and-system-calls.md) prices the crossing that every architecture must pay; [inter-process communication](../02-process-management/inter-process-communication.md) prices the message that replaces a function call.

## Common misconceptions

- **"Microkernels are inherently slow."** Mach was slow; L4-family kernels made IPC cheap enough that seL4 and QNX run in performance-sensitive embedded and automotive systems.
- **"Loadable modules make Linux a microkernel."** Modules are a packaging mechanism. They share the kernel's address space and privilege, so a buggy module can corrupt anything.
- **"A verified kernel makes the system secure."** seL4's proof covers the kernel against its specification under stated assumptions (correct hardware, compiler and boot code); user-level servers and hardware side channels are outside it.

## Go deeper

- Jochen Liedtke, "On µ-Kernel Construction" (SOSP 1995): why IPC cost was an implementation problem.
- Gerwin Klein et al., "seL4: Formal Verification of an OS Kernel" (SOSP 2009): the first full functional-correctness proof of a general-purpose kernel.
- Dawson R. Engler, M. Frans Kaashoek and James O'Toole, "Exokernel: An Operating System Architecture for Application-Level Resource Management" (SOSP 1995).
- Andrew S. Tanenbaum and Herbert Bos, *Modern Operating Systems* (4th ed., 2014): broad comparison of kernel structures.
