# Electromagnetism and Charge

> **Layer:** [00 Engineering Foundations](../README.md) › [Physics of Computation](README.md)
> **Builds on:** [Calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md)
> **Enables:** [Circuit Laws](../02-electrical-circuits/circuit-laws.md), [Capacitance and Timing](../02-electrical-circuits/capacitance-and-timing.md), [The MOSFET](../03-semiconductor-devices/the-mosfet.md), [DRAM and Storage Devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md)

## Essence

Every bit in a conventional computer is a physical arrangement of electric charge or magnetic orientation, and every operation moves charge from one place to another. Electromagnetism is the theory of how charges create fields, how fields push charges, and how changing fields propagate as waves. Three consequences matter most for computing: voltage (energy per unit charge) can control whether a material conducts, which is how transistors switch; storing charge on a capacitor is how bits are held; and signals travel as electromagnetic waves at a fraction of the speed of light, which puts a hard floor under latency. Everything from circuit laws to memory technology is a consequence of these facts.

## Core tenets

1. **Charge is conserved, and current is the rate at which charge moves.** Charge cannot be created or destroyed, only moved, so whatever flows into a node must flow out or accumulate there. This is the physical root of Kirchhoff's current law and of the fact that changing a stored bit always means moving charge through some resistance, which costs time and energy.

2. **Voltage is energy per unit charge, and it is what a transistor senses.** Moving charge `q` across a potential difference `V` takes or releases energy `qV`. Logic levels are defined as voltages, not currents, because a field-effect transistor's gate responds to the electric field across an insulator, which is set by voltage. A voltage can be held with almost no current, so a stored logic level costs little to maintain.

3. **A field can control conduction without any current flowing into the controlling terminal.** An electric field applied across a thin insulator attracts or repels mobile charge in the material beneath it. This field effect lets one wire change the conductivity of another while drawing no steady current. It is the principle behind the Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET), and it is why one logic gate can drive many others.

4. **Capacitance stores charge in proportion to voltage: `Q = CV`.** Any two conductors separated by an insulator form a capacitor. Holding a bit means holding charge on such a capacitor; the energy stored is `CV²/2`. Every wire and transistor gate has capacitance, so every logic transition must fill or drain charge, which is the origin of both delay and dynamic power.

5. **Signals travel as electromagnetic waves, not as electrons racing down a wire.** Electrons in a copper wire drift at millimetres per second, yet a signal arrives at a large fraction of the speed of light. The wave travels in the field around the conductor at `c / sqrt(εr)`: roughly 30 cm/ns in vacuum and about 15 cm/ns on a common printed circuit board (relative permittivity near 4). At 3 GHz a clock cycle lasts 0.33 ns, during which light in vacuum covers only 10 cm. Physical size therefore bounds latency in chips, boards and data centres alike.

6. **Changing currents create magnetic fields, and changing magnetic fields induce voltages.** Faraday's law means a wire carrying a rapidly changing current induces voltages in its neighbours (crosstalk) and in itself (inductance, `V = L di/dt`). When many outputs switch at once, the sudden current through the package's inductance makes the local ground "bounce". Fast edges also radiate, which is why high-speed design is partly an exercise in controlling fields.

7. **Resistance comes from charge carriers scattering, and it grows as wires shrink.** In a conductor, carriers collide with lattice vibrations and impurities, giving resistance `R = ρL/A`. Shrinking a wire's cross-section raises its resistance per unit length, while capacitance per unit length stays roughly constant. This is why on-chip wires, not transistors, now dominate delay in many designs.

8. **Magnetisation gives a second, non-volatile way to store bits.** Magnetic domains point one way or another and stay put because flipping them requires crossing an energy barrier. Hard disks, tape and Magnetoresistive Random-Access Memory (MRAM) store bits this way, reading them through the field or through resistance changes such as giant magnetoresistance.

## Key concepts

| Term | Meaning |
|---|---|
| Charge | Conserved quantity carried by electrons and holes; measured in coulombs. |
| Current | Rate of charge flow, `I = dQ/dt`; measured in amperes. |
| Voltage (potential difference) | Energy per unit charge between two points; measured in volts. |
| Electric field | Force per unit charge at a point; points from high to low potential. |
| Capacitance | Charge stored per volt, `C = Q/V`; set by geometry and the insulator. |
| Inductance | Voltage induced per rate of change of current, `V = L di/dt`. |
| Resistivity | Material property `ρ` giving resistance `R = ρL/A`. |
| Permittivity | How strongly an insulator responds to a field; sets capacitance and wave speed. |
| Propagation delay (physical) | Time for a field disturbance to travel a distance, bounded by the speed of light. |

## How it fits

- **Below:** This is the floor of the stack. It assumes only classical field theory and the calculus needed to state it (Maxwell's equations are differential equations).
- **Above:** [Circuit laws](../02-electrical-circuits/circuit-laws.md) are the low-frequency simplification of these equations. [Capacitance and timing](../02-electrical-circuits/capacitance-and-timing.md) turns `Q = CV` into gate delay. The field effect becomes [the MOSFET](../03-semiconductor-devices/the-mosfet.md). Charge storage becomes Dynamic Random-Access Memory (DRAM) cells and flash, and magnetisation becomes disks ([DRAM and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md)). The speed of light reappears as a fixed cost in [networking latency](../../08-networking/01-principles/latency-bandwidth-and-queueing.md).
- **Siblings:** [Quantum mechanics and band theory](quantum-mechanics-and-band-theory.md) explains *which* materials have mobile charges to push around; [thermodynamics and energy](thermodynamics-and-energy.md) explains where the energy goes when they move.

## Common misconceptions

- **"Electricity is electrons flowing at nearly light speed."** The signal is a field wave that travels quickly; individual electrons drift very slowly.
- **"A logic gate's input consumes current while it holds a value."** A MOSFET gate is a capacitor; it draws current only while its voltage changes (plus tiny leakage).
- **"Wires are ideal connections."** Every wire has resistance, capacitance and inductance, and at modern speeds these often matter more than the transistors.

## Go deeper

- Richard Feynman, Robert Leighton and Matthew Sands, *The Feynman Lectures on Physics, Vol. II* (1964): field-based intuition for electromagnetism.
- Edward Purcell and David Morin, *Electricity and Magnetism* (3rd ed., 2013): rigorous but readable treatment of fields and capacitance.
- David Griffiths, *Introduction to Electrodynamics* (1981): the standard undergraduate text on Maxwell's equations.
