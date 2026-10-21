# Fabrication and Scaling

> **Layer:** [00 Engineering Foundations](../README.md) › [Semiconductor Devices](README.md)
> **Builds on:** [The MOSFET](the-mosfet.md), [Doping and the PN Junction](doping-and-the-pn-junction.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md)
> **Enables:** [FPGA and ASIC](../../03-digital-logic/04-hardware-design/fpga-and-asic.md), [Power and the End of Scaling](../../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md), [Domain-Specific Accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md)

## Essence

Integrated circuits are made by printing patterns onto a silicon wafer, layer by layer, using light projected through masks, then etching, doping and depositing material where the pattern allows. Because every transistor on a wafer is printed at once, the cost of a transistor is roughly the cost of the wafer area it occupies, so shrinking features made transistors exponentially cheaper. That economic fact is Moore's law. For three decades, Dennard scaling also made each shrink faster and no more power-hungry per area. Dennard scaling ended in the mid-2000s and density gains have slowed and grown far more expensive, which explains much of modern computer architecture: multicore, specialisation and the obsession with energy.

## Core tenets

1. **Chips are printed, not assembled.** Photolithography projects a mask's pattern onto light-sensitive resist on the wafer; the exposed pattern then guides etching, ion implantation of dopants, or deposition. Transistors are formed first (front end of line), then wired together by a stack of ten or more metal layers (back end of line). Because the whole wafer is processed in parallel, adding transistors costs area, not assembly labour.

2. **Resolution is set by wavelength, optics and tricks.** The smallest printable feature is about `k1 · λ / NA`, where `λ` is the light's wavelength, `NA` the numerical aperture of the lens, and `k1` a process factor. Industry used 193 nm light (with water immersion) far below its wavelength through multiple patterning, then introduced Extreme Ultraviolet (EUV) lithography at 13.5 nm in high-volume production around 2019. Each step multiplied tool cost; a leading-edge fab now costs on the order of 10 to 20 billion US dollars.

3. **Yield falls exponentially with die area.** Random defects land on a wafer with some density `D`. A simple Poisson model gives the fraction of good dies as `Y ≈ e^{-A·D}` for die area `A`. Big dies are therefore disproportionately expensive, which pushes designers toward smaller dies, redundancy (spare cache rows) and chiplets: several small dies in one package.

4. **Moore's law is an economic observation about density.** Gordon Moore observed in 1965 that the number of components per chip at minimum cost was doubling every year, and in 1975 revised the rate to about every two years. It held roughly for decades because shrinking features packed more transistors into the same costly area. It is not a law of physics, and the cost per transistor has fallen much more slowly at recent nodes.

5. **Dennard scaling made smaller also mean faster and cooler, until it stopped.** Dennard and colleagues (1974) showed that scaling all dimensions and voltages by `1/κ` makes each transistor `κ` times faster, `κ²` times smaller and keeps power per area constant. The rule required voltage to fall with size. Once threshold voltage hit its limit (about 60 mV per decade of subthreshold current) and leakage soared, voltage stalled near 1 V around 2005. Power density then rose with each shrink, so clock rates plateaued and the extra transistors went into more cores and specialised units.

6. **"Node" names stopped measuring anything physical.** Process names like "7 nm" or "3 nm" once matched a feature such as gate length; since the late 1990s they have become generation labels. Actual gate pitches and metal pitches at these nodes are tens of nanometres. Compare processes by measured density (transistors per mm²), performance and power, not by name.

7. **Smaller devices vary more.** When a channel contains only tens of dopant atoms and its edges are a few atoms rough, "identical" transistors differ measurably in threshold and drive. Designs must work across process, voltage and temperature corners, which costs margin and therefore speed and energy.

8. **Packaging is now part of scaling.** As monolithic scaling slows, performance comes from integrating many dies: stacking memory on logic, placing chiplets on silicon interposers, and through-silicon vias. Communication between dies is cheaper than going off-package but still costlier than on-die wires.

## Key concepts

| Term | Meaning |
|---|---|
| Photolithography | Patterning resist on a wafer with light through a mask. |
| Mask (reticle) | Template carrying one layer's pattern. |
| Extreme Ultraviolet (EUV) | 13.5 nm lithography used at leading-edge nodes. |
| Yield | Fraction of dies that work. |
| Die / wafer | One chip / the 300 mm silicon disc on which many are made. |
| Moore's law | Doubling of economical transistor count per chip about every two years. |
| Dennard scaling | Constant power density under proportional shrinking of size and voltage. |
| Process corner | A combination of process, voltage and temperature extremes a design must tolerate. |
| Chiplet | A small die combined with others in one package. |

## How it fits

- **Below:** It manufactures [Metal-Oxide-Semiconductor Field-Effect Transistors (MOSFETs)](the-mosfet.md) by placing [doped regions](doping-and-the-pn-junction.md); quantum tunnelling from [band theory](../01-physics-of-computation/quantum-mechanics-and-band-theory.md) limits how thin layers can get. Yield models use [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md).
- **Above:** Mask cost and yield shape the economics of [FPGA and ASIC](../../03-digital-logic/04-hardware-design/fpga-and-asic.md) design. The end of Dennard scaling is the starting point of [power and the end of scaling](../../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md), [multicore](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md) and [domain-specific accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md). Cheap transistors also fuelled the computing history told in [history of computing](../../15-computing-in-context/history-of-computing.md).
- **Siblings:** This leaf makes the devices of [the MOSFET](the-mosfet.md) and [CMOS](cmos.md); scaling changed their properties each generation.

## Common misconceptions

- **"Moore's law says performance doubles every 18 months."** It concerns transistor count per economical chip; performance gains came from Dennard scaling and architecture, and slowed earlier.
- **"Moore's law is dead, so nothing is improving."** Density still increases, more slowly and at higher cost; gains have shifted to packaging, specialisation and energy efficiency.
- **"A 3 nm chip has 3 nm transistors."** Node names are labels, not measurements.

## Go deeper

- Gordon Moore, "Cramming More Components onto Integrated Circuits" (1965): the original observation.
- Robert Dennard et al., "Design of Ion-Implanted MOSFET's with Very Small Physical Dimensions" (1974): the scaling rules.
- James Plummer, Michael Deal and Peter Griffin, *Silicon VLSI Technology: Fundamentals, Practice and Modeling* (2000): how chips are actually made.
