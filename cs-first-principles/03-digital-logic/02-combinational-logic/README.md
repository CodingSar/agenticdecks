# Combinational Logic

> **Layer:** [03 Digital Logic](../README.md) › Combinational Logic
> **Children:** [Logic Gates](logic-gates.md) · [Logic Minimization](logic-minimization.md) · [Arithmetic and Building Blocks](arithmetic-and-building-blocks.md)

## What this area is about

Combinational logic is hardware that computes a function: its outputs depend only on its present inputs, with no memory of the past. This area answers: *how do we turn any Boolean function into a physical circuit, how do we make that circuit small and fast, and what standard circuits do computers actually need?* It is the place where the formal pillar's Boolean algebra and the physical pillar's Complementary Metal-Oxide-Semiconductor (CMOS) transistors first meet as working parts.

The unifying idea is that **a function is a network of gates, and its cost is size (area, energy) and depth (delay)**. Any function can be built, because a few gate types are functionally complete; the engineering question is how cheaply. Minimisation reduces size for arbitrary logic. For the regular, heavily used functions, especially arithmetic, the best circuits come from algorithmic insight: an adder that computes carries with a parallel-prefix tree has logarithmic rather than linear depth.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Logic Gates](logic-gates.md) | The primitives: Boolean functions with timing, functional completeness, CMOS realities, hazards | Boolean algebra, CMOS |
| [Logic Minimization](logic-minimization.md) | Making arbitrary logic cheap: prime implicants, Karnaugh maps, heuristics, BDDs (Binary Decision Diagrams) | Gates |
| [Arithmetic and Building Blocks](arithmetic-and-building-blocks.md) | The standard parts: multiplexers, decoders, adders, multipliers, shifters, the ALU (Arithmetic Logic Unit) | Gates, number representation |

Read gates first: they define the vocabulary and the cost model (fan-in, fan-out, delay). Minimisation and building blocks are two complementary answers to "how do we build functions well?": minimisation is the general-purpose, automated approach for irregular control logic, while building blocks are the hand-designed, algorithmically optimised structures for regular datapath functions. Real designs use both: a processor's ALU is a building block, its control decoding is minimised logic.

```
   Boolean algebra (01)        CMOS (00)
             \                  /
              ▼                ▼
               logic gates  (function + delay)
                 │                    │
         irregular logic       regular datapath functions
                 ▼                    ▼
        logic minimization    arithmetic & building blocks
                 └─────────┬──────────┘
                           ▼
            combinational part of every digital system
```

## Connections to sibling areas

- **[Number Representation](../01-number-representation/README.md):** The encodings determine the circuits: two's complement lets one adder handle signed and unsigned values; floating-point formats determine the structure of floating-point units.
- **[Sequential Logic](../03-sequential-logic/README.md):** Adding feedback to gates creates memory. Every synchronous circuit is combinational logic between flip-flops, and the combinational delay sets the clock period.
- **[Hardware Design](../04-hardware-design/README.md):** Designers write combinational logic in hardware description languages; synthesis tools minimise and map it; timing analysis checks its depth; on Field-Programmable Gate Arrays it becomes lookup tables.

## Connections across layers

From below, gates take their functions from [Boolean algebra](../../01-mathematical-foundations/04-algebra/boolean-algebra.md) and their physics from [CMOS](../../00-engineering-foundations/03-semiconductor-devices/cmos.md) and [capacitance and timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md). Minimisation is hard for the reasons given in [P, NP and NP-completeness](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md). Upward, these blocks form the [datapath and control](../../04-computer-architecture/02-processor-microarchitecture/datapath-and-control.md) of processors and the multiply-accumulate arrays of [domain-specific accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md). Fast adders are parallel prefix computations, the same pattern analysed in [work, span and parallel models](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md); BDDs and satisfiability reappear in [model checking](../../06-programming-languages/05-formal-methods/model-checking.md).

## Cross-cutting threads

- [Composition](../../CROSS-CUTTING.md#composition): any function is composed from a functionally complete gate set, with delays that add along paths.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): transistors hidden behind truth tables, gates hidden behind blocks such as the ALU.
- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): parallel-prefix adders and carry-save trees trade area for depth.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): area against delay against power in every block.
