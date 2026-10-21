# The MOSFET

> **Layer:** [00 Engineering Foundations](../README.md) › [Semiconductor Devices](README.md)
> **Builds on:** [Doping and the PN Junction](doping-and-the-pn-junction.md), [Electromagnetism and Charge](../01-physics-of-computation/electromagnetism-and-charge.md), [Quantum Mechanics and Band Theory](../01-physics-of-computation/quantum-mechanics-and-band-theory.md)
> **Enables:** [CMOS](cmos.md), [Logic Gates](../../03-digital-logic/02-combinational-logic/logic-gates.md), [Memory Cells](../../03-digital-logic/03-sequential-logic/memory-cells.md), [DRAM and Storage Devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md)

## Essence

The Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET) is a voltage-controlled switch, and it is the most manufactured device in history. A gate electrode sits on a thin insulator above a channel of silicon between two doped terminals, the source and the drain. A voltage on the gate creates an electric field that pulls carriers into the channel, forming a conducting path; remove the voltage and the path disappears. Because the gate is insulated, it draws no steady current, so one transistor's output can drive many others. Digital design treats the MOSFET as an ideal switch with some on-resistance and some capacitance, and nearly all of computing rests on that simplification.

## Core tenets

1. **The gate controls the channel through an electric field, not a current.** In an n-channel MOSFET (nMOS), source and drain are n-type regions in p-type silicon. A positive gate voltage repels holes and attracts electrons beneath the oxide. Once it exceeds the threshold voltage `Vt`, a thin inversion layer of electrons connects source and drain. The gate and channel form a capacitor, so the gate draws current only while being charged.

2. **There are two complementary types.** A p-channel MOSFET (pMOS) is the mirror image: p-type source and drain in n-type silicon, turned on by a gate voltage *below* its source. nMOS transistors pass a strong 0 but a weak 1 (they stop conducting when the output nears `Vdd - Vt`); pMOS pass a strong 1 but a weak 0. Using each only where it is strong is the logic of [Complementary Metal-Oxide-Semiconductor (CMOS)](cmos.md).

3. **Above threshold, current depends on gate overdrive and geometry.** For a long-channel device in saturation, the classic square law is `Id ≈ (μ Cox / 2)(W/L)(Vgs - Vt)²`. Current grows with width `W`, falls with length `L`, and grows with mobility `μ` and oxide capacitance `Cox`. Designers set `W` to trade drive strength against area and input capacitance; electrons' higher mobility is why pMOS devices are drawn roughly two to three times wider to match nMOS.

4. **Short channels deviate from the square law.** In modern devices the lateral field is so high that carriers hit a maximum velocity (velocity saturation), so current grows closer to linearly with overdrive. The drain's field also reaches into the channel and lowers the barrier (drain-induced barrier lowering), so the device is harder to turn off. Short-channel effects are why device engineers redesign geometry each generation rather than just shrinking it.

5. **Below threshold, the transistor is not truly off.** Current falls exponentially as gate voltage drops below `Vt`, by at most a factor of ten per about 60 mV at room temperature, because carriers follow Boltzmann statistics. Billions of slightly leaky transistors add up to watts of static power. This limit is why `Vt`, and hence supply voltage, stopped scaling down.

6. **The digital model is a switch with resistance and capacitance.** For logic, an on transistor is a resistor `Ron ∝ L/W`, an off transistor is open, and every terminal carries capacitance. With [capacitance and timing](../02-electrical-circuits/capacitance-and-timing.md), this model predicts gate delay well enough to design processors. The abstraction hides the device physics behind three numbers.

7. **Better gate control is the theme of modern transistor structures.** The gate must dominate the channel's electrostatics over the drain. Steps along this path: high-k metal gates (late 2000s) to allow thinner effective insulators without tunnelling leakage; FinFETs (about 2011 onward), where the channel is a vertical fin wrapped on three sides; and gate-all-around nanosheets (from about 2022), with the gate on all four sides.

8. **The same device stores bits.** A Dynamic Random-Access Memory (DRAM) cell is one MOSFET acting as an access switch to a capacitor. A flash cell is a MOSFET with an extra isolated "floating" gate or charge-trap layer, whose trapped charge shifts `Vt` and so encodes bits that persist without power.

## Key concepts

| Term | Meaning |
|---|---|
| Gate / source / drain / body | Control electrode; the two channel terminals; the substrate beneath. |
| Threshold voltage (`Vt`) | Gate-to-source voltage at which a conducting channel forms. |
| Inversion layer | Thin channel of minority carriers induced under the gate. |
| nMOS / pMOS | MOSFETs with electron / hole channels. |
| Saturation | Regime where drain current is roughly independent of drain voltage. |
| Subthreshold conduction | Exponentially small current below `Vt`; the source of leakage. |
| On-resistance | Effective resistance of a fully on transistor. |
| FinFET / gate-all-around | 3D transistor shapes that wrap the gate around the channel. |

## How it fits

- **Below:** Source and drain are [doped regions and junctions](doping-and-the-pn-junction.md). Gate control is the field effect from [electromagnetism](../01-physics-of-computation/electromagnetism-and-charge.md), and tunnelling through the oxide is from [quantum mechanics](../01-physics-of-computation/quantum-mechanics-and-band-theory.md).
- **Above:** Pairs of nMOS and pMOS make [CMOS](cmos.md) gates, which are the [logic gates](../../03-digital-logic/02-combinational-logic/logic-gates.md) of digital design. MOSFETs as access switches and charge-storing gates form the Static Random-Access Memory (SRAM), DRAM and flash cells of [memory cells](../../03-digital-logic/03-sequential-logic/memory-cells.md), organised into systems in [DRAM and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md). Leakage and threshold limits explain [power and the end of scaling](../../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md).
- **Siblings:** [Doping](doping-and-the-pn-junction.md) supplies the materials, [CMOS](cmos.md) combines MOSFETs into logic, and [fabrication and scaling](fabrication-and-scaling.md) explains how they are made smaller each generation.

## Common misconceptions

- **"A transistor is a perfect on/off switch."** It has finite on-resistance, leaks when off, and passes one logic level only weakly.
- **"Node names describe gate length."** Names such as "5 nm" are marketing labels; physical gate lengths and pitches are larger and differ by manufacturer.
- **"The MOSFET came after the bipolar transistor was perfected."** The field-effect idea was patented by Lilienfeld in the 1920s; the first working MOSFET was demonstrated by Atalla and Kahng at Bell Labs in 1959.

## Go deeper

- Simon Sze, *Physics of Semiconductor Devices* (1969): definitive device physics reference.
- Yannis Tsividis, *Operation and Modeling of the MOS Transistor* (1987): the MOSFET in depth, from physics to models.
- Chenming Hu, *Modern Semiconductor Devices for Integrated Circuits* (2010): modern devices by a co-inventor of the FinFET.
