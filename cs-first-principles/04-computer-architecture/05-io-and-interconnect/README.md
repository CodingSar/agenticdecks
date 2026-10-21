# I/O and Interconnect

> **Layer:** [04 Computer Architecture](../README.md) › I/O and Interconnect
> **Children:** [Buses and interrupts](buses-and-interrupts.md) · [DMA and devices](dma-and-devices.md)

## What this area is about

A processor that cannot talk to the outside world is useless. Input/Output (I/O) is how a computer exchanges data with storage, networks, displays, sensors and accelerators, and the interconnect is the set of wires and protocols that carries those exchanges, both between chips and, increasingly, within one. The question this area answers is: how does a fast, synchronous processor coordinate with devices that are slower, faster, or simply unpredictable, without wasting its time waiting for them?

Two ideas unify the answer. First, **devices look like memory**: the processor controls a device by reading and writing its registers at reserved addresses, and devices move bulk data by reading and writing main memory directly. Second, **events, not polling**: a device announces that something happened by raising an interrupt, so the processor does other work until it is needed. Together these let an Operating System (OS) treat a 100 Gbit/s network card, a Non-Volatile Memory Express (NVMe) solid-state drive and a keyboard through the same small set of mechanisms.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Buses and interrupts](buses-and-interrupts.md) | How components are connected and addressed, and how devices get the processor's attention | ISA (exceptions, privilege), digital logic (signalling) |
| [DMA and devices](dma-and-devices.md) | How devices move data without the processor, and how a device's interface is structured | Buses and interrupts, memory hierarchy |

Read [buses and interrupts](buses-and-interrupts.md) first: it covers the physical and logical connection (from shared parallel buses to point-to-point serial links such as Peripheral Component Interconnect Express (PCIe)) and the interrupt mechanism that ties devices into the processor's exception model. [DMA and devices](dma-and-devices.md) builds on this: once a device can be addressed and can interrupt, Direct Memory Access (DMA) lets it transfer whole buffers into memory and signal only on completion, which is how all high-bandwidth I/O works.

```
  CPU cores --- caches --- memory controller --- DRAM
                   |
              root complex / I/O hub (IOMMU)
              /         |           \
         PCIe link  PCIe link    PCIe link
          NVMe SSD   NIC          GPU
   control: MMIO register writes   data: DMA to/from DRAM   events: interrupts (MSI)
```

## Connections to sibling areas

- **[Instruction Set Architecture](../01-instruction-set-architecture/README.md)**: interrupts are part of the Instruction Set Architecture's (ISA's) exception model; memory-mapped I/O uses ordinary loads and stores, while x86 also keeps separate `in`/`out` port instructions.
- **[Processor Microarchitecture](../02-processor-microarchitecture/README.md)**: an interrupt must enter the pipeline at a precise point between instructions; device register accesses must not be speculated or reordered.
- **[Memory Hierarchy](../03-memory-hierarchy/README.md)**: DMA writes memory behind the caches' backs, so caches must be kept coherent with I/O; an I/O Memory Management Unit (IOMMU) translates device addresses as the Memory Management Unit (MMU) does for programs.
- **[Parallel Architecture](../04-parallel-architecture/README.md)**: Graphics Processing Units (GPUs) and accelerators are I/O devices attached over the same links; interrupts are steered to particular cores to spread load.
- **[Performance](../06-performance/README.md)**: I/O latency and bandwidth often dominate end-to-end time; interrupt overhead becomes significant at millions of events per second.

## Connections across layers

Signalling relies on [noise and signal integrity](../../00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md) and [encoding and framing](../../08-networking/02-link-layer/encoding-and-framing.md) ideas shared with networking (PCIe lanes are serial links with line coding). Upward, [device drivers and interrupt handling](../../07-operating-systems/06-io-and-devices/device-drivers-and-interrupt-handling.md) and [I/O models](../../07-operating-systems/06-io-and-devices/io-models.md) in the OS are built on these mechanisms; [virtual machines](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md) use the IOMMU to give guests direct device access; network interface cards are the hardware end of [08 Networking](../../08-networking/README.md).

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): device registers and descriptor rings form a narrow interface that drivers wrap.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): DMA and interrupt coalescing amortise per-event cost over large transfers.
- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): devices are named by addresses in the memory map; the IOMMU adds translation.
- [State and time](../../CROSS-CUTTING.md#state-and-time): interrupts are asynchronous events that arrive at arbitrary points in a program.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): polling vs interrupts trades CPU time for latency.
