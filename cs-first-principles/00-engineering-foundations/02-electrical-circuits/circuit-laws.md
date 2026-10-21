# Circuit Laws

> **Layer:** [00 Engineering Foundations](../README.md) › [Electrical Circuits](README.md)
> **Builds on:** [Electromagnetism and Charge](../01-physics-of-computation/electromagnetism-and-charge.md), [Linear Algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md)
> **Enables:** [Capacitance and Timing](capacitance-and-timing.md), [CMOS](../03-semiconductor-devices/cmos.md), [Logic Gates](../../03-digital-logic/02-combinational-logic/logic-gates.md)

## Essence

Circuit theory is the first great abstraction in the stack. Instead of solving Maxwell's equations for every wire, you model a circuit as a graph of ideal elements (resistors, capacitors, sources, switches) joined at nodes, with each element described only by the relation between the voltage across it and the current through it. Two conservation laws, Kirchhoff's current and voltage laws, then determine everything. This "lumped" model is valid when the circuit is small compared with the wavelength of the signals in it, and inside that boundary it lets engineers reason about billions of devices with algebra rather than field theory.

## Core tenets

1. **The lumped abstraction replaces fields with a few numbers per element.** If the circuit is much smaller than the signal wavelength and no element's changing field couples to another, each element can be treated as a black box with two terminals, a voltage across and a current through. Agarwal and Lang call these constraints the "lumped matter discipline". The model breaks down for long wires at high frequency, where you must treat them as transmission lines.

2. **Kirchhoff's current law (KCL) is conservation of charge at a node.** The currents into any node sum to zero, because a node (an ideal wire junction) cannot store charge. Where charge does accumulate, the model puts an explicit capacitor. KCL gives one linear equation per node.

3. **Kirchhoff's voltage law (KVL) is conservation of energy around a loop.** The voltage drops around any closed loop sum to zero, because in the lumped regime the electric field is conservative: moving a charge around a loop and back to its start gains no net energy. KVL makes voltage a property of nodes (a potential) rather than of paths.

4. **Ohm's law and similar element laws close the system.** A resistor obeys `V = IR`; a capacitor `I = C dV/dt`; an inductor `V = L dI/dt`. With KCL, KVL and one element law per component, a circuit with `n` nodes yields a system of equations that nodal analysis solves directly. For resistive circuits this is a linear system, solvable with the tools of linear algebra; circuit simulators do exactly this.

5. **Power is `P = VI`, and resistors turn it into heat.** Any element with voltage across it and current through it absorbs `VI` watts. For a resistor this is `I²R = V²/R`, all dissipated as heat. This is why a conducting path from supply to ground is costly and why logic families that avoid such paths in steady state, such as Complementary Metal-Oxide-Semiconductor (CMOS), won.

6. **Linear circuits obey superposition, and any linear two-terminal network is equivalent to a source plus a resistor.** In a circuit of linear elements, the response to several sources is the sum of the responses to each alone. Thévenin's theorem says any such network, viewed from two terminals, behaves like one voltage source in series with one resistance. This is an early, exact instance of hiding implementation behind an interface: the driver of a logic gate can be summarised by its output resistance.

7. **Voltage dividers explain logic levels and loading.** Two resistors in series split a voltage in proportion to their resistances: `Vout = Vin · R2/(R1+R2)`. A transistor that is "on" acts like a small resistor and one that is "off" like a huge one, so a gate's output level is set by a divider between pull-up and pull-down paths. If both paths conduct, the output lands somewhere in the middle, which is an invalid logic level and wastes power.

8. **Nonlinear elements break superposition, so we linearise or switch.** Diodes and transistors have exponential or quadratic voltage-current relations. Analog designers linearise them around an operating point to get small-signal models. Digital designers instead treat transistors as switches that are either fully on or fully off, which restores simple reasoning at the cost of ignoring the transition.

## Key concepts

| Term | Meaning |
|---|---|
| Node | A point where elements connect; has one voltage. |
| Branch | An element between two nodes; has one current. |
| Kirchhoff's Current Law (KCL) | Currents into a node sum to zero. |
| Kirchhoff's Voltage Law (KVL) | Voltages around a loop sum to zero. |
| Ohm's law | `V = IR` for a resistor. |
| Thévenin equivalent | A voltage source plus series resistance that mimics any linear network at two terminals. |
| Superposition | In linear circuits, total response equals the sum of responses to each source. |
| Lumped matter discipline | Conditions under which elements can be treated as ideal points. |
| Ground | A reference node defined to be 0 V. |

## How it fits

- **Below:** KCL and KVL are the low-frequency, small-size limit of [electromagnetism](../01-physics-of-computation/electromagnetism-and-charge.md). Solving circuits is applied [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md).
- **Above:** The switch-and-resistor view of transistors becomes the [CMOS](../03-semiconductor-devices/cmos.md) gate, and the voltage divider explains why only one of its networks may conduct. [Logic gates](../../03-digital-logic/02-combinational-logic/logic-gates.md) are circuits viewed through one more abstraction, the digital one ([analog vs digital](../04-signals-and-systems/analog-vs-digital.md)).
- **Siblings:** [Capacitance and timing](capacitance-and-timing.md) adds the time dimension that resistors alone lack. [Noise and signal integrity](noise-and-signal-integrity.md) covers what happens when the lumped model's assumptions fail.

## Common misconceptions

- **"Kirchhoff's laws are always exactly true."** They hold only within the lumped approximation; with fast edges on long wires, voltage differs along a "single" wire.
- **"Current is used up by a resistor."** Current in equals current out; energy, not charge, is what is dissipated.
- **"Ground is the same everywhere."** Ground is a reference node; real ground wires have resistance and inductance, so their voltage varies with current.

## Go deeper

- Anant Agarwal and Jeffrey Lang, *Foundations of Analog and Digital Electronic Circuits* (2005): builds circuits explicitly as a chain of abstractions up to digital logic.
- Paul Horowitz and Winfield Hill, *The Art of Electronics* (1980; 3rd ed., 2015): practical intuition for real circuits.
