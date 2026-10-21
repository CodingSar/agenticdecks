# Latches and Flip-Flops

> **Layer:** [03 Digital Logic](../README.md) › [Sequential Logic](README.md)
> **Builds on:** [Logic Gates](../02-combinational-logic/logic-gates.md), [Feedback and Control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md), [CMOS](../../00-engineering-foundations/03-semiconductor-devices/cmos.md)
> **Enables:** [Clocking and Synchronous Design](clocking-and-synchronous-design.md), [Finite State Machines](finite-state-machines.md), [Cache Design](../../04-computer-architecture/03-memory-hierarchy/cache-design.md)

## Essence

Combinational logic forgets: its output depends only on its present input. To compute over time, hardware must remember, and memory comes from feedback. Two inverters connected in a loop have two stable states and hold either one indefinitely while powered. Add a way to force the loop into a chosen state and you have a latch; put two latches back to back with opposite enables and you have an edge-triggered flip-flop, which captures its input at the instant the clock rises and holds it for a whole cycle. Flip-flops are the state of every synchronous circuit, from a processor's registers to a controller's current state. Their one unavoidable flaw is metastability: an input that changes at exactly the wrong moment can leave the loop balanced between states for an unbounded time.

## Core tenets

1. **Memory is positive feedback.** Two cross-coupled inverters reinforce each other: if one output is high, it drives the other low, which keeps the first high. The loop has two stable states (storing 0 or 1) and one unstable balance point in between. Any small push away from balance grows until the loop reaches a rail. This bistability, not any special memory material, is how all static on-chip storage works.

2. **A latch is a bistable loop with a way to write it.** The Set-Reset (SR) latch, two cross-coupled NOR (or NAND) gates, is set or reset by pulsing one input. The D latch adds an enable: while enable is high the latch is *transparent* and its output follows input `D`; when enable falls it holds the last value. Transparency is the latch's defining property and its hazard: changes race straight through while it is open.

3. **A flip-flop samples on a clock edge by pairing two latches.** In a master-slave D flip-flop, the master latch is transparent while the clock is low and the slave while it is high. At the rising edge the master closes, capturing `D`, and the slave opens, passing that captured value to `Q`. The net effect is edge-triggered behaviour: `Q` takes the value `D` had just before the edge and holds it for a full cycle, no matter how `D` changes in between. Edge triggering is what lets the output of a flip-flop feed logic that feeds back into the same flip-flop without racing.

4. **Sampling requires the input to be stable around the edge.** A flip-flop specifies a setup time (`D` must be stable this long *before* the edge) and a hold time (and this long *after*), and a clock-to-Q delay before the new output appears. These three numbers are the interface between flip-flops and the timing analysis of the whole circuit.

5. **Violating setup or hold can cause metastability, and it cannot be eliminated.** If `D` changes inside the setup-hold window, the loop may be left near its balance point. It will fall to one side eventually, but the time required is unbounded: the probability that it is still unresolved after time `t` decays as `e^{-t/τ}`, where `τ` is a device time constant of order tens of picoseconds. Any device that must turn a continuous-time input into a discrete decision in bounded time has this problem (Chaney and Molnar demonstrated it experimentally in 1973).

6. **Synchronisers make metastability rare, not impossible.** Signals from another clock domain or from the outside world arrive at arbitrary times. A synchroniser passes them through two (or more) flip-flops in series, giving the first one nearly a whole cycle to resolve before the second samples it. Because resolution probability improves exponentially with waiting time, one extra cycle typically pushes the mean time between failures from seconds to centuries. Designers compute this figure explicitly for every asynchronous input.

7. **Registers, register files and static memory are organised latches.** A register is `n` flip-flops sharing a clock. A register file is an array of registers with read multiplexers and a write decoder. A Static Random-Access Memory (SRAM) cell is the minimal version: two cross-coupled inverters plus two access transistors, six transistors in all, read and written through shared bit lines. Dynamic Random-Access Memory (DRAM) instead stores charge on a capacitor, which leaks and must be refreshed; it is denser because it needs only one transistor and one capacitor per bit.

## Key concepts

| Term | Meaning |
|---|---|
| Bistable element | Circuit with two stable states, such as cross-coupled inverters. |
| SR latch | Latch with separate set and reset inputs. |
| D latch | Latch that is transparent while enabled and holds when disabled. |
| D flip-flop | Edge-triggered storage element that samples `D` at the clock edge. |
| Setup time / hold time | Required stability of input before / after the clock edge. |
| Clock-to-Q delay | Time from clock edge to valid output. |
| Metastability | Unresolved state near the balance point after a timing violation. |
| Synchroniser | Chain of flip-flops that reduces the chance of metastable failure. |
| Register file | Addressable array of registers with read and write ports. |

## How it fits

- **Below:** The bistable loop is positive [feedback](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md) built from [Complementary Metal-Oxide-Semiconductor (CMOS)](../../00-engineering-foundations/03-semiconductor-devices/cmos.md) inverters; latches are wired from [logic gates](../02-combinational-logic/logic-gates.md). Metastability is the cost at the boundary described in [analog vs digital](../../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md).
- **Above:** Flip-flops are the state elements of [clocking and synchronous design](clocking-and-synchronous-design.md) and [finite state machines](finite-state-machines.md). Pipeline registers implement [pipelining](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md); SRAM arrays form caches ([cache design](../../04-computer-architecture/03-memory-hierarchy/cache-design.md)); DRAM is covered in [DRAM and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md). Hardware arbitration between concurrent requests faces the same metastability problem that software faces as [race conditions](../../07-operating-systems/03-concurrency/race-conditions-and-critical-sections.md).
- **Siblings:** [Clocking and synchronous design](clocking-and-synchronous-design.md) builds a whole-circuit discipline on flip-flop timing; [finite state machines](finite-state-machines.md) give stored bits their meaning.

## Common misconceptions

- **"Latches and flip-flops are the same thing."** A latch is level-sensitive (transparent while enabled); a flip-flop is edge-triggered. Mixing them up causes races.
- **"Good design eliminates metastability."** It can only make failure arbitrarily unlikely by allowing more resolution time; no bounded-time circuit avoids it entirely.
- **"Memory needs special materials."** On-chip static memory is just logic gates in a feedback loop.

## Go deeper

- David Harris and Sarah Harris, *Digital Design and Computer Architecture* (2007): latches, flip-flops and timing.
- Thomas Chaney and Charles Molnar, "Anomalous Behavior of Synchronizer and Arbiter Circuits" (1973): the experimental demonstration of metastability.
- Ran Ginosar, "Metastability and Synchronizers: A Tutorial" (2011): practical analysis and synchroniser design.
