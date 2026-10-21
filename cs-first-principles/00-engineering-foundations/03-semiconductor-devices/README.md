# Semiconductor Devices

> **Layer:** [00 Engineering Foundations](../README.md) › Semiconductor Devices
> **Children:** [Doping and the PN Junction](doping-and-the-pn-junction.md) · [The MOSFET](the-mosfet.md) · [CMOS](cmos.md) · [Fabrication and Scaling](fabrication-and-scaling.md)

## What this area is about

Computing needs a switch: a device in which one signal controls whether another flows, that can be made tiny, cheap and in astronomical numbers, and whose output can drive further switches. This area answers: *how do we build such a switch out of matter, how do we combine switches into logic, and how did we learn to make billions of them on a fingernail?* The answer runs from doped silicon through the Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET) to Complementary Metal-Oxide-Semiconductor (CMOS) logic, and finally to the lithographic manufacturing that made transistors exponentially cheaper for half a century.

The unifying idea is **field-effect control of a semiconductor channel**. An insulated gate's voltage determines whether a channel of carriers exists between two doped terminals. Because the gate draws no steady current, one switch can drive many; because the device is planar, it can be printed by the billion; and because n-type and p-type versions are complementary, they can be paired so that logic draws almost no power while idle.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Doping and the PN Junction](doping-and-the-pn-junction.md) | Materials: setting carrier type and density; junctions for isolation and diodes | Band theory, thermodynamics |
| [The MOSFET](the-mosfet.md) | The device: a voltage-controlled switch, with its threshold, leakage and short-channel limits | Doping, electromagnetism |
| [CMOS](cmos.md) | The circuit style: complementary pull-up and pull-down networks forming restoring, low-power logic | MOSFET, circuit laws, Boolean algebra |
| [Fabrication and Scaling](fabrication-and-scaling.md) | Manufacturing and economics: lithography, yield, Moore's law, Dennard scaling and its end | All three above |

The reading order is the order of construction. Doping makes regions of controlled conductivity. Two such regions with a gate between them make a MOSFET. Pairs of complementary MOSFETs make CMOS gates. Fabrication explains how all of this is printed, why shrinking it made each transistor cheaper and (for a while) faster and cooler, and why that free ride ended.

```
  doped silicon ──► pn junctions ──► MOSFET (switch) ──► CMOS gate (logic + memory cell)
                                          ▲                        │
                                          └──── fabrication & scaling (make it smaller, cheaper)
```

## Connections to sibling areas

- **[Physics of Computation](../01-physics-of-computation/README.md):** Band theory explains why doping works; the field effect is electromagnetism; the 60 mV per decade subthreshold limit and leakage come from thermodynamics.
- **[Electrical Circuits](../02-electrical-circuits/README.md):** For design, transistors become switches with resistance and capacitance; gate delay is then resistance-capacitance (RC) timing, and CMOS output levels are voltage dividers that never fight.
- **[Signals and Systems](../04-signals-and-systems/README.md):** The high gain of the CMOS inverter is what makes digital restoration possible; cross-coupled inverters are positive feedback.
- **[Engineering Method](../05-engineering-method/README.md):** Yield is reliability statistics; scaling is a history of tradeoffs between speed, power, density and cost.

## Connections across layers

This area is the physical half of the meeting point in [03 Digital Logic](../../03-digital-logic/README.md): CMOS gates *are* the [logic gates](../../03-digital-logic/02-combinational-logic/logic-gates.md), and cross-coupled CMOS inverters are [latches and flip-flops](../../03-digital-logic/03-sequential-logic/latches-and-flip-flops.md). Manufacturing economics decide between [Field-Programmable Gate Arrays (FPGAs) and Application-Specific Integrated Circuits (ASICs)](../../03-digital-logic/04-hardware-design/fpga-and-asic.md). The end of Dennard scaling is the starting point of modern architecture: [power and the end of scaling](../../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md), [multicore](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md) and [domain-specific accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md). MOSFET-based cells form the memories in [Dynamic Random-Access Memory (DRAM) and storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md). Physical device behaviour even leaks through to security in [side channels](../../11-security-and-cryptography/03-system-security/side-channels.md), for example power analysis and DRAM disturbance errors.

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): the MOSFET is abstracted as a switch, CMOS as a Boolean gate.
- [Composition](../../CROSS-CUTTING.md#composition): series and parallel transistors compose into AND and OR, with predictable duality.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): subthreshold slope, tunnelling and lithography resolution bound how far devices shrink.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): drive strength against capacitance and area; threshold voltage against leakage.
