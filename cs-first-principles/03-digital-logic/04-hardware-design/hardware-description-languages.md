# Hardware Description Languages

> **Layer:** [03 Digital Logic](../README.md) › [Hardware Design](README.md)
> **Builds on:** [Finite State Machines](../03-sequential-logic/finite-state-machines.md), [Logic Minimization](../02-combinational-logic/logic-minimization.md), [Clocking and Synchronous Design](../03-sequential-logic/clocking-and-synchronous-design.md)
> **Enables:** [FPGA and ASIC](fpga-and-asic.md), [Timing and Power](timing-and-power.md), [Datapath and Control](../../04-computer-architecture/02-processor-microarchitecture/datapath-and-control.md)

## Essence

Modern chips contain billions of transistors, far too many to draw. Designers instead write text in a Hardware Description Language (HDL), such as Verilog, VHDL (the Very High Speed Integrated Circuit Hardware Description Language) or SystemVerilog, describing registers and the logic between them at the Register-Transfer Level (RTL). Two very different programs consume that text. A simulator executes it to predict behaviour, and a synthesis tool compiles it into a netlist of gates and flip-flops to be built. An HDL looks like a programming language but describes something fundamentally different: many pieces of hardware that all exist and operate at the same time. The central discipline is writing code whose simulated meaning and synthesised hardware agree.

## Core tenets

1. **HDL code describes structure that runs concurrently, not steps that run in order.** Every `assign` statement and every `always` block in Verilog is a separate piece of hardware operating in parallel all the time. A line lower in the file does not happen "after" a line above it. Programmers new to HDLs most often go wrong by imagining sequential execution.

2. **Register-transfer level is the working abstraction.** At RTL, the designer specifies which registers exist, and for each clock cycle what combinational function of registers and inputs computes their next values. This matches the synchronous design model exactly: registers plus logic plus a clock. Synthesis tools then handle gate-level detail, minimisation and technology mapping, the way a compiler handles instruction selection.

3. **Simulation semantics and synthesis semantics differ.** Simulators use an event-driven model: when a signal changes, processes sensitive to it are re-evaluated, ordered by a scheduler with explicit rules. Synthesis infers hardware from patterns. Only a subset of the language is synthesisable (delays such as `#10`, file input/output and most loops with run-time bounds are simulation-only). Code outside the synthesisable subset, or code relying on simulation ordering, can simulate correctly and produce different or no hardware.

4. **Coding idioms decide what hardware is inferred.** In Verilog, `always @(posedge clk)` with non-blocking assignments (`<=`) infers flip-flops that all update together at the edge, matching real registers. Combinational blocks use `always @*` with blocking assignments (`=`). If a combinational block fails to assign a signal on some path, the tool must remember its old value and infers an unintended latch. Mixing these idioms is the classic source of simulation-synthesis mismatch.

```verilog
// A 4-bit counter with synchronous reset: one register, one adder, one mux.
always @(posedge clk)
  if (reset) count <= 4'd0;
  else       count <= count + 4'd1;
```

5. **Verification dominates the effort.** Because a chip costs millions to fabricate and cannot be patched, designs are tested exhaustively before tape-out. Testbenches drive inputs and check outputs; SystemVerilog adds assertions, constrained-random stimulus and coverage metrics; formal tools prove properties and check that the synthesised netlist is equivalent to the RTL. On large projects verification commonly takes more engineering effort than design.

6. **Higher-level generators raise abstraction further.** High-Level Synthesis (HLS) compiles C or C++ functions into RTL, scheduling operations into cycles and choosing hardware resources. Hardware construction languages such as Chisel (embedded in Scala, 2012) use a general-purpose language to *generate* RTL, making parameterised designs (a cache of any size, a processor with any number of pipelines) practical. These trade some control over the result for productivity.

7. **HDL history reflects two traditions.** Verilog (1984, standardised by the Institute of Electrical and Electronics Engineers (IEEE) as IEEE 1364 in 1995) came from industry simulators and has C-like syntax. VHDL (IEEE 1076, 1987) came from a United States defence programme and is strongly typed in the style of Ada. SystemVerilog (IEEE 1800, 2005) extended Verilog with verification features and is now the dominant language in industry.

## Key concepts

| Term | Meaning |
|---|---|
| Hardware Description Language (HDL) | A language for describing digital circuits for simulation and synthesis. |
| Register-Transfer Level (RTL) | Description in terms of registers and the logic computing their next values. |
| Synthesis | Compiling HDL into a gate-level netlist for a target technology. |
| Netlist | A list of cells and the wires connecting them. |
| Event-driven simulation | Re-evaluating processes when signals they depend on change. |
| Blocking / non-blocking assignment | Immediate (`=`) versus end-of-step (`<=`) update in Verilog. |
| Inferred latch | Unintended storage created when a combinational signal is not always assigned. |
| Testbench | Non-synthesisable code that stimulates and checks a design in simulation. |
| High-Level Synthesis (HLS) | Generating RTL from a software-like language description. |

## How it fits

- **Below:** HDLs express [finite state machines](../03-sequential-logic/finite-state-machines.md), [combinational building blocks](../02-combinational-logic/arithmetic-and-building-blocks.md) and [synchronous design](../03-sequential-logic/clocking-and-synchronous-design.md); synthesis runs [logic minimization](../02-combinational-logic/logic-minimization.md).
- **Above:** The netlist is implemented on a [Field-Programmable Gate Array (FPGA) or Application-Specific Integrated Circuit (ASIC)](fpga-and-asic.md) and checked by [timing and power](timing-and-power.md) analysis. Processors, from their [datapath and control](../../04-computer-architecture/02-processor-microarchitecture/datapath-and-control.md) to [domain-specific accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md), are written in HDLs. As languages, HDLs have a [syntax and semantics](../../06-programming-languages/02-semantics-and-types/syntax-and-semantics.md) like any other, and synthesis is a compiler problem ([intermediate representations](../../06-programming-languages/03-compilers/intermediate-representations.md)), and HDL verification draws on [model checking](../../06-programming-languages/05-formal-methods/model-checking.md) and [testing](../../12-software-engineering/03-quality/testing.md).
- **Siblings:** HDLs are the front end of the design flow; [FPGA and ASIC](fpga-and-asic.md) are the two back ends; [timing and power](timing-and-power.md) is the analysis that decides whether the result meets its targets.

## Common misconceptions

- **"Verilog is like C."** The syntax is similar, but the meaning is concurrent hardware; sequential intuition gives wrong circuits.
- **"If it simulates correctly, the chip will work."** Simulation may use non-synthesisable constructs or rely on scheduling order; equivalence checking and timing analysis are also needed.
- **"High-level synthesis makes hardware design like software."** It raises productivity for some kernels, but good results still require thinking about parallelism, memory structure and timing.

## Go deeper

- David Harris and Sarah Harris, *Digital Design and Computer Architecture* (2007): HDL coding side by side with the hardware it produces.
- Donald Thomas and Philip Moorby, *The Verilog Hardware Description Language* (1991): the language from one of its creators.
- Jonathan Bachrach et al., "Chisel: Constructing Hardware in a Scala Embedded Language" (2012): hardware generators as a higher abstraction.
