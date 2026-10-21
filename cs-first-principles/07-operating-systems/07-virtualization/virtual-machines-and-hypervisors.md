# Virtual Machines and Hypervisors

> **Layer:** [07 Operating Systems](../README.md) › [Virtualization](README.md)
> **Builds on:** [Kernel mode and system calls](../01-kernel-and-abstractions/kernel-mode-and-system-calls.md), [Address spaces and paging](../04-memory-management/address-spaces-and-paging.md), [The ISA contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md), [Device drivers and interrupt handling](../06-io-and-devices/device-drivers-and-interrupt-handling.md)
> **Enables:** [Cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md), [Isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md), [Containers](containers.md)

## Essence

A **hypervisor** (virtual machine monitor, VMM) runs several **virtual machines** (VMs), each a faithful copy of the real hardware on which an unmodified Operating System (OS) can run. It works like an OS one level down: guest code runs directly on the Central Processing Unit (CPU) at full speed, but every operation that would let a guest observe or control real hardware (changing page tables, disabling interrupts, touching devices) must trap to the hypervisor, which emulates its effect on the guest's *virtual* hardware. Popek and Goldberg (1974) stated when this trap-and-emulate approach works; x86 originally failed their test, which led to binary translation, then paravirtualization, and finally hardware support (Intel VT-x, AMD-V, 2005–2006) that today's hypervisors such as the Kernel-based Virtual Machine (KVM), Xen, Hyper-V and VMware ESXi rely on.

## Core tenets

1. **A VM must be equivalent, efficient and controlled.** Popek and Goldberg's requirements: a program behaves the same as on real hardware (equivalence), most instructions run natively (efficiency), and the hypervisor keeps full control of resources (resource control). Their theorem: an architecture can be virtualized by trap-and-emulate if every *sensitive* instruction (one that reads or changes privileged state) is also *privileged* (traps when run in user mode).

2. **Classic x86 violated the theorem, and three generations of fixes followed.** Some x86 instructions were sensitive but did not trap; `popf` silently ignored attempts to change the interrupt flag in user mode, so a deprivileged guest kernel would misbehave without the hypervisor knowing. VMware (1999) solved this with *binary translation*, rewriting guest kernel code on the fly. Xen (2003) used *paravirtualization*, modifying the guest kernel to call the hypervisor explicitly (hypercalls). Intel VT-x and AMD-V then added a new CPU mode (root and non-root) in which guest kernels run at their normal privilege and sensitive operations cause a *VM exit* to the hypervisor.

3. **Memory virtualization needs two levels of translation.** A guest OS maps guest-virtual to guest-physical addresses; the hypervisor must map guest-physical to host-physical memory. Before hardware help, hypervisors maintained *shadow page tables* combining both mappings, trapping every guest page-table write. Extended Page Tables (EPT, Intel) and Nested Page Tables (NPT, AMD) let the Memory Management Unit (MMU) walk both levels in hardware. The cost is a longer Translation Lookaside Buffer (TLB) miss: a two-dimensional walk can take up to 24 memory references with four-level tables, which is why huge pages matter even more in VMs.

4. **Input/output (I/O) is the expensive part, so it is paravirtualized or passed through.** Emulating a real network card means trapping every register access, many per packet. *Paravirtual* devices (virtio in KVM, Xen's split drivers) give the guest a driver designed for virtualization, which exchanges batches of requests through shared-memory rings with few exits. *Device passthrough* hands a physical device (or a Single Root I/O Virtualization (SR-IOV) slice of one) directly to a guest, with the Input-Output Memory Management Unit (IOMMU) confining its Direct Memory Access (DMA) to that guest's memory.

5. **Type 1 and type 2 differ in where the hypervisor sits, but the line has blurred.** A type 1 (bare-metal) hypervisor runs directly on hardware: Xen, VMware ESXi, Microsoft Hyper-V. A type 2 (hosted) hypervisor runs on a conventional OS: VirtualBox, VMware Workstation. KVM turns the Linux kernel itself into a hypervisor (each VM is a Linux process, each virtual CPU a thread), and pairs it with a user-space device model such as QEMU or Firecracker. Xen keeps its own small hypervisor and runs device drivers in a privileged Linux "domain 0".

6. **Hypervisors multiplex resources by applying OS techniques to whole OSs.** Virtual CPUs are scheduled on physical CPUs like threads. Memory can be overcommitted using *ballooning* (a guest driver allocates memory to hand back to the host) and page sharing. Because a VM's entire state is data, it can be snapshotted, cloned, and *live-migrated* to another host by copying memory pages iteratively while the guest runs, then pausing briefly to copy the remainder (Clark et al., 2005); downtime is typically well under a second.

7. **The hypervisor is a small trusted base, but not a perfect wall.** VMs share CPUs, caches and memory buses, so side channels leak between them; Spectre and the L1 Terminal Fault (L1TF) vulnerability forced hypervisors to flush caches and disable simultaneous multithreading in some deployments. Hypervisor bugs and emulated-device bugs (the 2015 VENOM bug in QEMU's floppy controller) can let a guest escape. Even so, a hardware-level interface is far narrower than a full system-call interface, which is why public clouds isolate tenants with VMs.

## Key concepts

| Term | Meaning |
|---|---|
| Hypervisor (VMM) | Software that creates and runs virtual machines and controls real hardware |
| Guest / host | The OS running inside a VM / the system running the hypervisor |
| Trap-and-emulate | Run guest code natively; trap sensitive operations and emulate them |
| Sensitive instruction | An instruction that reads or alters privileged machine state |
| VM exit | Hardware-assisted transfer of control from guest to hypervisor |
| Paravirtualization | Modifying the guest to cooperate with the hypervisor via hypercalls or virtual devices |
| Nested paging (EPT/NPT) | Hardware two-level translation, guest-virtual to host-physical |
| virtio | Standard paravirtual device interface using shared-memory queues |
| Live migration | Moving a running VM between hosts with brief downtime |

## How it fits

- **Below:** depends on CPU privilege levels and virtualization extensions defined in [the Instruction Set Architecture (ISA) contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md), on [virtual memory hardware](../../04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md), and on the [trap mechanism](../01-kernel-and-abstractions/kernel-mode-and-system-calls.md).
- **Above:** Infrastructure-as-a-Service clouds sell VMs ([cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md)); security uses them for strong isolation ([isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md)) and must defend against cross-VM [side channels](../../11-security-and-cryptography/03-system-security/side-channels.md).
- **Siblings:** [containers](containers.md) virtualize the OS interface instead of the hardware, trading isolation for density; microVMs (Firecracker, gVisor's approach of a user-space kernel) combine the two.

## Common misconceptions

- **"VMs are slow because everything is emulated."** With hardware assists, CPU-bound code runs within a few percent of native; overhead concentrates in VM exits, TLB misses and I/O.
- **"A Java Virtual Machine is the same kind of thing."** A language VM implements an abstract instruction set for programs; a system VM replicates real hardware for whole OSs.
- **"VM isolation is absolute."** Shared microarchitectural state and hypervisor bugs have both allowed cross-VM leaks and escapes.

## Go deeper

- Gerald J. Popek and Robert P. Goldberg, "Formal Requirements for Virtualizable Third Generation Architectures" (1974).
- Paul Barham et al., "Xen and the Art of Virtualization" (SOSP 2003).
- Keith Adams and Ole Agesen, "A Comparison of Software and Hardware Techniques for x86 Virtualization" (ASPLOS 2006).
- Christopher Clark et al., "Live Migration of Virtual Machines" (NSDI 2005).
