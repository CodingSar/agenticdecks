# Pipelining

> **Layer:** [04 Computer Architecture](../README.md) › [Processor Microarchitecture](README.md)
> **Builds on:** [Datapath and control](datapath-and-control.md), [Clocking and synchronous design](../../03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md), [RISC vs CISC](../01-instruction-set-architecture/risc-vs-cisc.md)
> **Enables:** [Hazards and branch prediction](hazards-and-branch-prediction.md), [Superscalar and out-of-order](superscalar-and-out-of-order.md), [The performance equation](../06-performance/the-performance-equation.md)

## Essence

Pipelining splits the execution of each instruction into stages and runs different instructions in different stages at the same time, like an assembly line. Each stage is a slice of the datapath separated from the next by pipeline registers, so the clock period shrinks to the length of the slowest stage rather than the whole instruction. With k balanced stages, a new instruction can start every cycle and throughput approaches k times that of the unpipelined design, even though each individual instruction takes as long as before, or slightly longer. Pipelining raises throughput, not latency, and that distinction explains all of its benefits and all of its problems.

## Core tenets

1. **Throughput, not latency, is what improves.** The classic five-stage Reduced Instruction Set Computer (RISC) pipeline (Fetch, Decode, Execute, Memory, Write-back) still takes five cycles per instruction, but completes one instruction per cycle once full. For a long run of instructions, Cycles Per Instruction (CPI) approaches 1 while the cycle time drops to about one fifth. Programs are long, so throughput is what matters.

2. **Pipeline registers are what make overlap possible.** Between stages sit registers that hold each instruction's intermediate results and control signals. They isolate stages from each other so that each stage works on a different instruction in the same cycle. They also cost time: each adds setup time and clock-to-output delay, typically tens of picoseconds in modern processes, which is pure overhead.

3. **The slowest stage sets the clock.** If one stage takes 400 ps and the others 200 ps, the clock must be 400 ps and the fast stages idle half the time. Designers balance stages by moving logic between them or splitting slow ones. The cache access stage is often the hardest to shorten, which is why level-1 (L1) caches are kept small (32–64 KiB per core in 2020s designs).

4. **Deeper pipelines have diminishing and then negative returns.** Splitting into more stages shortens each, but the fixed register overhead per stage grows as a fraction, and every stall or flush throws away more work. The Intel Pentium 4 (2000–2006) pushed to 20 and then 31 stages to reach 3.8 GHz, but its high misprediction cost and power led Intel back to roughly 14-stage designs (Core, 2006). Most 2020s high-performance cores have roughly 10–20 stages.

5. **Overlap exposes dependences as hazards.** An instruction that needs a result not yet written, two instructions wanting the same hardware, or a branch whose outcome is unknown when the next instruction must be fetched all prevent the next instruction from entering the pipeline. These hazards are the price of pipelining; handling them (forwarding, stalling, prediction) is the subject of [hazards and branch prediction](hazards-and-branch-prediction.md).

6. **Regular instructions pipeline well, irregular ones do not.** Pipelining assumes each instruction passes through the same stages in the same order, using each stage once. Fixed-length, load/store Reduced Instruction Set Computer (RISC) instructions fit that pattern; complex instructions with several memory operands do not. This is why pipelining was the decisive argument for RISC in the 1980s and why x86 cores break instructions into simple micro-operations before pipelining them.

7. **Pipelining is a general principle, not only a processor trick.** Floating-point units are pipelined internally (a fused multiply-add typically takes 4 cycles of latency but accepts a new one every cycle). The same idea appears in graphics pipelines, network protocols that keep several packets in flight, and data-processing stages in software.

```
cycle:    1  2  3  4  5  6  7
i1        F  D  E  M  W
i2           F  D  E  M  W
i3              F  D  E  M  W
i4                 F  D  E  M  W   <- one instruction completes per cycle from cycle 5
```

## Key concepts

| Term | Meaning |
|---|---|
| Stage | One slice of the instruction's work, taking one clock cycle |
| Pipeline register | State element between stages holding an instruction's in-flight data and control |
| Pipeline depth | Number of stages |
| Throughput | Instructions completed per unit time |
| Latency | Time from an instruction's start to its completion |
| CPI | Average cycles per instruction; ideal pipelined CPI is 1 |
| Stall (bubble) | A cycle in which a stage does no useful work because of a hazard |
| Flush | Discarding instructions in the pipeline that should not have entered it |

## How it fits

- **Below:** each stage is combinational logic bounded by [clocked registers](../../03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md); stage timing comes from [timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md) analysis.
- **Above:** [compilers](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md) schedule instructions to fill load and branch delays; the throughput–latency distinction reappears in [networking](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) and in [Graphics Processing Unit (GPU) rasterization pipelines](../../14-human-and-visual-computing/02-computer-graphics/rasterization-pipeline.md).
- **Siblings:** builds on the [datapath](datapath-and-control.md); creates the problems solved by [hazard handling and branch prediction](hazards-and-branch-prediction.md); [superscalar](superscalar-and-out-of-order.md) cores run several pipelines side by side.

## Common misconceptions

- **"Pipelining makes each instruction faster."** Each instruction takes the same or slightly longer; only the rate of completion goes up.
- **"More stages always means more speed."** Beyond a point, register overhead, branch-misprediction penalties and power outweigh the shorter cycle; the Pentium 4 is the standard cautionary example.
- **"A k-stage pipeline gives exactly k times speedup."** Unbalanced stages, register overhead and hazards all keep the real gain below k.

## Go deeper

- Patterson and Hennessy, *Computer Organization and Design* (RISC-V edition, 2017), Chapter 4: the five-stage pipeline in detail.
- Hennessy and Patterson, *Computer Architecture: A Quantitative Approach* (6th ed., 2017), Appendix C: pipelining basics with quantitative examples.
- Hartstein and Puzak, *The Optimum Pipeline Depth for a Microprocessor* (ISCA 2002): a model of why depth has an optimum.
