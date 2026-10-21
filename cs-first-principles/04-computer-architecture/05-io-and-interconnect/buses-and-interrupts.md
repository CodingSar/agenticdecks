# Buses and Interrupts

> **Layer:** [04 Computer Architecture](../README.md) › [I/O and Interconnect](README.md)
> **Builds on:** [The ISA contract](../01-instruction-set-architecture/the-isa-contract.md), [Noise and signal integrity](../../00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md), [Clocking and synchronous design](../../03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md)
> **Enables:** [DMA and devices](dma-and-devices.md), [Device drivers and interrupt handling](../../07-operating-systems/06-io-and-devices/device-drivers-and-interrupt-handling.md), [Scheduling](../../07-operating-systems/02-process-management/scheduling.md), [I/O models](../../07-operating-systems/06-io-and-devices/io-models.md)

## Essence

A bus or interconnect is the shared or point-to-point communication path that links processors, memory and devices; an interrupt is a signal by which a device asks the processor to stop what it is doing and handle an event. Together they answer two questions: how does the processor reach a device, and how does a device reach the processor? The processor reaches devices mostly by memory-mapped Input/Output (I/O): device control registers appear at physical addresses, and ordinary loads and stores read and write them. Devices reach the processor through interrupts, which the Instruction Set Architecture (ISA) treats like exceptions: save the current state, switch to kernel mode, run a handler. Interconnects evolved from wide shared parallel buses to fast serial point-to-point links, because at high speeds the physics of wires made sharing impossible.

## Core tenets

1. **Devices are controlled through registers that look like memory.** A network card might expose a status register, a control register and a "doorbell" register at a range of physical addresses. Writing the doorbell tells the device new work is ready; reading status reports completion or errors. These addresses are marked uncacheable and strongly ordered in the page tables, because a device register is not memory: reading it can change it, and writes must arrive in order and not be merged.

2. **Polling wastes the processor; interrupts let it do other work.** The processor could repeatedly read a status register until a device is ready (polling), but a disk access of 5 ms is about 15 million cycles at 3 GHz. With interrupts, the processor runs other work and the device signals when done. The interrupt hardware saves the program counter, switches to kernel mode and jumps through a vector table to the handler, exactly as for an exception.

3. **Interrupts are asynchronous, so they must be handled precisely and briefly.** An interrupt can arrive between any two instructions. The processor takes it at an instruction boundary so the interrupted program can resume as if nothing happened. Handlers run with further interrupts partly masked, so they do minimal work (acknowledge the device, queue the event) and defer the rest to a lower-priority context (Linux "softirqs" and threaded handlers).

4. **Interrupt controllers prioritise and route.** A system may have thousands of interrupt sources. An interrupt controller (the x86 Advanced Programmable Interrupt Controller (APIC), the ARM Generic Interrupt Controller (GIC), the RISC-V Platform-Level Interrupt Controller (PLIC)) assigns priorities, masks sources, and steers each interrupt to a chosen core. Modern devices use Message-Signalled Interrupts (MSI-X): the device writes a special value to a special address, so an interrupt is just a memory write, and a device can have many vectors, one per queue and core.

5. **The timer interrupt is what makes an operating system possible.** A periodic or programmable timer interrupt returns control to the kernel even if a user program loops forever. Preemptive scheduling, time-slicing and timeouts all rest on it. Without it, the Operating System (OS) would depend on programs voluntarily yielding.

6. **Interrupts have a cost that becomes visible at high rates.** Taking an interrupt and returning costs roughly a microsecond or more once cache and pipeline disruption is counted. At a million interrupts per second that is an entire core. High-speed devices therefore coalesce interrupts (one per batch), and high-performance networking and storage often switch to polling under load (Linux's New API (NAPI) for network drivers, and user-space frameworks such as the Data Plane Development Kit (DPDK) and the Storage Performance Development Kit (SPDK)).

7. **Shared parallel buses gave way to serial point-to-point links.** Early systems (the Unibus of 1970, and the Industry Standard Architecture and Peripheral Component Interconnect (PCI) buses in personal computers) used a shared set of parallel wires with arbitration. As clock rates rose, skew between parallel wires, reflections and capacitive loading of many attached devices limited speed. Peripheral Component Interconnect Express (PCIe, 2003) replaced shared buses with switched serial lanes using embedded clocking: PCIe 5.0 runs 32 GT/s per lane, about 4 GB/s per direction per lane, or about 64 GB/s for a 16-lane slot. The same shift happened on chip: cores now talk over rings and meshes, not a single bus.

8. **Interconnects are packet networks.** PCIe has physical, data link (with Cyclic Redundancy Checks (CRCs) and retries) and transaction layers. Coherent links such as Compute Express Link (CXL) extend this to shared memory between processors and accelerators: networking's ideas at nanosecond scale.

## Key concepts

| Term | Meaning |
|---|---|
| Bus | Shared set of wires connecting several components, with arbitration for access |
| Point-to-point link | Dedicated connection between two components, often serial and high-speed |
| Memory-Mapped I/O (MMIO) | Device registers accessed with ordinary loads and stores at reserved physical addresses |
| Port-mapped I/O | Separate I/O address space reached by special instructions (x86 `in`/`out`) |
| Interrupt | Asynchronous signal from a device that diverts the processor to a handler |
| Interrupt vector | Number identifying an interrupt source, used to select its handler |
| Interrupt controller | Hardware that prioritises, masks and routes interrupts to cores |
| MSI-X | Interrupt delivered as a memory write by the device, supporting many vectors |
| Interrupt coalescing | Delivering one interrupt for many events to reduce overhead |

## How it fits

- **Below:** fast serial links depend on [signal integrity](../../00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md) and line coding; crossing clock domains uses [synchronous design](../../03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md) techniques; interrupts are part of [the ISA contract's](../01-instruction-set-architecture/the-isa-contract.md) exception model.
- **Above:** [device drivers and interrupt handling](../../07-operating-systems/06-io-and-devices/device-drivers-and-interrupt-handling.md), [preemptive scheduling](../../07-operating-systems/02-process-management/scheduling.md) and [I/O models](../../07-operating-systems/06-io-and-devices/io-models.md) are built on these mechanisms; the layered link design mirrors [network layering](../../08-networking/01-principles/layering-and-the-end-to-end-principle.md).
- **Siblings:** [Direct Memory Access (DMA) and devices](dma-and-devices.md) uses the same links for bulk data and interrupts for completion.

## Common misconceptions

- **"Interrupts are always better than polling."** At high event rates, interrupt overhead dominates and polling gives lower latency and higher throughput; modern systems switch between them adaptively.
- **"A bus is a set of wires that everything shares."** That was true of older designs; modern "buses" such as PCIe are switched networks of point-to-point serial links.
- **"Device registers behave like memory."** Reads can have side effects and writes can trigger actions, which is why they must be uncached and strictly ordered.

## Go deeper

- Budruk, Anderson and Shanley, *PCI Express System Architecture* (2003): the layered PCIe protocol, from lanes to transactions and message-signalled interrupts.
- Arpaci-Dusseau and Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (2018), chapter on I/O devices: polling, interrupts and DMA from the OS side.
