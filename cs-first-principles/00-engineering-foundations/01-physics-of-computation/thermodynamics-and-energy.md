# Thermodynamics and Energy

> **Layer:** [00 Engineering Foundations](../README.md) › [Physics of Computation](README.md)
> **Builds on:** [Electromagnetism and Charge](electromagnetism-and-charge.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md)
> **Enables:** [Timing and Power](../../03-digital-logic/04-hardware-design/timing-and-power.md), [Power and the End of Scaling](../../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md), [Entropy and Information](../../02-theory-of-computation/01-information-theory/entropy-and-information.md)

## Essence

Computation is a physical process, so it consumes energy and produces heat, and the heat must be removed. Thermodynamics tells us three things that shape every computer. First, today's chips spend energy mostly on charging and discharging capacitance, so energy per operation scales with capacitance times voltage squared. Second, thermal agitation at temperature `T` (energy scale `kT`) makes noise and sets how sharply a transistor can turn off, which stopped supply voltages from shrinking. Third, there is a fundamental minimum: erasing one bit of information must dissipate at least `kT ln 2` of heat (Landauer's principle). Present hardware sits many orders of magnitude above that floor, but the practical limit, getting heat out of silicon, is already binding.

## Core tenets

1. **Switching a node costs `CV²` per full cycle, independent of how fast you do it.** In Complementary Metal-Oxide-Semiconductor (CMOS) logic, charging capacitance `C` to voltage `V` through a resistor draws `CV²` from the supply: half is stored on the capacitor and half is lost as heat in the resistor, whatever its value. Discharging dumps the stored half. Dynamic power is therefore `P = αCV²f`, where `α` is the fraction of nodes switching per cycle and `f` the clock frequency. Voltage enters squared, which is why lowering voltage is the strongest lever on energy.

2. **Heat removal, not transistor count, is the binding limit on performance.** A chip turns nearly all its input power into heat. Air and liquid cooling can extract on the order of 100 W/cm² from a die in practice. Once a chip hits that ceiling, more transistors switching faster would melt it, so designers must leave parts of the chip idle ("dark silicon") or slow them down. Mobile devices face a much lower budget of a few watts.

3. **Thermal energy `kT` sets the scale of noise and of transistor turn-off.** At room temperature `kT ≈ 0.026 eV`, or `kT/q ≈ 26 mV`. Carriers in a transistor below threshold follow a Boltzmann distribution, so current can drop at most tenfold per `(kT/q) ln 10 ≈ 60 mV` of gate voltage. To get a good on/off ratio the threshold voltage cannot fall much below a few hundred millivolts, so supply voltage stalled near 1 V around 2005. With voltage stuck, `CV²f` could no longer fall as transistors shrank, ending Dennard scaling and the era of ever-rising clock frequency.

4. **Logically irreversible operations have an unavoidable heat cost.** Landauer (1961) showed that erasing a bit, merging two possible states into one, reduces the information-bearing entropy of the computer, and the Second Law requires that entropy to go into the environment as heat of at least `kT ln 2`: about 2.9 × 10⁻²¹ J at 300 K. Experiments in 2012 confirmed the bound. A typical CMOS logic operation dissipates on the order of femtojoules (10⁻¹⁵ J) including wires, roughly a million times more.

5. **Reversible computing could in principle avoid the Landauer cost.** Bennett (1973) showed that any computation can be done with logically reversible steps that never erase information, so there is no thermodynamic minimum on computation itself, only on erasure. Doing this cheaply requires running slowly and adiabatically and keeping garbage bits, so it remains largely a research topic. It shows which costs are fundamental and which are artefacts of current design.

6. **Heat degrades reliability and increases leakage.** Leakage current rises roughly exponentially with temperature because carrier populations follow `exp(-E/kT)`. Higher leakage means more heat, which can feed back into thermal runaway. Many wear-out mechanisms, such as electromigration in wires, accelerate exponentially with temperature (Arrhenius behaviour), so hot chips also die sooner.

7. **Information entropy and thermodynamic entropy share a formula for a reason.** Shannon's entropy `H = -Σ p log p` has the same form as Gibbs' statistical entropy. Landauer's principle is the bridge: physical systems that store information must pay in thermodynamic entropy to forget it. This connection resolved the paradox of Maxwell's demon, which must eventually erase its memory.

## Key concepts

| Term | Meaning |
|---|---|
| `kT` | Thermal energy per degree of freedom; about 26 meV at 300 K. |
| Dynamic power | `αCV²f`, from charging and discharging capacitance. |
| Static (leakage) power | Power drawn by transistors that are nominally off. |
| Landauer limit | Minimum heat `kT ln 2` per bit erased. |
| Reversible computing | Computing without erasing information, avoiding the Landauer cost. |
| Subthreshold slope | Gate-voltage change per tenfold current change below threshold; at least about 60 mV at room temperature. |
| Thermal Design Power (TDP) | The sustained power a cooling system is designed to remove. |
| Dark silicon | Transistors that must stay unpowered or slowed to fit the power budget. |
| Arrhenius behaviour | Rates that scale as `exp(-Ea/kT)`, such as many failure mechanisms. |

## How it fits

- **Below:** It uses [electromagnetism](electromagnetism-and-charge.md) (energy of charge on a capacitor) and statistical reasoning from [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md).
- **Above:** `αCV²f` drives [timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md) in hardware design and explains [power and the end of scaling](../../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md), which in turn forced the move to [multicore](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md) and [accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md). Landauer links physics to [entropy and information](../../02-theory-of-computation/01-information-theory/entropy-and-information.md). Energy cost also dominates [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md) and data-centre design in [cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md).
- **Siblings:** [Electromagnetism](electromagnetism-and-charge.md) says where energy is stored; this leaf says where it goes. [Quantum mechanics](quantum-mechanics-and-band-theory.md) and this leaf together explain why carrier counts depend exponentially on temperature.

## Common misconceptions

- **"Computation fundamentally requires energy."** Only erasure does; reversible computation has no thermodynamic floor. Practical hardware is far above even the erasure floor.
- **"Switching faster with a lower-resistance transistor saves energy."** The `CV²` charging cost is independent of resistance; faster switching changes power (energy per second), not energy per operation.
- **"Clock speeds stopped rising because transistors stopped getting faster."** They stopped because voltage could not keep falling, so power density would have become unmanageable.

## Go deeper

- Rolf Landauer, "Irreversibility and Heat Generation in the Computing Process" (1961): the original argument for the erasure bound.
- Charles Bennett, "The Thermodynamics of Computation: A Review" (1982): reversible computation and Maxwell's demon.
- Richard Feynman, *Feynman Lectures on Computation* (1996): the physics of computing, including energy limits, from first principles.
