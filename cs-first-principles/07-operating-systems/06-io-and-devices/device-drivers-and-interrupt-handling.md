# Device Drivers and Interrupt Handling

> **Layer:** [07 Operating Systems](../README.md) › [I/O and devices](README.md)
> **Builds on:** [Buses and interrupts](../../04-computer-architecture/05-io-and-interconnect/buses-and-interrupts.md), [DMA and devices](../../04-computer-architecture/05-io-and-interconnect/dma-and-devices.md), [Kernel architectures](../01-kernel-and-abstractions/kernel-architectures.md)
> **Enables:** [I/O models](io-models.md), [File system implementation](../05-storage-and-file-systems/file-system-implementation.md), [Media access and Ethernet](../../08-networking/02-link-layer/media-access-and-ethernet.md), [Virtual machines and hypervisors](../07-virtualization/virtual-machines-and-hypervisors.md)

## Essence

A **device driver** is kernel code that knows how to operate one kind of device: which registers to write to start an operation, how to set up Direct Memory Access (DMA) so the device moves data to or from memory itself, and how to interpret the device's status. The driver plugs into a generic interface (block device, network interface, character device), so the rest of the Operating System (OS) never sees device specifics. Devices report completion with **interrupts**, which preempt whatever the Central Processing Unit (CPU) is doing; the kernel handles them in two halves, a tiny urgent part that runs immediately and a deferred part that does the real work later. Under very high event rates, **polling** beats interrupts, and modern systems switch between the two.

## Core tenets

1. **Drivers translate a generic interface into device-specific register operations.** The kernel defines a few device classes with fixed operations: a block device accepts read/write requests for numbered blocks, a network device transmits and receives packets, a character device offers a byte stream. Each driver implements one class for its hardware. This is what lets ext4 run unchanged on a Serial AT Attachment (SATA) disk, an Non-Volatile Memory Express (NVMe) Solid-State Drive (SSD) or a virtual disk.

2. **The CPU talks to devices through registers, and devices talk to memory through DMA.** Device registers appear either in a separate input/output (I/O) port space (x86 `in`/`out`) or, far more commonly today, as memory-mapped I/O addresses that the driver reads and writes like memory, but uncached. For bulk data the driver writes descriptors (address, length) into a ring buffer in memory and rings a "doorbell" register; the device then transfers the data by DMA without CPU involvement. High-speed devices such as NVMe drives and modern network cards keep many submission and completion queues, often one per core.

   ```
   driver: fill descriptor ring -> write doorbell register
   device: DMA data from/to memory -> write completion entry -> raise interrupt
   ```

3. **Interrupts let the CPU do other work while devices are busy.** Instead of repeatedly checking a status register (programmed I/O with busy-waiting), the CPU runs other threads; the device raises an interrupt when done. The interrupt controller (the Advanced Programmable Interrupt Controller (APIC) on x86, the Generic Interrupt Controller (GIC) on ARM) delivers it to a core, which saves state and jumps to the registered handler. Message-Signalled Interrupts (MSI-X) on Peripheral Component Interconnect Express (PCIe) let one device raise many distinct interrupts aimed at different cores.

4. **Interrupt handlers are split into an urgent top half and a deferred bottom half.** While a handler runs, it has interrupted arbitrary code, may have further interrupts masked, and cannot sleep. So the top half does the minimum: acknowledge the device, grab the completion status, schedule further work. The bottom half (Linux softirqs, tasklets, workqueues, threaded interrupts; Windows Deferred Procedure Calls (DPCs)) runs soon after with interrupts enabled and does protocol processing, buffer management and waking the waiting thread.

5. **At high rates, interrupts cost more than they save, so systems poll.** Each interrupt costs on the order of a microsecond in overhead and cache disruption. A 100 Gb/s network card can deliver millions of packets per second; one interrupt each would leave no CPU for anything else (receive livelock). Linux's New API (NAPI) switches a busy network device to polling: after one interrupt, the kernel disables further interrupts and processes packets in batches until the queue empties. Interrupt coalescing in the device does similar batching. Kernel-bypass frameworks (the Data Plane Development Kit (DPDK), the Storage Performance Development Kit (SPDK)) poll from user space with dedicated cores, trading CPU for microsecond latency.

6. **Drivers are the least reliable part of the kernel.** They are numerous, written by many vendors, and tested on less hardware than core code. Studies of Linux found drivers had error rates several times higher than the rest of the kernel (Chou et al., 2001), and Microsoft found third-party drivers caused most Windows crashes. Responses include static verification of driver Application Programming Interface (API) usage (Microsoft's Static Driver Verifier), running drivers in user space (Windows' User-Mode Driver Framework, MINIX 3, microkernels), and isolating devices with an Input-Output Memory Management Unit (IOMMU).

7. **DMA is a protection hole unless the IOMMU closes it.** A device doing DMA writes physical memory directly, bypassing the CPU's page tables. A buggy or malicious device (or a hostile Thunderbolt peripheral) could overwrite the kernel. An IOMMU (Intel VT-d, AMD-Vi) translates and checks device addresses against per-device tables, so a device can only reach buffers the OS mapped for it. The same mechanism lets a hypervisor hand a physical device to a virtual machine safely.

## Key concepts

| Term | Meaning |
|---|---|
| Device driver | Kernel module implementing a generic device interface for specific hardware |
| Memory-mapped I/O | Device registers accessed through ordinary load/store addresses |
| DMA | Direct Memory Access: the device copies data to or from memory without the CPU |
| Descriptor ring | Circular buffer of request/completion entries shared between driver and device |
| Interrupt handler (top half) | Minimal code run immediately on an interrupt |
| Bottom half | Deferred interrupt work run later with interrupts enabled |
| Polling | Checking device status in a loop instead of waiting for interrupts |
| Interrupt coalescing | Device delays interrupts to report many completions at once |
| IOMMU | Hardware that translates and restricts device memory accesses |

## How it fits

- **Below:** uses the hardware interrupt and DMA mechanisms of [buses and interrupts](../../04-computer-architecture/05-io-and-interconnect/buses-and-interrupts.md) and [DMA and devices](../../04-computer-architecture/05-io-and-interconnect/dma-and-devices.md); where drivers run is a [kernel architecture](../01-kernel-and-abstractions/kernel-architectures.md) decision.
- **Above:** the block layer serves [file systems](../05-storage-and-file-systems/file-system-implementation.md); network drivers feed the protocol stack ([media access and Ethernet](../../08-networking/02-link-layer/media-access-and-ethernet.md)); hypervisors emulate or pass through devices ([virtual machines and hypervisors](../07-virtualization/virtual-machines-and-hypervisors.md)).
- **Siblings:** [I/O models](io-models.md) define how completions surfaced by drivers are delivered to programs.

## Common misconceptions

- **"Interrupts are always better than polling."** Only at low event rates; at high rates interrupt overhead dominates and polling (or hybrid NAPI-style schemes) wins.
- **"Device memory accesses behave like normal memory."** Memory-mapped registers have side effects, must not be cached or reordered freely, and need special accessors and barriers.
- **"The OS controls all memory access."** Without an IOMMU, any DMA-capable device can read or write all of physical memory.

## Go deeper

- Jonathan Corbet, Alessandro Rubini and Greg Kroah-Hartman, *Linux Device Drivers* (3rd ed., 2005): the classic hands-on guide.
- Jeffrey C. Mogul and K. K. Ramakrishnan, "Eliminating Receive Livelock in an Interrupt-Driven Kernel" (1997): why polling wins under load.
- Andy Chou et al., "An Empirical Study of Operating Systems Errors" (SOSP 2001): where kernel bugs live.
- Michael M. Swift, Brian N. Bershad and Henry M. Levy, "Improving the Reliability of Commodity Operating Systems" (SOSP 2003): isolating drivers (Nooks).
