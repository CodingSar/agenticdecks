# Feedback and Control

> **Layer:** [00 Engineering Foundations](../README.md) › [Signals and Systems](README.md)
> **Builds on:** [Calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md), [Circuit Laws](../02-electrical-circuits/circuit-laws.md)
> **Enables:** [Latches and Flip-Flops](../../03-digital-logic/03-sequential-logic/latches-and-flip-flops.md), [Congestion Control](../../08-networking/04-transport-layer/congestion-control.md), [Scalability Patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md), [Learning as Optimization](../../13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md)

## Essence

Feedback means measuring a system's output and using it to adjust the input. Negative feedback opposes deviations: it makes a system precise and robust even when its parts are imprecise, at the cost of raw gain and with a risk of oscillation if the loop reacts too late. Positive feedback reinforces deviations: it drives a system to one of two extremes, which is exactly what is needed to store a bit or make a clean decision. Computing uses both everywhere, from the cross-coupled inverters in every memory cell to clock generators, voltage regulators, Transmission Control Protocol (TCP) congestion control, autoscaling and the training loops of machine learning.

## Core tenets

1. **Negative feedback trades gain for precision.** An amplifier with large but unreliable gain `A`, whose output is fed back through a stable network `β`, has closed-loop gain `A / (1 + Aβ)`. When `Aβ` is large this is almost exactly `1/β`, independent of `A`. Harold Black's feedback amplifier (published 1934) used this to build precise telephone repeaters from imprecise vacuum tubes. The principle is general: a loop can be as accurate as its sensor even if its actuator is sloppy.

2. **Feedback suppresses disturbances and widens bandwidth by the same factor.** Errors injected inside a loop are reduced by roughly `1 + Aβ`, the loop gain. The same factor that shrinks gain also extends the range of frequencies the system handles faithfully. Feedback does not create performance; it redistributes it from gain into accuracy, speed and robustness.

3. **Delay in the loop causes oscillation.** A loop that reacts late can push in the right direction at the wrong time, so its correction adds to the error instead of cancelling it. If the loop gain is still at least 1 when accumulated delay reaches half a cycle (180° phase shift), the system oscillates. Nyquist's 1932 criterion and Bode's phase and gain margins quantify how much delay a loop can tolerate. The practical rule: the more delay, the gentler the corrections must be.

4. **Positive feedback creates bistability, which is memory.** Two inverters in a ring push each other to opposite rails: any small deviation from the midpoint grows until the circuit saturates. The result has two stable states and one unstable balance point. This is the latch, the flip-flop and the Static Random-Access Memory (SRAM) cell. The unstable balance point is also why metastability exists: a latch caught exactly at the midpoint takes time to fall off it.

5. **Oscillators are feedback loops designed to be unstable.** A ring of an odd number of inverters can never settle and oscillates at a rate set by gate delay. Crystal oscillators use a resonator to fix frequency precisely. A Phase-Locked Loop (PLL) adds negative feedback, comparing a generated clock against a reference and adjusting it until they align; PLLs generate the gigahertz clocks of processors from a slow crystal.

6. **Proportional, integral and derivative terms address different errors.** A Proportional-Integral-Derivative (PID) controller adds three corrections: one proportional to current error (fast response), one to accumulated error (removes steady offset), and one to its rate of change (damps overshoot). It is the workhorse of industrial control, and its logic shows up in software controllers that adjust thread pools, rate limits and caches.

7. **The same loop structure governs computer systems.** Voltage regulators hold supply steady as load changes; Dynamic Voltage and Frequency Scaling (DVFS) and thermal throttling adjust clock speed from measured temperature and load. TCP congestion control raises its sending rate until it detects loss, then backs off. Autoscalers add servers when latency rises. Gradient descent is a feedback loop on a loss function. Each inherits the classic risks: too much gain or too much delay makes it oscillate.

## Key concepts

| Term | Meaning |
|---|---|
| Negative feedback | Feedback that opposes deviation from a set point. |
| Positive feedback | Feedback that reinforces deviation, driving toward an extreme. |
| Loop gain | Total gain around the feedback loop, `Aβ`. |
| Set point | The target value a controller tries to maintain. |
| Stability | Whether disturbances die out rather than grow or oscillate. |
| Phase margin | How far the loop's phase is from 180° when loop gain is 1. |
| Bistability | Having two stable states. |
| Phase-Locked Loop (PLL) | Feedback circuit that locks a generated clock to a reference. |
| PID controller | Controller combining proportional, integral and derivative corrections. |

## How it fits

- **Below:** Loops are analysed with differential equations from [calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md) and built from circuits obeying [circuit laws](../02-electrical-circuits/circuit-laws.md).
- **Above:** Positive feedback gives [latches and flip-flops](../../03-digital-logic/03-sequential-logic/latches-and-flip-flops.md); PLLs feed [clocking and synchronous design](../../03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md); DVFS appears in [timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md). Negative feedback governs [congestion control](../../08-networking/04-transport-layer/congestion-control.md), autoscaling in [scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md), and training in [learning as optimization](../../13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md) and [reinforcement learning](../../13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md).
- **Siblings:** [Analog vs digital](analog-vs-digital.md) relies on the gain and positive feedback described here for restoration and storage. [Sampling and quantization](sampling-and-quantization.md) supplies the measurements digital controllers act on.

## Common misconceptions

- **"More gain always means tighter control."** Beyond a point, more gain with the same loop delay causes overshoot and oscillation.
- **"Feedback is an analog topic."** Feedback is a structure, not a technology; it governs network protocols, schedulers and learning algorithms as much as amplifiers.
- **"Positive feedback is bad."** It is how every bit of static memory is held and every clean decision is made.

## Go deeper

- Karl Åström and Richard Murray, *Feedback Systems: An Introduction for Scientists and Engineers* (2008): modern, readable control theory with computing examples.
- Harold Black, "Stabilized Feedback Amplifiers" (1934): the paper that introduced negative feedback in electronics.
- Norbert Wiener, *Cybernetics* (1948): feedback as a unifying idea across machines and organisms.
