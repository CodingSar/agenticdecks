# DRAM and Storage Devices

> **Layer:** [04 Computer Architecture](../README.md) › [Memory Hierarchy](README.md)
> **Builds on:** [Capacitance and timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md), [The MOSFET](../../00-engineering-foundations/03-semiconductor-devices/the-mosfet.md), [Quantum mechanics and band theory](../../00-engineering-foundations/01-physics-of-computation/quantum-mechanics-and-band-theory.md), [Locality and caching](locality-and-caching.md)
> **Enables:** [File system implementation](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md), [Crash consistency and journaling](../../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md), [LSM trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md), [B-trees](../../09-data-management/02-storage-and-indexing/b-trees.md)

## Essence

Below the caches sit the memories that hold most of the data: Dynamic Random-Access Memory (DRAM) for working memory, and non-volatile storage (NAND flash in Solid-State Drives (SSDs), and magnetic Hard Disk Drives (HDDs)) for everything that must survive power loss. Each is cheap per bit because it stores a bit in a very simple physical structure, and each pays for that simplicity with access behaviour that is far from uniform: DRAM rows must be opened before they are read, flash must be erased in large blocks before it is rewritten, and disks must move a head mechanically. The levels above, and the software that uses them, are designed around these quirks: reading and writing in large, sequential, aligned units is fast everywhere, and small random access is slow everywhere.

## Core tenets

1. **A DRAM bit is a capacitor and a transistor, which is why it is dense and why it forgets.** One transistor and one capacitor (1T1C) per bit makes DRAM roughly an order of magnitude denser than six-transistor Static RAM (SRAM). The charge leaks, so every row must be refreshed about every 64 ms, and reading is destructive: the tiny charge is sensed by amplifiers and must be written back.

2. **DRAM is organised in banks of rows, and the row buffer is a cache.** Accessing data means activating a row (typically 1–8 KiB) into the bank's row buffer, then reading columns from it. A hit in an already-open row takes roughly 15 ns of column access; opening a different row first requires closing (precharging) the old one, so a row conflict can take 40–50 ns at the device. Memory controllers reorder requests to maximise row hits and spread accesses across banks and channels.

3. **DRAM latency has barely improved while bandwidth has soared.** Raw device latency has stayed around 10–15 ns per timing step for decades, and a full load-to-use miss is still about 80–100 ns on 2020s servers. Bandwidth, meanwhile, rose from about 1.6 GB/s per channel (DDR-200, 2000) to about 50 GB/s (DDR5-6400). Stacked High Bandwidth Memory (HBM) beside GPUs and accelerators reaches several TB/s. This is why modern design hides latency with parallelism (many outstanding misses, prefetching) rather than reducing it.

4. **NAND flash stores charge on an insulated gate and cannot be overwritten in place.** Electrons are trapped by quantum tunnelling into a floating gate or charge-trap layer, changing the transistor's threshold voltage; storing 2, 3 or 4 bits per cell (MLC, TLC, QLC) means distinguishing 4, 8 or 16 voltage levels. Reads and writes happen in pages (around 4–16 KiB), but erasure happens only in much larger blocks (megabytes). Each cell survives a limited number of erase cycles (thousands for TLC, fewer for QLC).

5. **The flash translation layer makes flash look like a disk.** Because pages cannot be rewritten in place, the SSD controller writes new data to fresh pages, keeps a mapping from logical block addresses to physical pages, and garbage-collects blocks with mostly stale pages. This causes write amplification (more physical writes than logical ones) and makes performance depend on free space. Writing sequentially and telling the device which blocks are free (TRIM) helps it. Log-structured file systems and Log-Structured Merge (LSM) trees match this behaviour.

6. **Disks are dominated by mechanical motion.** An HDD reads magnetised regions on spinning platters. A random access needs a seek (moving the arm, several ms) and rotational latency (half a revolution: 4.2 ms at 7,200 RPM). Once positioned, sequential transfer runs at 200–300 MB/s. So a disk does roughly 100–200 random operations per second but streams well, which is why disk-era data structures (B-trees, extent-based file systems) read and write large contiguous blocks.

7. **The interface matters as much as the medium.** Non-Volatile Memory Express (NVMe) over Peripheral Component Interconnect Express (PCIe) gives SSDs up to 65,535 parallel queues, each up to 65,536 commands deep, versus the single 32-entry queue and higher overheads of the older SATA/AHCI interface designed for disks. With flash reads taking tens of microseconds (and low-latency media around 10 µs), Operating System (OS) software overhead per I/O becomes a significant fraction of the total.

8. **Volatility defines the persistence boundary.** DRAM loses everything on power loss; SSDs and HDDs do not, but they often buffer writes in volatile caches. Durability therefore requires explicit flush commands and careful ordering, which is the root problem of crash consistency in file systems and databases.

| Device (2020s) | Random read latency | Sequential bandwidth | Unit of efficient access |
|---|---|---|---|
| DRAM (DDR5) | ~80–100 ns (load-to-use) | ~50 GB/s per channel | 64-byte line, open row |
| NVMe TLC SSD | ~50–100 µs | 3–14 GB/s | 4–16 KiB page, large writes |
| HDD (7,200 RPM) | ~5–10 ms | 0.2–0.3 GB/s | Large sequential extents |

## Key concepts

| Term | Meaning |
|---|---|
| DRAM | Dynamic RAM: one transistor and capacitor per bit, needs periodic refresh |
| Row buffer | Per-bank latch holding the currently open DRAM row |
| Refresh | Periodic rewriting of DRAM rows to restore leaking charge |
| NAND flash | Non-volatile memory storing charge in transistor gates, erased in blocks |
| Erase block | Smallest unit of flash that can be erased, much larger than a page |
| Flash Translation Layer (FTL) | SSD firmware mapping logical blocks to physical flash pages |
| Write amplification | Ratio of physical writes to logical writes caused by garbage collection |
| Seek time / rotational latency | Time to move a disk head / wait for the sector to rotate under it |
| HBM | High Bandwidth Memory: DRAM stacked near the processor with a very wide interface |

## How it fits

- **Below:** DRAM cells rely on [capacitance](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md) and [MOSFET](../../00-engineering-foundations/03-semiconductor-devices/the-mosfet.md) switches; flash on [quantum tunnelling](../../00-engineering-foundations/01-physics-of-computation/quantum-mechanics-and-band-theory.md); reliability on [error-correcting codes](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md) built into memory and SSD controllers.
- **Above:** [file systems](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md), [journaling](../../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md), [B-trees](../../09-data-management/02-storage-and-indexing/b-trees.md) and [LSM trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md) are shaped by these devices; Rowhammer, where repeated DRAM row activation flips bits in neighbouring rows, is a hardware fault turned [security attack](../../11-security-and-cryptography/03-system-security/side-channels.md).
- **Siblings:** these are the lowest levels of the hierarchy described in [locality and caching](locality-and-caching.md); [virtual memory](virtual-memory-hardware.md) uses DRAM as a page cache for storage; storage is reached through [DMA and device interfaces](../05-io-and-interconnect/dma-and-devices.md).

## Common misconceptions

- **"RAM is random access, so every address costs the same."** DRAM latency depends on whether the row is open, which bank is busy and how far away the memory controller is; sequential access is much faster.
- **"SSDs have no penalty for random writes."** Random small writes cause garbage collection and write amplification; sustained random-write throughput can be far below the advertised peak.
- **"Data written is data saved."** Until a flush completes, data may sit in volatile OS or device caches and be lost on power failure.

## Go deeper

- Jacob, Ng and Wang, *Memory Systems: Cache, DRAM, Disk* (2008): the comprehensive reference across all three.
- Drepper, *What Every Programmer Should Know About Memory* (2007): DRAM organisation and its effect on software.
- Arpaci-Dusseau and Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (2018), chapters on hard disks and flash-based SSDs.
- Kim et al., *Flipping Bits in Memory Without Accessing Them* (ISCA 2014): the Rowhammer paper.
