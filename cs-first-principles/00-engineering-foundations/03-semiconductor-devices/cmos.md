# CMOS

> **Layer:** [00 Engineering Foundations](../README.md) › [Semiconductor Devices](README.md)
> **Builds on:** [The MOSFET](the-mosfet.md), [Circuit Laws](../02-electrical-circuits/circuit-laws.md), [Boolean Algebra](../../01-mathematical-foundations/04-algebra/boolean-algebra.md)
> **Enables:** [Logic Gates](../../03-digital-logic/02-combinational-logic/logic-gates.md), [Latches and Flip-Flops](../../03-digital-logic/03-sequential-logic/latches-and-flip-flops.md), [Timing and Power](../../03-digital-logic/04-hardware-design/timing-and-power.md)

## Essence

Complementary Metal-Oxide-Semiconductor (CMOS) is the circuit style used by almost every digital chip made since the late 1980s. Each logic gate has two networks of transistors: a pull-up network of p-channel Metal-Oxide-Semiconductor Field-Effect Transistors (MOSFETs), called pMOS, connecting the output to the supply, and a pull-down network of n-channel MOSFETs (nMOS) connecting it to ground. The two networks are logical duals, so for any input exactly one of them conducts. The output is therefore always firmly driven to one rail or the other, and in steady state there is no path from supply to ground, so an idle gate draws almost no power. CMOS is where Boolean algebra becomes physical: series transistors compute AND, parallel transistors compute OR, and De Morgan's laws relate the two networks.

## Core tenets

1. **Complementary networks mean one is on and one is off.** The pull-down network conducts exactly when the output should be 0; the pull-up network conducts exactly when it should be 1. Since they are never both on in steady state, the output sits at `Vdd` or ground with no voltage-divider compromise. This gives full rail-to-rail swing and large noise margins.

2. **Static power is near zero, so energy goes into switching.** With no steady path from supply to ground, a CMOS gate holding a value consumes only leakage current. Energy is spent when outputs change: charging load capacitance costs `CV²` per full cycle, plus a brief short-circuit current while both networks partly conduct during a transition. This property let CMOS displace earlier nMOS-only logic, which burned power whenever an output was low.

3. **Series and parallel transistors implement AND and OR, and the networks are duals.** nMOS transistors in series pull the output down only if all inputs are 1 (AND); in parallel, if any is 1 (OR). The pull-up network uses the dual arrangement with pMOS, which conduct on 0 inputs. A two-input NAND, for example, has two nMOS in series and two pMOS in parallel. The duality is De Morgan's law, `¬(a ∧ b) = ¬a ∨ ¬b`, built in silicon.

```
       Vdd ──┬───────────┐
             │           │
        A ─[pMOS]   B ─[pMOS]       pull-up: pMOS in parallel
             │           │
             └─────┬─────┘
                   ├────────── Y = NOT (A AND B)
              A ─[nMOS]
                   │                pull-down: nMOS in series
              B ─[nMOS]
                   │
                  GND
```

4. **Single CMOS gates are naturally inverting.** A rising input turns on nMOS (pulling the output down) and turns off pMOS. So a single-stage CMOS gate computes a *negated* (monotone decreasing) function: NOT, NAND, NOR, and-or-invert. Non-inverting functions such as AND need two stages. This is why NAND and NOR, not AND and OR, are the primitive gates of chip design.

5. **NAND is usually preferred to NOR because holes are slow.** Series transistors add resistance. A NOR puts pMOS in series in the pull-up, and pMOS are already weaker than nMOS, so they must be made much wider to match speed. A NAND puts its series stack in the faster nMOS network. For the same reason, gates rarely have more than about four inputs: long series stacks get slow.

6. **The inverter has high gain, which makes logic restoring.** The CMOS inverter's voltage transfer curve switches sharply around the midpoint: a small input change there causes a large output change, while inputs near either rail produce outputs pinned to the opposite rail. That gain is what restores degraded signals at every stage, the property on which the whole digital abstraction depends.

7. **Two cross-coupled inverters remember a bit.** Feeding an inverter's output into a second inverter and back again creates two stable states. With access transistors added, this becomes the six-transistor Static Random-Access Memory (SRAM) cell used in caches and register files ([memory cells](../../03-digital-logic/03-sequential-logic/memory-cells.md)), and the core of latches and flip-flops.

8. **CMOS has its own failure modes.** The parasitic structure of adjacent n and p regions forms a thyristor that can latch a short circuit between supply and ground (latch-up), prevented by layout rules and well contacts. Leakage, once negligible, now accounts for a large share of total power in many designs.

## Key concepts

| Term | Meaning |
|---|---|
| Pull-up network | pMOS transistors connecting the output to `Vdd`. |
| Pull-down network | nMOS transistors connecting the output to ground. |
| Dual network | Series in one network corresponds to parallel in the other. |
| Static CMOS | Gates whose output is always actively driven by one network. |
| Voltage Transfer Characteristic (VTC) | Output voltage as a function of input voltage for a gate. |
| Short-circuit current | Brief current through both networks during a transition. |
| Transmission gate | An nMOS and pMOS in parallel, passing both levels strongly. |
| Latch-up | Parasitic thyristor turning on and shorting supply to ground. |
| SRAM cell | Two cross-coupled inverters plus two access transistors. |

## How it fits

- **Below:** CMOS uses both kinds of [MOSFET](the-mosfet.md) and the voltage-divider reasoning of [circuit laws](../02-electrical-circuits/circuit-laws.md). Its structure realises [Boolean algebra](../../01-mathematical-foundations/04-algebra/boolean-algebra.md).
- **Above:** CMOS gates are the physical substrate of [logic gates](../../03-digital-logic/02-combinational-logic/logic-gates.md); cross-coupled inverters become [latches and flip-flops](../../03-digital-logic/03-sequential-logic/latches-and-flip-flops.md); its power behaviour drives [timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md) and the SRAM arrays of [cache design](../../04-computer-architecture/03-memory-hierarchy/cache-design.md).
- **Siblings:** [The MOSFET](the-mosfet.md) supplies the switches, [doping](doping-and-the-pn-junction.md) makes both types possible on one wafer, and [fabrication and scaling](fabrication-and-scaling.md) makes them smaller and cheaper.

## Common misconceptions

- **"CMOS consumes no power."** It consumes little *static* power; switching and leakage power are substantial and set the limits of modern chips.
- **"AND and OR are the basic gates."** In CMOS the cheap primitives are inverting: NAND, NOR and NOT. AND costs an extra inverter.
- **"Any arrangement of transistors gives a valid gate."** If the pull-up and pull-down networks are not exact duals, some input will leave the output floating or fighting, giving an invalid level.

## Go deeper

- Neil Weste and David Harris, *CMOS VLSI Design: A Circuits and Systems Perspective* (4th ed., 2010): the standard text on CMOS circuits.
- Carver Mead and Lynn Conway, *Introduction to VLSI Systems* (1980): the book that made chip design accessible to computer scientists.
- Jan Rabaey, Anantha Chandrakasan and Borivoje Nikolić, *Digital Integrated Circuits* (2nd ed., 2003): CMOS inverter, gates and power in detail.
