# Quantum Mechanics and Band Theory

> **Layer:** [00 Engineering Foundations](../README.md) › [Physics of Computation](README.md)
> **Builds on:** [Electromagnetism and Charge](electromagnetism-and-charge.md), [Linear Algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md)
> **Enables:** [Doping and the PN Junction](../03-semiconductor-devices/doping-and-the-pn-junction.md), [The MOSFET](../03-semiconductor-devices/the-mosfet.md), [Qubits and Quantum Circuits](../../02-theory-of-computation/05-quantum-computation/qubits-and-quantum-circuits.md)

## Essence

Classical physics cannot explain why copper conducts, glass insulates and silicon sits usefully in between. Quantum mechanics can: electrons in a solid may only occupy certain energy ranges called bands, and whether a material conducts depends on whether there are empty states close in energy to filled ones. In a semiconductor a modest energy gap separates a full band from an empty one, so its conductivity is tiny when pure but can be changed by many orders of magnitude by impurities, temperature, light or an applied field. That controllability is the whole reason transistors exist. Quantum effects also set limits: electrons tunnel through barriers that are thin enough, which caps how thin insulators can be.

## Core tenets

1. **Bound electrons have discrete energy levels, and no two can share a state.** Solving the Schrödinger equation for an electron near a nucleus gives only certain allowed energies. The Pauli exclusion principle allows at most one electron per quantum state (two per orbital, with opposite spin), so electrons fill levels from the bottom up. This filling order decides chemistry and, in solids, conduction.

2. **In a crystal, levels from many atoms merge into bands separated by gaps.** When about 10²² atoms per cubic centimetre sit in a regular lattice, their outer orbitals overlap and each atomic level splits into a near-continuum of states: a band. Between bands lie forbidden energy ranges, the band gaps. The highest mostly full band is the valence band; the next one up is the conduction band.

3. **Conduction needs empty states just above occupied ones.** To carry current, electrons must gain a little energy from an applied field, which means moving into nearby empty states. In a metal the highest occupied band is partly full, so this is easy. In an insulator the valence band is full and the gap is large (about 9 eV for silicon dioxide), so almost no electron can move. A semiconductor has the same structure as an insulator but a small gap: 1.12 eV for silicon at room temperature.

4. **Thermal energy excites carriers across the gap with exponential sensitivity.** The fraction of electrons kicked into the conduction band scales roughly as `exp(-Eg / 2kT)`, where `kT` is about 0.026 eV at 300 K. Pure silicon therefore has only about 10¹⁰ free electrons per cubic centimetre against roughly 5 × 10²² atoms. That is low enough that adding a few impurities dominates conduction, which is the basis of doping. The same exponential makes leakage in transistors climb steeply with temperature.

5. **A missing electron behaves like a positive carrier called a hole.** When an electron leaves the valence band, neighbouring electrons can shift into the vacancy, so the vacancy moves. It is simpler and accurate to model this as a positive particle with its own effective mass and mobility. Semiconductors thus have two carrier types, and devices are built by arranging regions where one or the other dominates. Holes in silicon are less mobile than electrons (roughly 2 to 3 times), which is why p-type transistors are drawn wider.

6. **Electrons tunnel through thin barriers with probability that falls exponentially with thickness.** A quantum particle's wavefunction does not stop at a barrier; it decays inside it. If the barrier is only a few nanometres thick, a measurable fraction of electrons appear on the other side. Gate oxides of silicon dioxide thinner than about 1.5 to 2 nm leak too much, which pushed the industry to high-permittivity ("high-k") gate dielectrics in the late 2000s. Flash memory exploits tunnelling deliberately to push charge onto and off an isolated gate.

7. **Devices are statistical ensembles, until they are not.** A transistor's current is the average behaviour of huge numbers of carriers, which is why it looks deterministic and classical. As devices shrink to a few nanometres, the count of dopant atoms in a channel can be tens, and random variation between "identical" transistors grows. Building computers out of individual quantum states instead, deliberately keeping their superposition, is the separate idea of quantum computation.

## Key concepts

| Term | Meaning |
|---|---|
| Energy band | Near-continuous range of allowed electron energies in a solid. |
| Band gap (`Eg`) | Forbidden energy range between valence and conduction bands. |
| Valence band | Highest band that is (nearly) full at absolute zero. |
| Conduction band | Lowest band that is (nearly) empty at absolute zero. |
| Fermi level | Energy at which a state has a 50% chance of being occupied; sets carrier populations. |
| Hole | The vacancy left by a missing valence electron, behaving as a positive carrier. |
| Intrinsic carrier concentration (`ni`) | Free carriers in pure semiconductor from thermal excitation alone. |
| Mobility | Carrier drift velocity per unit electric field; sets how fast devices switch. |
| Tunnelling | Quantum passage of a particle through a classically forbidden barrier. |

## How it fits

- **Below:** It refines [electromagnetism](electromagnetism-and-charge.md): the forces are still electrical, but electrons obey wave mechanics. Its mathematics is [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md) (states as vectors, observables as operators) and [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md).
- **Above:** Band structure explains [doping and the pn junction](../03-semiconductor-devices/doping-and-the-pn-junction.md) and hence [the Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET)](../03-semiconductor-devices/the-mosfet.md). Tunnelling limits [fabrication and scaling](../03-semiconductor-devices/fabrication-and-scaling.md) and enables flash [memory cells](../../03-digital-logic/03-sequential-logic/memory-cells.md) and storage ([Dynamic Random-Access Memory (DRAM) and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md)). The same formalism, used deliberately, gives [qubits and quantum circuits](../../02-theory-of-computation/05-quantum-computation/qubits-and-quantum-circuits.md).
- **Siblings:** [Electromagnetism](electromagnetism-and-charge.md) says how charges move once free; this leaf says which charges are free. [Thermodynamics](thermodynamics-and-energy.md) supplies the `kT` that sets carrier populations and leakage.

## Common misconceptions

- **"Semiconductors are just poor conductors."** Their value is that their conductivity is *controllable* over many orders of magnitude, not that it is middling.
- **"Holes are a bookkeeping trick with no physical effect."** Holes have measurable effective mass and positive Hall voltage; device behaviour is wrong if you ignore them.
- **"Ordinary computers do not depend on quantum mechanics."** Their logic is classical, but every transistor relies on band structure, and tunnelling sets hard limits on insulator thickness.

## Go deeper

- Charles Kittel, *Introduction to Solid State Physics* (1953; 8th ed., 2005): the classic account of bands and carriers.
- Simon Sze, *Physics of Semiconductor Devices* (1969): the reference for semiconductor physics as engineers use it.
- Richard Feynman, Robert Leighton and Matthew Sands, *The Feynman Lectures on Physics, Vol. III* (1965): quantum mechanics with an eye on semiconductors.
