# Clocking and Synchronous Design

> **Layer:** [03 Digital Logic](../README.md) › [Sequential Logic](README.md)
> **Builds on:** [Latches and Flip-Flops](latches-and-flip-flops.md), [Capacitance and Timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md), [Feedback and Control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md)
> **Enables:** [Finite State Machines](finite-state-machines.md), [Timing and Power](../04-hardware-design/timing-and-power.md), [Pipelining](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md), [The Performance Equation](../../04-computer-architecture/06-performance/the-performance-equation.md)

## Essence

Synchronous design is the discipline that makes complex digital systems possible. All state lives in flip-flops driven by one shared clock; between flip-flops sits only combinational logic. On each clock edge every flip-flop samples its input at once, and the logic then has one clock period to compute the next values. This divides time into discrete steps, so the designer can reason about the circuit as a sequence of states, like a program, and ignore glitches, races and the details of when each signal settles. Correctness then reduces to two inequalities per path, one on the slowest path (setup) and one on the fastest (hold), which tools can check exhaustively. The cost is that the whole circuit runs at the pace of its slowest path, and the clock itself must be delivered to billions of points nearly simultaneously.

## Core tenets

1. **The synchronous discipline separates function from timing.** If every cycle-crossing path starts and ends at a clocked flip-flop, and every combinational path settles within the clock period, then the circuit behaves exactly like an ideal state machine that steps once per edge. Logical correctness can be verified by simulation of cycles; timing correctness can be verified separately by analysis of delays. This separation is why synchronous design dominates.

2. **The setup constraint bounds the clock period by the slowest path.** Data launched at one edge must arrive before the next edge minus setup time: `Tclk ≥ tclk→Q + tpd(logic) + tsetup + tskew`. The longest such path is the critical path, and it sets the maximum frequency. Violations are fixed by slowing the clock, speeding the logic, or cutting the path with another register.

3. **The hold constraint bounds the fastest path, and the clock cannot fix it.** Data launched at an edge must not reach the next flip-flop so fast that it corrupts the value being captured at the same edge: `tclk→Q + tcd(logic) ≥ thold + tskew`. Because both sides refer to the *same* edge, slowing the clock does not help. Hold violations are fixed by adding delay to short paths, and a chip with one is broken at any frequency.

4. **Registers cut paths, trading latency for throughput.** Inserting a register in the middle of a long combinational path splits it into two shorter ones, so the clock can run faster. Each item now takes more cycles to traverse the circuit (higher latency) but a new item can enter every cycle (higher throughput). This is pipelining at the circuit level, and the register overhead (`tclk→Q + tsetup`) per stage limits how deep it can usefully go.

5. **Delivering the clock is a hard engineering problem.** The clock net drives every flip-flop on the chip, often the largest load and a large share of dynamic power. Differences in arrival time between flip-flops (skew) and variation of edges from cycle to cycle (jitter) eat into the timing budget. Designers use balanced trees, meshes and buffers to distribute it, Phase-Locked Loops (PLLs) to multiply a crystal reference to gigahertz frequencies, and clock gating to stop the clock to idle blocks and save power.

6. **Multiple clock domains need explicit crossings.** Large chips run blocks at different frequencies or from independent clocks. A signal crossing between domains is asynchronous to its receiver, so it must pass through a synchroniser, and multi-bit values must cross via handshakes or asynchronous First-In, First-Out (FIFO) buffers using Gray-coded pointers so that only one bit changes at a time. Clock domain crossing bugs are a classic source of rare, unreproducible failures.

7. **Asynchronous design is possible but rarely worth it.** Circuits can instead coordinate with local handshakes and no global clock (Ivan Sutherland's micropipelines, 1989), which avoids skew and runs each part at its natural speed. They are much harder to design, verify and test with standard tools, so they are used selectively, for example at interfaces and in some low-power designs.

## Key concepts

| Term | Meaning |
|---|---|
| Synchronous circuit | Circuit whose state changes only at edges of a shared clock. |
| Clock period (`Tclk`) | Time between successive active clock edges; inverse of frequency. |
| Critical path | The longest register-to-register combinational path. |
| Setup constraint | Max-delay requirement that data arrive before the next edge. |
| Hold constraint | Min-delay requirement that data not arrive too soon after the same edge. |
| Clock skew | Difference in clock arrival times at different flip-flops. |
| Jitter | Variation in clock edge timing from cycle to cycle. |
| Clock gating | Disabling the clock to idle logic to save dynamic power. |
| Clock Domain Crossing (CDC) | A signal passing between unrelated clocks, requiring synchronisation. |

## How it fits

- **Below:** It rests on the setup, hold and clock-to-Q parameters of [latches and flip-flops](latches-and-flip-flops.md) and on gate and wire delays from [capacitance and timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md). Clocks are generated by oscillators and PLLs ([feedback and control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md)).
- **Above:** The clock is the "tick" of [finite state machines](finite-state-machines.md). Setup and hold become the inputs to static analysis in [timing and power](../04-hardware-design/timing-and-power.md). Register insertion becomes processor [pipelining](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md), and clock period is one factor of [the performance equation](../../04-computer-architecture/06-performance/the-performance-equation.md). Lockstep rounds are also the model of synchronous systems in [system models and failures](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md), where no global clock exists and the problem becomes much harder.
- **Siblings:** [Latches and flip-flops](latches-and-flip-flops.md) supply the parts; [finite state machines](finite-state-machines.md) supply the meaning of each cycle's state.

## Common misconceptions

- **"A faster clock always fixes timing problems."** It never fixes hold violations, and makes setup violations worse; slowing the clock fixes only setup.
- **"The clock edge arrives everywhere at once."** Skew and jitter are real and must be budgeted.
- **"Higher clock frequency means a faster processor."** It often comes from deeper pipelines with more cycles per instruction; performance depends on both.

## Go deeper

- David Harris and Sarah Harris, *Digital Design and Computer Architecture* (2007): timing of sequential logic and the synchronous discipline.
- Neil Weste and David Harris, *CMOS VLSI Design* (4th ed., 2010): clock distribution and sequencing in real chips.
- Ivan Sutherland, "Micropipelines" (1989): the Turing Award lecture making the case for clockless design.
