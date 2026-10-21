# Measurement and Modeling

> **Layer:** [00 Engineering Foundations](../README.md) › [Engineering Method](README.md)
> **Builds on:** [Statistical Inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md), [Calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md)
> **Enables:** [The Performance Equation](../../04-computer-architecture/06-performance/the-performance-equation.md), [Latency, Bandwidth and Queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md), [Observability](../../12-software-engineering/04-operations/observability.md), [Evaluation and Experimentation](../../13-artificial-intelligence/02-machine-learning-foundations/evaluation-and-experimentation.md)

## Essence

Engineers do not reason about reality directly; they reason about models of it, and they check those models by measurement. A model is a deliberate simplification: an ideal switch for a transistor, a lumped resistor for a wire, a queue for a server. It is useful within a range of conditions and misleading outside it. Measurement keeps models honest, but measurement has its own errors, noise and biases, and the act of measuring can change the system. Good engineering alternates between the two: estimate with a simple model, measure, find where the model breaks, refine. Computer science inherits this loop wholesale, in performance analysis, capacity planning, benchmarking, debugging and the evaluation of learning systems.

## Core tenets

1. **Every model has a domain of validity.** The lumped circuit model holds while wires are short compared with signal wavelength; the square-law transistor model holds for long channels; the Random Access Machine (RAM) model of algorithms holds while data fits in fast memory. Using a model outside its domain gives confident, wrong answers. A good engineer knows a model's assumptions as well as its equations. As George Box put it, all models are wrong, but some are useful.

2. **Estimate before you build or measure.** Back-of-the-envelope calculation, with orders of magnitude and known reference numbers, catches impossible designs early and tells you what a measurement *should* show. Knowing that a main-memory access takes on the order of 100 ns, a level-1 (L1) cache hit about 1 ns, a round trip within a data centre roughly 0.1 to 0.5 ms and a cross-continent round trip tens of milliseconds (2020s hardware) is enough to rule out many designs in minutes.

3. **Units and dimensions check reasoning.** Every equation must balance in units: seconds equal resistance times capacitance (ohms × farads), bandwidth times delay equals bits in flight. Dimensional analysis catches algebra mistakes and often suggests the form of an answer before you derive it.

4. **Measure, do not guess, where time and resources go.** Intuition about bottlenecks is notoriously poor; profiles routinely show time spent somewhere unexpected. Optimising without measurement wastes effort on parts that do not matter. Measure the whole system under realistic load, find the dominant cost, and only then optimise.

5. **Every measurement has error, and variation is information.** Repeated measurements of the same thing differ because of noise, background activity and nondeterminism. Report central tendency *and* spread, use enough repetitions to estimate a confidence interval, and watch for skewed distributions where the mean hides a long tail. For latency-sensitive systems, the 99th percentile often matters more than the average.

6. **Measurement perturbs the system.** Instrumentation costs time, adds memory traffic and changes caching and timing; a probe on a circuit adds capacitance. Heavy tracing can make a race condition disappear. Choose measurement methods whose overhead is small relative to the effect being measured, and know what they disturb.

7. **Simple analytic laws carry surprising weight.** Little's law, `L = λW` (items in a system equal arrival rate times time in system), holds for any stable system regardless of distributions. Utilisation laws show that queueing delay grows sharply as utilisation approaches 100%. The Simulation Program with Integrated Circuit Emphasis (SPICE), first released in 1973, made circuit simulation the norm; simulation fills in where analysis is too hard, but it is only as good as its model inputs.

8. **Benchmarks become targets, and then stop measuring.** A benchmark is a model of a workload. Once designers optimise for it specifically, its scores improve faster than real performance (Goodhart's law). Use several benchmarks representative of the real workload, report how results were obtained, and distrust single-number summaries.

## Key concepts

| Term | Meaning |
|---|---|
| Model | A simplified description that predicts behaviour within a domain of validity. |
| Domain of validity | Conditions under which a model's assumptions hold. |
| Order-of-magnitude estimate | A calculation accurate to within a factor of about ten. |
| Dimensional analysis | Checking and deriving relations by balancing units. |
| Confidence interval | A range likely to contain the true value, given measurement variation. |
| Tail latency | High-percentile latency, such as the 99th percentile. |
| Little's law | `L = λW` for any stable system. |
| Benchmark | A standardised workload used to compare systems. |
| Observer effect | Change in a system caused by measuring it. |

## How it fits

- **Below:** Error bars and confidence come from [statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md); continuous models use [calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md).
- **Above:** [The performance equation](../../04-computer-architecture/06-performance/the-performance-equation.md) and [Amdahl's law](../../04-computer-architecture/06-performance/amdahls-law.md) are models in this sense. Queueing laws drive [latency, bandwidth and queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md). The [models of computation](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md) behind algorithm analysis are models with domains of validity. Measurement practice becomes [observability](../../12-software-engineering/04-operations/observability.md) and [debugging](../../12-software-engineering/03-quality/debugging.md) in software, and [evaluation and experimentation](../../13-artificial-intelligence/02-machine-learning-foundations/evaluation-and-experimentation.md) in machine learning.
- **Siblings:** Models are how you locate designs on the frontier described in [tradeoffs and constraints](tradeoffs-and-constraints.md); measured failure rates feed [reliability and redundancy](reliability-and-redundancy.md).

## Common misconceptions

- **"A more detailed model is always better."** Detail costs understanding and computation; the right model is the simplest one that answers the question within its validity range.
- **"The average tells you how the system performs."** Averages hide variance and tails, which often determine user experience and failure.
- **"A benchmark win means a faster system."** It means a faster system *on that benchmark*; whether it transfers depends on how representative the benchmark is.

## Go deeper

- Raj Jain, *The Art of Computer Systems Performance Analysis* (1991): measurement, simulation and queueing for computer systems.
- Jon Bentley, *Programming Pearls* (1986): back-of-the-envelope estimation for programmers.
- George Box, "Science and Statistics" (1976): the argument that all models are wrong, and the case for iterative modelling (the "but some are useful" wording appears in his 1979 work on robustness).
