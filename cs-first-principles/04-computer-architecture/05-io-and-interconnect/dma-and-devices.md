# DMA and Devices

> **Layer:** [04 Computer Architecture](../README.md) › [I/O and Interconnect](README.md)
> **Builds on:** [Buses and interrupts](buses-and-interrupts.md), [Cache design](../03-memory-hierarchy/cache-design.md), [Virtual memory hardware](../03-memory-hierarchy/virtual-memory-hardware.md)
> **Enables:** [Device drivers and interrupt handling](../../07-operating-systems/06-io-and-devices/device-drivers-and-interrupt-handling.md), [Virtual machines and hypervisors](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md), [Media access and Ethernet](../../08-networking/02-link-layer/media-access-and-ethernet.md), [File system implementation](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md)

## Essence

Direct Memory Access (DMA) lets a device read and write main memory itself, without the processor copying each word. The processor sets up a transfer (where in memory, how many bytes, which direction), the device moves the data at its own pace, and an interrupt reports completion. Every high-bandwidth device, from Solid-State Drives (SSDs) to network cards and Graphics Processing Units (GPUs), works this way, usually through rings of descriptors in shared memory that let the processor and device hand work back and forth with minimal synchronisation. DMA frees the processor, but it creates two problems that the architecture must solve: keeping caches consistent with memory the device changes, and stopping a device from writing memory it should not touch.

## Core tenets

1. **Programmed I/O does not scale.** If the processor moves every word with a load from a device register and a store to memory, a 10 GB/s device would occupy several cores just copying. DMA moves the copying to the device (or a DMA engine), so the processor's cost per transfer is fixed (set up, take one interrupt) rather than proportional to the bytes moved.

2. **Descriptor rings are the standard device interface.** The driver allocates a circular array of descriptors in memory, each pointing to a buffer and recording its length and status. The processor fills descriptors and writes a "tail" index to a device doorbell register; the device consumes them, performs DMA, writes back status, and advances a "head". Network interface cards, Non-Volatile Memory Express (NVMe) SSDs and GPUs all use variants of this producer-consumer queue, often with one pair of queues per core so cores do not contend.

3. **Scatter-gather avoids copying into contiguous buffers.** A program's buffer may span many physical pages that are not contiguous. Descriptors can list several (address, length) pieces, letting the device gather data from them or scatter data into them. This makes zero-copy I/O possible: data moves straight between the device and the application's pages.

4. **DMA must be coherent with caches.** A device writing memory leaves stale copies in processor caches; a device reading memory may miss newer data still in a write-back cache. x86 server platforms keep DMA cache-coherent in hardware (devices' accesses snoop the caches, and Intel's Data Direct I/O even places incoming data directly in the last-level cache). Many ARM and embedded systems are not coherent for all devices, so drivers must explicitly flush or invalidate cache lines around each transfer.

5. **Devices need address translation and protection too.** A buggy or malicious device that can DMA anywhere can overwrite the kernel. An Input/Output Memory Management Unit (IOMMU; Intel VT-d, AMD-Vi, ARM SMMU) translates device addresses through per-device page tables, so each device can reach only the buffers the Operating System (OS) mapped for it. The IOMMU also lets a virtual machine own a device directly (device pass-through) without being able to corrupt the host.

6. **Devices are computers too.** A modern SSD controller runs firmware on several embedded cores to manage its flash translation layer; a network card may offload checksums, segmentation and encryption, or run whole programs (SmartNICs and Data Processing Units). From the host's view they are still devices behind registers, rings and interrupts, but the boundary of "what the OS controls" has moved.

7. **Virtualising devices puts the mechanism in hardware.** Single Root I/O Virtualization (SR-IOV) lets one physical device present many virtual functions, each with its own queues and interrupts, assigned to different virtual machines through the IOMMU. This gives near-native I/O performance to guests, where software emulation would cost a trap per register access.

8. **Ordering and completion semantics matter for correctness.** A driver must make descriptor contents visible to the device before ringing the doorbell (a write barrier), and must not reuse a buffer until the device reports completion. A storage device acknowledging a write may still hold it in a volatile cache; durable storage requires an explicit flush. These rules are where hardware details leak into OS and database correctness.

## Key concepts

| Term | Meaning |
|---|---|
| DMA | Direct Memory Access: a device transferring data to or from memory without the processor |
| Programmed I/O | The processor moves every word between a device and memory itself |
| Descriptor | Memory record telling a device where a buffer is, its length and its status |
| Descriptor ring | Circular queue of descriptors shared by driver and device |
| Doorbell | Device register written to notify it of new work |
| Scatter-gather | DMA over a list of non-contiguous memory pieces |
| IOMMU | Translation and protection unit for device-initiated memory accesses |
| DMA coherence | Whether device accesses observe and update processor caches automatically |
| SR-IOV | Single Root I/O Virtualization: one device exposing multiple independent virtual functions |

## How it fits

- **Below:** DMA traffic runs over the links and uses the interrupts of [buses and interrupts](buses-and-interrupts.md); coherence with [caches](../03-memory-hierarchy/cache-design.md) and translation by the IOMMU mirror [virtual memory hardware](../03-memory-hierarchy/virtual-memory-hardware.md).
- **Above:** [device drivers](../../07-operating-systems/06-io-and-devices/device-drivers-and-interrupt-handling.md) manage rings and buffers; [hypervisors](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md) use IOMMUs and SR-IOV; [file systems](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md) and [crash consistency](../../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md) depend on flush semantics; [Ethernet](../../08-networking/02-link-layer/media-access-and-ethernet.md) cards deliver packets by DMA; DMA from untrusted peripherals is an [isolation](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md) concern.
- **Siblings:** [buses and interrupts](buses-and-interrupts.md) provides control and signalling; DMA provides bulk data. The devices at the other end are described in [DRAM and storage devices](../03-memory-hierarchy/dram-and-storage-devices.md).

## Common misconceptions

- **"DMA means the CPU is not involved."** The Central Processing Unit (CPU) still sets up transfers, handles completions and manages buffers; DMA removes only the per-byte copying.
- **"Device memory accesses are automatically safe."** Without an IOMMU, any device that can master the bus can read or write all of physical memory; attacks through Thunderbolt and FireWire ports have exploited this.
- **"Zero-copy is always faster."** Setting up mappings and pinning pages has cost; for small transfers a copy is often cheaper.

## Go deeper

- Arpaci-Dusseau and Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (2018), chapter on I/O devices: DMA, polling and interrupts from the OS view.
- Corbet, Rubini and Kroah-Hartman, *Linux Device Drivers* (3rd ed., 2005): DMA mapping and ring buffers in a real kernel.
- Ben-Yehuda et al., *The Price of Safety: Evaluating IOMMU Performance* (Ottawa Linux Symposium, 2007): what device isolation costs.
