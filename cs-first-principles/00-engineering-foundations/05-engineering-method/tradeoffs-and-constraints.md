# Tradeoffs and Constraints

> **Layer:** [00 Engineering Foundations](../README.md) › [Engineering Method](README.md)
> **Builds on:** [Optimization](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md), [Thermodynamics and Energy](../01-physics-of-computation/thermodynamics-and-energy.md)
> **Enables:** [Timing and Power](../../03-digital-logic/04-hardware-design/timing-and-power.md), [The Performance Equation](../../04-computer-architecture/06-performance/the-performance-equation.md), [Software Architecture](../../12-software-engineering/01-design/software-architecture.md), [Essential and Accidental Complexity](../../12-software-engineering/01-design/essential-and-accidental-complexity.md)

## Essence

Engineering is the art of choosing well when you cannot have everything. Every design lives inside constraints, some set by physics (the speed of light, heat removal, noise), some by economics (cost, schedule, volume) and some by people (skills, maintainability, regulations). Within those walls, improving one property almost always worsens another: speed against power, capacity against latency, generality against efficiency. The engineer's job is to make these tradeoffs explicit, quantify them, find the frontier of designs where no property can improve without another getting worse, and pick a point on it that fits the purpose. This habit of mind, more than any formula, is what layer 00 hands to every layer above.

## Core tenets

1. **Constraints come first, and they define the problem.** A design that ignores a binding constraint is not a cheaper design; it is not a design. Constraints are of two kinds: hard ones that cannot be violated (power ceiling, deadline, physical law) and soft ones that can be traded at a price (cost, area). Identifying which constraint actually binds, the bottleneck, focuses effort where it pays.

2. **Good designs lie on the Pareto frontier.** A design is Pareto-optimal if no other design is better in one objective without being worse in another. Designs off the frontier waste something for nothing and should be discarded. The frontier itself does not say which design to choose; that depends on the weighting of objectives, which is a decision about purpose rather than technique.

3. **Many tradeoffs come from conservation, so cost can be moved but not removed.** A cache does not eliminate memory latency; it moves cost into area, power and complexity, and into the miss cases. Pipelining raises throughput but adds latency per item and register overhead. Error correction buys reliability with redundant bits. When something seems free, look for where the cost went.

4. **Combine objectives into figures of merit, carefully.** Engineers fold competing goals into a single metric to compare designs: energy-delay product for circuits, performance per watt for processors, cost per transaction for systems. The choice of metric bakes in a weighting, and optimising the wrong one can produce designs that win the metric and lose the market. Make the weighting explicit.

5. **Returns diminish, so stop at the knee.** Most improvements follow a curve: the first effort pays well, later effort pays less. Doubling a cache's size cuts its miss rate by much less than half; adding cores helps only as far as the parallel fraction allows. Locating the knee of the curve, where marginal benefit falls below marginal cost, is usually the right stopping point.

6. **Optimising for the common case usually wins.** Make frequent operations fast and rare ones merely correct. This is how Reduced Instruction Set Computer (RISC) design, caching, branch prediction and fast paths in software all work. It fails when the "rare" case is adversarial (an attacker can trigger it) or when its cost is catastrophic, so the tail must still be bounded.

7. **Generality costs efficiency, and specialisation costs flexibility.** A general-purpose processor can run anything but spends most of its energy on overhead such as instruction fetch and scheduling rather than arithmetic. A fixed-function circuit can be orders of magnitude more efficient but does one thing. Field-programmable hardware, accelerators and domain-specific languages are points on this spectrum.

8. **Real design is satisficing under uncertainty.** Herbert Simon observed that designers rarely find the optimum; they search until they find a design that is good enough on every constraint. Requirements shift, models are approximate, and time is a constraint too. Leaving margin, keeping options open, and choosing designs that are easy to change are themselves tradeoffs worth making.

## Key concepts

| Term | Meaning |
|---|---|
| Constraint | A limit a design must respect, hard or soft. |
| Objective | A quantity to improve, such as speed, cost or energy. |
| Pareto frontier | Set of designs where no objective can improve without another worsening. |
| Bottleneck | The constraint or component that currently limits the whole. |
| Figure of merit | A single metric combining several objectives, such as energy-delay product. |
| Diminishing returns | Each extra unit of effort yields less improvement. |
| Common case | The situation that occurs most often and so deserves most optimisation. |
| Satisficing | Choosing the first design that meets all constraints well enough. |

## How it fits

- **Below:** The Pareto frontier and constrained optima come from [optimization](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md). Physical limits such as heat from [thermodynamics](../01-physics-of-computation/thermodynamics-and-energy.md) are the hardest constraints.
- **Above:** Speed versus power in [timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md); instruction count versus cycle time in [the performance equation](../../04-computer-architecture/06-performance/the-performance-equation.md); [Amdahl's law](../../04-computer-architecture/06-performance/amdahls-law.md) as diminishing returns; time versus space in [algorithms](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md); consistency versus availability in [impossibility results](../../10-distributed-and-parallel-computing/02-distributed-foundations/impossibility-results.md); and design decisions in [software architecture](../../12-software-engineering/01-design/software-architecture.md). The index of these appears under [tradeoffs](../../CROSS-CUTTING.md#tradeoffs).
- **Siblings:** [Reliability and redundancy](reliability-and-redundancy.md) is one specific tradeoff (cost for dependability); [measurement and modeling](measurement-and-modeling.md) is how you find out where on the frontier you actually are.

## Common misconceptions

- **"There is a best design."** There is a best design *for a given weighting of objectives and constraints*; change the purpose and the best design changes.
- **"Optimise everything."** Optimising a component that is not the bottleneck costs effort and complexity for no gain.
- **"Tradeoffs are a sign of a weak design."** Every real design embodies tradeoffs; weak designs are those that make them implicitly or by accident.

## Go deeper

- Herbert Simon, *The Sciences of the Artificial* (1969): design as search under bounded rationality, and satisficing.
- Butler Lampson, "Hints for Computer System Design" (1983): hard-won rules of thumb for systems tradeoffs.
- John Hennessy and David Patterson, *Computer Architecture: A Quantitative Approach* (1990): tradeoffs made quantitative, with the common-case principle at its core.
- Henry Petroski, *To Engineer Is Human: The Role of Failure in Successful Design* (1985): how engineering judgement is formed by tradeoffs and failures.
