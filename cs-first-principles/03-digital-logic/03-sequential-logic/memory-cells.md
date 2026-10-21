# Memory Cells

> **Layer:** [03 Digital Logic](../README.md) › [Sequential Logic](README.md)
> **Builds on:** [Latches and Flip-Flops](latches-and-flip-flops.md), [The MOSFET](../../00-engineering-foundations/03-semiconductor-devices/the-mosfet.md), [Capacitance and Timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md), [Quantum Mechanics and Band Theory](../../00-engineering-foundations/01-physics-of-computation/quantum-mechanics-and-band-theory.md)
> **Enables:** [Cache Design](../../04-computer-architecture/03-memory-hierarchy/cache-design.md), [DRAM and Storage Devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md), [Locality and Caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md)

## Essence

A flip-flop costs about twenty transistors, far too many for billions of bits. Bulk memory uses much smaller cells in a grid of word lines (rows) and bit lines (columns), each storing the bit in a different physical form. Static Random-Access Memory (SRAM) holds it in a six-transistor feedback loop. Dynamic Random-Access Memory (DRAM) holds it as charge on a capacitor behind one transistor. Flash holds it as electrons trapped behind an insulator for years without power. Their different tradeoffs of speed, density, volatility and endurance decide where each sits in the memory hierarchy.

## Core tenets

1. **Memory is a grid, and the bit line is the bottleneck.** A decoder raises one word line, connecting every cell in that row to its bit line. A bit line shared by hundreds of cells has far more capacitance than one tiny cell can drive quickly. Arrays therefore precharge bit lines and use a sense amplifier, a small cross-coupled latch, to turn a swing of tens of millivolts into a full logic level.

2. **SRAM is a latch stripped to six transistors.** Two cross-coupled Complementary Metal-Oxide-Semiconductor (CMOS) inverters hold the bit; two access transistors connect it to a complementary pair of bit lines. A read lets one precharged bit line droop; a write overpowers the loop. Sizing must ensure a read never flips the cell but a write always does. The bit holds while powered, with no refresh, in the logic process.

3. **SRAM is fast but large, and it has nearly stopped shrinking.** A six-transistor (6T) cell takes roughly 100 to 150 F² (F is the feature size), an order of magnitude more than a DRAM cell, and every cell leaks. Transistor variation limits how small and how low-voltage the cell can go: cell area barely changed from 5 nm-class to 3 nm-class processes, at about 0.02 µm².

4. **DRAM is one transistor and one capacitor (1T1C), and reading destroys the bit.** Robert Dennard invented this cell at IBM in 1966. The access Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET) connects a capacitor of a few femtofarads to a bit line with several times more capacitance, so opening the cell moves the bit line by only tens of millivolts. The sense amplifier resolves that difference and writes the full value back, because charge sharing erased it. Hence a whole row is opened into a row buffer, taking tens of nanoseconds.

5. **DRAM forgets, so it must be refreshed.** Charge leaks through the access transistor and junctions, faster when hot. Standard parts guarantee retention for 64 ms (often halved above 85 °C), so the controller rewrites every row within that window, costing bandwidth and energy that grow with capacity. The tall capacitors and low-leakage transistors need a process unsuited to fast logic, so DRAM is almost always a separate chip. Activating one row very often can disturb its dense neighbours (Rowhammer).

6. **Flash traps charge behind an insulator, so it keeps data without power.** A flash cell is a MOSFET with an extra storage layer, a conducting floating gate or a silicon-nitride charge trap, wrapped in oxide. Writing uses around 15 to 20 V to push electrons through the oxide by quantum tunnelling. The trapped charge shifts the threshold voltage, which a read senses non-destructively. Storing 2, 3 or 4 bits per cell means distinguishing 4, 8 or 16 threshold levels.

7. **Flash wears out and is erased in blocks.** Each program/erase cycle damages the tunnel oxide, so endurance falls from about 10⁵ cycles at one bit per cell to thousands or fewer at three or four. NAND flash chains cells in series strings for density, erases whole blocks at once, and so cannot overwrite in place; three-dimensional (3D) NAND stacks a few hundred layers of charge-trap cells. NOR flash wires cells in parallel for fast random reads of code.

8. **Each cell's physics fixes its place in the hierarchy.** SRAM gives about 1 ns access on the processor die, so it forms registers and caches of kilobytes to tens of megabytes. DRAM is roughly ten times denser but needs its own chip, refresh and slow destructive reads, so it forms gigabytes of main memory at about 100 ns. Flash is cheaper per bit still and non-volatile, but reads take tens of microseconds and writes wear it, so it is storage.

## Key concepts

| Term | Meaning |
|---|---|
| Word line / bit line | Row-select wire / shared column data wire. |
| Sense amplifier | Latch that resolves a small bit-line difference into a full logic level. |
| 6T SRAM cell | Two cross-coupled inverters plus two access transistors. |
| 1T1C DRAM cell | One access transistor and one storage capacitor. |
| Charge sharing | Cell charge spreading onto the bit line during a DRAM read. |
| Refresh | Periodic read-and-rewrite of DRAM rows to restore leaking charge. |
| Floating gate / charge trap | Isolated conductor / nitride layer that stores flash charge. |
| Endurance | Program/erase cycles a flash cell survives. |

## How it fits

- **Below:** SRAM is the bistable loop of [latches and flip-flops](latches-and-flip-flops.md) built from [CMOS](../../00-engineering-foundations/03-semiconductor-devices/cmos.md) inverters; DRAM and flash are variations on [the MOSFET](../../00-engineering-foundations/03-semiconductor-devices/the-mosfet.md). Bit-line delay and charge sharing come from [capacitance and timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md); flash relies on [tunnelling](../../00-engineering-foundations/01-physics-of-computation/quantum-mechanics-and-band-theory.md).
- **Above:** SRAM arrays become [cache design](../../04-computer-architecture/03-memory-hierarchy/cache-design.md). DRAM banks, row buffers and the flash translation layer are in [DRAM and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md). The speed and cost gaps between cells motivate [locality and caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md), and Rowhammer becomes an attack in [side channels](../../11-security-and-cryptography/03-system-security/side-channels.md).
- **Siblings:** [Latches and flip-flops](latches-and-flip-flops.md) supply the loop SRAM shrinks. Unlike flip-flops, cells are not clocked individually; [synchronous](clocking-and-synchronous-design.md) logic around the array, often a [finite state machine](finite-state-machines.md) controller, sequences row activation and refresh.

## Common misconceptions

- **"SRAM is static, so it uses no power."** "Static" means no refresh; every cell still leaks.
- **"DRAM is slow because its transistors are slow."** It is slow mainly because a tiny charge must be sensed on a long, heavily loaded bit line and then restored.
- **"Flash is just DRAM that keeps its data."** It cannot overwrite in place and wears out, so it needs very different management.

## Go deeper

- Robert Dennard, "Field-Effect Transistor Memory," U.S. Patent 3,387,286 (1968): the one-transistor DRAM cell.
- Jan Rabaey, Anantha Chandrakasan and Borivoje Nikolić, *Digital Integrated Circuits* (2nd ed., 2003): memory cells and sense amplifiers at circuit level.
- Bruce Jacob, Spencer Ng and David Wang, *Memory Systems: Cache, DRAM, Disk* (2008): from cell to system.
- Yoongu Kim et al., "Flipping Bits in Memory Without Accessing Them" (2014): the Rowhammer study.
