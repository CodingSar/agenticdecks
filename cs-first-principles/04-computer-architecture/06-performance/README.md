# Performance

> **Layer:** [04 Computer Architecture](../README.md) › Performance
> **Children:** [The performance equation](the-performance-equation.md) · [Amdahl's law](amdahls-law.md) · [Power and the end of scaling](power-and-the-end-of-scaling.md)

## What this area is about

Computer architecture is a quantitative discipline: every feature is justified by how much faster, cheaper or more efficient it makes real programs, and every feature costs area, power and design effort. This area gathers the laws that make those judgements possible. The question it answers is: how do you measure a machine's speed honestly, predict the effect of a change before building it, and know which limits no design can escape?

Three laws do most of the work. The **performance equation** breaks execution time into instruction count, cycles per instruction and clock period, and shows which layers (compiler, Instruction Set Architecture (ISA), microarchitecture, circuits) control each factor. **Amdahl's law** says that speeding up part of a task is limited by the part you did not speed up, which bounds the value of every optimisation and every extra core. **Power and the end of scaling** explains the physical turning point around 2005, when Dennard scaling ended and power density, not transistor count, became the limit; that one change redirected the field from faster single cores to multicore, Graphics Processing Units (GPUs) and domain-specific accelerators.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [The performance equation](the-performance-equation.md) | Defines what to measure and decomposes time into factors that different layers control | Datapath, pipelining, ISA |
| [Amdahl's law](amdahls-law.md) | Bounds the gain from improving part of a system, including adding processors | The performance equation |
| [Power and the end of scaling](power-and-the-end-of-scaling.md) | Explains the physical limit that ended frequency scaling and why parallelism and specialisation followed | Digital logic timing and power, the performance equation |

Read the [performance equation](the-performance-equation.md) first: it is the frame for the other two. [Amdahl's law](amdahls-law.md) applies it to partial improvements. [Power and the end of scaling](power-and-the-end-of-scaling.md) adds the constraint that shaped the 21st century: since about 2005 the question has been not "how fast can it go?" but "how much can it compute per joule within a fixed power budget?"

```
 time = instructions x CPI x clock period          (what to optimise)
 speedup <= 1 / ((1 - f) + f / s)                  (how much optimising part can help)
 power ~ activity x C x V^2 x frequency             (what it costs, and why frequency stalled)
```

## Connections to sibling areas

- **[Instruction Set Architecture](../01-instruction-set-architecture/README.md)**: the ISA, together with the compiler, sets instruction count; Reduced vs Complex Instruction Set Computer (RISC vs CISC) design is a debate about trading instruction count against cycles per instruction.
- **[Processor Microarchitecture](../02-processor-microarchitecture/README.md)**: pipelining shortens the clock period, and superscalar and out-of-order execution lower cycles per instruction; their power cost is what hit the wall.
- **[Memory Hierarchy](../03-memory-hierarchy/README.md)**: memory stalls are often the largest component of cycles per instruction; the roofline model asks whether a program is limited by memory bandwidth or by compute.
- **[Parallel Architecture](../04-parallel-architecture/README.md)**: the response to the power wall, and the main domain of Amdahl's law.
- **[I/O and Interconnect](../05-io-and-interconnect/README.md)**: end-to-end performance often depends more on I/O latency and bandwidth than on the processor; Amdahl's law applies to the whole system.

## Connections across layers

The power equation comes from [timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md) in digital logic and from [Complementary Metal-Oxide-Semiconductor (CMOS)](../../00-engineering-foundations/03-semiconductor-devices/cmos.md) and [fabrication and scaling](../../00-engineering-foundations/03-semiconductor-devices/fabrication-and-scaling.md); measuring performance well is an instance of [measurement and modeling](../../00-engineering-foundations/05-engineering-method/measurement-and-modeling.md). Upward, [asymptotic analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md) ignores constant factors that this area measures; [work–span analysis](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md) generalises Amdahl's law; [scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md) and [observability](../../12-software-engineering/04-operations/observability.md) apply the same quantitative thinking to whole services.

## Cross-cutting threads

- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): every architectural feature trades area, power and complexity for speed.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): Amdahl's law and the power wall are limits no design escapes.
- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): the main way to buy performance once frequency stopped rising.
- [Composition](../../CROSS-CUTTING.md#composition): speedups of parts combine through Amdahl's law, not by multiplication.
