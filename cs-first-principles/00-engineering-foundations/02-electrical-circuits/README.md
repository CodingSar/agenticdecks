# Electrical Circuits

> **Layer:** [00 Engineering Foundations](../README.md) › Electrical Circuits
> **Children:** [Circuit Laws](circuit-laws.md) · [Capacitance and Timing](capacitance-and-timing.md) · [Noise and Signal Integrity](noise-and-signal-integrity.md)

## What this area is about

Electromagnetism is too detailed to design with directly. Circuit theory is the first abstraction that makes design tractable: it replaces continuous fields with a graph of idealised elements, each described by a simple relation between voltage and current, and lets two conservation laws determine the rest. This area answers: *how do we reason about networks of conductors and devices precisely enough to build them, and what do the simplifications cost?*

The unifying idea is **the lumped abstraction and its limits**. Within its domain (circuits small relative to signal wavelengths), Kirchhoff's laws and element equations predict behaviour exactly enough to design billions of transistors. Its first refinement adds time: every node has capacitance, so changes take RC time, which becomes gate delay and clock speed. Its boundary is noise and signal integrity: at high speed or over long wires, coupling, reflection and fundamental noise break the ideal picture, and engineers must either restore the assumptions (termination, shielding) or design with margins that tolerate their violation.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Circuit Laws](circuit-laws.md) | The static model: KCL, KVL, Ohm's law, power, Thévenin equivalents, the voltage divider | Electromagnetism |
| [Capacitance and Timing](capacitance-and-timing.md) | The dynamic model: RC delay, gate and wire delay, critical paths, `CV²` energy | Circuit laws |
| [Noise and Signal Integrity](noise-and-signal-integrity.md) | Where the model fails: noise sources, noise margins, transmission lines, differential signalling | Circuit laws, capacitance |

Read them in order. Circuit laws give a timeless snapshot: which voltage each node settles to. Capacitance and timing add how long settling takes and what it costs, which is the origin of every delay number in digital design. Noise and signal integrity then asks what disturbs those settled values and how much margin a design needs so that disturbances do not change a 0 into a 1.

```
  fields (physics)
       │  lumped approximation
       ▼
  circuit laws ──(add C, time)──► capacitance & timing ──► delay, clock period, energy
       │                                   │
       └───────(where assumptions fail)────┴──► noise & signal integrity ──► margins
```

## Connections to sibling areas

- **[Physics of Computation](../01-physics-of-computation/README.md):** Circuit laws are the low-frequency limit of electromagnetism; thermal noise and `CV²` energy come from thermodynamics.
- **[Semiconductor Devices](../03-semiconductor-devices/README.md):** Transistors enter circuit analysis as nonlinear elements, simplified for logic to switches with on-resistance and capacitance. CMOS (Complementary Metal-Oxide-Semiconductor) gate design is voltage-divider reasoning plus RC timing.
- **[Signals and Systems](../04-signals-and-systems/README.md):** Noise margins are what make the digital abstraction possible, and feedback circuits (amplifiers, oscillators, latches) are circuits analysed as systems.
- **[Engineering Method](../05-engineering-method/README.md):** The lumped model is the textbook case of a model with a domain of validity; speed against energy against noise margin is a classic tradeoff.

## Connections across layers

This area supplies the timing and energy model that [03 Digital Logic](../../03-digital-logic/README.md) relies on: propagation delay in [logic gates](../../03-digital-logic/02-combinational-logic/logic-gates.md), the setup and hold constraints of [clocking and synchronous design](../../03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md), and power analysis in [timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md). Wire delay explains why big caches are slow ([cache design](../../04-computer-architecture/03-memory-hierarchy/cache-design.md)) and why critical paths motivate [pipelining](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md). Transmission lines and line codes reappear in [encoding and framing](../../08-networking/02-link-layer/encoding-and-framing.md), and the noisy channel is formalised in [channel capacity and error correction](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md).

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): the lumped model hides fields behind two numbers per element.
- [Interface vs implementation](../../CROSS-CUTTING.md#interface-vs-implementation): a Thévenin equivalent describes any linear network by its behaviour at two terminals.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): thermal noise sets a floor no circuit removes.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): noise margins are redundancy in voltage space.
