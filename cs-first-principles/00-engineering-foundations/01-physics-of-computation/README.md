# Physics of Computation

> **Layer:** [00 Engineering Foundations](../README.md) › Physics of Computation
> **Children:** [Electromagnetism and Charge](electromagnetism-and-charge.md) · [Quantum Mechanics and Band Theory](quantum-mechanics-and-band-theory.md) · [Thermodynamics and Energy](thermodynamics-and-energy.md)

## What this area is about

A computer is a physical system, and everything it does is something physics allows. This area answers the question: *what physical facts must be true for a machine to store and transform information, and what limits do those facts impose?* Three bodies of physics carry the load. Electromagnetism says how charges push one another, how fields control conduction and how signals travel. Quantum mechanics, through band theory, says why some materials have controllable numbers of mobile charges, which is the precondition for a transistor. Thermodynamics says what computation costs in energy and heat, and where the unavoidable floors lie.

The unifying idea is that **information is a physical state, and computation is controlled change of state that costs energy and time**. A bit is charge on a capacitor or the orientation of a magnet. Changing it means moving charge through resistance (time), dissipating energy (heat), and fighting thermal noise (reliability). Every limit you meet higher in the stack, such as clock speed, power walls, memory density and network latency, traces back to one of these three leaves.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Electromagnetism and Charge](electromagnetism-and-charge.md) | How charge, voltage, fields, capacitance and wave propagation work; the field effect | Calculus only |
| [Quantum Mechanics and Band Theory](quantum-mechanics-and-band-theory.md) | Why semiconductors exist, why their conductivity is controllable, and where tunnelling limits lie | Electromagnetism |
| [Thermodynamics and Energy](thermodynamics-and-energy.md) | What switching costs (`CV²`), why `kT` sets noise and turn-off, and the Landauer bound | Electromagnetism, with statistical ideas shared with band theory |

Read electromagnetism first: it supplies the vocabulary (charge, voltage, capacitance) that the other two use. Band theory then explains which materials let us exploit those forces with control. Thermodynamics closes the loop by pricing every operation and by explaining why carrier populations, leakage and noise all depend exponentially on temperature.

```
   electromagnetism ──► how charges move, how fields control them, how fast signals go
          │
          ├──► band theory ──► which materials have controllable mobile charge
          │
          └──► thermodynamics ──► what each move costs; noise; the kT ln 2 floor
```

## Connections to sibling areas

- **[Electrical Circuits](../02-electrical-circuits/README.md):** Circuits are the lumped approximation of electromagnetism. Kirchhoff's laws restate charge and energy conservation; resistance-capacitance (RC) delay is capacitance from this area in action; thermal noise comes from thermodynamics.
- **[Semiconductor Devices](../03-semiconductor-devices/README.md):** Devices are band theory and the field effect engineered into structures. Doping, junctions and the Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET) are direct applications, and the 60 mV per decade turn-off limit is thermodynamics.
- **[Signals and Systems](../04-signals-and-systems/README.md):** The analog-versus-digital bargain is a response to noise, whose fundamental part is thermal. Sampling theory describes the electromagnetic signals sensors capture.
- **[Engineering Method](../05-engineering-method/README.md):** Physical laws are the hardest constraints in any tradeoff. Heat removal and the speed of light are the archetypal non-negotiable limits.

## Connections across layers

Upward, the physics here explains the shape of the whole machine. The energy cost of switching drives [timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md) in digital design and [power and the end of scaling](../../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md) in architecture. Charge storage and magnetisation become Dynamic Random-Access Memory (DRAM) and other [storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md). Signal propagation speed bounds [latency in networks](../../08-networking/01-principles/latency-bandwidth-and-queueing.md). Landauer's principle ties thermodynamic entropy to [Shannon's entropy](../../02-theory-of-computation/01-information-theory/entropy-and-information.md), and the quantum mechanics that explains bands also underlies [qubits and quantum circuits](../../02-theory-of-computation/05-quantum-computation/qubits-and-quantum-circuits.md).

Downward there is nothing in this knowledge base: this is the floor. Its mathematical language, though, comes from the parallel formal root, [01 Mathematical Foundations](../../01-mathematical-foundations/README.md): calculus for fields, linear algebra for quantum states, probability for statistical physics.

## Cross-cutting threads

- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): the speed of light, heat removal and the Landauer bound are limits no design escapes.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): a bit must be encoded as a physical state; the choice (charge, magnetisation) decides speed, density and volatility.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): speed against energy is fixed at this level by `CV²` and `RC`.
- [State and time](../../CROSS-CUTTING.md#state-and-time): signals take finite time to propagate, so "simultaneous" is already approximate inside one chip.
