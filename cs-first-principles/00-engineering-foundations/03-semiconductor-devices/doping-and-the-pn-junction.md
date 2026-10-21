# Doping and the PN Junction

> **Layer:** [00 Engineering Foundations](../README.md) › [Semiconductor Devices](README.md)
> **Builds on:** [Quantum Mechanics and Band Theory](../01-physics-of-computation/quantum-mechanics-and-band-theory.md), [Thermodynamics and Energy](../01-physics-of-computation/thermodynamics-and-energy.md)
> **Enables:** [The MOSFET](the-mosfet.md), [CMOS](cmos.md), [Fabrication and Scaling](fabrication-and-scaling.md)

## Essence

Pure silicon conducts poorly, but adding a tiny, precisely controlled amount of the right impurity, a process called doping, raises its conductivity by many orders of magnitude and decides whether the current is carried mainly by electrons (n-type) or holes (p-type). Placing an n-type region against a p-type region creates a pn junction. Carriers diffuse across the boundary and leave behind a thin depleted zone with a built-in electric field. The junction conducts easily in one direction and hardly at all in the other, with current depending exponentially on voltage. Every transistor is built from doped regions and junctions, and every chip relies on reverse-biased junctions to keep its devices electrically isolated.

## Core tenets

1. **A few impurity atoms control conductivity.** Replacing a silicon atom (four valence electrons) with phosphorus or arsenic (five) adds an electron that is only weakly bound and is freed at room temperature: a donor, making n-type silicon. Boron (three) leaves a hole: an acceptor, making p-type silicon. Typical doping ranges from about one dopant per 10⁸ silicon atoms (lightly doped channels) to about one per 10³ (heavily doped contacts), yet this raises the carrier count from about 10¹⁰ to roughly 10¹⁴ to 10¹⁹ per cubic centimetre, and higher still in the most heavily doped regions.

2. **Electrons and holes are linked by the mass-action law.** In thermal equilibrium the product of electron and hole concentrations is fixed: `n · p = ni²`. Adding donors raises `n` and suppresses `p` by the same factor. The abundant type is the majority carrier and the scarce type the minority carrier. Many device behaviours, including the junction's forward current, are carried by minority carriers.

3. **Current flows by drift and by diffusion.** Carriers drift in an electric field, at a speed set by their mobility. They also diffuse from regions of high concentration to low, with no field needed, because random thermal motion spreads them out. At equilibrium the two balance; devices work by upsetting that balance.

4. **A pn junction builds its own barrier.** When p and n regions meet, electrons diffuse into the p side and holes into the n side, where they recombine. This leaves fixed ionised dopants behind, positive on the n side and negative on the p side, forming a depletion region with no free carriers. The resulting field opposes further diffusion and creates a built-in potential of roughly 0.6 to 0.9 V in silicon.

5. **The junction rectifies, with current exponential in forward voltage.** A forward voltage (p side positive) lowers the barrier and lets diffusion resume. The current follows the Shockley diode equation `I = Is (e^{V/VT} - 1)`, where `VT = kT/q ≈ 26 mV` at room temperature: about tenfold more current per 60 mV. A reverse voltage raises the barrier, leaving only a tiny leakage current `Is`. This one-way behaviour makes diodes useful for rectification and protection.

6. **Reverse-biased junctions isolate devices and form capacitors.** The depletion region acts as an insulator between two conductive regions, so a reverse-biased junction behaves like a capacitor whose value shrinks as the reverse voltage widens the depletion zone. On a chip, transistor sources and drains sit in wells of opposite doping, kept reverse-biased so that neighbouring devices do not conduct into one another. These junction capacitances add to the load every gate must drive.

7. **Light and junctions interact both ways.** A photon with energy above the band gap can create an electron-hole pair, and the junction's field sweeps them apart as current: the photodiode, the basis of camera sensors and solar cells. In direct-gap materials such as gallium arsenide, recombination emits light: the Light-Emitting Diode (LED) and laser diode used in optical communication.

## Key concepts

| Term | Meaning |
|---|---|
| Doping | Deliberate addition of impurities to set carrier type and concentration. |
| Donor / acceptor | Impurity that supplies an electron (n-type) or a hole (p-type). |
| Majority / minority carrier | The abundant and the scarce carrier type in a doped region. |
| Mass-action law | `n · p = ni²` in equilibrium. |
| Drift | Carrier motion driven by an electric field. |
| Diffusion | Carrier motion driven by a concentration gradient. |
| Depletion region | Zone near a junction emptied of free carriers, holding fixed charge. |
| Built-in potential | Voltage across the depletion region at equilibrium. |
| Forward / reverse bias | Applied voltage that lowers / raises the junction barrier. |

## How it fits

- **Below:** Doping works only because [band theory](../01-physics-of-computation/quantum-mechanics-and-band-theory.md) gives silicon a moderate gap and few intrinsic carriers. The exponential `e^{V/VT}` comes from the Boltzmann statistics of [thermodynamics](../01-physics-of-computation/thermodynamics-and-energy.md).
- **Above:** [The Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET)](the-mosfet.md) is two junctions (source and drain) with a field-controlled channel between them. [Complementary Metal-Oxide-Semiconductor (CMOS)](cmos.md) puts n-type and p-type transistors on one chip using wells isolated by junctions. Doping profiles are written during [fabrication](fabrication-and-scaling.md) by ion implantation. Photodiodes and laser diodes underpin optical links in [networking](../../08-networking/02-link-layer/encoding-and-framing.md) and image sensors feeding [computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md).
- **Siblings:** This is the materials foundation for the other three leaves: the MOSFET uses junctions, CMOS uses both doping types, and fabrication is how doping is placed.

## Common misconceptions

- **"Doped silicon is charged."** Each dopant ion is balanced by its freed carrier, so doped material is neutral overall; only the depletion region holds net charge.
- **"Diodes have a fixed 0.7 V drop."** Current is exponential in voltage; 0.7 V is merely where silicon diode current becomes noticeable at typical currents.
- **"Reverse-biased junctions block current completely."** They leak, and that leakage grows rapidly with temperature.

## Go deeper

- William Shockley, "The Theory of p-n Junctions in Semiconductors and p-n Junction Transistors" (1949): the paper that derived the diode equation.
- Ben Streetman and Sanjay Banerjee, *Solid State Electronic Devices* (1972; 7th ed., 2014): standard undergraduate device physics.
- Robert Pierret, *Semiconductor Device Fundamentals* (1996): careful, intuitive treatment of carriers and junctions.
