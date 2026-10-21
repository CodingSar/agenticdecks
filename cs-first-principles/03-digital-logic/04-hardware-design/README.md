# Hardware Design

> **Layer:** [03 Digital Logic](../README.md) › Hardware Design
> **Children:** [Hardware Description Languages](hardware-description-languages.md) · [FPGA and ASIC](fpga-and-asic.md) · [Timing and Power](timing-and-power.md)

## What this area is about

The previous three areas explain what digital circuits are made of. This one explains how real chips with billions of transistors are actually designed, built and signed off. It answers: *how do engineers describe hardware at a manageable level of abstraction, turn that description into a physical implementation, and verify that it will be fast enough and cool enough?*

The unifying idea is **a design flow that compiles a description into hardware under constraints**. A Hardware Description Language (HDL) captures registers and logic at the register-transfer level. Synthesis, placement and routing compile it either onto a configurable Field-Programmable Gate Array (FPGA) or into a custom Application-Specific Integrated Circuit (ASIC). At every step, timing and power analysis check the result against the physical limits inherited from layer 00. It is the hardware counterpart of a software toolchain, with the difference that a shipped ASIC can never be patched.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Hardware Description Languages](hardware-description-languages.md) | The front end: describing concurrent hardware at Register-Transfer Level (RTL); simulation versus synthesis; verification | Sequential and combinational logic |
| [FPGA and ASIC](fpga-and-asic.md) | The back ends: configurable lookup-table fabric versus custom silicon, and the economics of choosing | HDLs, fabrication |
| [Timing and Power](timing-and-power.md) | Sign-off: static timing analysis, process corners, dynamic and leakage power, voltage scaling | Clocking, physical delay and energy |

The flow runs left to right through the table, with timing and power as a feedback loop around it:

```
   HDL (RTL) ──synthesis──► netlist ──place & route──► FPGA bitstream  or  ASIC layout
       ▲                                                   │
       └────────── timing & power analysis: fix and iterate ┘
```

Read HDLs first, since they define what a "design" is. FPGA and ASIC explain where it goes and why one is chosen over the other. Timing and power close the loop: a design that is functionally correct but misses its clock or power budget is not finished.

## Connections to sibling areas

- **[Number Representation](../01-number-representation/README.md):** Data widths and formats chosen there dominate area and power here; narrower formats (16-bit and 8-bit floating point) are a power decision as much as a numerical one.
- **[Combinational Logic](../02-combinational-logic/README.md):** Synthesis performs logic minimisation and maps standard building blocks onto library cells or lookup tables; critical paths run through adders and multiplexers.
- **[Sequential Logic](../03-sequential-logic/README.md):** HDL code is written in the synchronous style; static timing analysis checks precisely the setup and hold constraints defined there.

## Connections across layers

From layer 00 come the physical facts that make this area hard: [capacitance and timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md) gives delay, [thermodynamics and energy](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md) gives `CV²` and leakage, and [fabrication and scaling](../../00-engineering-foundations/03-semiconductor-devices/fabrication-and-scaling.md) gives mask cost, yield and variability. Upward, every processor in [04 Computer Architecture](../../04-computer-architecture/README.md) is produced by this flow; the power limits analysed here explain [power and the end of scaling](../../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md) and the rise of [domain-specific accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md). The toolchain parallels software compilation ([intermediate representations](../../06-programming-languages/03-compilers/intermediate-representations.md)), and verification borrows from [model checking](../../06-programming-languages/05-formal-methods/model-checking.md) and [testing](../../12-software-engineering/03-quality/testing.md).

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): RTL hides gates; synthesis and place-and-route fill them in.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): flexibility (FPGA) against efficiency (ASIC); speed against power through supply voltage.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): chips cannot be patched, so verification dominates effort.
- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): dynamic voltage and frequency scaling adjusts operating point from measured load and temperature.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): power density caps how much of a chip can run at once.
