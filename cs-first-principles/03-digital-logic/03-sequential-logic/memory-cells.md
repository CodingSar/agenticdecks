# Memory Cells

> **Layer:** [03 Digital Logic](../README.md) › [Sequential Logic](README.md)
> **Builds on:** [Latches and Flip-Flops](latches-and-flip-flops.md), [CMOS](../../00-engineering-foundations/03-semiconductor-devices/cmos.md), [The MOSFET](../../00-engineering-foundations/03-semiconductor-devices/the-mosfet.md), [Capacitance and Timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md), [Quantum Mechanics and Band Theory](../../00-engineering-foundations/01-physics-of-computation/quantum-mechanics-and-band-theory.md)
> **Enables:** [Cache Design](../../04-computer-architecture/03-memory-hierarchy/cache-design.md), [DRAM and Storage Devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md), [Locality and Caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md)

## Essence

A flip-flop stores a bit well but costs about twenty transistors, far too many for billions of bits. Bulk memory uses much smaller cells arranged in a grid of word lines (rows) and bit lines (columns), and each design stores a bit in a different physical form. Static Random-Access Memory (SRAM) holds it in a positive-feedback loop of six transistors. Dynamic Random-Access Memory (DRAM) holds it as charge on a capacitor behind one transistor. Flash holds it as electrons trapped in an insulator, where they stay for years without power. Each form trades speed, density, volatility and endurance differently. Those tradeoffs, not design fashion, decide where each technology sits in the memory hierarchy.

## Core tenets

1. **Memory is a grid, and the bit line is the bottleneck.** A decoder raises one word line, which connects every cell in that row to its bit line. A bit line is long and shared by hundreds of cells, so its capacitance is far larger than one cell can quickly drive. Arrays therefore precharge the bit lines and use a sense amplifier, a small cross-coupled latch, to turn a swing of tens of millivolts into a full logic level. The physics of the cell decides how large and how fast that swing is.

2. **SRAM is a latch stripped to six transistors.** Two cross-coupled Complementary Metal-Oxide-Semiconductor (CMOS) inverters hold the bit. Two access transistors, gated by the word line, connect the two storage nodes to a complementary pair of bit lines. A read lets one precharged bit line droop slightly. A write drives the bit lines hard enough to overpower the loop. Transistor sizes must satisfy two opposing demands: a read must not flip the cell, and a write must. The bit holds for as long as power is on, with no refresh, and it is built in the same logic process as the processor.

3. **SRAM is fast but large, and it has stopped shrinking.** A 6T cell takes roughly 100 to 150 F², where F is the process feature size. That is an order of magnitude or more larger than a DRAM cell, and every cell leaks. At leading-edge nodes, variation between "identical" transistors limits how small and how low-voltage the cell can go. Cell area barely changed between 5 nm-class and 3 nm-class processes, at about 0.02 µm². Register files use variants with extra ports or a separate read path (8T cells), trading more area for bandwidth and stability.

4. **DRAM is one transistor and one capacitor, and reading destroys the bit.** Robert Dennard invented the one-transistor cell at IBM in 1966. The access Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET) connects a capacitor of a few femtofarads to a bit line with several times more capacitance. Opening the cell shares its charge with the bit line and moves the bit line by only tens of millivolts. The sense amplifier resolves that difference and then writes the full value back, because charge sharing has erased it. This is why a DRAM access opens a whole row into a row buffer and why array timing is tens of nanoseconds.

5. **DRAM forgets, so it must be refreshed.** Charge leaks through the access transistor's subthreshold current and through junctions, and the leakage rises steeply with temperature. Standard parts guarantee retention for 64 ms (often halved above 85 °C). The controller therefore issues refresh commands that read and rewrite every row within that window, which costs bandwidth and energy and grows with capacity. Cells are tall stacked or deep-trench capacitors on low-leakage transistors, a process unsuited to fast logic, so DRAM is almost always a separate chip. Packing rows densely also lets heavy activation of one row disturb its neighbours (Rowhammer).

6. **Flash stores charge behind an insulator, so it keeps data without power.** A flash cell is a MOSFET with an extra storage layer: a conducting floating gate, or a silicon-nitride charge-trap layer, surrounded by oxide. Writing uses high voltage (around 15 to 20 V) to push electrons through the oxide by quantum tunnelling. The trapped charge raises the threshold voltage, which a read senses without disturbing the bit. The barrier keeps the charge for years. Storing 2, 3 or 4 bits per cell means distinguishing 4, 8 or 16 threshold levels.

7. **Flash wears out and is erased in blocks.** Each program/erase cycle damages the tunnel oxide, so endurance runs from about 10⁵ cycles for one bit per cell down to thousands or fewer for three and four bits. NAND flash wires cells in series strings sharing one contact, which makes it dense. Cells are erased together by block, so data cannot be overwritten in place. Today's 3D NAND stacks charge-trap cells in a few hundred layers. NOR flash wires cells in parallel for fast random reads and suits code storage.

8. **Each cell's physics fixes its place in the hierarchy.** SRAM gives about 1 ns access in the logic process, so it forms registers and caches of kilobytes to tens of megabytes. DRAM is roughly ten times denser per bit but needs its own process, refresh and slow destructive reads. It forms gigabytes of main memory at about 100 ns. Flash costs roughly a tenth of DRAM per bit or less and survives power loss. Its reads take tens of microseconds and its writes are slower and wearing, so it is storage, not memory. Newer cells, such as Magnetoresistive Random-Access Memory (MRAM) and phase-change memory, try to fill the gaps between these levels.

## Key concepts

| Term | Meaning |
|---|---|
| Word line / bit line | Row-select wire / shared column wire carrying data to and from cells. |
| Sense amplifier | Latch that resolves a small bit-line difference into a full logic level. |
| 6T SRAM cell | Two cross-coupled inverters plus two access transistors. |
| 1T1C DRAM cell | One access transistor and one storage capacitor. |
| Charge sharing | Redistribution of cell charge onto the bit line during a DRAM read. |
| Refresh | Periodic read-and-rewrite of DRAM rows to restore leaking charge. |
| Retention time | How long a cell keeps a readable value without refresh or power. |
| Floating gate / charge trap | Isolated conductor / insulating nitride layer that stores flash charge. |
| Endurance | Number of program/erase cycles a flash cell survives. |
| F² | Cell area in units of the squared feature size, for comparing density across processes. |

## How it fits

- **Below:** SRAM is the bistable loop of [latches and flip-flops](latches-and-flip-flops.md) built from [CMOS](../../00-engineering-foundations/03-semiconductor-devices/cmos.md) inverters. DRAM and flash are variations on [the MOSFET](../../00-engineering-foundations/03-semiconductor-devices/the-mosfet.md). Bit-line delay and charge sharing come from [capacitance and timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md), and flash relies on tunnelling from [quantum mechanics and band theory](../../00-engineering-foundations/01-physics-of-computation/quantum-mechanics-and-band-theory.md). Particle-induced soft errors, described in [noise and signal integrity](../../00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md), are why large arrays carry error-correcting codes.
- **Above:** SRAM arrays become [cache design](../../04-computer-architecture/03-memory-hierarchy/cache-design.md) and register files. DRAM banks, row buffers and refresh, and the flash translation layer that hides erase blocks, are covered in [DRAM and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md). The resulting speed and cost gaps are the reason for [locality and caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md). Rowhammer becomes an attack in [side channels](../../11-security-and-cryptography/03-system-security/side-channels.md).
- **Siblings:** [Latches and flip-flops](latches-and-flip-flops.md) give the bistable loop that SRAM shrinks. Unlike flip-flops, memory cells are not clocked one by one. They are read and written through a decoder by the [synchronous](clocking-and-synchronous-design.md) logic around the array, often a [finite state machine](finite-state-machines.md) controller that sequences row activation and refresh.

## Common misconceptions

- **"SRAM is static, so it uses no power."** "Static" means it needs no refresh. Every cell still leaks, and large caches spend a real share of chip power on leakage.
- **"DRAM is slow because its transistors are slow."** It is slow mainly because a tiny charge must be sensed on a long, heavily loaded bit line and then restored.
- **"Flash is just slow DRAM that keeps its data."** Flash cannot be overwritten in place and wears out, so it needs very different management from memory.

## Go deeper

- Robert Dennard, "Field-Effect Transistor Memory," U.S. Patent 3,387,286 (1968): the one-transistor DRAM cell.
- Jan Rabaey, Anantha Chandrakasan and Borivoje Nikolić, *Digital Integrated Circuits* (2nd ed., 2003): memory arrays, cells and sense amplifiers at circuit level.
- Bruce Jacob, Spencer Ng and David Wang, *Memory Systems: Cache, DRAM, Disk* (2008): from cell to system across the hierarchy.
- Yoongu Kim et al., "Flipping Bits in Memory Without Accessing Them" (2014): the Rowhammer study of DRAM disturbance errors.
