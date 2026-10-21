# Analog vs Digital

> **Layer:** [00 Engineering Foundations](../README.md) › [Signals and Systems](README.md)
> **Builds on:** [Noise and Signal Integrity](../02-electrical-circuits/noise-and-signal-integrity.md), [CMOS](../03-semiconductor-devices/cmos.md)
> **Enables:** [Logic Gates](../../03-digital-logic/02-combinational-logic/logic-gates.md), [Binary and Positional Notation](../../03-digital-logic/01-number-representation/binary-and-positional-notation.md), [Entropy and Information](../../02-theory-of-computation/01-information-theory/entropy-and-information.md)

## Essence

The physical world is analog: voltages, positions and sound pressures take continuous values and change continuously in time. A digital system deliberately ignores most of that continuum. It agrees to read a voltage only as "low" or "high", and usually only at clock ticks, and builds every component so that its outputs land firmly inside those bands. The price is waste: many transistors and much energy represent what one analog wire could carry. The prize is that errors no longer accumulate. Each stage restores its signal, so a computation can be billions of steps long, copied perfectly, stored indefinitely and checked by codes. This trade, giving up precision per wire to gain reliability per system, is the foundational bargain of computing.

## Core tenets

1. **Digital means agreeing to see only a few distinguishable states.** A digital signal maps a continuous quantity onto a finite set of symbols, usually two, by assigning ranges of value to each and forbidding the ranges in between. Two levels are the most robust choice: with a fixed voltage swing, two states give the largest possible separation for a given noise budget, and a simple transistor switch produces them naturally.

2. **The static discipline is the contract that makes the abstraction hold.** Every digital component promises: if its inputs are valid logic levels, its outputs will be valid logic levels with margin to spare (`VOH > VIH` and `VOL < VIL`). If every component honours this, a designer can reason about circuits purely in terms of 0s and 1s, never voltages. It is an interface in the software sense, and everything above layer 00 is built on it.

3. **Restoration is what defeats noise accumulation.** In an analog chain, each stage adds noise to the signal and passes the sum on, so error grows with the number of stages. A digital gate with gain above 1 in its switching region regenerates a full-strength output from a degraded input, discarding the noise. Errors therefore do not accumulate; a signal is either read correctly or, if noise exceeds the margin, read wrong outright.

4. **Precision costs scale very differently.** Adding one bit of digital precision costs roughly a constant number of extra devices (linear in bits). Halving the noise of an analog signal to gain one bit of effective precision typically costs about four times the power, because thermal noise power falls only in proportion to the energy spent. For low precision, analog is cheaper per operation; for high precision or long computations, digital wins decisively.

5. **Exact copying makes stored programs and software possible.** A digital value can be duplicated, transmitted and stored without degradation, because each copy is restored to an exact symbol. This is what lets a program be data, lets a disk image be identical on a million machines, and lets error-correcting codes detect and fix the rare mistakes. Analog recordings, by contrast, lose quality with every copy.

6. **The boundary between analog and digital is never clean.** Sensors, radios, displays and every wire are analog, so systems need converters (sampling and quantisation) at their edges. Even inside, a digital signal sampled while it is changing can settle into an undefined level for an unbounded time: metastability. Clocking disciplines and synchronisers exist to keep this rare, not to eliminate it.

7. **Analog computing returns where precision is cheap to give up.** Neural network inference tolerates low precision, and moving data costs more energy than computing on it, so analog in-memory computing and low-bit digital formats are active research areas. They revisit the same trade with different numbers.

## Key concepts

| Term | Meaning |
|---|---|
| Analog signal | A quantity carrying information in its continuous value. |
| Digital signal | A quantity interpreted as one of a finite set of symbols. |
| Logic level | A voltage range assigned to a symbol, such as 0 or 1. |
| Forbidden zone | Voltages between valid levels, which outputs must not produce. |
| Static discipline | Valid inputs guarantee valid outputs with margin. |
| Restoration (regeneration) | A stage's ability to output clean levels from degraded inputs. |
| Gain | Ratio of output change to input change. |
| Metastability | An unresolved state between levels, possible whenever a continuous signal is forced into a discrete choice. |

## How it fits

- **Below:** The static discipline relies on the noise margins of [noise and signal integrity](../02-electrical-circuits/noise-and-signal-integrity.md) and on the high-gain inverter of [Complementary Metal-Oxide-Semiconductor (CMOS)](../03-semiconductor-devices/cmos.md).
- **Above:** It is the reason [logic gates](../../03-digital-logic/02-combinational-logic/logic-gates.md) can be described by truth tables and [binary notation](../../03-digital-logic/01-number-representation/binary-and-positional-notation.md) can represent numbers. Metastability resurfaces in [latches and flip-flops](../../03-digital-logic/03-sequential-logic/latches-and-flip-flops.md). Discrete symbols are what [information theory](../../02-theory-of-computation/01-information-theory/entropy-and-information.md) counts, and low-precision arithmetic reappears in [domain-specific accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md).
- **Siblings:** [Sampling and quantization](sampling-and-quantization.md) is how analog signals cross into the digital domain. [Feedback and control](feedback-and-control.md) explains the gain and positive feedback that make restoration and memory work.

## Common misconceptions

- **"Digital is more accurate than analog."** Digital is *reproducible*; its accuracy is whatever number of bits you pay for. A good analog circuit can beat a low-bit digital one.
- **"Inside a computer, signals really are 0 and 1."** They are continuous voltages that the design keeps away from the forbidden zone at sampling times; the 0s and 1s are an abstraction.
- **"Digital systems degrade gracefully."** They tend to fail abruptly when noise crosses the margin, which is why margins and error correction matter.

## Go deeper

- Stephen Ward and Robert Halstead, *Computation Structures* (1990): introduces the static discipline and digital abstraction from first principles.
- Anant Agarwal and Jeffrey Lang, *Foundations of Analog and Digital Electronic Circuits* (2005): builds the digital abstraction on circuits explicitly.
- Rahul Sarpeshkar, "Analog Versus Digital: Extrapolating from Electronics to Neurobiology" (1998): quantitative comparison of the costs of each.
