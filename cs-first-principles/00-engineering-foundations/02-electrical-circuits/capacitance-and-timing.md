# Capacitance and Timing

> **Layer:** [00 Engineering Foundations](../README.md) › [Electrical Circuits](README.md)
> **Builds on:** [Circuit Laws](circuit-laws.md), [Electromagnetism and Charge](../01-physics-of-computation/electromagnetism-and-charge.md), [Calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md)
> **Enables:** [Clocking and Synchronous Design](../../03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md), [Timing and Power](../../03-digital-logic/04-hardware-design/timing-and-power.md), [Pipelining](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md)

## Essence

A digital signal cannot change instantly, because every wire and every transistor gate is a capacitor that must be filled or drained through some resistance. The product of that resistance and capacitance, the resistance-capacitance (RC) time constant, sets how fast a node can move from one logic level to another. Gate delays, wire delays, maximum clock frequency and dynamic energy all follow from this one mechanism. Understanding it explains why gates have limited fan-out, why long wires need repeaters, and why on-chip communication is often slower than computation.

## Core tenets

1. **Every node has capacitance, and changing its voltage takes charge.** Transistor gates, wire-to-wire spacing and transistor junctions all contribute capacitance. To move a node by `ΔV` you must deliver charge `CΔV` through whatever drives it. Since current is limited by resistance, this takes time.

2. **An RC circuit responds exponentially with time constant `τ = RC`.** Charging a capacitor through a resistor gives `V(t) = V_final (1 - e^{-t/RC})`. The node reaches 50% of its final value after about `0.69 RC` and 90% after about `2.3 RC`. Digital circuits care about the 50% point because that is where the next gate's switching threshold roughly sits.

3. **Gate delay is the driver's resistance times the load it sees.** A transistor that is on acts like a resistor whose value shrinks as the transistor gets wider. The load is the input capacitance of every gate it drives plus the wire. Driving more gates (higher fan-out) means more load and proportionally more delay; making the driver wider helps but raises the load on whatever drives *it*. The method of logical effort turns this into a design rule for sizing chains of gates.

4. **A wire is a distributed RC line, and its delay grows with the square of its length.** Both a wire's resistance and its capacitance grow linearly with length, so their product grows quadratically. Elmore's approximation gives roughly `0.5 rc L²` for a line of length `L` with resistance `r` and capacitance `c` per unit length. Long wires are therefore broken by repeaters (buffers) into segments, making delay linear in length again at the cost of area and power.

5. **Shrinking transistors speeds them up, but shrinking wires slows them down.** Scaling a transistor reduces its capacitance and roughly keeps its resistance, so its delay falls. Scaling a wire's cross-section raises its resistance per unit length while capacitance per unit length stays about the same, so a wire spanning a fixed fraction of the chip gets slower each generation. This is why modern designs treat communication distance as a first-class cost and why chips are divided into regions that talk sparingly.

6. **The slowest path through combinational logic sets the clock period.** A synchronous circuit must let signals settle through the longest chain of gates and wires (the critical path) before the next clock edge. Delay is the sum of the RC delays along that path. Making the clock faster requires either shortening the path (fewer gates, faster gates) or cutting it with registers, which is pipelining.

7. **Every transition costs energy `CV²`, so capacitance is also a power budget.** Charging and discharging a node once draws `CV²` from the supply. Less capacitance means both faster and cheaper switching, which is a large part of why smaller transistors were such a gift. Inductance, ignored here, matters too once current changes very fast: `L di/dt` noise on supply lines is the main reason chips need many power and ground pins.

## Key concepts

| Term | Meaning |
|---|---|
| Time constant (`τ`) | `RC`; time for an RC circuit to cover 63% of a step. |
| Propagation delay | Time from an input crossing 50% to the output crossing 50%. |
| Rise/fall time | Time for a signal to move between 10% and 90% of its swing. |
| Load capacitance | Total capacitance a gate output must charge: fan-out gates plus wire. |
| Fan-out | Number of gate inputs driven by one output. |
| Elmore delay | First-order estimate of delay in an RC tree, summing resistance times downstream capacitance. |
| Repeater | A buffer inserted in a long wire to make its delay linear in length. |
| Critical path | The slowest combinational path between registers; sets clock period. |
| Logical effort | A method that estimates and minimises delay through chains of gates. |

## How it fits

- **Below:** It applies [circuit laws](circuit-laws.md) to capacitors, which store charge as described in [electromagnetism and charge](../01-physics-of-computation/electromagnetism-and-charge.md). The exponential response is a first-order differential equation from [calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md).
- **Above:** RC delay becomes the propagation delay of [logic gates](../../03-digital-logic/02-combinational-logic/logic-gates.md), the timing constraints of [clocking and synchronous design](../../03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md), and the analysis in [timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md). Critical paths motivate [pipelining](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md), and wire delay shapes [cache design](../../04-computer-architecture/03-memory-hierarchy/cache-design.md): a bigger cache is a slower cache partly because its wires are longer.
- **Siblings:** [Circuit laws](circuit-laws.md) give the static picture; this leaf gives the dynamic one. [Noise and signal integrity](noise-and-signal-integrity.md) covers what disturbs these transitions.

## Common misconceptions

- **"Gate delay is a fixed property of the gate."** It depends strongly on the load the gate drives and on the slope of its input.
- **"Wires are free."** In modern processes a cross-chip wire can take several clock cycles; wire delay and wire energy often exceed those of logic.
- **"Smaller is always faster."** Smaller transistors are faster; smaller wires are slower.

## Go deeper

- Neil Weste and David Harris, *CMOS VLSI Design: A Circuits and Systems Perspective* (4th ed., 2010): delay models, wires and sizing in depth.
- Ivan Sutherland, Bob Sproull and David Harris, *Logical Effort: Designing Fast CMOS Circuits* (1999): the clearest method for reasoning about gate delay.
- Jan Rabaey, Anantha Chandrakasan and Borivoje Nikolić, *Digital Integrated Circuits: A Design Perspective* (2nd ed., 2003): interconnect and timing from the circuit level.
