# Logic Gates

> **Layer:** [03 Digital Logic](../README.md) › [Combinational Logic](README.md)
> **Builds on:** [Boolean Algebra](../../01-mathematical-foundations/04-algebra/boolean-algebra.md), [CMOS](../../00-engineering-foundations/03-semiconductor-devices/cmos.md), [Analog vs Digital](../../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md)
> **Enables:** [Logic Minimization](logic-minimization.md), [Arithmetic and Building Blocks](arithmetic-and-building-blocks.md), [Latches and Flip-Flops](../03-sequential-logic/latches-and-flip-flops.md)

## Essence

A logic gate is a physical circuit that computes a Boolean function of its inputs and drives its output to a clean, restored logic level after a short delay. Gates are where the two roots of computer science meet: Boolean algebra supplies the functions, and Complementary Metal-Oxide-Semiconductor (CMOS) transistors supply circuits that implement them. Claude Shannon showed in 1937 that switching circuits obey Boolean algebra, which meant circuit design could be done with algebra instead of trial and error. A small set of gate types is functionally complete, so any Boolean function, and therefore any finite computation step, can be built by wiring gates together. A combinational circuit is just such a network without feedback: its outputs depend only on its current inputs.

## Core tenets

1. **A gate is a Boolean function plus a timing and electrical contract.** Logically, a two-input NAND is the function `¬(a ∧ b)`. Physically, it promises valid output levels whenever its inputs are valid (the static discipline), after a propagation delay `tpd` at most, and it starts changing no sooner than a contamination delay `tcd`. Logic design uses the Boolean view; timing analysis uses the delays; both are needed.

2. **Shannon's insight: switches in series and parallel compute AND and OR.** In his 1937 master's thesis (published 1938), Shannon mapped relay contacts in series to conjunction and in parallel to disjunction, so simplifying an algebraic expression simplifies the circuit. CMOS realises the same mapping with transistors, which is why logic design is algebra.

3. **NAND alone (or NOR alone) can build anything.** Every Boolean function can be written using AND, OR and NOT (for example as a sum of products). NAND can make NOT (`NAND(a, a)`), AND (NAND then NOT) and OR (by De Morgan, `NAND(¬a, ¬b)`). A set of gates with this property is functionally complete. Practically, chips are built from a library of a few hundred standard cells, but completeness means correctness never depends on having any particular gate.

4. **CMOS makes inverting gates cheapest.** A single CMOS stage can only compute functions that are monotone decreasing in its inputs, such as NOT, NAND, NOR and and-or-invert. Non-inverting gates such as AND and OR are built as an inverting gate plus an inverter, costing an extra stage of delay. Good logic design pushes inversions around (using De Morgan's laws) to match the technology.

5. **Fan-in and fan-out have physical limits.** A gate with many inputs needs long series transistor stacks, which are slow, so gates rarely exceed about four inputs; wider functions use trees of gates, costing logarithmic depth. A gate driving many others sees large load capacitance, so its delay grows with fan-out unless it is upsized or buffered.

6. **Combinational circuits are acyclic, and their delay is the longest path.** With no feedback loops, the output is a pure function of present inputs once signals settle. Delay through a network is set by the slowest input-to-output path. Depth (the number of gate levels) is thus a direct measure of speed, which is why parallel algorithms for addition and comparison matter in hardware.

7. **Outputs can glitch before they settle.** When inputs change, different paths have different delays, so an output can briefly take a wrong value (a hazard) before reaching the correct one. Synchronous design makes glitches harmless by sampling outputs only after everything has settled. Glitches still waste power and matter wherever a signal is used asynchronously, such as clocks and resets.

8. **Some outputs are not simply 0 or 1.** Tri-state outputs can disconnect (high impedance) so several drivers can share a bus wire, provided only one drives at a time. Open-drain outputs only pull down, letting many devices share a line with a pull-up resistor (wired-AND). These are electrical conventions that extend the pure Boolean model.

## Key concepts

| Term | Meaning |
|---|---|
| Truth table | Complete listing of a function's output for every input combination. |
| NAND / NOR | AND / OR followed by NOT; each functionally complete alone. |
| XOR | Exclusive OR; output 1 when inputs differ; the core of addition. |
| Functional completeness | Ability of a gate set to express every Boolean function. |
| Propagation delay (`tpd`) | Maximum time from input change to settled output. |
| Contamination delay (`tcd`) | Minimum time from input change to any output change. |
| Fan-in / fan-out | Number of inputs to a gate / number of gate inputs it drives. |
| Hazard (glitch) | A transient wrong output during settling. |
| Combinational circuit | Gate network without feedback; outputs depend only on current inputs. |

## How it fits

- **Below:** The functions come from [Boolean algebra](../../01-mathematical-foundations/04-algebra/boolean-algebra.md) and [propositional logic](../../01-mathematical-foundations/01-logic/propositional-logic.md); the circuits are [CMOS](../../00-engineering-foundations/03-semiconductor-devices/cmos.md) gates; restoration and the static discipline come from [analog vs digital](../../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md); delays come from [capacitance and timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md).
- **Above:** Gates are simplified by [logic minimization](logic-minimization.md), assembled into [arithmetic and building blocks](arithmetic-and-building-blocks.md), and, with feedback added, form [latches and flip-flops](../03-sequential-logic/latches-and-flip-flops.md). Ultimately they make up the [datapath and control](../../04-computer-architecture/02-processor-microarchitecture/datapath-and-control.md) of processors. Circuit size and depth are also models in [complexity classes](../../02-theory-of-computation/04-complexity/complexity-classes.md) (circuit complexity).
- **Siblings:** [Logic minimization](logic-minimization.md) chooses *which* gates to use; [arithmetic and building blocks](arithmetic-and-building-blocks.md) shows the standard structures gates are combined into.

## Common misconceptions

- **"AND, OR and NOT are the hardware primitives."** In CMOS the cheap primitives are inverting (NAND, NOR, NOT); AND and OR cost more.
- **"A combinational output is correct as soon as an input changes."** It is correct only after the propagation delay, and may glitch on the way.
- **"Any gate can drive any number of others."** Fan-out increases delay roughly linearly; large fan-outs need buffer trees.

## Go deeper

- Claude Shannon, "A Symbolic Analysis of Relay and Switching Circuits" (1938): the founding link between Boolean algebra and circuits.
- David Harris and Sarah Harris, *Digital Design and Computer Architecture* (2007): clear modern treatment of gates, timing and the static discipline.
- Noam Nisan and Shimon Schocken, *The Elements of Computing Systems* (2005): build a whole computer starting from NAND.
