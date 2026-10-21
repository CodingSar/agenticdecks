# Noise and Signal Integrity

> **Layer:** [00 Engineering Foundations](../README.md) › [Electrical Circuits](README.md)
> **Builds on:** [Circuit Laws](circuit-laws.md), [Electromagnetism and Charge](../01-physics-of-computation/electromagnetism-and-charge.md), [Thermodynamics and Energy](../01-physics-of-computation/thermodynamics-and-energy.md)
> **Enables:** [Analog vs Digital](../04-signals-and-systems/analog-vs-digital.md), [Logic Gates](../../03-digital-logic/02-combinational-logic/logic-gates.md), [Encoding and Framing](../../08-networking/02-link-layer/encoding-and-framing.md), [Channel Capacity and Error Correction](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md)

## Essence

Real voltages are never exactly what the designer intended. Thermal agitation, neighbouring wires, supply fluctuations, reflections on long wires and even cosmic rays all add unwanted signal, called noise. Signal integrity is the discipline of keeping noise small enough that a receiver still reads the right value. Digital logic survives noise by defining wide bands of voltage as "0" and "1", leaving guard bands (noise margins) between what a driver promises and what a receiver demands, and by using gates that restore weak signals to full strength at every stage. Where that is not enough, as in fast links between chips, engineers shape the wire itself and add error-correcting codes.

## Core tenets

1. **Noise is unavoidable, and some of it is fundamental.** Thermal (Johnson-Nyquist) noise in any resistor has mean-square voltage `4kTRB` over bandwidth `B`, purely from the random motion of carriers. Shot noise comes from charge arriving in discrete electrons. These set a floor no design removes. Most practical noise, however, is self-inflicted: crosstalk, supply noise and reflections from the circuit's own switching.

2. **Noise margins turn uncertainty into a contract.** A driver promises its "1" output is at least `VOH` and its "0" at most `VOL`; a receiver promises to read any input above `VIH` as 1 and below `VIL` as 0. The gaps `NMH = VOH - VIH` and `NML = VIL - VOL` are the noise margins: how much noise a signal can pick up on the way and still be read correctly. Values between `VIL` and `VIH` are forbidden; the design must ensure valid signals never sit there when sampled.

3. **Restoring logic stops noise from accumulating.** A gate with gain greater than 1 in its transition region and less than 1 near the rails maps a slightly degraded input back to a clean output. Each stage therefore throws away the noise it received instead of passing it on. This is the physical reason a chain of a billion digital gates works while a chain of a billion analog amplifiers would drown in noise.

4. **Crosstalk and supply noise come from the circuit's own activity.** Adjacent wires are coupled by capacitance and inductance, so a switching "aggressor" wire injects a pulse into a quiet "victim". When many gates switch together, current surges through the resistance and inductance of the power network, so the supply sags (IR drop) and ground bounces (`L di/dt`). Designers counter this with spacing, shielding, decoupling capacitors and many power pins.

5. **Fast signals on long wires behave as waves, so wires must be terminated.** When a signal's rise time is comparable to the time it takes to travel the wire, the wire is a transmission line with a characteristic impedance (often 50 Ω on boards). If the far end does not match that impedance, part of the wave reflects back, causing ringing and false transitions. Matching terminations absorb the wave. This is why board-level and cable links are designed as controlled-impedance channels.

6. **Differential signalling cancels common noise.** Sending a signal as the difference between two wires carrying opposite voltages means noise that hits both wires equally cancels at the receiver. It also reduces radiated interference and lets the swing be small (hundreds of millivolts), saving power. Most fast serial links between chips, such as Peripheral Component Interconnect Express (PCIe), Universal Serial Bus (USB) and Ethernet, use it.

7. **At the limit, signal integrity becomes information theory.** For high-speed links the eye opening (the clean region in an overlay of many bit periods) shrinks until raw errors are inevitable. Links then use equalisation to undo channel distortion and forward error correction to fix residual errors. Shannon's channel capacity says how many bits per second a channel of given bandwidth and signal-to-noise ratio can carry reliably at all.

8. **Rare particles flip bits in storage.** Alpha particles from packaging and neutrons from cosmic-ray showers deposit charge in silicon that can flip a stored bit without damaging anything: a soft error. As stored charge per bit has shrunk, these upsets became significant in large memories, which is why servers use error-correcting code memory.

## Key concepts

| Term | Meaning |
|---|---|
| Noise margin | Guard band between guaranteed output levels and required input levels. |
| `VOH`, `VOL`, `VIH`, `VIL` | Output high/low guarantees and input high/low thresholds. |
| Thermal noise | Random voltage from carrier motion, mean-square `4kTRB`. |
| Crosstalk | Signal coupled from one wire into a neighbour. |
| Ground bounce | Local ground voltage shift caused by fast current through inductance. |
| Transmission line | A wire long enough relative to rise time that it must be modelled as a wave guide. |
| Characteristic impedance | Ratio of voltage to current for a wave on a transmission line. |
| Differential signalling | Encoding a bit as the difference between two complementary wires. |
| Eye diagram | Overlay of many bit periods showing how much clean margin remains. |
| Soft error | A transient bit flip caused by a particle strike or noise, not by a defect. |

## How it fits

- **Below:** It uses [circuit laws](circuit-laws.md) and [electromagnetism](../01-physics-of-computation/electromagnetism-and-charge.md) for coupling and reflection, and [thermodynamics](../01-physics-of-computation/thermodynamics-and-energy.md) for thermal noise.
- **Above:** Noise margins and restoration are the basis of the digital abstraction in [analog vs digital](../04-signals-and-systems/analog-vs-digital.md) and of [logic gates](../../03-digital-logic/02-combinational-logic/logic-gates.md). Line coding for wired links appears in [encoding and framing](../../08-networking/02-link-layer/encoding-and-framing.md). Shannon's limit and error-correcting codes are in [channel capacity and error correction](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md). Soft errors motivate error-correcting memory in [reliability and redundancy](../05-engineering-method/reliability-and-redundancy.md).
- **Siblings:** [Circuit laws](circuit-laws.md) assume ideal wires; this leaf handles the cases where that assumption fails. [Capacitance and timing](capacitance-and-timing.md) and noise interact: slow edges are more vulnerable to noise, fast ones create more of it.

## Common misconceptions

- **"Digital signals are immune to noise."** They tolerate noise up to the noise margin; beyond it they fail abruptly rather than gracefully.
- **"A wire is a wire."** At gigabit rates a board trace is a transmission line, and its shape, length and termination decide whether the link works.
- **"Bit flips mean broken hardware."** Most are transient soft errors from particles or marginal timing, which is why error correction rather than replacement is the usual remedy.

## Go deeper

- Howard Johnson and Martin Graham, *High-Speed Digital Design: A Handbook of Black Magic* (1993): practical transmission lines, termination and crosstalk.
- William Dally and John Poulton, *Digital Systems Engineering* (1998): noise, signalling and timing from first principles.
- Paul Horowitz and Winfield Hill, *The Art of Electronics* (3rd ed., 2015): noise sources and practical mitigation.
