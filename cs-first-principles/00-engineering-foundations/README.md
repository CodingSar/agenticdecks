# 00 Engineering Foundations

> **Layer:** 00 Engineering Foundations (physical root of the stack)
> **Children:** [Physics of Computation](01-physics-of-computation/README.md) · [Electrical Circuits](02-electrical-circuits/README.md) · [Semiconductor Devices](03-semiconductor-devices/README.md) · [Signals and Systems](04-signals-and-systems/README.md) · [Engineering Method](05-engineering-method/README.md)

## What this area is about

Every computation is a physical event. Before there can be bits, gates, instructions or programs, there must be matter arranged so that one signal reliably controls another, so that a state can be held, and so that all of this can be made small, fast, cheap and cool enough to be useful. This layer answers the question: *what does the physical world have to provide for computing to be possible, and what limits does it impose that no amount of cleverness higher up can remove?*

The answer has a single thread. Physics supplies charge, fields and semiconductors whose conductivity can be controlled. Circuit theory abstracts fields into networks with delay and noise. Semiconductor devices turn controllable conductivity into the Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET), and pairs of them into Complementary Metal-Oxide-Semiconductor (CMOS) logic that draws almost no power at rest. Signals and systems explain why we then choose to see only two voltage levels, the digital abstraction that stops noise from accumulating. Engineering method supplies the habits of thought (tradeoffs, redundancy, measurement) that every later layer reuses.

The one interface this layer contributes to the stack is the **digital switch obeying the static discipline**: a device that, given valid logic levels at its inputs, produces valid, restored logic levels at its outputs after a predictable delay and at a predictable energy cost. Everything above layer 00 treats the physical world through that contract.

## Why this layer sits here

This is the **bottom layer**: the physical root of the whole knowledge base. Nothing in the tree lies beneath it. It needs no other layer's results, only mathematics as a language.

That language comes from [01 Mathematical Foundations](../01-mathematical-foundations/README.md), which is the **parallel formal root**. Layer 01 does not depend on 00, and 00 does not depend on 01's theorems: electrons obey physics whether or not anyone has written down Boolean algebra. Layer 00 *uses* 01's notation ([calculus](../01-mathematical-foundations/05-continuous-mathematics/calculus.md) for fields and resistance-capacitance (RC) transients, [linear algebra](../01-mathematical-foundations/04-algebra/linear-algebra.md) for circuits and quantum states, [probability](../01-mathematical-foundations/06-probability-and-statistics/probability.md) for noise and reliability) the way any engineering does. The numbering 00 and 01 only reflects reading order; the two are siblings at the base.

The two roots grow separately for one layer: 01 leads to [02 Theory of Computation](../02-theory-of-computation/README.md), which asks what can be computed at all, while 00 builds the switch. They **meet at [03 Digital Logic](../03-digital-logic/README.md)**, where [Boolean algebra](../01-mathematical-foundations/04-algebra/boolean-algebra.md) from the formal pillar is realised in [CMOS](03-semiconductor-devices/cmos.md) from the physical pillar. From layer 04 upward every layer stands on both.

```
   02 Theory of Computation            (formal pillar continues)
            ▲
   01 Mathematical Foundations ─────┐
                                    ├──► 03 Digital Logic ──► 04 Architecture ──► ...
   00 Engineering Foundations ──────┘
   (physical root: this layer)
```

What the layers above need from this one: switches with known delay and energy ([capacitance and timing](02-electrical-circuits/capacitance-and-timing.md), [thermodynamics and energy](01-physics-of-computation/thermodynamics-and-energy.md)); reliable discrete levels ([analog vs digital](04-signals-and-systems/analog-vs-digital.md)); a way to remember a bit ([feedback and control](04-signals-and-systems/feedback-and-control.md), via positive feedback); physical media for storage ([electromagnetism and charge](01-physics-of-computation/electromagnetism-and-charge.md), turned into static, dynamic and flash [memory cells](../03-digital-logic/03-sequential-logic/memory-cells.md) in layer 03); and the scaling trends that set the economics of every chip ([fabrication and scaling](03-semiconductor-devices/fabrication-and-scaling.md)).

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Physics of Computation](01-physics-of-computation/README.md) | Charge, fields, bands and energy: what matter allows and what it costs | Mathematics only |
| [Electrical Circuits](02-electrical-circuits/README.md) | The lumped abstraction: laws, RC timing, noise and margins | Physics |
| [Semiconductor Devices](03-semiconductor-devices/README.md) | Doping, the MOSFET, CMOS logic, fabrication and scaling | Physics, circuits |
| [Signals and Systems](04-signals-and-systems/README.md) | The digital abstraction, sampling and quantisation, feedback | Circuits, devices |
| [Engineering Method](05-engineering-method/README.md) | Tradeoffs, reliability and redundancy, measurement and modelling | Used by all of the above |

Read the first four in order: each is the next step of abstraction away from raw physics. Physics says what is possible; circuits make it tractable to analyse; devices make the controllable switch; signals and systems turn analog switches into a reliable digital medium. Engineering method runs alongside all four: it is introduced here because this is where its ideas are clearest and most physical, and because every higher layer reuses them.

## Connections to neighbouring layers

- **[01 Mathematical Foundations](../01-mathematical-foundations/README.md):** The parallel formal root. It supplies the language (calculus, linear algebra, probability, optimisation) and, crucially, the [Boolean algebra](../01-mathematical-foundations/04-algebra/boolean-algebra.md) that layer 03 will build out of this layer's switches.
- **[02 Theory of Computation](../02-theory-of-computation/README.md):** Physics meets information theory in Landauer's principle and in Shannon's channel capacity, which bounds what noisy wires can carry. Quantum computation uses the same quantum mechanics that explains semiconductor bands.
- **[03 Digital Logic](../03-digital-logic/README.md):** The direct consumer. CMOS gates become logic gates, cross-coupled inverters become flip-flops, RC delay becomes timing analysis, and `CV²f` becomes power analysis.
- **[04 Computer Architecture](../04-computer-architecture/README.md):** The end of Dennard scaling, wire delay and memory-cell physics shape caches, multicore and accelerators.
- **[08 Networking](../08-networking/README.md):** The speed of light sets the floor on latency; signal integrity and line coding shape the link layer.
- **[10 Distributed and Parallel Computing](../10-distributed-and-parallel-computing/README.md) and [12 Software Engineering](../12-software-engineering/README.md):** Reliability through redundancy and measurement-driven engineering, first stated here, return as replication and site reliability practice.

## Connections across layers

This layer gives the whole stack its physical limits. Signal propagation and RC delay limit clock rates and favour [pipelining](../04-computer-architecture/02-processor-microarchitecture/pipelining.md). Power density and the end of voltage scaling explain [power and the end of scaling](../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md) and the turn to parallelism. Physical leakage of information becomes [side channels](../11-security-and-cryptography/03-system-security/side-channels.md). The energy cost of moving data is a large part of why [training at scale](../13-artificial-intelligence/03-deep-learning/training-at-scale.md) is a hardware problem. The rise of cheap transistors is the engine of the [history of computing](../15-computing-in-context/history-of-computing.md).

## Cross-cutting threads

- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): fields become circuits, circuits become switches, switches become digital levels.
- [Limits and impossibility](../CROSS-CUTTING.md#limits-and-impossibility): the speed of light, `kT`, the Landauer bound and lithography resolution.
- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): speed, energy, area, noise margin and cost are traded at every step.
- [Redundancy and fault tolerance](../CROSS-CUTTING.md#redundancy-and-fault-tolerance): noise margins, error-correcting codes and von Neumann's reliable-from-unreliable principle.
- [Feedback and control](../CROSS-CUTTING.md#feedback-and-control): negative feedback for precision, positive feedback for memory.
- [Encoding and representation](../CROSS-CUTTING.md#encoding-and-representation): a bit is a physical state, and the choice of state decides its cost.
